'use client';

import { useState } from 'react';
import { useGuideEngine } from '@/components/GuideEngineContext';
      {
        id: 'clue-outfit',
        title: 'Equip the best clue hunter outfit',
        description: 'Use light armor for agility while still preserving useful teleport gear.',
        requiredInventory: ['Graceful hood', 'Clue hunter cape', 'Teleports'],
        teleports: ['Seers village teleport'],
        estimatedMinutes: 5,
        reason: 'Fast movement reduces time spent traveling between clue locations.',
        alternative: 'Dragonhide can be used if you want a small defense boost.',
      },
    ],
  },
  {
    title: 'Execution',
    summary: 'Complete the clue steps, mark progress, and use focus mode for uninterrupted gameplay.',
    items: [
      {
        id: 'step-one',
        title: 'Travel to the first clue location',
        description: 'Open the clue and read the first instruction. Move to the location immediately.',
        requiredInventory: ['Teleport to Khardehn', 'Food for healing'],
        teleports: ['Khardehn teleport', 'Camelot teleport'],
        estimatedMinutes: 8,
        reason: 'Starting quickly keeps your session momentum high.',
        alternative: 'Use a ring of dueling for faster bank access if you need supplies.',
      },
      {
        id: 'step-two',
        title: 'Complete the emote challenge',
        description: 'Execute the required emote in the target area before the timer expires.',
        requiredInventory: ['Emote clue page', 'Agility boots'],
        teleports: ['Falador teleport', 'Ardougne teleport'],
        estimatedMinutes: 6,
        reason: 'Emote clues are often time-sensitive; staying ahead reduces retries.',
        alternative: 'Bring a teleport charged amulet to reset if you misclick.',
      },
    ],
  },
  {
    title: 'Wrap-up',
    summary: 'Finish the final clue, secure rewards, and log the completed session progress.',
    items: [
      {
        id: 'final-step',
        title: 'Open the reward casket and record outcomes',
        description: 'Ensure you have enough bank space, then open the casket and log the reward.',
        requiredInventory: ['Bank space', 'Teleport out'],
        teleports: ['Home teleport', 'Teleport to house'],
        estimatedMinutes: 7,
        reason: 'Logging rewards helps the guide recommend the next best target.',
        alternative: 'Leave the casket unopened if you need more bank space first.',
      },
    ],
  },
];

