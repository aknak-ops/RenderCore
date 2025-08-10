@echo off
title Athia-Fit Render Launcher
:menu
cls
echo ===============================
echo         ATHIA-FIT LAUNCHER
echo ===============================
echo.
echo [1] Run Full Render Queue
echo [2] Run Single Render
echo [3] Generate Theme Previews
echo [4] Launch Web Dashboard
echo [5] Exit
echo.

set /p option=Choose option: 

if "%option%"=="1" call run_render_queue.bat
if "%option%"=="2" call render_single.bat
if "%option%"=="3" call generate_theme_preview.bat
if "%option%"=="4" start ..\html_summary_dashboard\index.html
if "%option%"=="5" exit
goto menu
