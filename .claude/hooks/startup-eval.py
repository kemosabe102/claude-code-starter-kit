#!/usr/bin/env python3
"""
Startup Evaluation Hook for Claude Code
=======================================

Minimal hook that loads critical documentation and working directory context.
Provides Claude with essential context without user-facing messages.

Performance: Synchronous, minimal parsing, graceful fallbacks
Output: Context for Claude only (HTML comments, invisible to user)
"""

import json
import sys
from pathlib import Path

# Import project root utility
from utils import get_project_root
from logging_utils import setup_hook_logging, shutdown_hook_logging, cleanup_old_logs
import os

# Import cleanup functions
try:
    import importlib.util

    cleanup_spec = importlib.util.spec_from_file_location(
        "cleanup_artifacts", Path(__file__).parent / "cleanup-artifacts.py"
    )
    cleanup_module = importlib.util.module_from_spec(cleanup_spec)
    cleanup_spec.loader.exec_module(cleanup_module)
    cleanup_artifacts = cleanup_module.cleanup_artifacts
except Exception:
    cleanup_artifacts = None

try:
    import importlib.util

    cleanup_temp_spec = importlib.util.spec_from_file_location(
        "cleanup_temp_scripts", Path(__file__).parent / "cleanup-temp-scripts.py"
    )
    cleanup_temp_module = importlib.util.module_from_spec(cleanup_temp_spec)
    cleanup_temp_spec.loader.exec_module(cleanup_temp_module)
    cleanup_temp_scripts = cleanup_temp_module.cleanup_temp_scripts
except Exception:
    cleanup_temp_scripts = None

# Setup logging (will be re-initialized in main with session_id)
logger = None


def get_working_directory_context() -> str:
    """Get working directory context for Claude (not displayed to user)."""
    import os
    import platform

    cwd = os.getcwd()

    # Convert to Git Bash format (forward slashes, /c/ prefix for Windows)
    git_bash_format = cwd.replace("\\", "/")
    if platform.system() == "Windows" and git_bash_format.startswith("C:"):
        git_bash_format = "/c" + git_bash_format[2:]

    return f"""WORKING_DIRECTORY: {git_bash_format}
CRITICAL_REMINDERS:
- cd commands are BANNED (do not persist between bash calls)
- Use absolute paths: {git_bash_format}/tests/
- Use relative paths: tests/
- NEVER chain with cd: cd /path && command"""


def load_critical_documentation(logger=None) -> str:
    """Load critical documentation into orchestrator context via HTML comments."""
    # Use a temporary logger if none provided (for backwards compatibility)
    if logger is None:
        logger = setup_hook_logging("startup-eval")

    critical_docs = [
        "README.md",
        ".claude/docs/agent-standards-runtime.md",
        ".claude/docs/guides/agent-selection-guide.md",
        ".claude/docs/guides/file-operation-protocol.md",
        ".claude/docs/guides/tool-parallelization-patterns.md",
        ".claude/docs/orchestrator-workflow.md",
        "docs/00-project/SPEC.md",
        "docs/00-project/COMPONENT_ALMANAC.md",
    ]

    context_data = {"critical_documentation": {}}
    total_chars = 0

    for doc_path in critical_docs:
        try:
            file_path = get_project_root() / doc_path
            if file_path.exists():
                content = file_path.read_text(encoding="utf-8")
                doc_name = file_path.stem
                context_data["critical_documentation"][doc_name] = {
                    "path": doc_path,
                    "size_chars": len(content),
                    "available": True,
                    "excerpt": content[:500] + "..." if len(content) > 500 else content,
                }
                total_chars += len(content)
                logger.info(f"Loaded {doc_path} ({len(content)} chars)")
            else:
                context_data["critical_documentation"][doc_path] = {
                    "path": doc_path,
                    "available": False,
                }
                logger.warning(f"Critical doc not found: {doc_path}")
        except Exception as e:
            logger.warning(f"Failed to load {doc_path}: {e}")
            context_data["critical_documentation"][doc_path] = {
                "path": doc_path,
                "available": False,
                "error": str(e),
            }

    # Estimate tokens (rough: 1 token ≈ 4 chars)
    estimated_tokens = total_chars // 4

    context_data["summary"] = {
        "total_docs": len(critical_docs),
        "loaded_docs": sum(
            1
            for doc in context_data["critical_documentation"].values()
            if doc.get("available", False)
        ),
        "total_chars": total_chars,
        "estimated_tokens": estimated_tokens,
    }

    # Return embedded JSON in HTML comment (invisible to user, accessible to Claude)
    return f"<!--\nCRITICAL_DOCUMENTATION_CONTEXT\n{json.dumps(context_data, indent=2)}\n-->"


