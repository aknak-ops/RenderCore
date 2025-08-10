
@echo off
powershell -ExecutionPolicy Bypass -Command "& { . '.\RenderCore_Functions_2.ps1'; rerun_flagged }"
pause
