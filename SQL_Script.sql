CREATE DATABASE IF NOT EXISTS youtube_db;
USE youtube_db;

-- Channels Table
CREATE TABLE IF NOT EXISTS channels (
    channel_id VARCHAR(50) PRIMARY KEY,
    title VARCHAR(255),
    description TEXT,
    subscribers BIGINT,
    views BIGINT,
    video_count INT
);


-- Videos Table
CREATE TABLE IF NOT EXISTS videos (
    video_id VARCHAR(50) PRIMARY KEY,
    channel_id VARCHAR(50),
    title VARCHAR(255),
    published_at DATETIME,
    duration VARCHAR(50),
    views BIGINT,
    likes BIGINT,
    comments_count BIGINT,
    FOREIGN KEY (channel_id) REFERENCES channels(channel_id)
);


-- Comments Table
CREATE TABLE IF NOT EXISTS comments (
    comment_id VARCHAR(100) PRIMARY KEY,
    video_id VARCHAR(50),
    author VARCHAR(255),
    comment_text TEXT,
    published_at DATETIME,
    like_count INT,
    FOREIGN KEY (video_id) REFERENCES videos(video_id)
);


-- Engagement Analysis
-- Top 10 videos by views
SELECT video_id, title, views
FROM videos
ORDER BY views DESC
LIMIT 10;



-- Like to view ratio (engagement rate)
SELECT 
    video_id,
    title,
    ROUND((likes / views) * 100, 2) AS Likes_View_Ratio
FROM videos
ORDER BY Likes_View_Ratio DESC;



-- Average comments per video per channel
select count(*) as avg_comments,video_id
from comments s
Join comments s on v.comment_id = s.comment_id
join channels c on v.channel_id = c.channel_id
group by avg_comments
order by avg_comments;

-- Best Posting Times
-- Extract best posting day
SELECT DAYNAME(published_at) AS day_of_week,
       COUNT(*) AS total_videos,
       SUM(views) AS total_views
FROM videos
GROUP BY day_of_week
ORDER BY total_views DESC;

-- Extract best posting hour (24h format)
SELECT Hour(published_at) AS hour_of_the_day,
       COUNT(*) AS total_videos,
       SUM(views) AS total_views
FROM videos
GROUP BY hour_of_the_day
ORDER BY total_views DESC;



-- Subscriber growth per channel
SELECT title, subscribers, views, video_count
FROM channels
ORDER BY subscribers DESC;



-- Recent trending videos (last 30 days, by views)
-- Top 10 recent trending videos (last 30 days, by views)
SELECT 
    video_id, 
    title, 
    published_at, 
    views
FROM videos 
WHERE published_at >= DATE_SUB(CURRENT_DATE, INTERVAL 30 DAY)
ORDER BY views DESC
LIMIT 10;


-- Sentiment



-- Comment count per channel (approx. engagement)
SELECT c.title AS channel_name,
       COUNT(s.comment_id) AS total_comments
FROM comments s
JOIN videos v ON s.video_id = v.video_id
JOIN channels c ON v.channel_id = c.channel_id
GROUP BY c.channel_id, c.title
ORDER BY total_comments DESC;



Select views ,title , subscribers,views,count(*) as Growth_per_day
from channels
group by subscribers,title, views
order by Growth_per_day;
