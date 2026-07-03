import type { Metadata } from 'next';
import './styles/globals.css';
import { TopNav } from '@/components/TopNav';
import { GuideEngineProvider } from '@/components/GuideEngineContext';

export const metadata: Metadata = {
  title: 'Lodestone',
  description: 'Lodestone activity coordination and progress dashboard',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className="min-h-screen bg-background text-slate-100 antialiased">
        <GuideEngineProvider>
          <TopNav />
          <main>{children}</main>
        </GuideEngineProvider>
      </body>
    </html>
  );
}
