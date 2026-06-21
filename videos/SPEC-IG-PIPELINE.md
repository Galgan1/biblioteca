# SPEC Retroativa — Pipeline de Automação Instagram
**Canal:** @minutoreal1701 | **Lane:** Instagram/Facebook | **Versão:** 1.0 | **Data:** 2026-06-20

> Documento de constituição técnica da lane IG. Gerado retroativamente por spec cross-model (5 subagentes Opus+Sonnet). Akita-compliance: plano antes de codar, contratos invioláveis, diagnóstico honesto de gaps.

---

## 1. Diagrama de Arquitetura

```
PC LOCAL (Windows)
==================

  [HUMANO] define slug + data
       │
       ▼
  agendar_lote.py  ──────────── (YouTube: longo + 4 shorts + agendamento)
       │ chama sincronizar.enqueue()
       ▼
  sincronizar.py  (enqueue)
    │  calcula ig_alvo_brt = anchor + offset_h (default +2h, max 4h)
    │  monta job dict com cmd: [file_reel|carousel|story, slug, idx]
    │
    ├─[REEL]    SCP  _shorts/<slug>_NN.mp4
    │                → /opt/minutoreal/ig-provisorio/<slug>/
    ├─[STORY]   SCP  _carrossel/<slug>_stories/NN.png
    │                → /opt/minutoreal/_carrossel/<slug>_stories/
    ├─[CAROUSEL] SCP PNGs → /opt/minutoreal/_carrossel/<slug>_overview/
    │            (agendar_instagram.py / agendar_denso.py fazem este SCP)
    └─[MANIFEST] SCP _sync/sync_manifest.json
                     → /opt/minutoreal/sync_manifest.json


VPS  root@andregalgani.com.br
==============================

  CRON: */15 * * * *  /opt/minutoreal/run_ig.sh >> /opt/minutoreal/ig.log 2>&1
       │
       ▼
  ig_runner_vps.py  (main)
    ├── lê sync_manifest.json  (fila de intenção)
    ├── lê sync_state.json     (estado de execução — fonte de verdade)
    ├── filtra: pendentes = sem media_id no state
    ├── filtra: vencidos  = ig_alvo_utc <= now()
    │
    ├─[REEL]    ig.post_reel(mp4, caption)
    │             1) POST /{uid}/media → creation_id  (upload resumível)
    │             2) PUT bytes do mp4 → rupload.facebook.com
    │             3) poll status_code até FINISHED
    │             4) POST /{uid}/media_publish → media_id
    │
    ├─[CAROUSEL] ig.post_carousel(slug, 'overview', publish=True)
    │             1) _png_to_jpg(): PNG → JPEG (Pillow)
    │             2) _scp_host(): detecta VPS → cópia local
    │                destino: /var/www/andregalgani/biblioteca/_carrossel/<slug>_overview/
    │             3) POST N containers-filho
    │             4) POST container CAROUSEL
    │             5) poll + media_publish
    │
    ├─[STORY]   ig.post_story_from_urls(urls, publish=True)
    │             1) Pillow: PNG → JPEG → /var/www/.../biblioteca/_carrossel/<slug>_stories/
    │             2) URL pública: https://andregalgani.com.br/biblioteca/_carrossel/...
    │             3) POST N containers STORIES + media_publish cada
    │
    └── sync_state.json ← {slug|tipo|parte: {media_id, em}}
        sync_manifest.json ← status: publicado
        limpar_provisorio() → rm /opt/minutoreal/ig-provisorio/<slug>/
```

---

## 2. Arquivos-Chave

| Arquivo | Responsabilidade |
|---|---|
| `agendar_lote.py` | Ponto de entrada humano: agenda YT + dispara eco IG em uma ação |
| `sincronizar.py` | Orquestrador local: calcula horário IG, SCP da mídia, escreve/espelha manifesto |
| `agendar_instagram.py` | Agendamento em lote de Reels fora do ciclo YouTube (6 slugs novos + extras 48-leis) |
| `agendar_denso.py` | Calendário denso: preenche 1 carrossel + 2 stories/dia de Jun/18 a Ago/09 |
| `_sync/sync_manifest.json` | Fila de jobs IG — fonte de verdade do scheduler local |
| `ig_runner_vps.py` | Runner da VPS: publica quando a hora chega, atualiza estado |
| `instagram_post.py` | Poster: toda a comunicação real com a Graph API v21.0 |
| `roteiros/<slug>.json` | Roteiro do livro: fonte de legenda e índice do Reel-herói |

