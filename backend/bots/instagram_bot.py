# backend/bots/instagram_bot.py
import requests
from database.supabase_client import log_event

def run_instagram(keyword: str, platform: str):
    # Instagram API access token and Instagram user ID
    access_token = "your_instagram_access_token"
    instagram_user_id = "your_instagram_user_id"

    # Post image with caption to Instagram
    image_url = "https://example.com/path-to-your-image.jpg"
    caption = f"Discover more about {keyword} on our page!"

    url = f"https://graph.facebook.com/v15.0/{instagram_user_id}/media"
    params = {
        "image_url": image_url,
        "caption": caption,
        "access_token": access_token
    }

    response = requests.post(url, params=params)
    
    if response.status_code == 200:
        log_event(platform, "Instagram Account", f"Posted image with caption related to keyword: {keyword}")
    else:
        print(f"Failed to post image: {response.text}")
