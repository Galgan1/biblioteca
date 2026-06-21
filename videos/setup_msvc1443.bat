@echo off
REM ============================================================
REM  Adiciona o toolset MSVC 14.43 (VS 17.13) — compativel com
REM  o nvcc do CUDA 12.8 (o 14.44 instalado e' novo demais).
REM  RODE COMO ADMINISTRADOR (clique direito -> Executar como administrador).
REM  ~300-600 MB.
REM ============================================================
echo.
echo Instalando o toolset MSVC 14.43 (VC v143 17.13)...
winget install --id Microsoft.VisualStudio.2022.BuildTools --silent --accept-package-agreements --accept-source-agreements --override "--quiet --wait --add Microsoft.VisualStudio.Component.VC.14.43.17.13.x86.x64"
echo.
echo ============================================================
echo  CONCLUIDO. Feche esta janela e avise o Claude no chat.
echo ============================================================
pause
