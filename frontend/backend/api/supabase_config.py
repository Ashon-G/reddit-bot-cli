from supabase import create_client, Client

url = "your-supabase-url"
key = "your-supabase-key"

supabase: Client = create_client(url, key)
