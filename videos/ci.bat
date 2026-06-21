@echo off
REM Gate de CI LOCAL (Akita pilar 5) - rode antes de commitar. Verde = exit 0.
REM Mesmo comando que a GitHub Actions roda (.github/workflows/ci.yml).
cd /d "%~dp0"

echo [1/2] checando sintaxe do caminho critico...
python -m py_compile net.py dag.py contracts.py circuit_breaker.py pipeline_state.py cost_tracker.py orquestrador.py
if errorlevel 1 exit /b 1

echo [2/2] rodando o mural de testes...
python -m unittest discover -s tests -t .
if errorlevel 1 exit /b 1

echo.
echo [ok] CI local verde.
