# C04 — Isolamento de execução (Akita pilar 8) aplicado ao projeto

> Fonte do método: `~/.claude/skills/akita/SKILL.md` (pilar 8) + nota `_akita_pesquisa/A07_isolamento_execucao.md`
> (artigo "AI Agents: Garantindo a Proteção do seu Sistema", akitaonrails.com, 10/01/2026).
> Plataforma: **Windows 11 + PowerShell** — `bwrap`/Bubblewrap NÃO se aplica direto; foco no que é viável aqui.
> Regra desta nota: só DIAGNÓSTICO + PROPOSTA. Nada de código de produção alterado.

O pilar 8 do Akita tem **dois** comandos: (1) **ponto único idempotente** — toda execução passa por um
wrapper/script revisável, nunca comando solto no host; (2) **permissões mínimas** (`allow`/`deny`/`ask`),
negando `rm -rf`/`sudo`/`git push --force`, jamais "YOLO mode" (`--dangerously-skip-permissions`).
Esta nota mede o projeto contra esses dois comandos e propõe o caminho realista no Windows.

---

## 1. Estado atual (paths)

### 1a. O ponto único JÁ EXISTE (parcial) — e é bom
- **`videos/orquestrador.py`** — o candidato natural e já em uso. Recebe um `slug`, lê o estado, e
  faz fan-out paralelo (`ThreadPoolExecutor`) das lanes via `subprocess.run([sys.executable, '<script>.py', ...])`.
  - É **idempotente**: cada runner começa com `if ps.is_done(slug, '<stage>'): return {'status': 'skipped'}`
    (linhas 111, 121, 132, 144, 162, 174). Rodar 2x não refaz o que já está `done`.
  - Tem `--dry-run` (linha 78-80): mostra o `cmd` sem executar — revisável antes de disparar.
  - Respeita o DAG (`videos/dag.py`) e as lanes ativas de `canal-state.json`.
- **`videos/pipeline_state.py`** — a **base da idempotência**. Estado físico em `pipeline/state/<slug>.json`;
  `mark_done/mark_blocked/mark_skipped/is_done/pending_stages`; **lock por slug** (`_get_lock`, linha 32) para o
  fan-out paralelo não corromper o JSON; telemetria append-only em `pipeline/events.jsonl`.
- **`vp100.py`** — simulador dry-run NARRADO (zero efeito colateral) + `vp100 mapa` que já deriva
  `stage→script` do orquestrador, lista **divergências** e **órfãos** (scripts não alcançados = código morto OU
  ferramenta manual). É a "lente" que prova o que o ponto único cobre.
- **`videos/doctor.py`** — loop de auditoria read-only (pilar 7), exit code 0/1; já existe e casa com o tema.

### 1b. Comando solto (host) — onde o pilar 8 é violado hoje
- **`atualizar_metadados.bat`** (raiz) — roda **direto no host**, fora do orquestrador:
  `python videos\coletar_datas.py`, `python gerar_metadados.py`, depois **`scp`**, **`ssh ... chmod/chown`**
  contra a VPS de produção (`root@andregalgani.com.br`). É comando solto com poder de deploy. Disparado por
  tarefa agendada do Windows (`MinutoReal_Metadados`) — roda sem revisão a cada execução.
- **`videos/ci.bat`** — `py_compile` + `unittest`. Solto, mas **read-only/inofensivo** (só compila e testa).
- **`verificar.bat`** — chama `vp100` (dry-run). Inofensivo.
- **`videos/auditoria.bat`, `videos/gravar_demo.bat`, `run_link.bat`, `venci.bat`** — utilitários soltos avulsos.
- **Scripts de rede chamados direto pelo agente/maestro** (fora do orquestrador, conforme `UNMANAGED` na linha 205
  e os `subs` do vp100): `instagram_post.py`, `tiktok_post.py`, `agendar_lote.py` — publicam em conta real
  quando rodados à mão.

### 1c. Permissões (allow/deny/ask) — quase ausentes
- **`~/.claude/settings.json`** (user, global) — só `{theme, agentPushNotifEnabled}`. **Sem bloco `permissions`.**
  Não há `deny` de `rm -rf`/`sudo`/`git push --force` em lugar nenhum por default.
- **`.claude/settings.local.json`** (projeto) — tem **só `allow`**, e um item é o **anti-padrão**:
  ```json
  "allow": ["Bash(rm -rf _work/*)", "Bash(timeout 400 python gerar_video.py roteiros/arte-da-guerra.json)", "mcp__Claude_in_Chrome__javascript_tool"]
  ```
  `Bash(rm -rf _work/*)` está **pré-aprovado** (o agente apaga sem perguntar) e **não há `deny` nem `ask`**.
