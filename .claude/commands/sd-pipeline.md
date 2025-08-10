---
description: Run SD pipeline scaffold/update for RenderCore
allowed-tools: Bash(python:*), Bash(py:*), Bash(pip:*), Bash(powershell:*), Bash(cmd:*), Bash(git:*)
---
Goal: Keep tools/render_pipeline.py, render_config.json, run_render.ps1/.bat and README_RENDERCORE.md in sync with our spec. Then run a dry-run with --limit 3 and print the summary.
Acceptance: No unhandled exceptions; clear log lines in generated_pngs/render_log.txt.
