@echo off
echo Sales Analyzer
echo =============

REM Check if Python is installed
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Error: Python is not installed or not in PATH.
    echo Please install Python and try again.
    pause
    exit /b 1
)

REM Set default output file
set OUTPUT_FILE=sales_report.txt

REM Check if a CSV file was provided as an argument
if "%~1"=="" (
    REM No argument provided, ask user for input file
    set /p INPUT_FILE="Enter CSV file name (or press Enter for sample_sales_data.csv): "
    
    REM If user just pressed Enter, use the default
    if "!INPUT_FILE!"=="" set INPUT_FILE=sample_sales_data.csv
) else (
    REM Use the provided argument as input file
    set INPUT_FILE=%~1
)

echo.
echo Running sales analysis on %INPUT_FILE%...
echo.

REM Run the Python script
python main.py %INPUT_FILE% %OUTPUT_FILE%

REM Check if the script ran successfully
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Error running the Python script.
    pause
    exit /b %ERRORLEVEL%
)

REM Copy the report to report.txt
if exist %OUTPUT_FILE% (
    copy %OUTPUT_FILE% report.txt
    echo.
    echo Report copied to report.txt
) else (
    echo.
    echo Warning: Report file not found.
)

echo.
echo Process completed.
pause