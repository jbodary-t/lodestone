import { Card } from '@/components/Card';
import { HealthStatus } from '@/components/HealthStatus';
import { Sidebar } from '@/components/Sidebar';

const cards = [
  {
    title: 'Current Goal',
    value: 'Launch MVP',
    description: 'Define the next software milestone and align activity tracking around it.',
    icon: '🎯',
  },
  {
    title: 'Progress',
    value: '54%',
    description: 'Measure momentum across active quests and skill improvements.',
    icon: '📈',
  },
  {
    title: 'Recommended Next Step',
    value: 'Review Journey',
    description: 'Inspect the next scheduled activity and adjust priorities.',
    icon: '🧭',
  },
  {
    title: 'Upcoming Bottlenecks',
    value: '2 items',
    description: 'Identify the next areas that may require more focus or resources.',
    icon: '⚠️',
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
                <p className="text-sm uppercase tracking-[0.31em] text-slate-500">Dashboard</p>
                <h2 className="mt-3 text-4xl font-semibold text-white">Progress Overview</h2>
              </div>
              <HealthStatus />
            </div>
          </section>

          <section className="grid gap-6 md:grid-cols-2">
            {cards.map((card) => (
              <Card key={card.title} title={card.title} value={card.value} description={card.description} icon={card.icon} />
            ))}
          </section>
        </main>
      </div>
    </div>
  );
}
