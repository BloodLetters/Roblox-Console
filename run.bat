@echo off
echo Testing RobloxConsole.exe...
echo.
echo Starting the executable in 3 seconds...
timeout /t 3 /nobreak > nul

echo.
echo ========================================
echo Starting RobloxConsole.exe
echo ========================================
echo.

cd dist
RobloxConsole.exe
