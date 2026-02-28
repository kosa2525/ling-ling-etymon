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
    premium: document.getElementById('nav-premium'),
    notifications: document.getElementById('nav-notifications')
};

// Global cache for dynamically loaded content
window.ESSAY_CACHE = [];

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
                <div class="word-options-container" style="position:absolute; top:0; right:0;">
                    <button id="word-options-trigger" style="background:none; border:none; font-size:1.8rem; cursor:pointer; color:var(--color-text-dim); padding:0.5rem;">⋯</button>
                    <div id="word-options-menu" style="display:none; position:absolute; top:40px; right:0; background:var(--color-surface); border:1px solid var(--color-border); border-radius:12px; box-shadow:0 10px 30px rgba(0,0,0,0.3); z-index:100; min-width:160px; overflow:hidden;">
                        <button onclick="toggleSaveWord('${word.id}')" style="width:100%; padding:1rem; background:none; border:none; color:white; text-align:left; cursor:pointer; font-size:0.9rem; border-bottom:1px solid var(--color-border);">
                            ${State.savedWordIds.includes(word.id) ? '🔖 Unsave' : '📑 Save Word'}
                        </button>
                        <button onclick="hideItem('word', '${word.id}')" style="width:100%; padding:1rem; background:none; border:none; color:white; text-align:left; cursor:pointer; font-size:0.9rem;">
                            👁️‍🗨️ Hide this Word
                        </button>
                    </div>
                </div>
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

    if (State.isPremium) loadReflections(word.id);
    document.querySelectorAll('.morpheme-link').forEach(l => l.onclick = () => { if (!State.isPremium) return navigate('premium'); State.searchFilter = l.dataset.term; navigate('archive'); });

    const trigger = document.getElementById('word-options-trigger');
    const menu = document.getElementById('word-options-menu');
    if (trigger && menu) {
        trigger.onclick = (e) => { e.stopPropagation(); menu.style.display = menu.style.display === 'block' ? 'none' : 'block'; };
        document.addEventListener('click', () => { menu.style.display = 'none'; }, { once: true });
    }
}