### Onde Cada Mídia Fica

| Tipo | Local (PC) | VPS provisório | VPS web |
|---|---|---|---|
| Reel (mp4) | `_shorts/<slug>_NN.mp4` | `/opt/minutoreal/ig-provisorio/<slug>/` | removido após post |
| Carrossel (PNG→JPEG) | `_carrossel/<slug>_overview/` | `/opt/minutoreal/_carrossel/<slug>_overview/` | `/var/www/andregalgani/biblioteca/_carrossel/<slug>_overview/` |
| Story (PNG→JPEG) | `_carrossel/<slug>_stories/` | `/opt/minutoreal/_carrossel/<slug>_stories/` | `/var/www/andregalgani/biblioteca/_carrossel/<slug>_stories/` |

---

## 3. Contratos Invioláveis

**C1 — Eco obrigatório: IG nunca antes do YouTube**
`offset_h > 0` e `<= 4h` sempre. `clamp_offset()` impõe automaticamente. Edições manuais no manifesto que violem isso invalidam a coreografia do canal.

**C2 — `media_id` em `sync_state.json` é a fonte de verdade de "publicado"**
O campo `status` no manifesto é informativo. Um job só está publicado de verdade se `sync_state.json` tiver `media_id` não-nulo para a chave. Nunca inferir estado apenas do `status`.

**C3 — Chave de idempotência `slug|tipo|parte` é o identificador único**
Existe divergência atual entre PC (tupla Python) e VPS (string pipe). O contrato que deve valer: `"{slug}|{tipo}|{parte}"` em ambas as pontas. Toda nova lógica deve usar esse formato.

**C4 — Pasta provisória da VPS é efêmera; o PC é o backup permanente**
Nenhum código deve depender de arquivos em `ig-provisorio/` para recuperar. Se sumir, o PC é a origem para re-upload.

**C5 — Falha sem limite de tentativas exige monitoramento manual**
O runner não tem contador de tentativas nem alerta. Enquanto não houver mecanismo de `status=bloqueado` após N falhas, o operador deve monitorar `ig.log` após cada janela de publicação.

**C6 — Legenda calculada na VPS no momento do disparo**
Nunca embutir legenda no manifesto. Isso garante que ajustes de copy feitos após o enfileiramento ainda se aplicam.

**C7 — Arquivos de estado são runtime: nunca versionados**
`sync_manifest.json` e `sync_state.json` são operacionais. Assim como `canal-state.json`, não versionar — são fonte de estado de runtime, não de código.

**C8 — Roteiro obrigatório apenas para tipo `reel`**
Carrosseis e stories não precisam de `roteiros/<slug>.json`. Correção aplicada em `sincronizar.py:158`: `cfg = _cfg(slug) if tipo == 'reel' else {}`.

---

## 4. Decisões Arquiteturais (ADRs)

### ADR-01: Manifesto JSON local + push (não chamada direta à API)
**Porquê:** A Graph API não aceita `published_at` futuro para Reels. O PC não fica ligado 24h. A solução: fila JSON local espelhada para VPS que tem cron permanente.
**Trade-off:** Manifesto sem lock → possível race condition se dois processos escreverem simultaneamente.

### ADR-02: Cron a cada 15 min (não event-driven)
**Porquê:** Sem daemon, sem infra adicional. 15 min de granularidade é aceitável para publicações que têm offset de horas.
**Trade-off:** Se o cron falhar silenciosamente, jobs ficam pendentes sem alerta.

### ADR-03: Eco atrelado ao horário do YouTube (+2h, janela ≤ 4h)
**Porquê:** Curto deve levar ao longo que acabou de entrar no ar. Algoritmo IG 2026 favorece 20h-22h BRT — exatamente onde o eco cai.
**Trade-off:** Rigidez: eco nunca pode sair >4h depois do longo sem alterar `MAX_OFFSET_H`.

### ADR-04: Upload de Reel via pasta provisória (não URL pública)
**Porquê:** URL pública exporia o vídeo antes da publicação. Upload resumível `rupload.facebook.com` envia bytes direto.
**Trade-off:** Depende de espaço em disco na VPS (não monitorado).

### ADR-05: Stdlib only no PC; poster importado em runtime na VPS
**Porquê:** `sincronizar.py` precisa rodar em ambiente Python minimal. `Pillow` e `google-api-python-client` são dependências da VPS, não do PC.
**Trade-off:** Acoplamento implícito entre `ig_runner_vps.py` e `instagram_post.py` — quebra em runtime, não em import.

