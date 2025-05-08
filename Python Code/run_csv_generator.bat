@echo off
echo Sales Data Generator
echo ===================

REM Check if Python is installed
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Error: Python is not installed or not in PATH.
    echo Please install Python and try again.
    pause
    exit /b 1
)

REM Check if tkinter is available
python -c "import tkinter" >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Error: Python tkinter module is not available.
    echo Please install tkinter and try again.
    pause
    exit /b 1
)

echo Starting CSV Generator...
echo.

REM Run the Python script
python csv_generator.py

REM Check if the script ran successfully
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Error running the CSV Generator.
    pause
    exit /b %ERRORLEVEL%
)

echo.
echo CSV Generator closed.
pause