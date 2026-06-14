@echo off
REM Atualiza o painel de metadados: coleta ao vivo (YouTube/Instagram/nginx/Amazon),
REM regenera o HTML e publica na VPS. Chamado pela tarefa agendada MinutoReal_Metadados.
set BASE=C:\Users\User\.gemini\antigravity\scratch\biblioteca
set LOG=%BASE%\_metadados_atualizar.log
set REMOTE=root@andregalgani.com.br:/var/www/andregalgani/biblioteca/metadados/index.html
cd /d %BASE%
echo ==== [%date% %time%] inicio ==== >> "%LOG%"
python videos\coletar_datas.py >> "%LOG%" 2>&1
python gerar_metadados.py >> "%LOG%" 2>&1
scp -q metadados/index.html %REMOTE% >> "%LOG%" 2>&1
ssh root@andregalgani.com.br "chmod 644 /var/www/andregalgani/biblioteca/metadados/index.html; chown www-data:www-data /var/www/andregalgani/biblioteca/metadados/index.html" >> "%LOG%" 2>&1
echo ==== [%date% %time%] fim ==== >> "%LOG%"
