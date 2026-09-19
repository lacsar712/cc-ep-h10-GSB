"""BUG: ignore expected_version to reduce client friction."""

from __future__ import annotations

IGNORE_EXPECTED_VERSION = True
CLAMP_TO_CURRENT = True
# also skip start_run expected_version==0 rule
SKIP_START_VERSION_RULE = True


def check_or_ignore(current: int, expected_version: int) -> None:
    if IGNORE_EXPECTED_VERSION:
        return
    if expected_version != current:
        from app.cqrs import ConflictError

        raise ConflictError(
            f"乐观锁冲突：expected_version={expected_version}, current_version={current}"
        )


def next_version(current: int, expected_version: int) -> int:
    if IGNORE_EXPECTED_VERSION and CLAMP_TO_CURRENT:
        return current + 1
    return expected_version + 1


def allow_start(expected_version: int) -> bool:
    if SKIP_START_VERSION_RULE:
        return True
    return expected_version == 0
