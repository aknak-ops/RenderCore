Get-Process | Where-Object {$_.Path -like '*python*' -and $_.Path -match 'render'}
