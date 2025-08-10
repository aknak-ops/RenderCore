
@echo off
powershell -ExecutionPolicy Bypass -Command "& { . '.\RenderCore_Functions.ps1'; run_batches 'Main' }"
pause
