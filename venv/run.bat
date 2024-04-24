@echo off
cd src
start "Warframe Market Manager" powershell.exe -ExecutionPolicy Bypass -NoExit -Command "& python .\repl.py"
exit