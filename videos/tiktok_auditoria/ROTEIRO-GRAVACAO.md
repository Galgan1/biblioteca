# Roteiro da gravação do vídeo demo (≈90 s)

> Objetivo: mostrar o fluxo TikTok ponta a ponta (Login Kit + Content Posting API + escopos) no sandbox.
> Tudo já está pré-armado. Você só grava seguindo os 5 passos.

## Antes de apertar REC
- **Gravador:** Ferramenta de Captura do Windows 11 → ícone de **vídeo** → **Tela inteira** → **Iniciar**.
  (Atalho: `Win + Shift + S` abre a barra; escolha o modo de gravação. Ou use `Win + G` / Xbox Game Bar.)
- Deixe abertos: o **navegador** (já no perfil @minuto_real2) e o arquivo **`videos\gravar_demo.bat`** à mão.

## Os 5 passos (gravando)

**1. (~0–10s) Login Kit / escopos.** Na barra de endereço do navegador, cole e abra esta URL (mostre a barra; os 3 escopos aparecem nela):
```
https://www.tiktok.com/v2/auth/authorize/?client_key=sbawsqlaz2nv3re5q1&scope=user.info.basic%2Cvideo.publish%2Cvideo.upload&response_type=code&redirect_uri=https%3A%2F%2Fwww.andregalgani.com.br%2Ftiktok-callback.html&state=demoRECfinal01
```

**2. (~10–25s) Autorização + callback.** Ela conclui a autorização e cai na **página de callback no nosso domínio** `www.andregalgani.com.br/tiktok-callback.html` — deixe o domínio visível na barra. Clique em **"Copiar tudo"**.

**3. (~25–35s) Abrir o app.** Dê dois cliques em **`gravar_demo.bat`**. Abre um terminal com o cabeçalho "MINUTO REAL POSTER — Content Posting API (Sandbox)". Pressione **uma tecla**.

**4. (~35–70s) Content Posting API.** O terminal mostra, em sequência:
   - `[1/2] Exchanging the authorization code...` → `Token salvo OK -> conta @Minuto Real`
   - `[2/2] Uploading a book-summary video...` → `OK ✓ SEND_TO_USER_INBOX · publish_id=...`

**5. (~70–90s) Resultado.** Deixe a tela final do terminal (a confirmação `SEND_TO_USER_INBOX`) visível por uns segundos. Opcional: volte ao navegador e mostre o perfil **@minuto_real2** (marca/identidade).

**Pare a gravação** e salve como `.mp4`.

## Depois
- Me diga onde salvou o `.mp4` (ou arraste aqui). Eu **comprimo pra ≤50 MB** (ffmpeg) e devolvo pronto pra anexar no campo *App review → demo video*.
- Aí: colar os textos do dossiê + subir o ícone + Products/Scopes + **Submit**.

## Observações honestas
- **Tela de consentimento (botão "Autorizar"):** não aparece porque a conta já autorizou o app antes, e o TikTok web não permite revogar (só o app de celular). O fluxo ainda demonstra os escopos (visíveis na URL) e a autorização concluída. Se você tiver o **app no celular**, dá pra revogar lá (Configurações → Segurança → Gerenciar permissões de apps) ANTES de gravar — aí a tela de consentimento aparece (versão mais forte). Não é obrigatório.
- O post vai pro **inbox/rascunho** (Direct Post público só depois desta auditoria). A prova é a confirmação no terminal.
