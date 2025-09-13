import os
import tweepy
from datetime import datetime

# Load keys from environment (GitHub Actions secrets)
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_secret = os.getenv("ACCESS_SECRET")
bearer_token = os.getenv("BEARER_TOKEN")

# Create Tweepy client (v2)
client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_secret,
    bearer_token=bearer_token
)

# Target date for the movie release
release_date = datetime(2025, 9, 25)

# Calculate days left
days_left = (release_date - datetime.now()).days

# If the movie is not yet released
if days_left > 0:
    tweet_text = f"⏳ {days_left} days left until #OG hits the screens! 🔥"
    gif_url = "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExa2pucDJvNzh3cDFoeGZwbG1pb2R1bmw4Z20wcDlsNHNqdDE1MWZ5cCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/WVCz7hhi1gRHUfr5Wf/giphy.gif"
    
    # Tweet with GIF URL directly in text (simplest approach)
    client.create_tweet(text=f"{tweet_text} {gif_url}")
    print("Tweet posted:", tweet_text)
else:
    print("The movie is already released or today is the release date!")
