from api.supabase_config import init_supabase

supabase = init_supabase()

def log_event(platform, user, message):
    data = {
        "platform": platform,
        "user": user,
        "message": message
    }
    supabase.table("events").insert(data).execute()

def get_keywords():
    response = supabase.table("keywords").select("*").execute()
    return response.data

def log_message(platform, message):
    supabase.table("messages").insert({"platform": platform, "message": message}).execute()
