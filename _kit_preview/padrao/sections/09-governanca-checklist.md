## 09. Governança, Checklist & Guardrail

> *Padrão sem governança é só opinião bonita. Esta seção fecha a bíblia: transforma tudo o que veio antes (00–08) em **regra viva** — um checklist que se marca antes de cada peça, uma tabela de pecados capitais, e um **guardrail técnico que falha o build** se a marca derivar. Aqui o belo vira verificável.*

---

### 09.1 Checklist pré-voo (por peça)

Antes de declarar **qualquer** imagem pronta — carrossel, feed, Story, thumbnail, infográfico — passe esta lista. Marque de verdade. Uma caixa desmarcada é um motivo para não publicar.

**Paleta (seção 01)**
- [ ] Canvas é o **dark da marca**: fundo `#08080c` (papel), texto `#f2f2f5` (tinta).
- [ ] O **verde lidera** — `#3faf76` (verde) é a cor estrutural dominante da peça.
- [ ] O **ouro `#d8a64a` aparece no máximo como 1 acento** (destaque/realce premium), nunca como cor de fundo nem espalhado.
- [ ] O **alerta `#e8744f` só aparece em contexto de aviso/voto** — jamais decorativo.
- [ ] **Sem arco-íris**: nenhuma cor fora da paleta da marca. Categorias NÃO são distinguidas por matizes aleatórios.

**Objeto fotorrealista (seções 04–05)**
- [ ] Há **um objeto fotorrealista por item** (ocupa o slot circular/`seal`), não um ícone de linha.
- [ ] O objeto está **tingido na marca** (banhado no verde/ouro no compositing) — não é um stock cru fora da paleta.
- [ ] **Não há mistura**: nenhuma peça com ícone flat *e* objeto fotorreal lado a lado.
- [ ] Todos os objetos da peça pertencem ao **mesmo "mundo" material** (mesma família estética).

**Tipografia (seção 02)**
- [ ] Título em **Hanken Grotesk Black** (display) — `marca.font('display', s, 'Black')`, nunca fonte de sistema.
- [ ] Corpo/editorial em **Literata** (serif) onde a anatomia pede.
- [ ] Nenhuma `arial.ttf` / `ariblk.ttf` / `georgia.ttf` hardcodada — tudo via `marca.font(...)`.

**Anatomia & acabamento (seções 03, 07)**
- [ ] **Moldura + grão + grade de pontos** presentes (a textura premium do canvas).
- [ ] **Glow contido** — sem brilho estourado/clipado em volta do objeto.
- [ ] Hierarquia da grade respeitada (kicker → título → itens → assinatura).

**Legibilidade (seção 08)**
- [ ] Todo texto sobre imagem/objeto tem **scrim** (véu escuro por baixo) garantindo contraste.
- [ ] Cada categoria é sinalizada por **cor + ícone + rótulo** — **nunca só por cor** (acessibilidade; daltônico tem de distinguir).
- [ ] Contraste AA: tinta sobre papel ≥ 4.5:1; verde/ouro sobre papel ≥ 3.0:1 (validado em `check_marca.py`).

**Identidade & formato (seção 00)**
- [ ] Assinatura **@minutoreal1701** presente.
- [ ] **Formato/dimensão corretos** para o destino (feed 1:1, Story/Reel 9:16, thumbnail 16:9).

---

### 09.2 Faça / Não faça — os pecados capitais

| Faça | Não faça |
|---|---|
| Verde `#3faf76` lidera; ouro `#d8a64a` como **único** acento | **Arco-íris** — uma cor por categoria, paleta de banco de imagens |
| `marca.font('display', s, 'Black')` (Hanken) | **Fonte de sistema** (Arial/Calibri/Georgia hardcodada) |
| Um **objeto fotorrealista** por item, na marca | **Misturar** ícone flat com objeto fotorreal na mesma peça |
| Tingir o objeto na cor da marca no compositing | Objeto **fora da paleta** (stock cru, azul/vermelho aleatório) |
| **Scrim** sob todo texto que cai sobre imagem | Texto **sem scrim** — branco sumindo no claro do objeto |
| Glow sutil, sob controle | **Glow estourado** (halo clipado, "brilho de Word") |
| Sinalizar categoria por **cor + ícone + rótulo** | **Cor como único sinal** (falha para daltônicos) |
| Ler toda cor/fonte de `marca.py` | **Hardcodar** `#d8a64a`, `arial.ttf`, OKLCH antigo |

---

### 09.3 O guardrail técnico — `check_marca.py`

A marca não depende de boa vontade: ela é **defendida por código**. `marca.py` é a **fonte única de verdade** (toda cor e fonte saem de `TOKENS` e `font()`), e `check_marca.py` é o porteiro que garante que ninguém burlou isso.

**Como rodar (antes de fechar trabalho de imagem):**

```
python check_marca.py
```

Sai com **código ≠ 0 se houver deriva** — pode (e deve) entrar em CI/pré-commit para barrar regressões.

**O que ele faz, em três frentes:**

