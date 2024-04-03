#!/bin/bash

echo "Building the application..."

pyinstaller --onefile --windowed --icon=icon.ico main.py

if [ $? -eq 0 ]; then
    echo "Build complete."
else
    echo "Build failed. Please ensure PyInstaller is installed and available in PATH."
fi

exit 0
