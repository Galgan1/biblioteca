# A07 — Isolamento de execução de agentes de IA (sandbox / jail)

**Fonte:** https://akitaonrails.com/2026/01/10/ai-agents-garantindo-a-protecao-do-seu-sistema/
**Publicado:** 10 de janeiro de 2026
**Artigo:** "AI Agents: Garantindo a Proteção do seu Sistema" (Fábio Akita)

> Tema central: o agente de IA **não é confiável sozinho** — pode "halucinar a qualquer momento e decidir apagar coisas". Logo, em vez de confiar no agente, isola-se a execução. O agente roda dentro de um **sandbox / JAIL**, nunca como **comando solto no host**.

## Práticas concretas

- **Sandbox via Bubblewrap (`bwrap`).** Cria um **JAIL** que confina o agente. É o componente que permite Flatpak. "É basicamente assim que um container de Docker ou Podman funciona também."
- **Sistema em read-only, projeto em read-write.** As libs/binários do sistema entram como `--ro-bind` (`/usr`, `/bin`, `/lib`, `/lib64`); **só `$(pwd)`** recebe escrita (`--bind $(pwd) $(pwd)` + `--chdir $(pwd)`). Assim um `rm -Rf` não alcança nada fora do diretório do projeto.
- **Namespaces isolados:** `--unshare-all` (isola tudo) e, quando há rede, reativa-se explicitamente com `--share-net` — o agente precisa de rede para acessar APIs externas. Também `--dev /dev`, `--proc /proc`, `--die-with-parent`.
- **Comando básico literal:**
  ```bash
  bwrap --ro-bind /usr /usr \
        --ro-bind /bin /bin \
        --ro-bind /lib /lib \
        --ro-bind /lib64 /lib64 \
        --dev /dev \
        --proc /proc \
        --bind $(pwd) $(pwd) \
        --chdir $(pwd) \
        --unshare-all \
        --share-net \
        bash
  ```
- **Wrapper/script único de execução — `ai-jail`.** Empacota o sandbox num único ponto: `~/.local/bin/ai-jail` (`chmod +x ~/.local/bin/ai-jail`), usado como `~/.local/bin/ai-jail crush`. Em vez de digitar `bwrap` solto toda vez, **roda-se o agente sempre via `ai-jail`** (ponto único de execução).
- **Deny-list / allow-list de diretórios sensíveis no `ai-jail`:** bloqueia segredos (`.gnupg`, `.aws`, `.mozilla`, carteiras `.basilisk-dev`/`.sparrow`) e libera RW só o necessário (`.claude`, `.crush`, `.codex`, `.aider`, `.config`, `.cargo`). Suporta GPU, socket Docker e display X11/Wayland conforme preciso.
- **Permissões mínimas no Claude Code** (`~/.claude/settings.json`): listas `allow` / `deny` / `ask`.
  ```json
  {
    "permissions": {
      "allow": ["Bash(git add *)", "Bash(npm *)", "Bash(ls *)", "WebSearch"],
      "deny":  ["Bash(rm -rf *)", "Bash(sudo *)", "Bash(git push --force *)", "Bash(git reset --hard *)"],
      "ask":   ["Bash(git push *)", "Bash(docker run *)"]
    }
  }
  ```
- **Escalonamento de risco:** "Sempre rode coisas realmente suspeitas somente numa VM ou, no mínimo, dentro de um jail como esse." VM = último recurso; jail/bwrap = mínimo aceitável.

## Anti-padrões

- **"YOLO mode" / pular permissões:** usar `--allow-dangerously-skip-permissions` por preguiça — "Todo mundo acaba ficando com preguiça e diz foda-se, roda o que quiser". Anula toda a proteção.
- **Confiar no agente sozinho:** LLM alucina e pode apagar coisas; comportamento "bem-comportado" não é garantia.
- **Rodar comando solto no host:** sem sandbox, um `rm -Rf /` ou similar atinge o sistema inteiro, fora do diretório do projeto.
- **Ignorar supply-chain:** **ataques de supply-chain** invadem bibliotecas open source; software aberto não é garantia de segurança — daí a "restrição máxima".

## Termos

- **JAIL / sandbox** — ambiente confinado onde o agente roda.
- **Bubblewrap (`bwrap`)** — ferramenta de sandbox (base do Flatpak); flags: `--ro-bind`, `--bind`, `--dev-bind`, `--dev`, `--proc`, `--tmpfs`, `--symlink`, `--chdir`, `--unshare-all`, `--share-net`, `--die-with-parent`.
- **`ai-jail`** — script wrapper em `~/.local/bin/ai-jail`; ponto único de execução do agente.
- **allow-list / deny-list / ask** — listas de permissão em `~/.claude/settings.json`.
- **YOLO mode** / `--allow-dangerously-skip-permissions` — o anti-padrão de autorizar tudo.
- **ataques de supply-chain** — vetor de risco mesmo com software "comportado".
- **Docker / Podman / VM** — alternativas/escalonamento de isolamento.

## Aplicação (1-2 linhas)

No projeto Biblioteca, rodar todo agente que executa código via um **ponto único idempotente** (estilo `ai-jail`) que confina escrita ao diretório do projeto e nega `rm -rf`/`sudo`/segredos — nunca comando solto no host nem `--dangerously-skip-permissions`. Casa direto com o pilar Akita "execução só por ponto único idempotente" e "isolamento de execução".
