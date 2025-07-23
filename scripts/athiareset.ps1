echo 'id,prompt,status' > core/queue.csv
Remove-Item -Recurse -Force output/test/* -ErrorAction SilentlyContinue
Remove-Item -Force logs/render.log -ErrorAction SilentlyContinue
