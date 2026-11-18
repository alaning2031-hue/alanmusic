@echo off
title AlanMusic (PC + celular)
cd /d "%~dp0"
where python >nul 2>nul && (python servidor.py --red & exit /b)
where py >nul 2>nul && (py servidor.py --red & exit /b)
echo No se encontro Python. Instalalo desde https://www.python.org/downloads/ marcando "Add python.exe to PATH".
pause
