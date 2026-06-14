# Dossiê de Submissão — Auditoria TikTok (Content Posting API / Direct Post)

**App:** Minuto Real Poster · **App ID:** 7650869667216689160 · **Conta:** @minuto_real2
**Objetivo:** aprovar **Direct Post** para que `tiktok_post.py` publique público 100% sozinho (sem rascunho, sem navegador).
**Portal:** https://developers.tiktok.com/app/7650869667216689160/pending → ambiente **Production** (Draft).

> Tudo aqui é **texto pronto pra colar**. Você revisa e clica **Submit for review**. Nada é enviado por mim.

---

## 1. App details → Basic information

| Campo | Valor (colar) | Status |
|---|---|---|
| **App icon** | arquivo `videos/tiktok_auditoria/app_icon_1024.png` (1024×1024, 164 KB, PNG) | ⬜ subir |
| **App name** | `Minuto Real Poster` | ✅ já preenchido |
| **Category** | `Education` | ✅ marcado no rascunho |
| **Description** (≤120) | `Internal app that auto-publishes our own book-summary videos to our Minuto Real TikTok account.` | ⬜ colar |
| **Terms of Service URL** | `https://www.andregalgani.com.br/termos.html` | ⬜ colar (página no ar ✓) |
| **Privacy Policy URL** | `https://www.andregalgani.com.br/privacidade.html` | ⬜ colar (página no ar ✓) |
| **Platforms** | marcar **Web** + **Desktop** | ⬜ marcar |

*Por que Web+Desktop:* o fluxo OAuth acontece numa página web no nosso domínio (`tiktok-callback.html` em andregalgani.com.br) e a publicação roda num script de desktop. O vídeo demo mostra os dois.

---

## 2. App review → Required information

**Campo "Explain how each product and scope works…" (≤1000) — colar:**

```
Minuto Real is an educational channel that publishes original short video summaries of books. "Minuto Real Poster" is our internal tool: it posts videos only to our own accounts, is not offered to third parties, and never posts for other users.

Content Posting API (Direct Post): after the account owner authorizes via Login Kit, the app uploads an MP4 from our channel and creates a post on our own account (@minuto_real2), with the AI-generated-content (AIGC) disclosure enabled.

Scopes:
- user.info.basic - verify the authorized account is ours (open_id / display name) before posting.
- video.upload - send the video file to TikTok (draft/inbox during testing).
- video.publish - create the post directly on our own account (Direct Post).

The demo video shows the full flow in the Sandbox: the owner logs in and grants the three scopes, the app uploads one of our book-summary videos, and the post appears on our account.
```

**Demo video** (obrigatório, ver §5 abaixo) — ⬜ subir o MP4.

---

## 3. Products

- **Add products → Content Posting API.**
- Configurar **Direct Post** (não só "Upload"). É o que destrava a publicação pública automática.
- **Verificação de domínio:** NÃO é necessária — usamos `FILE_UPLOAD` (enviamos o arquivo), não `PULL_FROM_URL`.

## 4. Scopes

- **Add scopes** e incluir exatamente os 3 que o app usa (e nada além — escopo sobrando atrasa a revisão):
  - `user.info.basic`
  - `video.upload`
  - `video.publish`

---

## 5. Vídeo demo — o único item que exige uma gravação de tela

**Regras do TikTok:** mostrar o fluxo ponta a ponta **no Sandbox**, com UI e interações reais; o domínio que aparece no vídeo tem que bater com a URL do site (andregalgani.com.br); mp4/mov, ≤50 MB.

**Roteiro recomendado (~90 s, grava a tela):**

1. **(0–10s)** Abrir o navegador na **URL de OAuth** do nosso app (em `www.tiktok.com/v2/auth/authorize/...`, client_key do sandbox). Mostrar a barra de endereço.
2. **(10–30s)** Tela de **consentimento do TikTok**: aparecem os 3 escopos (user.info.basic, video.upload, video.publish). Clicar **Autorizar** com a conta @minuto_real2.
3. **(30–40s)** Redireciona para **`https://www.andregalgani.com.br/tiktok-callback.html`** — mostrar o domínio na barra (casa com a Website URL).
4. **(40–70s)** No terminal, rodar `python tiktok_post.py save-the-cat` (Direct Post, sandbox). Mostrar a saída: init → upload → `PUBLISH_COMPLETE`.
5. **(70–90s)** Abrir o perfil **@minuto_real2** e mostrar o vídeo publicado.

**Como gravar (escolha um):**
- **Você grava (≈2 min):** Win+G (Xbox Game Bar) → gravar a tela seguindo o roteiro. É a via de maior aprovação (movimento e interação reais).
- **Eu gravo via plugin:** capturo a sequência de telas do fluxo no sandbox e monto um screencast com a pipeline de vídeo. Mais rápido pra você, porém é "slideshow" de prints (risco maior de o revisor pedir interação real).

---

## 6. Checklist final (na ordem)

- [ ] App icon → subir `app_icon_1024.png`
- [ ] Description, ToS URL, Privacy URL → colar
- [ ] Platforms → Web + Desktop
- [ ] Products → Content Posting API + **Direct Post**
- [ ] Scopes → user.info.basic, video.upload, video.publish
- [ ] App review → colar a narrativa + subir o **vídeo demo**
- [ ] **Submit for review** (ação sua)

**Prazo:** a revisão do TikTok costuma levar de alguns dias a ~2 semanas. Enquanto não aprova, seguimos no modo rascunho (`--draft`) ou upload manual.

**Quando aprovar:** `python tiktok_post.py <slug>` (sem `--draft`) passa a publicar público sozinho — fim do toque manual.
