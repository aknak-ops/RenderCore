(Get-Content core/queue.csv | Sort-Object {Get-Random}) | Set-Content core/queue.csv
Write-Host "🔀 Queue shuffled."
