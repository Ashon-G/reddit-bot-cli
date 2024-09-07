# backend/bots/facebook_bot.py
import requests
from database.supabase_client import log_event

def run_facebook(keyword: str, platform: str):
    # Facebook API access token and page id
    access_token = "your_facebook_page_access_token"
    page_id = "your_facebook_page_id"

    # Create a post on the Facebook page
    url = f"https://graph.facebook.com/{page_id}/feed"
    data = {
        "message": f"Check out our content related to {keyword}!",
        "access_token": access_token
    }

    response = requests.post(url, data=data)
    
    if response.status_code == 200:
        log_event(platform, "Facebook Page", f"Posted message related to keyword: {keyword}")
    else:
        print(f"Failed to post message: {response.text}")
