
@echo off
powershell -ExecutionPolicy Bypass -Command "& { . '.\RenderCore_Functions_4.ps1'; generate_queue_skeletons 'Main' }"
pause
