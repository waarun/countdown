import os
from datetime import datetime
import tweepy

# Load keys from environment (GitHub Actions secrets)
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_secret = os.getenv("ACCESS_SECRET")
bearer_token = os.getenv("BEARER_TOKEN")  # <- add this in GitHub Secrets

# Create Tweepy client (v2)
client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_secret,
    bearer_token=bearer_token
)

# Target date for countdown
event_date = datetime(2025, 12, 31)
days_left = (event_date - datetime.now()).days

# Tweet content
tweet = f"⏳ Countdown: {days_left} days until New Year 2026! 🎉"

# Post tweet
client.create_tweet(text=tweet)

print("Tweet posted:", tweet)
