import os
import tweepy
from datetime import datetime

# Load keys from environment (GitHub Actions secrets)
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_secret = os.getenv("ACCESS_SECRET")

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_secret)
api = tweepy.API(auth)

# Target date (set your own event here)
event_date = datetime(2025, 12, 31)
days_left = (event_date - datetime.now()).days

tweet = f"⏳ Countdown: {days_left} days until New Year 2026! 🎉"
api.update_status(tweet)

print("Tweet posted:", tweet)
