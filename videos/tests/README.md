# Testes — caminho crítico do pipeline (Akita, etapa 3)

Mural de testes do caminho crítico. **Verde = exit code 0** (princípio Akita: o "pronto" é o teste passar, não a IA achar que está certo).

## Como rodar
```bash
cd videos
python -m unittest discover -s tests -t .
```
Exit 0 = tudo verde. Exit ≠ 0 = algo quebrou (não consolide).

## Ambiente
- **Stdlib `unittest`** — zero dependência nova (alinhado à soberania do projeto).
- `test_contracts.py` usa `pydantic` (já é dependência de runtime do pipeline); se ausente, esses testes são **pulados** (skip), não falham.

## Cobertura atual (caminho crítico)
| Arquivo | Módulo testado | O que cobre |
|---|---|---|
| `test_dag.py` | `dag.py` | ordem topológica, stages prontos, grupos paralelos (deps antes dos dependentes) |
| `test_contracts.py` | `contracts.py` | roteiro válido/ inválido, mínimo de cenas, índice de short inválido, faixa de `tts_rate` |
| `test_circuit_breaker.py` | `circuit_breaker.py` | retry (sucesso/esgota/CircuitOpen), abre no threshold, OPEN levanta, half_open→closed |
| `test_pipeline_state.py` | `pipeline_state.py` | mark_done/is_done, persistência, pending, blocked, custo, **escrita concorrente** |

Estado de runtime (canal-state.json, pipeline/state/) é **isolado em arquivos temporários** nos testes — nunca toca os dados reais.

## Próximo (fora desta etapa)
Postadores de rede (IG/FB/TikTok) precisam de mocks de rede — cobertura futura. CI que roda este comando = etapa 5.