- CI já existe e é boa: `.github/workflows/ci.yml` (unittest no push/PR) + `videos/ci.bat` (gate local). Isolamento
  da CI já vem de graça (roda em `ubuntu-latest`, efêmero) — esse flanco está coberto.

---

## 2. Gap vs. Akita

| # | Pilar 8 diz | No projeto hoje | Veredito |
|---|---|---|---|
| G1 | Execução só por **ponto único idempotente** | `orquestrador.py` existe e é idempotente, MAS `atualizar_metadados.bat` (deploy via scp/ssh) e os scripts de rede `UNMANAGED` rodam **fora** dele | **Parcial** — o ponto único não cobre deploy de metadados nem publicações manuais |
| G2 | **Permissões mínimas** `allow`/`deny`/`ask` | `~/.claude/settings.json` sem `permissions`; `settings.local.json` só `allow` (com `rm -rf` pré-aprovado) | **Faltando** — não há `deny`, e há um allow perigoso |
| G3 | Anti "YOLO mode" | Nenhum `--dangerously-skip-permissions` encontrado no disco | **OK** (manter assim) |
| G4 | Sandbox que confina escrita ao `$(pwd)` (bwrap) | Inexistente (e **inviável** nativo no Windows) | **N/A no Windows** — ver §4 |

**Causa-raiz:** o projeto tem o *esqueleto* certo (orquestrador + pipeline_state + doctor + vp100), mas o
**deploy/publicação ainda escapa por `.bat` solto** e a **camada de permissões está vazia** — o agente que
roda no host tem mais liberdade do que o Akita aceita.

---

## 3. Proposta REALISTA p/ Windows (gap → mudança → verificação)

### P1 — Política de permissões (G2) · maior retorno, custo quase zero
**Mudança (config, não código de produção):** preencher `deny`/`ask` e remover o `allow` perigoso.
- Em `~/.claude/settings.json` (global, vale p/ todos os projetos), adicionar:
  ```json
  "permissions": {
    "deny": ["Bash(rm -rf /*)", "Bash(rm -rf ~/*)", "Bash(sudo *)",
             "Bash(git push --force*)", "Bash(git reset --hard*)"],
    "ask":  ["Bash(scp *)", "Bash(ssh *)", "Bash(git push*)"]
  }
  ```
- Em `.claude/settings.local.json` (projeto): **trocar** `Bash(rm -rf _work/*)` (apaga sem perguntar) por
  `ask` ou restringir ao caminho absoluto do `_work` do projeto; manter `allow` só do que é repetitivo e seguro
  (o `timeout python gerar_video.py`, o MCP do Chrome).
- ⚠️ Honestidade: a sintaxe acima reflete a do A07; **a allowlist do Claude Code casa por prefixo e tem
  ressalvas** (ex.: `rm -rf /*` não cobre toda variação de `rm`). Tratar como **rede de segurança, não
  garantia** — o isolamento real continua vindo do ponto único + dry-run, não da string de glob.
**Verificação:** `deny` é testável — peça ao agente um comando negado e confirme que ele **recusa/pede**.
Idempotência: editar o JSON 2x = mesmo conteúdo (chave única, não-lista-duplicada). Sem efeito colateral.

### P2 — Consolidar deploy de metadados no ponto único (G1)
**Candidato existente:** `atualizar_metadados.bat` deve virar um **stage do orquestrador** (ou um runner
`run_metadados`), com a MESMA assinatura idempotente dos demais:
```python
def run_metadados(slug, dry_run):          # ou stage 'metadados' sem slug, agendado
    if ps.is_done(slug, 'metadados'): return {'status': 'skipped', ...}
    # coletar_datas.py → gerar_metadados.py → (scp/ssh só se não dry_run)
```
- **Interface mantida:** `python orquestrador.py <slug> --stages metadados [--dry-run]`. O `.bat` da tarefa
  agendada passa a chamar `orquestrador.py --stages metadados` em vez de scp/ssh soltos.
- Ganho: o scp/ssh de produção fica **atrás do `--dry-run`** (revisável) e do `deny`/`ask` de P1, e o estado
  registra que rodou (telemetria + idempotência).
- ⚠️ Esta é mudança em **código de produção** (orquestrador.py) → **fora do escopo desta nota** (só CRIO em
  `_akita_pesquisa/`). Fica como proposta para a lane dona do orquestrador, sob o loop-agente normal.
**Verificação (idempotência — o teste do "rodar 2x"):**
1. `python videos\orquestrador.py <slug> --stages biblioteca --dry-run` → imprime o `cmd`, **não** toca disco/VPS.
2. Rodar a 1ª vez de verdade → `pipeline/state/<slug>.json` marca `biblioteca: done`.
3. Rodar a 2ª vez → saída `status: skipped` e o JSON **não muda** (mesmo `ts`). Mesmo estado = idempotente. ✓
   (Hoje isso já vale para os 6 stages que têm runner; P2 estende para metadados.)

