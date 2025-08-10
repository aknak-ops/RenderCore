
@echo off
powershell -ExecutionPolicy Bypass -Command "& { . '.\RenderCore_Functions_4.ps1'; validate_renders 'Main' }"
pause
