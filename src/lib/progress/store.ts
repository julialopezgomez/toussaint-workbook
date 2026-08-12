// IndexedDB-backed progress store. Progress is attempted-work-based, not page-view-based:
// a module only counts as "in progress" once at least one exercise attempt is recorded here.

const DB_NAME = 'toussaint-workbook-progress';
const DB_VERSION = 1;
const ATTEMPTS_STORE = 'attempts';
const MODULES_STORE = 'modules';

export interface AttemptRecord {
  exerciseId: string;
  moduleId: string;
  timestamp: number;
  answer: string;
  checkResult?: { passed: boolean; mode: 'deterministic' | 'symbolic' | 'rubric-self' };
}

export interface ModuleProgress {
  moduleId: string;
  status: 'not-started' | 'in-progress' | 'mastered';
  timeSpentMinutes: number;
  lastVisited: number;
}

function openDb(): Promise<IDBDatabase> {
  return new Promise((resolve, reject) => {
    const req = indexedDB.open(DB_NAME, DB_VERSION);
    req.onupgradeneeded = () => {
      const db = req.result;
      if (!db.objectStoreNames.contains(ATTEMPTS_STORE)) {
        const store = db.createObjectStore(ATTEMPTS_STORE, { keyPath: ['exerciseId', 'timestamp'] });
        store.createIndex('byExercise', 'exerciseId');
        store.createIndex('byModule', 'moduleId');
      }
      if (!db.objectStoreNames.contains(MODULES_STORE)) {
        db.createObjectStore(MODULES_STORE, { keyPath: 'moduleId' });
      }
    };
    req.onsuccess = () => resolve(req.result);
    req.onerror = () => reject(req.error);
  });
}

export async function recordAttempt(record: AttemptRecord): Promise<void> {
  const db = await openDb();
  await new Promise<void>((resolve, reject) => {
    const tx = db.transaction([ATTEMPTS_STORE, MODULES_STORE], 'readwrite');
    tx.objectStore(ATTEMPTS_STORE).put(record);
    const modStore = tx.objectStore(MODULES_STORE);
    const getReq = modStore.get(record.moduleId);
    getReq.onsuccess = () => {
      const existing: ModuleProgress = getReq.result ?? {
        moduleId: record.moduleId,
        status: 'not-started',
        timeSpentMinutes: 0,
        lastVisited: Date.now(),
      };
      existing.status = existing.status === 'mastered' ? 'mastered' : 'in-progress';
      existing.lastVisited = Date.now();
      modStore.put(existing);
    };
    tx.oncomplete = () => resolve();
    tx.onerror = () => reject(tx.error);
  });
}

export async function getAttempts(exerciseId: string): Promise<AttemptRecord[]> {
  const db = await openDb();
  return new Promise((resolve, reject) => {
    const tx = db.transaction(ATTEMPTS_STORE, 'readonly');
    const idx = tx.objectStore(ATTEMPTS_STORE).index('byExercise');
    const req = idx.getAll(exerciseId);
    req.onsuccess = () => resolve(req.result as AttemptRecord[]);
    req.onerror = () => reject(req.error);
  });
}

export async function exportProgress(): Promise<string> {
  const db = await openDb();
  const [attempts, modules] = await Promise.all([
    new Promise<AttemptRecord[]>((resolve, reject) => {
      const tx = db.transaction(ATTEMPTS_STORE, 'readonly');
      const req = tx.objectStore(ATTEMPTS_STORE).getAll();
      req.onsuccess = () => resolve(req.result as AttemptRecord[]);
      req.onerror = () => reject(req.error);
    }),
    new Promise<ModuleProgress[]>((resolve, reject) => {
      const tx = db.transaction(MODULES_STORE, 'readonly');
      const req = tx.objectStore(MODULES_STORE).getAll();
      req.onsuccess = () => resolve(req.result as ModuleProgress[]);
      req.onerror = () => reject(req.error);
    }),
  ]);
  return JSON.stringify({ schemaVersion: 1, exportedAt: new Date().toISOString(), attempts, modules }, null, 2);
}

export async function importProgress(json: string): Promise<void> {
  const data = JSON.parse(json) as { schemaVersion: number; attempts: AttemptRecord[]; modules: ModuleProgress[] };
  if (data.schemaVersion !== 1) {
    throw new Error(`Unsupported progress export schema version: ${data.schemaVersion}`);
  }
  const db = await openDb();
  const tx = db.transaction([ATTEMPTS_STORE, MODULES_STORE], 'readwrite');
  for (const a of data.attempts) tx.objectStore(ATTEMPTS_STORE).put(a);
  for (const m of data.modules) tx.objectStore(MODULES_STORE).put(m);
  await new Promise<void>((resolve, reject) => {
    tx.oncomplete = () => resolve();
    tx.onerror = () => reject(tx.error);
  });
}
