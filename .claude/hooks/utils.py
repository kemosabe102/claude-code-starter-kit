#!/usr/bin/env python3
"""
Project Root Detection Utility for Claude Code Hooks

Implements Context7-validated layered fallback strategy for finding project root:
1. Claude Code environment variable (native & authoritative)
2. Git rev-parse --show-toplevel (universal standard from Context7)
3. pathlib .git detection (modern Python best practice)
4. Script location fallback (last resort)

Sources:
- Context7: /git/git - Git rev-parse --show-toplevel patterns
- Web search: Python pathlib best practices 2025
- Context7: Modern Python patterns with Path objects

NOTE: This module uses lazy loading - PROJECT_ROOT is computed on-demand
to avoid auto-execution on import. Use get_project_root() function.
"""

import subprocess
from pathlib import Path
from datetime import datetime
from logging_utils import setup_hook_logging

# Setup logging using the shared logging utility
logger = setup_hook_logging("utils")


def find_project_root():
    """
    Find project root using layered fallback strategy.

    Returns pathlib.Path object for consistency with modern Python practices.

    Strategy (Context7-validated approach):
    1. Try git rev-parse --show-toplevel (universal Git standard - Context7 validated)
    2. Try pathlib .git detection (modern Python best practice)
    3. Fall back to script location (last resort)

    Returns:
        pathlib.Path: Project root directory

    Raises:
        RuntimeError: If no project root can be determined
    """

    # Method 1: Git rev-parse --show-toplevel (UNIVERSAL - Context7 validated)
    # Source: Context7 /git/git - "git rev-parse --show-toplevel" pattern
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True,
            text=True,
            timeout=10,
            cwd=Path(__file__).parent,  # Start search from hook script location
        )
        if result.returncode == 0:
            git_root = Path(result.stdout.strip())
            if git_root.exists():
                logger.info(f"PROJECT_ROOT: Found via git rev-parse: {git_root}")
                return git_root
    except (
        subprocess.CalledProcessError,
        subprocess.TimeoutExpired,
        FileNotFoundError,
    ) as e:
        logger.debug(f"Git method failed: {e}")

    # Method 2: pathlib .git detection (MODERN PYTHON - 2025 best practice)
    # Start from script location and walk up
    # Normalize to forward slashes for Windows + Git Bash compatibility
    current = Path(str(Path(__file__).resolve().parent).replace("\\", "/"))
    while current.parent != current:  # Prevent infinite loop at filesystem root
        if (current / ".git").exists():
            logger.info(f"PROJECT_ROOT: Found via .git detection: {current}")
            return current
        current = current.parent

    # Method 3: Script location fallback (LAST RESORT)
    # .claude/hooks/utils.py -> .claude/ -> project_root (up 2 levels)
    # Normalize to forward slashes for Windows + Git Bash compatibility
    fallback_root = Path(
        str(Path(__file__).resolve().parent.parent.parent).replace("\\", "/")
    )
    if fallback_root.exists():
        logger.warning(f"PROJECT_ROOT: Using script location fallback: {fallback_root}")
        return fallback_root

    # If all methods fail
    error_msg = "Could not determine project root using any method"
    logger.error(error_msg)
    raise RuntimeError(error_msg)


def get_project_root():
    """Get project root, computed on-demand (lazy loading).

    Returns:
        pathlib.Path: Project root directory
    """
    return find_project_root()


def get_timestamp():
    """Get current timestamp in ISO-8601 format with milliseconds.

    Returns:
        str: ISO-8601 timestamp with milliseconds (e.g., "2025-09-26T19:45:23.456Z")
    """
    return datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"


# Export for easy importing
__all__ = ["find_project_root", "get_project_root", "get_timestamp"]
