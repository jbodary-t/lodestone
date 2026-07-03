import Link from 'next/link';
import { Card } from '@/components/Card';
import { HealthStatus } from '@/components/HealthStatus';
import { Sidebar } from '@/components/Sidebar';

const cards = [
  {
    title: 'Guide',
    description: 'Follow a live RuneScape progression checklist while you play.',
    href: '/guide',
    status: 'Live',
    icon: '📘',
  },
  {
    title: 'Journey',
    description: 'Define and track your destination goals for progression.',
    href: '/journey',
    status: 'Coming Soon',
    icon: '🧭',
  },
  {
    title: 'Account',
    description: 'Manage account state, progression details, and settings.',
    href: '/account',
    status: 'Coming Soon',
    icon: '👤',
  },
  {
    title: 'Atlas',
    description: 'Review foundational game data and content facts.',
    href: '/atlas',
    status: 'Coming Soon',
    icon: '🗺️',
  },
  {
    title: 'Navigator',
    description: 'Explore future recommendation capabilities and direction.',
    href: '/navigator',
    status: 'Coming Soon',
    icon: '🚀',
  },
  {
    title: 'Chronicle',
    description: 'Capture progress logs and history for later review.',
    href: '/chronicle',
    status: 'Coming Soon',
    icon: '📜',
  },
  {
    title: 'Forecast',
    description: 'Predict future progression opportunities and blockers.',
    href: '/forecast',
    status: 'Coming Soon',
    icon: '🔮',
  },
  {
    title: 'Advisor',
    description: 'Access guidance and high-level planning tools.',
    href: '/advisor',
    status: 'Coming Soon',
    icon: '💡',
  },
  {
    title: 'Settings',
    description: 'Adjust Lodestone preferences and workspace configuration.',
    href: '/settings',
    status: 'Coming Soon',
    icon: '⚙️',
  },
];

export default function DashboardPage() {
  return (
    <div className="min-h-screen bg-background text-slate-100">
      <div className="mx-auto flex min-h-screen max-w-[1600px] gap-6 px-6 py-8">
        <Sidebar />
        <main className="flex-1 space-y-8">
          <section className="rounded-3xl border border-slate-700 bg-slate-950/80 p-8 shadow-2xl shadow-slate-950/20">
            <div className="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
              <div>
                <p className="text-sm uppercase tracking-[0.31em] text-slate-500">Mission Control</p>
                <h2 className="mt-3 text-4xl font-semibold text-white">Dashboard</h2>
                <p className="mt-2 max-w-2xl text-sm leading-6 text-slate-400">
                  Mission Control gives you an at-a-glance view of what’s active, where you should focus next, and the health of Lodestone while you play.
                </p>
              </div>
              <div className="space-y-3 text-right">
                <HealthStatus />
                <div className="rounded-2xl border border-slate-700 bg-slate-900/80 px-4 py-3 text-sm text-slate-400">
                  Environment: <span className="text-white">{process.env.NEXT_PUBLIC_APP_ENVIRONMENT ?? process.env.NODE_ENV ?? 'development'}</span>
                </div>
              </div>
            </div>
          </section>

          <section className="grid gap-6 xl:grid-cols-2">
            {cards.map((card) => (
              <Link key={card.title} href={card.href} className="block rounded-3xl border border-slate-700 bg-slate-900/80 p-6 shadow-xl shadow-slate-950/20 transition hover:border-slate-500 hover:bg-slate-800">
                <div className="flex items-center justify-between gap-4">
                  <div>
                    <p className="text-sm uppercase tracking-[0.24em] text-slate-500">{card.title}</p>
                    <p className="mt-3 text-2xl font-semibold text-white">{card.status}</p>
                  </div>
                  <div className="inline-flex h-14 w-14 items-center justify-center rounded-3xl bg-slate-800 text-slate-200">
                    {card.icon}
                  </div>
                </div>
                <p className="mt-5 text-sm leading-6 text-slate-400">{card.description}</p>
              </Link>
            ))}
          </section>
        </main>
      </div>
    </div>
  );
}
