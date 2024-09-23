from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from bots.reddit_bot import RedditBot
from bots.linkedin_bot import LinkedInBot
from supabase_config import supabase

router = APIRouter()

class BotSettings(BaseModel):
    reddit_client_id: str
    reddit_client_secret: str
    linkedin_access_token: str

@router.post("/save-settings")
async def save_settings(settings: BotSettings):
    try:
        # Save settings to Supabase
        supabase.table("environment_variables").upsert({
            "reddit_client_id": settings.reddit_client_id,
            "reddit_client_secret": settings.reddit_client_secret,
            "linkedin_access_token": settings.linkedin_access_token,
        }).execute()
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get-settings")
async def get_settings():
    try:
        data = supabase.table("environment_variables").select("*").execute()
        return {"settings": data.data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
