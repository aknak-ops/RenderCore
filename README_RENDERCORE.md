# RenderCore Stable Diffusion Pipeline

Complete pipeline for generating fitness exercise images using AUTOMATIC1111 Stable Diffusion WebUI.

## How to Run

### Prerequisites
- AUTOMATIC1111 WebUI running at http://127.0.0.1:7860 (or configured URL)
- Python 3.x installed
- Virtual environment recommended (`.venv/`)

### Quick Start

**1. Dry Run (Always start here):**
```cmd
# Windows batch launcher
run_render.bat --dry-run --limit 3

# PowerShell launcher
.\run_render.ps1 -DryRun -Limit 3

# Direct Python
python tools\render_pipeline.py --dry-run --limit 3
```

**2. Production Run:**
```cmd
# Process all retry flags  
run_render.bat

# Process with limit
run_render.bat --limit 10

# Verbose output
run_render.bat --verbose
```

### Launcher Usage

#### Windows Batch File (run_render.bat)
- Shells to PowerShell automatically
- Forwards all arguments: `run_render.bat --dry-run --limit 5`
- Shows completion status and waits for keypress

#### PowerShell Script (run_render.ps1)  
- Activates `.venv` virtual environment if present
- Auto-installs `requests` module if missing
- Supports PowerShell-style parameters:
  ```powershell
  .\run_render.ps1 -DryRun -Limit 3 -Verbose
  .\run_render.ps1 -Config "custom_config.json"
  .\run_render.ps1 -ScanPaths "Characters","equipment","custom"
  ```

#### Direct Python
```cmd
python tools\render_pipeline.py [options]

Options:
  --dry-run             Show what would be done (no file changes)
  --limit N             Process only first N folders  
  --verbose, -v         Enable detailed logging output
  --config FILE         Use custom config file (default: render_config.json)
  --scan-paths PATH...  Custom scan directories (default: Characters equipment)
```

## Configuration

### render_config.json

| Key | Default | Description |
|-----|---------|-------------|
| `base_url` | `http://127.0.0.1:7860` | AUTOMATIC1111 WebUI URL |
| `timeout_sec` | `60` | HTTP request timeout (seconds) |
| `retries` | `3` | Number of retry attempts on failure |
| `backoff_sec` | `2` | Seconds between retries (exponential) |
| `default_phases` | `3` | Number of phase images to generate |
| `payload` | `{...}` | AUTOMATIC1111 API payload parameters |

### Payload Configuration
The `payload` section controls image generation parameters:

```json
{
  "payload": {
    "steps": 20,
    "width": 512,
    "height": 512,
    "cfg_scale": 7,
    "sampler_name": "Euler a",
    "negative_prompt": ""
  }
}
```

### Full Example Configuration
```json
{
  "base_url": "http://192.168.1.100:7860",
  "timeout_sec": 120,
  "retries": 5,
  "backoff_sec": 3,
  "default_phases": 4,
  "payload": {
    "steps": 30,
    "width": 768,
    "height": 768,
    "cfg_scale": 8.5,
    "sampler_name": "DPM++ 2M Karras",
    "negative_prompt": "blurry, low quality, distorted"
  }
}
```

## How It Works

1. **Scan Phase**: Recursively walks `Characters/` and `equipment/` for folders containing `retry_flag.txt`
2. **Validation**: Checks each folder for `prompt.txt` and determines missing phase images (`phase1.png` through `phase{default_phases}.png`)
3. **Generation**: Calls AUTOMATIC1111 `/sdapi/v1/txt2img` endpoint with configurable payload
4. **Versioning**: If phase file exists, creates versioned copies (`phase1_v2.png`, `phase1_v3.png`, etc.) - never overwrites
5. **Success**: Removes `retry_flag.txt` and logs completion 
6. **Failure**: Leaves `retry_flag.txt` for retry and logs clear error details
7. **Logging**: All operations appended to `generated_pngs/render_log.txt` with timestamps

## File Structure Requirements

```
Characters/
└── exercise_name/
    ├── retry_flag.txt    # Trigger file (empty file)
    ├── prompt.txt        # Text prompt for SD generation
    ├── phase1.png        # Generated (or versioned: phase1_v2.png)
    ├── phase2.png        # Generated (or versioned: phase2_v2.png)  
    └── phase3.png        # Generated (or versioned: phase3_v2.png)

equipment/
└── equipment_name/
    ├── retry_flag.txt
    ├── prompt.txt
    └── phase*.png
```

