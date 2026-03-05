/**
 * ling-ling-etymon - Refined UI & Premium Essay Favorites
 */

// --- Application State ---
const State = {
    currentUser: localStorage.getItem('currentUser') || null,
    isPremium: localStorage.getItem('isPremium') === 'true',
    isOperator: localStorage.getItem('isOperator') === 'true',
    currentView: 'today',
    savedWordIds: JSON.parse(localStorage.getItem('savedWords') || '[]'),
    savedEssayIds: JSON.parse(localStorage.getItem('savedEssays') || '[]'),
    todayWord: null,
    searchFilter: null,
    letterFilter: null,
    followedUsers: [],

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
    etymap: document.getElementById('nav-etymap'),
    synthesizer: document.getElementById('nav-synthesizer'),
    essays: document.getElementById('nav-essays'),
    settings: document.getElementById('nav-settings'),
    premium: document.getElementById('nav-premium'),
    notifications: document.getElementById('nav-notifications'),
    network: document.getElementById('nav-network'),
    timeline: document.getElementById('nav-timeline'),
    search: document.getElementById('global-search-input')
};

// Global cache for dynamically loaded content
window.ESSAY_CACHE = [];
window.currentAudio = null;

const API_BASE = window.location.origin;

// --- Design System Colors ---
const PART_COLORS = {
    word: 'var(--color-accent)', // Maps to UI theme
    root: 'var(--color-premium)',  // Maps to Semantic Roots
    prefix: '#22c55e', // Green
    suffix: '#ef4444'  // Red
};

// Canvas rendering (like vis.js) needs explicit hex/rgb colors instead of CSS variables
const resolveColor = (val) => {
    if (val.startsWith('var(')) {
        const varName = val.replace(/var\(|\)/g, '').trim();
        return getComputedStyle(document.body).getPropertyValue(varName).trim() || '#3b82f6';
    }
    return val;
};