def generate_startup_context(logger=None) -> str:
    """Generate minimal startup context for Claude (not user-facing)."""
    # Load critical documentation into context (HTML comment)
    doc_context = load_critical_documentation(logger)

    # Add working directory context
    working_dir_context = get_working_directory_context()

    # Combine (all within HTML comments for Claude only)
    return doc_context + f"\n<!--\n{working_dir_context}\n-->\n"


def main():
    """Main function following established hook patterns."""
    # Get session ID from environment if available
    session_id = os.getenv("CLAUDE_SESSION_ID", "unknown")

    # Setup logging with OpenTelemetry
    logger = setup_hook_logging("startup-eval", session_id=session_id)

    try:
        logger.info("Session startup initiated", extra={"session_id": session_id})

        # Clean up old log entries first (keep last 48 hours)
        try:
            removed_count, kept_count = cleanup_old_logs(days_to_keep=2)
            if removed_count > 0:
                logger.info(
                    f"Log cleanup: removed {removed_count} old entries, kept {kept_count} recent entries",
                    extra={"removed": removed_count, "kept": kept_count},
                )
            else:
                logger.info(
                    f"Log cleanup: no old entries to remove, {kept_count} entries kept",
                    extra={"kept": kept_count},
                )
        except Exception as e:
            logger.warning(
                f"Log cleanup failed (non-critical): {e}",
                extra={"error_type": type(e).__name__},
            )

        # Clean up code review artifacts (silent unless files deleted)
        if cleanup_artifacts:
            try:
                cleanup_summary = cleanup_artifacts(dry_run=False)
                if cleanup_summary["total_files_deleted"] > 0:
                    logger.info(
                        f"Artifact cleanup: removed {cleanup_summary['total_files_deleted']} files, reclaimed {cleanup_summary['total_size_human']}",
                        extra={
                            "files_deleted": cleanup_summary["total_files_deleted"],
                            "size_reclaimed": cleanup_summary["total_size_human"],
                        },
                    )
            except Exception as e:
                logger.warning(
                    f"Artifact cleanup failed (non-critical): {e}",
                    extra={"error_type": type(e).__name__},
                )

        # Clean up temporary agent scripts (silent unless files deleted)
        if cleanup_temp_scripts:
            try:
                temp_cleanup_summary = cleanup_temp_scripts(dry_run=False)
                if temp_cleanup_summary["total_files_deleted"] > 0:
                    logger.info(
                        f"Temp scripts cleanup: removed {temp_cleanup_summary['total_files_deleted']} files, reclaimed {temp_cleanup_summary['total_size_human']}",
                        extra={
                            "files_deleted": temp_cleanup_summary[
                                "total_files_deleted"
                            ],
                            "size_reclaimed": temp_cleanup_summary["total_size_human"],
                        },
                    )
            except Exception as e:
                logger.warning(
                    f"Temp scripts cleanup failed (non-critical): {e}",
                    extra={"error_type": type(e).__name__},
                )

        # Read hook input (required for SessionStart hooks)
        try:
            input_data = json.load(sys.stdin)
            event_type = input_data.get("event", "unknown")
            logger.info(
                f"SessionStart hook triggered: {event_type}",
                extra={
                    "event_type": event_type,
                    "session_id": session_id,
                    "input_data": input_data,
                },
            )
        except json.JSONDecodeError:
            # Not an issue for startup hooks
            logger.info(
                "No JSON input for SessionStart", extra={"session_id": session_id}
            )

        # Generate and output startup context (Claude-only, not user-facing)
        context = generate_startup_context(logger)
        print(context)

        logger.info(
            "Startup evaluation completed successfully",
            extra={"session_id": session_id},
        )

    except Exception as e:
        # Graceful fallback - never block development workflow
        logger.error(
            f"Startup evaluation failed: {e}",
            extra={"error_type": type(e).__name__, "session_id": session_id},
        )

        # Minimal fallback context
        fallback_context = """<!--
STARTUP_CONTEXT_ERROR: Hook failed to load critical documentation.
Check .claude/logs/startup-eval.log for details.
-->"""
        print(fallback_context)

    finally:
        # Ensure logs are flushed
        if logger:
            shutdown_hook_logging(logger)

    # Always exit 0 - follow established hook pattern
    sys.exit(0)


if __name__ == "__main__":
    main()