**(A) `scan_drift()` — caça hardcode.** Varre cada arquivo da lista **`TARGETS`** e procura, linha a linha, qualquer token do dict **`FORBIDDEN`**. Se achar, imprime `DRIFT <arquivo>:<linha> "<token>" — <correção>` e incrementa o contador. Os `TARGETS` hoje:

```
gerar_carrossel.py, gerar_infografico.py, assets/style.css,
videos/gerar_video.py, videos/gerar_thumb.py, videos/gerar_canal_art.py
```

O dict `FORBIDDEN` proíbe, entre outros: `#d8a64a` (ouro hardcoded → use `marca.hex_of("ouro")`), `ariblk.ttf`/`arial.ttf`/`georgia.ttf` (fontes de sistema → `marca.font(...)`), e os **OKLCH antigos** que ficaram para trás na unificação (ex.: `oklch(84% 0.115 92)` ouro h92, `oklch(73% 0.15 152)` verde L73). Achou? **Drift — build falha.**

**(B) Contraste no canvas escuro — `contrast_report()`.** Calcula a razão WCAG dos pares-chave lendo as cores **da própria marca** (`marca.hex_of(...)`): tinta sobre papel (min 4.5), verde sobre papel (min 3.0), ouro sobre papel (min 3.0), texto escuro sobre pílula verde (min 4.5). Cada par sai marcado `AA ok` ou `ABAIXO`.

**(C) Contraste no modo claro do site — `contrast_report_light()`.** Mesmo relatório para o tema claro, convertendo os OKLCH `[0]` de `marca.TOKENS` para sRGB (`oklch_to_srgb`).

**Regra de ouro do guardrail — para QUALQUER novo gerador de imagem:**
1. **Leia cor/fonte de `marca.py`** (`hex_of`, `rgb`, `font`, `css_root`). Zero hardcode.
2. **Entre na lista `TARGETS`** de `check_marca.py`. Um gerador fora dos `TARGETS` é um gerador sem porteiro — é onde a deriva volta a entrar.

> Hoje `gerar_infografico.py` **já está** nos `TARGETS`. Todo gerador futuro de objeto/imagem segue o mesmo caminho.

---

### 09.4 Fluxo de produção do objeto (gera-uma-vez → cache)

O objeto-por-conceito segue **exatamente** o mesmo espírito dos campos curados que `gerar_infografico.py` já lê (`FLUXO`, `COMPARA`, `NUMEROS`, `ANATOMIA`): é **dado curado no `_data.py` do livro**, não improvisado no gerador.

| Etapa | O quê | Onde |
|---|---|---|
| **1. Curar** | Declarar o objeto-símbolo de cada conceito como **campo no `<slug>_data.py`** (mesmo padrão de `FLUXO`/`COMPARA`) | `<slug>_data.py` |
| **2. Prompt** | Montar o prompt fotorrealista do objeto conforme a **seção 05** | seção 05 |
| **3. Gerar** | Render via **`videos/imagen.py`** (Google Imagen) — passa por `cost_tracker` + `circuit_breaker` | `videos/imagen.py` |
| **4. Tingir** | Aplicar a **tinta de marca** no compositing (verde/ouro), banhar na paleta | compositing |
| **5. Cachear** | Salvar o ativo **versionado em disco** — gera-uma-vez, reusa em tudo | `assets/kit/<slug>/...` |

**Disciplina de custo (Modo Soberano).** O Imagen custa na conta Google do usuário. Por isso: **gera-se uma vez por conceito, tinge-se, e guarda-se em cache versionado**. As peças seguem rodando local/grátis; a IA é a **exceção**, não a rotina. O `circuit_breaker` em `imagen.py` é o freio de mão — se algo dispara, a geração para, não sangra orçamento.

**Onde os assets vivem.** O cache do objeto fica junto dos demais ativos do livro, no padrão já em uso:

```
assets/kit/<slug>/        ← capa-story.png, citacao-feed.png, manifest.json, caps/, thumbs/, [objetos]
```

Como em `gerar_infografico.py`, **a presença do campo no `_data.py` controla a geração** (lá, `if field and not hasattr(data, field): pula`). Sem o campo curado, sem objeto — o gerador degrada com graça, nunca quebra.

---

### 09.5 Versionamento da bíblia

Esta bíblia é **documento vivo**, não tábua de pedra.

- **Dono:** Diretor de Design (lane de unificação da rede, nomeada 14/jun/2026).
- **Registro:** toda revisão anota **data + versão** no cabeçalho do documento mestre.
- **Processo de mudança:** qualquer alteração de padrão (nova cor, nova fonte, novo arquétipo, mudança no objeto) **passa por aqui** — atualiza-se a seção pertinente **e**, se for cor/fonte, atualiza-se `marca.py` (fonte única) e o `FORBIDDEN`/`TARGETS` de `check_marca.py` no mesmo movimento. Bíblia e guardrail andam juntos: mudar uma sem a outra é criar deriva.
- **Critério de aceite de um padrão novo:** ele só é "lei" quando (a) está escrito nesta bíblia, (b) sai de `marca.py`, e (c) é coberto por `check_marca.py`.

---

### Regra de ouro da governança

> **Se a cor ou a fonte não saiu de `marca.py` e não passou no `python check_marca.py`, a peça não está pronta — por mais bonita que pareça.**