function toggleSaveWord(id) {
    const idx = State.savedWordIds.indexOf(id);
    if (idx > -1) State.savedWordIds.splice(idx, 1);
    else State.savedWordIds.push(id);
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
    const data = await apiGet(`/api/reflections/${targetId}?username=${State.currentUser || ''}`);
    listEl.innerHTML = data.map(r => `
        <div style="border-bottom: 1px solid rgba(255,255,255,0.05); padding: 2rem 0;">
            <div style="display:flex; justify-content:space-between; font-size:0.9rem; margin-bottom:1rem; opacity:0.8;">
                <div><b>${r.username}</b> <span class="dimmed">${r.date}</span></div>
                <div class="ugc-actions" style="display:flex; gap:10px;">
                    <button onclick="reportItem('reflection', ${r.id}, '${r.username}')" title="通報" style="background:none; border:none; cursor:pointer; opacity:0.5;">🚩</button>
                    ${r.username !== State.currentUser ? `
                        <button onclick="blockUser('${r.username}')" title="ブロック" style="background:none; border:none; cursor:pointer; opacity:0.5;">🚫</button>
                    ` : ''}
                    <button onclick="hideItem('reflection', ${r.id})" title="非表示" style="background:none; border:none; cursor:pointer; opacity:0.5;">👁️‍🗨️</button>
                    ${State.isOperator ? `
                        <button onclick="adminDeleteContent('reflection', ${r.id})" title="削除 (Admin)" style="background:none; border:none; cursor:pointer; opacity:0.5; color:red;">🗑️</button>
                    ` : ''}
                </div>
            </div>
            <p style="font-size:1.1rem; line-height: 1.7; margin-bottom: 1.5rem;">${r.content}</p>
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
    await apiPost('/api/follow', { follower: State.currentUser, followed: targetUser });
    showToast(`Followed ${targetUser}`);
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
    let list = (typeof WORDS !== 'undefined') ? [...WORDS] : [];
    list.sort((a, b) => a.word.localeCompare(b.word));

    // 非表示フィルタの適用
    if (localStorage.getItem('hiddenWords')) {
        const hiddenIds = JSON.parse(localStorage.getItem('hiddenWords'));
        list = list.filter(w => !hiddenIds.includes(w.id));
    }

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

async function renderEssays() {
    const officialEssays = (typeof ESSAYS !== 'undefined') ? [...ESSAYS] : [];
    const userEssays = await apiGet('/api/user-essays');
    const allEssays = [...officialEssays, ...userEssays];
    allEssays.sort((a, b) => b.date.localeCompare(a.date));
    window.ESSAY_CACHE = allEssays; // キャッシュに保存

    // 非表示フィルタの適用
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
                        <span class="dimmed" style="font-size:0.9rem;">${e.date}</span>
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
                <button type="submit" class="primary-btn" style="width:100%; margin-top:3rem; padding:1.5rem; font-weight:bold; font-size:1.2rem; border-radius:16px;">Publish Essay</button>
            </form>
        </div>`;
    document.getElementById('essay-form').onsubmit = async (e) => {
        e.preventDefault();
        const res = await apiPost('/api/submit-essay', {
            username: State.currentUser,
            title: document.getElementById('e-title').value,
            content: document.getElementById('e-content').value
        });
        if (res.status === 'success') { showToast('Essay Published.'); navigate('essays'); }
        else showToast(res.message);
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
                        ${e.author && e.author !== State.currentUser && e.author !== 'etymon_official' ? `<button onclick="followUser('${e.author}')" class="chip" style="font-size:0.7rem;">Follow</button>` : ''}
                    </div>
                </div>
                <h1 style="font-size:3.5rem; margin:1.5rem 0; line-height:1.1; letter-spacing:-0.03em;">${e.title}</h1>
            </header>
            <div class="essay-body" style="font-size:1.3rem; line-height:2; color:var(--color-text); font-family: 'Inter', sans-serif;">
                ${e.content.split('\n').map(l => l.trim() ? `<p style="margin-bottom:2.5rem;">${l}</p>` : '').join('')}
            </div>
            <footer style="margin-top: 4rem; padding-top: 1.5rem; border-top: 1px solid var(--color-border); opacity:0.4; font-size:0.75rem; font-style:italic;">
                ※ 本エッセイは、一部AIによって生成された、またはAIの補助を受けて作成された可能性があります。
            </footer>
            ${renderReflectionSection(e.id)}
        </div>`;
    loadReflections(e.id);

    const trigger = document.getElementById('essay-options-trigger');
    const menu = document.getElementById('essay-options-menu');
    if (trigger && menu) {
        trigger.onclick = (ev) => { ev.stopPropagation(); menu.style.display = menu.style.display === 'block' ? 'none' : 'block'; };
        document.addEventListener('click', () => { menu.style.display = 'none'; }, { once: true });
    }
}

function toggleSaveEssay(id) {
    const idx = State.savedEssayIds.indexOf(id);
    if (idx > -1) State.savedEssayIds.splice(idx, 1);
    else State.savedEssayIds.push(id);
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
                    ${State.currentUser ? `
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
        if (res.status === 'success') { if (mode === 'register') { showToast('Success. Please login.'); mode = 'login'; setupAuthListeners(); } else { State.currentUser = username; State.isPremium = res.is_premium; State.isOperator = res.is_operator; localStorage.setItem('currentUser', username); localStorage.setItem('isPremium', res.is_premium); localStorage.setItem('isOperator', res.is_operator); applySettings(); navigate('today'); } }
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
            case 'admin': renderAdmin(); break;
            case 'connections': renderConnections(); break;
            case 'notifications': renderNotifications(); break;
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
    if (navItems.notifications) navItems.notifications.onclick = () => navigate('notifications');

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
