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
