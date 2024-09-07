import praw
from database.supabase_client import log_event

def run_reddit(keyword, platform):
    reddit = praw.Reddit(client_id="your_client_id",
                         client_secret="your_client_secret",
                         user_agent="your_user_agent")
    
    for submission in reddit.subreddit("all").search(keyword):
        log_event(platform, submission.author.name, submission.title)
        submission.reply(f"Hey, I noticed you mentioned {keyword}. Let's connect!")