### ADR-06: `_scp_host()` detecta VPS e usa cópia local (fix Jun/2026)
**Porquê:** VPS não consegue SSH para si mesma (`root@andregalgani.com.br` de dentro da VPS falha). Fix: `if Path(VPS_BASE).exists(): shutil.copy2()`.
**Trade-off:** Código detects-environment — funciona, mas é um code smell.

---

## 5. Diagnóstico Honesto — Estado Atual

### O que funciona (evidência empírica)
- `post_reel()` — testado em produção (Padrão Bitcoin ×4, Arte da Guerra ×4, Maquiavel ×4, Save the Cat ×4, 48 Leis ×1)
- `_scp_host()` para carrossel local → VPS — funcionou nos primeiros carrosseis
- `_token()` / `_user_id()` — verificados na sessão inicial
- Cron `*/15 * * * *` rodando — confirmado via `crontab -l`

### Gaps de TDD — zero cobertura no subsistema IG
`instagram_post.py`, `sincronizar.py`, `ig_runner_vps.py` não têm nenhum teste automatizado. O pipeline de vídeo tem ~15 arquivos de teste mas nenhum toca a lane IG.

### Pontos frágeis críticos
1. **`_token()` chama `sys.exit()`** — se o arquivo de token não existir, mata o processo do cron inteiro, não só o job.
2. **`sync_state.json` perdido = republicação** — se o arquivo de estado sumir, todos os jobs com `status=publicado` no manifesto serão retentados.
3. **Loop infinito silencioso em falha** — job falho é retentado a cada 15 min sem limite nem alerta.
4. **`longo_publico()` fallback para `True`** — se a API YouTube falhar, o eco pode sair antes do longo.
5. **Carrossel na VPS requer PNGs em `/opt/minutoreal/_carrossel/`** — não verificado antes do disparo; falha em runtime sem aviso prévio.

### 3 Testes Prioritários a Criar
```python
# Teste 1: clamp_offset + build_job calculam horário correto
def test_build_job_reel_horario():
    anchor = datetime(2026, 6, 20, 19, 0, tzinfo=BRT)
    job = build_job('habitos-atomicos', 'reel', anchor, offset_h=2.0)
    assert '21:00' in job['ig_alvo_brt']
    assert build_job('x', 'reel', anchor, 10.0)['offset_h'] == 4.0  # clamp

# Teste 2: runner não republica job com media_id no state
def test_runner_nao_republica():
    state = {'slug|reel|1': {'media_id': '999', 'em': 9999}}
    pendentes = [j for j in [job_passado] if not state.get(job_key(j), {}).get('media_id')]
    assert pendentes == []

# Teste 3: caption_for não vaza URL Amazon na legenda do IG
def test_caption_sem_url_amazon():
    import re
    legenda = caption_for(cfg_mock, 0)
    assert not re.findall(r'https?://amazon', legenda)
    assert 'Associado' in legenda  # disclosure presente
```

---

## 6. Runbook Operacional

### Operações de Rotina (semanais)
1. Confirmar slugs prontos para os dois slots (qua e qui) em `canal-state.json`
2. Para cada slug: `python agendar_lote.py <slug> <youtube_id> <DD/MM>`
3. Verificar fila: `python sincronizar.py list`
4. Revisar log da VPS: `ssh root@andregalgani.com.br "tail -30 /opt/minutoreal/ig.log"`
5. Se fila < 7 dias: `python agendar_denso.py`

### Agendar Livro Novo (comandos completos)
```bash
# 1. Dry-run — confirmar horário
python sincronizar.py enqueue <slug> 23/07 19:00 --dry-run

# 2. Agendar YT + IG em uma ação (use QUARTAS ou QUINTAS)
python agendar_lote.py <slug> <youtube_video_id> 23/07

# 3. Carrossel/story avulso em data diferente
python sincronizar.py enqueue <slug> 25/07 17:00 --tipo carousel
python sincronizar.py enqueue <slug> 26/07 17:00 --tipo story

# 4. Verificar que entrou
python sincronizar.py list
```

### Verificar Saúde da Fila
```bash
# Local
python sincronizar.py list

# VPS — manifesto
ssh root@andregalgani.com.br "python3 /opt/minutoreal/ig_runner_vps.py"

# VPS — contagem
ssh root@andregalgani.com.br "python3 -c \"import json; j=json.load(open('/opt/minutoreal/sync_manifest.json')); print(sum(1 for x in j if x['status']=='pendente'), 'pendentes de', len(j))\""
```

