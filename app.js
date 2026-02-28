/**
 * ling-ling-etymon - Refined UI & Premium Essay Favorites
 */

// --- Application State ---
const State = {
    currentUser: localStorage.getItem('currentUser') || null,
    isPremium: localStorage.getItem('isPremium') === 'true',
    currentView: 'today',
    savedWordIds: JSON.parse(localStorage.getItem('savedWords') || '[]'),
    savedEssayIds: JSON.parse(localStorage.getItem('savedEssays') || '[]'),
    todayWord: null,
    searchFilter: null,
    letterFilter: null,

    // UI Settings
    fontSize: parseInt(localStorage.getItem('set_fontSize') || '16'),
    theme: localStorage.getItem('set_theme') || 'dark'
};

// --- DOM Elements ---
const viewContainer = document.getElementById('view-container');
const navItems = {
    today: document.getElementById('nav-today'),
    archive: document.getElementById('nav-archive'),
    saved: document.getElementById('nav-saved'),
    contribute: document.getElementById('nav-contribute'),
    essays: document.getElementById('nav-essays'),
    settings: document.getElementById('nav-settings'),
    premium: document.getElementById('nav-premium')
};

const API_BASE = window.location.origin;

// --- Utils ---
async function apiGet(endpoint) {
    try { const response = await fetch(`${API_BASE}${endpoint}`); return response.json(); }
    catch (e) { console.error(e); return []; }
}
async function apiPost(endpoint, data) {
    try {
        const response = await fetch(`${API_BASE}${endpoint}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        return response.json();
    } catch (e) { return { status: 'error', message: 'Connection failed' }; }
}

function applySettings() {
    document.documentElement.style.fontSize = State.fontSize + 'px';
    document.body.className = `theme-${State.theme}`;
    Object.keys(navItems).forEach(k => { if (navItems[k]) navItems[k].classList.remove('active'); });
    if (navItems[State.currentView]) navItems[State.currentView].classList.add('active');
}

// --- View Controllers ---

async function renderToday() {
    const word = State.todayWord;
    if (!word) { viewContainer.innerHTML = `<div class="empty-msg">No word found.</div>`; return; }

    viewContainer.innerHTML = `
        <article class="word-card fade-in">
            <header class="word-header" style="position: relative;">
                <span class="section-label">Word</span>
                <h2 class="word-title" style="font-size: 3rem; margin: 0.5rem 0;">${word.word}</h2>
                <div class="etymology-box">
                    <span class="section-label">Structure ${!State.isPremium ? '🔒' : ''}</span>
                    <div class="etymology-breakdown" style="font-size: 1.1rem; margin-top:0.5rem;">
                        ${word.etymology.breakdown.map(b => `
                            <span class="morpheme-link" data-term="${b.text}" style="cursor:${State.isPremium ? 'pointer' : 'default'}">
                                <span class="morpheme-text" style="color:${State.isPremium ? 'var(--color-accent)' : 'inherit'}; font-weight:bold;">${b.text}</span>
                                <span class="morpheme-meaning">（${b.meaning}）</span>
                            </span>
                        `).join(' + ')}
                    </div>
                </div>
                <button class="save-btn ${State.savedWordIds.includes(word.id) ? 'active' : ''}" data-id="${word.id}" style="position:absolute; top:0; right:0; background:none; border:none; font-size:1.5rem; cursor:pointer;">
                    ${State.savedWordIds.includes(word.id) ? '🔖' : '📑'}
                </button>
            </header>

            <section class="section"><span class="section-label">Essence</span><p class="concept-text" style="font-size: 1.25rem;">${word.core_concept.ja}</p></section>
            
            <section class="section">
                <span class="section-label">Philological Layers</span>
                <div class="thinking-text" style="font-size: 1.1rem; line-height: 1.8;">
                    ${(word.thinking_layer || '').split('\n').map(l => l.trim() ? `<p style="margin-bottom:1.2rem;">${l}</p>` : '').join('')}
                </div>
            </section>
            
            <div style="display:grid; grid-template-columns: 1fr 1fr; gap:1.2rem; margin-bottom: 2.5rem;">
                <section class="section" style="background:rgba(255,255,255,0.03); padding:1.2rem; border-radius:16px;"><span class="section-label">Synonyms</span><div style="display:flex; flex-wrap:wrap; gap:0.5rem; margin-top:0.5rem;">${(word.synonyms || []).map(s => `<span class="chip">${s}</span>`).join('') || '--'}</div></section>
                <section class="section" style="background:rgba(255,255,255,0.03); padding:1.2rem; border-radius:16px;"><span class="section-label">Antonyms</span><div style="display:flex; flex-wrap:wrap; gap:0.5rem; margin-top:0.5rem;">${(word.antonyms || []).map(a => `<span class="chip">${a}</span>`).join('') || '--'}</div></section>
            </div>

            <section class="section aftertaste-section" style="border-left: 2px solid var(--color-accent); padding-left: 1.5rem;"><span class="section-label">Resonance</span><p class="aftertaste-text" style="font-family: 'Times New Roman', serif; font-style: italic; font-size: 1.3rem;">${word.aftertaste}</p></section>

            <footer style="margin-top: 3rem; padding-top: 1.5rem; border-top: 1px solid var(--color-border); display:flex; justify-content:space-between; opacity:0.5; font-size:0.8rem;">
                <div>Source: ${word.source || '--'}</div>
                <div>by <b>${word.author || 'etymon_official'}</b></div>
            </footer>
            
            <div class="deep-dive">${State.isPremium ? renderDeepDiveContent(word) : renderDeepDiveLock()}</div>

            ${renderReflectionSection(word.id)}
        </article>
    `;

    if (State.isPremium) loadReflections(word.id);
    document.querySelectorAll('.morpheme-link').forEach(l => l.onclick = () => { if (!State.isPremium) return navigate('premium'); State.searchFilter = l.dataset.term; navigate('archive'); });
}

function renderReflectionSection(targetId) {
    return `
        <section class="section reflections-section" style="margin-top:5rem; border-top: 2px solid var(--color-border); padding-top:3rem;">
            <h3 class="section-label" style="font-size: 1.3rem; letter-spacing: 0.1em;">Reflections</h3>
            <div id="reflection-list" style="margin: 2rem 0;">
                ${State.isPremium ? '<p class="dimmed">Gathering thoughts...</p>' : '<div class="lock-container" onclick="navigate(\'premium\')" style="padding:1.5rem; border-radius:12px; cursor:pointer;">🔒 Premiumメンバーのみ他の思索を閲覧できます</div>'}
            </div>
            <div class="reflection-form" style="background:var(--color-surface); padding:2rem; border-radius:20px;">
                <textarea id="ref-input" maxlength="300" placeholder="この言葉へのリフレクションを記す（200〜300字）" style="width:100%; min-height:120px; background:transparent; color:white; border:1px solid var(--color-border); border-radius:12px; padding:1.2rem; font-size: 1rem; line-height:1.6;"></textarea>
                <div style="display:flex; justify-content:space-between; align-items:center; margin-top:1rem;">
                    <span id="char-count" style="font-size:0.8rem; opacity:0.5;">0 / 300</span>
                    <button id="ref-submit" class="primary-btn" style="min-width:150px;">Contribute Thought</button>
                </div>
            </div>
        </section>
    `;
}

async function loadReflections(targetId) {
    const listEl = document.getElementById('reflection-list');
    if (!listEl) return;
    const data = await apiGet(`/api/reflections/${targetId}`);
    listEl.innerHTML = data.map(r => `
        <div style="border-bottom: 1px solid rgba(255,255,255,0.05); padding: 2rem 0;">
            <div style="display:flex; justify-content:space-between; font-size:0.9rem; margin-bottom:1rem; opacity:0.8;"><b>${r.username}</b> <span class="dimmed">${r.date}</span></div>
            <p style="font-size:1.1rem; line-height: 1.7; margin-bottom: 1.5rem;">${r.content}</p>
            <div style="margin-left: 2rem; border-left: 2px solid var(--color-accent); padding-left: 1.5rem;">
                ${r.replies.map(rep => `<div style="font-size:0.95rem; margin-bottom:0.8rem;"><b style="opacity:0.6;">${rep.username}:</b> ${rep.content}</div>`).join('')}
                <input type="text" placeholder="Add a Layer..." class="layer-input" data-rid="${r.id}" style="background:none; border:none; border-bottom: 1px solid var(--color-border); color:white; font-size:0.9rem; width:100%; outline:none; padding:8px 0; margin-top:0.5rem;">
            </div>
        </div>
    `).join('') || '<p class="dimmed" style="text-align:center;">No reflections yet.</p>';

    const refInput = document.getElementById('ref-input');
    if (refInput) {
        refInput.oninput = () => { document.getElementById('char-count').textContent = `${refInput.value.length} / 300`; };
        document.getElementById('ref-submit').onclick = async () => {
            if (!State.currentUser) return navigate('premium');
            if (refInput.value.length < 200) return showToast('200文字以上必要です');
            await apiPost('/api/reflections', { word_id: targetId, username: State.currentUser, content: refInput.value });
            refInput.value = ''; loadReflections(targetId); showToast('Reflected.');
        };
    }
    listEl.querySelectorAll('.layer-input').forEach(i => i.onkeypress = async (e) => {
        if (e.key === 'Enter' && i.value.trim()) {
            if (!State.currentUser) return navigate('premium');
            await apiPost('/api/replies', { reflection_id: i.dataset.rid, username: State.currentUser, content: i.value });
            i.value = ''; loadReflections(targetId);
        }
    });
}

function renderArchive() {
    let list = (typeof WORDS !== 'undefined') ? [...WORDS] : [];
    list.sort((a, b) => a.word.localeCompare(b.word));
    if (State.searchFilter) list = list.filter(w => w.etymology.breakdown.some(b => b.text.includes(State.searchFilter)));
    else if (State.letterFilter) list = list.filter(w => w.word.toUpperCase().startsWith(State.letterFilter));

    viewContainer.innerHTML = `
        <div class="archive-container fade-in">
            <div class="alphabet-bar" style="display:flex; flex-wrap:wrap; gap:6px; margin-bottom: 3rem; justify-content:center;">
                ${'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('').map(l => `<button class="index-letter ${State.letterFilter === l ? 'active' : ''}" onclick="State.letterFilter='${l}';State.searchFilter=null;renderArchive()">${l}</button>`).join('')}
                <button class="index-letter" style="width:auto; padding:0 12px;" onclick="State.letterFilter=null;State.searchFilter=null;renderArchive()">ALL</button>
            </div>
            <div class="archive-grid" style="display:grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap:2rem;">
                ${list.map(w => `
                    <div class="archive-item" onclick="State.todayWord=WORDS.find(x=>x.id==='${w.id}');navigate('today')" style="position:relative; padding:1.8rem; border:1px solid var(--color-border); border-radius:20px; background:var(--color-surface); height:160px; display:flex; flex-direction:column; justify-content:space-between; transition:all 0.3s ease;">
                        <div style="flex-grow:1; text-align: left;">
                            <span style="font-weight:700; font-size:1.5rem; color:var(--color-accent); letter-spacing:-0.02em; display:block;">${w.word}</span>
                            <div style="font-size:0.95rem; opacity:0.75; margin-top:0.8rem; line-height:1.5; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden;">${w.core_concept.ja}</div>
                        </div>
                        <div style="font-size:0.75rem; opacity:0.4; text-align:right; border-top: 1px solid rgba(255,255,255,0.05); padding-top:0.8rem;">
                            by <b style="opacity:1;">${w.author || 'etymon_official'}</b>
                        </div>
                    </div>
                `).join('')}
            </div>
        </div>
    `;
}

function renderEssays() {
    const list = (typeof ESSAYS !== 'undefined') ? [...ESSAYS] : [];
    list.sort((a, b) => b.date.localeCompare(a.date)); // 日付順に降順ソート
    viewContainer.innerHTML = `
        <div class="essays-view fade-in">
            <h3 class="section-label" style="text-align:center; margin-bottom:4rem; font-size:1.4rem;">Weekly Philology</h3>
            <div class="essay-list">${list.map(e => `
                <div class="essay-card" onclick="openEssay('${e.id}')" style="background:var(--color-surface); padding:3rem; border-radius:24px; margin-bottom:2rem; border:1px solid var(--color-border); cursor:pointer; position:relative;">
                    <span class="dimmed" style="font-size:0.9rem;">${e.date}</span>
                    <h2 style="margin: 1rem 0; font-size:2rem; line-height:1.2;">${e.title} ${!State.isPremium ? '🔒' : ''}</h2>
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <p class="dimmed">Tap to experience the depth...</p>
                        ${State.isPremium ? `<span class="essay-save-icon" style="font-size:1.5rem;">${State.savedEssayIds.includes(e.id) ? '🔖' : '📑'}</span>` : ''}
                    </div>
                </div>`).join('') || '<p class="dimmed" style="text-align:center;">Deep sea of thoughts is being prepared...</p>'}</div>
        </div>`;
}

function openEssay(id) {
    if (!State.isPremium) { showToast('Premium access required.'); navigate('premium'); return; }
    const e = ESSAYS.find(x => x.id === id);
    viewContainer.innerHTML = `
        <div class="essay-content fade-in" style="max-width:800px; margin:0 auto; padding-bottom:100px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:3rem;">
                <button class="chip" onclick="renderEssays()">← Archives</button>
                <button class="essay-save-btn" data-id="${e.id}" style="background:none; border:none; font-size:2rem; cursor:pointer;">
                    ${State.savedEssayIds.includes(e.id) ? '🔖' : '📑'}
                </button>
            </div>
            <header style="margin-bottom: 5rem;">
                <span class="dimmed" style="font-size:1rem;">${e.date}</span>
                <h1 style="font-size:3.5rem; margin:1.5rem 0; line-height:1.1; letter-spacing:-0.03em;">${e.title}</h1>
            </header>
            <div class="essay-body" style="font-size:1.3rem; line-height:2; color:var(--color-text); font-family: 'Inter', sans-serif;">
                ${e.content.split('\n').map(l => l.trim() ? `<p style="margin-bottom:2.5rem;">${l}</p>` : '').join('')}
            </div>
            ${renderReflectionSection(e.id)}
        </div>`;
    loadReflections(e.id);

    document.querySelector('.essay-save-btn').onclick = () => {
        const idx = State.savedEssayIds.indexOf(e.id);
        if (idx > -1) State.savedEssayIds.splice(idx, 1);
        else State.savedEssayIds.push(e.id);
        localStorage.setItem('savedEssays', JSON.stringify(State.savedEssayIds));
        openEssay(e.id);
    };
}

function renderSaved() {
    const list = (typeof WORDS !== 'undefined') ? WORDS : [];
    const savedWords = list.filter(w => State.savedWordIds.includes(w.id));
    const essayList = (typeof ESSAYS !== 'undefined') ? ESSAYS : [];
    const savedEssays = essayList.filter(e => State.savedEssayIds.includes(e.id));

    viewContainer.innerHTML = `
        <div class="saved-view fade-in">
            <h3 class="section-label" style="text-align:center; margin-bottom:3rem;">Acquired Knowledge</h3>
            
            <section style="margin-bottom: 4rem;">
                <h4 class="section-label" style="font-size:0.8rem; opacity:0.6; margin-bottom:1.5rem;">WORDS</h4>
                <div class="archive-grid" style="gap:1.5rem;">
                    ${savedWords.map(w => `<div class="archive-item" onclick="State.todayWord=WORDS.find(x=>x.id==='${w.id}');navigate('today')" style="padding:2rem; border:1px solid var(--color-border); border-radius:24px; background:var(--color-surface); font-weight:bold; color:var(--color-accent); font-size:1.4rem; text-align:center; cursor:pointer;">${w.word}</div>`).join('') || '<p class="dimmed">No words in inventory.</p>'}
                </div>
            </section>

            <section>
                <h4 class="section-label" style="font-size:0.8rem; opacity:0.6; margin-bottom:1.5rem;">ESSAYS</h4>
                <div class="essay-list">
                    ${savedEssays.map(e => `
                        <div class="essay-card" onclick="openEssay('${e.id}')" style="background:var(--color-surface); padding:2rem; border-radius:20px; margin-bottom:1rem; border:1px solid var(--color-border); cursor:pointer;">
                            <span class="dimmed" style="font-size:0.8rem;">${e.date}</span>
                            <h2 style="font-size:1.4rem;">${e.title}</h2>
                        </div>
                    `).join('') || '<p class="dimmed">No essays in inventory.</p>'}
                </div>
            </section>
        </div>
    `;
}

function renderSettings() {
    viewContainer.innerHTML = `
        <div class="settings-view fade-in" style="max-width:500px; margin: 4rem auto; padding: 3rem; background:var(--color-surface); border-radius:28px; border:1px solid var(--color-border);">
            <h3 class="section-label" style="margin-bottom:3rem;">Settings</h3>
            <div class="setting-group" style="margin-bottom:3rem;">
                <label style="display:block; margin-bottom:1.2rem; font-weight:bold; opacity:0.8;">Text Readability</label>
                <input type="range" id="set-fontSize" min="14" max="22" value="${State.fontSize}" style="width:100%;">
                <div style="text-align:center; margin-top:0.8rem; font-size:0.9rem; opacity:0.6;">Size: ${State.fontSize}px</div>
            </div>
            <div class="setting-group" style="margin-bottom:3rem;">
                <label style="display:block; margin-bottom:1.2rem; font-weight:bold; opacity:0.8;">Interface Theme</label>
                <div style="display:flex; gap:12px;">
                    <button class="primary-btn" onclick="State.theme='dark';saveSettings()" style="flex:1; background:${State.theme === 'dark' ? 'var(--color-accent)' : 'transparent'};">Dark</button>
                    <button class="primary-btn" onclick="State.theme='light';saveSettings()" style="flex:1; background:${State.theme === 'light' ? 'var(--color-accent)' : 'transparent'};">Light</button>
                </div>
            </div>
            <button class="primary-btn" onclick="saveSettings()" style="width:100%; padding:1.2rem; border-radius:14px; font-weight:bold; margin-bottom: 2rem;">Commit Changes</button>
            
            <div class="setting-group" style="padding-top: 2rem; border-top: 1px solid var(--color-border);">
                <label style="display:block; margin-bottom:1.2rem; font-weight:bold; opacity:0.8;">Account</label>
                <div style="display:flex; flex-direction:column; gap:12px;">
                    <p class="dimmed" style="font-size:0.9rem; margin-bottom:0.5rem;">Current Identity: <b style="color:var(--color-text);">${State.currentUser || 'None'}</b></p>
                    <button onclick="logout()" class="primary-btn" style="width:100%; padding:1rem; border-radius:12px; background:transparent; border:1px solid var(--color-border); color:var(--color-text-dim); transition:all 0.3s; cursor:pointer;" onmouseover="this.style.borderColor='var(--color-accent)';this.style.color='var(--color-text)'" onmouseout="this.style.borderColor='var(--color-border)';this.style.color='var(--color-text-dim)'">
                        Logout (Leave Identity)
                    </button>
                </div>
            </div>
        </div>
    `;
    document.getElementById('set-fontSize').oninput = (e) => { State.fontSize = e.target.value; applySettings(); };
}

function saveSettings() { localStorage.setItem('set_fontSize', State.fontSize); localStorage.setItem('set_theme', State.theme); applySettings(); showToast('Configured.'); }

function renderDeepDiveContent(word) {
    return `<div class="deep-dive-unlocked" style="margin-top:4rem;"><span class="section-label" style="color:var(--color-premium);">Proto-Indo-European Roots</span><div class="roots-grid" style="display:grid; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); gap:1.2rem; margin:2rem 0;">${(word.deep_dive.roots || []).map(r => `<div class="root-item" style="padding:1.2rem; border:1px solid var(--color-premium); border-radius:16px; background:rgba(245,158,11,0.03);"><b style="color:var(--color-premium); font-size:1.3rem;">${r.term}</b><br><span style="font-size:0.9rem; opacity:0.8;">${r.meaning}</span></div>`).join('')}</div><ul style="list-style:none; padding:0;">${(word.deep_dive.points || []).map(p => `<li style="margin-bottom:1.5rem; font-size:1.15rem; padding-left:1.8rem; position:relative; line-height:1.6;"><span style="position:absolute; left:0; color:var(--color-premium); font-size:1.5rem; top:-0.2rem;">◎</span>${p}</li>`).join('')}</ul></div>`;
}
function renderDeepDiveLock() { return `<div class="lock-container" onclick="navigate('premium')" style="padding:4rem; border:1px dashed var(--color-border); border-radius:24px; text-align:center; cursor:pointer; margin-top:4rem; background:rgba(255,255,255,0.02); transition:all 0.3s;"><div style="font-size:2.5rem; margin-bottom:1rem;">🕯️</div><div style="font-weight:bold; color:var(--color-premium); font-size:1.2rem;">Illuminate the Deep Roots</div><p class="dimmed" style="margin-top:0.5rem;">Access PIE roots and advanced philological analysis.</p></div>`; }

function renderPremium() {
    if (State.isPremium && State.currentUser) { viewContainer.innerHTML = `<div class="premium-view" style="text-align:center; padding:8rem 2rem;"><div style="font-size:4rem; margin-bottom:2rem;">✨</div><h2>Citizen ${State.currentUser}</h2><p class="dimmed">Your mind is connected to the deeper structures.</p><button onclick="logout()" class="primary-btn" style="margin-top:4rem; background:transparent; border:1px solid var(--color-border);">Leave Identity</button></div>`; return; }
    if (!State.currentUser) {
        viewContainer.innerHTML = `<div class="auth-view fade-in" style="max-width:420px; margin: 6rem auto; padding: 3.5rem; background:var(--color-surface); border-radius:32px; border:1px solid var(--color-border);"><h2 id="auth-title" style="text-align:center; margin-bottom:3rem; font-weight:300; letter-spacing:0.2em;">IDENTITY</h2><div class="input-group"><label>Username</label><input type="text" id="auth-username" style="width:100%; background:var(--color-bg); padding:1rem; border-radius:12px; border:1px solid var(--color-border); color:white;"></div><div class="input-group" style="margin-top:1.5rem;"><label>Password</label><input type="password" id="auth-password" style="width:100%; background:var(--color-bg); padding:1rem; border-radius:12px; border:1px solid var(--color-border); color:white;"></div><button id="auth-submit" class="primary-btn" style="width:100%; margin-top:3rem; padding:1.2rem; border-radius:14px; font-weight:bold; font-size:1.1rem;">ENTER</button><p style="text-align:center; margin-top:2rem;"><a href="#" id="auth-toggle" style="opacity:0.5; font-size:0.85rem; text-decoration:none;">Initialize New Identity</a></p></div>`;
        setupAuthListeners(); return;
    }
    viewContainer.innerHTML = `<div class="premium-view" style="text-align:center; padding:6rem 2rem;"><div style="font-size:3.5rem; margin-bottom:1.5rem;">🔱</div><h2>The Inner Circle</h2><p class="dimmed" style="max-width:400px; margin: 0 auto 4rem; line-height:1.6;">Unlock weekly scholarly essays, participate in shared reflections, and access Proto-Indo-European root analysis.</p><button id="buy-premium-btn" class="primary-btn" style="width:100%; max-width:400px; padding:1.8rem; font-size:1.3rem; border-radius:20px; box-shadow: 0 10px 30px rgba(var(--color-accent-rgb), 0.3);">UNSEAL ALL LAYERS (¥980/mo)</button></div>`;
    document.getElementById('buy-premium-btn').onclick = async () => { const res = await apiPost('/create-checkout-session?username=' + State.currentUser, {}); const stripe = Stripe('pk_test_51T5KW45XPK1iD6ycU5CgxWXqSgxgKUDSNWImeARHpDFXHrfBC1y8BI4w4tr2cvftIb9uiSickAv3PoGIM5i2SX5F00W2Uz21M8'); await stripe.redirectToCheckout({ sessionId: res.id }); };
}

function setupAuthListeners() {
    let mode = 'login';
    const title = document.getElementById('auth-title'), submit = document.getElementById('auth-submit'), toggle = document.getElementById('auth-toggle');
    toggle.onclick = (e) => { e.preventDefault(); mode = (mode === 'login' ? 'register' : 'login'); title.textContent = (mode === 'login' ? 'IDENTITY' : 'INITIALIZE'); submit.textContent = (mode === 'login' ? 'ENTER' : 'REGISTER'); };
    submit.onclick = async () => {
        const username = document.getElementById('auth-username').value, password = document.getElementById('auth-password').value;
        const res = await apiPost('/api/' + mode, { username, password });
        if (res.status === 'success') { if (mode === 'register') { showToast('Success. Please login.'); mode = 'login'; setupAuthListeners(); } else { State.currentUser = username; State.isPremium = res.is_premium; localStorage.setItem('currentUser', username); localStorage.setItem('isPremium', res.is_premium); applySettings(); navigate('today'); } }
        else showToast(res.message);
    };
}

function logout() { localStorage.clear(); location.reload(); }

function navigate(view) {
    State.currentView = view;
    Object.keys(navItems).forEach(k => { if (navItems[k]) navItems[k].classList.toggle('active', k === view); });
    viewContainer.classList.remove('fade-in');
    setTimeout(() => {
        switch (view) {
            case 'today': renderToday(); break;
            case 'archive': renderArchive(); break;
            case 'saved': renderSaved(); break;
            case 'contribute': renderContribute(); break;
            case 'essays': renderEssays(); break;
            case 'settings': renderSettings(); break;
            case 'premium': renderPremium(); break;
        }
        viewContainer.classList.add('fade-in');
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }, 50);
}

function showToast(msg) {
    const container = document.getElementById('toast-container');
    const t = document.createElement('div');
    t.className = 'toast'; t.textContent = msg; container.appendChild(t);
    setTimeout(() => { t.style.opacity = '1'; t.style.transform = 'translateY(0)'; }, 10);
    setTimeout(() => { t.style.opacity = '0'; setTimeout(() => t.remove(), 300); }, 3000);
}

function renderContribute() {
    if (!State.currentUser) { showToast('Identity required.'); navigate('premium'); return; }
    viewContainer.innerHTML = `
        <div class="contribute-view fade-in" style="max-width:640px; margin: 0 auto; padding-bottom:120px;">
            <h3 class="section-label" style="text-align:center; margin-bottom:4rem;">Contribution to Archive</h3>
            <form id="word-form" style="background:var(--color-surface); padding:3rem; border-radius:32px; border:1px solid var(--color-border);">
                <div class="input-group"><label>Word Entry</label><input type="text" id="w-word" required style="width:100%; background:var(--color-bg); border-radius:12px; border:1px solid var(--color-border); color:white; padding:1.2rem;"></div>
                <div class="input-group" style="margin-top:2rem;"><label>Etymological Structure (prefix:meaning, ...)</label><input type="text" id="w-breakdown" required style="width:100%; background:var(--color-bg); border-radius:12px; border:1px solid var(--color-border); color:white; padding:1.2rem;"></div>
                <div class="input-group" style="margin-top:2rem;"><label>Concept Essence (Japanese)</label><input type="text" id="w-concept-ja" required style="width:100%; background:var(--color-bg); border-radius:12px; border:1px solid var(--color-border); color:white; padding:1.2rem;"></div>
                <div class="input-group" style="margin-top:2rem;"><label>Detailed Thought</label><textarea id="w-thinking" rows="8" style="width:100%; background:var(--color-bg); border-radius:12px; border:1px solid var(--color-border); color:white; padding:1.5rem; font-size: 1.1rem; line-height: 1.6;"></textarea></div>
                <button type="submit" class="primary-btn" style="width:100%; margin-top:3rem; padding:1.5rem; font-weight:bold; font-size:1.2rem; border-radius:16px;">Publish Knowledge</button>
            </form>
        </div>`;
    document.getElementById('word-form').onsubmit = async (e) => {
        e.preventDefault();
        const wordData = {
            id: document.getElementById('w-word').value.toLowerCase().trim(),
            word: document.getElementById('w-word').value.trim(),
            etymology: { breakdown: document.getElementById('w-breakdown').value.split(',').map(x => ({ text: x.split(':')[0].trim(), meaning: x.split(':')[1].trim() })), original_statement: "" },
            core_concept: { en: "", ja: document.getElementById('w-concept-ja').value },
            thinking_layer: document.getElementById('w-thinking').value,
            synonyms: [], antonyms: [], aftertaste: "", deep_dive: { roots: [], points: [] }, source: "Citizen Contribution", author: State.currentUser
        };
        const res = await apiPost('/api/submit-word', { username: State.currentUser, wordData });
        if (res.status === 'success') { showToast('Accepted.'); setTimeout(() => location.reload(), 1000); }
    };
}

document.addEventListener('DOMContentLoaded', async () => {
    applySettings();
    if (navItems.today) navItems.today.onclick = () => navigate('today');
    if (navItems.archive) navItems.archive.onclick = () => { State.letterFilter = null; State.searchFilter = null; navigate('archive'); };
    if (navItems.saved) navItems.saved.onclick = () => navigate('saved');
    if (navItems.contribute) navItems.contribute.onclick = () => navigate('contribute');
    if (navItems.essays) navItems.essays.onclick = () => navigate('essays');
    if (navItems.settings) navItems.settings.onclick = () => navigate('settings');
    if (navItems.premium) navItems.premium.onclick = () => navigate('premium');

    const params = new URLSearchParams(window.location.search);
    const sid = params.get('session_id'), user = params.get('user');
    if (sid && user) {
        const res = await fetch(`${API_BASE}/check-subscription?session_id=${sid}&user=${user}`);
        const data = await res.json();
        if (data.status === 'paid') { State.isPremium = true; localStorage.setItem('isPremium', 'true'); applySettings(); }
        window.history.replaceState({}, '', '/');
    }
    if (typeof WORDS !== 'undefined' && WORDS.length) {
        if (!State.todayWord) State.todayWord = WORDS[Math.floor(Math.random() * WORDS.length)];
    }
    if (!State.currentUser) navigate('premium'); else navigate('today');
});

viewContainer.addEventListener('click', e => {
    const saveBtn = e.target.closest('.save-btn');
    if (saveBtn) {
        const id = saveBtn.dataset.id;
        const idx = State.savedWordIds.indexOf(id);
        if (idx > -1) State.savedWordIds.splice(idx, 1);
        else State.savedWordIds.push(id);
        localStorage.setItem('savedWords', JSON.stringify(State.savedWordIds));
        renderToday();
    }
});
