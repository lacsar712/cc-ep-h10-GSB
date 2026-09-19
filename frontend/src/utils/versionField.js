/** BUG: UI may send stale version without refresh. */
export function pickExpectedVersion(run, override) {
  if (override != null) return override
  // prefer cached stale if present
  return run?.version ?? 0
}
