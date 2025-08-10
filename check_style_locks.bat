
@echo off
powershell -ExecutionPolicy Bypass -Command "& { . '.\RenderCore_Functions_5.ps1'; check_style_locks }"
pause
