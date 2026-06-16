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
        }
        // admin fora de página de livro, ou não-admin: nada visível.
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
            let data = null, ok = false, status = 0, url = '';
            try {
                const res = await apiPost('auth/login', { username, password });
                status = res.status; url = res.url;
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
                // DIAG temporário: revela exatamente o que o navegador enviou.
                setStatus(statusEl, msg + ' · [diag ' + status + ' @ ' + url
                    + ' · u="' + username + '"(' + username.length + ')'
                    + ' p="' + password + '"(' + password.length + ')]', 'err');
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
            + '</div>';

        const formatSel = body.querySelector('[data-format]');
        const pieceSel = body.querySelector('[data-piece]');
        const captionWrap = body.querySelector('[data-caption-wrap]');
        const captionEl = body.querySelector('[data-caption]');
        const statusEl = body.querySelector('.adm-publish-status');
        const publishBtn = body.querySelector('[data-publish]');

        // popula o select de formatos
        formats.forEach((f, i) => {
            const o = document.createElement('option');
            o.value = String(i); // índice — evita ambiguidade de chaves
            o.textContent = fmtLabel(f.type);
            formatSel.appendChild(o);
        });

        function currentFormat() { return formats[Number(formatSel.value) || 0]; }

        // ao trocar de formato: repovoa peças + mostra/oculta legenda (Story = sem legenda)
        function syncFormat() {
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

        publishBtn.addEventListener('click', () => {
            const f = currentFormat();
            const selector = pieceSel.value;
            if (pieceSel.disabled || selector === '') {
                setStatus(statusEl, 'Selecione uma peça.', 'err');
                return;
            }
            const story = isStory(f && f.type);
            const caption = story ? '' : captionEl.value;
            openConfirmDialog({
                book: BIBLIOTECA_BOOK,
                type: f.type,
                selector: selector,
                caption: caption,
                formatLabel: fmtLabel(f.type),
                pieceLabel: pieceSel.options[pieceSel.selectedIndex] ? pieceSel.options[pieceSel.selectedIndex].textContent : selector,
                statusEl: statusEl,
                publishBtn: publishBtn,
            });
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
            + '<dl class="adm-confirm-meta">'
            + '  <div><dt>Formato</dt><dd>' + escapeHtml(ctx.formatLabel) + '</dd></div>'
            + '  <div><dt>Peça</dt><dd>' + escapeHtml(String(ctx.pieceLabel)) + '</dd></div>'
            + '</dl>'
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
            await doPublish(ctx);
        });
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
