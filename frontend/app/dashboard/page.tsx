// pages/dashboard.tsx
import React from 'react';
import BotDashboard from '@/components/BotDashboard';
import BotSettings from '@/components/BotSettings';

const Dashboard: React.FC = () => {
  return (
    <div className="min-h-screen bg-gray-100 py-10">
      <div className="container mx-auto px-4">
        <h1 className="text-4xl font-bold mb-6">Admin Dashboard</h1>
        <BotDashboard />
        <BotSettings />
      </div>
    </div>
  );
};

export default Dashboard;
