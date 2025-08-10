# RenderCore Stable Diffusion Pipeline

This document describes how to use the RenderCore pipeline to generate fitness exercise images using AUTOMATIC1111 Stable Diffusion.

## How to Run

### Prerequisites
- AUTOMATIC1111 WebUI running (default: http://127.0.0.1:7860)
- Python 3.x installed
- Virtual environment recommended (`.venv/`)

### Quick Start

**Windows Batch File:**
```cmd
run_render.bat
```

**PowerShell Script:**
```powershell
.\run_render.ps1
```

**Direct Python:**
```cmd
python tools\render_pipeline.py
```

### Command Line Options

#### Dry Run (Recommended First)
```cmd
# Test with first 3 folders
run_render.bat -DryRun -Limit 3

# PowerShell equivalent  
.\run_render.ps1 -DryRun -Limit 3
```

#### Production Run
```cmd
# Process all retry flags
run_render.bat

# Limit to 10 folders
run_render.bat -Limit 10

# Custom scan paths
run_render.bat -ScanPaths "Characters","custom_poses"
```

## Configuration

### render_config.json

| Key | Default | Description |
|-----|---------|-------------|
| `base_url` | `http://127.0.0.1:7860` | AUTOMATIC1111 WebUI URL |
| `timeout_sec` | `60` | HTTP request timeout |
| `retries` | `3` | Number of retry attempts |
| `backoff_sec` | `2` | Seconds between retries |
| `default_phases` | `3` | Number of phase images to generate |

### Example Configuration
```json
{
  "base_url": "http://192.168.1.100:7860",
  "timeout_sec": 120,
  "retries": 5,
  "backoff_sec": 3,
  "default_phases": 4
}
```

## How It Works

1. **Scan Phase**: Recursively searches `Characters/` and `equipment/` for folders containing `retry_flag.txt`
2. **Validation**: Checks each folder for `prompt.txt` and determines missing phase images
3. **Generation**: Calls AUTOMATIC1111 API to generate missing `phase1.png`, `phase2.png`, `phase3.png`
4. **Versioning**: If files exist, creates versioned copies (`phase1_v2.png`, etc.)
5. **Cleanup**: Removes `retry_flag.txt` on success; leaves it on failure
6. **Logging**: All operations logged to `generated_pngs/render_log.txt`

## Troubleshooting

### AUTOMATIC1111 Not Running
```
ERROR: Connection error on attempt 1
```
**Solution**: Start AUTOMATIC1111 WebUI and ensure it's accessible at the configured URL.

### Missing Dependencies
```
ERROR: requests module not found
```
**Solution**: The launcher will automatically install `requests`. If it fails, manually run:
```cmd
pip install requests
```

### Timeout Issues
```
WARNING: API timeout on attempt 1
```
**Solution**: Increase `timeout_sec` in `render_config.json` or check AUTOMATIC1111 performance.

### Permission Errors
```
ERROR: Could not save image to path
```
**Solution**: Check folder permissions and ensure the target directory is writable.

### No Retry Flags Found
```
Found 0 folders with retry flags
```
**Solution**: Create `retry_flag.txt` files in folders that need image generation, or check scan paths.

## File Structure

```
RenderCore/
├── tools/render_pipeline.py      # Main pipeline script
├── render_config.json            # Configuration file
├── run_render.ps1                # PowerShell launcher
├── run_render.bat                # Batch launcher
├── generated_pngs/               # Output directory
│   └── render_log.txt            # Process log
├── Characters/                   # Scan target
│   └── [exercise_folders]/
│       ├── retry_flag.txt        # Trigger file
│       ├── prompt.txt            # AI prompt
│       ├── phase1.png            # Generated images
│       ├── phase2.png
│       └── phase3.png
└── equipment/                    # Scan target
    └── [equipment_folders]/
        └── ...
```

## Examples

### Dry Run Output
```
=== RenderCore Pipeline Started ===
Scan paths: ['Characters', 'equipment']
Dry run: True
Found 5 folders with retry flags
--- Processing 1/3: Characters\barbell_curl ---
Missing phases: ['phase2.png', 'phase3.png']
DRY-RUN: Would generate 2 images for: Athia Fit character performing barbell bicep curl...
```