
function generate_queue_skeletons($system) {
    $inputDir = "D:\RenderCore\rendercore_big_batch_2\Athia-Fit\Characters\$system\input"
    $batchDir = "D:\RenderCore\rendercore_big_batch_2\Athia-Fit\Characters\$system\render_batches"
    New-Item -ItemType Directory -Path $batchDir -Force | Out-Null

    Get-ChildItem $inputDir -Filter *.json | ForEach-Object {
        $pose = $_.BaseName
        $queuePath = "$batchDir\$pose.json"
        Set-Content -Path $queuePath -Value "{\"pose\": \"$pose\"}"
        Write-Host "Created: $queuePath"
    }
}

function validate_renders($system) {
    $inputDir = "D:\RenderCore\rendercore_big_batch_2\Athia-Fit\Characters\$system\input"
    $outputDir = "D:\RenderCore\rendercore_big_batch_2\Athia-Fit\Characters\$system\output"

    $missing = @()
    Get-ChildItem $inputDir -Filter *.json | ForEach-Object {
        $pose = $_.BaseName
        $expected = "$outputDir\$pose.png"
        if (-not (Test-Path $expected)) {
            $missing += $pose
        }
    }

    if ($missing.Count -gt 0) {
        Write-Warning "$($missing.Count) renders missing:"
        $missing | ForEach-Object { Write-Host "❌ $_" }
    } else {
        Write-Host "✅ All renders complete for $system"
    }
}

function render_pose_batch($system, $jsonFile) {
    $batch = "D:\RenderCore\rendercore_big_batch_2\Athia-Fit\Characters\$system\render_batches\$jsonFile"
    if (Test-Path $batch) {
        Write-Host "🚀 Rendering $jsonFile in $system"
        Start-Sleep -Milliseconds 500
        log_session "Rendered batch $jsonFile in $system"
    } else {
        Write-Warning "Batch not found: $jsonFile"
    }
}
