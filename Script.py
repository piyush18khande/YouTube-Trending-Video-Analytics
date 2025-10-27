
import requests
import mysql.connector
from datetime import datetime

# ---------------- CONFIG ----------------
API_KEY = "AIzaSyCw4nwXrpD3QNoEBNe2ptRSgOrZjk2XlzE"   # replace with your YouTube API key
CHANNEL_ID = "UC_x5XG1OV2P6uZZ5FSM9Ttw"  # Example: Google Developers channel

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "RolexDaytona27",
    "database": "youtube_db"
}

# ---------------- DB CONNECTION ----------------
conn = mysql.connector.connect(**DB_CONFIG)
cursor = conn.cursor()

# ---------------- UTILS ----------------
def format_datetime(dt_str):
    """Convert YouTube datetime format to MySQL DATETIME"""
    try:
        return datetime.strptime(dt_str, "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d %H:%M:%S")
    except Exception:
        return None

# ---------------- API CALLS ----------------
def get_channel_details(channel_id):
    url = f"https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id={channel_id}&key={API_KEY}"
    res = requests.get(url).json()

    for item in res.get("items", []):
        channel_id = item["id"]
        title = item["snippet"]["title"]
        desc = item["snippet"]["description"]
        subs = item["statistics"]["subscriberCount"]
        views = item["statistics"]["viewCount"]
        videos = item["statistics"]["videoCount"]

        cursor.execute("""
            INSERT INTO channels (channel_id, title, description, subscribers, views, video_count)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE 
                title=VALUES(title),
                description=VALUES(description),
                subscribers=VALUES(subscribers),
                views=VALUES(views),
                video_count=VALUES(video_count)
        """, (channel_id, title, desc, subs, views, videos))
        conn.commit()
        print(f"✅ Channel inserted: {title}")

def get_videos(channel_id):
    url = f"https://www.googleapis.com/youtube/v3/search?key={API_KEY}&channelId={channel_id}&part=snippet,id&order=date&maxResults=5"
    res = requests.get(url).json()

    video_ids = []
    for item in res.get("items", []):
        if item["id"]["kind"] == "youtube#video":
            video_ids.append(item["id"]["videoId"])

    details_url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet,contentDetails,statistics&id={','.join(video_ids)}&key={API_KEY}"
    details = requests.get(details_url).json()

    for item in details.get("items", []):
        video_id = item["id"]
        channel_id = item["snippet"]["channelId"]
        title = item["snippet"]["title"]
        published_at = format_datetime(item["snippet"]["publishedAt"])
        duration = item["contentDetails"]["duration"]
        views = item["statistics"].get("viewCount", 0)
        likes = item["statistics"].get("likeCount", 0)
        comments_count = item["statistics"].get("commentCount", 0)

        cursor.execute("""
            INSERT INTO videos (video_id, channel_id, title, published_at, duration, views, likes, comments_count)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE 
                title=VALUES(title),
                published_at=VALUES(published_at),
                duration=VALUES(duration),
                views=VALUES(views),
                likes=VALUES(likes),
                comments_count=VALUES(comments_count)
        """, (video_id, channel_id, title, published_at, duration, views, likes, comments_count))
        conn.commit()
        print(f"📹 Video inserted: {title}")
        get_comments(video_id)

def get_comments(video_id):
    url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={video_id}&key={API_KEY}&maxResults=5"
    res = requests.get(url).json()

    for item in res.get("items", []):
        c = item["snippet"]["topLevelComment"]["snippet"]
        comment_id = item["id"]
        author = c["authorDisplayName"]
        text = c["textDisplay"]
        published_at = format_datetime(c["publishedAt"])
        like_count = c["likeCount"]

        cursor.execute("""
            INSERT INTO comments (comment_id, video_id, author, comment_text, published_at, like_count)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE 
                comment_text=VALUES(comment_text),
                published_at=VALUES(published_at),
                like_count=VALUES(like_count)
        """, (comment_id, video_id, author, text, published_at, like_count))
        conn.commit()
        print(f"💬 Comment inserted by {author}")

# ---------------- MAIN ----------------
if __name__ == "__main__":
    get_channel_details(CHANNEL_ID)
    get_videos(CHANNEL_ID)

    cursor.close()
    conn.close()