// --- Utils ---
async function apiGet(endpoint) {
    try {
        const response = await fetch(`${API_BASE}${endpoint}`, { signal: AbortSignal.timeout(15000) });
        return await response.json();
    }
    catch (e) { console.error("apiGet failed:", e); return []; }
}
async function apiPost(endpoint, data) {
    try {
        const response = await fetch(`${API_BASE}${endpoint}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data),
            signal: AbortSignal.timeout(15000)
        });
        return await response.json();
    } catch (e) { console.error("apiPost failed:", e); return { status: 'error', message: 'サーバー接続エラーが発生しました' }; }
}

// Function to submit a new layer (e.g., Deep Dive, Reflection)
async function submitLayer(targetType, targetId, content) {
    if (!State.currentUser) {
        alert('ログインしてコンテンツを投稿してください。');
        return { status: 'error', message: 'ログインが必要です。' };
    }
    if (!content || content.trim() === '') {
        alert('内容を入力してください。');
        return { status: 'error', message: '内容が空です。' };
    }

    const res = await apiPost('/api/submit-layer', {
        username: State.currentUser,
        target_type: targetType,
        target_id: targetId,
        content: content
    });

    if (res.status === 'success') {
        alert('コンテンツが投稿されました！');
        return res;
    } else {
        alert(`投稿に失敗しました: ${res.message}`);
        return res;
    }
}

async function adminAction(action, type, target_id, report_id) {
    if (action === 'delete') {
        if (!confirm('本当にこのコンテンツを削除しますか？')) return;
        const res = await apiPost('/api/admin/delete-content', {
            admin_username: State.currentUser,
            target_type: type,
            target_id: target_id,
            report_id: report_id
        });
        if (res.status === 'success') {
            showToast('コンテンツを削除しました');
            renderOperatorPanel();
        }
    } else if (action === 'dismiss') {
        const res = await apiPost('/api/admin/dismiss-report', {
            admin_username: State.currentUser,
            report_id: report_id
        });
        if (res.status === 'success') {
            showToast('通報を却下しました');
            renderOperatorPanel();
        }
    }
}

// Function to load saved items from the backend
async function loadSavedItems() {
    if (State.currentUser) {
        try {
            const savedData = await apiGet(`/api/saved-items?username=${State.currentUser}`);
            if (savedData && savedData.words) {
                State.savedWordIds = savedData.words;
                localStorage.setItem('savedWords', JSON.stringify(State.savedWordIds));
            }
            if (savedData && savedData.essays) {
                State.savedEssayIds = savedData.essays;
                localStorage.setItem('savedEssays', JSON.stringify(State.savedEssayIds));
            }
        } catch (e) {
            console.error("Failed to load saved items from backend:", e);
            // Fallback to local storage if backend fails
            State.savedWordIds = JSON.parse(localStorage.getItem('savedWords') || '[]');
            State.savedEssayIds = JSON.parse(localStorage.getItem('savedEssays') || '[]');
        }
    } else {
        // If not logged in, rely solely on local storage
        State.savedWordIds = JSON.parse(localStorage.getItem('savedWords') || '[]');
        State.savedEssayIds = JSON.parse(localStorage.getItem('savedEssays') || '[]');
    }
}

// Placeholder for login function (assuming it exists elsewhere or will be added)
async function login(username, password) {
    const res = await apiPost('/api/login', { username, password });
    if (res.status === 'success') {
        State.currentUser = username;
        State.isPremium = res.is_premium;
        State.isOperator = res.is_operator;
        localStorage.setItem('currentUser', username);
        localStorage.setItem('isPremium', res.is_premium);
        localStorage.setItem('isOperator', res.is_operator);
        await loadSavedItems(); // Call loadSavedItems after successful login
        applySettings(); // Re-apply settings to update UI based on premium status etc.
        navigate(State.currentView); // Re-render current view
        return true;
    } else {
        alert(res.message);
        return false;
    }
}


function applySettings() {
    document.documentElement.style.fontSize = State.fontSize + 'px';
    document.body.className = `theme-${State.theme}`;
    Object.keys(navItems).forEach(k => { if (navItems[k]) navItems[k].classList.remove('active'); });
    if (navItems[State.currentView]) navItems[State.currentView].classList.add('active');

    // Ads logic
    const adBanner = document.getElementById('ad-banner');
    if (adBanner) {
        if (State.isPremium) {
            adBanner.style.display = 'none';
            document.getElementById('main-content').style.paddingBottom = '2rem';
        } else {
            adBanner.style.display = 'flex';
            document.getElementById('main-content').style.paddingBottom = '100px';
        }
    }
}

// --- View Controllers ---

async function renderToday() {
    const word = State.todayWord || {};
    if (!word) { viewContainer.innerHTML = `<div class="empty-msg">No word found.</div>`; return; }

    viewContainer.innerHTML = `
        <article class="word-card fade-in">
            <header class="word-header" style="position: relative;">
                <div style="display:flex; align-items:center;">
                    <span class="section-label" style="margin-bottom:0;">Word</span>
                    <button onclick="if(typeof WORDS !== 'undefined' && WORDS.length > 0){State.todayWord = WORDS[Math.floor(Math.random() * WORDS.length)]; renderToday();}" class="chip" style="background:none; border:1px solid var(--color-accent); color:var(--color-accent); font-size:0.8rem; margin-left:12px; padding:0.2rem 0.8rem;">↻ Regenerate</button>
                </div>
                <h2 class="word-title" style="font-size: 3rem; margin: 0.5rem 0;">${word.word}</h2>
                <div style="margin-bottom: 2rem; display: flex; gap: 1rem; align-items: center; opacity: 0.8;">
                    ${word.part_of_speech ? `<span class="chip" style="font-style: italic; background: rgba(255,255,255,0.1); border: 1px solid var(--color-border); font-size: 0.8rem; padding: 0.3rem 0.8rem;">${word.part_of_speech}</span>` : ''}
                    ${word.meaning ? `<span style="font-size: 1.1rem; color: var(--color-accent); font-weight: 500;">${word.meaning}</span>` : ''}
                </div>
                <div class="etymology-box">
                    <span class="section-label">Structure ${!State.isPremium ? '🔒' : ''}</span>
                    <div class="etymology-breakdown" style="font-size: 1.1rem; margin-top:0.5rem;">
                        ${(word.etymology.breakdown || (word.etymology.components ? word.etymology.components.map(c => {
        if (typeof c === 'string') {
            const parts = c.split(' (');
            return { text: parts[0], meaning: parts[1] ? parts[1].replace(')', '') : '', type: 'root' };
        }
        return c;
    }) : [])).map(b => {
        const b_type = (b.type || '').toLowerCase();
        const color = b_type.includes('prefix') ? PART_COLORS.prefix
            : (b_type.includes('suffix') ? PART_COLORS.suffix
                : (b_type.includes('root') ? PART_COLORS.root
                    : PART_COLORS.word));
        return `
                                <span class="morpheme-link" data-term="${b.text}" style="cursor:${State.isPremium ? 'pointer' : 'default'}">
                                    <span class="morpheme-text" style="color:${color}; font-weight:bold;">${b.text}</span>
                                    <span class="morpheme-meaning">（${b.meaning}）</span>
                                </span>
                            `;
    }).join(' + ')}
                    </div>
                </div>
                <div class="word-options-container" style="position:absolute; top:0; right:0;">
                    <button id="word-options-trigger" style="background:none; border:none; font-size:1.8rem; cursor:pointer; color:var(--color-text-dim); padding:0.5rem;">⋯</button>
                    <div id="word-options-menu" style="display:none; position:absolute; top:40px; right:0; background:var(--color-surface); border:1px solid var(--color-border); border-radius:12px; box-shadow:0 10px 30px rgba(0,0,0,0.3); z-index:100; min-width:160px; overflow:hidden;">
                        <button onclick="toggleSaveWord('${word.id}')" style="width:100%; padding:1rem; background:none; border:none; color:white; text-align:left; cursor:pointer; font-size:0.9rem; border-bottom:1px solid var(--color-border);">
                            ${State.savedWordIds.includes(word.id) ? '🔖 Unsave' : '📑 Save Word'}
                        </button>
                        <button onclick="downloadWordCard('${word.id}')" style="width:100%; padding:1rem; background:none; border:none; color:white; text-align:left; cursor:pointer; font-size:0.9rem; border-top:1px solid var(--color-border);">
                            🖼️ Share as Image
                        </button>
                    </div>
                </div>
            </header>

            <section class="section"><span class="section-label">Essence</span><p class="concept-text" style="font-size: 1.25rem;">${word.core_concept?.ja || word.concept || ''}</p></section>
            
            <section class="section">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span class="section-label">Philological Layers</span>
                    ${State.isPremium ? `<button onclick="toggleTTS('${btoa(unescape(encodeURIComponent(word.thinking_layer)))}')" class="chip" style="background:var(--color-premium-bg); color:var(--color-premium); border:1px solid var(--color-premium);">🔊 Listen (Echo)</button>` : ''}
                </div>
                <div class="thinking-text" style="font-size: 1.1rem; line-height: 1.8;">
                    ${(word.thinking_layer || word.thinking || '').split('\n').map(l => l.trim() ? `<p style="margin-bottom:1.2rem;">${l}</p>` : '').join('')}
                </div>
            </section>
            
            <div style="display:grid; grid-template-columns: 1fr 1fr; gap:1.2rem; margin-bottom: 2.5rem;">
                <section class="section" style="background:rgba(255,255,255,0.03); padding:1.2rem; border-radius:16px;"><span class="section-label">Synonyms</span><div style="display:flex; flex-wrap:wrap; gap:0.5rem; margin-top:0.5rem;">${(word.synonyms || []).map(s => `<span class="chip" onclick="searchToArchive('${s}')" style="cursor:pointer; border:1px solid var(--color-accent);">${s}</span>`).join('') || '--'}</div></section>
                <section class="section" style="background:rgba(255,255,255,0.03); padding:1.2rem; border-radius:16px;"><span class="section-label">Antonyms</span><div style="display:flex; flex-wrap:wrap; gap:0.5rem; margin-top:0.5rem;">${(word.antonyms || []).map(a => `<span class="chip" onclick="searchToArchive('${a}')" style="cursor:pointer; border:1px solid var(--color-border);">${a}</span>`).join('') || '--'}</div></section>
            </div>

            <section class="section aftertaste-section" style="border-left: 2px solid var(--color-accent); padding-left: 1.5rem;"><span class="section-label">Resonance</span><p class="aftertaste-text" style="font-family: 'Times New Roman', serif; font-style: italic; font-size: 1.3rem;">${word.aftertaste}</p></section>

            <div style="display:flex; justify-content:center; margin-bottom: 2.5rem;">
                <button id="fl-btn-word-${word.id}" onclick="toggleFlourish('word', '${word.id}', this, '${word.author || ''}')"
                    style="background:none; border:1px solid var(--color-border); color:var(--color-text-dim); font-size:0.9rem; padding:0.5rem 1.2rem; border-radius:100px; cursor:pointer; transition:all 0.2s; display:flex; align-items:center; gap:6px;">
                    ✦ Flourish · <span class="fl-cnt" id="fl-cnt-word-${word.id}">…</span>
                </button>
            </div>

            <footer style="margin-top: 3rem; padding-top: 1.5rem; border-top: 1px solid var(--color-border); display:flex; flex-direction:column; gap:0.5rem; opacity:0.5; font-size:0.8rem;">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <div>by <b>${word.author || 'etymon_official'}</b></div>
                    <div style="display:flex; gap:10px;">
                        ${word.author && word.author !== State.currentUser ? `
                            <button onclick="followUser('${word.author}')" class="chip" style="font-size:0.7rem; border:1px solid var(--color-accent); background:none; color:var(--color-accent);">Follow</button>
                            <button onclick="blockUser('${word.author}')" class="chip" style="font-size:0.7rem; border:1px solid #721c24; background:none; color:#f8d7da;">Block</button>
                        ` : ''}
                    </div>
                </div>
                <div style="display:flex; justify-content:space-between;">
                    <div>Source: ${word.source || '--'}</div>
                </div>
                <div style="font-style:italic; font-size:0.7rem; color:var(--color-text-dim);">
                    ※ 本コンテンツは、一部AIによって生成された、またはAIの補助を受けて作成された可能性があります。
                </div>
            </footer>
            
            <div class="deep-dive">${State.isPremium ? renderDeepDiveContent(word) : renderDeepDiveLock()}</div>

            ${renderReflectionSection(word.id)}
        </article>
    `;

    // Flourishカウント取得
    apiGet(`/api/flourish-count?target_type=word&target_id=${word.id}&username=${State.currentUser || ''}`)
        .then(fc => {
            const cnt = document.getElementById(`fl-cnt-word-${word.id}`);
            const btn = document.getElementById(`fl-btn-word-${word.id}`);
            if (cnt) cnt.textContent = fc.count;
            if (btn && fc.flourished) {
                btn.style.borderColor = 'var(--color-premium)';
                btn.style.color = 'var(--color-premium)';
                btn.dataset.flourished = 'true';
            }
        }).catch(() => { });

    loadReflections(word.id, word.author || 'etymon_official', word.word);
    document.querySelectorAll('.morpheme-link').forEach(l => l.onclick = () => { if (!State.isPremium) return navigate('premium'); State.searchFilter = l.dataset.term; navigate('archive'); });

    const trigger = document.getElementById('word-options-trigger');
    const menu = document.getElementById('word-options-menu');
    if (trigger && menu) {
        trigger.onclick = (e) => { e.stopPropagation(); menu.style.display = menu.style.display === 'block' ? 'none' : 'block'; };
        document.addEventListener('click', () => { menu.style.display = 'none'; }, { once: true });
    }
}

async function toggleSaveWord(id) {
    if (State.currentUser) {
        const res = await apiPost('/api/save-item', { username: State.currentUser, target_type: 'word', target_id: id });
        if (res.status === 'success') {
            const idx = State.savedWordIds.indexOf(id);
            if (res.action === 'saved' && idx === -1) State.savedWordIds.push(id);
            else if (res.action === 'unsaved' && idx > -1) State.savedWordIds.splice(idx, 1);
        }
    } else {
        const idx = State.savedWordIds.indexOf(id);
        if (idx > -1) State.savedWordIds.splice(idx, 1);
        else State.savedWordIds.push(id);
    }
    localStorage.setItem('savedWords', JSON.stringify(State.savedWordIds));
    renderToday();
}

function renderReflectionSection(targetId) {
    return `
        <section class="section reflections-section" style="margin-top:5rem; border-top: 2px solid var(--color-border); padding-top:3rem;">
            <h3 class="section-label" style="font-size: 1.3rem; letter-spacing: 0.1em;">Reflections</h3>
            <div id="reflection-list" style="margin: 2rem 0;">
                ${State.isPremium ? '<p class="dimmed">Gathering thoughts...</p>' : '<div class="lock-container" onclick="navigate(\'premium\')" style="padding:1.5rem; border-radius:12px; cursor:pointer;">🔒 Premiumメンバーのみ他の思索を閲覧できます</div>'}
            </div>
            <div class="reflection-form" style="background:var(--color-surface); padding:2.5rem; border-radius:32px; border: 1px solid var(--color-border); margin-top:2rem;">
                <textarea id="ref-input" maxlength="300" placeholder="この言葉へのリフレクションを記す（思索を深めるため200〜300字程度を推奨）" style="width:100%; min-height:160px; background:transparent; color:white; border:none; border-radius:12px; font-size: 1.1rem; line-height:1.8; outline:none; resize:none;"></textarea>
                <div style="display:flex; justify-content:space-between; align-items:center; margin-top:1.5rem; padding-top:1.5rem; border-top:1px solid rgba(255,255,255,0.05);">
                    <div id="char-count" style="font-size:0.9rem; opacity:0.5; font-family: 'Inter', sans-serif;">0 / 300 characters</div>
                    <button id="ref-submit" class="primary-btn" style="padding: 0.8rem 2.5rem; border-radius: 100px; font-weight: 600;">Publish Reflection</button>
                </div>
            </div>
        </section>
    `;
}

async function loadReflections(targetId, targetAuthor, wordName) {
    const listEl = document.getElementById('reflection-list');
    if (!listEl) return;

    // フォームのセットアップ（プレミアムに関わらず常に行う、API待機前に同期的にセットアップ）
    setupReflectionForm(targetId, targetAuthor, wordName);

    // プレミアムならリストを読み込む
    if (State.isPremium) {
        try {
            const data = await apiGet(`/api/reflections/${targetId}?username=${State.currentUser || ''}`);
            listEl.innerHTML = data.map(r => `
                <div style="border-bottom: 1px solid rgba(255,255,255,0.05); padding: 2rem 0;">
                    <div style="display:flex; justify-content:space-between; font-size:0.9rem; margin-bottom:1rem; opacity:0.8;">
                        <div><b>${r.username}</b> <span class="dimmed">${r.date}</span></div>
                        <div class="ugc-actions" style="display:flex; gap:10px;">
                            <button onclick="reportItem('reflection', ${r.id}, '${r.username}')" title="通報" style="background:none; border:none; cursor:pointer; opacity:0.5;">🚩</button>
                            ${r.username !== State.currentUser ? `<button onclick="blockUser('${r.username}')" title="ブロック" style="background:none; border:none; cursor:pointer; opacity:0.5;">🚫</button>` : ''}
                            <button onclick="hideItem('reflection', ${r.id})" title="非表示" style="background:none; border:none; cursor:pointer; opacity:0.5;">👁️‍🗨️</button>
                            ${State.isOperator ? `<button onclick="adminDeleteContent('reflection', ${r.id})" title="削除 (Admin)" style="background:none; border:none; cursor:pointer; opacity:0.5; color:red;">🗑️</button>` : ''}
                        </div>
                    </div>
                    <p style="font-size:1.1rem; line-height: 1.7; margin-bottom: 1.5rem; white-space: pre-wrap; overflow-wrap: break-word; word-break: break-word; padding-left: 0.5rem; border-left: 3px solid rgba(255,255,255,0.05);">${r.content}</p>
                    <div style="display:flex; align-items:center; gap:0.5rem; margin-bottom:1.5rem;">
                        <button id="fl-btn-reflection-${r.id}" onclick="toggleFlourish('reflection', '${r.id}', this, '${r.username}')"
                            style="background:none; border:1px solid var(--color-border); color:var(--color-text-dim); font-size:0.82rem; padding:0.35rem 0.9rem; border-radius:100px; cursor:pointer; transition:all 0.2s; display:flex; align-items:center; gap:4px;">
                            ✦ Flourish · <span class="fl-cnt" id="fl-cnt-reflection-${r.id}">…</span>
                        </button>
                    </div>
                    <div style="margin-left: 2rem; border-left: 2px solid var(--color-accent); padding-left: 1.5rem;">
                        ${r.replies.map(rep => `
                            <div style="font-size:0.95rem; margin-bottom:0.8rem; display:flex; justify-content:space-between;">
                                <div><b style="opacity:0.6;">${rep.username}:</b> ${rep.content}</div>
                                <div class="ugc-actions">
                                    <button onclick="reportItem('reply', ${rep.id}, '${rep.username}')" style="background:none; border:none; font-size:0.75rem; opacity:0.3; cursor:pointer;">🚩</button>
                                    <button onclick="hideItem('reply', ${rep.id})" style="background:none; border:none; font-size:0.75rem; opacity:0.3; cursor:pointer;">👁️‍🗨️</button>
                                    ${State.isOperator ? `<button onclick="adminDeleteContent('reply', ${rep.id})" style="background:none; border:none; font-size:0.75rem; opacity:0.3; cursor:pointer; color:red;">🗑️</button>` : ''}
                                </div>
                            </div>
                        `).join('')}
                        <div style="display:flex; align-items:center; gap:0.5rem; width:100%; margin-top:0.5rem;">
                            <input type="text" placeholder="Add a Layer..." class="layer-input" data-rid="${r.id}" style="background:none; border:none; border-bottom: 1px solid var(--color-border); color:white; font-size:0.9rem; flex-grow:1; outline:none; padding:8px 0;">
                            <button onclick="submitLayer(${r.id})" class="chip" style="font-size:0.7rem; padding:0.3rem 0.8rem; border:1px solid var(--color-accent); color:var(--color-accent); background:none; cursor:pointer;">Publish</button>
                        </div>
                    </div>
                </div>
            `).join('') || '<p class="dimmed" style="text-align:center;">No reflections yet.</p>';

            listEl.querySelectorAll('.layer-input').forEach(i => i.onkeypress = (e) => {
                if (e.key === 'Enter' && i.value.trim()) {
                    submitLayer(i.dataset.rid);
                }
            });
        } catch (e) {
            console.error("Failed to load reflections", e);
        }

        // Flourishカウントを非同期で取得
        if (data && Array.isArray(data)) {
            data.forEach(r => {
                apiGet(`/api/flourish-count?target_type=reflection&target_id=${r.id}&username=${State.currentUser || ''}`)
                    .then(fc => {
                        const cnt = document.getElementById(`fl-cnt-reflection-${r.id}`);
                        const btn = document.getElementById(`fl-btn-reflection-${r.id}`);
                        if (cnt) cnt.textContent = fc.count;
                        if (btn && fc.flourished) {
                            btn.style.borderColor = 'var(--color-premium)';
                            btn.style.color = 'var(--color-premium)';
                            btn.dataset.flourished = 'true';
                        }
                    }).catch(() => { });
            });
        }
    }
}

function setupReflectionForm(targetId, targetAuthor, wordName) {
    const refInput = document.getElementById('ref-input');
    const refSubmit = document.getElementById('ref-submit');
    const charCount = document.getElementById('char-count');

    if (refInput && refSubmit) {
        // カウンターの初期化と入力イベント
        refInput.oninput = () => {
            const count = refInput.value.length;
            if (charCount) {
                charCount.textContent = `${count} / 300 characters`;
                charCount.style.color = count >= 200 ? 'var(--color-accent)' : 'inherit';
                charCount.style.opacity = count >= 200 ? '1' : '0.5';
            }
        };

        refSubmit.onclick = async () => {
            if (!State.currentUser) {
                showToast('ログインが必要です');
                navigate('premium');
                return;
            }
            const content = refInput.value.trim();
            if (content.length < 200) {
                showToast(`あと ${200 - content.length} 文字必要です（200〜300字を推奨）`);
                return;
            }

            refSubmit.innerText = 'Publishing...';
            refSubmit.disabled = true;

            try {
                const res = await apiPost('/api/reflections', {
                    word_id: targetId,
                    username: State.currentUser,
                    content: content,
                    target_author: targetAuthor,
                    word_name: wordName
                });

                if (res.status === 'success') {
                    showRichToast('✦ 思索が宇宙へと放たれました', '言葉は今、誰かの心に届こうとしています。');
                    refInput.value = '';
                    if (charCount) charCount.textContent = '0 / 300 characters';
                    // 再読み込み
                    if (State.isPremium) {
                        await loadReflections(targetId, targetAuthor, wordName);
                    }
                } else {
                    showToast('投稿エラーが発生しました');
                }
            } catch (err) {
                showToast('通信エラーが発生しました');
            } finally {
                refSubmit.innerText = 'Publish Reflection';
                refSubmit.disabled = false;
            }
        };
    }
}

async function loadSavedItems() {
    if (!State.currentUser) return;
    try {
        const res = await apiGet(`/api/saved-items?username=${State.currentUser}`);
        if (res.saved_words) State.savedWordIds = res.saved_words;
        if (res.saved_essays) State.savedEssayIds = res.saved_essays;
        localStorage.setItem('savedWords', JSON.stringify(State.savedWordIds));
        localStorage.setItem('savedEssays', JSON.stringify(State.savedEssayIds));
    } catch (e) { console.error("Failed to load saved items", e); }
}

async function renderNotifications() {
    if (!State.currentUser) return navigate('premium');
    const data = await apiGet(`/api/notifications?username=${State.currentUser}`);
    viewContainer.innerHTML = `
        <div class="notifications-view fade-in" style="max-width:600px; margin: 0 auto; padding: 3rem;">
            <h3 class="section-label">Notifications</h3>
            <div class="notif-list" style="margin-top:2rem;">
                ${data.map(n => `
                    <div onclick="markNotifRead(${n.id}, '${n.link}')" style="background:${n.is_read ? 'var(--color-surface)' : 'rgba(96, 165, 250, 0.1)'}; padding:1.5rem; border-radius:16px; margin-bottom:1rem; border:1px solid var(--color-border); cursor:pointer; position:relative;">
                        <div style="font-size:0.8rem; opacity:0.6; margin-bottom:0.5rem;">${n.date}</div>
                        <div style="font-size:1rem;">${n.message}</div>
                        ${!n.is_read ? '<span style="position:absolute; top:1.5rem; right:1.5rem; width:8px; height:8px; background:var(--color-accent); border-radius:50%;"></span>' : ''}
                    </div>
                `).join('') || '<p class="dimmed">No notifications.</p>'}
            </div>
        </div>
    `;
}

async function markNotifRead(id, link) {
    await apiPost('/api/notifications/read', { id });
    if (link) navigate(link);
    else renderNotifications();
}

async function followUser(targetUser) {
    if (!State.currentUser) return navigate('premium');
    const isFollowing = State.followedUsers.includes(targetUser);

    try {
        if (isFollowing) {
            await apiPost('/api/unfollow', { follower: State.currentUser, followed: targetUser });
            State.followedUsers = State.followedUsers.filter(u => u !== targetUser);
            showToast(`Unsubscribed from ${targetUser}`);
        } else {
            await apiPost('/api/follow', { follower: State.currentUser, followed: targetUser });
            State.followedUsers.push(targetUser);
            showToast(`Subscribed to ${targetUser}`);
        }

        // 現時点のビューを再描画してボタン表示を更新
        const btns = document.querySelectorAll(`button[onclick^="followUser('${targetUser}')"]`);
        btns.forEach(btn => {
            const isNowFollowing = State.followedUsers.includes(targetUser);
            btn.textContent = isNowFollowing ? 'Followed' : 'Follow';
            btn.classList.toggle('followed', isNowFollowing);
        });
    } catch (e) {
        showToast("Error update follow status");
    }
}

async function loadFollows() {
    if (!State.currentUser) return;
    try {
        const res = await apiGet(`/api/follows?username=${State.currentUser}`);
        State.followedUsers = res || [];
    } catch (e) { console.error(e); }
}

async function unfollowUser(targetUser) {
    await apiPost('/api/unfollow', { follower: State.currentUser, followed: targetUser });
    showToast(`Unfollowed ${targetUser}`);
    renderConnections();
}

async function unblockUser(targetUser) {
    await apiPost('/api/unblock', { blocker: State.currentUser, blocked: targetUser });
    showToast(`Unblocked ${targetUser}`);
    renderConnections();
}

async function unhideItem(type, id) {
    await apiPost('/api/unhide', { username: State.currentUser, target_type: type, target_id: id });
    showToast('解除しました');
    renderConnections();
}

// --- UGC Actions ---
async function reportItem(type, id, targetUser) {
    const reason = prompt('通報理由を入力してください（不適切な投稿、誹謗中傷など）:');
    if (!reason) return;
    await apiPost('/api/report', { reporter: State.currentUser || 'anonymous', target_username: targetUser, target_type: type, target_id: id, reason: reason });
    showToast('通報を受け付けました。ご協力ありがとうございます。');
}

async function blockUser(targetUser) {
    if (!State.currentUser) return navigate('premium');
    if (!confirm(`${targetUser} さんをブロックしますか？このユーザーの投稿が表示されなくなります。`)) return;
    await apiPost('/api/block', { blocker: State.currentUser, blocked: targetUser });
    showToast('ユーザーをブロックしました。');
    location.reload();
}

async function hideItem(type, id) {
    if (!State.currentUser) { showToast('非表示機能にはログインが必要です'); return; }
    await apiPost('/api/hide', { username: State.currentUser, target_type: type, target_id: id });
    if (type === 'word') {
        const hidden = JSON.parse(localStorage.getItem('hiddenWords') || '[]');
        hidden.push(id);
        localStorage.setItem('hiddenWords', JSON.stringify(hidden));
        navigate('archive');
    }
    showToast('この項目を非表示にしました。');
}

async function adminDeleteContent(type, id) {
    if (!confirm('【管理者権限】この投稿を完全に削除しますか？')) return;
    await apiPost('/api/admin/delete-content', { admin_username: State.currentUser, target_type: type, target_id: id });
    showToast('コンテンツを削除しました。');
    location.reload();
}

async function renderConnections() {
    if (!State.currentUser) return navigate('premium');
    const blocked = await apiGet(`/api/blocked-users?username=${State.currentUser}`);
    const follows = await apiGet(`/api/follows?username=${State.currentUser}`);
    const hiddens = await apiGet(`/api/hidden-items?username=${State.currentUser}`);

    viewContainer.innerHTML = `
        <div class="connections-view fade-in" style="max-width:600px; margin: 0 auto; padding: 3rem;">
            <h3 class="section-label">Manage Connections</h3>
            
            <section style="margin-bottom:3rem;">
                <h4 class="section-label" style="font-size:0.8rem; margin-bottom:1rem;">Following</h4>
                ${follows.map(u => `
                    <div style="display:flex; justify-content:space-between; align-items:center; background:var(--color-surface); padding:1rem; border-radius:12px; margin-bottom:0.5rem;">
                        <span>${u}</span>
                        <button onclick="unfollowUser('${u}')" class="chip">Unfollow</button>
                    </div>
                `).join('') || '<p class="dimmed">No following users.</p>'}
            </section>

            <section style="margin-bottom:3rem;">
                <h4 class="section-label" style="font-size:0.8rem; margin-bottom:1rem; color:#721c24;">Blocked Users</h4>
                ${blocked.map(u => `
                    <div style="display:flex; justify-content:space-between; align-items:center; background:var(--color-surface); padding:1rem; border-radius:12px; margin-bottom:0.5rem;">
                        <span>${u}</span>
                        <button onclick="unblockUser('${u}')" class="chip">Unblock</button>
                    </div>
                `).join('') || '<p class="dimmed">No blocked users.</p>'}
            </section>

            <section>
                <h4 class="section-label" style="font-size:0.8rem; margin-bottom:1rem;">Hidden Items</h4>
                ${hiddens.map(h => `
                    <div style="display:flex; justify-content:space-between; align-items:center; background:var(--color-surface); padding:1rem; border-radius:12px; margin-bottom:0.5rem;">
                        <span style="font-size:0.85rem;">${h.type} ID: ${h.id}</span>
                        <button onclick="unhideItem('${h.type}', ${typeof h.id === 'string' ? `'${h.id}'` : h.id})" class="chip">Show</button>
                    </div>
                `).join('') || '<p class="dimmed">No hidden items.</p>'}
            </section>
        </div>
    `;
}

function renderArchive() {
    viewContainer.innerHTML = `
            <div style="max-width:600px; margin: 0 auto 1.5rem auto; display:flex; flex-direction:column; gap:1rem;">
                <div style="text-align:center;">
                    <button onclick="navigate('contribute')" class="primary-btn" style="padding:1rem 2rem; border-radius:100px; font-size:0.9rem;">+ Contribute Word</button>
                </div>
                <div style="position:relative;">
                    <input type="text" id="archive-search" placeholder="Search by word or meaning..." value="${State.searchFilter || ''}" style="width:100%; padding:1.2rem 3rem; background:var(--color-surface); border:1px solid var(--color-border); border-radius:100px; color:white; font-size:1.1rem;">
                    <span style="position:absolute; left:1.2rem; top:50%; transform:translateY(-50%); opacity:0.5;">🔍</span>
                </div>
            </div>
            <div id="archive-stats" style="text-align:center; margin-bottom:2rem; font-size:0.9rem; color:var(--color-text-dim);">
                <!-- Total count will be here -->
            </div>
            <div class="alphabet-bar" style="display:flex; flex-wrap:wrap; gap:6px; margin-bottom: 3rem; justify-content:center;">
                ${'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('').map(l => `
                    <button class="index-letter ${State.letterFilter === l ? 'active' : ''}" onclick="State.letterFilter='${l}';State.searchFilter=null;renderArchive()">${l}</button>
                `).join('')}
                <button class="index-letter" style="width:auto; padding:0 12px;" onclick="State.letterFilter=null;State.searchFilter=null;renderArchive()">ALL</button>
            </div>
            <div id="archive-grid" class="archive-grid" style="display:grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap:2rem;">
                <!-- Content will be updated by updateArchiveGrid -->
            </div>
        </div>
    `;
    updateArchiveGrid();

    const searchInput = document.getElementById('archive-search');
    if (searchInput) {
        searchInput.oninput = (e) => {
            State.searchFilter = e.target.value.toLowerCase();
            State.letterFilter = null;
            updateArchiveGrid();
        };
    }
}

function updateArchiveGrid() {
    const grid = document.getElementById('archive-grid');
    if (!grid) return;

    let list = (typeof WORDS !== 'undefined') ? [...WORDS] : [];
    const totalCount = list.length;
    list.sort((a, b) => a.word.localeCompare(b.word));

    // 非表示フィルタの適用
    if (localStorage.getItem('hiddenWords')) {
        const hiddenIds = JSON.parse(localStorage.getItem('hiddenWords'));
        list = list.filter(w => !hiddenIds.includes(w.id));
    }

    if (State.searchFilter) {
        const query = State.searchFilter.toLowerCase();
        list = list.filter(w =>
            (w.word && w.word.toLowerCase().includes(query)) ||
            (w.meaning && w.meaning.toLowerCase().includes(query)) ||
            (w.etymology && w.etymology.breakdown && Array.isArray(w.etymology.breakdown) && w.etymology.breakdown.some(b => b.text && b.text.toLowerCase().includes(query)))
        );
    } else if (State.letterFilter) {
        list = list.filter(w => w.word.toUpperCase().startsWith(State.letterFilter));
    }

    const statsElem = document.getElementById('archive-stats');
    if (statsElem) {
        if (State.searchFilter || State.letterFilter) {
            statsElem.innerHTML = `Found <b style="color:var(--color-accent);">${list.length}</b> / <b style="color:var(--color-text);">${totalCount}</b> total words in Archive`;
        } else {
            statsElem.innerHTML = `Exploration Archive: <b style="color:var(--color-text); font-size:1.2rem;">${totalCount}</b> total words`;
        }
    }

    grid.innerHTML = list.map(w => `
        <div class="archive-item" onclick="State.todayWord=(typeof WORDS !== 'undefined') ? WORDS.find(x=>x.id==='${w.id}') : null;navigate('today')" style="position:relative; padding:1.8rem; border:1px solid var(--color-border); border-radius:20px; background:var(--color-surface); min-height:180px; display:flex; flex-direction:column; justify-content:space-between; transition:all 0.3s ease; cursor:pointer;">
            <div style="text-align: left;">
                <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:0.5rem;">
                    <span style="font-weight:700; font-size:1.5rem; color:var(--color-accent); letter-spacing:-0.02em;">${w.word}</span>
                    ${w.part_of_speech ? `<span style="font-size:0.7rem; font-style:italic; opacity:0.5; border:1px solid rgba(255,255,255,0.1); padding:2px 6px; border-radius:4px;">${w.part_of_speech}</span>` : ''}
                </div>
                <div style="font-size:0.9rem; color:var(--color-text); font-weight:500; margin-bottom:0.8rem;">${w.meaning || ''}</div>
                <div style="font-size:0.85rem; opacity:0.6; line-height:1.4; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden;">${w.core_concept?.ja || w.concept || ''}</div>
            </div>
            <div style="font-size:0.75rem; opacity:0.4; text-align:right; border-top: 1px solid rgba(255,255,255,0.05); padding-top:0.8rem; margin-top:auto;">
                by <b style="opacity:1;">${w.author || 'etymon_official'}</b>
            </div>
        </div>
    `).join('') || '<p class="dimmed" style="grid-column: 1/-1; text-align:center;">No words matched your criteria.</p>';
}

async function renderEssays() {
    viewContainer.innerHTML = `
        <div class="essays-view fade-in" style="text-align:center; padding: 5rem;">
            <p class="dimmed">Gathering thoughts from the deep sea...</p>
        </div>`;

    const officialEssays = (typeof ESSAYS !== 'undefined') ? [...ESSAYS] : [];
    let userEssays = [];
    try {
        userEssays = await apiGet('/api/user-essays');
        if (!Array.isArray(userEssays)) userEssays = [];
    } catch (e) {
        console.error("Failed to fetch user essays:", e);
    }

    const allEssays = [...officialEssays, ...userEssays];
    // 日付順にソート（日付がない場合は古いものとして扱う）
    allEssays.sort((a, b) => (b.date || '').localeCompare(a.date || ''));
    window.ESSAY_CACHE = allEssays;

    let list = allEssays;
    if (localStorage.getItem('hiddenEssays')) {
        const hiddenIds = JSON.parse(localStorage.getItem('hiddenEssays'));
        list = list.filter(e => !hiddenIds.includes(e.id));
    }

    viewContainer.innerHTML = `
        <div class="essays-view fade-in">
            <h3 class="section-label" style="text-align:center; margin-bottom:4rem; font-size:1.4rem;">Weekly Philology</h3>
            
            ${State.isPremium ? `
                <div style="text-align:center; margin-bottom:3rem;">
                    <button onclick="renderEssayForm()" class="primary-btn" style="padding:1rem 2rem; border-radius:100px; font-size:0.9rem;">+ Write Essay</button>
                </div>
            ` : ''}

            <div class="essay-list">${list.map(e => `
                <div class="essay-card" onclick="openEssay('${e.id}')" style="background:var(--color-surface); padding:3rem; border-radius:24px; margin-bottom:2rem; border:1px solid var(--color-border); cursor:pointer; position:relative;">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <span class="dimmed" style="font-size:0.9rem;">${e.date || 'Unknown Date'}</span>
                        <span class="dimmed" style="font-size:0.8rem;">by <b>${e.author || 'etymon_official'}</b></span>
                    </div>
                    <h2 style="margin: 1rem 0; font-size:2rem; line-height:1.2;">${e.title} ${!State.isPremium ? '🔒' : ''}</h2>
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <p class="dimmed">Tap to experience the depth...</p>
                        ${State.isPremium ? `<span class="essay-save-icon" style="font-size:1.5rem;">${State.savedEssayIds.includes(e.id) ? '🔖' : '📑'}</span>` : ''}
                    </div>
                </div>`).join('') || '<p class="dimmed" style="text-align:center;">Deep sea of thoughts is being prepared...</p>'}</div>
        </div>`;
}

function renderEssayForm() {
    viewContainer.innerHTML = `
        <div class="contribute-view fade-in" style="max-width:640px; margin: 0 auto; padding-bottom:120px;">
            <header style="margin-bottom:3rem; display:flex; gap:1rem; align-items:center;">
                <button onclick="navigate('essays')" class="chip">← Back</button>
                <h3 class="section-label">Write Essay</h3>
            </header>
            <form id="essay-form" style="background:var(--color-surface); padding:3rem; border-radius:32px; border:1px solid var(--color-border);">
                <div class="input-group"><label>Title</label><input type="text" id="e-title" required style="width:100%; background:var(--color-bg); border-radius:12px; border:1px solid var(--color-border); color:white; padding:1.2rem;"></div>
                <div class="input-group" style="margin-top:2rem;"><label>Content</label><textarea id="e-content" rows="15" required style="width:100%; background:var(--color-bg); border-radius:12px; border:1px solid var(--color-border); color:white; padding:1.5rem; font-size: 1.1rem; line-height: 1.6;"></textarea></div>
                <button type="submit" id="submit-essay-btn" class="primary-btn" style="width:100%; margin-top:3rem; padding:1.5rem; font-weight:bold; font-size:1.2rem; border-radius:16px;">Publish Essay</button>
            </form>
        </div>`;
    document.getElementById('essay-form').onsubmit = async (e) => {
        e.preventDefault();
        const btn = document.getElementById('submit-essay-btn');
        if (btn) { btn.innerText = 'Publishing...'; btn.disabled = true; }

        const res = await apiPost('/api/submit-essay', {
            username: State.currentUser,
            title: document.getElementById('e-title').value,
            content: document.getElementById('e-content').value
        });

        if (res.status === 'success') {
            showRichToast('✦ Essay Published', 'あなたの思索が世界に放たれました。');
            navigate('essays');
        } else {
            showToast(res.message);
            if (btn) { btn.innerText = 'Publish Essay'; btn.disabled = false; }
        }
    };
}

function openEssay(id) {
    if (!State.isPremium) { showToast('Premium access required.'); navigate('premium'); return; }

    // JSデータまたはDBデータ(キャッシュ)から検索
    let e = (typeof ESSAYS !== 'undefined') ? ESSAYS.find(x => x.id === id) : null;
    if (!e) {
        e = window.ESSAY_CACHE && window.ESSAY_CACHE.find(x => x.id === id);
    }
    if (!e) return;

    viewContainer.innerHTML = `
        <div class="essay-content fade-in" style="max-width:800px; margin:0 auto; padding-bottom:100px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:3rem;">
                <button class="chip" onclick="navigate('essays')">← Archives</button>
                <div class="word-options-container" style="position:relative;">
                    <button id="essay-options-trigger" style="background:none; border:none; font-size:1.8rem; cursor:pointer; color:var(--color-text-dim);">⋯</button>
                    <div id="essay-options-menu" style="display:none; position:absolute; top:40px; right:0; background:var(--color-surface); border:1px solid var(--color-border); border-radius:12px; box-shadow:0 10px 30px rgba(0,0,0,0.3); z-index:100; min-width:160px; overflow:hidden;">
                        <button onclick="toggleSaveEssay('${e.id}')" style="width:100%; padding:1rem; background:none; border:none; color:white; text-align:left; cursor:pointer; font-size:0.9rem; border-bottom:1px solid var(--color-border);">
                            ${State.savedEssayIds.includes(e.id) ? '🔖 Unsaved' : '📑 Favorite Essay'}
                        </button>
                        <button onclick="hideEssay('${e.id}')" style="width:100%; padding:1rem; background:none; border:none; color:white; text-align:left; cursor:pointer; font-size:0.9rem;">
                            👁️‍🗨️ Hide this Essay
                        </button>
                    </div>
                </div>
            </div>
            <header style="margin-bottom: 5rem;">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span class="dimmed" style="font-size:1rem;">${e.date}</span>
                    <div style="display:flex; gap:10px; align-items:center;">
                        <span class="dimmed">by <b>${e.author || 'etymon_official'}</b></span>
                        ${e.author && e.author !== State.currentUser && e.author !== 'etymon_official' ? `<button onclick="followUser('${e.author}')" class="chip ${State.followedUsers.includes(e.author) ? 'followed' : ''}" style="font-size:0.7rem;">${State.followedUsers.includes(e.author) ? 'Followed' : 'Follow'}</button>` : ''}
                    </div>
                </div>
                <h1 style="font-size:3.5rem; margin:1.5rem 0; line-height:1.1; letter-spacing:-0.03em;">${e.title}</h1>
            </header>
            <div class="essay-body" style="font-size:1.3rem; line-height:2.1; color:var(--color-text); font-family: 'Inter', sans-serif; white-space: pre-wrap; overflow-wrap: break-word; word-break: break-word; padding-left: 1rem; border-left: 2px solid rgba(255,255,255,0.03);">${e.content}</div>
            
            <div style="display:flex; justify-content:center; margin-top:3rem; margin-bottom: 2rem;">
                <button id="fl-btn-essay-${e.id}" onclick="toggleFlourish('essay', '${e.id}', this, '${e.author || 'etymon_official'}')"
                    style="background:none; border:1px solid var(--color-border); color:var(--color-text-dim); font-size:0.9rem; padding:0.5rem 1.2rem; border-radius:100px; cursor:pointer; transition:all 0.2s; display:flex; align-items:center; gap:6px;">
                    ✦ Flourish · <span class="fl-cnt" id="fl-cnt-essay-${e.id}">…</span>
                </button>
            </div>

            <footer style="margin-top: 4rem; padding-top: 1.5rem; border-top: 1px solid var(--color-border); opacity:0.4; font-size:0.75rem; font-style:italic;">
                ※ 本エッセイは、一部AIによって生成された、またはAIの補助を受けて作成された可能性があります。
            </footer>
            ${renderReflectionSection(e.id)}
        </div>`;

    // Flourishカウント取得
    apiGet(`/api/flourish-count?target_type=essay&target_id=${e.id}&username=${State.currentUser || ''}`)
        .then(fc => {
            const cnt = document.getElementById(`fl-cnt-essay-${e.id}`);
            const btn = document.getElementById(`fl-btn-essay-${e.id}`);
            if (cnt) cnt.textContent = fc.count;
            if (btn && fc.flourished) {
                btn.style.borderColor = 'var(--color-premium)';
                btn.style.color = 'var(--color-premium)';
                btn.dataset.flourished = 'true';
            }
        }).catch(() => { });

    loadReflections(e.id, e.author || 'etymon_official', e.title);

    const trigger = document.getElementById('essay-options-trigger');
    const menu = document.getElementById('essay-options-menu');
    if (trigger && menu) {
        trigger.onclick = (ev) => { ev.stopPropagation(); menu.style.display = menu.style.display === 'block' ? 'none' : 'block'; };
        document.addEventListener('click', () => { menu.style.display = 'none'; }, { once: true });
    }
}

async function toggleSaveEssay(id) {
    if (State.currentUser) {
        const res = await apiPost('/api/save-item', { username: State.currentUser, target_type: 'essay', target_id: id });
        if (res.status === 'success') {
            const idx = State.savedEssayIds.indexOf(id);
            if (res.action === 'saved' && idx === -1) State.savedEssayIds.push(id);
            else if (res.action === 'unsaved' && idx > -1) State.savedEssayIds.splice(idx, 1);
        }
    } else {
        const idx = State.savedEssayIds.indexOf(id);
        if (idx > -1) State.savedEssayIds.splice(idx, 1);
        else State.savedEssayIds.push(id);
    }
    localStorage.setItem('savedEssays', JSON.stringify(State.savedEssayIds));
    openEssay(id);
}

function hideEssay(id) {
    const hidden = JSON.parse(localStorage.getItem('hiddenEssays') || '[]');
    hidden.push(id);
    localStorage.setItem('hiddenEssays', JSON.stringify(hidden));
    navigate('essays');
    showToast('Essay hidden.');
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
                    ${savedWords.map(w => `<div class="archive-item" onclick="State.todayWord=(typeof WORDS !== 'undefined') ? WORDS.find(x=>x.id==='${w.id}') : null;navigate('today')" style="padding:2rem; border:1px solid var(--color-border); border-radius:24px; background:var(--color-surface); font-weight:bold; color:var(--color-accent); font-size:1.4rem; text-align:center; cursor:pointer;">${w.word}</div>`).join('') || '<p class="dimmed">No words in inventory.</p>'}
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
                    ${State.currentUser ? `
                    <button onclick="navigate('my-posts')" class="primary-btn" style="width:100%; padding:1rem; border-radius:12px; background:transparent; border:1px solid var(--color-accent); color:var(--color-accent); margin-top:1rem;">
                        My Posts (Manage Content)
                    </button>
                    <button onclick="navigate('connections')" class="primary-btn" style="width:100%; padding:1rem; border-radius:12px; background:transparent; border:1px solid var(--color-accent); color:var(--color-accent); margin-top:1rem;">
                        Connections (Follow & Blocks)
                    </button>
                    <button onclick="requestDeleteAccount()" class="primary-btn" style="width:100%; padding:1rem; border-radius:12px; background:transparent; border:1px solid #721c24; color:#f8d7da; margin-top:1rem; font-size:0.8rem;">
                        Delete Account (Identity Erasure)
                    </button>
                    ` : ''}
                    ${State.isOperator ? `
                    <button onclick="navigate('admin')" class="primary-btn" style="width:100%; padding:1rem; border-radius:12px; background:var(--color-premium); color:white; margin-top:1rem;">
                        Admin Dashboard
                    </button>
                    ` : ''}
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
function renderDeepDiveLock() {
    return `
        <div class="lock-container" onclick="navigate('premium')" style="padding:4rem; border:1px dashed var(--color-border); border-radius:24px; text-align:center; cursor:pointer; margin-top:4rem; background:rgba(255,255,255,0.02); transition:all 0.3s;">
            <div style="font-size:2.5rem; margin-bottom:1rem;">🕯️</div>
            <div style="font-weight:bold; color:var(--color-premium); font-size:1.2rem; margin-bottom:1.5rem;">Illuminate the Deep Roots</div>
            <ul style="list-style:none; padding:0; text-align:left; max-width:280px; margin:0 auto; font-size:0.9rem; line-height:1.8; color:var(--color-text-dim);">
                <li>✨ 週間フィロロジー・エッセイの閲覧</li>
                <li>✨ 広告の完全非表示</li>
                <li>✨ 同語源を持つ単語一覧の開放</li>
                <li>✨ 他のユーザーによる思索（Reflection）の閲覧</li>
                <li>✨ 印欧祖語（PIE）のルーツ解析</li>
            </ul>
            <p style="margin-top:2rem; font-weight:bold; color:var(--color-premium);">タップして深淵へ</p>
        </div>
    `;
}

function renderPremium() {
    if (State.isPremium && State.currentUser) { viewContainer.innerHTML = `<div class="premium-view" style="text-align:center; padding:8rem 2rem;"><div style="font-size:4rem; margin-bottom:2rem;">✨</div><h2>Citizen ${State.currentUser}</h2><p class="dimmed">Your mind is connected to the deeper structures.</p><button onclick="logout()" class="primary-btn" style="margin-top:4rem; background:transparent; border:1px solid var(--color-border);">Leave Identity</button></div>`; return; }
    if (!State.currentUser) {
        viewContainer.innerHTML = `<div class="auth-view fade-in" style="max-width:420px; margin: 6rem auto; padding: 3.5rem; background:var(--color-surface); border-radius:32px; border:1px solid var(--color-border);"><h2 id="auth-title" style="text-align:center; margin-bottom:3rem; font-weight:300; letter-spacing:0.2em;">IDENTITY</h2><div class="input-group"><label>Username</label><input type="text" id="auth-username" style="width:100%; background:var(--color-bg); padding:1rem; border-radius:12px; border:1px solid var(--color-border); color:white;"></div><div class="input-group" style="margin-top:1.5rem;"><label>Password</label><input type="password" id="auth-password" style="width:100%; background:var(--color-bg); padding:1rem; border-radius:12px; border:1px solid var(--color-border); color:white;"></div><button id="auth-submit" class="primary-btn" style="width:100%; margin-top:3rem; padding:1.2rem; border-radius:14px; font-weight:bold; font-size:1.1rem;">ENTER</button><p style="text-align:center; margin-top:2rem;"><a href="#" id="auth-toggle" style="opacity:0.5; font-size:0.85rem; text-decoration:none;">Initialize New Identity</a></p></div>`;
        setupAuthListeners(); return;
    }
    viewContainer.innerHTML = `
        <div class="premium-view" style="text-align:center; padding:6rem 2rem;">
            <div style="font-size:3.5rem; margin-bottom:1.5rem;">🔱</div>
            <h2>The Inner Circle</h2>
            <div class="premium-benefits" style="max-width:450px; margin: 2rem auto 4rem; text-align:left; background:var(--color-surface); padding:2rem; border-radius:24px; border:1px solid var(--color-border);">
                <ul style="list-style:none; padding:0; line-height:2.2; font-size:1.1rem;">
                    <li>📖 <b>Scholarly Essays</b>: 毎週更新される深い語源的洞察</li>
                    <li>🚫 <b>No Advertisements</b>: 広告のない洗練された読書体験</li>
                    <li>🔗 <b>Deep Connections</b>: 同語源の単語をリンクし、知の鎖を辿る</li>
                    <li>🧠 <b>Shared Reflections</b>: 他のユーザーが残した思索の痕跡を辿る</li>
                    <li>🏺 <b>Archaic Roots</b>: 究極のルーツである印欧祖語（PIE）の解析</li>
                </ul>
            </div>
            <button id="buy-premium-btn" class="primary-btn" style="width:100%; max-width:400px; padding:1.8rem; font-size:1.3rem; border-radius:20px; box-shadow: 0 10px 30px rgba(var(--color-accent-rgb), 0.3);">UNSEAL ALL LAYERS (¥980/mo)</button>
        </div>`;
    document.getElementById('buy-premium-btn').onclick = async () => { const res = await apiPost('/create-checkout-session?username=' + State.currentUser, {}); const stripe = Stripe('pk_test_51T5KW45XPK1iD6ycU5CgxWXqSgxgKUDSNWImeARHpDFXHrfBC1y8BI4w4tr2cvftIb9uiSickAv3PoGIM5i2SX5F00W2Uz21M8'); await stripe.redirectToCheckout({ sessionId: res.id }); };
}

async function renderAdmin() {
    if (!State.isOperator) return navigate('today');
    const reports = await apiGet(`/api/admin/reports?username=${State.currentUser}`);
    viewContainer.innerHTML = `
        <div class="admin-view fade-in" style="max-width:800px; margin: 0 auto; padding: 3rem;">
            <h2 class="section-label">Operator Dashboard</h2>
            <div class="report-list" style="margin-top:2rem;">
                ${reports.map(r => `
                    <div style="background:var(--color-surface); padding:2rem; border-radius:16px; margin-bottom:1.5rem; border:1px solid var(--color-border);">
                        <div style="display:flex; justify-content:space-between; margin-bottom:1rem;">
                            <span><b>Reporter:</b> ${r.reporter}</span>
                            <span class="dimmed">${r.date}</span>
                        </div>
                        <p><b>Target:</b> ${r.target_username} (${r.target_type} ID: ${r.target_id})</p>
                        <p style="background:rgba(255,0,0,0.1); padding:1rem; border-radius:8px; margin:1rem 0;"><b>Reason:</b> ${r.reason}</p>
                        <div style="display:flex; gap:10px;">
                            <button onclick="adminDeleteContent('${r.target_type}', ${r.target_id})" class="chip" style="background:red; color:white;">Delete Content</button>
                            <button onclick="showToast('無視しました')" class="chip">Dismiss</button>
                        </div>
                    </div>
                `).join('') || '<p class="dimmed">No pending reports.</p>'}
            </div>
        </div>
    `;
}

async function requestDeleteAccount() {
    const password = prompt('アカウントを完全に削除します。確認のためにパスワードを入力してください：');
    if (!password) return;
    if (!confirm('本当に削除しますか？この操作は取り消せません。')) return;
    const res = await apiPost('/api/delete-account', { username: State.currentUser, password: password });
    if (res.status === 'success') {
        showToast('アカウントを消去しました。');
        logout();
    } else {
        showToast(res.message);
    }
}

function setupAuthListeners() {
    let mode = 'login';
    const title = document.getElementById('auth-title'), submit = document.getElementById('auth-submit'), toggle = document.getElementById('auth-toggle');
    toggle.onclick = (e) => { e.preventDefault(); mode = (mode === 'login' ? 'register' : 'login'); title.textContent = (mode === 'login' ? 'IDENTITY' : 'INITIALIZE'); submit.textContent = (mode === 'login' ? 'ENTER' : 'REGISTER'); };
    submit.onclick = async () => {
        const username = document.getElementById('auth-username').value, password = document.getElementById('auth-password').value;
        const res = await apiPost('/api/' + mode, { username, password });
        if (res.status === 'success') { if (mode === 'register') { showToast('Success. Please login.'); mode = 'login'; setupAuthListeners(); } else { State.currentUser = username; State.isPremium = res.is_premium; State.isOperator = res.is_operator; localStorage.setItem('currentUser', username); localStorage.setItem('isPremium', res.is_premium); localStorage.setItem('isOperator', res.is_operator); applySettings(); await loadFollows(); navigate('today'); } }
        else showToast(res.message);
    };
}

function logout() { localStorage.clear(); location.reload(); }

async function navigate(view) {
    State.currentView = view;
    Object.keys(navItems).forEach(k => { if (navItems[k]) navItems[k].classList.toggle('active', k === view); });

    // 切り替え時に一旦非表示にする、またはローディング表示を検討
    viewContainer.style.opacity = '0';

    setTimeout(async () => {
        // 表示の初期化とローディングの表示
        viewContainer.innerHTML = `
            <div class="loading-indicator">
                <div class="spinner"></div>
                <p>少々お時間をください...</p>
            </div>
        `;
        viewContainer.style.opacity = '1';

        try {
            switch (view) {
                case 'today': renderToday(); break;
                case 'archive': renderArchive(); break;
                case 'saved': renderSaved(); break;
                case 'contribute': renderContribute(); break;
                case 'essays': await renderEssays(); break;
                case 'settings': renderSettings(); break;
                case 'premium': renderPremium(); break;
                case 'admin': await renderAdmin(); break;
                case 'my-posts': await renderMyPosts(); break;
                case 'connections': await renderConnections(); break;
                case 'notifications': await renderNotifications(); break;
                case 'network': await renderWordNetwork(); break;
                case 'timeline': renderTimeline(); break;
                case 'etymap': renderEtyMap(); break;
                case 'synthesizer': renderSynthesizer(); break;
            }
        } catch (err) {
            console.error("Navigation error:", err);
            viewContainer.innerHTML = `<div style="padding:5rem; text-align:center;">Error loading view. <button onclick="location.reload()" class="chip">Reload</button></div>`;
        }
        viewContainer.style.opacity = '1';
        viewContainer.classList.add('fade-in');
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }, 50);
}

function setupNavListeners() {
    if (navItems.today) navItems.today.onclick = () => navigate('today');
}

async function toggleTTS(base64Text) {
    if (window.currentAudio) {
        window.currentAudio.pause();
        window.currentAudio = null;
        showToast("Playback stopped.");
        return;
    }
    const text = decodeURIComponent(escape(atob(base64Text)));
    showToast("Generating voice... (Echo)");
    try {
        const response = await fetch(`${API_BASE}/api/tts`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text, username: State.currentUser })
        });
        if (!response.ok) throw new Error("TTS failed");
        const blob = await response.blob();
        const url = URL.createObjectURL(blob);
        window.currentAudio = new Audio(url);
        window.currentAudio.play();
        window.currentAudio.onended = () => { window.currentAudio = null; };
    } catch (e) {
        showToast("TTS Error: " + e.message);
    }
}

async function renderWordNetwork(mode = 'global') {
    const ids = State.savedWordIds.join(',');
    viewContainer.innerHTML = `
        <div class="network-view fade-in" style="height: calc(100vh - 200px); position:relative;">
            <div style="display:flex; justify-content:center; gap:1rem; padding-top:1.5rem; position: relative; z-index: 20;">
                <button id="net-global" class="chip ${mode === 'global' ? 'followed' : ''}">Global Universe</button>
                <button id="net-personal" class="chip ${mode === 'personal' ? 'followed' : ''}">My Mind Garden</button>
                <button id="net-reload" class="chip" style="border-color: var(--color-accent); color: var(--color-accent); flex-shrink: 0;"><span style="font-size:1.1rem; vertical-align:middle; margin-right:4px;">↻</span> Regenerate</button>
            </div>
            <div id="network-graph" style="height:calc(100% - 60px); width:100%; display:flex; align-items:center; justify-content:center;">
                <div class="loading-indicator">
                    <div class="spinner"></div>
                    <p>思考の宇宙を再構成中...</p>
                </div>
            </div>
            <div style="position:absolute; bottom:20px; left:20px; background:var(--color-surface); padding:1.2rem; border-radius:16px; border:1px solid var(--color-border); font-size:0.8rem; opacity:0.95; line-height:1.7; z-index:10; box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
                <div style="font-weight:bold; margin-bottom:0.5rem; border-bottom:1px solid var(--color-border); padding-bottom:0.3rem;">Legend</div>
                <div style="display:flex; align-items:center; gap:8px;"><span style="width:12px; height:12px; background:${PART_COLORS.word}; border-radius:50%; display:inline-block;"></span> 🔵 Word (Click to view)</div>
                <div style="display:flex; align-items:center; gap:8px;"><span style="width:12px; height:12px; background:${PART_COLORS.root}; border-radius:50%; display:inline-block;"></span> 🟡 Root (Click to search)</div>
                <div style="display:flex; align-items:center; gap:8px;"><span style="width:12px; height:12px; background:${PART_COLORS.prefix}; border-radius:50%; display:inline-block;"></span> 🟢 Prefix (Click to search)</div>
                <div style="display:flex; align-items:center; gap:8px;"><span style="width:12px; height:12px; background:${PART_COLORS.suffix}; border-radius:50%; display:inline-block;"></span> 🔴 Suffix (Click to search)</div>
            </div>
        </div>
    `;

    document.getElementById('net-global').onclick = () => renderWordNetwork('global');
    document.getElementById('net-personal').onclick = () => renderWordNetwork('personal');
    document.getElementById('net-reload').onclick = () => renderWordNetwork(mode);

    // キャッシュを回避するためにランダムなパラメータ(t)を付与することで、常に新しいランダムの500単語を取得
    const data = await apiGet(`/api/word-network?mode=${mode}&username=${State.currentUser || ''}&ids=${ids}&t=${Date.now()}`);
    const container = document.getElementById('network-graph');

    // Resolve CSS variables for canvas rendering before creating the dataset
    const wordColor = resolveColor(PART_COLORS.word);
    const rootColor = resolveColor(PART_COLORS.root);
    const prefixColor = resolveColor(PART_COLORS.prefix);
    const suffixColor = resolveColor(PART_COLORS.suffix);

    const nodes = new vis.DataSet(data.nodes.map(n => ({
        ...n,
        font: { color: '#ffffff', size: 14, strokeWidth: 2, strokeColor: '#000000' },
        shape: 'dot',
        size: n.group === 'word' ? 15 : 25
    })));
    const edges = new vis.DataSet(data.edges);
    const options = {
        physics: { stabilization: true, barnesHut: { gravitationalConstant: -2000 } },
        edges: { color: 'rgba(255,255,255,0.2)' },
        groups: {
            word: { color: wordColor },
            root: { color: rootColor },
            prefix: { color: prefixColor },
            suffix: { color: suffixColor }
        }
    };
    const network = new vis.Network(container, { nodes, edges }, options);
    network.on("click", function (params) {
        if (params.nodes.length > 0) {
            const nodeId = params.nodes[0];
            const nodeData = nodes.get(nodeId);
            if (nodeData && (nodeData.group === 'root' || nodeData.group === 'prefix' || nodeData.group === 'suffix')) {
                searchToArchive(nodeData.label);
            } else {
                const word = (typeof WORDS !== 'undefined') ? WORDS.find(w => w.word === nodeId) : null;
                if (word) {
                    State.todayWord = word;
                    navigate('today');
                }
            }
        }
    });
}

function renderTimeline() {
    const list = (typeof WORDS !== 'undefined') ? [...WORDS] : [];

    // --- 起源言語を抽出するヘルパー ---
    const extractLanguage = (word) => {
        const stmt = ((word.etymology && word.etymology.original_statement) || '').toLowerCase();
        const era = (word.era || '').toLowerCase();

        if (stmt.includes('proto-indo-european') || era.includes('proto-indo-european') || era.includes('pie')) return 'Proto-Indo-European';
        if (stmt.includes('proto-germanic') || era.includes('proto-germanic')) return 'Proto-Germanic';
        if (stmt.includes('ancient greek') || stmt.includes('from greek') || era.includes('ancient greek') || era.includes('greek')) return 'Ancient Greek';
        if (stmt.includes('from latin') || era.includes('latin')) return 'Latin';
        if (stmt.includes('old norse') || era.includes('old norse')) return 'Old Norse';
        if (stmt.includes('old english') || era.includes('old english')) return 'Old English';
        if (stmt.includes('old french') || era.includes('old french')) return 'Old French';
        if (stmt.includes('middle english') || era.includes('middle english')) return 'Middle English';
        if (stmt.includes('from french') || era.includes('french')) return 'French';
        if (stmt.includes('from arabic') || era.includes('arabic')) return 'Arabic';
        if (stmt.includes('from italian') || era.includes('italian')) return 'Italian';
        if (stmt.includes('from spanish') || era.includes('spanish')) return 'Spanish';
        if (stmt.includes('from german') || era.includes('german')) return 'German';
        if (stmt.includes('from dutch') || era.includes('dutch')) return 'Dutch';
        if (stmt.includes('from japanese') || era.includes('japanese')) return 'Japanese';
        if (stmt.includes('from hebrew') || era.includes('hebrew')) return 'Hebrew';
        return 'Other / Unknown';
    };

    // --- 言語の時系列スコア ---
    const LANG_SCORE = {
        'Proto-Indo-European': -5000,
        'Proto-Germanic': -2000,
        'Ancient Greek': -800,
        'Latin': -700,
        'Old Norse': 850,
        'Old English': 900,
        'Old French': 950,
        'Middle English': 1200,
        'Arabic': 1300,
        'French': 1400,
        'Italian': 1450,
        'Spanish': 1500,
        'German': 1550,
        'Dutch': 1600,
        'Hebrew': 1700,
        'Japanese': 1800,
        'Other / Unknown': 9999,
    };

    // --- 単語内 era スコア（グループ内ソート用）---
    const getEraScore = (era) => {
        const e = (era || '').toLowerCase();
        if (e.includes('pie') || e.includes('proto')) return -10000;
        if (e.includes('ancient')) return -5000;
        if (e.includes('old english')) return -3000;
        if (e.includes('latin') || e.includes('greek')) return -2000;
        if (e.includes('middle english')) return -1000;
        const cen = e.match(/(\d+)th\s*century/);
        if (cen) return parseInt(cen[1]) * 100;
        const yr = e.match(/(\d{3,4})/);
        if (yr) return parseInt(yr[1]);
        return 0;
    };

    // --- 言語別グループ化 ---
    const allGroups = {};
    list.forEach(w => {
        const lang = extractLanguage(w);
        if (!allGroups[lang]) allGroups[lang] = [];
        allGroups[lang].push(w);
    });

    // 言語グループを時系列順にソート
    const sortedLangs = Object.keys(allGroups).sort((a, b) =>
        (LANG_SCORE[a] ?? 5000) - (LANG_SCORE[b] ?? 5000)
    );

    // 各言語グループ内をもとのeraスコアでソート
    sortedLangs.forEach(lang => {
        allGroups[lang].sort((a, b) => getEraScore(a.era) - getEraScore(b.era));
    });

    const langToId = (lang) => 'lang-' + lang.replace(/[^a-zA-Z0-9]/g, '_');

    // 言語ラベルを絵文字付きで見やすく
    const LANG_LABEL = {
        'Proto-Indo-European': 'Proto-Indo-European',
        'Proto-Germanic': 'Proto-Germanic',
        'Ancient Greek': 'Ancient Greek',
        'Latin': 'Latin',
        'Old Norse': 'Old Norse',
        'Old English': 'Old English',
        'Old French': 'Old French',
        'Middle English': 'Middle English',
        'Arabic': 'Arabic',
        'French': 'French',
        'Italian': 'Italian',
        'Spanish': 'Spanish',
        'German': 'German',
        'Dutch': 'Dutch',
        'Hebrew': 'Hebrew',
        'Japanese': 'Japanese',
        'Other / Unknown': 'Other / Unknown',
    };

    viewContainer.innerHTML = `
        <div class="timeline-root fade-in" style="position:relative; display:flex; flex-direction:column; max-width:960px; margin:0 auto; padding: 2rem 1rem 1rem;">
            <h3 class="section-label" style="text-align:center; margin-bottom:0.5rem;">River of Etymon</h3>
            <p style="text-align:center; font-size:0.8rem; opacity:0.5; margin-bottom:1.5rem;">Grouped by language of origin · Chronological order</p>

            <!-- 検索バー -->
            <div style="margin-bottom:2rem; position:sticky; top:0; z-index:30; background:var(--color-bg); padding:0.75rem 0;">
                <input id="timeline-search" type="text" placeholder="🔍 Search words in timeline..."
                    style="width:100%; padding:0.75rem 1.2rem; border-radius:100px; border:1.5px solid var(--color-border); background:var(--color-surface); color:var(--color-text); font-size:0.95rem; outline:none; transition:border-color 0.2s;"
                    oninput="window._tlSearch(this.value)" />
            </div>

            <div style="display:flex; gap:1.5rem; align-items:flex-start;">
                <!-- タイムライン本体 -->
                <div id="timeline-scroll-area" style="flex:1; min-width:0;">
                    <div class="timeline-thread" style="position:relative; border-left: 2px solid var(--color-border); padding-left: 2.5rem; margin-left: 1rem;">
                        ${sortedLangs.map(lang => `
                            <div class="era-group" id="${langToId(lang)}" data-era="${lang}" style="margin-bottom: 4rem;">
                                <h4 style="font-size:1.25rem; color:var(--color-premium); margin-bottom: 1.5rem; position:relative; display:flex; align-items:center; gap:0.5rem;">
                                    <span style="position:absolute; left: calc(-2.5rem - 11px); top: 50%; transform:translateY(-50%); width:20px; height:20px; background:var(--color-bg); border-radius:50%; border:4px solid var(--color-premium);"></span>
                                    ${LANG_LABEL[lang] || lang}
                                    <span style="font-size:0.7rem; font-weight:400; opacity:0.5; margin-left:0.5rem;">${allGroups[lang].length} words</span>
                                </h4>
                                <div class="era-entries">
                                ${allGroups[lang].map(w => `
                                    <div class="timeline-entry"
                                        data-word="${w.word.toLowerCase()}"
                                        data-meaning="${(w.meaning || '').toLowerCase()}"
                                        onclick="State.todayWord=(typeof WORDS !== 'undefined') ? WORDS.find(x=>x.id==='${w.id}') : null;navigate('today')"
                                        style="position:relative; margin-bottom:1.2rem; cursor:pointer; padding:0.9rem 1.2rem; border:1px solid var(--color-border); border-radius:14px; background:var(--color-surface); transition:all 0.2s ease;">
                                        <div style="position:absolute; left: calc(-2.5rem - 8px); top: 16px; width:12px; height:12px; background:var(--color-accent); border-radius:50%; border:3px solid var(--color-bg);"></div>
                                        <div style="display:flex; align-items:baseline; gap:0.6rem; flex-wrap:wrap;">
                                            <h2 style="font-size:1.2rem; color:var(--color-accent);">${w.word}</h2>
                                            ${w.era ? `<span style="font-size:0.7rem; opacity:0.45; font-style:italic;">${w.era}</span>` : ''}
                                        </div>
                                        <p style="opacity:0.7; font-size:0.85rem; margin-top:0.2rem;">${w.meaning || ''}</p>
                                    </div>
                                `).join('')}
                                </div>
                            </div>
                        `).join('')}
                    </div>
                    <p id="tl-no-results" style="display:none; text-align:center; padding:4rem; opacity:0.5;">No words matched your search.</p>
                </div>

                <!-- 右サイドバー: 言語ナビゲーター -->
                <div id="era-nav" style="
                    position: sticky;
                    top: 100px;
                    width: 140px;
                    flex-shrink: 0;
                    max-height: calc(100vh - 140px);
                    overflow-y: auto;
                    scrollbar-width: none;
                    padding: 0.5rem 0;
                    border-left: 2px solid var(--color-border);
                    padding-left: 0.75rem;
                ">
                    <p style="font-size:0.62rem; text-transform:uppercase; letter-spacing:0.08em; opacity:0.4; margin-bottom:0.5rem;">Jump to Language</p>
                    ${sortedLangs.map(lang => `
                        <button onclick="document.getElementById('${langToId(lang)}').scrollIntoView({behavior:'smooth', block:'start'})"
                            id="nav-${langToId(lang)}"
                            class="era-nav-item"
                            style="display:block; width:100%; text-align:left; background:none; border:none; color:var(--color-text-dim); font-size:0.7rem; padding:0.3rem 0.4rem; margin-bottom:0.1rem; cursor:pointer; border-radius:6px; line-height:1.4; transition:all 0.15s; white-space:normal; word-break:break-word;">
                            ${LANG_LABEL[lang] || lang}
                        </button>
                    `).join('')}
                </div>
            </div>
        </div>
    `;

    // ホバースタイル
    viewContainer.querySelectorAll('.timeline-entry').forEach(el => {
        el.addEventListener('mouseenter', () => { el.style.borderColor = 'var(--color-accent)'; el.style.transform = 'translateX(3px)'; });
        el.addEventListener('mouseleave', () => { el.style.borderColor = 'var(--color-border)'; el.style.transform = ''; });
    });

    // IntersectionObserver でサイドバーハイライト
    const eraGroups = viewContainer.querySelectorAll('.era-group');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            const lang = entry.target.dataset.era;
            const navBtn = document.getElementById(`nav-${langToId(lang)}`);
            if (!navBtn) return;
            if (entry.isIntersecting) {
                navBtn.style.color = 'var(--color-accent)';
                navBtn.style.fontWeight = '700';
                navBtn.style.background = 'rgba(59,130,246,0.08)';
            } else {
                navBtn.style.color = 'var(--color-text-dim)';
                navBtn.style.fontWeight = '';
                navBtn.style.background = '';
            }
        });
    }, { rootMargin: '-15% 0px -55% 0px' });
    eraGroups.forEach(el => observer.observe(el));

    // 検索機能
    window._tlSearch = (query) => {
        const q = query.trim().toLowerCase();
        let anyVisible = false;
        eraGroups.forEach(eraGroup => {
            const entries = eraGroup.querySelectorAll('.timeline-entry');
            let eraHasMatch = false;
            entries.forEach(entry => {
                const word = entry.dataset.word || '';
                const meaning = entry.dataset.meaning || '';
                const match = !q || word.includes(q) || meaning.includes(q);
                entry.style.display = match ? '' : 'none';
                if (match) eraHasMatch = true;
            });
            eraGroup.style.display = eraHasMatch ? '' : 'none';
            const navBtn = document.getElementById(`nav-${langToId(eraGroup.dataset.era)}`);
            if (navBtn) navBtn.style.opacity = eraHasMatch ? '1' : '0.3';
            if (eraHasMatch) anyVisible = true;
        });
        const noResults = document.getElementById('tl-no-results');
        if (noResults) noResults.style.display = anyVisible ? 'none' : 'block';
    };
}





