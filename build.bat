@echo off
echo Building your application...
pyinstaller --onefile --windowed --icon=icon.ico main.py
echo Build complete.
pause
