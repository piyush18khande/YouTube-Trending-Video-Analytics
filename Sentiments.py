import pandas as pd
from textblob import TextBlob

# Load your comments CSV (replace with your file path)
dataset = pd.read_csv("comments.csv")   # <-- Add this line

# Function for sentiment classification
def get_sentiment(text):
    if pd.isna(text):
        return "Neutral"
    polarity = TextBlob(str(text)).sentiment.polarity
    if polarity > 0.1:
        return "Positive"
    elif polarity < -0.1:
        return "Negative"
    else:
        return "Neutral"

# Apply on comment_text column
dataset["sentiment"] = dataset["comment_text"].apply(get_sentiment)

# Save output
dataset.to_csv("comments_with_sentiment.csv", index=False)
print("Sentiment column created successfully!")
