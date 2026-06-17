# Revisão de Design & Criação (Akita) · Minuto Real

> Revisão do sistema de design (marca/tokens) + do pipeline de criação de imagens (geradores HTML→PNG), fundada em 4 auditorias grounded no código. Conduzida pelo loop-agente (4 subagentes Sonnet → síntese Opus → verificação cross-model).

## Veredicto
A **IDENTIDADE está sólida** e quase toda em fonte única (`marca.py` → `tokens.py`). Os problemas reais estão na **camada de CRIAÇÃO**, não na marca: o auto-fit é incompleto/duplicado/sem teste, há peças fora do sistema de tokens, o "DNA visual" não tem fonte única, e alguns slides são densos demais (Krug). É dívida de engenharia da criação — não de marca.

## Matriz (4 facetas)
| Faceta | Estado | Evidência |
|---|---|---|
| **Marca/tokens** | **BOM** | `marca.py` fonte única; `gerar_capa/infografico/dados_kit/dados_carrossel` consomem; |
| ↳ fraturas residuais | PARCIAL | `gerar_premium.py` 100% fora (hardcoda verde L72/C0.16, ouro, fontes); `gerar_carrossel.STORY_CSS` (L661-667) redeclara tokens à mão |
| **Fit/robustez** | **FRACO** | `_FIT_JS`/KIT_FIT em infográfico/kit/pdf-service; `gerar_carrossel._render` tem fit **incompleto** (cobre título+`.ed-body`, NÃO `.quote`/`.cta`/stories) → `overflow:hidden` **corta em silêncio** |
| ↳ CAROUSEL_SHRINK | RISCO | em `server.js` é chamado **sem IIFE** (≠ KIT_FIT) → pode ser **no-op** no Puppeteer (fit do carrossel nunca roda) |
| ↳ teste de overflow | **FALTA** | nenhum teste objetivo de fit em lugar nenhum (gap Akita) |
| **Princípios (Norman/Krug)** | BOM-PARCIAL | fortes: hierarquia 4 camadas, ouro parcimonioso, citação-feed = billboard. Fracos: densidade de texto (50-70 palavras/slide), contraste do CTA "RESUMO · UMA PÁGINA" |
| **Dívida/duplicação** | FRACO | DNA visual (`.slide` fundo+grade+moldura) duplicado em carrossel+infográfico; `_FIT_JS` em 4 cópias; `_font_face()` em 3; `_render` Playwright em 5 |

## GAP Nº1
**A camada de criação não tem fonte única do "DNA visual" nem teste de fit.** Consistência e robustez dependem de **sincronia manual** que deriva: o `premium` saiu do sistema, o `STORY_CSS` foi copiado à mão, o `_FIT_JS` vive em 4 versões divergentes e o `CAROUSEL_SHRINK` pode estar mudo. Resultado: corte silencioso de conteúdo denso e marca que pode dessincronizar — exatamente o que a fonte única deveria impedir.

## Gaps priorizados
| Sev | Gap | Onde | Direção do fix |
|---|---|---|---|
| ALTA | Fit do carrossel incompleto (quote/cta/stories estouram, corte silencioso) | `gerar_carrossel._render` L548-564 | completar o fit p/ todos os tipos de slide |
| ALTA | Sem teste objetivo de overflow | (ausente) | teste que mede `scrollHeight>clientHeight` e falha (verde=exit code) |
| ALTA | `gerar_premium.py` fora do sistema de tokens | `gerar_premium.py` | passar a consumir `marca.py`/`tokens.py` |
| MÉDIA | `CAROUSEL_SHRINK` possivelmente no-op (sem IIFE) | `pdf-service/server.js` L916 | padronizar IIFE `(${FN})()` |
| MÉDIA | Densidade de texto (Krug: ~35 palavras/slide) | curadoria em `*_data.py` | teto de palavras por slide |
| MÉDIA | Contraste fraco do CTA das capas | `gerar_capa.py` | botão preenchido (verde + tinta escura) |
| MÉDIA | DNA visual / `_FIT_JS` / `_font_face` / `_render` duplicados | vários | extrair fontes únicas compartilhadas |
| BAIXA | `STORY_CSS` redeclara tokens à mão | `gerar_carrossel.py` L661 | derivar de `tokens.ROOT` |

## Pontos fortes (não mexer)
- `marca.py`→`tokens.py` como fonte única funciona (capa/infográfico/kit/carrossel-base consomem).
- Hierarquia editorial de 4 camadas nos carrosséis; ouro usado com parcimônia; **citação-feed** é o billboard ideal (Krug).

## Plano-alvo (norte de design + criação)
1. **Fit completo + testado:** um único módulo de auto-fit que cobre TODO tipo de slide + um **teste de overflow** (verde = nada estoura). Fecha o pilar TDD do Akita para imagem.
2. **DNA visual em fonte única:** `tokens.slide_css()` (fundo+grade+moldura), `_font_face` e `_render` compartilhados — editar o visual num lugar só.
3. **Tudo no sistema de tokens:** `gerar_premium.py` e `STORY_CSS` passam a derivar de `marca.py`.
4. **Conteúdo escaneável:** teto de ~35 palavras/slide (Krug) aplicado na curadoria do `*_data.py`.
5. **Affordance:** CTA das capas preenchido (contraste — Norman).

## Caminho (etapas Akita, ordem de risco)
teste de overflow (red) → completar+unificar o fit (green) → extrair o DNA visual → trazer premium/story ao sistema → teto de palavras + contraste do CTA.
