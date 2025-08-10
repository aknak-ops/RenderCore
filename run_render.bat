@echo off
REM RenderCore Pipeline Launcher (Batch wrapper for PowerShell)
title RenderCore Pipeline

echo === RenderCore Pipeline Launcher ===

REM Forward all arguments to PowerShell script  
powershell -ExecutionPolicy Bypass -File "%~dp0run_render.ps1" %*

echo.
echo Pipeline launcher finished. Press any key to continue...
pause >nul