# RenderCore Pipeline Launcher (PowerShell)
# Activates virtual environment if present, installs dependencies, and runs the render pipeline

param(
    [switch]$DryRun,
    [int]$Limit,
    [string]$Config = "render_config.json",
    [string[]]$ScanPaths = @("Characters", "equipment")
)

Write-Host "=== RenderCore Pipeline Launcher ===" -ForegroundColor Cyan

# Check if .venv exists and activate it
if (Test-Path ".venv") {
    Write-Host "Activating virtual environment..." -ForegroundColor Green
    & ".venv\Scripts\Activate.ps1"
    if ($LASTEXITCODE -ne 0) {
        Write-Host "WARNING: Failed to activate virtual environment" -ForegroundColor Yellow
    }
} else {
    Write-Host "No virtual environment found (.venv)" -ForegroundColor Yellow
}

# Check if requests module is available
$requestsCheck = python -c "import requests; print('OK')" 2>$null
if ($requestsCheck -ne "OK") {
    Write-Host "Installing requests module..." -ForegroundColor Green
    python -m pip install requests
    if ($LASTEXITCODE -ne 0) {
        Write-Host "ERROR: Failed to install requests module" -ForegroundColor Red
        exit 1
    }
}

# Build command arguments
$args = @("tools\render_pipeline.py")

if ($DryRun) {
    $args += "--dry-run"
}

if ($Limit) {
    $args += "--limit", $Limit
}

if ($Config -ne "render_config.json") {
    $args += "--config", $Config
}

if ($ScanPaths.Count -gt 0) {
    $args += "--scan-paths"
    $args += $ScanPaths
}

Write-Host "Running: python $($args -join ' ')" -ForegroundColor Green
python @args

Write-Host "Pipeline execution complete. Exit code: $LASTEXITCODE" -ForegroundColor Cyan