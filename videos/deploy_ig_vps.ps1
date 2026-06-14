# deploy_ig_vps.ps1 - Deploy idempotente da sincronia IG (eco YouTube->Instagram) na VPS.
#
# Conta: root@andregalgani.com.br (SSH SEM SENHA). Base reusada: /opt/minutoreal
# (cron + venv + .secrets chmod 600, FORA da web).
#
# DUAS FASES (rode a infra AGORA; o poster DEPOIS que as legendas estiverem prontas):
#
#   .\deploy_ig_vps.ps1            # FASE 1 (infra): pasta provisoria, venv+Pillow,
#                                  #   ig_runner_vps.py, run_ig.sh, cron a cada 15 min.
#                                  #   NAO copia instagram_post.py nem segredos do IG.
#
#   .\deploy_ig_vps.ps1 -Poster   # FASE 2 (poster): copia instagram_post.py + deps
#                                  #   (roteiros) + segredos do IG (chmod 600) + token.json.
#                                  #   >>> SO RODAR DEPOIS que o outro agente terminar as
#                                  #   >>> legendas de instagram_post.py / gerar_carrossel.py.
#
# Seguro de re-rodar quantas vezes quiser (mkdir -p, copia por cima, cron de-duplicado).

param([switch]$Poster)

$ErrorActionPreference = 'Stop'
$VPS  = 'root@andregalgani.com.br'
$BASE = '/opt/minutoreal'
$HERE = $PSScriptRoot

function Rexec($cmd)  { & ssh.exe $VPS $cmd }
function Rcopy($src, $dst) { & scp.exe -q $src "${VPS}:$dst" }

Write-Host '=== Deploy sincronia IG (eco) na VPS ==='

# ---------------------------------------------------------------------------
# FASE 1 - INFRA (sempre roda)
# ---------------------------------------------------------------------------
Write-Host '[1/5] pasta provisoria (fora da web)'
Rexec "mkdir -p $BASE/ig-provisorio && chmod 700 $BASE/ig-provisorio"

Write-Host '[2/5] garantindo Pillow no venv (carrossel PNG->JPEG)'
Rexec "$BASE/venv/bin/python -c 'import PIL' 2>/dev/null || $BASE/venv/bin/pip install --quiet Pillow"

Write-Host '[3/5] runner ig_runner_vps.py'
Rcopy "$HERE\ig_runner_vps.py" "$BASE/ig_runner_vps.py"
Rexec "chmod 755 $BASE/ig_runner_vps.py"

Write-Host '[4/5] run_ig.sh + manifesto vazio (se ainda nao existir)'
# Gera o run_ig.sh REMOTAMENTE com printf (LF, sem BOM) — escrever a string do
# PowerShell por pipe injetaria BOM/CRLF e quebraria o shebang sob o cron.
Rexec "printf '%s\n' '#!/bin/bash' 'cd $BASE' '$BASE/venv/bin/python ig_runner_vps.py' > $BASE/run_ig.sh && chmod 755 $BASE/run_ig.sh"
Rexec "test -f $BASE/sync_manifest.json || echo '[]' > $BASE/sync_manifest.json"

Write-Host '[5/5] cron a cada 15 min (idempotente)'
$cronline = "*/15 * * * * $BASE/run_ig.sh >> $BASE/ig.log 2>&1"
Rexec "( crontab -l 2>/dev/null | grep -v 'run_ig.sh' ; echo '$cronline' ) | crontab -"

Write-Host 'INFRA OK: provisoria + venv(Pillow) + runner + run_ig.sh + cron 15min'

if (-not $Poster) {
    Write-Host ''
    Write-Host '>>> FASE 2 (poster) NAO executada de proposito.'
    Write-Host '>>> Rode  .\deploy_ig_vps.ps1 -Poster  DEPOIS que as legendas de'
    Write-Host '>>> instagram_post.py / gerar_carrossel.py estiverem prontas.'
    exit 0
}

# ---------------------------------------------------------------------------
# FASE 2 - POSTER (so com -Poster; roda DEPOIS das legendas prontas)
# ---------------------------------------------------------------------------
Write-Host ''
Write-Host '=== FASE 2: poster do IG (instagram_post.py + segredos) ==='

Write-Host '[poster 1/3] instagram_post.py + roteiros (deps de legenda)'
Rcopy "$HERE\instagram_post.py" "$BASE/instagram_post.py"
Rexec "mkdir -p $BASE/roteiros"
scp -q "$HERE\roteiros\*.json" "${VPS}:$BASE/roteiros/"

Write-Host '[poster 2/3] segredos do IG (chmod 600, fora da web)'
Rexec "mkdir -p $BASE/.secrets && chmod 700 $BASE/.secrets"
foreach ($s in @('instagram_token.txt','instagram_token.json','instagram_user_id.txt',
                 'instagram_app_id.txt','instagram_app_secret.txt')) {
    $local = Join-Path "$HERE\.secrets" $s
    if (Test-Path $local) {
        Rcopy $local "$BASE/.secrets/$s"
        Rexec "chmod 600 $BASE/.secrets/$s"
        Write-Host "  + $s"
    } else {
        Write-Host "  (ausente, pulado) $s"
    }
}

Write-Host '[poster 3/3] sanity import na VPS'
Rexec "cd $BASE && $BASE/venv/bin/python -c 'import instagram_post; print(123)'"

Write-Host 'POSTER OK: instagram_post.py + roteiros + segredos do IG na VPS.'
Write-Host 'A sincronia esta completa. O cron disparara os ecos automaticamente.'
