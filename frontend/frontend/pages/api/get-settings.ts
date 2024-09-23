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
