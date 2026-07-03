import { Sidebar } from '@/components/Sidebar';

export default function AdvisorPage() {
  return (
    <div className="min-h-screen bg-background text-slate-100">
      <div className="mx-auto flex min-h-screen max-w-[1600px] gap-6 px-6 py-8">
        <Sidebar />
        <main className="flex-1 space-y-8">
          <section className="rounded-3xl border border-slate-700 bg-slate-950/80 p-8 shadow-2xl shadow-slate-950/20">
            <div className="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
              <div>
                <p className="text-sm uppercase tracking-[0.31em] text-slate-500">Advisor</p>
                <h2 className="mt-3 text-4xl font-semibold text-white">Guidance Center</h2>
              </div>
              <p className="max-w-xl text-sm leading-6 text-slate-400">
                Access decision support, planning insights, and future guidance from Lodestone.
              </p>
            </div>
          </section>

          <section className="grid gap-6 md:grid-cols-2">
            <div className="rounded-3xl border border-slate-700 bg-slate-900/80 p-6 shadow-xl shadow-slate-950/20">
              <h3 className="text-xl font-semibold text-white">Decision Support</h3>
              <p className="mt-4 text-slate-400">Advisor will help determine the best path for your journey objectives.</p>
            </div>
            <div className="rounded-3xl border border-slate-700 bg-slate-900/80 p-6 shadow-xl shadow-slate-950/20">
              <h3 className="text-xl font-semibold text-white">Actionable Tips</h3>
              <p className="mt-4 text-slate-400">Surface recommendations, warnings, and strategic notes.</p>
            </div>
          </section>
        </main>
      </div>
    </div>
  );
}
