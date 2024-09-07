import React, { useState, useEffect } from 'react';
import axios from 'axios';

interface Bot {
  platform: string;
  status: string;
  last_event: string;
}

const BotDashboard: React.FC = () => {
  const [bots, setBots] = useState<Bot[]>([]);

  useEffect(() => {
    axios.get('/api/get-bot-status').then((response) => {
      setBots(response.data);
    });
  }, []);

  return (
    <div>
      <h1>Bot Dashboard</h1>
      <table>
        <thead>
          <tr>
            <th>Platform</th>
            <th>Status</th>
            <th>Last Event</th>
          </tr>
        </thead>
        <tbody>
          {bots.map((bot, index) => (
            <tr key={index}>
              <td>{bot.platform}</td>
              <td>{bot.status}</td>
              <td>{bot.last_event}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default BotDashboard;
