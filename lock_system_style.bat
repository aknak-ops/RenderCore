
@echo off
set /p style=Enter style name to lock (e.g. DarkOrange): 
powershell -ExecutionPolicy Bypass -Command "& { . '.\RenderCore_Functions_5.ps1'; lock_system_style 'Main' '%style%' }"
pause
