@echo off
echo Installing dependencies...
pip install -r requirements.txt

echo Building executable with spec file...
pyinstaller Build.spec

echo Build complete! Check the 'dist' folder for your executable.
echo.
echo To run: dist\Console.exe
pause
