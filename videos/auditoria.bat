@echo off
REM Loop de auditoria (Akita pilar 7). Agende este .bat (Windows Task Scheduler
REM ou cron) para rodar sozinho, ex.: de hora em hora. Verde = exit 0.
REM   1) ci.bat   -> saude do CODIGO (sintaxe + mural de testes)
REM   2) doctor   -> saude do ESTADO (circuits, bloqueios, segredos)
cd /d "%~dp0"

call "%~dp0ci.bat"
if errorlevel 1 (
  echo [auditoria] CODIGO com problema.
  exit /b 1
)

python doctor.py
if errorlevel 1 (
  echo [auditoria] ESTADO com problema (ver doctor acima).
  exit /b 1
)

echo.
echo [ok] auditoria verde (codigo + estado).
