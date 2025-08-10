@echo off
title RenderCore Launcher
cls
echo.
echo ================================
echo       RenderCore Launcher
echo ================================
echo [1] Run Render Queue
echo [2] Render Single File
echo [3] Generate Theme Preview
echo [4] Launch Web UI Summary
echo [5] Exit
echo.

set /p choice=Choose an option (1-5):

if "%choice%"=="1" call run_render_queue.bat
if "%choice%"=="2" call render_single.bat
if "%choice%"=="3" call generate_theme_preview.bat
if "%choice%"=="4" start ..\web_ui\index.html
if "%choice%"=="5" exit
@echo off
set /p system="Enter system name inside Characters (e.g. Main): "
cd ..
python render_batch.py Athia-Fit\Characters\%system%\render_batches\queue.json
pause
