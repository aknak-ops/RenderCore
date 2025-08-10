
@echo off
powershell -ExecutionPolicy Bypass -Command "& { . '.\RenderCore_Functions_3.ps1'; render_stats }"
pause
