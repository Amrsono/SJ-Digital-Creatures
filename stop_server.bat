@echo off
title Stop SJ Incubator Server
echo Stopping SJ Incubator server processes...
for /f "tokens=5" %%a in ('netstat -aon ^| findstr ":8080" ^| findstr "LISTENING"') do (
    taskkill /F /PID %%a >nul 2>&1
)
echo Server stopped.
timeout /t 2 /nobreak >nul