// --- Flourish トグル ---
async function toggleFlourish(targetType, targetId, btn, targetAuthor = null) {
    if (!State.currentUser) { showToast('ログインが必要です'); return; }
    const res = await apiPost('/api/flourish', {
        username: State.currentUser, target_type: targetType, target_id: targetId, target_author: targetAuthor
    });
    if (res.status === 'success') {
        const cnt = document.getElementById(`fl-cnt-${targetType}-${targetId}`);
        if (cnt) cnt.textContent = res.count;
        if (res.action === 'added') {
            btn.style.borderColor = 'var(--color-premium)';
            btn.style.color = 'var(--color-premium)';
            btn.dataset.flourished = 'true';
        } else {
            btn.style.borderColor = 'var(--color-border)';
            btn.style.color = 'var(--color-text-dim)';
            btn.dataset.flourished = 'false';
        }
    }
}

// --- リッチトースト ---
function showRichToast(title, sub) {
    const old = document.getElementById('rich-toast');
    if (old) old.remove();
    const el = document.createElement('div');
    el.id = 'rich-toast';
    el.innerHTML = `
        <div style="font-weight:700; font-size:1rem; margin-bottom:0.25rem;">${title}</div>
        <div style="font-size:0.82rem; opacity:0.8;">${sub}</div>
    `;
    Object.assign(el.style, {
        position: 'fixed', bottom: '2.5rem', left: '50%', transform: 'translateX(-50%) translateY(20px)',
        background: 'var(--color-primary)', color: 'white',
        padding: '1rem 2rem', borderRadius: '16px',
        boxShadow: '0 8px 32px rgba(0,0,0,0.3)',
        textAlign: 'center', zIndex: '2000',
        opacity: '0', transition: 'all 0.4s cubic-bezier(0.4,0,0.2,1)',
        border: '1px solid rgba(245,158,11,0.3)',
        minWidth: '260px'
    });
    document.body.appendChild(el);
    setTimeout(() => { el.style.opacity = '1'; el.style.transform = 'translateX(-50%) translateY(0)'; }, 20);
    setTimeout(() => { el.style.opacity = '0'; el.style.transform = 'translateX(-50%) translateY(10px)'; setTimeout(() => el.remove(), 400); }, 3500);
}

