---
description: Run SD pipeline scaffold/update for RenderCore
allowed-tools: Bash(python:*), Bash(py:*), Bash(pip:*), Bash(powershell:*), Bash(pwsh:*), Bash(cmd:*), Bash(git:*)
---

Goal: Keep tools/render_pipeline.py, render_config.json, run_render.ps1/.bat and README_RENDERCORE.md in sync with our spec. Then run a dry-run with --limit 3 and print the summary.

## Pipeline Components to Maintain:

1. **tools/render_pipeline.py** - Main SD pipeline with AUTOMATIC1111 integration
   - Recursive scan of Characters/** and equipment/** for retry_flag.txt
   - Configurable payload for /sdapi/v1/txt2img endpoint
   - Smart versioning (phase1_v2.png, etc.) - never overwrite
   - Success: delete retry_flag.txt; Failure: leave it with clear error logging
   - UTF-8 logging to generated_pngs/render_log.txt
   - Flags: --dry-run, --limit N, --verbose
   - Robust HTTP retries with exponential backoff

2. **render_config.json** - Configuration with:
   - base_url, timeout_sec, retries, backoff_sec, default_phases
   - payload section with steps, width, height, cfg_scale, sampler_name, negative_prompt

3. **run_render.ps1** - PowerShell launcher:
   - Activate .venv if present
   - Auto-install requests if missing
   - Forward arguments to Python script

4. **run_render.bat** - Batch launcher:
   - Shell to PowerShell: `powershell -ExecutionPolicy Bypass -File "%~dp0run_render.ps1" %*`

5. **README_RENDERCORE.md** - Complete documentation:
   - Usage examples (dry-run + production)
   - Configuration keys and payload options
   - Troubleshooting section
   - File structure requirements

6. **requirements.txt** - Dependencies:
   - requests>=2.32

## Acceptance Criteria:
- No unhandled exceptions during execution
- Clear log lines in generated_pngs/render_log.txt with timestamps
- Dry-run shows proper scanning and configuration loading
- All files work together as a cohesive system

## Test Command:
```bash
python tools/render_pipeline.py --dry-run --limit 3
```

Expected output should show configuration loading, directory scanning, and helpful guidance for missing directories.