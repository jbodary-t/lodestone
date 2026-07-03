'use client';

import { createContext, useContext, useEffect, useMemo, useState } from 'react';

export type GuideStep = {
  id: string;
  title: string;
  description: string;
  requiredInventory: string[];
  teleports: string[];
  estimatedMinutes: number;
  reason: string;
  alternative: string;
  dialogue?: string;
};

export type GuideChapter = {
  title: string;
  summary: string;
  items: GuideStep[];
};

export type GuideActivity = {
  id: string;
  name: string;
  objective: string;
  recommendedTeleport: string;
  estimatedSessionMinutes: number;
  status: string;
};

export type GuideIntegrationAdapter = {
  name: string;
  enabled: boolean;
  connect: () => Promise<void>;
};

export interface GuideEngineValue {
  activities: GuideActivity[];
  currentActivity: GuideActivity;
  chapters: GuideChapter[];
  currentStep: GuideStep;
  completedStepIds: string[];
  progressPercent: number;
  totalSteps: number;
  currentStepIndex: number;
  currentStepNumber: number;
  markStepComplete: (id: string) => void;
  markStepIncomplete: (id: string) => void;
  resetProgress: () => void;
  moveNextStep: () => void;
  movePreviousStep: () => void;
  selectStep: (id: string) => void;
  selectActivity: (id: string) => void;
  registerIntegration: (adapter: GuideIntegrationAdapter) => void;
  integrations: GuideIntegrationAdapter[];
}

const sampleChapters: GuideChapter[] = [
  {
    title: 'Preparation',
    summary:
      'Gather required items, teleport methods, and optional secondary tools before starting the active RuneScape session.',
    items: [
      {
        id: 'prep-potions',
        title: 'Prepare prayer potions and teleport runes',
        description:
          'Stock your inventory with prayer restoration and enough teleports for the planned route.',
        requiredInventory: ['Prayer potion x5', 'Teleport runes', 'Food'],
        teleports: ['Varrock teleport', 'Ardougne teleport'],
        estimatedMinutes: 10,
        reason:
          'Preparation keeps the session fluid and ensures you can reach each objective without detours.',
        alternative: 'If you prefer a lighter inventory, swap to super restores and a ring of dueling.',
        dialogue:
          'Are you ready to start the clue path? Confirm your teleport and potion setup before moving on.',
      },
      {
        id: 'prep-outfit',
        title: 'Equip a compact clue runner outfit',
        description:
          'Use an outfit optimized for movement, teleport access, and a little bit of defense.',
        requiredInventory: ['Graceful hood', 'Clue hunter cape', 'Teleport jewelry'],
        teleports: ['Seers Village teleport'],
        estimatedMinutes: 5,
        reason:
          'A compact outfit reduces travel time while still giving you enough safety to react to content.',
        alternative: 'Dragonhide works if you want a bit more defensive buffer.',
      },
    ],
  },
  {
    title: 'Execution',
    summary:
      'Complete step-by-step objectives, mark progress, and keep the session moving toward the final reward.',
    items: [
      {
        id: 'exec-first-step',
        title: 'Move to the first clue location',
        description:
          'Open the clue scroll, read the first instruction, and travel to the designated location immediately.',
        requiredInventory: ['Teleport to Khardehn', 'Easy food', 'Light armor'],
        teleports: ['Khardehn teleport', 'Camelot teleport'],
        estimatedMinutes: 8,
        reason:
          'Starting promptly avoids losing momentum and reduces the chance of the clue path becoming stale.',
        alternative:
          'Use a charged amulet of glory if you want faster banking before the first task.',
        dialogue: 'First clue ready. Choose your fastest route and move in.',
      },
      {
        id: 'exec-emote-challenge',
        title: 'Complete the emote clue',
        description:
          'Execute the required emote at the correct location and check whether the reward piece appears.',
        requiredInventory: ['Emote clue page', 'Agility boots', 'Teleport jewelry'],
        teleports: ['Falador teleport', 'Ardougne teleport'],
        estimatedMinutes: 6,
        reason:
          'Emote clues are timing-sensitive, so staying on track reduces retries and wasted gameplay time.',
        alternative:
          'A teleport-charged ring can help you recover quickly if you need to resupply or reposition.',
      },
    ],
  },
  {
    title: 'Wrap-up',
    summary:
      'Finish the final clue, collect your reward, and capture the session outcome for future recommendations.',
    items: [
      {
        id: 'wrap-reward',
        title: 'Open the reward casket and log your results',
        description:
          'Open the casket in a safe area, note the reward, and update the companion state for the next session.',
        requiredInventory: ['Bank space', 'Teleport out'],
        teleports: ['Home teleport', 'Teleport to house'],
        estimatedMinutes: 7,
        reason:
          'Recording the reward helps the guide refine future recommendations and keeps your progression history accurate.',
        alternative:
          'Delay opening if you need more bank space, then resume once the inventory is ready.',
      },
    ],
  },
];