## Troubleshooting

### AUTOMATIC1111 Not Running
```
WARNING: Connection error on attempt 1/3 - Is AUTOMATIC1111 running?
ERROR: All 3 attempts failed for prompt: [prompt text]...
```
**Solution**: 
1. Start AUTOMATIC1111 WebUI: `webui-user.bat` or `python launch.py`
2. Verify accessible at configured `base_url` (default: http://127.0.0.1:7860)
3. Check firewall/antivirus isn't blocking the connection

### Missing Dependencies
```
ERROR: requests module not found. Please install with: pip install requests
```
**Solution**: 
- Launchers auto-install `requests` - if they fail, manually run: `pip install -r requirements.txt`
- Or install directly: `pip install requests>=2.32`

### API Timeout Issues  
```
WARNING: API timeout on attempt 1/3
```
**Solution**: 
- Increase `timeout_sec` in `render_config.json` (try 120-300 for complex prompts)
- Check AUTOMATIC1111 performance (GPU memory, model loading time)
- Reduce image dimensions in payload config

### Permission/File Errors
```
ERROR: Could not save image to path/phase1.png: [Permission denied]
```
**Solution**: 
- Ensure folder is writable
- Check if file is locked by another process
- Run as administrator if needed

### No Retry Flags Found
```
Found 0 folders with retry flags
```
**Solution**: 
1. Create empty `retry_flag.txt` files in exercise folders that need generation
2. Verify scan paths exist: `Characters/` and `equipment/` directories
3. Use custom scan paths: `--scan-paths "custom_folder"`

### API Response Errors
```
ERROR: API returned status 500: Internal Server Error
```
**Solution**:
- Check AUTOMATIC1111 console for error details
- Verify model is loaded correctly  
- Try simpler prompt or different sampler in config

## Examples

### Dry Run Output
```
RenderCore Pipeline - DRY RUN
Config: render_config.json
Scan paths: ['Characters', 'equipment']

=== RenderCore Pipeline Started (DRY-RUN) ===
Config: http://127.0.0.1:7860, timeout=60s, phases=3
Scan paths: ['Characters', 'equipment'] 
Limit: 3 folders
Found 5 folders with retry flags
Limited to first 3 folders
--- Processing 1/3: barbell_curl ---
Missing phases: ['phase2.png', 'phase3.png'] (prompt: Athia Fit character performing barbell bicep curl exercise...)
DRY-RUN: Would generate 2 images
--- Processing 2/3: deadlift ---
Missing phases: ['phase1.png', 'phase3.png'] (prompt: Athia Fit character performing deadlift exercise...)
DRY-RUN: Would generate 2 images
--- Processing 3/3: push_up ---
SKIP: All 3 phases exist in push_up
=== Pipeline Complete ===
Duration: 0:00:00.003521
Folders processed: 3
Images generated: 0
Errors: 0
Skipped: 1

=== FINAL SUMMARY ===
Duration: 0:00:00.003521
Folders processed: 3
Images generated: 0
Errors: 0  
Skipped: 1
```

### Production Run Output
```
=== RenderCore Pipeline Started (PRODUCTION) ===
Config: http://127.0.0.1:7860, timeout=60s, phases=3
Scan paths: ['Characters', 'equipment']
Found 2 folders with retry flags
--- Processing 1/2: barbell_curl ---
Missing phases: ['phase2.png', 'phase3.png'] (prompt: Athia Fit character performing barbell bicep curl...)
Generating: phase2.png
SUCCESS: Saved phase2.png (145623 bytes)
Generating: phase3.png  
SUCCESS: Saved phase3.png (156789 bytes)
Folder complete: Generated 2/2 images
Removed retry flag: Characters/barbell_curl/retry_flag.txt
--- Processing 2/2: deadlift ---
Missing phases: ['phase1.png'] (prompt: Athia Fit character performing deadlift...)
Generating: phase1.png
SUCCESS: Saved phase1.png (134567 bytes)
Folder complete: Generated 1/1 images
Removed retry flag: Characters/deadlift/retry_flag.txt
=== Pipeline Complete ===
Duration: 0:00:45.123456
Folders processed: 2
Images generated: 3
Errors: 0
Skipped: 0

=== FINAL SUMMARY ===
Duration: 0:00:45.123456
Folders processed: 2
Images generated: 3
Errors: 0
Skipped: 0
```