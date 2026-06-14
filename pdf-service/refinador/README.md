# Refinador de PDF — laço de qualidade "patus"

Sai do "imprimir página" e entra num **laço que gera → mede → ajusta → regera**
até o PDF passar do alvo de qualidade, e só chama a Anthropic quando empaca.
Tudo **local e offline**. Não publica nada.

## A ideia
O motor (`../server.js`) gera uma vez e entrega. O refinador fecha o laço por
cima dele, **sem tocar em produção a cada request**: aprende a melhor
configuração offline, grava em `tuned.json`, e o motor lê isso em produção
(rápido e determinístico, como antes).

```
GERAR ─▶ RASTERIZAR ─▶ MEDIR "patus" ─▶ < alvo? ─▶ AJUSTAR ─▶ (regera)
(motor)   (PyMuPDF)     (metricas.py)        │                    ▲
                                             └─ empacou? ─▶ ROTA DE FUGA (Claude) ┘
                                                            (claude_cli.py)
                            tudo abaixo do alvo por causa do CSS/motor?
                                     └─▶ propor_patch.py  (patch p/ revisão — PORTÃO)
```

## A nota de "patus" (`metricas.py`)
Proxies determinísticos do que separa um PDF gostoso de um desconfortável:
`coverage` (desce até o pé?), `density` (nem deserto, nem amontoado),
`gap_frac` (buraco no meio), `edge_ink` (encostando na borda), `pages`
(coube no alvo?). É proxy — quando trava, a rota de fuga dá o julgamento que a
métrica não pega. Alvo padrão: **0.85**.

## Os botões (tune)
O `adaptiveFit` do motor virou parametrizável. Sem `tuned.json`, usa os defaults
(= comportamento de hoje). Botões: `maxFs`, `fillTarget`, `rhythmCap`, `padCap`,
`marginMul` (faixas em `claude_cli.py:KNOBS`). O `tuned.json` é por **livro →
página exata** (cada página pode ter sua config).

## Uso
```bash
# uma página / um livro inteiro / o catálogo inteiro
python refinar.py padrao-bitcoin ch07-ciclos-economicos
python refinar.py padrao-bitcoin
python refinar.py --all --budget 12

# nota de um PDF avulso
python metricas.py arquivo.pdf

# patch estrutural (quando o tune não resolve) — só PROPÕE, não aplica
python propor_patch.py padrao-bitcoin/visao-geral outro/cap
```
O serviço sobe sozinho (porta 3009, `REFINADOR=1`) e é encerrado no fim. Em
produção o env `REFINADOR` não existe, então as rotas `/_refinar` nem nascem.

## Auto-melhora — os dois níveis
1. **Config aprendida (autônomo, reversível):** `refinar.py` grava `tuned.json`.
   Melhora sozinho, sem tocar código. É só apagar o arquivo para reverter.
2. **Patch estrutural (com PORTÃO):** `propor_patch.py` pede ao Claude um diff
   real do CSS/motor e salva em `propostas/<ts>/`. **Não aplica, não publica.**
   Aplicar = branch + `refinar.py --all` (regressão) + deploy com OK explícito.

## Fronteira de segurança
- Nada aqui faz `scp`/deploy. Publicar no site é sempre passo humano.
- `*.py`, `propostas/` e este README ficam locais (não vão pro ar).
- O que vai pro ar é só o `server.js` (motor) e o `tuned.json` (config aprendida).

## Arquivos
`metricas.py` nota · `engine.py` sobe/fala com o serviço · `claude_cli.py` rota
de fuga · `refinar.py` o laço · `propor_patch.py` patch estrutural (portão) ·
`tuned.json` config aprendida (lida pelo motor).