### P3 — `ai-jail.ps1` (wrapper conceitual de execução) · ver §5
Equivalente Windows do `~/.local/bin/ai-jail`: um **ponto único de invocação** que (a) força `cwd` no projeto,
(b) recusa argumentos com `rm -rf`/`sudo`/`scp`/`ssh` a menos que `-Allow`, (c) loga o comando antes de rodar.
Não é sandbox de kernel (impossível nativo, §4) — é uma **portaria revisável** + deny-list em PowerShell.
**Verificação:** `ai-jail.ps1 -DryRun python doctor.py` imprime e não executa; `ai-jail.ps1 python "rm -rf x"`
é **bloqueado** (exit ≠ 0) sem `-Allow`. Rascunho em `aplicacao/ai-jail.ps1` (conceitual, não instalado).

---

## 4. O que é INVIÁVEL no Windows (e o equivalente)

| Akita (Linux) | Por que não nativo no Windows | Equivalente viável aqui |
|---|---|---|
| **Bubblewrap `bwrap`** (`--ro-bind`, `--unshare-all`) | É baseado em **namespaces de usuário do kernel Linux**; não existe no Win32 | **WSL2** (rodar o agente dentro do Ubuntu do WSL e usar `bwrap` lá) — só vale se a toolchain já roda em WSL; senão, ficar na portaria PowerShell de P3 |
| `--bind $(pwd)` confinando escrita ao projeto | Sem o mecanismo de bind-mount do kernel | **Docker Desktop** (container com volume só do projeto) p/ rodar coisa realmente suspeita; ou **VM/Sandbox do Windows** (Windows Sandbox, edições Pro) como "último recurso" do A07 |
| Deny-list de diretórios no host (`.gnupg`, `.aws`…) por bind | idem | ACL do NTFS é pesada demais; na prática, **`deny`/`ask` do Claude Code (P1)** + **`.secrets/` já isolado** (doctor.py lê só os NOMES, nunca o conteúdo) cobrem o essencial |

**Resumo honesto:** no Windows nativo não há "jail" de kernel barato. O isolamento forte real exige **WSL2,
Docker Desktop ou Windows Sandbox**. Sem eles, a defesa é em camadas mais fracas porém reais:
**ponto único idempotente (orquestrador) + dry-run + deny/ask + doctor**. É o "mínimo aceitável" adaptado —
não teatro: cada camada é verificável por exit code.

---

## 5. Rascunho conceitual do wrapper (`ai-jail.ps1`)

Criado em `_akita_pesquisa/aplicacao/ai-jail.ps1` (**conceitual** — não instalado, não no PATH, não toca produção).
É a tradução possível do `ai-jail` do A07: portaria de comando + deny-list, **não** sandbox de kernel.

---

## 6. Risco / colisão

- **Repo compartilhado entre sessões:** múltiplos agentes editam o mesmo working tree (ver `.claude/worktrees/`).
  P1 toca **config** (`settings*.json`) — baixo risco de colisão, mas **não é código** e não exige GitGuy.
- **Git:** nada aqui commita/pusha (constituição: só GitGuy). Esta nota é disco puro.
- **Produção:** P2 mexe no orquestrador (produção) → **NÃO feito aqui**; entregue como proposta para a lane dona,
  sob loop-agente + teste verde. Risco se aplicado sem TDD: quebrar o fan-out — por isso fica fora desta nota.
- **`settings.local.json`:** mudar o `allow` afeta o comportamento das OUTRAS sessões nesta pasta — alinhar antes.
- **`deny` global mal-calibrado** pode travar trabalho legítimo (ex.: `scp` é deploy real e desejado) → por isso
  `scp`/`ssh` vão em **`ask`**, não `deny`.

---

## 7. Resumo do gap → mudança → verificação

| Gap | Mudança proposta | Onde | Verificação (exit code / 2x) |
|---|---|---|---|
| G2 sem deny/ask | bloco `permissions` (deny rm-rf/sudo/force; ask scp/ssh/push) | `~/.claude/settings.json` (+ tirar `rm -rf` do allow local) | agente recusa comando negado; editar 2x = mesmo JSON |
| G1 deploy solto | `atualizar_metadados.bat` → stage do `orquestrador.py` | proposta p/ lane do orquestrador (não aqui) | `--dry-run` não toca VPS; 2ª run = `skipped`, JSON imutável |
| G1 portaria | `ai-jail.ps1` (cwd-lock + deny-list + log) | `_akita_pesquisa/aplicacao/` (conceitual) | `-DryRun` imprime sem rodar; `rm -rf` sem `-Allow` = exit≠0 |
| G4 sandbox | WSL2/Docker/Windows Sandbox p/ o suspeito | doc (inviável nativo) | comando suspeito confinado ao container/VM |
