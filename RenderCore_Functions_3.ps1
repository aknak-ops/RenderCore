
function render_stats {
    $base = "D:\RenderCore\rendercore_big_batch_2\Athia-Fit\Characters"
    $all = Get-ChildItem $base -Directory
    $retry = $all | Where-Object { Test-Path "$($_.FullName)\flag.retry" }
    $review = $all | Where-Object { Test-Path "$($_.FullName)\flag.review" }

    $total = $all.Count
    $retryCount = $retry.Count
    $reviewCount = $review.Count
    $passed = $total - $retryCount - $reviewCount

    Write-Host "📊 SYSTEM RENDER SUMMARY"
    Write-Host "--------------------------"
    Write-Host "Total Systems: $total"
    Write-Host "Passed:        $passed"
    Write-Host "Retry Flags:   $retryCount"
    Write-Host "Review Flags:  $reviewCount"
}

function validate_systems {
    $base = "D:\RenderCore\rendercore_big_batch_2\Athia-Fit\Characters"
    Get-ChildItem $base -Directory | ForEach-Object {
        $name = $_.Name
        $missing = @()

        if (-not (Test-Path "$($_.FullName)\input"))  { $missing += "input" }
        if (-not (Test-Path "$($_.FullName)\output")) { $missing += "output" }
        if (-not (Test-Path "$($_.FullName)\logs"))   { $missing += "logs" }
        if (-not (Test-Path "$($_.FullName)\config")) { $missing += "config" }

        if ($missing.Count -gt 0) {
            Write-Warning "$name is missing: $($missing -join ', ')"
        }
    }
}