const sampleActivity: GuideActivity = {
  id: 'elite-clue-run',
  name: 'Elite Clue Progression',
  objective: 'Complete the active clue path with minimal downtime and reliable teleport coverage.',
  recommendedTeleport: 'Varrock teleport',
  estimatedSessionMinutes: 45,
  status: 'Ready',
};

const activities: GuideActivity[] = [sampleActivity];

const GuideEngineContext = createContext<GuideEngineValue | undefined>(undefined);

export function GuideEngineProvider({ children }: { children: React.ReactNode }) {
  const [completedStepIds, setCompletedStepIds] = useState<string[]>([]);
  const [selectedStepId, setSelectedStepId] = useState<string>(sampleChapters[0].items[0].id);
  const [selectedActivityId, setSelectedActivityId] = useState<string>(sampleActivity.id);
  const [integrations, setIntegrations] = useState<GuideIntegrationAdapter[]>([]);

  const allSteps = useMemo(() => sampleChapters.flatMap((chapter) => chapter.items), []);
  const totalSteps = allSteps.length;
  const currentStepIndex = useMemo(
    () => Math.max(0, allSteps.findIndex((step) => step.id === selectedStepId)),
    [allSteps, selectedStepId]
  );
  const currentStep = useMemo(
    () => allSteps[currentStepIndex] ?? allSteps[0],
    [allSteps, currentStepIndex]
  );
  const currentActivity = useMemo(
    () => activities.find((activity) => activity.id === selectedActivityId) ?? activities[0],
    [selectedActivityId]
  );
  const progressPercent = useMemo(
    () => Math.round((completedStepIds.length / totalSteps) * 100),
    [completedStepIds.length, totalSteps]
  );

  const loadSavedState = () => {
    try {
      const savedSteps = window.localStorage.getItem('lodestone-guide-completed-steps');
      const savedStepId = window.localStorage.getItem('lodestone-guide-selected-step');
      const savedActivityId = window.localStorage.getItem('lodestone-guide-selected-activity');

      if (savedSteps) {
        const parsed = JSON.parse(savedSteps);
        if (Array.isArray(parsed)) {
          setCompletedStepIds(parsed.filter((id) => typeof id === 'string'));
        }
      }

      if (savedStepId && allSteps.some((step) => step.id === savedStepId)) {
        setSelectedStepId(savedStepId);
      }

      if (savedActivityId && activities.some((activity) => activity.id === savedActivityId)) {
        setSelectedActivityId(savedActivityId);
      }
    } catch {
      // ignore invalid local storage content
    }
  };

  const saveState = () => {
    window.localStorage.setItem('lodestone-guide-completed-steps', JSON.stringify(completedStepIds));
    window.localStorage.setItem('lodestone-guide-selected-step', selectedStepId);
    window.localStorage.setItem('lodestone-guide-selected-activity', selectedActivityId);
  };

  useEffect(() => {
    if (typeof window !== 'undefined') {
      loadSavedState();
    }
  }, []);

  useEffect(() => {
    if (typeof window !== 'undefined') {
      saveState();
    }
  }, [completedStepIds, selectedStepId, selectedActivityId]);

  const markStepComplete = (id: string) => {
    setCompletedStepIds((previous) => (previous.includes(id) ? previous : [...previous, id]));
  };

  const markStepIncomplete = (id: string) => {
    setCompletedStepIds((previous) => previous.filter((stepId) => stepId !== id));
  };

  const resetProgress = () => {
    setCompletedStepIds([]);
  };

  const moveNextStep = () => {
    const nextIndex = Math.min(totalSteps - 1, currentStepIndex + 1);
    setSelectedStepId(allSteps[nextIndex].id);
  };

  const movePreviousStep = () => {
    const previousIndex = Math.max(0, currentStepIndex - 1);
    setSelectedStepId(allSteps[previousIndex].id);
  };

  const selectStep = (id: string) => {
    if (allSteps.some((step) => step.id === id)) {
      setSelectedStepId(id);
    }
  };

  const selectActivity = (id: string) => {
    if (activities.some((activity) => activity.id === id)) {
      setSelectedActivityId(id);
    }
  };

  const registerIntegration = (adapter: GuideIntegrationAdapter) => {
    setIntegrations((previous) => {
      if (previous.some((item) => item.name === adapter.name)) {
        return previous;
      }
      return [...previous, adapter];
    });
  };

  const value: GuideEngineValue = {
    activities,
    currentActivity,
    chapters: sampleChapters,
    currentStep,
    completedStepIds,
    progressPercent,
    totalSteps,
    currentStepIndex,
    currentStepNumber: currentStepIndex + 1,
    markStepComplete,
    markStepIncomplete,
    resetProgress,
    moveNextStep,
    movePreviousStep,
    selectStep,
    selectActivity,
    registerIntegration,
    integrations,
  };

  return <GuideEngineContext.Provider value={value}>{children}</GuideEngineContext.Provider>;
}

export function useGuideEngine() {
  const context = useContext(GuideEngineContext);
  if (!context) {
    throw new Error('useGuideEngine must be used within a GuideEngineProvider');
  }
  return context;
}
