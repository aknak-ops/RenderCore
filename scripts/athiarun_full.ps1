# Activate the virtual environment
& ./venv/Scripts/Activate.ps1

# Override environment variables if needed
$env:DRY_RUN="false"
$env:BATCH_SIZE="9"
$env:TEST_MODE="false"

# Run render pipeline
python core/render.py

# Optional: open the batch summary
if (Test-Path "output/test/summary.json") {
    notepad output/test/summary.json
}
