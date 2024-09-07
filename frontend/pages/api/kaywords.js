import { supabase } from '../../../backend/api/supabase_config';

export default async function handler(req, res) {
  if (req.method === 'POST') {
    const { keyword } = req.body;

    if (!keyword) {
      return res.status(400).json({ error: 'Keyword is required' });
    }

    const { data, error } = await supabase
      .from('keywords')
      .insert([{ keyword }]);

    if (error) {
      return res.status(400).json({ error: error.message });
    }

    return res.status(200).json({ message: 'Keyword added!' });
  } else {
    return res.status(405).json({ error: 'Method Not Allowed' });
  }
}
