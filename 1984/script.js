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
    // ícones de linha por tipo de peça (na gramática da marca, traço 2)
    const _SVG = (inner) => '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
        + 'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + inner + '</svg>';
    const KIT_ICONS = {
        quote: _SVG('<path d="M7 7h4v4c0 2-1 3-3 4M13 7h4v4c0 2-1 3-3 4"/>'),
        idea: _SVG('<path d="M9 18h6M10 21h4M12 3a6 6 0 0 1 4 10.5c-.7.7-1 1.2-1 2.5H9c0-1.3-.3-1.8-1-2.5A6 6 0 0 1 12 3Z"/>'),
        cover: _SVG('<path d="M5 4.5A1.5 1.5 0 0 1 6.5 3H18a1 1 0 0 1 1 1v16a1 1 0 0 1-1 1H6.5A1.5 1.5 0 0 1 5 19.5Z"/><path d="M5 17.5A1.5 1.5 0 0 1 6.5 16H19"/>'),
        link: _SVG('<path d="M9.5 14.5 14.5 9.5"/><path d="M11 7.5l1-1a3.5 3.5 0 0 1 5 5l-1 1"/><path d="M13 16.5l-1 1a3.5 3.5 0 0 1-5-5l1-1"/>'),
        carousel: _SVG('<rect x="8" y="6" width="8" height="12" rx="1.5"/><path d="M5 8v8M19 8v8"/>'),
    };
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
        if (isOverview) {
            // visão geral → kit do livro (pílulas)
            fetch(prefix + 'assets/kit/' + BIBLIOTECA_BOOK + '/manifest.json')
                .then(r => (r.ok ? r.json() : null))
                .then(m => { if (m && Array.isArray(m.assets) && m.assets.length) renderKit(m); })
                .catch(() => { /* sem manifesto, sem kit */ });
        } else if (chapterMatch) {
            // capítulo → carrossel daquele capítulo
            const cap = chapterMatch[1];
            fetch(prefix + 'assets/kit/' + BIBLIOTECA_BOOK + '/caps/' + cap + '/manifest.json')
                .then(r => (r.ok ? r.json() : null))
                .then(m => { if (m && Array.isArray(m.slides) && m.slides.length) renderChapterKit(m); })
                .catch(() => { /* capítulo sem carrossel */ });
        }
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
        // V1 — pílulas compactas (porte do botão de PDF): ícone + rótulo + formato esmaecido
        const pills = document.createElement('div');
        pills.className = 'kit-pills';
        const ondemand = !!m.ondemand;
        m.assets.forEach(a => {
            const pill = document.createElement('button');
            pill.type = 'button';
            pill.className = 'kit-pill';
            pill.title = (ondemand ? 'Gerar ' : 'Abrir ') + a.label + ' — ' + a.rede + ' · ' + a.fmt;
            pill.innerHTML = (KIT_ICONS[a.icon] || KIT_ICONS.quote)
                + '<span class="kit-pill__label">' + a.label + '</span>'
                + '<span class="kit-pill__fmt">· ' + (a.pill || (a.rede + ' · ' + a.fmt)) + '</span>';
            if (ondemand) pill.addEventListener('click', () => genAndShow(a, pill));
            else pill.addEventListener('click', () => openKitLightbox(a, prefix + a.href));
            pills.appendChild(pill);
        });
        sec.appendChild(pills);
        const anchor = document.querySelector('.pdf-actions') || header;
        anchor.insertAdjacentElement('afterend', sec);
    }
    // chama a "função de geração" do formato no servidor (gera no 1º clique;
    // depois serve o cache) e apresenta o resultado. Gerar = curtir.
    function genAndShow(a, pill) {
        if (pill.classList.contains('is-generating')) return;
        registerKitLike(BIBLIOTECA_BOOK);
        const url = prefix + 'pdf/asset/' + BIBLIOTECA_BOOK + '/' + a.id + '.png';
        const fmt = pill.querySelector('.kit-pill__fmt');
        const orig = fmt ? fmt.textContent : '';
        pill.classList.add('is-generating');
        if (fmt) fmt.textContent = '· Gerando…';
        const img = new Image();
        img.onload = () => {
            pill.classList.remove('is-generating');
            pill.classList.add('is-generated');
            if (fmt) fmt.textContent = orig;
            openKitLightbox(a, url);
        };
        img.onerror = () => {
            pill.classList.remove('is-generating');
            if (fmt) fmt.textContent = '· erro, tente de novo';
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
    // capítulo: dropdown com o carrossel daquele capítulo (abre o visualizador C3)
    function renderChapterKit(m) {
        const sec = document.createElement('details');
        sec.className = 'kit-section';
        const sum = document.createElement('summary');
        sum.className = 'kit-summary';
        sum.innerHTML = '<span class="kit-summary-text">Kit de Divulgação'
            + '<span class="kit-summary-count">carrossel do capítulo</span></span>'
            + '<span class="kit-arrow" aria-hidden="true">▾</span>';
        sec.appendChild(sum);
        const p = document.createElement('p');
        p.className = 'kit-intro';
        p.textContent = 'Um carrossel pronto sobre este capítulo — ' + m.count + ' slides no padrão da Biblioteca. Abrir conta como um curtir.';
        sec.appendChild(p);
        const pills = document.createElement('div');
        pills.className = 'kit-pills';
        const pill = document.createElement('button');
        pill.type = 'button';
        pill.className = 'kit-pill';
        pill.title = 'Ver o carrossel do capítulo (' + m.count + ' slides)';
        pill.innerHTML = KIT_ICONS.carousel
            + '<span class="kit-pill__label">Carrossel do capítulo</span>'
            + '<span class="kit-pill__fmt">· ' + m.count + ' slides · 4:5</span>';
        pill.addEventListener('click', () => { registerKitLike(BIBLIOTECA_BOOK); openCarousel(m); });
        pills.appendChild(pill);
        sec.appendChild(pills);
        const anchor = document.querySelector('.pdf-actions') || header;
        anchor.insertAdjacentElement('afterend', sec);
    }
    // visualizador C3: palco + trilho de miniaturas, navegação por teclado, baixar
    function openCarousel(m) {
        const view = (m.view || m.slides || []).map(s => prefix + s);  // webp leve p/ exibir
        const full = (m.slides || []).map(s => prefix + s);            // png cheio p/ baixar
        const total = view.length;
        if (!total) return;
        const pad = n => (n < 10 ? '0' : '') + n;
        let idx = 0;
        const overlay = document.createElement('div');
        overlay.className = 'cv-overlay';
        overlay.setAttribute('role', 'dialog');
        overlay.setAttribute('aria-modal', 'true');
        overlay.setAttribute('aria-label', 'Carrossel do capítulo');
        const rail = view.map((s, i) => '<button class="cv-thumb" data-i="' + i + '">'
            + '<img src="' + s + '" loading="lazy" alt="Miniatura do slide ' + (i + 1) + '">'
            + '<span class="cv-thumb-n">' + pad(i + 1) + '</span></button>').join('');
        const ZIP = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h7l2 2h7v12a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z"/><path d="M12 11v5m0 0l-2-2m2 2l2-2"/></svg>';
        overlay.innerHTML =
            '<header class="cv-head"><div class="cv-title"><span class="cv-dot"></span><h2>Carrossel do capítulo</h2>'
            + '<span class="cv-sub">· ' + total + ' slides · 1080×1350</span></div>'
            + '<button class="cv-close" data-close aria-label="Fechar"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg></button></header>'
            + '<div class="cv-stage"><button class="cv-nav" data-prev aria-label="Slide anterior"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 5l-7 7 7 7"/></svg></button>'
            + '<figure class="cv-frame"><span class="cv-counter"><b class="cv-cur">01</b> / ' + pad(total) + '</span>'
            + '<img class="cv-stage-img" src="' + view[0] + '" alt="Slide 1 do carrossel"></figure>'
            + '<button class="cv-nav" data-next aria-label="Próximo slide"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 5l7 7-7 7"/></svg></button></div>'
            + '<nav class="cv-rail" aria-label="Miniaturas">' + rail + '</nav>'
            + '<div class="cv-actions"><button class="cv-btn cv-btn--ghost" data-dl-slide>' + DL_ICON + 'Baixar este slide</button>'
            + (m.zip ? '<a class="cv-btn cv-btn--solid" href="' + prefix + m.zip + '" download>' + ZIP + 'Baixar carrossel (.zip)</a>' : '')
            + '</div>';
        document.body.appendChild(overlay);
        const stageImg = overlay.querySelector('.cv-stage-img');
        const curEl = overlay.querySelector('.cv-cur');
        const thumbs = overlay.querySelectorAll('.cv-thumb');
        function go(i) {
            idx = (i + total) % total;
            stageImg.src = view[idx];
            stageImg.alt = 'Slide ' + (idx + 1) + ' do carrossel';
            curEl.textContent = pad(idx + 1);
            thumbs.forEach(t => t.classList.toggle('is-active', Number(t.dataset.i) === idx));
        }
        go(0);
        overlay.querySelector('[data-prev]').addEventListener('click', () => go(idx - 1));
        overlay.querySelector('[data-next]').addEventListener('click', () => go(idx + 1));
        thumbs.forEach(t => t.addEventListener('click', () => go(Number(t.dataset.i))));
        overlay.querySelector('[data-dl-slide]').addEventListener('click', () => {
            const a = document.createElement('a');
            a.href = full[idx];
            a.download = BIBLIOTECA_BOOK + '-' + (m.chapter || 'cap') + '-' + pad(idx + 1) + '.png';
            document.body.appendChild(a); a.click(); a.remove();
        });
        function close() { document.removeEventListener('keydown', onKey); overlay.remove(); }
        function onKey(e) {
            if (e.key === 'ArrowLeft') go(idx - 1);
            else if (e.key === 'ArrowRight') go(idx + 1);
            else if (e.key === 'Escape') close();
        }
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
