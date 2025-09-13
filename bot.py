from datetime import datetime
import os
import tweepy

# ================================
# Load Twitter API keys from GitHub Secrets
# ================================
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_secret = os.getenv("ACCESS_SECRET")
bearer_token = os.getenv("BEARER_TOKEN")

# ================================
# Initialize Tweepy v2 client (text-only tweets)
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
days_left = (release_date - datetime.now()).days

# ================================
# Compose tweet text
# ================================
if days_left > 0:
    tweet_text = f"{days_left}"
else:
    tweet_text = "Firestorm Unleashed"

# ================================
# Post tweet
# ================================
client.create_tweet(text=tweet_text)
print("Tweet posted:", tweet_text)
