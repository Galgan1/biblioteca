@echo off
chcp 65001 >nul
title Minuto Real Poster - Content Posting API demo (Sandbox)
cd /d "%~dp0"
cls
echo ============================================================
echo   MINUTO REAL POSTER  -  Content Posting API (Sandbox) demo
echo ============================================================
echo.
echo   1) Authorize in the browser as @minuto_real2
echo   2) On the callback page, click "Copiar tudo"
echo   3) Come back here and press any key
echo.
pause >nul
echo.
echo [1/2] Exchanging the authorization code for an access token...
python tiktok_oauth.py
echo.
echo [2/2] Uploading a book-summary video via the Content Posting API...
python tiktok_post.py file "_shorts\save-the-cat_01.mp4" "Save the Cat! - resumo em 1 minuto | Minuto Real  #resumodelivro #livros #savethecat" --draft
echo.
echo ============================================================
echo   Done. The video was delivered to the @minuto_real2 account.
echo ============================================================
pause
