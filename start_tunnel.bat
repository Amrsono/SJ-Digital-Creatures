@echo off
title SJ Incubator - Remote Tunnel
echo ===================================================
echo   SJ Digital Creatures - Incubator Remote Tunnel
echo ===================================================
echo.

echo [1/2] Checking local Ollama on port 11434...
curl -s http://localhost:11434/api/tags >nul 2>&1
if errorlevel 1 (
    echo [!] WARNING: Ollama is not responding on port 11434.
    echo     Please make sure Ollama is running so AI agents can respond.
    echo.
) else (
    echo [OK] Ollama is active.
)

echo [2/2] Checking Incubator Server on port 8080...
curl -s http://localhost:8080/api/auth/status >nul 2>&1
if errorlevel 1 (
    echo [!] NOTE: server.py is not running on port 8080. Starting server...
    start "SJ Incubator Server" python server.py
    timeout /t 3 /nobreak >nul
) else (
    echo [OK] Incubator Server is active on port 8080.
)

echo.
echo ===================================================
echo   Connecting Cloudflare Tunnel to port 8080...
echo   Copy the 'https://*.trycloudflare.com' URL below!
echo   Share that link with Moeen and keep this window OPEN.
echo ===================================================
echo.

set "CF_PATH=C:\Program Files (x86)\cloudflared\cloudflared.exe"
if not exist "%CF_PATH%" set "CF_PATH=cloudflared"

"%CF_PATH%" tunnel --url http://localhost:8080

echo.
echo Tunnel process has ended.
pause
