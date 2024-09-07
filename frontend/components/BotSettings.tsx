import React, { useState } from 'react';
import axios from 'axios';

const BotSettings: React.FC = () => {
  const [keyword, setKeyword] = useState<string>("");

  const addKeyword = () => {
    axios.post('/api/add-keyword', { keyword })
      .then(() => {
        alert('Keyword added!');
      })
      .catch((error) => {
        console.error('Error adding keyword', error);
      });
  };

  return (
    <div>
      <h1>Bot Settings</h1>
      <input 
        type="text" 
        value={keyword} 
        onChange={(e) => setKeyword(e.target.value)} 
        placeholder="Enter a keyword" 
      />
      <button onClick={addKeyword}>Add Keyword</button>
    </div>
  );
};

export default BotSettings;
