# Auditoria do Facebook — Linha de Base dos Post-Link (Página "Minuto Real")

**Tipo:** auditoria READ-ONLY (somente `GET`). Nenhum post foi criado, editado ou apagado.
**Data da coleta:** 2026-06-15
**API:** Graph API v21.0 (helper de request espelhado de `videos/facebook_post.py`)
**Página:** Minuto Real (id em `.secrets/facebook_page_id.txt`)
**Escopo:** os 4 primeiros posts da Página — todos no formato **post-link do YouTube** (mensagem-gancho + link `youtu.be`, que vira card de preview). É justamente o formato que o feed do Facebook mais rebaixa.

> Objetivo: fixar a LINHA DE BASE de alcance/engajamento desses post-link, para sustentar com números reais a virada para conteúdo nativo.

---

## Tabela — os 4 post-link

| Slug | Data/hora de publicação (UTC) | Alcance / Impressões | Engajamento | Cliques | Link (permalink) |
|---|---|---|---|---|---|
| arte-da-guerra | 2026-06-14 15:51:22 | não medível¹ | não medível² | não medível¹ | https://www.facebook.com/122108790531353681/posts/122107926099353681 |
| maquiavel-pedagogo | 2026-06-14 15:51:29 | não medível¹ | não medível² | não medível¹ | https://www.facebook.com/122108790531353681/posts/122107926135353681 |
| save-the-cat | 2026-06-14 15:51:36 | não medível¹ | não medível² | não medível¹ | https://www.facebook.com/122108790531353681/posts/122107926201353681 |
| futebol-brasileiro | 2026-06-14 16:28:42 | não medível¹ | não medível² | não medível¹ | https://www.facebook.com/122108790531353681/posts/122107953597353681 |

Os **metadados** (data de publicação, permalink, mensagem) foram lidos com sucesso para os 4 posts via
`GET /{post_id}?fields=created_time,permalink_url,message`. O que **não** se conseguiu medir foram os números de desempenho — detalhado abaixo, sem maquiar.

---

## Por que os números não saíram (honesto)

A coleta foi feita exatamente como pedido. O resultado dos insights tem duas causas distintas, ambas reais:

### 1. Métricas descontinuadas na v21.0 (erro #100)
Das métricas solicitadas, **duas não existem mais** como nome válido nesta versão da API e retornaram
`(#100) The value must be a valid insights metric`:

