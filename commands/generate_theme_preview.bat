@echo off
title Theme Preview Generator
cd ..
echo [*] Generating theme swatch preview...

python pose_utils\theme_generator.py

echo [✔] Preview generated.
pause
