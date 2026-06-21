# Veredicto Sonnet — Relatório de Saúde CLAUDE.md
> Verificação cross-model (autor = Opus, juiz = Sonnet). Data: 2026-06-20.

## Evidências coletadas (spot-check)

### ALTA-1 + ALTA-2: Carrossel / Gate cego
- `wc -l gerar_carrossel.py` → **895 linhas** (contrato diz ≤350). CONFIRMADO.
- `grep -n "_carousel" gerar_carrossel.py` → **zero matches** (arquivo não importa os módulos). CONFIRMADO.
- Arquivos órfãos existem: `_carousel_css.py`, `_carousel_slides.py`, `_carousel_stories.py` — não importados.
- `pytest tests/test_carrossel.py -q` → **6 falham, 2 passam (exit 1)**. CONFIRMADO.
- `python testar.py` → **451 testes VERDE** — usa `unittest discover`, NÃO coleta `test_carrossel.py` (pytest-style). CONFIRMADO.
- CLAUDE.md L17: "verificados pela bateria de testes (`pytest tests/test_carrossel.py`)" e "violar = teste vermelho" — afirmação **falsa hoje**: o gate oficial (testar.py) é cego a esses testes.
- **Veredicto ALTA-1/ALTA-2: CONFIRMADO. Sem falso-positivo.**

### ALTA-3: Contradição constituição × skill
- CLAUDE.md L11: "verificação cross-model (juiz ≠ autor: Opus ↔ Sonnet) ... sem exceção" — mandatório.
- akita SKILL.md §11 (linha 85): "**Multi-modelo NÃO é default**... mistura é 'otimização prematura'... Opus solo vence em ~90%."
- akita SKILL.md linha 86: "Nosso `loop-agente` (Verifier cross-model) é **acréscimo nosso** — não atribua ao Akita."
- A contradição é real: o CLAUDE.md ordena o que a skill (que ele mesmo cita como fonte) chama de anti-padrão para ~90% dos casos.
- **Veredicto ALTA-3: CONFIRMADO. Contradição real, não falso-positivo.**
- Nota de calibração: severidade ALTA é justificada — cria fricção toda vez que um agente lê as duas fontes.

### ALTA-4: Dead references
- `_akita_pesquisa/` → **não existe** no disco. CONFIRMADO.
- `.claude/settings.local.json` → verificado em DUAS localizações (`~/.claude/` e `biblioteca/.claude/`) — **não existe em nenhuma**. CONFIRMADO.
- `~/.claude/` tem `settings.json` mas não `settings.local.json`.
- **Veredicto ALTA-4: CONFIRMADO. Sem falso-positivo.**

### ALTA-5: Duplicação quase-literal doc × skill
- CLAUDE.md L88: "meta < 5 hits de grep" + L114: "cemitério de superstição".
- akita SKILL.md linha 71: "<5 grep hits" + linha 80: "cemitério de superstição".
- Frases idênticas (mesma dicção, mesmo conceito) em ambos os arquivos.
- **Veredicto ALTA-5: CONFIRMADO. Duplicação real.**

---

## Avaliação de severidade

| Achado | Severidade reportada | Avaliação do juiz |
|--------|---------------------|-------------------|
| ALTA-1/2 (monolito + gate cego) | ALTA | **CORRETA** — falha de integridade: constituição afirma enforcement que não existe |
| ALTA-3 (contradição loop × skill) | ALTA | **CORRETA** — cria instruções contraditórias para o agente |
| ALTA-4 (dead refs) | ALTA | **PARCIALMENTE EXAGERADA** — refs quebradas são reais, mas impacto é doc incorreto, não falha operacional. Rebaixar para MÉDIA seria defensável. Manter ALTA é conservador mas aceitável. |
| ALTA-5 (duplicação) | ALTA | **EXAGERADA** — duplicação é real, mas não quebra nada hoje; drift é risco futuro. MÉDIA é mais adequado. |

---

## Veredito final

**APROVADO COM RESSALVA** — o relatório é substancialmente fiel. Todos os 5 achados ALTA foram confirmados por evidência direta. Nenhum falso-positivo encontrado nos ALTAs. Duas calibrações de severidade: ALTA-4 e ALTA-5 poderiam ser MÉDIA sem perder informação. Os saudáveis (451 testes VERDE, fantasmas ausentes, módulos de vídeo) também foram confirmados.

**Prioridade de ação:** ALTA-2 (gate cego + claim falso) é o achado mais urgente — a constituição mente sobre seu próprio enforcement; corrigir a linha 17 do CLAUDE.md para citar `python testar.py` e reconhecer que `test_carrossel.py` está fora do gate é a correção mais barata e de maior impacto. ALTA-1 (portar ou reescrever a seção de contratos) e ALTA-3 (adicionar ressalva A05 ao "Modo PADRÃO") vêm em seguida.
