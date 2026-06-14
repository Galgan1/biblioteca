#!/bin/bash
# Atualiza o painel de metadados de forma AUTONOMA na VPS (independe do PC do Andre).
# Coleta ao vivo (YouTube + Instagram + logs nginx LOCAIS) e regenera o HTML direto no web root.
# Agendado via cron (de hora em hora). Log em /opt/minutoreal/metadados.log
cd /opt/minutoreal || exit 1
export MR_BASE=/opt/minutoreal
export MR_OUT=/var/www/andregalgani/biblioteca/metadados
export MR_LOCAL_LOGS=1
PY=/opt/minutoreal/venv/bin/python
LOG=/opt/minutoreal/metadados.log
echo "==== $(date '+%F %T') inicio ====" >> "$LOG"
$PY /opt/minutoreal/coletar_datas.py >> "$LOG" 2>&1
$PY /opt/minutoreal/gerar_metadados.py >> "$LOG" 2>&1
chmod 644 "$MR_OUT/index.html" 2>/dev/null
chown www-data:www-data "$MR_OUT/index.html" 2>/dev/null
echo "==== $(date '+%F %T') fim ====" >> "$LOG"