- `post_impressions` → **inválida** (#100)
- `post_engaged_users` → **inválida** (#100)

As outras duas **são nomes válidos** e foram aceitas pela API (não deram erro de permissão nem de nome):

- `post_impressions_unique` → válida
- `post_clicks` → válida

(Probe adicional: `post_reactions_by_type_total` também é válida; `post_impressions_organic` e `post_activity` são inválidas nesta versão.)

### 2. As métricas válidas retornaram VAZIO (`data: []`)
Para `post_impressions_unique`, `post_clicks` e `post_reactions_by_type_total` — todas com nome aceito — a API
respondeu com `"data": []` (lista vazia), sem nenhum valor numérico, para os **4 posts**. Não houve erro de permissão de insights.

Esse vazio é, ele próprio, o sinal da linha de base. Duas leituras (não excludentes):

- **Posts muito recentes:** todos foram publicados em 14/jun e a coleta é de 15/jun (< 24h). O Facebook
  costuma ter latência na consolidação de insights por post.
- **Alcance abaixo do piso de reporte:** o Facebook frequentemente suprime/zera insights de post quando o
  alcance é pequeno demais. Para post-link de uma Página nova (4 posts no total), alcance perto de zero é o
  cenário esperado — e bate com o vazio retornado.

### 3. Contagem direta de reações/comentários/compartilhamentos: bloqueada por permissão
Tentei o caminho alternativo `GET /{post_id}?fields=reactions.summary(...),comments.summary(...),shares`.
Os 4 posts retornaram:
`(#10) This endpoint requires the 'pages_read_engagement' permission or the 'Page Public Content Access' feature.`
Ou seja, o token de Página atual **não tem** `pages_read_engagement` — então likes/comentários/compartilhamentos
por contagem **não são medíveis** com as permissões de hoje.

**Resumo do que é medível hoje:**
- Medível: data de publicação, permalink, mensagem (os 4 posts). ✅
- Não medível — métrica descontinuada (#100): impressões totais, usuários engajados.
- Não medível — insights retornam vazio (`data: []`): alcance único, cliques, reações por tipo. Provável piso de alcance e/ou latência < 24h.
- Não medível — falta de permissão (#10 `pages_read_engagement`): contagem de reações/comentários/compartilhamentos.

---

## Conclusão (honesta) sobre os post-link

1. **A linha de base de desempenho dos post-link é, na prática, nula/imperceptível.** Mesmo com o token
   tendo acesso a insights (as métricas válidas não deram erro de permissão), o Facebook **não reportou
   um único número** de alcance, cliques ou reações para nenhum dos 4 posts. Para fins de baseline, isso é
   tão eloquente quanto um zero: não há tração mensurável a registrar.

2. **O formato é o suspeito principal.** Os 4 são post-link saindo do feed para o YouTube — exatamente o
   formato que o algoritmo do Facebook mais penaliza (ele empurra o usuário para fora da plataforma). O
   próprio cabeçalho de `facebook_post.py` assume esse formato como padrão. Some-se a isso uma Página nova
   com base de seguidores ~zero, e o alcance perto do piso de reporte é o desfecho previsível.

3. **Ressalva metodológica honesta:** parte do vazio pode ser latência (< 24h) e parte é limitação de
   permissão/métrica da API — não é prova matemática de alcance exatamente zero. Mas, do ponto de vista do
   operador, a conclusão prática é a mesma: **nenhum sinal de tração** veio dos post-link.

---

## Recomendação: migrar para conteúdo NATIVO

- **Parar de publicar como post-link** (link de saída para o YouTube). É o formato mais rebaixado e foi o que
  produziu uma linha de base sem tração mensurável.
- **Publicar nativo no Facebook:** vídeo carregado direto na Página (Reels / vídeo nativo) e/ou carrossel de
  imagens nativo, mantendo o link do acervo/YouTube no comentário ou na bio — não como o objeto do post.
  Conteúdo que fica dentro do feed é favorecido pela distribuição.
- **Reauditar com a API corrigida** depois de publicar nativo, já com:
  - nomes de métrica atuais da v21.0 (`post_impressions_unique`, `post_clicks`, `post_reactions_by_type_total`
    e, para vídeo nativo, as métricas de `post_video_*`), evitando as descontinuadas que deram #100;
  - a permissão `pages_read_engagement` adicionada ao token, para liberar contagem de reações/comentários/compartilhamentos;
  - uma janela ≥ 48–72h após a publicação, para o Facebook consolidar os insights.
- Assim a comparação nativo × post-link terá números dos dois lados — esta auditoria fixa o lado "link" como
  **baseline sem tração mensurável**.

---

### Anexo — mensagens publicadas (os 4 post-link)

- **arte-da-guerra** — gancho: "O tratado de guerra que manda você NÃO lutar"
- **maquiavel-pedagogo** — gancho: "A escola não está falhando. Está funcionando."
- **save-the-cat** — gancho: "As 15 batidas secretas de toda boa história"
- **futebol-brasileiro** — gancho: "Como o Brasil virou o PAÍS DO FUTEBOL — a história do futebol brasileiro (de 1894 ao 7 a 1)"

Todas seguem o mesmo molde de `caption_for()`: gancho + "destiladas, em minutos" + CTA para o acervo + reforço
do vídeo abaixo + 5 hashtags de nicho.

> Nota de segurança: nenhum token ou conteúdo de `.secrets` foi impresso, logado ou versionado nesta
> auditoria. Os arquivos temporários usados na coleta foram apagados; este relatório contém apenas
> permalinks públicos e metadados não sensíveis.
