@echo off
REM Compila o backend CUDA do gsplat com o ambiente MSVC + CUDA 12.8 (Blackwell sm_120).
REM -vcvars_ver=14.43: força o toolset MSVC compativel com o nvcc do CUDA 12.8
call "C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\Build\vcvars64.bat" -vcvars_ver=14.43
set "CUDA_PATH=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.8"
set "CUDA_HOME=%CUDA_PATH%"
set "PATH=%CUDA_PATH%\bin;%PATH%"
set "TORCH_CUDA_ARCH_LIST=12.0"
set "DISTUTILS_USE_SDK=1"
echo === nvcc ===
nvcc --version
echo === cl ===
where cl
echo === compilando gsplat backend (JIT, pode demorar 10-30 min) ===
python -c "from gsplat.cuda._backend import _C; print('GSPLAT_BACKEND:', 'OK' if _C is not None else 'FAIL')"
echo === fim ===
