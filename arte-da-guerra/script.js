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
    nav.setAttribute('aria-label', 'Ações: baixar em PDF e seguir o canal');
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

    // botão "Seguir" no Instagram do canal (@minutoreal1701) — ao lado dos PDFs.
    // Link direto (clicável) é o lever real de seguidores; clique medido via beacon.
    const IG_ICON = '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">'
        + '<rect x="3" y="3" width="18" height="18" rx="5" stroke="currentColor" stroke-width="2"/>'
        + '<circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="2"/>'
        + '<circle cx="17.5" cy="6.5" r="1.2" fill="currentColor"/></svg>';
    const seguir = document.createElement('a');
    seguir.className = 'pdf-btn';
    seguir.href = 'https://www.instagram.com/minutoreal1701';
    seguir.target = '_blank';
    seguir.rel = 'noopener';
    seguir.innerHTML = IG_ICON + '<span>Seguir no Instagram</span>';
    seguir.addEventListener('click', () => {
        if (location.hostname.endsWith('andregalgani.com.br')) {
            try { navigator.sendBeacon(prefix + 'pdf/hit?book=_seguir_ig'); } catch (e) { /* sem beacon, sem contagem */ }
        }
    });
    nav.appendChild(seguir);

    // botão "Inscreva-se" no YouTube (Minuto Real); sub_confirmation=1 abre o popup de inscrição
    const YT_ICON = '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">'
        + '<rect x="2" y="5" width="20" height="14" rx="4" stroke="currentColor" stroke-width="2"/>'
        + '<path d="M10 9.2l5 2.8-5 2.8z" fill="currentColor"/></svg>';
    const youtube = document.createElement('a');
    youtube.className = 'pdf-btn';
    youtube.href = 'https://www.youtube.com/channel/UC2N5xZ-gyCU3hNvH1QqNahA?sub_confirmation=1';
    youtube.target = '_blank';
    youtube.rel = 'noopener';
    youtube.innerHTML = YT_ICON + '<span>Inscreva-se no YouTube</span>';
    youtube.addEventListener('click', () => {
        if (location.hostname.endsWith('andregalgani.com.br')) {
            try { navigator.sendBeacon(prefix + 'pdf/hit?book=_youtube_sub'); } catch (e) { /* sem beacon, sem contagem */ }
        }
    });
    nav.appendChild(youtube);

    header.insertAdjacentElement('afterend', nav);
});
