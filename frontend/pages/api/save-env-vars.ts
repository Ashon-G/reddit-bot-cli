import { supabase } from '../../backend/api/supabase_config';

export default async function handler(req: { method: string; body: { linkedinEmail: any; linkedinPassword: any; twitterConsumerKey: any; twitterConsumerSecret: any; twitterAccessToken: any; twitterAccessTokenSecret: any; facebookAccessToken: any; facebookPageId: any; instagramAccessToken: any; instagramUserId: any; redditClientId: any; redditClientSecret: any; redditUserAgent: any; supabaseUrl: any; supabaseKey: any; }; }, res: { status: (arg0: number) => { (): any; new(): any; json: { (arg0: { error?: string; message?: string; }): void; new(): any; }; }; }) {
  if (req.method === 'POST') {
    const {
      linkedinEmail, linkedinPassword,
      twitterConsumerKey, twitterConsumerSecret, twitterAccessToken, twitterAccessTokenSecret,
      facebookAccessToken, facebookPageId,
      instagramAccessToken, instagramUserId,
      redditClientId, redditClientSecret, redditUserAgent,
      supabaseUrl, supabaseKey,
    } = req.body;

    // Save environment variables securely in Supabase
    const { data, error } = await supabase
      .from('environment_variables')
      .insert([
        {
          linkedin_email: linkedinEmail,
          linkedin_password: linkedinPassword,
          twitter_consumer_key: twitterConsumerKey,
          twitter_consumer_secret: twitterConsumerSecret,
          twitter_access_token: twitterAccessToken,
          twitter_access_token_secret: twitterAccessTokenSecret,
          facebook_access_token: facebookAccessToken,
          facebook_page_id: facebookPageId,
          instagram_access_token: instagramAccessToken,
          instagram_user_id: instagramUserId,
          reddit_client_id: redditClientId,
          reddit_client_secret: redditClientSecret,
          reddit_user_agent: redditUserAgent,
          supabase_url: supabaseUrl,
          supabase_key: supabaseKey,
        }
      ]);

    if (error) {
      return res.status(500).json({ error: 'Failed to save environment variables' });
    }

    res.status(200).json({ message: 'Environment variables saved successfully!' });
  } else {
    res.status(405).json({ error: 'Method Not Allowed' });
  }
}