function showToast(msg) {

    const container = document.getElementById('toast-container');
    const t = document.createElement('div');
    t.className = 'toast'; t.textContent = msg; container.appendChild(t);
    setTimeout(() => { t.style.opacity = '1'; t.style.transform = 'translateY(0)'; }, 10);
    setTimeout(() => { t.style.opacity = '0'; setTimeout(() => t.remove(), 300); }, 3000);
}

function searchToArchive(term) {
    State.searchFilter = term.toLowerCase();
    State.letterFilter = null;
    navigate('archive');
}

function downloadWordCard(id) {
    const word = WORDS.find(w => w.id === id);
    if (!word) return;

    // 非表示のオフスクリーンキャンバスで描画
    const canvas = document.createElement('canvas');
    canvas.width = 1200;
    canvas.height = 630;
    const ctx = canvas.getContext('2d');

    // 背景
    const gradient = ctx.createLinearGradient(0, 0, 1200, 630);
    gradient.addColorStop(0, '#030712');
    gradient.addColorStop(1, '#0f172a');
    ctx.fillStyle = gradient;
    ctx.fillRect(0, 0, 1200, 630);

    // 装飾
    ctx.strokeStyle = '#60a5fa';
    ctx.lineWidth = 2;
    ctx.strokeRect(40, 40, 1120, 550);
    ctx.globalAlpha = 0.1;
    ctx.beginPath();
    ctx.arc(1100, 100, 200, 0, Math.PI * 2);
    ctx.fillStyle = '#60a5fa';
    ctx.fill();
    ctx.globalAlpha = 1.0;

    // --- テキスト折り返し用ヘルパー ---
    // 指定幅(maxWidth)でテキストを折り返し、複数行描画して、書き終わりのY座標を返す
    function wrapText(context, text, x, y, maxWidth, lineHeight) {
        if (!text) return y;
        const words = text.split(' ');
        let line = '';
        let currentY = y;

        for (let n = 0; n < words.length; n++) {
            const testLine = line + words[n] + ' ';
            const metrics = context.measureText(testLine);
            const testWidth = metrics.width;
            if (testWidth > maxWidth && n > 0) {
                context.fillText(line, x, currentY);
                line = words[n] + ' ';
                currentY += lineHeight;
            } else {
                line = testLine;
            }
        }
        context.fillText(line, x, currentY);
        return currentY + lineHeight;
    }

    // 日本語/英語混在対応の1文字ずつ折り返す版 (主に意味や余韻用)
    function wrapTextChar(context, text, x, y, maxWidth, lineHeight) {
        if (!text) return y;
        let line = '';
        let currentY = y;

        for (let n = 0; n < text.length; n++) {
            const testLine = line + text[n];
            const metrics = context.measureText(testLine);
            const testWidth = metrics.width;
            if (testWidth > maxWidth && n > 0) {
                context.fillText(line, x, currentY);
                line = text[n];
                currentY += lineHeight;
            } else {
                line = testLine;
            }
        }
        context.fillText(line, x, currentY);
        return currentY + lineHeight;
    }

    // ヘッダーテキスト
    ctx.fillStyle = '#60a5fa';
    ctx.font = 'bold 30px "Inter"';
    ctx.fillText('ling-ling-etymon', 80, 100);

    const maxWidth = 1040; // 1200 - 80*2
    let currentY = 220;

    // 見出し (Word)
    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 100px "Inter"';
    currentY = wrapText(ctx, word.word, 80, currentY, maxWidth, 110);

    // 品詞
    currentY += 10;
    ctx.fillStyle = '#60a5fa';
    ctx.font = 'italic 36px "Inter"';
    ctx.fillText(word.part_of_speech || '', 80, currentY);
    currentY += 70;

    // 意味 (Meaning)
    ctx.fillStyle = '#f1f5f9';
    ctx.font = '500 48px "Noto Sans JP", sans-serif';
    currentY = wrapTextChar(ctx, word.meaning || '', 80, currentY, maxWidth, 64);

    // 余韻 (Resonance)
    currentY += 30; // 隙間
    ctx.fillStyle = 'rgba(241, 245, 249, 0.6)';
    ctx.font = 'italic 32px "Times New Roman"';
    const resonance = word.aftertaste || '';
    wrapTextChar(ctx, resonance, 80, currentY, maxWidth, 44);

    // ダウンロード実行
    const link = document.createElement('a');
    link.download = `etymon_${word.word}.png`;
    link.href = canvas.toDataURL();
    link.click();
    showToast("Image Generated.");
}

