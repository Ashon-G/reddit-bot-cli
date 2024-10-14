# bot.py
import time
import logging

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
    comment_text = config['bot_settings']['comment_text']

    try:
        for subreddit_name in subreddits:
            subreddit = reddit.subreddit(subreddit_name)
            for submission in subreddit.new(limit=10):
                title = submission.title.lower()
                if any(keyword in title for keyword in keywords):
                    logging.info(f"Found a post with keyword: {submission.title}")
                    submission.reply(comment_text)
                    logging.info(f"Commented on: {submission.title}")
                    time.sleep(20)  # To avoid rate limiting
    except Exception as e:
        logging.error(f"An error occurred: {e}")
