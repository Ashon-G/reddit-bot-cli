import React, { useState } from 'react';
import axios from 'axios';

const EnvironmentSettings: React.FC = () => {
  // State to store environment variable inputs
  const [envVars, setEnvVars] = useState({
    linkedinEmail: '',
    linkedinPassword: '',
    twitterConsumerKey: '',
    twitterConsumerSecret: '',
    twitterAccessToken: '',
    twitterAccessTokenSecret: '',
    facebookAccessToken: '',
    facebookPageId: '',
    instagramAccessToken: '',
    instagramUserId: '',
    supabaseUrl: '',
    supabaseKey: '',
  });

  // Handle form input changes
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setEnvVars({
      ...envVars,
      [e.target.name]: e.target.value,
    });
  };

  // Handle form submission
  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    
    try {
      // Send the environment variables to the backend for saving
      const response = await axios.post('/api/save-env-vars', envVars);
      if (response.status === 200) {
        alert('Environment variables saved successfully!');
      }
    } catch (error) {
      console.error('Error saving environment variables', error);
      alert('Failed to save environment variables.');
    }
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Environment Settings</h1>
      <form onSubmit={handleSubmit} className="grid grid-cols-2 gap-4">

        {/* LinkedIn Settings */}
        <div className="col-span-2">
          <h2 className="font-semibold text-lg">LinkedIn Settings</h2>
        </div>
        <div className="col-span-1">
          <label className="block">LinkedIn Email</label>
          <input
            type="email"
            name="linkedinEmail"
            value={envVars.linkedinEmail}
            onChange={handleChange}
            className="input-field"
          />
        </div>
        <div className="col-span-1">
          <label className="block">LinkedIn Password</label>
          <input
            type="password"
            name="linkedinPassword"
            value={envVars.linkedinPassword}
            onChange={handleChange}
            className="input-field"
          />
        </div>

        {/* Twitter Settings */}
        <div className="col-span-2">
          <h2 className="font-semibold text-lg">Twitter Settings</h2>
        </div>
        <div className="col-span-1">
          <label className="block">Consumer Key</label>
          <input
            type="text"
            name="twitterConsumerKey"
            value={envVars.twitterConsumerKey}
            onChange={handleChange}
            className="input-field"
          />
        </div>
        <div className="col-span-1">
          <label className="block">Consumer Secret</label>
          <input
            type="text"
            name="twitterConsumerSecret"
            value={envVars.twitterConsumerSecret}
            onChange={handleChange}
            className="input-field"
          />
        </div>
        <div className="col-span-1">
          <label className="block">Access Token</label>
          <input
            type="text"
            name="twitterAccessToken"
            value={envVars.twitterAccessToken}
            onChange={handleChange}
            className="input-field"
          />
        </div>
        <div className="col-span-1">
          <label className="block">Access Token Secret</label>
          <input
            type="text"
            name="twitterAccessTokenSecret"
            value={envVars.twitterAccessTokenSecret}
            onChange={handleChange}
            className="input-field"
          />
        </div>

        {/* Facebook/Instagram Settings */}
        <div className="col-span-2">
          <h2 className="font-semibold text-lg">Facebook/Instagram Settings</h2>
        </div>
        <div className="col-span-1">
          <label className="block">Facebook Access Token</label>
          <input
            type="text"
            name="facebookAccessToken"
            value={envVars.facebookAccessToken}
            onChange={handleChange}
            className="input-field"
          />
        </div>
        <div className="col-span-1">
          <label className="block">Facebook Page ID</label>
          <input
            type="text"
            name="facebookPageId"
            value={envVars.facebookPageId}
            onChange={handleChange}
            className="input-field"
          />
        </div>
        <div className="col-span-1">
          <label className="block">Instagram Access Token</label>
          <input
            type="text"
            name="instagramAccessToken"
            value={envVars.instagramAccessToken}
            onChange={handleChange}
            className="input-field"
          />
        </div>
        <div className="col-span-1">
          <label className="block">Instagram User ID</label>
          <input
            type="text"
            name="instagramUserId"
            value={envVars.instagramUserId}
            onChange={handleChange}
            className="input-field"
          />
        </div>

        {/* Supabase Settings */}
        <div className="col-span-2">
          <h2 className="font-semibold text-lg">Supabase Settings</h2>
        </div>
        <div className="col-span-1">
          <label className="block">Supabase URL</label>
          <input
            type="text"
            name="supabaseUrl"
            value={envVars.supabaseUrl}
            onChange={handleChange}
            className="input-field"
          />
        </div>
        <div className="col-span-1">
          <label className="block">Supabase Key</label>
          <input
            type="text"
            name="supabaseKey"
            value={envVars.supabaseKey}
            onChange={handleChange}
            className="input-field"
          />
        </div>

        {/* Submit Button */}
        <div className="col-span-2 text-center">
          <button type="submit" className="btn-primary">
            Save Environment Variables
          </button>
        </div>
      </form>
    </div>
  );
};

export default EnvironmentSettings;
