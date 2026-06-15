document.addEventListener('DOMContentLoaded', () => {
    // contagem de visita da estante — beacon anônimo, só em produção
    if (location.hostname.endsWith('andregalgani.com.br')) {
        try { navigator.sendBeacon('pdf/hit?book=_estante'); } catch (e) { /* sem beacon, sem contagem */ }
    }

    const shelf = document.getElementById('bookshelf');
    const searchInput = document.getElementById('searchInput');
    const statusToggle = document.getElementById('statusToggle');
    const tagChipsEl = document.getElementById('tagChips');

    const CART_ICON = '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">'
        + '<path d="M3 4h2.5l2 11h10l2-8H7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'
        + '<circle cx="10" cy="20" r="1.5" fill="currentColor"/><circle cx="17" cy="20" r="1.5" fill="currentColor"/></svg>';
    // joinha (thumbs-up); o desjoinha reusa o mesmo ícone espelhado por CSS (scaleY(-1))
    const THUMB_ICON = '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">'
        + '<path d="M7 10v11H4a1 1 0 0 1-1-1v-9a1 1 0 0 1 1-1h3z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/>'
        + '<path d="M7 10l4-7a2 2 0 0 1 3.7 1.4L14 9h4.6a2 2 0 0 1 2 2.5l-1.7 7A2 2 0 0 1 17 22H7" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>'
        + '</svg>';

    let allBooks = [];
    const state = { status: 'tudo', tag: null, query: '' };

    // voto do próprio visitante (localStorage): { slug: 'up' | 'down' }
    const MYKEY = 'bib:meus-votos';
    let myVotes = {};
    try { myVotes = JSON.parse(localStorage.getItem(MYKEY)) || {}; } catch (e) { myVotes = {}; }
    const saveMyVotes = () => { try { localStorage.setItem(MYKEY, JSON.stringify(myVotes)); } catch (e) { /* ignora */ } };

    shelf.innerHTML = '<div class="skeleton skeleton-card"></div><div class="skeleton skeleton-card"></div>';

    // carrega o catálogo e as contagens de votos (ranking global) em paralelo
    Promise.all([
        fetch('books.json').then(r => { if (!r.ok) throw new Error('Falha ao carregar os livros.'); return r.json(); }),
        fetch('pdf/votes').then(r => r.ok ? r.json() : {}).catch(() => ({})),
    ]).then(([books, votes]) => {
        allBooks = books.map(b => {
            const v = votes[b.id] || {};
            return Object.assign({}, b, { _up: v.up || 0, _down: v.down || 0 });
        });
        if (searchInput) searchInput.placeholder = 'Pesquisar nas ' + books.length + ' obras — título ou autor…';
        buildStatusToggle();
        buildTagChips();
        render();
    }).catch(error => {
        console.error('Erro ao carregar books.json:', error);
        shelf.innerHTML = msg('Não foi possível carregar os livros. Verifique se a página está sendo servida por HTTP (ex: Live Server), não via file://.');
    });

    function msg(text) {
        return '<p class="grid-message">' + text + '</p>';
    }

    function buildStatusToggle() {
        if (!statusToggle) return;
        const prontos = allBooks.filter(b => !b.comingSoon).length;
        const opts = [
            ['tudo', 'Tudo', allBooks.length],
            ['pronto', 'Resumos prontos', prontos],
            ['embreve', 'Em breve', allBooks.length - prontos],
        ];
        statusToggle.innerHTML = '';
        opts.forEach(([key, label, n]) => {
            const b = document.createElement('button');
            b.type = 'button';
            b.textContent = label + ' (' + n + ')';
            b.setAttribute('aria-pressed', state.status === key);
            b.addEventListener('click', () => { state.status = key; buildStatusToggle(); render(); });
            statusToggle.appendChild(b);
        });
    }

    function buildTagChips() {
        if (!tagChipsEl) return;
        // conta livros por tag, ordena por frequência
        const freq = {};
        allBooks.forEach(b => (b.tags || []).forEach(t => { freq[t] = (freq[t] || 0) + 1; }));
        const tags = Object.entries(freq).sort((a, b) => b[1] - a[1]).map(([t]) => t);
        tagChipsEl.innerHTML = '';
        tags.forEach(tag => {
            const btn = document.createElement('button');
            btn.type = 'button';
            btn.className = 'tag-chip';
            btn.setAttribute('aria-pressed', state.tag === tag);
            btn.textContent = tag + ' (' + freq[tag] + ')';
            btn.addEventListener('click', () => {
                state.tag = (state.tag === tag) ? null : tag;
                buildTagChips();
                render();
            });
            tagChipsEl.appendChild(btn);
        });
    }

    // ranking: mais curtidos primeiro; empata por menos desjoinhas, depois prontos, depois título
    function rankSort(a, b) {
        if ((b._up || 0) !== (a._up || 0)) return (b._up || 0) - (a._up || 0);
        if ((a._down || 0) !== (b._down || 0)) return (a._down || 0) - (b._down || 0);
        const pa = a.comingSoon ? 1 : 0, pb = b.comingSoon ? 1 : 0;
        if (pa !== pb) return pa - pb;
        return a.title.localeCompare(b.title, 'pt');
    }

    function render() {
        const q = state.query.trim().toLowerCase();
        const statusOk = b => state.status === 'tudo' || (state.status === 'pronto' ? !b.comingSoon : !!b.comingSoon);
        const queryOk = b => !q || b.title.toLowerCase().includes(q) || b.author.toLowerCase().includes(q);

        shelf.innerHTML = '';

        const tagOk = b => !state.tag || (b.tags || []).includes(state.tag);
        let books = allBooks.filter(statusOk).filter(queryOk).filter(tagOk);
        if (!books.length) { shelf.innerHTML = msg('Nenhum livro encontrado.'); return; }
        books = books.slice().sort(rankSort);
        const title = q ? 'Resultados'
            : state.tag ? state.tag
            : state.status === 'pronto' ? 'Resumos prontos'
            : state.status === 'embreve' ? 'Em breve'
            : 'Acervo · do mais curtido ao menos';
        renderSection(title, books);
    }

    function renderSection(title, books) {
        const sec = document.createElement('section');
        sec.className = 'shelf-section';
        const h = document.createElement('h2');
        h.className = 'section-title';
        h.innerHTML = '<span>' + title + '</span><span class="section-count">' + books.length + (books.length === 1 ? ' livro' : ' livros') + '</span>';
        sec.appendChild(h);
        const grid = document.createElement('div');
        grid.className = 'shelf-grid';
        books.forEach((book, i) => grid.appendChild(makeCard(book, i)));
        sec.appendChild(grid);
        shelf.appendChild(sec);
    }

    function makeCard(book, index) {
        // wrapper: card + chip de compra + voto, sem aninhar <a>/<button> dentro do card
        const item = document.createElement('div');
        item.className = 'shelf-item animate-entrance';
        item.style.setProperty('--i', index);

        const bookEl = document.createElement('a');
        // "Em breve": card ainda sem página de resumo — não navega (sem href);
        // só o chip "Comprar" (afiliado) leva à Amazon.
        bookEl.className = book.comingSoon ? 'card card-soon' : 'card';
        if (!book.comingSoon) bookEl.href = book.url;
        bookEl.innerHTML = `
            <div class="card-cover">
                <img src="${book.coverUrl}" alt="Capa do livro ${book.title}" loading="lazy">
            </div>
            <div class="card-content">
                <div class="card-title">${book.title}</div>
                <p class="card-author">${book.author}</p>
                <p class="card-progress">${book.progress}</p>
            </div>
        `;
        item.appendChild(bookEl);

        if (book.amazon) {
            const buy = document.createElement('a');
            buy.className = 'card-buy';
            buy.href = book.amazon;
            buy.target = '_blank';
            buy.rel = 'nofollow sponsored noopener';
            buy.title = 'Comprar na Amazon';
            buy.setAttribute('aria-label', 'Comprar ' + book.title + ' na Amazon');
            buy.innerHTML = CART_ICON + '<span>Comprar</span>';
            item.appendChild(buy);
        }

        item.appendChild(makeVote(book));
        return item;
    }

    function makeVote(book) {
        const wrap = document.createElement('div');
        wrap.className = 'card-vote';
        ['up', 'down'].forEach(dir => {
            const btn = document.createElement('button');
            btn.type = 'button';
            btn.className = 'vote-btn ' + (dir === 'up' ? 'vote-up' : 'vote-down');
            const count = document.createElement('span');
            count.className = 'vote-count';
            btn.innerHTML = THUMB_ICON;
            btn.appendChild(count);
            btn.setAttribute('aria-label', (dir === 'up' ? 'Curtir ' : 'Não curtir ') + book.title);
            btn._refresh = () => {
                btn.setAttribute('aria-pressed', myVotes[book.id] === dir);
                count.textContent = dir === 'up' ? (book._up || 0) : (book._down || 0);
            };
            btn._refresh();
            btn.addEventListener('click', () => vote(book, dir, wrap));
            wrap.appendChild(btn);
        });
        return wrap;
    }

    function vote(book, dir, wrap) {
        const from = myVotes[book.id] || 'none';
        const to = from === dir ? 'none' : dir;

        // ajuste otimista local (some no fim do clique; o servidor confirma depois)
        if (from === 'up') book._up = Math.max(0, (book._up || 0) - 1);
        if (from === 'down') book._down = Math.max(0, (book._down || 0) - 1);
        if (to === 'up') book._up = (book._up || 0) + 1;
        if (to === 'down') book._down = (book._down || 0) + 1;
        if (to === 'none') delete myVotes[book.id]; else myVotes[book.id] = to;
        saveMyVotes();
        wrap.querySelectorAll('.vote-btn').forEach(b => b._refresh());

        // servidor (ranking global) — reconcilia a contagem com a resposta
        fetch('pdf/vote?book=' + encodeURIComponent(book.id) + '&from=' + from + '&to=' + to, { method: 'POST' })
            .then(r => r.ok ? r.json() : null)
            .then(v => {
                if (v && typeof v.up === 'number') {
                    book._up = v.up; book._down = v.down;
                    wrap.querySelectorAll('.vote-btn').forEach(b => b._refresh());
                }
            })
            .catch(() => { /* offline/local sem serviço: fica só o otimista */ });
    }

    if (searchInput) {
        searchInput.addEventListener('input', (e) => { state.query = e.target.value; render(); });
        // atalho "/" foca a busca, como em qualquer ferramenta séria
        document.addEventListener('keydown', (e) => {
            if (e.key === '/' && document.activeElement !== searchInput) {
                e.preventDefault();
                searchInput.focus();
            }
        });
    }
});