function renderContribute() {
    if (!State.currentUser) { showToast('Identity required.'); navigate('premium'); return; }
    viewContainer.innerHTML = `
        <div class="contribute-view fade-in" style="max-width:640px; margin: 0 auto; padding-bottom:120px;">
            <header style="margin-bottom:3rem; display:flex; gap:1rem; align-items:center;">
                <button onclick="navigate('archive')" class="chip">← Back</button>
                <h3 class="section-label">Contribution to Archive</h3>
            </header>
            <form id="word-form" style="background:var(--color-surface); padding:3rem; border-radius:32px; border:1px solid var(--color-border);">
                <div class="input-group"><label>Word Entry</label><input type="text" id="w-word" required style="width:100%; background:var(--color-bg); border-radius:12px; border:1px solid var(--color-border); color:white; padding:1.2rem;"></div>
                <div class="input-group" style="margin-top:2rem;"><label>Etymological Structure (prefix:meaning, ...)</label><input type="text" id="w-breakdown" required style="width:100%; background:var(--color-bg); border-radius:12px; border:1px solid var(--color-border); color:white; padding:1.2rem;"></div>
                <div class="input-group" style="margin-top:2rem;"><label>Concept Essence (Japanese)</label><input type="text" id="w-concept-ja" required style="width:100%; background:var(--color-bg); border-radius:12px; border:1px solid var(--color-border); color:white; padding:1.2rem;"></div>
                <div class="input-group" style="margin-top:2rem;"><label>Detailed Thought</label><textarea id="w-thinking" rows="8" style="width:100%; background:var(--color-bg); border-radius:12px; border:1px solid var(--color-border); color:white; padding:1.5rem; font-size: 1.1rem; line-height: 1.6;"></textarea></div>
                <button type="submit" id="submit-word-btn" class="primary-btn" style="width:100%; margin-top:3rem; padding:1.5rem; font-weight:bold; font-size:1.2rem; border-radius:16px;">Publish Knowledge</button>
            </form>
        </div>`;
    document.getElementById('word-form').onsubmit = async (e) => {
        e.preventDefault();
        const btn = document.getElementById('submit-word-btn');
        if (btn) { btn.innerText = 'Publishing...'; btn.disabled = true; }

        const wordData = {
            id: document.getElementById('w-word').value.toLowerCase().trim(),
            word: document.getElementById('w-word').value.trim(),
            etymology: { breakdown: document.getElementById('w-breakdown').value.split(',').map(x => ({ text: x.split(':')[0] ? x.split(':')[0].trim() : '', meaning: x.split(':')[1] ? x.split(':')[1].trim() : '' })), original_statement: "" },
            core_concept: { en: "", ja: document.getElementById('w-concept-ja').value },
            thinking_layer: document.getElementById('w-thinking').value,
            synonyms: [], antonyms: [], aftertaste: "", deep_dive: { roots: [], points: [] }, source: "Citizen Contribution", author: State.currentUser
        };
        const res = await apiPost('/api/submit-word', { username: State.currentUser, wordData });
        if (res.status === 'success') {
            showRichToast('✦ Knowledge Added', `「${wordData.word}」が宇宙の記憶に刻まれました。`);

            // リロードせずにWORDSに追加
            if (typeof WORDS !== 'undefined') {
                WORDS.push(JSON.parse(JSON.stringify(wordData)));
            }

            document.getElementById('word-form').reset();
            setTimeout(() => {
                State.letterFilter = null;
                State.searchFilter = null;
                navigate('archive');
            }, 1200);
        } else {
            showToast(res.message || '投稿エラーが発生しました。もう一度お試しください。');
            if (btn) { btn.innerText = 'Publish Knowledge'; btn.disabled = false; }
        }
    };
}

