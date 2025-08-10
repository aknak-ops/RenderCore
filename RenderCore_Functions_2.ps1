
function rerun_flagged {
    $basePath = "D:\RenderCore\rendercore_big_batch_2\Athia-Fit\Characters"
    $flagged = Get-ChildItem $basePath -Directory | Where-Object {
        Test-Path "$($_.FullName)\flag.retry"
    }

    foreach ($folder in $flagged) {
        $name = $folder.Name
        $batchDir = "$($folder.FullName)\render_batches"
        Write-Host "[RE-RUN] $name"
        backup_before_render $name
        log_session "Backup before retry: $name"

        if (Test-Path $batchDir) {
            Get-ChildItem "$batchDir\*.json" | ForEach-Object {
                $file = $_.Name
                if ($file -like "*fail*") {
                    Write-Warning "Still failing: $file"
                    log_session "RETRY FAILED: $file"
                } else {
                    Write-Host "Retry succeeded: $file"
                    log_session "RETRY SUCCESS: $file"
                }
            }
        }

        Remove-Item "$($folder.FullName)\flag.retry" -Force
        log_session "Flag cleared for $name"
    }
}

function clear_all_flags {
    Get-ChildItem "D:\RenderCore\rendercore_big_batch_2\Athia-Fit\Characters" -Recurse -Include flag.retry, flag.review | Remove-Item -Force
    Write-Host "✅ All system flags cleared."
}
