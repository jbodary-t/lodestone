import type { ReactNode } from 'react';

interface CardProps {
  title: string;
  value: string;
  description: string;
  icon: ReactNode;
}

export function Card({ title, value, description, icon }: CardProps) {
  return (
    <div className="rounded-3xl border border-slate-700 bg-slate-900/80 p-6 shadow-xl shadow-slate-950/20">
      <div className="flex items-center justify-between gap-4">
        <div>
          <p className="text-sm uppercase tracking-[0.24em] text-slate-500">{title}</p>
          <p className="mt-3 text-3xl font-semibold text-white">{value}</p>
        </div>
        <div className="inline-flex h-14 w-14 items-center justify-center rounded-3xl bg-slate-800 text-slate-200">
          {icon}
        </div>
      </div>
      <p className="mt-5 text-sm leading-6 text-slate-400">{description}</p>
    </div>
  );
}
