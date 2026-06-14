@echo off
echo === Forcando remocao de arquivos travados ===
del /f /q "C:\Users\User\AppData\Local\hermes\gateway.lock" 2>nul
del /f /q "C:\Users\User\AppData\Local\hermes\state.db" 2>nul
del /f /q "C:\Users\User\AppData\Local\hermes\state.db-shm" 2>nul
del /f /q "C:\Users\User\AppData\Local\hermes\state.db-wal" 2>nul

echo === Removendo subpastas ===
rmdir /s /q "C:\Users\User\AppData\Local\hermes\hermes-agent" 2>nul
rmdir /s /q "C:\Users\User\AppData\Local\hermes\logs" 2>nul
rmdir /s /q "C:\Users\User\AppData\Local\hermes\migration" 2>nul
rmdir /s /q "C:\Users\User\AppData\Local\hermes\skills" 2>nul

echo === Removendo pasta raiz ===
rmdir /s /q "C:\Users\User\AppData\Local\hermes" 2>nul

if not exist "C:\Users\User\AppData\Local\hermes" (
    echo.
    echo === HERMES REMOVIDO COM SUCESSO ===
) else (
    echo.
    echo === Restam arquivos - tentando PowerShell ===
    powershell -Command "Remove-Item -Path 'C:\Users\User\AppData\Local\hermes' -Recurse -Force -ErrorAction SilentlyContinue"
    if not exist "C:\Users\User\AppData\Local\hermes" (
        echo === HERMES REMOVIDO VIA POWERSHELL ===
    ) else (
        echo === FALHA FINAL - reinicie o PC e tente novamente ===
    )
)
