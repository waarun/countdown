import os
from datetime import datetime
import tweepy

# Load secrets from environment
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_secret = os.getenv("ACCESS_SECRET")
bearer_token = os.getenv("BEARER_TOKEN")  # <- add this in GitHub Secrets too

# Create Tweepy Client for Twitter API v2
client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_secret,
    bearer_token=bearer_token
)

# Target date
event_date = datetime(2025, 12, 31)
days_left = (event_date - datetime.now()).days

tweet = f"⏳ Countdown: {days_left} days until New Year 2026! 🎉"
client.create_tweet(text=tweet)

print("Tweet posted:", tweet)
