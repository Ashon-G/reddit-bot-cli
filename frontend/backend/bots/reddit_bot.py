import praw

class RedditBot:
    def __init__(self, client_id: str, client_secret: str):
        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent="my_bot"
        )

    def fetch_posts(self, subreddit: str):
        return self.reddit.subreddit(subreddit).hot(limit=10)
