# backend/api/bot_controller.py
from database.supabase_client import get_keywords
from bots.twitter_bot import run_twitter
from bots.linkedin_bot import run_linkedin
from bots.facebook_bot import run_facebook
from bots.instagram_bot import run_instagram

def start_bot(bot_function, platform: str):
    keywords = get_keywords()
    for keyword in keywords:
        bot_function(keyword, platform)

def run_all_bots():
    platforms = [
        (run_twitter, 'Twitter'),
        (run_linkedin, 'LinkedIn'),
        (run_facebook, 'Facebook'),
        (run_instagram, 'Instagram')
    ]
    for bot_func, platform in platforms:
        start_bot(bot_func, platform)
