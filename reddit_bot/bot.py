# bot.py
import time
import logging
from reddit_bot.ml_models import sentiment_analyzer, generate_response  # Import your ML models

def search_and_comment(reddit, config):
    """
    Searches for posts with specified keywords in given subreddits
    and comments on them.

    Parameters:
    - reddit: Initialized PRAW Reddit instance.
    - config: ConfigParser object with loaded configuration.
    """
    keywords = [keyword.strip().lower() for keyword in config['bot_settings']['keywords'].split(',')]
    subreddits = [subreddit.strip() for subreddit in config['bot_settings']['subreddits'].split(',')]
    
    try:
        for subreddit_name in subreddits:
            subreddit = reddit.subreddit(subreddit_name)
            for submission in subreddit.new(limit=10):
                title = submission.title.lower()
                # Check for keywords in title
                if any(keyword in title for keyword in keywords):
                    logging.info(f"Found a post with keyword: {submission.title}")
                    
                    # Analyze the sentiment of the post
                    sentiment = sentiment_analyzer(submission.selftext)  # Analyze the post text
                    response = generate_response(submission.selftext)     # Generate a dynamic response

                    # Adjust response based on sentiment
                    if sentiment[0]['label'] == 'NEGATIVE':
                        response += " I'm sorry to hear that."
                    elif sentiment[0]['label'] == 'POSITIVE':
                        response += " I'm glad to hear that!"

                    # Comment on the post
                    submission.reply(response)
                    logging.info(f"Commented on: {submission.title}")
                    time.sleep(20)  # To avoid rate limiting
    except Exception as e:
        logging.error(f"An error occurred: {e}")

