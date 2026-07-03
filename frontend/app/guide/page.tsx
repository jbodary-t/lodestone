import { Sidebar } from '@/components/Sidebar';
import { GuideChecklist } from '@/components/GuideChecklist';

export default function GuidePage() {
  return (
    <div className="min-h-screen bg-background text-slate-100">
        <div className="mx-auto flex min-h-screen max-w-[1600px] gap-6 px-6 py-8">
          <Sidebar />
          <main className="flex-1 space-y-8">
            <section className="rounded-3xl border border-slate-700 bg-slate-950/80 p-8 shadow-2xl shadow-slate-950/20">
              <div className="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
                <div>
                  <p className="text-sm uppercase tracking-[0.31em] text-slate-500">Guide</p>
                  <h2 className="mt-3 text-4xl font-semibold text-white">Live progression checklist</h2>
                  <p className="mt-2 max-w-2xl text-sm leading-6 text-slate-400">
                    Your interactive RuneScape guide for the current session, complete with objectives, travel planning, inventory prep, and step-by-step progression.
                  </p>
                </div>
                <div className="grid gap-3 sm:grid-cols-2">
                  <div className="rounded-2xl border border-slate-700 bg-slate-900/80 px-4 py-4 text-sm text-slate-300">
                    Current objective
                    <p className="mt-2 text-lg font-semibold text-white">Finish the elite clue scroll path</p>
                  </div>
                  <div className="rounded-2xl border border-slate-700 bg-slate-900/80 px-4 py-4 text-sm text-slate-300">
                    Estimated completion
                    <p className="mt-2 text-lg font-semibold text-white">~45 minutes</p>
                  </div>
                </div>
              </div>
            </section>

            <GuideChecklist />
          </main>
        </div>
      </div>
  );
}
