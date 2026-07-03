"use client";

import { useEffect, useState } from 'react';

interface HealthResponse {
  status: string;
  project?: string;
  version?: string;
  uptime?: string;
}

export function HealthStatus() {
  const [statusText, setStatusText] = useState('Checking...');
  const [backendVersion, setBackendVersion] = useState<string | null>(null);

  useEffect(() => {
    const apiUrl = process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:8000/api';

    fetch(`${apiUrl}/health`)
      .then((response) => {
        if (!response.ok) {
          throw new Error('Backend offline');
        }
        return response.json() as Promise<HealthResponse>;
      })
      .then((data) => {
        if (data?.status === 'ok') {
          setStatusText('Backend Connected');
          setBackendVersion(data.version ?? null);
        } else {
          setStatusText('Backend Offline');
        }
      })
      .catch(() => {
        setStatusText('Backend Offline');
        setBackendVersion(null);
      });
  }, []);

  return (
    <div className="rounded-3xl border border-slate-700 bg-slate-900/80 p-4 text-sm text-slate-100 shadow-lg shadow-slate-950/20">
      <div className="flex items-center justify-between gap-4">
        <span className="font-semibold">{statusText}</span>
        <span className={`rounded-full px-3 py-1 text-xs font-semibold ${statusText === 'Backend Connected' ? 'bg-emerald-500/20 text-emerald-300' : 'bg-rose-500/20 text-rose-300'}`}>
          {statusText === 'Backend Connected' ? 'Online' : 'Offline'}
        </span>
      </div>
      {backendVersion ? (
        <p className="mt-2 text-xs text-slate-400">Backend version: {backendVersion}</p>
      ) : (
        <p className="mt-2 text-xs text-slate-500">Unable to retrieve backend details.</p>
      )}
      <p className="mt-2 text-xs text-slate-500">Environment: {process.env.NEXT_PUBLIC_APP_ENVIRONMENT ?? process.env.NODE_ENV ?? 'development'}</p>
    </div>
  );
}
