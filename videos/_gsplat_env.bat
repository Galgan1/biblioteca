@echo off
REM Roda `python <args>` no ambiente pronto p/ gsplat: MSVC 14.43 + CUDA 12.8 + ninja no PATH.
cd /d "C:\Users\User\.gemini\antigravity\scratch\biblioteca\videos"
call "C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\Build\vcvars64.bat" -vcvars_ver=14.43 >nul 2>&1
set "CUDA_PATH=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.8"
set "CUDA_HOME=%CUDA_PATH%"
set "PATH=%CUDA_PATH%\bin;C:\Users\User\AppData\Local\Programs\Python\Python313\Scripts;%PATH%"
set "TORCH_CUDA_ARCH_LIST=12.0"
set "DISTUTILS_USE_SDK=1"
set "NO_COLOR=1"
set "PYTHONIOENCODING=utf-8"
python %*
