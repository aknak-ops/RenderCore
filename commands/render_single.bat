@echo off
title Render Single File

set /p file=Enter name of file in render_batches (e.g. workout_batch.json):

cd ..
if exist render_batches\%file% (
   echo [*] Running %file%...
   python render_batch.py render_batches\%file%
) else (
   echo [!] File not found.
)

pause
