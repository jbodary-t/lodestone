import type { Config } from 'tailwindcss';

const config: Config = {
  content: ['./app/**/*.{js,ts,jsx,tsx}', './components/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        background: '#0f172a',
        surface: '#111827',
        border: '#334155',
        primary: '#7c3aed',
        muted: '#94a3b8',
        accent: '#22c55e'
      },
    },
  },
  plugins: [],
};

export default config;
