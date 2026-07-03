import Link from 'next/link';

const navItems = [
  { label: 'Guide', href: '/guide' },
  { label: 'Journey', href: '/journey' },
  { label: 'Account', href: '/account' },
  { label: 'Atlas', href: '/atlas' },
  { label: 'Navigator', href: '/navigator' },
  { label: 'Chronicle', href: '/chronicle' },
  { label: 'Forecast', href: '/forecast' },
  { label: 'Advisor', href: '/advisor' },
  { label: 'Settings', href: '/settings' },
];

export function TopNav() {
  return (
    <header className="sticky top-0 z-40 border-b border-slate-800 bg-slate-950/95 backdrop-blur-xl">
      <div className="mx-auto flex max-w-[1600px] items-center justify-between gap-4 px-6 py-4">
        <div className="flex items-center gap-3">
          <div className="inline-flex h-12 w-12 items-center justify-center rounded-2xl bg-gradient-to-br from-violet-600 to-sky-500 text-xl font-semibold text-white shadow-lg shadow-violet-600/20">
            L
          </div>
          <div>
            <p className="text-sm uppercase tracking-[0.3em] text-slate-500">Lodestone</p>
            <p className="text-sm text-slate-400">v0.1.0</p>
          </div>
        </div>

        <div className="hidden items-center gap-4 md:flex">
          {navItems.slice(0, 6).map((item) => (
            <Link key={item.href} href={item.href} className="rounded-2xl px-3 py-2 text-sm font-medium text-slate-300 transition hover:bg-slate-900 hover:text-white">
              {item.label}
            </Link>
          ))}
          <span className="rounded-2xl border border-slate-700 bg-slate-900/80 px-3 py-2 text-xs uppercase tracking-[0.24em] text-slate-500">Beta</span>
        </div>

        <div className="flex items-center gap-3">
          <button className="rounded-2xl border border-slate-700 bg-slate-900/80 px-3 py-2 text-sm text-slate-200 transition hover:border-slate-500">
            Game
          </button>
          <button className="rounded-2xl border border-slate-700 bg-slate-900/80 px-3 py-2 text-sm text-slate-200 transition hover:border-slate-500">
            Theme
          </button>
        </div>
      </div>
    </header>
  );
}
