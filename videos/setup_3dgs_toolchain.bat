@echo off
REM ============================================================
REM  Toolchain p/ 3D Gaussian Splatting (gsplat) — RODE COMO ADMIN
REM  Clique direito neste arquivo -> "Executar como administrador"
REM  (precisa de admin: instala no sistema; ~8 GB no total)
REM ============================================================
echo.
echo [1/2] CUDA Toolkit 12.8 (~3 GB) — casa com o torch cu128...
winget install --id Nvidia.CUDA --version 12.8 --silent --accept-package-agreements --accept-source-agreements
echo.
echo [2/2] Visual Studio Build Tools + workload C++ (~5 GB)...
winget install --id Microsoft.VisualStudio.2022.BuildTools --silent --accept-package-agreements --accept-source-agreements --override "--quiet --wait --add Microsoft.VisualStudio.Workload.VCTools --includeRecommended"
echo.
echo ============================================================
echo  CONCLUIDO. Feche esta janela e avise o Claude no chat.
echo  Ele vai compilar o gsplat e provar com um render-smoke.
echo ============================================================
pause
