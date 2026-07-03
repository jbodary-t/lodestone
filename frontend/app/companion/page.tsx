import { CompanionMode } from '@/components/CompanionMode';

export const metadata = {
  title: 'Lodestone Companion',
  description: 'Compact RuneScape companion mode for active gameplay support.',
};

export default function CompanionPage() {
  return (
      <div className="min-h-screen bg-background text-slate-100 px-6 py-8">
        <div className="mx-auto max-w-[460px]">
          <CompanionMode />
        </div>
      </div>
  );
}
