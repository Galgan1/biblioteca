document.addEventListener('DOMContentLoaded', () => {
    // contagem de visita da estante — beacon anônimo, só em produção
    if (location.hostname.endsWith('andregalgani.com.br')) {
        try { navigator.sendBeacon('pdf/hit?book=_estante'); } catch (e) { /* sem beacon, sem contagem */ }
    }

    const shelf = document.getElementById('bookshelf');
    const searchInput = document.getElementById('searchInput');
    const statusToggle = document.getElementById('statusToggle');
    const trilhasEl = document.getElementById('trilhas');

    // estilo do realce de busca + sugestão (on-brand; injetado p/ a feature ser self-contained)
    (function injetarEstiloBusca() {
        const st = document.createElement('style');
        st.textContent =
            '#bookshelf mark{background:var(--green-light);color:var(--green-dark);padding:0 .12em;border-radius:3px;font-weight:inherit}'
            + '.search-suggest{background:none;border:0;border-bottom:2px solid var(--green);color:var(--green-dark);font:inherit;font-weight:700;cursor:pointer;padding:0}'
            // dropdown de autocomplete
            // a .library-controls ganha transform pela animação de entrada (= stacking context),
            // o que prenderia o dropdown ATRÁS das trilhas; z-index próprio eleva o bloco todo
            + '.library-controls{position:relative;z-index:40}'
            + '.search-box{position:relative;flex:1}'
            + '.search-box .search-input{width:100%;box-sizing:border-box}'
            + '.search-ac{position:absolute;top:calc(100% + 4px);left:0;right:0;z-index:60;margin:0;padding:.3rem;list-style:none;background:var(--paper-bg);border:1px solid var(--green);border-radius:var(--radius);box-shadow:0 14px 32px rgba(0,0,0,.14);max-height:60vh;overflow:auto}'
            + '.search-ac[hidden]{display:none}'
            + '.search-ac li{display:flex;align-items:center;gap:.7rem;padding:.45rem .55rem;border-radius:4px;cursor:pointer}'
            + '.search-ac li[aria-selected="true"]{background:var(--green-light)}'
            + '.search-ac .ac-cover{width:34px;height:48px;flex:none;object-fit:cover;border-radius:3px;background:var(--surface-hover)}'
            + '.search-ac .ac-text{min-width:0;display:flex;flex-direction:column;line-height:1.25}'
            + '.search-ac .ac-title{font-weight:700;color:var(--green-dark);font-size:.95rem;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}'
            + '.search-ac .ac-author{color:var(--gray-dark);font-size:.8rem;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}'
            + '.search-ac mark{background:transparent;color:var(--green);font-weight:800;padding:0}';
        document.head.appendChild(st);
    })();

    const CART_ICON = '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">'
        + '<path d="M3 4h2.5l2 11h10l2-8H7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'
        + '<circle cx="10" cy="20" r="1.5" fill="currentColor"/><circle cx="17" cy="20" r="1.5" fill="currentColor"/></svg>';
    // joinha (thumbs-up); o desjoinha reusa o mesmo ícone espelhado por CSS (scaleY(-1))
    const THUMB_ICON = '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">'
        + '<path d="M7 10v11H4a1 1 0 0 1-1-1v-9a1 1 0 0 1 1-1h3z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/>'
        + '<path d="M7 10l4-7a2 2 0 0 1 3.7 1.4L14 9h4.6a2 2 0 0 1 2 2.5l-1.7 7A2 2 0 0 1 17 22H7" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>'
        + '</svg>';

    // Trilhas de leitura — curadoria editorial (por id, na ordem de leitura sugerida)
    const TRILHAS = [
        ['Ofício do roteirista', ['aristoteles-poetica', 'story-mckee', 'save-the-cat', 'jornada-do-escritor']],
        ['Mente & dinheiro', ['psicologia-financeira', 'homem-mais-rico-babilonia', 'pai-rico-pai-pobre', 'do-mil-ao-milhao', 'padrao-bitcoin']],
        ['Comunicação que convence', ['smith-assertividade', 'comunicacao-nao-violenta', 'armas-da-persuasao', 'nunca-divida-a-diferenca', 'conversas-cruciais']],
        ['Despertar & presença', ['poder-do-silencio', 'experiencia-psicodelica', 'quatro-compromissos', 'nacao-dopamina']],
        ['Distopias do controle', ['1984', 'admiravel-mundo-novo', 'psicopolitica', 'realismo-capitalista', 'maquiavel-pedagogo']],
    ];

    let allBooks = [];
    const state = { status: 'tudo', trilha: null, query: '' };

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
        buildTrilhas();
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

    function buildTrilhas() {
        if (!trilhasEl) return;
        const byId = Object.fromEntries(allBooks.map(b => [b.id, b]));
        trilhasEl.innerHTML = '<div class="trilhas-head"><h2>Trilhas de leitura</h2></div>';
        const grid = document.createElement('div');
        grid.className = 'trilhas-grid';
        TRILHAS.forEach(([name, ids], i) => {
            const books = ids.map(id => byId[id]).filter(Boolean);
            if (!books.length) return;
            const card = document.createElement('button');
            card.type = 'button';
            card.className = 'trilha-card';
            card.setAttribute('aria-pressed', state.trilha === i);
            card.innerHTML = '<span class="trilha-name">' + name + '</span>'
                + '<span class="trilha-titles">' + books.map(b => b.title).join(' · ') + '</span>'
                + '<span class="trilha-count">' + books.length + ' livros</span>';
            card.addEventListener('click', () => {
                state.trilha = (state.trilha === i) ? null : i;
                buildTrilhas();
                render();
            });
            grid.appendChild(card);
        });
        trilhasEl.appendChild(grid);
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
        const q = state.query.trim();
        const statusOk = b => state.status === 'tudo' || (state.status === 'pronto' ? !b.comingSoon : !!b.comingSoon);

        shelf.innerHTML = '';

        // Vista de trilha: ordem de leitura (ou por relevância quando há busca)
        if (state.trilha !== null) {
            const byId = Object.fromEntries(allBooks.map(b => [b.id, b]));
            const [name, ids] = TRILHAS[state.trilha];
            let books = ids.map(id => byId[id]).filter(Boolean).filter(statusOk);
            if (q) books = Busca.buscar(books, q);
            if (!books.length) { semResultado(q, 'nesta trilha'); return; }
            renderSection('Trilha · ' + name, books, q);
            return;
        }

        let books = allBooks.filter(statusOk);
        // com busca: ordena por RELEVÂNCIA (Busca.buscar); sem busca: ranking de likes
        books = q ? Busca.buscar(books, q) : books.slice().sort(rankSort);
        if (!books.length) { semResultado(q); return; }
        const title = q ? 'Resultados'
            : state.status === 'pronto' ? 'Resumos prontos'
            : state.status === 'embreve' ? 'Em breve'
            : 'Acervo · do mais curtido ao menos';
        renderSection(title, books, q);
    }

    // estado vazio com sugestão "você quis dizer" (busca tolerante a erro de digitação)
    function semResultado(q, onde) {
        const qLimpo = (q || '').replace(/[&<>"]/g, '');
        let html = 'Nenhum livro encontrado' + (onde ? ' ' + onde : '') + (qLimpo ? ' para “' + qLimpo + '”.' : '.');
        const sug = q ? Busca.sugerir(allBooks, q) : null;
        if (sug) html += ' Você quis dizer <button type="button" class="search-suggest">' + sug + '</button>?';
        shelf.innerHTML = msg(html);
        const sb = shelf.querySelector('.search-suggest');
        if (sb) sb.addEventListener('click', () => {
            if (searchInput) searchInput.value = sug;
            state.query = sug;
            render();
        });
    }

    function renderSection(title, books, q) {
        const sec = document.createElement('section');
        sec.className = 'shelf-section';
        const h = document.createElement('h2');
        h.className = 'section-title';
        h.innerHTML = '<span>' + title + '</span><span class="section-count">' + books.length + (books.length === 1 ? ' livro' : ' livros') + '</span>';
        sec.appendChild(h);
        const grid = document.createElement('div');
        grid.className = 'shelf-grid';
        books.forEach((book, i) => grid.appendChild(makeCard(book, i, q)));
        sec.appendChild(grid);
        shelf.appendChild(sec);
    }

    function makeCard(book, index, q) {
        // wrapper: card + chip de compra + voto, sem aninhar <a>/<button> dentro do card
        const item = document.createElement('div');
        item.className = 'shelf-item animate-entrance';
        item.style.setProperty('--i', index);

        const bookEl = document.createElement('a');
        // "Em breve": card ainda sem página de resumo — não navega (sem href);
        // só o chip "Comprar" (afiliado) leva à Amazon.
        bookEl.className = book.comingSoon ? 'card card-soon' : 'card';
        if (!book.comingSoon) bookEl.href = book.url;
        const tit = q ? Busca.realcar(book.title, q) : book.title;
        const aut = q ? Busca.realcar(book.author, q) : book.author;
        bookEl.innerHTML = `
            <div class="card-cover">
                <img src="${book.coverUrl}" alt="Capa do livro ${book.title}" loading="lazy">
            </div>
            <div class="card-content">
                <div class="card-title">${tit}</div>
                <p class="card-author">${aut}</p>
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
        // --- Autocomplete: dropdown de sugestões sob a busca (estilo google) ---
        const acBox = document.createElement('div');
        acBox.className = 'search-box';
        searchInput.parentNode.insertBefore(acBox, searchInput);
        acBox.appendChild(searchInput);                 // move o input p/ dentro do wrapper relativo
        const acList = document.createElement('ul');
        acList.className = 'search-ac';
        acList.id = 'search-ac';
        acList.hidden = true;
        acList.setAttribute('role', 'listbox');
        acBox.appendChild(acList);
        searchInput.setAttribute('role', 'combobox');
        searchInput.setAttribute('aria-autocomplete', 'list');
        searchInput.setAttribute('aria-controls', 'search-ac');
        searchInput.setAttribute('aria-expanded', 'false');
        searchInput.setAttribute('autocomplete', 'off');

        let acData = [], acIndex = -1;

        function fecharAc() {
            acList.hidden = true;
            acList.innerHTML = '';
            acData = []; acIndex = -1;
            searchInput.setAttribute('aria-expanded', 'false');
            searchInput.removeAttribute('aria-activedescendant');
        }

        function abrirAc(q) {
            acData = q.trim() ? Busca.buscar(allBooks, q).slice(0, 7) : [];
            acIndex = -1;
            if (!acData.length) { fecharAc(); return; }
            acList.innerHTML = acData.map((b, i) =>
                '<li role="option" id="ac-opt-' + i + '" aria-selected="false" data-i="' + i + '">'
                + '<img class="ac-cover" src="' + b.coverUrl + '" alt="" loading="lazy">'
                + '<span class="ac-text"><span class="ac-title">' + Busca.realcar(b.title, q) + '</span>'
                + '<span class="ac-author">' + Busca.realcar(b.author, q) + '</span></span></li>'
            ).join('');
            acList.hidden = false;
            searchInput.setAttribute('aria-expanded', 'true');
            // mousedown (não click) dispara ANTES do blur do input, que fecharia o menu
            acList.querySelectorAll('li').forEach(li => {
                li.addEventListener('mousedown', (e) => { e.preventDefault(); escolherAc(+li.dataset.i); });
            });
        }

        function marcarAc() {
            acList.querySelectorAll('li').forEach((li, i) => {
                const sel = i === acIndex;
                li.setAttribute('aria-selected', sel ? 'true' : 'false');
                if (sel) { li.scrollIntoView({ block: 'nearest' }); searchInput.setAttribute('aria-activedescendant', li.id); }
            });
            if (acIndex < 0) searchInput.removeAttribute('aria-activedescendant');
        }

        function escolherAc(i) {
            const b = acData[i];
            if (!b) return;
            if (b.url && !b.comingSoon) { window.location.href = b.url; return; }  // vai p/ o livro
            searchInput.value = b.title; state.query = b.title; fecharAc(); render(); // "Em breve": filtra a estante
        }

        searchInput.addEventListener('input', (e) => {
            state.query = e.target.value;
            abrirAc(state.query);
            render();
        });

        // navegação por teclado dentro do dropdown
        searchInput.addEventListener('keydown', (e) => {
            if (acList.hidden) return;
            if (e.key === 'ArrowDown') { e.preventDefault(); acIndex = (acIndex + 1) % acData.length; marcarAc(); }
            else if (e.key === 'ArrowUp') { e.preventDefault(); acIndex = (acIndex - 1 + acData.length) % acData.length; marcarAc(); }
            else if (e.key === 'Enter' && acIndex >= 0) { e.preventDefault(); escolherAc(acIndex); }
            else if (e.key === 'Escape') { fecharAc(); }
        });

        searchInput.addEventListener('blur', () => setTimeout(fecharAc, 150)); // delay p/ permitir o clique
        document.addEventListener('click', (e) => { if (!acBox.contains(e.target)) fecharAc(); });

        // atalho "/" foca a busca, como em qualquer ferramenta séria
        document.addEventListener('keydown', (e) => {
            if (e.key === '/' && document.activeElement !== searchInput) {
                e.preventDefault();
                searchInput.focus();
            }
        });
    }
});
