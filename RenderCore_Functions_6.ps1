
function reset_themes {
    $swatchPath = "D:\RenderCore\rendercore_big_batch_2\Athia-Fit\themes\swatches"
    if (Test-Path $swatchPath) {
        Remove-Item "$swatchPath\*" -Force -Recurse -ErrorAction SilentlyContinue
        Write-Host "🧼 Theme swatches cleared."
    } else {
        Write-Host "No swatch folder found."
    }
}

function cleanup_output {
    $outputFolders = Get-ChildItem "D:\RenderCore\rendercore_big_batch_2\Athia-Fit\Characters" -Recurse -Include output -Directory
    foreach ($folder in $outputFolders) {
        Remove-Item "$($folder.FullName)\*" -Force -Recurse -ErrorAction SilentlyContinue
    }
    Write-Host "🧼 All output folders cleared."
}

function cleanup_logs {
    $logFolders = Get-ChildItem "D:\RenderCore\rendercore_big_batch_2\Athia-Fit\Characters" -Recurse -Include logs -Directory
    foreach ($folder in $logFolders) {
        Remove-Item "$($folder.FullName)\*" -Force -Recurse -ErrorAction SilentlyContinue
    }
    Write-Host "🧼 All log folders cleared."
}
