'use client';

import { useEffect, useState } from 'react';
import { useGuideEngine } from '@/components/GuideEngineContext';

export function CompanionMode() {
  const {
    currentActivity,
    currentStep,
    completedStepIds,
    progressPercent,
    currentStepNumber,
    totalSteps,
    markStepComplete,
    markStepIncomplete,
    moveNextStep,
    movePreviousStep,
  } = useGuideEngine();
  const [collapsed, setCollapsed] = useState(false);
  const completed = completedStepIds.includes(currentStep.id);

  useEffect(() => {
    if (typeof window === 'undefined') {
      return;
    }

    const saved = window.localStorage.getItem('lodestone-companion-window');
    if (saved) {
      try {
        const parsed = JSON.parse(saved);
        if (parsed.width && parsed.height) {
          window.resizeTo(parsed.width, parsed.height);
        }
        if (parsed.left != null && parsed.top != null) {
          window.moveTo(parsed.left, parsed.top);
        }
      } catch {
        // ignore invalid data
      }
    }

    const savePosition = () => {
      window.localStorage.setItem(
        'lodestone-companion-window',
        JSON.stringify({
          left: window.screenX,
          top: window.screenY,
          width: window.outerWidth,
          height: window.outerHeight,
        })
      );
    };

    window.addEventListener('resize', savePosition);
    window.addEventListener('beforeunload', savePosition);

    return () => {
      window.removeEventListener('resize', savePosition);
      window.removeEventListener('beforeunload', savePosition);
    };
  }, []);

  return (
    <div className="min-h-[480px] max-w-[420px] rounded-[32px] border border-slate-700 bg-slate-950/95 p-5 shadow-2xl shadow-slate-950/40 backdrop-blur-xl overflow-auto" style={{ resize: 'both' }}>
      <div className="flex items-start justify-between gap-4">
        <div>
          <p className="text-xs uppercase tracking-[0.3em] text-slate-500">Companion Mode</p>
          <h2 className="mt-2 text-xl font-semibold text-white">{currentActivity.name}</h2>
          <p className="mt-1 text-sm text-slate-400">{currentActivity.objective}</p>
        </div>
        <span className="rounded-2xl bg-slate-900/80 px-3 py-1 text-xs uppercase tracking-[0.24em] text-slate-400">{currentActivity.status}</span>
      </div>

      <div className="mt-6 rounded-3xl border border-slate-800 bg-slate-900/80 p-4">
        <p className="text-xs uppercase tracking-[0.3em] text-slate-500">Current step</p>
        <h3 className="mt-3 text-lg font-semibold text-white">{currentStep.title}</h3>
        <p className="mt-2 text-sm leading-6 text-slate-400">{currentStep.description}</p>
      </div>

      <div className="mt-5 grid gap-3 sm:grid-cols-2">
        <div className="rounded-3xl border border-slate-800 bg-slate-900/80 p-4">
          <p className="text-xs uppercase tracking-[0.3em] text-slate-500">Required items</p>
          <ul className="mt-3 space-y-1 text-sm text-slate-300">
            {currentStep.requiredInventory.map((item) => (
              <li key={item}>• {item}</li>
            ))}
          </ul>
        </div>
        <div className="rounded-3xl border border-slate-800 bg-slate-900/80 p-4">
          <p className="text-xs uppercase tracking-[0.3em] text-slate-500">Recommended teleport</p>
          <p className="mt-3 text-lg font-semibold text-white">{currentStep.teleports[0] ?? currentActivity.recommendedTeleport}</p>
          <p className="mt-2 text-sm text-slate-400">Estimated: {currentStep.estimatedMinutes} min</p>
        </div>
      </div>

      <div className="mt-5 rounded-3xl border border-slate-800 bg-slate-900/80 p-4">
        <div className="flex items-center justify-between gap-4">
          <div>
            <p className="text-xs uppercase tracking-[0.3em] text-slate-500">Dialogue</p>
            <p className="mt-3 min-h-[60px] text-sm leading-6 text-slate-300">
              {currentStep.dialogue ?? 'Follow the step and mark it complete when ready.'}
            </p>
          </div>
          <button
            type="button"
            onClick={() => setCollapsed(!collapsed)}
            className="rounded-2xl border border-slate-700 bg-slate-900/80 px-3 py-2 text-xs uppercase tracking-[0.24em] text-slate-300 transition hover:border-slate-500"
          >
            {collapsed ? 'Expand' : 'Collapse'}
          </button>
        </div>
      </div>

      {!collapsed && (
        <div className="mt-5 rounded-3xl border border-slate-800 bg-slate-900/80 p-4">
          <p className="text-xs uppercase tracking-[0.3em] text-slate-500">Details</p>
          <div className="mt-3 grid gap-3 sm:grid-cols-2">
            <div>
              <p className="text-sm text-slate-300">Required Items</p>
              <ul className="mt-2 space-y-1 text-sm text-slate-300">
                {currentStep.requiredInventory.map((item) => (
                  <li key={item}>• {item}</li>
                ))}
              </ul>
            </div>
            <div>
              <p className="text-sm text-slate-300">Recommended teleport</p>
              <p className="mt-2 text-lg font-semibold text-white">{currentStep.teleports[0] ?? currentActivity.recommendedTeleport}</p>
              <p className="mt-1 text-sm text-slate-400">Estimated: {currentStep.estimatedMinutes} min</p>
            </div>
          </div>
        </div>
      )}

      <div className="mt-5 flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
        <div className="rounded-3xl border border-slate-800 bg-slate-900/80 px-4 py-3 text-sm text-slate-200">
          Progress: {completed ? 'Complete' : 'In progress'} · {progressPercent}% · Step {currentStepNumber}/{totalSteps}
        </div>
        <div className="flex flex-wrap gap-2">
          <button
            type="button"
            onClick={movePreviousStep}
            className="rounded-2xl border border-slate-700 bg-slate-900/80 px-4 py-2 text-sm text-slate-200 transition hover:border-slate-500"
          >
            Previous
          </button>
          <button
            type="button"
            onClick={() => {
              if (completed) {
                markStepIncomplete(currentStep.id);
              } else {
                markStepComplete(currentStep.id);
              }
            }}
            className="rounded-2xl border border-emerald-500 bg-emerald-500/10 px-4 py-2 text-sm text-emerald-200 transition hover:bg-emerald-500/20"
          >
            {completed ? 'Unmark Complete' : 'Mark Complete'}
          </button>
          <button
            type="button"
            onClick={moveNextStep}
            className="rounded-2xl border border-slate-700 bg-slate-900/80 px-4 py-2 text-sm text-slate-200 transition hover:border-slate-500"
          >
            Next
          </button>
        </div>
      </div>
    </div>
  );
}
