// admin.js — painel de administração da Biblioteca (carregado SÓ para admins).
// O integrador injeta este script apenas nas sessões autenticadas como admin;
// ainda assim ele se protege sozinho (checa pdf/auth/me e some em silêncio se
// não for admin). Fala com o pdf-service sob ${prefix}pdf/ com credentials:'include'.
//
// Espelha as convenções de script-livro.js:
//  - BIBLIOTECA_BOOK derivado do src do <script> (aqui: .../<livro>/admin.js ou
//    o admin.js dos assets) com fallback pelo location.pathname;
//  - isOverview / chapterMatch / prefix ('' na visão geral, '../' nos capítulos);
//  - overlays "dark-glass" com role=dialog, ESC fecha, mesmo padrão do kit/Pix.
(() => {
    'use strict';

    // ---------- detecção de livro + prefixo (robusta, autossuficiente) ----------
    // O script-livro.js (carregado via <book>/script.js) já resolve isto e expõe em
    // window.BIBLIOTECA_CTX. Se não estiver presente (script.js antigo em cache),
    // derivamos do próprio caminho /…/biblioteca/<...>: overview = "<livro>.html",
    // capítulo = "<livro>/<cap>.html". NÃO usamos o src (admin.js mora em /assets/, o
    // que antes casava "assets" como slug e quebrava o prefixo → 404 no login).
    function ctxFromPath() {
        const m = location.pathname.match(/\/biblioteca\/(.+)$/);
        if (!m) return { book: '', isOverview: false, chapter: null, prefix: '' };
        const parts = m[1].split('/').filter(Boolean);
        if (parts.length >= 2) {
            return { book: parts[0], isOverview: false,
                chapter: parts[1].replace(/\.html$/, ''), prefix: '../'.repeat(parts.length - 1) };
        }
        return { book: parts[0].replace(/\.html$/, ''), isOverview: true, chapter: null, prefix: '' };
    }
    const CTX = (typeof window !== 'undefined' && window.BIBLIOTECA_CTX) || ctxFromPath();
    const BIBLIOTECA_BOOK = CTX.book || '';
    const isOverview = !!CTX.isOverview;
    const isHome = !!CTX.isHome;
    const chapterMatch = CTX.chapter ? [null, CTX.chapter] : null;
    const onBookPage = isOverview || !!chapterMatch;
    const prefix = typeof CTX.prefix === 'string' ? CTX.prefix : (isOverview ? '' : '../');

    // ---------- helpers de fetch (nunca lançam para fora) ----------
    // Toda chamada usa credentials:'include' (cookie de sessão do pdf-service).
    function apiUrl(p) { return prefix + 'pdf/' + p; }

    async function apiGet(p) {
        const res = await fetch(apiUrl(p), { credentials: 'include' });
        return res;
    }
    async function apiPost(p, body) {
        const res = await fetch(apiUrl(p), {
            method: 'POST',
            credentials: 'include',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(body || {}),
        });
        return res;
    }
    // tenta parsear JSON sem explodir em respostas vazias/HTML de erro
    async function safeJson(res) {
        try { return await res.json(); } catch (e) { return null; }
    }
    const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
    const PAUSE_MS = 4000; // respiro entre posts no "Todos" (educado com a API)
    // cota diária do IG; null = não foi possível consultar (não bloqueia — fail-open)
    async function fetchLimit() {
        try {
            const res = await apiGet('admin/instagram/limit');
            if (!res.ok) return null;
            const d = await safeJson(res);
            return (d && d.remaining != null) ? d : null;
        } catch (e) { return null; }
    }

    // ---------- ícones de linha (gramática da marca, traço 2) ----------
    const _SVG = (inner) => '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
        + 'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + inner + '</svg>';
    const IG_ICON = _SVG('<rect x="3" y="3" width="18" height="18" rx="5"/>'
        + '<circle cx="12" cy="12" r="4"/><path d="M17 6.5h.01"/>');
    const SEND_ICON = _SVG('<path d="M22 2 11 13"/><path d="M22 2 15 22l-4-9-9-4 20-7z"/>');
    const OUT_ICON = _SVG('<path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/>'
        + '<path d="M16 17l5-5-5-5"/><path d="M21 12H9"/>');
    const X_ICON = _SVG('<path d="M6 6l12 12M18 6 6 18"/>');
    const LINK_ICON = _SVG('<path d="M9.5 14.5 14.5 9.5"/><path d="M11 7.5l1-1a3.5 3.5 0 0 1 5 5l-1 1"/>'
        + '<path d="M13 16.5l-1 1a3.5 3.5 0 0 1-5-5l1-1"/>');
    const YT_ICON = _SVG('<rect x="2" y="5" width="20" height="14" rx="4"/><path d="M10 9l5 3-5 3z"/>');
    const EYE_ICON = _SVG('<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7-10-7-10-7z"/><circle cx="12" cy="12" r="3"/>');
    const EYE_OFF_ICON = _SVG('<path d="M3 3l18 18"/><path d="M10.6 10.6a3 3 0 0 0 4.2 4.2"/>'
        + '<path d="M9.9 5.2A10 10 0 0 1 12 5c6.5 0 10 7 10 7a17 17 0 0 1-3 3.6"/>'
        + '<path d="M6.1 6.2A17 17 0 0 0 2 12s3.5 7 10 7a10 10 0 0 0 3.3-.6"/>');

    // rótulos amigáveis para os formatos do Instagram (chaves do contrato)
    const FORMAT_LABELS = {
        feed: 'Feed',
        story: 'Story',
        carousel: 'Carrossel',
        carrossel: 'Carrossel',
        reels: 'Reels',
        reel: 'Reels',
    };
    const STORY_TYPES = new Set(['story', 'stories']);
    function fmtLabel(type) {
        return FORMAT_LABELS[String(type || '').toLowerCase()] || (type || 'Formato');
    }
    function isStory(type) { return STORY_TYPES.has(String(type || '').toLowerCase()); }

    // ---------- ponto de entrada ----------
    // Este script é injetado DINAMICAMENTE pelo script-livro.js, normalmente já
    // depois do DOMContentLoaded — então, se o DOM já está pronto, chamamos boot()
    // na hora (senão o boot nunca rodaria). Caso raro de carga antecipada: espera o evento.
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', boot);
    } else {
        boot();
    }

    async function boot() {
        // checa a sessão; qualquer falha de rede ⇒ trata como deslogado (silencioso).
        let me = null;
        try {
            const res = await apiGet('auth/me');
            if (res.ok) me = await safeJson(res);
        } catch (e) { me = null; }

        if (me && me.role === 'admin') {
            // já é admin: monta o painel direto (se estiver numa página de livro).
            mountForState(me);
        } else if (me && me.user) {
            // logado, mas não-admin: nada (silencioso, conforme contrato).
            return;
        } else {
            // deslogado: expõe um pequeno gatilho "entrar" que abre o modal de login.
            injectLoginAffordance();
        }
    }

    // estado de sessão atual (preenchido após login/me)
    let SESSION = null;

    function mountForState(me) {
        SESSION = me;
        if (me.role === 'admin' && onBookPage && BIBLIOTECA_BOOK) {
            injectAdminPanel();
        } else if (me.role === 'admin' && isHome) {
            injectUploadPanel();
        }
        // não-admin, ou admin sem contexto: nada visível.
    }

    // ======================================================================
    //  Gatilho "entrar" + modal de login
    // ======================================================================
    function injectLoginAffordance() {
        // botão discreto, canto inferior; só abre o login. Não polui a página.
        if (document.querySelector('.adm-entrar')) return;
        const btn = document.createElement('button');
        btn.type = 'button';
        btn.className = 'adm-entrar';
        btn.title = 'Área administrativa';
        btn.setAttribute('aria-label', 'Entrar na área administrativa');
        btn.innerHTML = OUT_ICON + '<span>entrar</span>';
        btn.addEventListener('click', openLoginModal);
        document.body.appendChild(btn);
    }

    function openLoginModal() {
        const overlay = makeOverlay('adm-overlay', 'Entrar na área administrativa');
        const modal = document.createElement('div');
        modal.className = 'adm-modal adm-modal--login';
        modal.innerHTML =
            '<div class="adm-modal-head">'
            + '<span class="adm-dot"></span>'
            + '<h2 id="adm-login-title">Área administrativa</h2>'
            + '<button type="button" class="adm-x" data-close aria-label="Fechar">' + X_ICON + '</button>'
            + '</div>'
            + '<form class="adm-form" novalidate autocomplete="off">'
            + '  <label class="adm-field"><span>Usuário</span>'
            + '    <input type="text" name="username" autocomplete="off" autocapitalize="off" '
            + '      spellcheck="false" required></label>'
            + '  <label class="adm-field"><span>Senha</span>'
            + '    <span class="adm-pass-wrap">'
            + '      <input type="password" name="password" autocomplete="off" autocapitalize="off" '
            + '        spellcheck="false" required>'
            + '      <button type="button" class="adm-pass-eye" data-eye aria-label="Mostrar senha" '
            + '        title="Mostrar/ocultar senha">' + EYE_ICON + '</button>'
            + '    </span></label>'
            + '  <p class="adm-status" role="status" aria-live="polite"></p>'
            + '  <div class="adm-actions">'
            + '    <button type="submit" class="adm-btn adm-btn--solid">Entrar</button>'
            + '    <button type="button" class="adm-btn adm-btn--ghost" data-close>Cancelar</button>'
            + '  </div>'
            + '</form>';
        overlay.appendChild(modal);
        overlay.setAttribute('aria-labelledby', 'adm-login-title');
        document.body.appendChild(overlay);

        const form = modal.querySelector('.adm-form');
        const statusEl = modal.querySelector('.adm-status');
        const submitBtn = modal.querySelector('button[type="submit"]');
        const userInput = modal.querySelector('input[name="username"]');

        wireClose(overlay);

        // olho: mostra/oculta a senha (deixa o usuário CONFERIR o que está no campo —
        // pega autofill errado, espaço invisível ou Caps Lock na hora).
        const passInput = form.querySelector('input[name="password"]');
        const eyeBtn = modal.querySelector('[data-eye]');
        if (eyeBtn && passInput) {
            eyeBtn.addEventListener('click', () => {
                const show = passInput.type === 'password';
                passInput.type = show ? 'text' : 'password';
                eyeBtn.innerHTML = show ? EYE_OFF_ICON : EYE_ICON;
                eyeBtn.setAttribute('aria-label', show ? 'Ocultar senha' : 'Mostrar senha');
                try { passInput.focus(); } catch (e) {}
            });
        }

        // foca o primeiro campo (acessibilidade)
        setTimeout(() => { try { userInput.focus(); } catch (e) {} }, 30);

        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            const username = userInput.value.trim();
            const password = passInput.value.trim(); // apara espaços (autofill/cola)
            if (!username || !password) {
                setStatus(statusEl, 'Preencha usuário e senha.', 'err');
                return;
            }
            submitBtn.disabled = true;
            setStatus(statusEl, 'Entrando…', 'busy');
            let data = null, ok = false;
            try {
                const res = await apiPost('auth/login', { username, password });
                data = await safeJson(res);
                ok = res.ok;
            } catch (err) { ok = false; }

            if (ok && data && data.role) {
                setStatus(statusEl, 'Bem-vindo, ' + (data.user || username) + '.', 'ok');
                closeOverlay(overlay);
                const entrar = document.querySelector('.adm-entrar');
                if (entrar) entrar.remove();
                mountForState(data);
            } else {
                submitBtn.disabled = false;
                const msg = (data && data.error) ? data.error : 'Usuário ou senha inválidos.';
                setStatus(statusEl, msg, 'err');
            }
        });
    }

    // ======================================================================
    //  Painel "Publicar no Instagram" (admin + página de livro)
    // ======================================================================
    async function injectAdminPanel() {
        if (document.querySelector('.adm-panel')) return; // idempotente

        // ponto de injeção: depois da .kit-section se existir, senão depois do header.
        // O kit é montado por script-livro.js em paralelo; ele pode ainda não estar
        // no DOM. Esperamos um pouco por ele e caímos no header como fallback.
        const anchor = await waitForAnchor();
        if (!anchor) return; // página sem header nem kit — não há onde ancorar.

        const panel = document.createElement('section');
        panel.className = 'adm-panel';
        panel.setAttribute('aria-label', 'Publicar no Instagram');
        panel.innerHTML =
            '<div class="adm-panel-head">'
            + '<span class="adm-ig-badge">' + IG_ICON + '</span>'
            + '<div class="adm-panel-titles">'
            + '  <h2>Publicar no Instagram</h2>'
            + '  <span class="adm-panel-sub">@minutoreal1701 · ' + (BIBLIOTECA_BOOK || '') + '</span>'
            + '</div>'
            + '<button type="button" class="adm-logout" data-logout title="Sair">' + OUT_ICON + '<span>sair</span></button>'
            + '</div>'
            + '<div class="adm-panel-body">'
            + '  <div class="adm-loading">Carregando opções…</div>'
            + '</div>';
        anchor.insertAdjacentElement('afterend', panel);

        panel.querySelector('[data-logout]').addEventListener('click', () => doLogout(panel));

        const body = panel.querySelector('.adm-panel-body');
        let opts = null, ok = false;
        try {
            const res = await apiGet('admin/instagram/options?book=' + encodeURIComponent(BIBLIOTECA_BOOK));
            ok = res.ok;
            if (ok) opts = await safeJson(res);
        } catch (e) { ok = false; }

        if (!ok || !opts || !Array.isArray(opts.options) || !opts.options.length) {
            body.innerHTML = '<p class="adm-empty">Nenhuma peça disponível para publicar neste livro.</p>';
            return;
        }
        renderPanelForm(body, opts);
    }

    // monta os selects (formato → peça), a legenda e o botão Publicar
    function renderPanelForm(body, opts) {
        const formats = opts.options; // [{type, selectors:[...]}]
        const captionPreview = typeof opts.captionPreview === 'string' ? opts.captionPreview : '';

        body.innerHTML =
            '<div class="adm-row">'
            + '  <label class="adm-field"><span>Formato</span>'
            + '    <select class="adm-select" data-format></select></label>'
            + '  <label class="adm-field"><span>Peça</span>'
            + '    <select class="adm-select" data-piece></select></label>'
            + '</div>'
            + '<label class="adm-field adm-field--caption" data-caption-wrap>'
            + '  <span>Legenda</span>'
            + '  <textarea class="adm-caption" data-caption rows="5" '
            + '    placeholder="Legenda da publicação…"></textarea>'
            + '</label>'
            + '<p class="adm-status adm-publish-status" role="status" aria-live="polite"></p>'
            + '<div class="adm-actions adm-actions--publish">'
            + '  <button type="button" class="adm-btn adm-btn--solid" data-publish>'
            + SEND_ICON + '<span>Publicar</span></button>'
            + '</div>'
            + '<div class="adm-yt-sep"></div>'
            + '<p class="adm-status adm-yt-status" role="status" aria-live="polite"></p>'
            + '<div class="adm-actions">'
            + '  <button type="button" class="adm-btn adm-btn--yt" data-publish-yt>'
            + YT_ICON + '<span>Publicar vídeo no YouTube</span></button>'
            + '</div>';

        const formatSel = body.querySelector('[data-format]');
        const pieceSel = body.querySelector('[data-piece]');
        const captionWrap = body.querySelector('[data-caption-wrap]');
        const captionEl = body.querySelector('[data-caption]');
        const statusEl = body.querySelector('.adm-publish-status');
        const publishBtn = body.querySelector('[data-publish]');
        const ytBtn = body.querySelector('[data-publish-yt]');
        const ytStatus = body.querySelector('.adm-yt-status');
        if (ytBtn) ytBtn.addEventListener('click', () => confirmYT(ytBtn, ytStatus));

        // "Todos os formatos" (publica 1 de cada, em sequência) — só com 2+ formatos
        if (formats.length > 1) {
            const oa = document.createElement('option');
            oa.value = 'all'; oa.textContent = 'Todos os formatos';
            formatSel.appendChild(oa);
        }
        // popula o select de formatos
        formats.forEach((f, i) => {
            const o = document.createElement('option');
            o.value = String(i); // índice — evita ambiguidade de chaves
            o.textContent = fmtLabel(f.type);
            formatSel.appendChild(o);
        });

        const isAll = () => formatSel.value === 'all';
        function currentFormat() { return isAll() ? null : formats[Number(formatSel.value) || 0]; }

        // peça representativa de cada formato p/ o modo "Todos os formatos"
        function pickFor(fmt) {
            const sels = (fmt.selectors || []).map((s) => (s && typeof s === 'object') ? s.value : s).filter(Boolean);
            if (!sels.length) return null;
            const pref = {
                feed: ['mapa', 'ideia', 'citacao-feed'],
                story: ['capa-story', 'citacao-story', 'insights-story'],
                carrossel: ['overview'], carousel: ['overview'],
            }[String(fmt.type || '').toLowerCase()] || [];
            for (const p of pref) if (sels.includes(p)) return p;
            return sels[0];
        }

        // ao trocar de formato: repovoa peças + mostra/oculta legenda (Story = sem legenda)
        function syncFormat() {
            if (isAll()) {
                pieceSel.innerHTML = '<option>1 de cada formato</option>';
                pieceSel.disabled = true;
                publishBtn.disabled = false;
                captionWrap.hidden = false;            // legenda vale p/ feed/carrossel/reels
                captionEl.value = captionPreview;
                setStatus(statusEl, '', '');
                return;
            }
            const f = currentFormat();
            const selectors = Array.isArray(f && f.selectors) ? f.selectors : [];
            pieceSel.innerHTML = '';
            if (!selectors.length) {
                const o = document.createElement('option');
                o.value = '';
                o.textContent = '— sem peças —';
                pieceSel.appendChild(o);
                pieceSel.disabled = true;
                publishBtn.disabled = true;
            } else {
                pieceSel.disabled = false;
                publishBtn.disabled = false;
                selectors.forEach((sel) => {
                    const o = document.createElement('option');
                    // selector pode ser string ou {value,label}
                    if (sel && typeof sel === 'object') {
                        o.value = sel.value != null ? String(sel.value) : '';
                        o.textContent = sel.label || sel.value || '(peça)';
                    } else {
                        o.value = String(sel);
                        o.textContent = String(sel);
                    }
                    pieceSel.appendChild(o);
                });
            }
            // Story não leva legenda: oculta o campo e zera o valor.
            if (isStory(f && f.type)) {
                captionWrap.hidden = true;
                captionEl.value = '';
            } else {
                captionWrap.hidden = false;
                captionEl.value = captionPreview;
            }
            setStatus(statusEl, '', '');
        }

        formatSel.addEventListener('change', syncFormat);
        syncFormat(); // estado inicial

        publishBtn.addEventListener('click', async () => {
            let payload;
            if (isAll()) {
                const list = formats.map((f) => {
                    const sel = pickFor(f);
                    return sel ? { type: f.type, selector: sel, label: fmtLabel(f.type) } : null;
                }).filter(Boolean);
                if (!list.length) { setStatus(statusEl, 'Nenhuma peça disponível.', 'err'); return; }
                payload = { all: true, list: list, caption: captionEl.value, statusEl: statusEl, publishBtn: publishBtn };
            } else {
                const f = currentFormat();
                const selector = pieceSel.value;
                if (pieceSel.disabled || selector === '') {
                    setStatus(statusEl, 'Selecione uma peça.', 'err');
                    return;
                }
                const story = isStory(f && f.type);
                payload = {
                    book: BIBLIOTECA_BOOK, type: f.type, selector: selector,
                    caption: story ? '' : captionEl.value,
                    formatLabel: fmtLabel(f.type),
                    pieceLabel: pieceSel.options[pieceSel.selectedIndex] ? pieceSel.options[pieceSel.selectedIndex].textContent : selector,
                    statusEl: statusEl, publishBtn: publishBtn,
                };
            }
            // checa a cota diária do IG antes de confirmar (bloqueia se não couber)
            const needed = payload.all ? payload.list.length : 1;
            setStatus(statusEl, 'Checando cota do Instagram…', 'busy');
            const lim = await fetchLimit();
            setStatus(statusEl, '', '');
            if (lim && lim.remaining < needed) {
                setStatus(statusEl, 'Cota diária do IG: restam ' + lim.remaining + ' post(s) hoje'
                    + (needed > 1 ? ', mas isto precisa de ' + needed + '. Publique menos formatos ou tente amanhã.' : '. Tente amanhã.'), 'err');
                return;
            }
            payload.remaining = lim ? lim.remaining : null;
            openConfirmDialog(payload);
        });
    }

    // ======================================================================
    //  Confirmação "AO VIVO" + publicação
    // ======================================================================
    function openConfirmDialog(ctx) {
        const overlay = makeOverlay('adm-overlay', 'Confirmar publicação no Instagram');
        const modal = document.createElement('div');
        modal.className = 'adm-modal adm-modal--confirm';
        modal.innerHTML =
            '<div class="adm-modal-head">'
            + '<span class="adm-dot adm-dot--live"></span>'
            + '<h2 id="adm-confirm-title">Publicar AO VIVO?</h2>'
            + '<button type="button" class="adm-x" data-close aria-label="Fechar">' + X_ICON + '</button>'
            + '</div>'
            + '<p class="adm-confirm-lead">Isto vai publicar <b>ao vivo</b> em <b>@minutoreal1701</b>.</p>'
            + (ctx.all
                ? '<dl class="adm-confirm-meta"><div><dt>Formatos</dt><dd>'
                    + ctx.list.map((i) => escapeHtml(i.label)).join(' · ')
                    + '</dd></div><div><dt>Total</dt><dd>' + ctx.list.length + ' posts (1 de cada)</dd></div></dl>'
                : '<dl class="adm-confirm-meta">'
                    + '<div><dt>Formato</dt><dd>' + escapeHtml(ctx.formatLabel) + '</dd></div>'
                    + '<div><dt>Peça</dt><dd>' + escapeHtml(String(ctx.pieceLabel)) + '</dd></div></dl>')
            + (ctx.remaining != null
                ? '<p class="adm-confirm-quota">Cota do Instagram: restam <b>' + ctx.remaining + '</b> post(s) hoje.</p>'
                : '')
            + '<div class="adm-actions">'
            + '  <button type="button" class="adm-btn adm-btn--live" data-confirm>Publicar agora</button>'
            + '  <button type="button" class="adm-btn adm-btn--ghost" data-close>Cancelar</button>'
            + '</div>';
        overlay.appendChild(modal);
        overlay.setAttribute('aria-labelledby', 'adm-confirm-title');
        document.body.appendChild(overlay);

        wireClose(overlay);
        const confirmBtn = modal.querySelector('[data-confirm]');
        setTimeout(() => { try { confirmBtn.focus(); } catch (e) {} }, 30);

        confirmBtn.addEventListener('click', async () => {
            closeOverlay(overlay);
            if (ctx.all) await doPublishAll(ctx);
            else await doPublish(ctx);
        });
    }

    // publica 1 de cada formato, em sequência, com progresso + resumo final.
    async function doPublishAll(ctx) {
        const { list, caption, statusEl, publishBtn } = ctx;
        publishBtn.disabled = true;
        const results = [];
        for (let i = 0; i < list.length; i++) {
            const item = list[i];
            setStatus(statusEl, 'Publicando ' + item.label + '… (' + (i + 1) + '/' + list.length + ')', 'busy');
            const cap = isStory(item.type) ? '' : caption;
            let data = null, ok = false;
            try {
                const res = await apiPost('admin/instagram/publish', {
                    book: BIBLIOTECA_BOOK, type: item.type, selector: item.selector, caption: cap, confirm: true,
                });
                data = await safeJson(res);
                ok = res.ok && data && data.ok;
            } catch (e) { ok = false; }
            results.push({ label: item.label, ok: ok, err: (data && data.error) || '' });
            // respiro entre posts (educado com a API; não pausa após o último)
            if (i < list.length - 1) {
                setStatus(statusEl, item.label + ' ' + (ok ? '✓' : '✗') + ' · aguardando (respiro)…', 'busy');
                await sleep(PAUSE_MS);
            }
        }
        const okN = results.filter((r) => r.ok).length;
        const summary = results.map((r) => r.label + ' ' + (r.ok ? '✓' : '✗')).join(' · ');
        if (okN === list.length) {
            setStatus(statusEl, 'Tudo publicado ✓ · ' + summary, 'ok');
        } else {
            const firstErr = (results.find((r) => !r.ok) || {}).err;
            setStatus(statusEl, okN + '/' + list.length + ' ok · ' + summary + (firstErr ? ' · ' + firstErr : ''), 'err');
        }
        publishBtn.disabled = false;
    }

    async function doPublish(ctx) {
        const { statusEl, publishBtn } = ctx;
        publishBtn.disabled = true;
        setStatus(statusEl, 'montando…', 'busy');

        // pequena transição de rótulo "publicando…" (feedback de etapa).
        // O backend trata a montagem+publicação no mesmo POST; o segundo estado
        // só marca progresso para o usuário, não dispara outra chamada.
        const stage2 = setTimeout(() => setStatus(statusEl, 'publicando…', 'busy'), 600);

        let data = null, ok = false;
        try {
            const res = await apiPost('admin/instagram/publish', {
                book: ctx.book,
                type: ctx.type,
                selector: ctx.selector,
                caption: ctx.caption,
                confirm: true,
            });
            data = await safeJson(res);
            ok = res.ok;
        } catch (e) { ok = false; }
        clearTimeout(stage2);

        if (ok && data && data.ok) {
            const link = data.permalink;
            if (link) {
                setStatusHtml(statusEl,
                    'Publicado ✓ <a class="adm-permalink" href="' + escapeAttr(link)
                    + '" target="_blank" rel="noopener">' + LINK_ICON + 'ver no Instagram</a>',
                    'ok');
            } else {
                setStatus(statusEl, 'Publicado ✓' + (data.mediaId ? ' (id ' + data.mediaId + ')' : ''), 'ok');
            }
        } else {
            const msg = (data && data.error) ? data.error : 'Falha ao publicar. Tente de novo.';
            setStatus(statusEl, msg, 'err');
        }
        publishBtn.disabled = false;
    }

    // ======================================================================
    //  YouTube — publica o vídeo do livro
    // ======================================================================
    function confirmYT(btn, statusEl) {
        const overlay = makeOverlay('adm-overlay', 'Confirmar publicação no YouTube');
        const modal = document.createElement('div');
        modal.className = 'adm-modal adm-modal--confirm';
        modal.innerHTML =
            '<div class="adm-modal-head"><span class="adm-dot adm-dot--live"></span>'
            + '<h2>Publicar no YouTube?</h2>'
            + '<button type="button" class="adm-x" data-close aria-label="Fechar">' + X_ICON + '</button></div>'
            + '<p class="adm-confirm-lead">Vai publicar o <b>vídeo</b> de <b>' + escapeHtml(BIBLIOTECA_BOOK)
            + '</b> no canal (privacidade: <b>não listado</b>).</p>'
            + '<div class="adm-actions">'
            + '  <button type="button" class="adm-btn adm-btn--live" data-confirm>Publicar agora</button>'
            + '  <button type="button" class="adm-btn adm-btn--ghost" data-close>Cancelar</button>'
            + '</div>';
        overlay.appendChild(modal);
        document.body.appendChild(overlay);
        wireClose(overlay);
        modal.querySelector('[data-confirm]').addEventListener('click', async () => {
            closeOverlay(overlay);
            await doPublishYT(btn, statusEl);
        });
    }

    async function doPublishYT(btn, statusEl) {
        btn.disabled = true;
        setStatus(statusEl, 'enviando vídeo ao YouTube…', 'busy');
        let data = null, ok = false;
        try {
            const res = await apiPost('admin/youtube/publish', { book: BIBLIOTECA_BOOK, confirm: true, privacy: 'unlisted' });
            data = await safeJson(res);
            ok = res.ok;
        } catch (e) { ok = false; }
        if (ok && data && data.ok) {
            if (data.dryRun) {
                setStatus(statusEl, 'Dry-run ✓ — "' + (data.title || '') + '" (não publicado; modo teste ligado).', 'ok');
            } else if (data.url) {
                setStatusHtml(statusEl, 'Publicado ✓ <a class="adm-permalink" href="' + escapeAttr(data.url)
                    + '" target="_blank" rel="noopener">' + LINK_ICON + 'ver no YouTube</a>', 'ok');
            } else {
                setStatus(statusEl, 'Publicado ✓', 'ok');
            }
        } else {
            setStatus(statusEl, (data && data.error) ? data.error : 'Falha ao publicar no YouTube.', 'err');
        }
        btn.disabled = false;
    }

    // ======================================================================
    //  Painel "Publicar um livro" (admin + HOME) — upload → skill → site
    // ======================================================================
    // Passos do pipeline, na ordem; `pct` = quanto a barra enche ao chegar nele.
    // O worker grava o `stage` (ia/gate/build/ready) no job → a barra é DESCRITIVA.
    const UP_STEPS = [
        { key: 'upload', short: 'Enviando', label: 'Enviando o arquivo', pct: 18 },
        { key: 'queued', short: 'Na fila', label: 'Na fila', pct: 26 },
        { key: 'ia', short: 'Gerando com IA', label: 'Lendo o livro e gerando o resumo com IA', pct: 66 },
        { key: 'gate', short: 'Validando', label: 'Validando a qualidade', pct: 82 },
        { key: 'build', short: 'Montando o site', label: 'Montando as páginas e o kit', pct: 93 },
        { key: 'ready', short: 'Pronto', label: 'Pronto para revisão', pct: 100 },
    ];
    const UP_HINT = { ia: ' — pode levar alguns minutos' };

    function injectUploadPanel() {
        if (document.querySelector('.adm-upload-panel')) return; // idempotente
        const panel = document.createElement('section');
        panel.className = 'adm-panel adm-upload-panel';
        panel.setAttribute('aria-label', 'Publicar um livro');
        const steps = UP_STEPS.map((s) => '<li data-st="' + s.key + '"><span class="adm-prog-dot"></span>'
            + escapeHtml(s.short) + '</li>').join('');
        panel.innerHTML =
            '<div class="adm-panel-head">'
            + '<div class="adm-panel-titles">'
            + '  <span class="adm-panel-title">Publicar um livro</span>'
            + '  <span class="adm-panel-sub">sobe o arquivo → vira resumo → você revisa → publica</span>'
            + '</div>'
            + '<button type="button" class="adm-x" data-logout aria-label="Sair">' + OUT_ICON + '</button>'
            + '</div>'
            + '<div class="adm-panel-body">'
            + '  <form class="adm-up-form" novalidate>'
            + '    <label class="adm-field"><span>Arquivo do livro (.pdf .epub .txt .docx .md)</span>'
            + '      <input type="file" name="book" accept=".pdf,.epub,.txt,.docx,.md,.html,.rtf" required></label>'
            + '    <label class="adm-field"><span>Slug (opcional — kebab-case, ex.: a-arte-da-guerra)</span>'
            + '      <input type="text" name="slug" autocomplete="off" autocapitalize="off" spellcheck="false"></label>'
            + '    <div class="adm-actions"><button type="submit" class="adm-btn adm-btn--solid">Enviar e gerar</button></div>'
            + '  </form>'
            + '  <div class="adm-prog" hidden aria-live="polite">'
            + '    <div class="adm-prog-track"><div class="adm-prog-fill"></div></div>'
            + '    <p class="adm-prog-label"></p>'
            + '    <ol class="adm-prog-steps">' + steps + '</ol>'
            + '  </div>'
            + '  <p class="adm-status adm-up-status" role="status" aria-live="polite"></p>'
            + '  <div class="adm-up-review" hidden></div>'
            + '</div>';
        const anchor = document.querySelector('header');
        if (anchor) anchor.insertAdjacentElement('afterend', panel);
        else document.body.insertBefore(panel, document.body.firstChild);
        panel.querySelector('[data-logout]').addEventListener('click', () => doLogout(panel));

        const ui = {
            form: panel.querySelector('.adm-up-form'),
            statusEl: panel.querySelector('.adm-up-status'),
            progEl: panel.querySelector('.adm-prog'),
            reviewEl: panel.querySelector('.adm-up-review'),
        };
        ui.form.addEventListener('submit', (e) => { e.preventDefault(); startUpload(ui); });
    }

    // pinta a barra no passo `key`; `uploadFrac` (0..1) só vale no passo 'upload'.
    function setProgress(progEl, key, uploadFrac) {
        progEl.hidden = false;
        const idx = UP_STEPS.findIndex((s) => s.key === key);
        const step = UP_STEPS[idx] || UP_STEPS[0];
        const pct = (key === 'upload' && typeof uploadFrac === 'number')
            ? Math.round(uploadFrac * step.pct) : step.pct;
        const fill = progEl.querySelector('.adm-prog-fill');
        fill.style.width = pct + '%';
        fill.classList.toggle('working', key !== 'ready'); // shimmer enquanto trabalha
        progEl.querySelector('.adm-prog-label').textContent = step.label + (UP_HINT[key] || '');
        progEl.querySelectorAll('.adm-prog-steps li').forEach((li) => {
            const i = UP_STEPS.findIndex((s) => s.key === li.getAttribute('data-st'));
            li.classList.toggle('done', i < idx || key === 'ready');
            li.classList.toggle('active', i === idx && key !== 'ready');
        });
    }

    // upload via XHR p/ ter o % REAL do envio (fetch não expõe progresso de upload).
    function xhrUpload(url, fd, onFrac) {
        return new Promise((resolve) => {
            const xhr = new XMLHttpRequest();
            xhr.open('POST', url);
            xhr.withCredentials = true;
            if (xhr.upload) xhr.upload.onprogress = (e) => {
                if (e.lengthComputable) onFrac(e.loaded / e.total);
            };
            xhr.onload = () => {
                let j = null; try { j = JSON.parse(xhr.responseText); } catch (e) { /* sem JSON */ }
                resolve({ ok: xhr.status >= 200 && xhr.status < 300, data: j });
            };
            xhr.onerror = () => resolve({ ok: false, data: null });
            xhr.send(fd);
        });
    }

    async function startUpload(ui) {
        const fileInput = ui.form.querySelector('input[name="book"]');
        const slug = ui.form.querySelector('input[name="slug"]').value.trim();
        if (!fileInput.files || !fileInput.files[0]) { setStatus(ui.statusEl, 'Escolha um arquivo.', 'err'); return; }
        const submitBtn = ui.form.querySelector('button[type="submit"]');
        submitBtn.disabled = true;
        ui.reviewEl.hidden = true; ui.reviewEl.innerHTML = '';
        setStatus(ui.statusEl, '', ''); // limpa erro de tentativa anterior
        setProgress(ui.progEl, 'upload', 0);
        const fd = new FormData();
        fd.append('book', fileInput.files[0]);
        if (slug) fd.append('slug', slug);
        const res = await xhrUpload(apiUrl('admin/upload'), fd, (frac) => setProgress(ui.progEl, 'upload', frac));
        if (!res.ok || !res.data || !res.data.jobId) {
            submitBtn.disabled = false; ui.progEl.hidden = true;
            setStatus(ui.statusEl, (res.data && res.data.error) ? res.data.error : 'Falha no upload.', 'err');
            return;
        }
        setProgress(ui.progEl, 'queued');
        pollJob(res.data.jobId, ui, submitBtn);
    }

    function pollJob(jobId, ui, submitBtn) {
        let tries = 0;
        const timer = setInterval(async () => {
            tries++;
            let s = null;
            try {
                const res = await apiGet('admin/upload/' + encodeURIComponent(jobId) + '/status');
                s = await safeJson(res);
            } catch (e) { return; }
            if (!s || !s.status) return;
            if (s.status === 'queued') setProgress(ui.progEl, 'queued');
            else if (s.status === 'processing') {
                // o worker grava stage = ia|gate|build; se faltar, mostra a 1ª (ia)
                const st = ['ia', 'gate', 'build'].indexOf(s.stage) >= 0 ? s.stage : 'ia';
                setProgress(ui.progEl, st);
            } else if (s.status === 'ready') {
                clearInterval(timer); setProgress(ui.progEl, 'ready');
                renderReview(jobId, s, ui, submitBtn);
            } else if (s.status === 'published') {
                clearInterval(timer); showPublished(ui, s.url); submitBtn.disabled = false;
            } else if (s.status === 'failed') {
                clearInterval(timer); ui.progEl.hidden = true;
                setStatus(ui.statusEl, s.error || 'Falhou ao gerar.', 'err'); submitBtn.disabled = false;
            }
            if (tries > 450) { clearInterval(timer); setStatus(ui.statusEl, 'demorou demais — confira o status mais tarde.', 'err'); submitBtn.disabled = false; }
        }, 4000);
    }

    function renderReview(jobId, s, ui, submitBtn) {
        const sm = s.summary || {};
        const caps = (sm.chapters != null) ? String(sm.chapters) : '—';
        ui.reviewEl.hidden = false;
        ui.reviewEl.innerHTML =
            '<div class="adm-up-card">'
            + '<p class="adm-up-lead">Gerado no staging (ainda <b>não</b> está no ar). Revise:</p>'
            + '<ul class="adm-up-meta">'
            + '<li><b>Título:</b> ' + escapeHtml(sm.title || s.slug || '—') + '</li>'
            + '<li><b>Autor:</b> ' + escapeHtml(sm.author || '—') + '</li>'
            + '<li><b>Capítulos:</b> ' + escapeHtml(caps) + '</li>'
            + '</ul>'
            + '<div class="adm-actions">'
            + '<button type="button" class="adm-btn adm-btn--live" data-pub>Publicar no site</button>'
            + '</div></div>';
        ui.reviewEl.querySelector('[data-pub]').addEventListener('click', async (e) => {
            const btn = e.currentTarget; btn.disabled = true;
            setStatus(ui.statusEl, 'publicando no site…', 'busy');
            let d = null, ok = false;
            try {
                const res = await apiPost('admin/upload/' + encodeURIComponent(jobId) + '/publish', {});
                d = await safeJson(res); ok = res.ok;
            } catch (er) { ok = false; }
            if (ok && d && d.ok) { showPublished(ui, d.url); submitBtn.disabled = false; }
            else { btn.disabled = false; setStatus(ui.statusEl, (d && d.error) ? d.error : 'Falha ao publicar.', 'err'); }
        });
    }

    function showPublished(ui, url) {
        ui.progEl.hidden = true;
        ui.reviewEl.hidden = true; ui.reviewEl.innerHTML = '';
        if (url) setStatusHtml(ui.statusEl, 'Publicado ✓ <a class="adm-permalink" href="' + escapeAttr(url)
            + '" target="_blank" rel="noopener">' + LINK_ICON + 'ver no site</a>', 'ok');
        else setStatus(ui.statusEl, 'Publicado ✓', 'ok');
    }

    // ======================================================================
    //  Logout
    // ======================================================================
    async function doLogout(panel) {
        try { await apiPost('auth/logout', {}); } catch (e) { /* segue mesmo offline */ }
        SESSION = null;
        if (panel) panel.remove();
        injectLoginAffordance();
    }

    // ======================================================================
    //  Utilidades (overlay, status, escaping, âncora)
    // ======================================================================
    function makeOverlay(cls, label) {
        const overlay = document.createElement('div');
        overlay.className = cls;
        overlay.setAttribute('role', 'dialog');
        overlay.setAttribute('aria-modal', 'true');
        overlay.setAttribute('aria-label', label);
        return overlay;
    }

    // ESC fecha; clique no fundo ou em [data-close] fecha. Padrão do kit/Pix.
    function wireClose(overlay) {
        function onKey(e) { if (e.key === 'Escape') closeOverlay(overlay); }
        overlay._onKey = onKey;
        document.addEventListener('keydown', onKey);
        overlay.addEventListener('click', (e) => {
            if (e.target === overlay || (e.target.closest && e.target.closest('[data-close]'))) {
                closeOverlay(overlay);
            }
        });
    }
    function closeOverlay(overlay) {
        if (!overlay) return;
        if (overlay._onKey) document.removeEventListener('keydown', overlay._onKey);
        overlay.remove();
    }

    // status inline com estados visuais (busy/ok/err); o aria-live anuncia.
    function setStatus(el, text, kind) {
        if (!el) return;
        el.textContent = text || '';
        applyStatusKind(el, kind, !!text);
    }
    function setStatusHtml(el, html, kind) {
        if (!el) return;
        el.innerHTML = html || '';
        applyStatusKind(el, kind, !!html);
    }
    function applyStatusKind(el, kind, visible) {
        el.classList.remove('is-busy', 'is-ok', 'is-err');
        if (kind === 'busy') el.classList.add('is-busy');
        else if (kind === 'ok') el.classList.add('is-ok');
        else if (kind === 'err') el.classList.add('is-err');
        el.classList.toggle('is-visible', visible);
    }

    function escapeHtml(s) {
        return String(s).replace(/[&<>"']/g, (c) => (
            { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]
        ));
    }
    function escapeAttr(s) { return escapeHtml(s); }

    // Espera a .kit-section aparecer (montada por script-livro.js, possivelmente
    // após um fetch). Tenta por ~1,2s; se não vier, usa header.header. Nunca lança.
    function waitForAnchor() {
        return new Promise((resolve) => {
            const header = document.querySelector('header.header');
            const existing = document.querySelector('.kit-section');
            if (existing) return resolve(existing);
            let tries = 0;
            const max = 24; // 24 × 50ms ≈ 1,2s
            const timer = setInterval(() => {
                const kit = document.querySelector('.kit-section');
                if (kit) { clearInterval(timer); resolve(kit); return; }
                if (++tries >= max) {
                    clearInterval(timer);
                    resolve(document.querySelector('.kit-section') || header || null);
                }
            }, 50);
        });
    }
})();
