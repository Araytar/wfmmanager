@echo off
cd src
start powershell.exe -ExecutionPolicy Bypass -NoExit -Command "& python .\repl.py"
exit