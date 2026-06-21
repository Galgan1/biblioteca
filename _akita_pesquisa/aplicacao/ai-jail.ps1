# ai-jail.ps1 — RASCUNHO CONCEITUAL (Akita pilar 8, adaptado ao Windows)
#
# NÃO instalado, NÃO no PATH, NÃO toca produção. É a tradução possível do
# `~/.local/bin/ai-jail` do artigo A07 (akitaonrails.com 10/01/2026) para Windows.
#
# O que ele É:   uma PORTARIA revisável de execução + deny-list, com cwd travado
#               no projeto e log do comando antes de rodar.
# O que ele NÃO é: um sandbox de kernel. Bubblewrap (--ro-bind/--unshare-all)
#               depende de namespaces do Linux e não existe no Win32. Para
#               isolamento forte real use WSL2 + bwrap, Docker Desktop, ou
#               Windows Sandbox (ver C04_isolamento.md §4). Isto é o "mínimo".
#
# Uso conceitual:
#   .\ai-jail.ps1 python videos\doctor.py            # roda dentro da portaria
#   .\ai-jail.ps1 -DryRun python orquestrador.py x   # imprime e NÃO executa
#   .\ai-jail.ps1 python "rm -rf foo"                # BLOQUEADO (exit 2)
#   .\ai-jail.ps1 -Allow scp arq root@host:/x        # libera 1 comando da ask-list
#
# Verificação (exit code):
#   -DryRun           -> imprime o comando, exit 0, nada executado
#   comando deny      -> exit 2 (bloqueado)
#   comando ask sem -Allow -> exit 3 (precisa confirmação)
#   comando permitido -> repassa o exit code real do processo

[CmdletBinding()]
param(
    [switch]$DryRun,                       # mostra o comando e sai (revisão antes de rodar)
    [switch]$Allow,                        # libera explicitamente 1 comando da ask-list
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Command                     # o comando a executar (ex.: python x.py)
)

# Raiz do projeto = pai da pasta _akita_pesquisa/aplicacao deste script.
$ProjectRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path

# DENY: jamais, nem com -Allow. (A string casa por substring — rede de segurança,
# não garantia; o isolamento real vem do ponto único + dry-run.)
$DenyPatterns = @(
    'rm -rf',  'rm -fr',
    'sudo ',
    'git push --force', 'git push -f',
    'git reset --hard',
    'Remove-Item -Recurse -Force',
    'format ',  'del /s'
)

# ASK: efeito colateral em produção; exige -Allow para passar.
$AskPatterns = @( 'scp ', 'ssh ', 'git push' )

if (-not $Command -or $Command.Count -eq 0) {
    Write-Host 'ai-jail: nenhum comando. Uso: .\ai-jail.ps1 [-DryRun] [-Allow] <comando>' -ForegroundColor Yellow
    exit 1
}

$flat = ($Command -join ' ')

# 1) DENY-LIST (bloqueio duro)
foreach ($p in $DenyPatterns) {
    if ($flat -like "*$p*") {
        Write-Host "ai-jail: BLOQUEADO (deny-list: '$p') -> $flat" -ForegroundColor Red
        exit 2
    }
}

# 2) ASK-LIST (precisa -Allow)
foreach ($p in $AskPatterns) {
    if ($flat -like "*$p*" -and -not $Allow) {
        Write-Host "ai-jail: requer confirmacao (ask-list: '$p'). Repita com -Allow." -ForegroundColor Yellow
        Write-Host "  comando: $flat" -ForegroundColor DarkGray
        exit 3
    }
}

# 3) LOG (proveniencia: o que rodou, quando, de onde)
$stamp = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
Write-Host "[ai-jail $stamp] cwd=$ProjectRoot :: $flat" -ForegroundColor DarkCyan

# 4) DRY-RUN (revisao antes de executar)
if ($DryRun) {
    Write-Host 'ai-jail: --DryRun -> nada executado.' -ForegroundColor Green
    exit 0
}

# 5) EXECUTA com cwd travado no projeto (equivalente fraco do --chdir $(pwd))
Push-Location $ProjectRoot
try {
    $exe  = $Command[0]
    $rest = if ($Command.Count -gt 1) { $Command[1..($Command.Count - 1)] } else { @() }
    & $exe @rest
    $code = $LASTEXITCODE
}
finally {
    Pop-Location
}
exit $code
