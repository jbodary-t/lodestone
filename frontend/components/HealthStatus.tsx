"use client";

import { useEffect, useState } from 'react';

export function HealthStatus() {
  const [status, setStatus] = useState('Checking...');

  useEffect(() => {
    const apiUrl = process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:8000/api';

    fetch(`${apiUrl}/health`)
      .then((response) => {
        if (!response.ok) {
          throw new Error('Backend offline');
        }
        return response.json();
      })
      .then((data) => {
        if (data?.status === 'ok') {
          setStatus('Backend Connected');
        } else {
          setStatus('Backend Offline');
        }
      })
      .catch(() => setStatus('Backend Offline'));
  }, []);

  return (
    <div className="rounded-2xl border border-slate-700 bg-slate-900/80 px-4 py-3 text-sm font-medium text-slate-100">
      {status}
    </div>
  );
}
