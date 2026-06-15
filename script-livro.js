// script.js compartilhado das páginas de livro:
// (1) expansão dos cards com detalhes;
// (2) botões "Baixar PDF" com liberação via Pix (modal) — serviço /biblioteca/pdf/.
// PAYWALL desligado enquanto os PDFs amadurecem — religar aqui E no server.js do pdf-service.
const PAYWALL = false;
const BIBLIOTECA_BOOK = (() => {
    const src = (document.currentScript && document.currentScript.src) || '';
    const m = src.match(/\/([a-z0-9-]+)\/script\.js/);
    return m ? m[1] : '';
})();

document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.card').forEach(card => {
        card.addEventListener('click', () => {
            if (card.querySelector('.card-details')) card.classList.toggle('expanded');
        });
    });

    // Densidade: o bloco de Lições flui dentro das colunas do grid (como no PDF),
    // eliminando a coluna manca quando o número de cards é ímpar.
    document.querySelectorAll('.grid').forEach(grid => {
        const lessons = grid.nextElementSibling;
        if (lessons && lessons.classList.contains('lessons')) grid.appendChild(lessons);
    });

    if (!BIBLIOTECA_BOOK) return;
    const header = document.querySelector('header.header');
    if (!header) return;

    const ICON = '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">'
        + '<path d="M12 4v10m0 0l-4-4m4 4l4-4M5 20h14" stroke="currentColor" stroke-width="2" '
        + 'stroke-linecap="round" stroke-linejoin="round"/></svg>';

    const path = location.pathname;
    const isOverview = path.endsWith('/' + BIBLIOTECA_BOOK + '.html');
    const chapterMatch = path.match(new RegExp('/' + BIBLIOTECA_BOOK + '/([a-z0-9-]+)\\.html$'));
    const prefix = isOverview ? '' : '../'; // base relativa até /biblioteca/

    // contagem de visita (geral + por livro) — beacon anônimo, só em produção
    if (location.hostname.endsWith('andregalgani.com.br')) {
        try { navigator.sendBeacon(prefix + 'pdf/hit?book=' + BIBLIOTECA_BOOK); } catch (e) { /* sem beacon, sem contagem */ }
    }

    // ---------- Kit de Divulgação ----------
    // Aparece só onde existe assets/kit/<livro>/manifest.json (por enquanto: 1984).
    // Clicar ABRE a imagem no browser (lightbox); de lá pode baixar. Abrir conta
    // como um curtir daquele visitante (1 por usuário, igual ao joinha da estante)
    // — é o sinal de demanda que promove o livro à esteira.
    const EXPAND_ICON = '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">'
        + '<path d="M4 9V4h5M20 9V4h-5M4 15v5h5M20 15v5h-5" stroke="currentColor" stroke-width="2" '
        + 'stroke-linecap="round" stroke-linejoin="round"/></svg>';
    const SPARK_ICON = '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">'
        + '<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8L12 3z" stroke="currentColor" '
        + 'stroke-width="1.8" stroke-linejoin="round"/></svg>';
    const DL_ICON = '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">'
        + '<path d="M12 4v10m0 0l-4-4m4 4l4-4M5 20h14" stroke="currentColor" stroke-width="2" '
        + 'stroke-linecap="round" stroke-linejoin="round"/></svg>';
    const VOTEKEY = 'bib:meus-votos';
    function registerKitLike(book) {
        let votes = {};
        try { votes = JSON.parse(localStorage.getItem(VOTEKEY)) || {}; } catch (e) { votes = {}; }
        const from = votes[book] || 'none';
        if (from === 'up') return;           // já curtido — gerar de novo não recurte
        votes[book] = 'up';
        try { localStorage.setItem(VOTEKEY, JSON.stringify(votes)); } catch (e) { /* ignora */ }
        fetch(prefix + 'pdf/vote?book=' + encodeURIComponent(book) + '&from=' + from + '&to=up', { method: 'POST' }).catch(() => {});
    }
    function buildKit() {
        if (!isOverview) return;             // o kit vive na página principal do livro
        fetch(prefix + 'assets/kit/' + BIBLIOTECA_BOOK + '/manifest.json')
            .then(r => (r.ok ? r.json() : null))
            .then(m => { if (m && Array.isArray(m.assets) && m.assets.length) renderKit(m); })
            .catch(() => { /* sem manifesto, sem kit */ });
    }
    function renderKit(m) {
        // dropdown nativo, FECHADO por padrão — não pesa o topo da página
        const sec = document.createElement('details');
        sec.className = 'kit-section';
        const sum = document.createElement('summary');
        sum.className = 'kit-summary';
        sum.innerHTML = '<span class="kit-summary-text">' + (m.title || 'Kit de Divulgação')
            + '<span class="kit-summary-count">' + m.assets.length + ' imagens</span></span>'
            + '<span class="kit-arrow" aria-hidden="true">▾</span>';
        sec.appendChild(sum);
        if (m.intro) {
            const p = document.createElement('p');
            p.className = 'kit-intro';
            p.textContent = m.intro;
            sec.appendChild(p);
        }
        const grid = document.createElement('div');
        grid.className = 'kit-grid';
        const ondemand = !!m.ondemand;
        m.assets.forEach(a => {
            const card = document.createElement('button');
            card.type = 'button';
            card.className = 'kit-card';
            const thumb = document.createElement('span');
            thumb.className = 'kit-thumb';
            if (a.w && a.h) thumb.style.aspectRatio = a.w + ' / ' + a.h;
            const info = document.createElement('span');
            info.className = 'kit-info';
            info.innerHTML = '<span class="kit-label">' + a.label + '</span>'
                + '<span class="kit-sub">' + a.rede + ' · ' + a.fmt + '</span>';
            const corner = document.createElement('span');
            corner.className = 'kit-dl';
            if (ondemand) {
                card.title = 'Gerar ' + a.label + ' (' + a.fmt + ')';
                thumb.classList.add('kit-thumb--empty');
                thumb.innerHTML = '<span class="kit-gen">' + SPARK_ICON + '<span class="kit-gen-label">Gerar</span></span>';
                corner.innerHTML = SPARK_ICON;
                card.append(thumb, info, corner);
                card.addEventListener('click', () => genAndShow(a, card));
            } else {
                card.title = 'Abrir ' + a.label + ' (' + a.fmt + ')';
                thumb.innerHTML = '<img src="' + prefix + (a.thumb || a.href) + '" loading="lazy" alt="' + a.label + ' — ' + a.fmt + '">';
                corner.innerHTML = EXPAND_ICON;
                card.append(thumb, info, corner);
                card.addEventListener('click', () => openKitLightbox(a, prefix + a.href));
            }
            grid.appendChild(card);
        });
        sec.appendChild(grid);
        const anchor = document.querySelector('.pdf-actions') || header;
        anchor.insertAdjacentElement('afterend', sec);
    }
    // chama a "função de geração" do formato no servidor (gera no 1º clique;
    // depois serve o cache) e apresenta o resultado. Gerar = curtir.
    function genAndShow(a, card) {
        if (card.classList.contains('is-generating')) return;
        registerKitLike(BIBLIOTECA_BOOK);
        const url = prefix + 'pdf/asset/' + BIBLIOTECA_BOOK + '/' + a.id + '.png';
        const label = card.querySelector('.kit-gen-label');
        card.classList.add('is-generating');
        if (label) label.textContent = 'Gerando…';
        const img = new Image();
        img.onload = () => {
            card.classList.remove('is-generating');
            card.classList.add('is-generated');
            const thumb = card.querySelector('.kit-thumb');
            thumb.classList.remove('kit-thumb--empty');
            thumb.innerHTML = '';
            const t = new Image(); t.src = url; t.alt = a.label + ' — ' + a.fmt;
            thumb.appendChild(t);
            const corner = card.querySelector('.kit-dl');
            if (corner) corner.innerHTML = EXPAND_ICON;
            openKitLightbox(a, url);
        };
        img.onerror = () => {
            card.classList.remove('is-generating');
            if (label) label.textContent = 'Erro — tente de novo';
        };
        img.src = url;
    }
    // apresenta o asset no browser; abrir = curtir
    function openKitLightbox(a, srcUrl) {
        registerKitLike(BIBLIOTECA_BOOK);
        const overlay = document.createElement('div');
        overlay.className = 'kit-overlay';
        overlay.setAttribute('role', 'dialog');
        overlay.setAttribute('aria-modal', 'true');
        overlay.setAttribute('aria-label', a.label + ' — ' + a.fmt);
        const fig = document.createElement('figure');
        fig.className = 'kit-lightbox';
        fig.innerHTML =
            '<span class="kit-lb-img"><img src="' + srcUrl + '" alt="' + a.label + ' — ' + a.fmt + '"></span>'
            + '<figcaption class="kit-cap">'
            + '<span class="kit-cap-meta"><b>' + a.label + '</b> · ' + a.rede + ' · ' + a.fmt + '</span>'
            + '<span class="kit-cap-actions">'
            + '<a class="pdf-btn" href="' + srcUrl + '" download>' + DL_ICON + '<span>Baixar imagem</span></a>'
            + '<button type="button" class="pdf-btn" data-close>Fechar</button>'
            + '</span></figcaption>';
        overlay.appendChild(fig);
        document.body.appendChild(overlay);
        function close() { document.removeEventListener('keydown', onKey); overlay.remove(); }
        function onKey(e) { if (e.key === 'Escape') close(); }
        document.addEventListener('keydown', onKey);
        overlay.addEventListener('click', (e) => {
            if (e.target === overlay || (e.target.closest && e.target.closest('[data-close]'))) close();
        });
    }
    buildKit();

    const items = [];
    if (isOverview) {
        items.push(['visao-geral', 'Visão geral em PDF']);
        items.push(['livro-completo', 'Resumo completo em PDF']);
    } else if (chapterMatch) {
        items.push([chapterMatch[1], 'Baixar em PDF']);
    }
    if (!items.length) return;

    // ---------- modal Pix ----------
    function openPixModal(page) {
        const overlay = document.createElement('div');
        overlay.className = 'pix-overlay';
        overlay.setAttribute('role', 'dialog');
        overlay.setAttribute('aria-modal', 'true');
        overlay.setAttribute('aria-label', 'Contribuição via Pix');

        const modal = document.createElement('div');
        modal.className = 'pix-modal';
        modal.innerHTML =
            '<h2 class="card-title">Apoie a Biblioteca</h2>'
            + '<p class="pix-amount">…</p>'
            + '<p class="pix-lead">Escaneie o QR ou use o copia-e-cola, e em seguida libere o seu PDF.</p>'
            + '<img class="pix-qr" alt="QR Code Pix" src="' + prefix + 'pdf/pix-qr.png">'
            + '<div class="pix-code" aria-label="Código Pix copia-e-cola">carregando…</div>'
            + '<div class="pix-actions">'
            + '  <button type="button" class="pdf-btn" data-act="copy">Copiar código Pix</button>'
            + '  <button type="button" class="pdf-btn" data-act="paid">Já fiz o Pix → baixar</button>'
            + '  <button type="button" class="pdf-btn" data-act="close">Fechar</button>'
            + '</div>'
            + '<p class="pix-note">O download é liberado por confiança — obrigado por apoiar este projeto. '
            + 'O link gerado vale por 90 minutos.</p>';
        overlay.appendChild(modal);
        document.body.appendChild(overlay);

        let pixCode = '';
        fetch(prefix + 'pdf/pix-info')
            .then(r => r.json())
            .then(info => {
                pixCode = info.code;
                modal.querySelector('.pix-amount').textContent = info.amount;
                modal.querySelector('.pix-code').textContent = info.code;
            })
            .catch(() => { modal.querySelector('.pix-code').textContent = 'Erro ao carregar o código Pix.'; });

        function close() {
            document.removeEventListener('keydown', onKey);
            overlay.remove();
        }
        function onKey(e) { if (e.key === 'Escape') close(); }
        document.addEventListener('keydown', onKey);
        overlay.addEventListener('click', (e) => { if (e.target === overlay) close(); });

        modal.addEventListener('click', (e) => {
            const act = e.target && e.target.getAttribute('data-act');
            if (!act) return;
            if (act === 'close') close();
            if (act === 'copy' && pixCode) {
                (navigator.clipboard ? navigator.clipboard.writeText(pixCode) : Promise.reject())
                    .then(() => { e.target.textContent = 'Copiado ✓'; })
                    .catch(() => { window.prompt('Copie o código Pix:', pixCode); });
            }
            if (act === 'paid') {
                e.target.textContent = 'Gerando…';
                // a aba precisa ser aberta DENTRO do gesto do usuário (senão o
                // navegador bloqueia o popup); a URL é atribuída após o fetch.
                const win = window.open('', '_blank');
                fetch(prefix + 'pdf/token', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ book: BIBLIOTECA_BOOK, page: page }),
                })
                    .then(r => r.json())
                    .then(({ t }) => {
                        const url = prefix + 'pdf/' + BIBLIOTECA_BOOK + '/' + page + '.pdf?t=' + encodeURIComponent(t);
                        if (win) { win.location = url; } else { window.location.href = url; }
                        close();
                    })
                    .catch(() => {
                        if (win) win.close();
                        e.target.textContent = 'Erro — tente de novo';
                    });
            }
        });
    }

    // ---------- botões ----------
    const nav = document.createElement('nav');
    nav.className = 'pdf-actions';
    nav.setAttribute('aria-label', 'Download em PDF');
    items.forEach(([page, label]) => {
        const a = document.createElement('a');
        a.className = 'pdf-btn';
        a.href = prefix + 'pdf/' + BIBLIOTECA_BOOK + '/' + page + '.pdf';
        a.innerHTML = ICON + '<span>' + label + '</span>';
        if (PAYWALL) {
            a.addEventListener('click', (e) => { e.preventDefault(); openPixModal(page); });
        } else {
            a.target = '_blank';
            a.rel = 'noopener';
        }
        nav.appendChild(a);
    });
    header.insertAdjacentElement('afterend', nav);
});
