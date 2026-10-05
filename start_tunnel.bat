@echo off
title SJ Incubator - Backend & AI Tunnel to Vercel
echo ===================================================
echo   SJ Digital Creatures - Incubator Backend Tunnel
echo ===================================================
echo.
echo [1/2] Checking local Ollama on port 11434...
curl -s http://localhost:11434/api/tags >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [!] WARNING: Ollama is not responding on port 11434.
    echo     Please make sure Ollama is running so AI agents can respond.
    echo.
) else (
    echo [OK] Ollama is active.
)

echo [2/2] Checking Incubator Server on port 8080...
curl -s http://localhost:8080/api/ollama/status >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [!] NOTE: server.py is not running on port 8080. Starting it in a new window...
    start "SJ Incubator Server" python server.py
    timeout /t 3 /nobreak >nul
) else (
    echo [OK] Incubator Server (server.py) is active on port 8080.
)

echo.
echo ===================================================
echo   Connecting Cloudflare Tunnel to port 8080...
echo   Copy the 'https://*.trycloudflare.com' URL below!
echo   Keep this window OPEN while testing your Vercel site.
echo ===================================================
echo.

powershell -NoProfile -ExecutionPolicy Bypass -Command ^
  "$cf = 'C:\Program Files (x86)\cloudflared\cloudflared.exe';" ^
  "if (-not (Test-Path $cf)) { $cf = 'cloudflared' };" ^
  "& $cf tunnel --url http://localhost:8080 --http-host-header localhost:8080"

pause