export function GuideChecklist() {
  const {
    currentActivity,
    currentStep,
    chapters,
    completedStepIds,
    progressPercent,
    totalSteps,
    markStepComplete,
    markStepIncomplete,
    moveNextStep,
    movePreviousStep,
    resetProgress,
  } = useGuideEngine();
  const [expandedChapters, setExpandedChapters] = useState<string[]>(['Preparation']);
  const [focusMode, setFocusMode] = useState(false);
  const completedCount = completedStepIds.length;

  if (!currentActivity) {
    return null;
  }

  return (
    <section className="space-y-6">
      <div className="grid gap-6 xl:grid-cols-[1.5fr_0.85fr]">
        <div className="rounded-3xl border border-slate-700 bg-slate-950/80 p-8 shadow-2xl shadow-slate-950/20">
          <div className="flex flex-col gap-4 sm:flex-row sm:items-end sm:justify-between">
            <div>
              <p className="text-sm uppercase tracking-[0.3em] text-slate-500">Current objective</p>
              <h3 className="mt-3 text-3xl font-semibold text-white">Complete the elite clue progression run</h3>
            </div>
            <button
              type="button"
              onClick={() => setFocusMode(!focusMode)}
              className="rounded-2xl border border-slate-700 bg-slate-900/80 px-4 py-3 text-sm text-slate-200 transition hover:border-slate-500"
            >
              {focusMode ? 'Exit Focus Mode' : 'Enter Focus Mode'}
            </button>
          </div>

          <div className="mt-6 grid gap-4 sm:grid-cols-3">
            <div className="rounded-3xl border border-slate-700 bg-slate-900/80 p-4">
              <p className="text-xs uppercase tracking-[0.3em] text-slate-500">Progress</p>
              <p className="mt-2 text-2xl font-semibold text-white">{completedCount}/{totalSteps}</p>
            </div>
            <div className="rounded-3xl border border-slate-700 bg-slate-900/80 p-4">
              <p className="text-xs uppercase tracking-[0.3em] text-slate-500">Completion</p>
              <p className="mt-2 text-2xl font-semibold text-white">{progressPercent}%</p>
            </div>
            <div className="rounded-3xl border border-slate-700 bg-slate-900/80 p-4">
              <p className="text-xs uppercase tracking-[0.3em] text-slate-500">Next step</p>
              <p className="mt-2 text-lg font-semibold text-white">{currentStep?.title ?? 'All done!'}</p>
            </div>
          </div>
        </div>

        <div className="space-y-4">
          <div className="rounded-3xl border border-slate-700 bg-slate-950/80 p-6 shadow-xl shadow-slate-950/20">
            <p className="text-sm uppercase tracking-[0.3em] text-slate-500">Estimated time</p>
            <p className="mt-2 text-3xl font-semibold text-white">~45 minutes</p>
          </div>
          <div className="rounded-3xl border border-slate-700 bg-slate-950/80 p-6 shadow-xl shadow-slate-950/20">
            <p className="text-sm uppercase tracking-[0.3em] text-slate-500">Required teleports</p>
            <div className="mt-4 flex flex-wrap gap-3">
              <span className="rounded-full border border-slate-700 bg-slate-900/80 px-3 py-1 text-sm text-slate-200">Ardougne</span>
              <span className="rounded-full border border-slate-700 bg-slate-900/80 px-3 py-1 text-sm text-slate-200">Varrock</span>
              <span className="rounded-full border border-slate-700 bg-slate-900/80 px-3 py-1 text-sm text-slate-200">Falador</span>
            </div>
          </div>
          <div className="rounded-3xl border border-slate-700 bg-slate-950/80 p-6 shadow-xl shadow-slate-950/20">
            <p className="text-sm uppercase tracking-[0.3em] text-slate-500">Required inventory</p>
            <ul className="mt-4 space-y-2 text-sm text-slate-300">
              <li>Prayer potion x5</li>
              <li>Graceful outfit</li>
              <li>Food and teleports</li>
            </ul>
          </div>
        </div>
      </div>

      <div className={focusMode ? 'rounded-3xl border border-slate-700 bg-slate-950/90 p-8 shadow-2xl shadow-slate-950/30' : 'rounded-3xl border border-slate-700 bg-slate-950/80 p-8 shadow-2xl shadow-slate-950/20'}>
        <div className="flex flex-col gap-6">
          <div className="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
            <div>
              <p className="text-sm uppercase tracking-[0.3em] text-slate-500">Checklist</p>
              <h3 className="mt-1 text-3xl font-semibold text-white">Step list</h3>
            </div>
            <div className="flex flex-wrap gap-3">
              <button
                type="button"
                onClick={resetProgress}
                className="rounded-2xl border border-slate-700 bg-slate-900/80 px-4 py-2 text-sm text-slate-200 transition hover:border-slate-500"
              >
                Reset Progress
              </button>
            </div>
          </div>

          {chapters.map((chapter) => {
            const isOpen = expandedChapters.includes(chapter.title);
            return (
              <div key={chapter.title} className="rounded-3xl border border-slate-700 bg-slate-900/80">
                <button
                  type="button"
                  onClick={() => {
                    setExpandedChapters((current) =>
                      current.includes(chapter.title)
                        ? current.filter((title) => title !== chapter.title)
                        : [...current, chapter.title]
                    );
                  }}
                  className="flex w-full items-center justify-between gap-4 px-6 py-5 text-left"
                >
                  <div>
                    <p className="text-sm uppercase tracking-[0.3em] text-slate-500">{chapter.title}</p>
                    <p className="mt-2 text-lg font-semibold text-white">{chapter.summary}</p>
                  </div>
                  <span className="text-xl text-slate-400">{isOpen ? '−' : '+'}</span>
                </button>
                {isOpen && (
                  <div className="space-y-4 border-t border-slate-700 px-6 py-5">
                    {chapter.items.map((item) => {
                      const completed = completedSteps.includes(item.id);
                      return (
                        <div key={item.id} className="rounded-3xl border border-slate-800 bg-slate-950/90 p-5">
                          <div className="flex flex-col gap-4 sm:flex-row sm:items-start sm:justify-between">
                            <div>
                              <div className="flex items-center gap-3">
                                <span className={`inline-flex h-8 w-8 items-center justify-center rounded-full ${completed ? 'bg-emerald-500 text-slate-950' : 'bg-slate-800 text-slate-400'}`}>
                                  {completed ? '✓' : '•'}
                                </span>
                                <h4 className="text-xl font-semibold text-white">{item.title}</h4>
                              </div>
                              <p className="mt-3 text-sm leading-6 text-slate-400">{item.description}</p>
                            </div>
                            <button
                              type="button"
                              onClick={() => {
                                if (completed) {
                                  markStepIncomplete(item.id);
                                } else {
                                  markStepComplete(item.id);
                                }
                              }}
                              className="rounded-2xl border border-slate-700 bg-slate-900/80 px-4 py-2 text-sm text-slate-200 transition hover:border-slate-500"
                            >
                              {completed ? 'Mark Incomplete' : 'Mark Complete'}
                            </button>
                          </div>

                          <div className="mt-5 grid gap-4 md:grid-cols-2">
                            <div className="rounded-3xl border border-slate-700 bg-slate-900/80 p-4">
                              <p className="text-xs uppercase tracking-[0.3em] text-slate-500">Why this matters</p>
                              <p className="mt-2 text-sm text-slate-300">{item.reason}</p>
                            </div>
                            <div className="rounded-3xl border border-slate-700 bg-slate-900/80 p-4">
                              <p className="text-xs uppercase tracking-[0.3em] text-slate-500">Alternative method</p>
                              <p className="mt-2 text-sm text-slate-300">{item.alternative}</p>
                            </div>
                          </div>

                          <div className="mt-5 grid gap-3 rounded-3xl border border-slate-700 bg-slate-900/80 p-4 text-sm text-slate-300 md:grid-cols-3">
                            <div>
                              <p className="text-xs uppercase tracking-[0.3em] text-slate-500">Inventory</p>
                              <ul className="mt-2 space-y-1">
                                {item.requiredInventory.map((inventory) => (
                                  <li key={inventory}>{inventory}</li>
                                ))}
                              </ul>
                            </div>
                            <div>
                              <p className="text-xs uppercase tracking-[0.3em] text-slate-500">Teleports</p>
                              <ul className="mt-2 space-y-1">
                                {item.teleports.map((teleport) => (
                                  <li key={teleport}>{teleport}</li>
                                ))}
                              </ul>
                            </div>
                            <div>
                              <p className="text-xs uppercase tracking-[0.3em] text-slate-500">Estimated time</p>
                              <p className="mt-2 text-lg font-semibold text-white">{item.estimatedMinutes} min</p>
                            </div>
                          </div>
                        </div>
                      );
                    })}
                  </div>
                )}
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
}