document.addEventListener('DOMContentLoaded', async () => {
    applySettings();
    if (navItems.today) navItems.today.onclick = () => navigate('today');
    if (navItems.archive) navItems.archive.onclick = () => { State.letterFilter = null; State.searchFilter = null; navigate('archive'); };
    if (navItems.saved) navItems.saved.onclick = () => navigate('saved');
    if (navItems.essays) navItems.essays.onclick = () => navigate('essays');
    if (navItems.settings) navItems.settings.onclick = () => navigate('settings');
    if (navItems.premium) navItems.premium.onclick = () => navigate('premium');
    if (navItems.notifications) navItems.notifications.onclick = () => navigate('notifications');
    if (navItems.network) navItems.network.onclick = () => navigate('network');
    if (navItems.timeline) navItems.timeline.onclick = () => navigate('timeline');
    if (navItems.etymap) navItems.etymap.onclick = () => navigate('etymap');
    if (navItems.synthesizer) navItems.synthesizer.onclick = () => navigate('synthesizer');

    if (navItems.search) {
        navItems.search.onkeypress = (e) => {
            if (e.key === 'Enter' && e.target.value.trim()) {
                State.searchFilter = e.target.value.trim().toLowerCase();
                State.letterFilter = null;
                navigate('archive');
                e.target.value = '';
            }
        };
    }

    const params = new URLSearchParams(window.location.search);
    const sid = params.get('session_id'), user = params.get('user');
    if (sid && user) {
        const res = await fetch(`${API_BASE}/check-subscription?session_id=${sid}&user=${user}`);
        const data = await res.json();
        if (data.status === 'paid') { State.isPremium = true; localStorage.setItem('isPremium', 'true'); applySettings(); }
        window.history.replaceState({}, '', '/');
    }

    try {
        const resWords = await apiGet('/api/user-words');
        if (typeof WORDS !== 'undefined' && Array.isArray(resWords)) {
            // Add user words that aren't already in the list
            resWords.forEach(uw => {
                if (!WORDS.find(w => w.id === uw.id)) {
                    WORDS.push(uw);
                }
            });
        }
    } catch (e) { console.error("Could not load user words"); }

    if (typeof WORDS !== 'undefined' && WORDS.length) {
        if (!State.todayWord) State.todayWord = WORDS[Math.floor(Math.random() * WORDS.length)];
    }
    await loadFollows();
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

async function renderMyPosts() {
    viewContainer.innerHTML = `
        <div class="my-posts-view fade-in" style="max-width:800px; margin: 0 auto;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:2rem;">
                <h3 class="section-label">My Posts</h3>
                <button class="chip" onclick="navigate('settings')">← Back to Settings</button>
            </div>
            <div id="my-posts-list">
                <div class="loading-indicator"><div class="spinner"></div><p>Loading your contributions...</p></div>
            </div>
        </div>
    `;

    if (!State.currentUser) {
        document.getElementById('my-posts-list').innerHTML = `<p class="dimmed">ログインが必要です。</p>`;
        return;
    }

    try {
        const data = await apiGet(`/api/my-posts?username=${State.currentUser}`);
        const listEl = document.getElementById('my-posts-list');

        let html = '';

        // Words
        html += `<h4 style="margin:2rem 0 1rem 0; color:var(--color-accent); border-bottom:1px solid var(--color-border); padding-bottom:0.5rem;">Words (Contributions)</h4>`;
        if (data.words && data.words.length > 0) {
            html += data.words.map(w => `
                <div style="background:var(--color-surface); padding:1.5rem; border-radius:16px; border:1px solid var(--color-border); margin-bottom:1rem; display:flex; justify-content:space-between; align-items:center;">
                    <div>
                        <b style="font-size:1.2rem;">${w.word}</b> <span class="dimmed" style="font-size:0.9rem;">${w.date || ''}</span>
                    </div>
                    <button onclick="deleteMyPost('word', '${w.id}')" class="chip" style="border:1px solid red; color:red; background:none;">Delete</button>
                </div>
            `).join('');
        } else {
            html += `<p class="dimmed">No words contributed yet.</p>`;
        }

        // Essays
        html += `<h4 style="margin:3rem 0 1rem 0; color:var(--color-accent); border-bottom:1px solid var(--color-border); padding-bottom:0.5rem;">Essays</h4>`;
        if (data.essays && data.essays.length > 0) {
            html += data.essays.map(e => `
                <div style="background:var(--color-surface); padding:1.5rem; border-radius:16px; border:1px solid var(--color-border); margin-bottom:1rem; display:flex; justify-content:space-between; align-items:center;">
                    <div>
                        <b style="font-size:1.2rem;">${e.title}</b> <span class="dimmed" style="font-size:0.9rem;">${e.date || ''}</span>
                    </div>
                    <div style="display:flex; gap:10px;">
                        <button onclick="State.essayFilterId='${e.id}'; navigate('essays')" class="chip">View</button>
                        <button onclick="deleteMyPost('essay', '${e.id}')" class="chip" style="border:1px solid red; color:red; background:none;">Delete</button>
                    </div>
                </div>
            `).join('');
        } else {
            html += `<p class="dimmed">No essays published yet.</p>`;
        }

        // Reflections
        html += `<h4 style="margin:3rem 0 1rem 0; color:var(--color-accent); border-bottom:1px solid var(--color-border); padding-bottom:0.5rem;">Reflections</h4>`;
        if (data.reflections && data.reflections.length > 0) {
            html += data.reflections.map(r => `
                <div style="background:var(--color-surface); padding:1.5rem; border-radius:16px; border:1px solid var(--color-border); margin-bottom:1rem; display:flex; justify-content:space-between; align-items:center;">
                    <div>
                        <p style="margin-bottom:0.5rem; font-style:italic;">"${r.content}"</p>
                        <span class="dimmed" style="font-size:0.9rem;">On word ID: ${r.word_id} | ${r.date || ''}</span>
                    </div>
                    <button onclick="deleteMyPost('reflection', '${r.id}')" class="chip" style="border:1px solid red; color:red; background:none;">Delete</button>
                </div>
            `).join('');
        } else {
            html += `<p class="dimmed">No reflections written yet.</p>`;
        }

        listEl.innerHTML = html;

    } catch (err) {
        document.getElementById('my-posts-list').innerHTML = `<p style="color:red;">Failed to load posts.</p>`;
    }
}

async function deleteMyPost(type, id) {
    if (!confirm('本当に削除しますか？この操作は取り消せません。')) return;

    try {
        const res = await apiPost('/api/my-delete', { username: State.currentUser, type, id });
        if (res.status === 'success') {
            showToast('削除しました');
            renderMyPosts();
        } else {
            showToast('削除に失敗しました: ' + (res.message || ''));
        }
    } catch (e) {
        showToast('通信エラーが発生しました');
    }
}

// --- Map & Synthesizer Logic ---

function renderEtyMap() {
    viewContainer.innerHTML = `
        <div class="etymap-view fade-in" style="height: calc(100vh - 100px); display:flex; flex-direction:column; align-items:center; justify-content:center; position:relative; overflow:hidden; padding-top:2rem;">
            <div style="position:absolute; top:2rem; text-align:center; z-index:10; width:100%;">
                <h2 style="font-size:2.2rem; font-weight:300; letter-spacing:0.1em; color:var(--color-premium); text-shadow: 0 0 20px rgba(245,158,11,0.5);">Etymology Map</h2>
                <p style="opacity:0.8; font-size:0.95rem; margin-top:1rem; max-width:800px; margin-left:auto; margin-right:auto; line-height:1.6; color:var(--color-text);">
                    印欧祖語（PIE）という数千年前の共通の祖先から、言葉がどのように大陸を渡り、形を変えて現代へと至ったのか。<br>
                    この地図は、一つの「根」から枝分かれした知の系譜を可視化したものです。
                </p>
                <div style="margin-top:2rem; display:flex; gap:10px; justify-content:center; flex-wrap:wrap;" id="map-buttons">
                    <button class="chip followed active" onclick="drawMapRoute('*sed-')">*sed- (座る)</button>
                    <button class="chip" onclick="drawMapRoute('*sta-')">*sta- (立つ)</button>
                    <button class="chip" onclick="drawMapRoute('*bher-')">*bher- (運ぶ)</button>
                    <button class="chip" onclick="drawMapRoute('*spec-')">*spec- (見る)</button>
                    <button class="chip" onclick="drawMapRoute('*gen-')">*gen- (生む)</button>
                    <button class="chip" onclick="drawMapRoute('*kap-')">*kap- (掴む)</button>
                </div>
            </div>
            
            <div id="map-container" style="position:relative; width: 100%; max-width: 900px; height: 500px; margin-top: 4rem; border-radius: 20px; box-shadow: 0 0 40px rgba(0,0,0,0.4); border: 1px solid rgba(255,255,255,0.08); background: radial-gradient(circle at center, #111827 0%, #030712 100%);">
                <svg id="epic-map" viewBox="0 0 800 500" style="width:100%; height:100%;">
                    <style>
                        .map-land { fill: #1f2937; stroke: #374151; stroke-width: 1; opacity:0.6; }
                        .route-line { fill: none; stroke: var(--color-premium); stroke-width: 2.5; stroke-linecap: round; filter: drop-shadow(0 0 10px var(--color-premium)); stroke-dasharray: 2000; stroke-dashoffset: 2000; animation: traceRoute 4s forwards cubic-bezier(0.25, 0.1, 0.25, 1); }
                        .node-point { fill: #fff; filter: drop-shadow(0 0 6px #fff); opacity:0; animation: fadeNode 0.8s forwards; }
                        .node-label { fill: #e5e7eb; font-size: 14px; font-family: 'Inter', sans-serif; font-weight:300; opacity:0; animation: fadeNode 0.8s forwards; text-anchor:middle; }
                        .pulse { fill: transparent; stroke: var(--color-premium); stroke-width:1; opacity:0; animation: pulseRing 2s infinite; }
                        @keyframes traceRoute { to { stroke-dashoffset: 0; } }
                        @keyframes fadeNode { to { opacity: 1; } }
                        @keyframes pulseRing { 0% { r: 5; opacity: 1; } 100% { r: 25; opacity: 0; } }
                    </style>
                    <!-- Abstract representation of Eurasia landmass -->
                    <path class="map-land" d="M 50,200 Q 150,150 300,120 T 550,100 Q 650,80 750,120 L 780,250 Q 700,350 600,420 Q 500,450 400,380 Q 350,450 250,400 Q 150,480 50,400 Z" />
                    <g id="map-traces"></g>
                </svg>
            </div>
            
            <div id="map-info" style="position:absolute; bottom:2rem; left:2rem; background:var(--color-surface); padding:1.5rem 2rem; border-radius:16px; border:1px solid var(--color-border); max-width:400px; opacity:0; transition: opacity 0.5s; box-shadow: 0 8px 32px rgba(0,0,0,0.4);">
                <h3 id="map-info-title" style="color:var(--color-premium); margin-bottom:0.5rem; font-size:1.4rem;"></h3>
                <p id="map-info-desc" style="font-size:0.95rem; line-height:1.6; color:var(--color-text-dim);"></p>
            </div>
        </div>
    `;

    window.mapTracesData = {
        '*sed-': {
            title: "The Journey of *sed-",
            desc: "「座る」という静かな行為を意味した印欧祖語の *sed- は、ギリシャ語の hedra（大聖堂：座る場所）、ラテン語の sedere（定住する、座る）、そして古フランス語を経て、現代英語の sit や session へと繋がりました。数千年の時を越えた「静止」の旅です。",
            route: "M 600,150 Q 500,280 400,320 Q 280,300 250,220 Q 200,180 120,200",
            nodes: [
                { x: 600, y: 150, label: "Proto-Indo-European\n*sed-", delay: 0 },
                { x: 400, y: 320, label: "Ancient Greek\nhedra", delay: 1000 },
                { x: 250, y: 220, label: "Latin\nsedere", delay: 2000 },
                { x: 180, y: 195, label: "Old French\nsee", delay: 2800 },
                { x: 120, y: 200, label: "Modern English\nsit, session", delay: 3500 }
            ]
        },
        '*sta-': {
            title: "The Persistence of *sta-",
            desc: "「立つ」を意味した語根 *sta- は、最も強固な語根の一つです。ラテン語の stare やギリシャ語の histanai、そしてゲルマン語派を経て、現代英語の stand、state (状態、国家)、statue (彫像) など、揺るぎない存在を示す多くの言葉を生み出しました。",
            route: "M 580,160 Q 450,180 300,250 Q 200,150 140,180",
            nodes: [
                { x: 580, y: 160, label: "PIE\n*sta-", delay: 0 },
                { x: 450, y: 180, label: "Proto-Germanic\n*standanan", delay: 1200 },
                { x: 300, y: 250, label: "Latin\nstare", delay: 2200 },
                { x: 140, y: 180, label: "English\nstand, state", delay: 3500 }
            ]
        },
        '*bher-': {
            title: "The Burden of *bher-",
            desc: "「運ぶ」「産む（重荷を負う）」を意味するこの語根は、ギリシャ語の pherein (metaphor)、ラテン語の ferre (transfer)、そして古英語の beran へと繋がり、現代英語の bear や burden に結実しました。言葉の重みを背負って旅をした語根です。",
            route: "M 620,130 Q 520,350 420,350 Q 300,320 280,260 Q 200,160 100,210",
            nodes: [
                { x: 620, y: 130, label: "PIE\n*bher-", delay: 0 },
                { x: 420, y: 350, label: "Greek\npherein", delay: 1000 },
                { x: 280, y: 260, label: "Latin\nferre", delay: 2000 },
                { x: 100, y: 210, label: "English\nbear, burden", delay: 3500 }
            ]
        },
        '*spec-': {
            title: "The Vision of *spec-",
            desc: "「見る」を意味する語根 *spec- は、ラテン語の specere を経て、spectacle (光景)、inspect (検査する)、respect (尊敬する＝振り返って見る) など、現代英語の視覚に関わる多くの抽象概念を形作りました。",
            route: "M 590,140 Q 400,160 300,280 Q 220,240 130,220",
            nodes: [
                { x: 590, y: 140, label: "PIE\n*spec-", delay: 0 },
                { x: 300, y: 280, label: "Latin\nspecere", delay: 1500 },
                { x: 130, y: 220, label: "English\nspectacle, respect", delay: 3500 }
            ]
        },
        '*gen-': {
            title: "The Genesis of *gen-",
            desc: "「生む」「種」を意味する *gen- は、ギリシャ語の genos、ラテン語の gignere を経て、gene (遺伝子)、generation (世代)、generous (寛大な＝高貴な生まれの) といった、生命と系統に関する豊かな語群を生み出しました。",
            route: "M 610,145 Q 500,250 430,330 Q 350,300 290,240 Q 200,180 110,190",
            nodes: [
                { x: 610, y: 145, label: "PIE\n*gen-", delay: 0 },
                { x: 430, y: 330, label: "Greek\ngenos", delay: 1200 },
                { x: 290, y: 240, label: "Latin\ngignere", delay: 2400 },
                { x: 110, y: 190, label: "English\ngene, generation", delay: 3500 }
            ]
        },
        '*kap-': {
            title: "The Grasp of *kap-",
            desc: "「掴む」「取る」を意味する *kap- は、ラテン語の capere を経て、capacity (収容能力)、capture (捕獲)、accept (受け入れる) などの言葉になりました。物理的な把握から、知的な理解までをカバーする重要な語根です。",
            route: "M 605,155 Q 450,220 310,270 Q 240,220 120,240",
            nodes: [
                { x: 605, y: 155, label: "PIE\n*kap-", delay: 0 },
                { x: 310, y: 270, label: "Latin\ncapere", delay: 1800 },
                { x: 120, y: 240, label: "English\ncapacity, accept", delay: 3500 }
            ]
        }
    };

    setTimeout(() => drawMapRoute('*sed-'), 100);
}

window.drawMapRoute = function (rootKey) {
    const data = window.mapTracesData[rootKey];
    if (!data) return;

    // Update buttons
    const btns = document.getElementById('map-buttons').querySelectorAll('button');
    btns.forEach(b => {
        b.classList.remove('followed', 'active');
        b.style.borderColor = 'var(--color-border)';
        b.style.color = 'var(--color-text-dim)';
        if (b.innerText.includes(rootKey)) {
            b.classList.add('followed', 'active');
            b.style.color = 'var(--color-premium)';
            b.style.borderColor = 'var(--color-premium)';
        }
    });

    const tracesGroup = document.getElementById('map-traces');
    tracesGroup.innerHTML = '';

    // Hide info temporarily
    const infoBox = document.getElementById('map-info');
    infoBox.style.opacity = '0';

    // Draw Route Line
    const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
    path.setAttribute("class", "route-line");
    path.setAttribute("d", data.route);
    tracesGroup.appendChild(path);

    // Draw Nodes
    data.nodes.forEach(node => {
        // Point
        const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
        circle.setAttribute("cx", node.x);
        circle.setAttribute("cy", node.y);
        circle.setAttribute("r", 5);
        circle.setAttribute("class", "node-point");
        circle.style.animationDelay = (node.delay / 1000) + 's';
        tracesGroup.appendChild(circle);

        // Pulse
        const pulse = document.createElementNS("http://www.w3.org/2000/svg", "circle");
        pulse.setAttribute("cx", node.x);
        pulse.setAttribute("cy", node.y);
        pulse.setAttribute("class", "pulse");
        pulse.style.animationDelay = (node.delay / 1000) + 's';
        tracesGroup.appendChild(pulse);

        // Text
        const lines = node.label.split('\\n');
        const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
        text.setAttribute("x", node.x);
        text.setAttribute("y", node.y - 25);
        text.setAttribute("class", "node-label");
        text.style.animationDelay = (node.delay / 1000) + 's';

        lines.forEach((l, i) => {
            const tspan = document.createElementNS("http://www.w3.org/2000/svg", "tspan");
            tspan.setAttribute("x", node.x);
            tspan.setAttribute("dy", i === 0 ? 0 : 16);
            if (i === 0) tspan.style.fontWeight = "bold";
            tspan.textContent = l;
            text.appendChild(tspan);
        });
        tracesGroup.appendChild(text);
    });

    // Show info after a slight delay
    setTimeout(() => {
        document.getElementById('map-info-title').textContent = data.title;
        document.getElementById('map-info-desc').textContent = data.desc;
        infoBox.style.opacity = '1';
    }, 1500);
};

// --- Root Synthesizer ---

const SYNTH_PIECES = {
    prefixes: [
        { id: 'pre-ab', text: 'ab-', meaning: 'away (離れて)', color: '#22c55e' },
        { id: 'pre-com', text: 'com- / con-', meaning: 'together (共に)', color: '#22c55e' },
        { id: 'pre-re', text: 're-', meaning: 'back, again (後ろに、再び)', color: '#22c55e' },
        { id: 'pre-in', text: 'in-', meaning: 'into / not (中に、否定)', color: '#22c55e' },
        { id: 'pre-ex', text: 'ex-', meaning: 'out (外に)', color: '#22c55e' },
        { id: 'pre-ad', text: 'ad-', meaning: 'to, toward (〜へ、向かって)', color: '#22c55e' },
        { id: 'pre-pro', text: 'pro-', meaning: 'forward (前へ)', color: '#22c55e' },
        { id: 'pre-sub', text: 'sub-', meaning: 'under (下に)', color: '#22c55e' },
        { id: 'pre-trans', text: 'trans-', meaning: 'across (越えて)', color: '#22c55e' },
        { id: 'pre-dis', text: 'dis-', meaning: 'apart / not (離れて、否定)', color: '#22c55e' },
        { id: 'pre-per', text: 'per-', meaning: 'through (越えて、完全に)', color: '#22c55e' },
        { id: 'pre-de', text: 'de-', meaning: 'down / away (下に、離れて)', color: '#22c55e' }
    ],
    roots: [
        { id: 'root-duc', text: 'duc / duct', meaning: 'to lead (導く)', color: 'var(--color-premium)' },
        { id: 'root-tract', text: 'tract', meaning: 'to pull (引く)', color: 'var(--color-premium)' },
        { id: 'root-spect', text: 'spect', meaning: 'to look (見る)', color: 'var(--color-premium)' },
        { id: 'root-ject', text: 'ject', meaning: 'to throw (投げる)', color: 'var(--color-premium)' },
        { id: 'root-mit', text: 'mit / miss', meaning: 'to send (送る)', color: 'var(--color-premium)' },
        { id: 'root-gen', text: 'gen', meaning: 'to birth, produce (生む)', color: 'var(--color-premium)' },
        { id: 'root-cap', text: 'cap / capt', meaning: 'to take, hold (掴む)', color: 'var(--color-premium)' },
        { id: 'root-port', text: 'port', meaning: 'to carry (運ぶ)', color: 'var(--color-premium)' },
        { id: 'root-fac', text: 'fac / fic', meaning: 'to make (作る)', color: 'var(--color-premium)' },
        { id: 'root-scrib', text: 'scrib / script', meaning: 'to write (書く)', color: 'var(--color-premium)' },
        { id: 'root-ced', text: 'ced / cess', meaning: 'to go (行く)', color: 'var(--color-premium)' },
        { id: 'root-ven', text: 'ven / vent', meaning: 'to come (来る)', color: 'var(--color-premium)' },
        { id: 'root-pon', text: 'pon / posit', meaning: 'to put / place (置く)', color: 'var(--color-premium)' },
        { id: 'root-fer', text: 'fer', meaning: 'to carry / bear (運ぶ、産む)', color: 'var(--color-premium)' },
        { id: 'root-vis', text: 'vid / vis', meaning: 'to see (見る)', color: 'var(--color-premium)' },
        { id: 'root-voc', text: 'voc / vok', meaning: 'to call (呼ぶ)', color: 'var(--color-premium)' },
        { id: 'root-anthrop', text: 'anthrop', meaning: 'human (人間)', color: 'var(--color-premium)' },
        { id: 'root-bio', text: 'bio', meaning: 'life (生命)', color: 'var(--color-premium)' },
        { id: 'root-chron', text: 'chron', meaning: 'time (時間)', color: 'var(--color-premium)' },
        { id: 'root-morph', text: 'morph', meaning: 'form (形)', color: 'var(--color-premium)' },
        { id: 'root-path', text: 'path', meaning: 'feeling (感情)', color: 'var(--color-premium)' },
        { id: 'root-phil', text: 'phil', meaning: 'love (愛)', color: 'var(--color-premium)' },
        { id: 'root-phob', text: 'phob', meaning: 'fear (恐怖)', color: 'var(--color-premium)' },
        { id: 'root-poly', text: 'poly', meaning: 'many (多く)', color: 'var(--color-premium)' },
        { id: 'root-mono', text: 'mono', meaning: 'one (一つ)', color: 'var(--color-premium)' },
        { id: 'root-auto', text: 'auto', meaning: 'self (自己)', color: 'var(--color-premium)' }
    ],
    suffixes: [
        { id: 'suf-ion', text: '-ion', meaning: 'act or state (こと、状態)', color: '#ef4444' },
        { id: 'suf-tion', text: '-tion', meaning: 'act or process (行為、過程)', color: '#ef4444' },
        { id: 'suf-able', text: '-able / -ible', meaning: 'capable of (できる)', color: '#ef4444' },
        { id: 'suf-or', text: '-or / -er', meaning: 'one who does (する人)', color: '#ef4444' },
        { id: 'suf-ive', text: '-ive', meaning: 'tending to (〜の性質の)', color: '#ef4444' },
        { id: 'suf-al', text: '-al', meaning: 'relating to (〜に関する)', color: '#ef4444' },
        { id: 'suf-ous', text: '-ous', meaning: 'full of (〜に満ちた)', color: '#ef4444' },
        { id: 'suf-ment', text: '-ment', meaning: 'action or result (行為、結果)', color: '#ef4444' },
        { id: 'suf-ate', text: '-ate', meaning: 'to cause or be (〜にする)', color: '#ef4444' },
        { id: 'suf-ence', text: '-ence / -ance', meaning: 'state or quality (状態、性質)', color: '#ef4444' },
        { id: 'suf-logy', text: '-logy', meaning: 'study of (学問)', color: '#ef4444' },
        { id: 'suf-phobia', text: '-phobia', meaning: 'fear of (恐怖)', color: '#ef4444' },
        { id: 'suf-philia', text: '-philia', meaning: 'love of (愛)', color: '#ef4444' },
        { id: 'suf-ism', text: '-ism', meaning: 'belief / practice (主義、慣行)', color: '#ef4444' },
        { id: 'suf-ist', text: '-ist', meaning: 'one who does (〜する人)', color: '#ef4444' },
        { id: 'suf-ize', text: '-ize', meaning: 'to make (〜化する)', color: '#ef4444' },
        { id: 'suf-ic', text: '-ic', meaning: 'relating to (〜に関する)', color: '#ef4444' },
        { id: 'suf-ity', text: '-ity', meaning: 'state or quality (性質、状態)', color: '#ef4444' },
        { id: 'suf-ness', text: '-ness', meaning: 'state of being (〜である状態)', color: '#ef4444' },
        { id: 'suf-ful', text: '-ful', meaning: 'full of (〜に満ちた)', color: '#ef4444' },
        { id: 'suf-less', text: '-less', meaning: 'without (〜なしの)', color: '#ef4444' },
        { id: 'suf-ly', text: '-ly', meaning: 'in the manner of (〜のように)', color: '#ef4444' }
    ]
};

window.synthState = { prefix: null, root: null, suffix1: null, suffix2: null, suffix3: null };

function renderSynthesizer() {
    window.synthState = { prefix: null, root1: null, root2: null, suffix1: null, suffix2: null, suffix3: null };

    const renderPiece = (p, type) => {
        return `<div class="synth-piece" draggable="true" data-id="${p.id}" data-type="${type}" data-text="${p.text}" data-mean="${p.meaning}" data-color="${p.color}" 
            style="background:var(--color-bg); border:1px solid ${p.color}; color:${p.color}; padding:0.6rem 1rem; border-radius:8px; cursor:grab; text-align:center; user-select:none; font-weight:bold; box-shadow:0 2px 8px rgba(0,0,0,0.2);">
                <span style="font-size:1.1rem;">${p.text}</span>
                <span style="display:block; font-size:0.7rem; font-weight:normal; opacity:0.8; margin-top:4px;">${p.meaning}</span>
            </div>`;
    };

    viewContainer.innerHTML = `
        <div class="synth-view fade-in" style="min-height: calc(100vh - 100px); padding: 2rem; display:flex; flex-direction:column; align-items:center;">
            <div style="text-align:center; margin-bottom:3rem;">
                <h2 style="font-size:2.5rem; font-weight:300; letter-spacing:0.1em; color:var(--color-premium); text-shadow: 0 0 20px rgba(245,158,11,0.5);">Root Synthesizer</h2>
                <p style="opacity:0.6; font-size:1rem; margin-top:0.5rem; font-style:italic;">The alchemy of words. Combine morphemes to distill meaning.</p>
            </div>
            
            <div style="display:flex; gap:2rem; width:100%; max-width:1100px; flex-wrap:wrap; justify-content:center;">
                <!-- Arsenal -->
                <div style="flex:1 1 300px; background:var(--color-surface); padding:1.5rem; border-radius:24px; border:1px solid var(--color-border); box-shadow: 0 8px 32px rgba(0,0,0,0.3);">
                    <h3 style="font-size:1rem; margin-bottom:1rem; padding-bottom:0.5rem; border-bottom:1px solid rgba(255,255,255,0.1); color:#22c55e;">Prefixes</h3>
                    <div id="synth-prefixes" class="piece-container" style="display:flex; flex-wrap:wrap; gap:10px; margin-bottom:1.5rem;">
                        ${SYNTH_PIECES.prefixes.map(p => renderPiece(p, 'prefix')).join('')}
                    </div>
                    
                    <h3 style="font-size:1rem; margin-bottom:1rem; padding-bottom:0.5rem; border-bottom:1px solid rgba(255,255,255,0.1); color:var(--color-premium);">Roots</h3>
                    <div id="synth-roots" class="piece-container" style="display:flex; flex-wrap:wrap; gap:10px; margin-bottom:1.5rem;">
                        ${SYNTH_PIECES.roots.map(p => renderPiece(p, 'root')).join('')}
                    </div>
                    
                    <h3 style="font-size:1rem; margin-bottom:1rem; padding-bottom:0.5rem; border-bottom:1px solid rgba(255,255,255,0.1); color:#ef4444;">Suffixes</h3>
                    <div id="synth-suffixes" class="piece-container" style="display:flex; flex-wrap:wrap; gap:10px;">
                        ${SYNTH_PIECES.suffixes.map(p => renderPiece(p, 'suffix')).join('')}
                    </div>
                </div>
                
                <!-- Alchemy Table -->
                <div style="flex:1.5 1 500px; display:flex; flex-direction:column; align-items:center; position:relative;">
                    
                    <div style="background:var(--color-surface); padding:2rem 1.5rem; border-radius:24px; border:1px solid var(--color-border); box-shadow: 0 12px 40px rgba(0,0,0,0.5); width:100%; background-image: radial-gradient(circle at center, rgba(245,158,11,0.08) 0%, transparent 60%);">
                        <div style="display:flex; justify-content:center; align-items:center; gap:1.5%; margin-bottom:1rem;">
                            <div class="drop-zone" data-type="prefix" style="width:18%; aspect-ratio:1/1; max-height:110px; border:2px dashed #22c55e; border-radius:16px; display:flex; flex-direction:column; align-items:center; justify-content:center; transition:all 0.3s; position:relative; background:rgba(34,197,94,0.05);">
                                <span style="opacity:0.4; font-size:0.75rem; text-align:center;">Prefix<br>(Opt)</span>
                            </div>
                            <div style="font-size:1.5rem; opacity:0.3; font-weight:300;">+</div>
                            <div class="drop-zone" data-type="root" data-slot="1" style="width:18%; aspect-ratio:1/1; max-height:110px; border:2px dashed var(--color-premium); border-radius:16px; display:flex; flex-direction:column; align-items:center; justify-content:center; transition:all 0.3s; position:relative; background:rgba(245,158,11,0.05);">
                                <span style="opacity:0.4; font-size:0.75rem; text-align:center;">Root 1<br>(Req)</span>
                            </div>
                            <div style="font-size:1.5rem; opacity:0.3; font-weight:300;">+</div>
                            <div class="drop-zone" data-type="root" data-slot="2" style="width:18%; aspect-ratio:1/1; max-height:110px; border:2px dashed var(--color-premium); border-radius:16px; display:flex; flex-direction:column; align-items:center; justify-content:center; transition:all 0.3s; position:relative; background:rgba(245,158,11,0.05);">
                                <span style="opacity:0.4; font-size:0.75rem; text-align:center;">Root 2<br>(Opt)</span>
                            </div>
                        </div>
                        <div style="display:flex; justify-content:center; align-items:center; gap:1.5%;">
                            <div class="drop-zone" data-type="suffix" data-slot="1" style="width:18%; aspect-ratio:1/1; max-height:110px; border:2px dashed #ef4444; border-radius:16px; display:flex; flex-direction:column; align-items:center; justify-content:center; transition:all 0.3s; position:relative; background:rgba(239,68,68,0.05);">
                                <span style="opacity:0.4; font-size:0.75rem; text-align:center;">Suffix 1<br>(Opt)</span>
                            </div>
                            <div style="font-size:1.5rem; opacity:0.3; font-weight:300;">+</div>
                            <div class="drop-zone" data-type="suffix" data-slot="2" style="width:18%; aspect-ratio:1/1; max-height:110px; border:2px dashed #ef4444; border-radius:16px; display:flex; flex-direction:column; align-items:center; justify-content:center; transition:all 0.3s; position:relative; background:rgba(239,68,68,0.05);">
                                <span style="opacity:0.4; font-size:0.75rem; text-align:center;">Suffix 2<br>(Opt)</span>
                            </div>
                            <div style="font-size:1.5rem; opacity:0.3; font-weight:300;">+</div>
                            <div class="drop-zone" data-type="suffix" data-slot="3" style="width:18%; aspect-ratio:1/1; max-height:110px; border:2px dashed #ef4444; border-radius:16px; display:flex; flex-direction:column; align-items:center; justify-content:center; transition:all 0.3s; position:relative; background:rgba(239,68,68,0.05);">
                                <span style="opacity:0.4; font-size:0.75rem; text-align:center;">Suffix 3<br>(Opt)</span>
                            </div>
                        </div>
                    </div>
                    
                    <div style="margin-top:2rem;">
                        <button class="primary-btn" onclick="executeSynthesis()" style="padding:1.2rem 4rem; font-size:1.3rem; font-weight:bold; letter-spacing:0.05em; border-radius:50px; box-shadow: 0 0 20px rgba(96,165,250,0.4); text-transform:uppercase;">Transmute</button>
                    </div>
                    
                    <div id="synth-result" style="margin-top:2.5rem; width:100%; text-align:center; padding:2rem; border-radius:16px; background:rgba(255,255,255,0.02); opacity:0; transition:opacity 0.5s; border:1px solid rgba(255,255,255,0.05); box-shadow:0 10px 30px rgba(0,0,0,0.2);">
                    </div>
                    <canvas id="synth-fx" style="position:absolute; top:0; left:0; width:100%; height:100%; pointer-events:none; z-index:20;"></canvas>
                </div>
            </div>
        </div>
        `;

    setTimeout(setupDragAndDrop, 100);
}

function setupDragAndDrop() {
    const pieces = document.querySelectorAll('.synth-piece');
    const zones = document.querySelectorAll('.drop-zone');

    pieces.forEach(p => {
        p.addEventListener('dragstart', (e) => {
            e.dataTransfer.setData('text/plain', JSON.stringify({
                id: p.dataset.id,
                type: p.dataset.type,
                text: p.dataset.text,
                mean: p.dataset.mean,
                color: p.dataset.color
            }));
            p.style.opacity = '0.5';
        });
        p.addEventListener('dragend', () => {
            p.style.opacity = '1';
        });
    });

    zones.forEach(z => {
        z.addEventListener('dragover', (e) => {
            e.preventDefault();
            z.style.background = 'rgba(255,255,255,0.1)';
        });
        z.addEventListener('dragleave', () => {
            z.style.background = ''; // revert
        });
        z.addEventListener('drop', (e) => {
            e.preventDefault();
            z.style.background = '';
            try {
                const data = JSON.parse(e.dataTransfer.getData('text/plain'));
                const zoneType = z.dataset.type;
                // Allow suffix into suffix slots, root into root slots, prefix into prefix slot
                if (zoneType === data.type || (zoneType === 'suffix' && data.type === 'suffix') || (zoneType === 'prefix' && data.type === 'prefix')) {
                    const slot = z.dataset.slot;
                    const stateKey = slot ? (zoneType + slot) : zoneType;
                    window.synthState[stateKey] = data;

                    // Update visual in drop zone
                    z.innerHTML = `
                        <div style="color:${data.color}; font-size:1rem; font-weight:bold; margin-bottom:5px; text-align:center;">${data.text}</div>
                        <div style="color:var(--color-text-dim); font-size:0.65rem; text-align:center; line-height:1.2;">${data.mean}</div>
                        <button onclick="clearSynthSlot('${zoneType}', ${slot || 'null'})" style="position:absolute; top:5px; right:5px; background:none; border:none; color:rgba(255,255,255,0.5); cursor:pointer;">✕</button>
                    `;
                    z.style.borderStyle = 'solid';
                } else {
                    showToast('Incorrect piece type for this slot.');
                }
            } catch (e) { }
        });
    });
}

window.clearSynthSlot = function (type, slot) {
    const stateKey = slot ? (type + slot) : type;
    window.synthState[stateKey] = null;
    const selector = slot ? `.drop-zone[data-type="${type}"][data-slot="${slot}"]` : `.drop-zone[data-type="${type}"]`;
    const z = document.querySelector(selector);

    let label = "Drop Piece";
    if (type === 'prefix') label = "Prefix<br>(Opt)";
    if (type === 'root') label = slot == 1 ? "Root 1<br>(Req)" : "Root 2<br>(Opt)";
    if (type === 'suffix') label = `Suffix ${slot || ''}<br>(Opt)`;

    z.innerHTML = `<span style="opacity:0.4; font-size:0.75rem; text-align:center;">${label}</span>`;
    z.style.borderStyle = 'dashed';
};

// --- Fuzzy matching helper ---
function synthLevenshtein(a, b) {
    const m = a.length, n = b.length;
    const dp = Array.from({ length: m + 1 }, (_, i) => Array(n + 1).fill(0));
    for (let i = 0; i <= m; i++) dp[i][0] = i;
    for (let j = 0; j <= n; j++) dp[0][j] = j;
    for (let i = 1; i <= m; i++)
        for (let j = 1; j <= n; j++)
            dp[i][j] = Math.min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + (a[i - 1] !== b[j - 1] ? 1 : 0));
    return dp[m][n];
}

function findSimilarWords(variants, parts) {
    if (typeof WORDS === 'undefined') return [];

    // Extract all possible text variations for each part (e.g. "com- / con-" -> ["com", "con"])
    const partExtracts = parts.map(p => {
        return p.text.replace(/-/g, '').toLowerCase().split('/').map(s => s.trim()).filter(Boolean);
    });

    const scored = [];

    for (const w of WORDS) {
        const wl = (w.word || '').toLowerCase();
        if (!wl || wl.length < 3) continue;

        // Component matching score
        let componentScore = 0;
        let matchedPartsCount = 0;

        for (const options of partExtracts) {
            let matched = false;
            for (const opt of options) {
                if (opt.length >= 2 && wl.includes(opt)) {
                    matched = true;
                    // Bonus if it matches at boundaries
                    if (wl.startsWith(opt) || wl.endsWith(opt)) {
                        componentScore += 5;
                    } else {
                        componentScore += 3;
                    }
                    break;
                }
            }
            if (matched) matchedPartsCount++;
        }

        // Levenshtein distance against the BEST variant
        let maxSimilarity = 0;
        for (const v of variants) {
            const dist = synthLevenshtein(v, wl);
            const maxLen = Math.max(v.length, wl.length);
            const similarity = 1 - (dist / maxLen);
            if (similarity > maxSimilarity) maxSimilarity = similarity;
        }

        // Skip if largely irrelevant
        if (matchedPartsCount === 0 && maxSimilarity < 0.6) continue;

        // Combined score weighting
        let totalScore = componentScore * 2 + maxSimilarity * 30;
        if (matchedPartsCount === parts.length && parts.length > 0) totalScore += 50; // Huge bonus for containing all parts
        else if (matchedPartsCount > 0) totalScore += matchedPartsCount * 5;

        if (componentScore >= 1 || maxSimilarity >= 0.5) {
            scored.push({ word: w.word, id: w.id, score: totalScore, componentScore, similarity: maxSimilarity });
        }
    }

    // Sort descending by calculated relevance score
    scored.sort((a, b) => b.score - a.score);
    return scored.slice(0, 10);
}

// --- Phonetic variation generator ---
function generatePhoneticVariants(pre, r1, r2, suf1, suf2, suf3) {
    const variants = new Set();
    const rootPart = r1 + r2;
    const suffPart = suf1 + suf2 + suf3;
    const base = pre + rootPart + suffPart;
    variants.add(base);

    // Prefix assimilation rules
    const prefixRules = [
        // in- assimilation
        [/^in([mbp])/, 'im$1'],
        [/^in([l])/, 'il$1'],
        [/^in([r])/, 'ir$1'],

        // con- / com- assimilation
        [/^con([mbp])/, 'com$1'],
        [/^con([l])/, 'col$1'],
        [/^con([r])/, 'cor$1'],
        [/^con([aeiouhw])/, 'co$1'],
        [/^com([l])/, 'col$1'],
        [/^com([r])/, 'cor$1'],
        [/^com([aeiouhw])/, 'co$1'],

        // ad- assimilation (ac, af, ag, al, an, ap, ar, as, at)
        [/^ad([cfglpnqrst])/, 'a$1$1'],

        // sub- assimilation (suc, suf, sug, sup, sur, sum)
        [/^sub([cfmpgr])/, 'su$1$1'],

        // ob- assimilation (oc, of, op)
        [/^ob([cfp])/, 'o$1$1'],

        // ex- assimilation
        [/^ex([f])/, 'ef$1'],
        [/^ex([bdgjmnrv])/, 'e$1'],

        // dis- assimilation
        [/^dis([f])/, 'dif$1'],
        [/^dis([bdglmnrv])/, 'di$1']
    ];

    for (const [regex, replacement] of prefixRules) {
        if (regex.test(base)) {
            variants.add(base.replace(regex, replacement));
        }
    }

    // Suffix joining variations (e.g., vis + ible = visible, not visible)
    // Remove duplicate vowels at junction points
    if (rootPart && suffPart) {
        const lastRoot = rootPart[rootPart.length - 1];
        const firstSuf = suffPart[0];
        // If root ends with same letter suffix starts with, deduplicate
        if (lastRoot === firstSuf) {
            variants.add(pre + rootPart + suffPart.slice(1));
        }
        // e-drop: if root ends with 'e' and suffix starts with vowel
        if (lastRoot === 'e' && 'aeiou'.includes(firstSuf)) {
            variants.add(pre + rootPart.slice(0, -1) + suffPart);
        }
    }

    // -able / -ible alternation
    for (const v of [...variants]) {
        if (v.includes('able')) variants.add(v.replace('able', 'ible'));
        if (v.includes('ible')) variants.add(v.replace('ible', 'able'));
        // -tion / -sion alternation
        if (v.includes('tion')) variants.add(v.replace('tion', 'sion'));
        if (v.includes('sion')) variants.add(v.replace('sion', 'tion'));
        // -ence / -ance alternation
        if (v.includes('ence')) variants.add(v.replace('ence', 'ance'));
        if (v.includes('ance')) variants.add(v.replace('ance', 'ence'));
        // -or / -er alternation
        if (v.endsWith('or')) variants.add(v.slice(0, -2) + 'er');
        if (v.endsWith('er')) variants.add(v.slice(0, -2) + 'or');
        // Double consonant before suffix (e.g., transmit + ion = transmission)
        if (rootPart && suffPart && 'bcdfgklmnprst'.includes(rootPart[rootPart.length - 1])) {
            variants.add(pre + rootPart + rootPart[rootPart.length - 1] + suffPart);
        }
        // Remove trailing 't' before '-ion' (e.g., duct + ion = duction not duction)
        if (rootPart.endsWith('t') && suffPart.startsWith('ion')) {
            variants.add(pre + rootPart.slice(0, -1) + suffPart);
        }
    }

    return [...variants].map(v => v.toLowerCase());
}

window.executeSynthesis = function () {
    const s = window.synthState;
    if (!s.root1 && !s.root2 && !s.prefix && !s.suffix1 && !s.suffix2 && !s.suffix3) {
        showToast("錬成する要素を配置してください。");
        return;
    }

    const cleanText = (piece) => {
        if (!piece) return '';
        return piece.text.split('/')[0].trim().replace(/^-|-$/g, '').replace(/\s+/g, '');
    };

    const pre = cleanText(s.prefix);
    const r1 = cleanText(s.root1);
    const r2 = cleanText(s.root2);
    const sf1 = cleanText(s.suffix1);
    const sf2 = cleanText(s.suffix2);
    const sf3 = cleanText(s.suffix3);

    // Generate all phonetic variants
    const variants = generatePhoneticVariants(pre, r1, r2, sf1, sf2, sf3);
    const primaryCombined = variants[0]; // The raw combination

    const resultBox = document.getElementById('synth-result');
    playSynthFx();

    setTimeout(() => {
        const parts = [s.prefix, s.root1, s.root2, s.suffix1, s.suffix2, s.suffix3].filter(Boolean);
        const meaningStrJa = parts.map(x => {
            const m = x.mean;
            const match = m.match(/（(.*?)）/);
            return match ? match[1] : m;
        }).join(' + ');

        // Check all variants against WORDS and local dictionary
        let matchedWord = null;
        let matchedVariant = null;

        // Build word lookup
        const wordMap = {};
        if (typeof WORDS !== 'undefined') {
            WORDS.forEach(w => { if (w.word) wordMap[w.word.toLowerCase()] = w; });
        }

        for (const v of variants) {
            if (wordMap[v]) {
                matchedWord = wordMap[v];
                matchedVariant = v;
                break;
            }
        }

        let html = '';
        if (matchedWord) {
            html = `
                <div style="color:var(--color-premium); font-size:1.2rem; font-weight:bold; margin-bottom:10px;">✨ Alignment Reached (真理への到達) ✨</div>
                <h3 style="font-size:2.8rem; margin:10px 0; color:#fff; letter-spacing:1px; text-transform:capitalize;">${matchedWord.word}</h3>
                <p style="font-size:1rem; opacity:0.8; margin-bottom:15px; font-style:italic;">"${meaningStrJa}"</p>
                ${matchedVariant !== primaryCombined ? `<p style="font-size:0.85rem; opacity:0.5; margin-bottom:10px;">音韻変化: ${primaryCombined} → ${matchedVariant}</p>` : ''}
                <div style="background:rgba(255,255,255,0.05); padding:1rem; border-radius:12px; display:inline-block; text-align:left; max-width:500px;">
                    <span style="color:var(--color-accent); font-weight:bold;">Discovery Unlocked.</span> この単語は実在します！
                    <br><br>
                    <button class="chip" onclick="searchToArchive('${matchedWord.word.toLowerCase()}')">アーカイブで詳細を見る →</button>
                </div>
            `;
        } else {
            // Find similar existing words comparing against all variants
            const similar = findSimilarWords(variants, parts);

            const pred = parts.map(x => {
                const m = x.mean;
                const match = m.match(/（(.*?)）/);
                return match ? match[1] : m;
            }).join(' + ');

            let similarHtml = '';
            if (similar.length > 0) {
                similarHtml = `
                    <div style="margin-top:1.5rem; padding-top:1.5rem; border-top:1px solid rgba(255,255,255,0.1);">
                        <div style="color:var(--color-accent); font-weight:bold; margin-bottom:0.8rem; font-size:0.95rem;">🔍 同じパーツを含む実在する単語:</div>
                        <div style="display:flex; flex-wrap:wrap; gap:8px; justify-content:center;">
                            ${similar.map(sw => `
                                <button class="chip" onclick="searchToArchive('${sw.word.toLowerCase()}')" style="border:1px solid var(--color-premium); color:var(--color-premium); background:rgba(245,158,11,0.1); font-size:0.9rem;">
                                    ${sw.word}
                                </button>
                            `).join('')}
                        </div>
                    </div>
                `;
            }

            html = `
                <div style="color:var(--color-text-dim); font-size:1.2rem; font-weight:bold; margin-bottom:10px;">🌀 Hypothetical Construct (仮説的構成) 🌀</div>
                <h3 style="font-size:2.8rem; margin:10px 0; color:var(--color-text-dim); letter-spacing:1px; text-transform:capitalize;">*${primaryCombined}</h3>
                <p style="font-size:1rem; opacity:0.8; margin-bottom:8px; font-style:italic;">"${meaningStrJa}"</p>
                ${variants.length > 1 ? `<p style="font-size:0.8rem; opacity:0.4; margin-bottom:15px;">検索した変化形: ${variants.slice(0, 5).join(', ')}${variants.length > 5 ? '...' : ''}</p>` : ''}
                <div style="background:rgba(255,255,255,0.05); padding:1rem; border-radius:12px; display:inline-block; text-align:left; max-width:500px; color:rgba(255,255,255,0.7);">
                    この単語は一般的ではありませんが、語源的には成立します。<br>
                    予測される意味: <b>「${pred}」</b>
                </div>
                ${similarHtml}
            `;
        }

        resultBox.innerHTML = html;
        resultBox.style.opacity = '1';
    }, 500);
};

function playSynthFx() {
    const canvas = document.getElementById('synth-fx');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    canvas.width = canvas.offsetWidth;
    canvas.height = canvas.offsetHeight;

    let particles = [];
    const centerX = canvas.width / 2;
    const centerY = canvas.height * 0.4; // roughly around drop zones

    for (let i = 0; i < 60; i++) {
        particles.push({
            x: centerX, y: centerY,
            vx: (Math.random() - 0.5) * 15, vy: (Math.random() - 0.5) * 15,
            life: 1.0, size: Math.random() * 4 + 2,
            color: Math.random() > 0.5 ? '#f59e0b' : '#3b82f6'
        });
    }

    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        let alive = false;
        particles.forEach(p => {
            p.x += p.vx; p.y += p.vy;
            p.life -= 0.02;
            if (p.life > 0) {
                alive = true;
                ctx.globalAlpha = p.life;
                ctx.fillStyle = p.color;
                ctx.beginPath(); ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2); ctx.fill();
            }
        });
        if (alive) requestAnimationFrame(animate);
    }
    animate();
}
