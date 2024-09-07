# backend/bots/twitter_bot.py
import tweepy
from database.supabase_client import log_event

def run_twitter(keyword: str, platform: str):
    # Authentication
    consumer_key = "your_consumer_key"
    consumer_secret = "your_consumer_secret"
    access_token = "your_access_token"
    access_token_secret = "your_access_token_secret"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    # Search for tweets containing the keyword
    tweets = api.search_tweets(q=keyword, lang="en", count=10)

    # Log event and reply to the tweets
    for tweet in tweets:
        try:
            tweet_id = tweet.id
            user = tweet.user.screen_name
            message = f"Hey @{user}, I noticed you mentioned {keyword}. Let's connect!"
            
            # Reply to the tweet
            api.update_status(status=message, in_reply_to_status_id=tweet_id, auto_populate_reply_metadata=True)
            
            # Log the event
            log_event(platform, user, f"Replied to tweet: {tweet.text}")
        except Exception as e:
            print(f"Error replying to tweet: {e}")
