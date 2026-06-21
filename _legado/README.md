# _legado — geradores aposentados (quarentena reversível)

Akita, etapa 7 (refatoração da dívida). Estes scripts são **geradores de página por-livro legados**: cada um reimplementava, à mão, o que o gerador canônico `gerar_livro.py` já faz a partir de `<slug>_data.py`. Foram movidos para cá (não apagados) para **reduzir a superfície ativa** sem risco — são reversíveis.

## Por que foi seguro aposentar
- O caminho canônico é `publicar_livro.py → gerar_livro.main(slug)`.
- Auditoria de referências: estes arquivos eram referenciados **apenas** por `test_mapa.json`, pela doc `AKITA-DIAGNOSTICO.md` e **entre si** — nenhum código vivo (publicar_livro, gerar_livro, orquestrador, etc.) os importa ou chama.
- Os HTML já gerados desses livros continuam no site (não dependem destes scripts em runtime).
- Nenhum `*_data.py` canônico (fonte da verdade) foi movido.

## Arquivos e o livro de origem
| Arquivo | Livro | Substituído por |
|---|---|---|
| `gerar_arte_rico.py`, `gerar_arte_dados.py` | Arte da Guerra | `gerar_livro.py` |
| `gerar_maquiavel_rico.py`, `gerar_maquiavel_dados.py`, `gerar_html_maquiavel.py` | Maquiavel Pedagogo | `gerar_livro.py` |
| `gerar_psicodelia.py`, `gerar_psicodelia_dados.py` | Experiência Psicodélica | `gerar_livro.py` |
| `gerar_smith.py` | Smith Assertividade | `gerar_livro.py` (+ `smith_data.py` segue na raiz) |
| `gerar_story.py` | Story (McKee) | `gerar_livro.py` (+ `story_data.py` segue na raiz) |
| `gerar_pdfs.py` | PDF antigo (print/) | `pdf-service/` |

## Como restaurar (se um dia precisar)
Mover o arquivo de volta para a raiz do projeto:
```
mv _legado/<arquivo>.py .
```
(Os pares gerador+dados foram movidos juntos, então continuam funcionais aqui dentro.)