### Recuperar Job Falho
```bash
# Forçar rodada imediata
ssh root@andregalgani.com.br "python3 /opt/minutoreal/ig_runner_vps.py"

# Reverter status manualmente (se travar em falhou)
ssh root@andregalgani.com.br python3 << 'EOF'
import json
p = '/opt/minutoreal/sync_manifest.json'
j = json.load(open(p))
for x in j:
    if x['slug'] == 'SLUG' and x['status'] == 'falhou':
        x['status'] = 'pendente'
        print('revertido:', x['slug'], x['tipo'])
open(p,'w').write(json.dumps(j, ensure_ascii=False, indent=1))
EOF

# Re-enviar mídia ausente
scp "videos\_shorts\<slug>_01.mp4" root@andregalgani.com.br:/opt/minutoreal/ig-provisorio/<slug>/
```

### Monitoramento
```bash
# Log da VPS
ssh root@andregalgani.com.br "tail -50 /opt/minutoreal/ig.log"

# Normal: "nada vencido agora (pendentes: N)"
# Alarme: "[!] midia ausente", "FALHOU", "status_code != FINISHED"

# Confirmar cron ativo
ssh root@andregalgani.com.br "crontab -l | grep ig"
# Esperado: */15 * * * * /opt/minutoreal/run_ig.sh >> /opt/minutoreal/ig.log 2>&1
```

### Segredos e Dependências

| Arquivo | Conteúdo | Quem usa | Quebra sem ele |
|---|---|---|---|
| `.secrets/client_secret.json` | OAuth 2.0 Google Cloud | YouTube agendamento | Agendamento YT falha |
| `.secrets/token_v2.json` | Token OAuth YouTube | `agendar_lote`, runner VPS | Agendamento + confirmação público falham |
| `.secrets/instagram_token.txt` | Access token IG (60 dias) | `instagram_post.py` | Toda publicação IG falha |
| `.secrets/instagram_user_id.txt` | ID `17841426834577980` | `instagram_post.py` | Toda publicação IG falha |

**Aviso crítico:** ao reautorizar YouTube, sempre escolher **"Minuto Real"** — nunca o canal pessoal `UCmSpZF4cVFd1kTYomdC_NUw`.

**Copiar segredos do PC para VPS:**
```bash
scp videos/.secrets/instagram_token.txt root@andregalgani.com.br:/opt/minutoreal/.secrets/
```

---

## 7. Estado da Fila (Jun/2026)

| Período | Cobertura | Tipos |
|---|---|---|
| Jun 18–23 | Reel/dia + carousel/dia + 2 stories/dia | ✅ agendado |
| Jun 24–29 | Carousel/dia + 2 stories/dia | ✅ agendado |
| Jun 30–Jul 5 | Story/dia + carousel/dia + 2ª story/dia | ✅ agendado |
| Jul 6–13 | Carousel/dia (catch-up) + 2 stories/dia | ✅ agendado |
| Jul 14–22 | Carousel pré-lançamento YT + 2 stories/dia | ✅ agendado |
| Jul 24–Ago 2 | Aquecimento Reels agosto + 2 stories/dia | ✅ agendado |
| Ago 3, 5, 7 | 48-Leis Reels extras (partes 4, 9, 11) | ⏳ pendente |
| Ago 10, 17, 20, 24 | Reels agosto (habitos, sutil-arte, psi-fin, pai-rico) | ✅ agendado |

---

## 8. Dívida Técnica Prioritária

1. **`_token()` não deve usar `sys.exit()`** — usar `raise RuntimeError` para não matar o cron inteiro
2. **Limite de tentativas no runner** — após 3 falhas, mover para `bloqueado` e logar alerta diferenciado
3. **Testes automatizados** — ao menos os 3 descritos na seção 5
4. **Chave de idempotência unificada** — PC e VPS devem usar `slug|tipo|parte` (string pipe) nas duas pontas
5. **Verificação de mídia pré-disparo** — antes de chamar a API, confirmar que o arquivo existe na VPS

---

*Spec gerada por: 5 subagentes Claude (Opus+Sonnet cross-model) | Método Akita | Loop-Agente v2*
*Verificação: Executor=Sonnet → Verificador=Opus (cruzado por design)*
