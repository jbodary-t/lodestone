import Link from 'next/link';

const navigation = [
  { label: 'Dashboard', href: '/' },
  { label: 'Journey', href: '/journey' },
  { label: 'Activities', href: '/activities' },
  { label: 'Settings', href: '/settings' },
];

export function Sidebar() {
  return (
    <aside className="w-72 border-r border-slate-700 bg-slate-950/80 p-6 text-slate-100">
      <div className="mb-10">
        <div className="inline-flex h-12 w-12 items-center justify-center rounded-2xl bg-gradient-to-br from-violet-600 to-sky-500 text-white shadow-lg shadow-violet-600/20">
          L
        </div>
        <div className="mt-6">
          <p className="text-sm uppercase tracking-[0.3em] text-slate-500">Lodestone</p>
          <h1 className="mt-2 text-2xl font-semibold">Progress Hub</h1>
        </div>
      </div>
      <nav className="space-y-2">
        {navigation.map((item) => (
          <Link
            key={item.href}
            href={item.href}
            className="block rounded-2xl px-4 py-3 text-sm font-medium text-slate-200 transition hover:bg-slate-800"
          >
            {item.label}
          </Link>
        ))}
      </nav>
    </aside>
  );
}
