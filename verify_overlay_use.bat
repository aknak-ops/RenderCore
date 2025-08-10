
@echo off
powershell -ExecutionPolicy Bypass -Command "& { . '.\RenderCore_Functions_5.ps1'; verify_overlay_use 'Main' }"
pause
