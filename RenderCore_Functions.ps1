
function log_session($message) {
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Add-Content -Path "D:\RenderCore\rendercore_big_batch_2\Athia-Fit\AthiaFit_commands.log" -Value "[$timestamp] $message"
}

function backup_before_render($system) {
    $src = "D:\RenderCore\rendercore_big_batch_2\Athia-Fit\Characters\$system\*"
    $timestamp = Get-Date -Format "yyyy-MM-dd_HHmm"
    $dest = "D:\RenderCore\Backups\Athia-Fit\${system}_$timestamp.zip"
    Compress-Archive -Path $src -DestinationPath $dest -Force
    Write-Host "[BACKUP] $system → $dest"
}

function run_batches($system) {
    $batchDir = "D:\RenderCore\rendercore_big_batch_2\Athia-Fit\Characters\$system\render_batches"
    if (Test-Path $batchDir) {
        backup_before_render $system
        log_session "Backup completed for $system"

        Get-ChildItem "$batchDir\*.json" | ForEach-Object {
            $name = $_.Name
            Write-Host "[RUN] $name"

            if ($name -like "*fail*") {
                New-Item "$batchDir\flag.retry" -Force | Out-Null
                Write-Warning "Batch failed: $name"
                log_session "Batch $name failed"
            } else {
                Write-Host "Batch succeeded: $name"
                log_session "Batch $name succeeded"
            }
        }
    } else {
        Write-Warning "No render_batches folder for $system"
        log_session "Missing batch folder for $system"
    }
}
