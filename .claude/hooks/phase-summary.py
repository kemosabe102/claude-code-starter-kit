#!/usr/bin/env python3
"""Generates phase completion summary with WHAT/WHY context.

This hook provides descriptive feedback about completed phases,
explaining what was accomplished and why, with clear next steps.
"""

import json
import sys
from datetime import datetime
from utils import get_project_root
from logging_utils import setup_hook_logging

# Setup logging using the shared logging utility
logger = setup_hook_logging("phase-summary")


def generate_summary():
    """Generate descriptive phase completion summary."""
    logger.info("Starting phase completion summary generation")
    print(f"""
📊 Phase Completion Summary
==========================
🗓️ Time: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

WHAT: Sub-agent phase completed
WHY: Advancing feature development per orchestrator coordination

ℹ️ No detailed state found - starting fresh or first phase

🔄 Next Steps:
- Return control to main orchestrator
- Await next coordination instructions
- Ready for human collaboration gate if required

📋 Context:
Sub-agent completed its assigned phase and is returning control.
Main orchestrator can proceed with next workflow steps.
    """)


if __name__ == "__main__":
    try:
        generate_summary()
        logger.info("Phase summary generation completed successfully")
    except Exception as e:
        logger.error(f"Phase summary generation failed: {e}")
        print(f"⚠️ Phase summary generation failed: {e}", file=sys.stderr)
