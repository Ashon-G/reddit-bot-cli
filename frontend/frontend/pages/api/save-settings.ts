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
