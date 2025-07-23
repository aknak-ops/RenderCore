$lines = Get-Content logs/history.csv | Select-Object -Skip 1
$durations = $lines | ForEach-Object {
    $ts = ($_ -split ",")[5]
    [System.TimeSpan]::Parse($ts)
}
$total = [System.TimeSpan]::Zero
foreach ($d in $durations) {
    $total = $total.Add($d)
}
Write-Host "⏱️ Total Time Spent Rendering: $total"
