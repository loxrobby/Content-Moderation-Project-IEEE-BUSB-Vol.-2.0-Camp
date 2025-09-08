@echo off
title Content Moderation App Launcher
color 0A

:menu
cls
echo ========================================
echo    Content Moderation App Launcher
echo ========================================
echo.
echo Choose an option:
echo.
echo 1. Start Frontend Only (React)
echo 2. Start Backend Only (Flask)
echo 3. Start Both Services
echo 4. Stop All Services
echo 5. Check Service Status
echo 6. Install Dependencies
echo 7. Exit
echo.
set /p choice="Enter your choice (1-7): "

if "%choice%"=="1" goto start_frontend
if "%choice%"=="2" goto start_backend
if "%choice%"=="3" goto start_both
if "%choice%"=="4" goto stop_all
if "%choice%"=="5" goto check_status
if "%choice%"=="6" goto install_deps
if "%choice%"=="7" goto exit
goto invalid

:start_frontend
cls
echo Starting React Frontend...
call start_frontend.bat
goto menu

:start_backend
cls
echo Starting Flask Backend...
call start_backend.bat
goto menu

:start_both
cls
echo Starting Both Services...
call start_both.bat
goto menu

:stop_all
cls
echo Stopping All Services...
call stop_all.bat
goto menu

:check_status
cls
echo ========================================
echo    Service Status Check
echo ========================================
echo.

echo Checking React Frontend (Port 3000)...
netstat -an | findstr ":3000" >nul
if %errorlevel% equ 0 (
    echo ✓ React Frontend is running on port 3000
) else (
    echo ✗ React Frontend is not running
)

echo.
echo Checking Flask Backend (Port 5000)...
netstat -an | findstr ":5000" >nul
if %errorlevel% equ 0 (
    echo ✓ Flask Backend is running on port 5000
) else (
    echo ✗ Flask Backend is not running
)

echo.
echo Checking Nginx (Port 80)...
netstat -an | findstr ":80" >nul
if %errorlevel% equ 0 (
    echo ✓ Nginx is running on port 80
) else (
    echo ✗ Nginx is not running
)

echo.
pause
goto menu

:install_deps
cls
echo ========================================
echo    Installing Dependencies
echo ========================================
echo.

echo Installing Python dependencies...
if exist requirements.txt (
    pip install -r requirements.txt
    if %errorlevel% equ 0 (
        echo ✓ Python dependencies installed successfully
    ) else (
        echo ✗ Failed to install Python dependencies
    )
) else (
    echo ✗ requirements.txt not found
)

echo.
echo Installing Node.js dependencies...
if exist package.json (
    npm install
    if %errorlevel% equ 0 (
        echo ✓ Node.js dependencies installed successfully
    ) else (
        echo ✗ Failed to install Node.js dependencies
    )
) else (
    echo ✗ package.json not found
)

echo.
pause
goto menu

:invalid
echo.
echo Invalid choice. Please enter a number between 1-7.
timeout /t 2 /nobreak >nul
goto menu

:exit
echo.
echo Goodbye!
timeout /t 1 /nobreak >nul
exit
