# auto_git.ps1 — Versionamento automático da Biblioteca
# Roda a cada 15 min via Task Scheduler.
# Só commita se nenhum processo do pipeline estiver ativo.

$repo    = "C:\Users\User\.gemini\antigravity\scratch\biblioteca"
$logfile = "$repo\_autogit.log"
$maxLog  = 500   # linhas máximas no log (rota-arquivo simples)

function Log($msg) {
    $ts = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $line = "$ts  $msg"
    Write-Host $line
    Add-Content $logfile $line -Encoding utf8
    # Trunca o log se ficar grande
    $lines = Get-Content $logfile -ErrorAction SilentlyContinue
    if ($lines.Count -gt $maxLog) {
        $lines | Select-Object -Last ($maxLog / 2) | Set-Content $logfile -Encoding utf8
    }
}

# ── 1. Verifica se pipeline está ativo ────────────────────────────────────────
$pipeline = @("gerar_", "publicar_livro", "orquestrador", "gerar_short",
              "gerar_video", "gerar_carrossel", "gerar_infografico", "gerar_capa",
              "gerar_metadados", "coletar_datas")

$active = Get-CimInstance Win32_Process -Filter "Name = 'python.exe' OR Name = 'python3.exe'" -ErrorAction SilentlyContinue |
    Where-Object { $cmd = $_.CommandLine; $pipeline | Where-Object { $cmd -like "*$_*" } }

if ($active) {
    Log "Pipeline ativo: $($active.CommandLine -join ' | '). Aguardando próximo ciclo."
    exit 0
}

# ── 2. Entra no repo ──────────────────────────────────────────────────────────
Set-Location $repo

# Garante que estamos no branch main
$branch = git rev-parse --abbrev-ref HEAD 2>$null
if ($branch -ne "main") {
    Log "Branch atual: $branch (não é main). Pulando."
    exit 0
}

# Puxa mudanças remotas antes de commitar
git fetch origin main --quiet 2>$null

# ── 3. Stage arquivos rastreados modificados ──────────────────────────────────
git add -u 2>$null

# ── 4. Stage novos arquivos seguros (*.html, *_data.py, *.py, docs) ──────────
# Exclui explicitamente: imagens *.png, runtime JSON, pasta videos/ exceto scripts
$safe = git ls-files --others --exclude-standard 2>$null |
    Where-Object {
        ($_ -match '\.(html|py|md|txt|json|js|css|xml|toml|cfg|ini)$') -and
        ($_ -notmatch '^videos/(canal-state|coletar_datas)') -and
        ($_ -notmatch '^(datas_coletadas|historico_metadados|_remote_books)') -and
        ($_ -notmatch '\.png$') -and
        ($_ -notmatch '\.mp4$|\.wav$|\.mp3$')
    }

if ($safe) {
    $safe | ForEach-Object { git add -- $_ 2>$null }
    Log "Novos arquivos staged: $($safe -join ', ')"
}

# ── 5. Remove runtime do staging (segurança extra) ────────────────────────────
$neverStage = @(
    "videos/canal-state.json",
    "datas_coletadas.json",
    "historico_metadados.json",
    "datas_coletadas.json"
)
foreach ($f in $neverStage) {
    $isTracked = git ls-files --error-unmatch $f 2>$null
    if ($LASTEXITCODE -eq 0) {
        git restore --staged $f 2>$null
    }
}

# ── 6. Verifica se tem algo staged ───────────────────────────────────────────
$staged = git diff --cached --name-only 2>$null
if (-not $staged) {
    Log "Nada a commitar."
    exit 0
}

Log "Staged: $($staged -join ', ')"

# ── 7. Commit ────────────────────────────────────────────────────────────────
$ts  = Get-Date -Format "yyyy-MM-dd HH:mm"
$msg = "chore(auto): versionamento automatico $ts`n`nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
git commit -m $msg 2>$null
if ($LASTEXITCODE -ne 0) {
    Log "ERRO no commit."
    exit 1
}
Log "Commit OK."

# ── 8. Push ──────────────────────────────────────────────────────────────────
git push origin main 2>$null
if ($LASTEXITCODE -ne 0) {
    Log "ERRO no push (conflito remoto?). Reverter se necessário."
    exit 1
}
Log "Push OK → origin/main."
