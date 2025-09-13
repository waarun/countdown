import os
import tweepy
from datetime import datetime
import requests

# ================================
# Load Twitter API keys from GitHub Secrets
# ================================
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_secret = os.getenv("ACCESS_SECRET")
bearer_token = os.getenv("BEARER_TOKEN")

# ================================
# Initialize Tweepy client (v2)
# ================================
client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_secret,
    bearer_token=bearer_token
)

# ================================
# Countdown Configuration
# ================================
release_date = datetime(2025, 9, 25)  # Movie release date
gif_url = "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExa2pucDJvNzh3cDFoeGZwbG1pb2R1bmw4Z20wcDlsNHNqdDE1MWZ5cCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/WVCz7hhi1gRHUfr5Wf/giphy.gif"

# ================================
# Calculate days left
# ================================
days_left = (release_date - datetime.now()).days

if days_left > 0:
    tweet_text = f"⏳ {days_left} days left until #OG hits the screens! 🔥"

    # ================================
    # Download GIF
    # ================================
    response = requests.get(gif_url)
    with open("og.gif", "wb") as f:
        f.write(response.content)

    # ================================
    # Upload GIF and Post Tweet
    # ================================
    media = client.upload_media("og.gif")
    client.create_tweet(text=tweet_text, media_ids=[media.media_id])

    print("Tweet posted successfully with GIF:", tweet_text)

else:
    print("The movie is already released or today is the release date!")
