@echo off
REM Auditoria noturna (Akita pilar 7): roda o gate unico testar.py e registra o veredito.
REM Criada 2026-06-20; agendada via schtasks "MinutoReal-Auditoria" (diaria 02:00).
REM Idempotente: pode rodar a qualquer hora; so anexa ao log (nada destrutivo).
cd /d "C:\Users\User\.gemini\antigravity\scratch\biblioteca"
set "LOG=videos\_auditoria.log"
echo ====================================================== >> "%LOG%"
echo [%date% %time%] auditoria iniciada >> "%LOG%"
python testar.py >> "%LOG%" 2>&1
if errorlevel 1 (echo [%date% %time%] VEREDITO: VERMELHO - regressao detectada >> "%LOG%") else (echo [%date% %time%] VEREDITO: VERDE >> "%LOG%")
