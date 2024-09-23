#!/bin/bash

# Define directories
BACKEND_DIR="backend"
BOTS_DIR="$BACKEND_DIR/bots"
API_DIR="$BACKEND_DIR/api"
FRONTEND_DIR="frontend"
PAGES_DIR="$FRONTEND_DIR/pages"
APP_DIR="$FRONTEND_DIR/app"
UTILS_DIR="$FRONTEND_DIR/utils"

# Remove existing directories
echo "Cleaning up existing directories..."
rm -rf $BACKEND_DIR $FRONTEND_DIR

# Create directories
echo "Creating directories..."
mkdir -p $BOTS_DIR
mkdir -p $API_DIR
mkdir -p $PAGES_DIR
mkdir -p $APP_DIR
mkdir -p $UTILS_DIR

# Initialize Next.js project in a temporary directory
echo "Initializing Next.js project..."
npx create-next-app@latest temp-frontend --typescript

# Move Next.js project to the desired location
mv temp-frontend $FRONTEND_DIR

# Navigate to frontend directory
cd $FRONTEND_DIR

# Install necessary packages
npm install @supabase/supabase-js tailwindcss postcss autoprefixer axios

# Initialize TailwindCSS
npx tailwindcss init -p

# Create frontend files
echo "Creating frontend files..."

# API utility file
mkdir -p $UTILS_DIR
cat <<EOL > $UTILS_DIR/supabaseClient.ts
import { createClient } from '@supabase/supabase-js'

const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL!
const supabaseKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
export const supabase = createClient(supabaseUrl, supabaseKey)
EOL

# Pages and API routes
mkdir -p $PAGES_DIR/api
cat <<EOL > $PAGES_DIR/api/save-settings.ts
import type { NextApiRequest, NextApiResponse } from 'next'
import { supabase } from '../../utils/supabaseClient'

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  if (req.method === 'POST') {
    const { redditClientId, redditClientSecret, linkedinAccessToken } = req.body

    try {
      await supabase
        .from('environment_variables')
        .upsert({ reddit_client_id: redditClientId, reddit_client_secret: redditClientSecret, linkedin_access_token: linkedinAccessToken })

      res.status(200).json({ status: 'success' })
    } catch (error) {
      res.status(500).json({ error: 'Failed to save settings' })
    }
  } else {
    res.status(405).end()
  }
}
EOL

cat <<EOL > $PAGES_DIR/api/get-settings.ts
import type { NextApiRequest, NextApiResponse } from 'next'
import { supabase } from '../../utils/supabaseClient'

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  if (req.method === 'GET') {
    try {
      const { data, error } = await supabase.from('environment_variables').select('*')

      if (error) throw error

      res.status(200).json({ settings: data })
    } catch (error) {
      res.status(500).json({ error: 'Failed to fetch settings' })
    }
  } else {
    res.status(405).end()
  }
}
EOL

# Create a simple interface for the dashboard
mkdir -p $APP_DIR/dashboard
cat <<EOL > $APP_DIR/dashboard/page.tsx
import { useState, useEffect } from 'react'
import axios from 'axios'

const Dashboard = () => {
  const [settings, setSettings] = useState<any>(null)
  const [redditClientId, setRedditClientId] = useState('')
  const [redditClientSecret, setRedditClientSecret] = useState('')
  const [linkedinAccessToken, setLinkedinAccessToken] = useState('')

  useEffect(() => {
    async function fetchSettings() {
      const response = await axios.get('/api/get-settings')
      setSettings(response.data.settings[0] || {})
      setRedditClientId(response.data.settings[0]?.reddit_client_id || '')
      setRedditClientSecret(response.data.settings[0]?.reddit_client_secret || '')
      setLinkedinAccessToken(response.data.settings[0]?.linkedin_access_token || '')
    }
    fetchSettings()
  }, [])

  const handleSave = async () => {
    await axios.post('/api/save-settings', {
      redditClientId,
      redditClientSecret,
      linkedinAccessToken,
    })
  }

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold">Bot Dashboard</h1>
      <div className="my-4">
        <label className="block">Reddit Client ID:</label>
        <input
          type="text"
          value={redditClientId}
          onChange={(e) => setRedditClientId(e.target.value)}
          className="border p-2"
        />
        <label className="block">Reddit Client Secret:</label>
        <input
          type="text"
          value={redditClientSecret}
          onChange={(e) => setRedditClientSecret(e.target.value)}
          className="border p-2"
        />
        <label className="block">LinkedIn Access Token:</label>
        <input
          type="text"
          value={linkedinAccessToken}
          onChange={(e) => setLinkedinAccessToken(e.target.value)}
          className="border p-2"
        />
        <button
          onClick={handleSave}
          className="mt-2 p-2 bg-blue-500 text-white"
        >
          Save Settings
        </button>
      </div>
      {/* Add monitoring and other functionalities here */}
    </div>
  )
}

export default Dashboard
EOL

# Tailwind configuration
cat <<EOL > $FRONTEND_DIR/tailwind.config.js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx}",
    "./pages/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
EOL

cat <<EOL > $FRONTEND_DIR/postcss.config.js
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
EOL

cat <<EOL > $FRONTEND_DIR/globals.css
@tailwind base;
@tailwind components;
@tailwind utilities;
EOL

# Create backend files
echo "Creating backend files..."

# Main FastAPI file
mkdir -p $BACKEND_DIR/api
mkdir -p $BOTS_DIR
cat <<EOL > $BACKEND_DIR/main.py
from fastapi import FastAPI
from api.bot_controller import router as bot_router

app = FastAPI()

app.include_router(bot_router, prefix="/api")
EOL

# Supabase config
cat <<EOL > $BACKEND_DIR/api/supabase_config.py
from supabase import create_client, Client

url = "your-supabase-url"
key = "your-supabase-key"

supabase: Client = create_client(url, key)
EOL

# Bot controller
cat <<EOL > $BACKEND_DIR/api/bot_controller.py
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
EOL

# Reddit bot
cat <<EOL > $BOTS_DIR/reddit_bot.py
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
EOL

# LinkedIn bot
cat <<EOL > $BOTS_DIR/linkedin_bot.py
from linkedin_api import Linkedin

class LinkedInBot:
    def __init__(self, access_token: str):
        self.linkedin = Linkedin(access_token)

    def get_connections(self):
        return self.linkedin.get_connections()
EOL

# Create virtual environment and install packages
echo "Creating virtual environment and installing packages..."
python3 -m venv venv
source venv/bin/activate

pip install fastapi uvicorn supabase-py praw linkedin-api

# Install additional dependencies to resolve conflicts
pip install httpx requests==2.31.0

echo "Setup complete. Please review and adjust configurations as needed."
