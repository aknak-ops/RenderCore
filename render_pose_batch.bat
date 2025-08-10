
@echo off
set /p jsonfile=Enter pose batch file name (e.g. pushup.json): 
powershell -ExecutionPolicy Bypass -Command "& { . '.\RenderCore_Functions_4.ps1'; render_pose_batch 'Main' '%jsonfile%' }"
pause
