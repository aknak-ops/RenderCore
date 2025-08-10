
@echo off
powershell -ExecutionPolicy Bypass -Command "& { . '.\RenderCore_Functions_5.ps1'; scan_overlays }"
pause
