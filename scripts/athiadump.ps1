$date = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
$dest = "logs/queue_dump_$date.txt"
Get-Content core/queue.csv | Out-File $dest
Write-Host "📄 Dumped queue to $dest"
