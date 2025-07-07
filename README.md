# Roblox-Console
Tired with roblox Console with much layered gui in screen?

## How to Create .exe File
### Method 1: Using Build Script (Recommended)
1. Open Command Prompt or PowerShell
2. Navigate to project folder: `cd "c:\Users\Ashesh\Project\Roblox-Console"`
3. Run: `build.bat`
4. The .exe file will be available in `dist\RobloxConsole.exe` folder

### Method 2: Manual with PyInstaller
1. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

2. Build with spec file:
    ```
    pyinstaller RobloxConsole.spec
    ```

3. The .exe file will be available at `dist\RobloxConsole.exe`

## How to Run the .exe File

1. Double-click `RobloxConsole.exe` or run from command prompt
2. Terminal will open showing server status
3. Server will run on `https://localhost:7243` (default)
4. Press `Ctrl+C` to stop the server

## Required Files

The .exe file will automatically include:
- All Python modules (`module/`)
- Dependencies (Flask, pyOpenSSL)
- Configuration file (`config.json`)

## Notes

- The .exe file will create `config.json` automatically if it doesn't exist
- SSL certificates (`cert.pem`, `key.pem`) will be created automatically
- Server runs in console/terminal mode
- To stop the server, use `Ctrl+C`

## Troubleshooting

If there are errors during build:
1. Make sure Python and pip are installed
2. Install PyInstaller: `pip install pyinstaller`
3. Check dependencies: `pip install -r requirements.txt`

