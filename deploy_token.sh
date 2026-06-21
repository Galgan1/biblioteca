#!/usr/bin/env bash
# Coloca o token do Instagram na VPS + cria o admin + confere — tudo num passo.
# VOCÊ roda (mexe com credencial viva, então é sua ação, não da IA).
#
#   bash deploy_token.sh <usuario_admin> '<senha_admin>'
#
# Ex.: bash deploy_token.sh andre 'MinhaSenhaForte123'
set -euo pipefail
cd "$(dirname "$0")"   # raiz do projeto (onde está videos/.secrets/)

ADMINU="${1:?uso: bash deploy_token.sh <usuario_admin> '<senha_admin>'}"
ADMINP="${2:?informe a senha do admin como 2o argumento}"
HOST="root@andregalgani.com.br"
REMOTE="/opt/biblioteca-pdf"
TOKEN_LOCAL="videos/.secrets/instagram_token.json"

[ -f "$TOKEN_LOCAL" ] || { echo "token local não encontrado: $TOKEN_LOCAL"; exit 1; }

echo "1/3 · enviando token p/ a VPS…"
scp "$TOKEN_LOCAL" "$HOST:$REMOTE/.secrets/instagram.json"
ssh "$HOST" "chmod 600 $REMOTE/.secrets/instagram.json"

echo "2/3 · criando admin '$ADMINU'…"
ssh "$HOST" "cd $REMOTE && ADMIN_USER='$ADMINU' ADMIN_PASSWORD='$ADMINP' node seed_admin.js"

echo "3/3 · conferindo…"
ssh "$HOST" "cd $REMOTE && node -e 'const t=require(\"./.secrets/instagram.json\"); console.log(\"  token ok:\", !!t.access_token, \"| len\", (t.access_token||\"\").length)'"
echo ""
echo "PRONTO. Abra um livro com #admin (ex.: .../biblioteca/48-leis-do-poder.html#admin),"
echo "faça login e teste os 4 formatos em dry-run. Depois me avise que eu verifico."
