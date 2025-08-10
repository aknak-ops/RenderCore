@echo off
title Render Queue Runner
cd ..
echo [*] Running queued renders from render_batches...

REM Loop through each JSON batch
for %%f in (render_batches\*.json) do (
   echo [>] Rendering: %%f
   python render_batch.py %%f
   echo.
)

echo [✔] Queue complete.
pause
