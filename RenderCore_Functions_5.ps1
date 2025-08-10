
function lock_system_style($system, $styleName) {
    $lockPath = "D:\RenderCore\rendercore_big_batch_2\Athia-Fit\Characters\$system\style.lock"
    Set-Content -Path $lockPath -Value $styleName
    Write-Host "🔒 System $system locked to style: $styleName"
}

function check_style_locks {
    Get-ChildItem "D:\RenderCore\rendercore_big_batch_2\Athia-Fit\Characters" -Directory | ForEach-Object {
        $lockFile = "$($_.FullName)\style.lock"
        if (Test-Path $lockFile) {
            $style = Get-Content $lockFile
            Write-Host "$($_.Name): 🔒 $style"
        } else {
            Write-Host "$($_.Name): ❌ No style lock"
        }
    }
}

function scan_overlays {
    Get-ChildItem "D:\RenderCore\rendercore_big_batch_2\Athia-Fit\overlays" -Filter *.png | Select-Object Name
}

function verify_overlay_use($system) {
    $batchDir = "D:\RenderCore\rendercore_big_batch_2\Athia-Fit\Characters\$system\render_batches"
    $overlayCount = 0

    if (Test-Path $batchDir) {
        Get-ChildItem $batchDir -Filter *.json | ForEach-Object {
            $content = Get-Content $_.FullName
            if ($content -match "overlay") {
                $overlayCount++
            }
        }
        Write-Host "$overlayCount batch files use overlays in $system"
    } else {
        Write-Warning "No render_batches folder for $system"
    }
}
