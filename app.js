/**
 * Logika Simulasi CAT CPNS (Pembaruan Multi-Instansi)
 * Mendukung SKD Nasional (110 Soal) dan SKB Spesifik Instansi (Kemenkeu, BSSN, Kemkomdigi, BKN, Kumham, Pemda)
 */

(function () {
  // Key Penyimpanan LocalStorage & SessionStorage
  const STORAGE_KEY_SESSION = 'cpns_cat_active_session';
  const STORAGE_KEY_HISTORY = 'cpns_cat_history';
  const STORAGE_KEY_CUSTOM_QUESTIONS = 'cpns_cat_custom_questions';
  const STORAGE_KEY_PIN_HASH = 'cpns_cat_pin_hash';
  const STORAGE_KEY_GATE_UNLOCKED = 'cpns_cat_gate_unlocked';
  const DEFAULT_PIN_HASH = '514196786f4e4';

  // State Aplikasi
  const state = {
    packetKey: 'skd',
    packetData: null,
    activeQuestions: [], // Daftar soal yang sedang diujikan (bisa hasil shuffle)
    currentIndex: 0,
    answers: {},         // { [questionId]: 'A' | 'B' | ... }
    doubts: new Set(),   // Set of questionId
    timerSeconds: 0,
    timerId: null,
    startTime: null,
    mode: 'simulasi',    // 'simulasi' | 'belajar'
    reviewFilter: 'all', // 'all' | 'wrong' | 'correct' | 'doubt'
    reviewSearchQuery: '',
    fontSize: 16
  };

  // Cache DOM Elements
  const el = {
    // Topbar Controls
    fontSizeDec: document.getElementById('btn-font-dec'),
    fontSizeReset: document.getElementById('btn-font-reset'),
    fontSizeInc: document.getElementById('btn-font-inc'),
    btnFullscreen: document.getElementById('btn-fullscreen'),
    btnThemeToggle: document.getElementById('btn-theme-toggle'),
    timerContainer: document.getElementById('timer-container'),
    timerDisplay: document.getElementById('timer-display'),
    examTitle: document.getElementById('exam-title'),

    // Screens & Banners
    resumeBanner: document.getElementById('resume-banner'),
    resumeInfoText: document.getElementById('resume-info-text'),
    btnResumeSession: document.getElementById('btn-resume-session'),
    btnDiscardSession: document.getElementById('btn-discard-session'),
    screenWelcome: document.getElementById('screen-welcome'),
    screenExam: document.getElementById('screen-exam'),
    screenResult: document.getElementById('screen-result'),

    // Tabs
    tabBtns: document.querySelectorAll('.tab-btn'),
    tabContents: document.querySelectorAll('.tab-content'),

    // Category Switcher (SKD vs SKB)
    btnCatSkd: document.getElementById('btn-cat-skd'),
    btnCatSkb: document.getElementById('btn-cat-skb'),
    viewCatSkd: document.getElementById('view-cat-skd'),
    viewCatSkb: document.getElementById('view-cat-skb'),

    // Packet & Instansi Selection
    packetCards: document.querySelectorAll('.packet-card'),
    instansiCards: document.querySelectorAll('.instansi-card'),
    modeCards: document.querySelectorAll('.mode-card'),
    modeCardSimulasi: document.getElementById('mode-card-simulasi'),
    modeCardBelajar: document.getElementById('mode-card-belajar'),
    rulesBoxTitle: document.getElementById('rules-box-title'),
    rulesBoxList: document.getElementById('rules-box-list'),
    optShuffleQuestions: document.getElementById('opt-shuffle-questions'),
    optShuffleOptions: document.getElementById('opt-shuffle-options'),
    btnStart: document.getElementById('btn-start'),

    // Study Mode Feedback Elements
    studyExpCard: document.getElementById('study-explanation-card'),
    studyExpContent: document.getElementById('study-explanation-content'),
    studyCorrectBadge: document.getElementById('study-correct-badge'),
    legendItemAnswered: document.getElementById('legend-item-answered'),
    legendLabelAnswered: document.getElementById('legend-label-answered'),
    legendItemWrong: document.getElementById('legend-item-wrong'),
    legendItemDoubt: document.getElementById('legend-item-doubt'),

    // Tab 2 (Riwayat & Statistik)
    statTotalExams: document.getElementById('stat-total-exams'),
    statAvgScore: document.getElementById('stat-avg-score'),
    statPassRate: document.getElementById('stat-pass-rate'),
    statHighestScore: document.getElementById('stat-highest-score'),
    historyTableBody: document.getElementById('history-table-body'),
    btnClearHistory: document.getElementById('btn-clear-history'),

    // Tab 3 (Kelola Bank Soal)
    bankSummaryList: document.getElementById('bank-summary-list'),
    btnOpenAddModal: document.getElementById('btn-open-add-modal'),
    btnExportJson: document.getElementById('btn-export-json'),
    inputImportJson: document.getElementById('input-import-json'),

    // Exam View
    qIndexBadge: document.getElementById('q-index-badge'),
    qInstansiTag: document.getElementById('q-instansi-tag'),
    qCategoryTag: document.getElementById('q-category-tag'),
    qSubcategoryTag: document.getElementById('q-subcategory-tag'),
    qText: document.getElementById('q-text'),
    optionsContainer: document.getElementById('options-container'),
    btnPrev: document.getElementById('btn-prev'),
    btnNext: document.getElementById('btn-next'),
    btnDoubt: document.getElementById('btn-doubt'),
    btnFinish: document.getElementById('btn-finish'),
    btnAbortSession: document.getElementById('btn-abort-session'),
    quickJumpContainer: document.getElementById('quick-jump-container'),
    jumpTwk: document.getElementById('jump-twk'),
    jumpTiu: document.getElementById('jump-tiu'),
    jumpTkp: document.getElementById('jump-tkp'),
    questionGrid: document.getElementById('question-grid'),

    // Mobile Bottom Bar & Bottom Sheet Drawer
    mobileExamBar: document.getElementById('mobile-exam-bar'),
    mobileBtnPrev: document.getElementById('mobile-btn-prev'),
    mobileBtnNext: document.getElementById('mobile-btn-next'),
    mobileBtnSheet: document.getElementById('mobile-btn-sheet'),
    mobileSheetProgress: document.getElementById('mobile-sheet-progress'),
    navSidebar: document.getElementById('nav-sidebar'),
    navSidebarBackdrop: document.getElementById('nav-sidebar-backdrop'),
    btnCloseSidebar: document.getElementById('btn-close-sidebar'),

    // Modal Selesai
    modalFinish: document.getElementById('modal-finish'),
    btnModalCancel: document.getElementById('btn-modal-cancel'),
    btnModalConfirm: document.getElementById('btn-modal-confirm'),
    recapAnswered: document.getElementById('recap-answered'),
    recapDoubt: document.getElementById('recap-doubt'),
    recapUnanswered: document.getElementById('recap-unanswered'),

    // Modal Hentikan Sesi
    modalAbort: document.getElementById('modal-abort'),
    btnModalAbortCancel: document.getElementById('btn-modal-abort-cancel'),
    btnModalAbortConfirm: document.getElementById('btn-modal-abort-confirm'),

    // Modal Tambah Soal
    modalAddQuestion: document.getElementById('modal-add-question'),
    formAddQuestion: document.getElementById('form-add-question'),
    btnCancelAddQ: document.getElementById('btn-cancel-add-q'),
    inputTargetPacket: document.getElementById('input-target-packet'),
    inputCategory: document.getElementById('input-category'),
    inputSubcategory: document.getElementById('input-subcategory'),
    inputQuestionText: document.getElementById('input-question-text'),
    inputOptA: document.getElementById('input-opt-a'),
    inputOptB: document.getElementById('input-opt-b'),
    inputOptC: document.getElementById('input-opt-c'),
    inputOptD: document.getElementById('input-opt-d'),
    inputOptE: document.getElementById('input-opt-e'),
    sectionAnswerStandard: document.getElementById('section-answer-standard'),
    sectionAnswerTkp: document.getElementById('section-answer-tkp'),
    inputCorrectOpt: document.getElementById('input-correct-opt'),
    tkpPtsA: document.getElementById('tkp-pts-a'),
    tkpPtsB: document.getElementById('tkp-pts-b'),
    tkpPtsC: document.getElementById('tkp-pts-c'),
    tkpPtsD: document.getElementById('tkp-pts-d'),
    tkpPtsE: document.getElementById('tkp-pts-e'),
    inputExplanation: document.getElementById('input-explanation'),

    // Result View
    resultContainer: document.getElementById('result-container'),

    // Security Gate & DevTools Protection Elements
    gateLockOverlay: document.getElementById('gate-lock-overlay'),
    formGatePin: document.getElementById('form-gate-pin'),
    inputGatePin: document.getElementById('input-gate-pin'),
    btnToggleGatePwd: document.getElementById('btn-toggle-gate-pwd'),
    gatePinError: document.getElementById('gate-pin-error'),
    btnLockSession: document.getElementById('btn-lock-session'),
    devtoolsLockOverlay: document.getElementById('devtools-lock-overlay'),
    formDevtoolsUnlock: document.getElementById('form-devtools-unlock'),
    inputDevtoolsPin: document.getElementById('input-devtools-pin'),
    devtoolsPinError: document.getElementById('devtools-pin-error'),
    securityToastContainer: document.getElementById('security-toast-container'),
    inputCustomPin: document.getElementById('input-custom-pin'),
    btnSaveCustomPin: document.getElementById('btn-save-custom-pin'),
    pinChangeStatus: document.getElementById('pin-change-status')
  };

  // ==========================================
  // INISIALISASI
  // ==========================================
  function init() {
    loadCustomQuestionsIntoBank();
    protectBankSoal(window.BANK_SOAL);
    setupThemeToggle();
    setupAccessibilityControls();
    setupTabNavigation();
    setupCategoryAndInstansiSelection();
    setupExamActionHandlers();
    setupAddQuestionModal();
    setupImportExport();
    setupSecuritySystem();

    renderHistoryDashboard();
    renderBankSummary();
    checkSavedSession();
  }

  // ==========================================
  // ENKRIPSI & PROTEKSI BANK SOAL RUNTIME
  // ==========================================
  const SEC_SALT = 0x5a;

  function obfuscateStr(str) {
    if (!str && str !== 0) return '';
    try {
      const bytes = new TextEncoder().encode(String(str));
      let binary = '';
      for (let i = 0; i < bytes.length; i++) {
        binary += String.fromCharCode(bytes[i] ^ (SEC_SALT + (i % 7)));
      }
      return btoa(binary);
    } catch (e) {
      return btoa(unescape(encodeURIComponent(String(str))));
    }
  }

  function deobfuscateStr(encoded) {
    if (!encoded) return '';
    try {
      const binary = atob(encoded);
      const bytes = new Uint8Array(binary.length);
      for (let i = 0; i < binary.length; i++) {
        bytes[i] = binary.charCodeAt(i) ^ (SEC_SALT + (i % 7));
      }
      return new TextDecoder().decode(bytes);
    } catch (e) {
      try {
        return decodeURIComponent(escape(atob(encoded)));
      } catch (err) {
        return encoded;
      }
    }
  }

  function getQuestionAnswer(q) {
    if (!q) return '';
    if (q._secAns) return deobfuscateStr(q._secAns);
    return q.answer || '';
  }

  function setQuestionAnswer(q, newAns) {
    if (!q) return;
    if (q._secAns || !q.answer) {
      q._secAns = obfuscateStr(newAns);
      delete q.answer;
    } else {
      q.answer = newAns;
    }
  }

  function getQuestionExplanation(q) {
    if (!q) return '';
    if (q._secExp) return deobfuscateStr(q._secExp);
    return q.explanation || '';
  }

  function getQuestionPoints(q) {
    if (!q) return null;
    if (q._secPts) {
      try {
        return JSON.parse(deobfuscateStr(q._secPts));
      } catch (e) {
        return null;
      }
    }
    return q.points || null;
  }

  function setQuestionPoints(q, newPts) {
    if (!q) return;
    if (q._secPts || !q.points) {
      q._secPts = obfuscateStr(JSON.stringify(newPts));
      delete q.points;
    } else {
      q.points = newPts;
    }
  }

  function protectBankSoal(bankSoal) {
    if (!bankSoal) return;
    try {
      Object.keys(bankSoal).forEach((pktKey) => {
        const pkt = bankSoal[pktKey];
        if (pkt && Array.isArray(pkt.questions)) {
          pkt.questions.forEach((q) => {
            if (q.answer && !q._secAns) {
              q._secAns = obfuscateStr(q.answer);
              delete q.answer;
            }
            if (q.explanation && !q._secExp) {
              q._secExp = obfuscateStr(q.explanation);
              delete q.explanation;
            }
            if (q.points && !q._secPts) {
              q._secPts = obfuscateStr(JSON.stringify(q.points));
              delete q.points;
            }
          });
        }
      });
    } catch (err) {
      console.warn('Bank soal security note:', err);
    }
  }

  // ==========================================
  // SISTEM KEAMANAN: PIN GATE, ANTI-F12 & DEVTOOLS TRAP
  // ==========================================
  let isDevToolsLocked = false;
  let adminDevToolsBypass = false;

  // Hashing Salted untuk Verifikasi PIN (PIN tidak pernah disimpan dalam plain-text)
  function hashPinSync(pin) {
    const salt = 'CPNS_CAT_BKN_SEC_2026_';
    let h1 = 0xdeadbeef, h2 = 0x41c6ce57;
    const str = salt + String(pin || '').trim();
    for (let i = 0; i < str.length; i++) {
      const ch = str.charCodeAt(i);
      h1 = Math.imul(h1 ^ ch, 2654435761);
      h2 = Math.imul(h2 ^ ch, 1597334677);
    }
    h1 = Math.imul(h1 ^ (h1 >>> 16), 2246822507) ^ Math.imul(h2 ^ (h2 >>> 13), 3266489909);
    h2 = Math.imul(h2 ^ (h2 >>> 16), 2246822507) ^ Math.imul(h1 ^ (h1 >>> 13), 3266489909);
    return (4294967296 * (2097151 & h2) + (h1 >>> 0)).toString(16);
  }

  function isPinValid(inputPin) {
    if (!inputPin) return false;
    const inputHash = hashPinSync(inputPin);
    const storedHash = localStorage.getItem(STORAGE_KEY_PIN_HASH) || DEFAULT_PIN_HASH;
    return inputHash === storedHash;
  }

  function showSecurityToast(msg, type = 'warning') {
    if (!el.securityToastContainer) return;
    const toast = document.createElement('div');
    toast.className = `security-toast toast-${type}`;
    let icon = '🔒';
    if (type === 'danger') icon = '🚨';
    if (type === 'success') icon = '✓';
    toast.innerHTML = `<span style="font-size:1.1rem;">${icon}</span> <span>${msg}</span>`;
    el.securityToastContainer.appendChild(toast);
    setTimeout(() => {
      if (toast.parentNode) toast.remove();
    }, 4000);
  }

  function triggerDevToolsLock(reason = '') {
    if (isDevToolsLocked || adminDevToolsBypass) return;
    isDevToolsLocked = true;
    if (el.devtoolsLockOverlay) {
      el.devtoolsLockOverlay.style.display = 'flex';
      if (el.inputDevtoolsPin) {
        el.inputDevtoolsPin.value = '';
        el.inputDevtoolsPin.focus();
      }
      if (el.devtoolsPinError) {
        el.devtoolsPinError.style.display = 'none';
      }
    }
  }



  function setupSecuritySystem() {
    // 1. Inisialisasi Gate PIN Akses Portal
    const isUnlocked = sessionStorage.getItem(STORAGE_KEY_GATE_UNLOCKED) === 'true';
    if (!isUnlocked && el.gateLockOverlay) {
      el.gateLockOverlay.style.display = 'flex';
      if (el.inputGatePin) {
        setTimeout(() => el.inputGatePin.focus(), 200);
      }
    } else if (el.gateLockOverlay) {
      el.gateLockOverlay.style.display = 'none';
    }

    // Submit PIN Masuk
    if (el.formGatePin) {
      el.formGatePin.addEventListener('submit', (e) => {
        e.preventDefault();
        const inputPin = el.inputGatePin ? el.inputGatePin.value.trim() : '';

        if (isPinValid(inputPin)) {
          sessionStorage.setItem(STORAGE_KEY_GATE_UNLOCKED, 'true');

          el.gateLockOverlay.style.display = 'none';
          if (el.gatePinError) el.gatePinError.style.display = 'none';
          if (el.inputGatePin) el.inputGatePin.value = '';
          showSecurityToast('Akses Berhasil Dibuka! Selamat Berlatih.', 'success');
        } else {
          if (el.gatePinError) el.gatePinError.style.display = 'block';
          if (el.inputGatePin) el.inputGatePin.select();
        }
      });
    }

    // Toggle Lihat/Sembunyikan PIN di Gate
    if (el.btnToggleGatePwd && el.inputGatePin) {
      el.btnToggleGatePwd.addEventListener('click', () => {
        const isPwd = el.inputGatePin.type === 'password';
        el.inputGatePin.type = isPwd ? 'text' : 'password';
        el.btnToggleGatePwd.textContent = isPwd ? '🙈' : '👁️';
      });
    }

    // Tombol Kunci Sesi Cepat di Topbar
    if (el.btnLockSession) {
      el.btnLockSession.addEventListener('click', () => {
        sessionStorage.removeItem(STORAGE_KEY_GATE_UNLOCKED);
        if (el.gateLockOverlay) {
          el.gateLockOverlay.style.display = 'flex';
          if (el.inputGatePin) {
            el.inputGatePin.value = '';
            el.inputGatePin.focus();
          }
          if (el.gatePinError) el.gatePinError.style.display = 'none';
        }
        showSecurityToast('Sesi simulasi berhasil dikunci.', 'warning');
      });
    }

    // 2. Proteksi DevTools / F12 Trap
    window.addEventListener('keydown', (e) => {
      // F12
      if (e.key === 'F12' || e.keyCode === 123) {
        e.preventDefault();
        e.stopPropagation();
        showSecurityToast('Tombol F12 (DevTools) dinonaktifkan.', 'danger');
        triggerDevToolsLock('Shortcut F12 ditekan');
        return false;
      }
      // Ctrl+Shift+I / Ctrl+Shift+J / Ctrl+Shift+C
      if (e.ctrlKey && e.shiftKey && (e.key === 'I' || e.key === 'i' || e.key === 'J' || e.key === 'j' || e.key === 'C' || e.key === 'c')) {
        e.preventDefault();
        e.stopPropagation();
        showSecurityToast('Akses Inspect Element dinonaktifkan.', 'danger');
        triggerDevToolsLock('Shortcut Inspect Element ditekan');
        return false;
      }
      // Ctrl+U (View Source)
      if (e.ctrlKey && (e.key === 'U' || e.key === 'u')) {
        e.preventDefault();
        e.stopPropagation();
        showSecurityToast('Akses Page Source dinonaktifkan.', 'danger');
        return false;
      }
      // Ctrl+S (Save Page)
      if (e.ctrlKey && (e.key === 'S' || e.key === 's')) {
        e.preventDefault();
        e.stopPropagation();
        showSecurityToast('Penyimpanan halaman dinonaktifkan.', 'warning');
        return false;
      }
    }, true);

    // Context Menu (Klik Kanan)
    document.addEventListener('contextmenu', (e) => {
      e.preventDefault();
      showSecurityToast('Menu klik kanan dinonaktifkan demi integritas CAT BKN.', 'warning');
      return false;
    });

    // Anti-Copy pada teks soal
    document.addEventListener('copy', (e) => {
      if (document.body.classList.contains('in-exam')) {
        e.preventDefault();
        showSecurityToast('Teks soal dilindungi dari penyalinan (Anti-Copy).', 'warning');
      }
    });

    // Deteksi Pembukaan Jendela DevTools (Docked Window Delta)
    function checkDevToolsDocked() {
      if (isDevToolsLocked || adminDevToolsBypass) return;
      const widthDelta = window.outerWidth - window.innerWidth;
      const heightDelta = window.outerHeight - window.innerHeight;
      if (widthDelta > 160 || heightDelta > 160) {
        triggerDevToolsLock('Jendela DevTools terbuka');
      }
    }
    window.addEventListener('resize', checkDevToolsDocked);
    setInterval(checkDevToolsDocked, 2500);

    // Form Unlock DevTools Lock
    if (el.formDevtoolsUnlock) {
      el.formDevtoolsUnlock.addEventListener('submit', (e) => {
        e.preventDefault();
        const pin = el.inputDevtoolsPin ? el.inputDevtoolsPin.value.trim() : '';
        if (isPinValid(pin)) {
          adminDevToolsBypass = true;
          isDevToolsLocked = false;
          if (el.devtoolsLockOverlay) el.devtoolsLockOverlay.style.display = 'none';
          showSecurityToast('Override DevTools berhasil diizinkan oleh Admin.', 'success');
        } else {
          if (el.devtoolsPinError) el.devtoolsPinError.style.display = 'block';
        }
      });
    }

    // 3. Manajemen Ganti PIN di Tab 3
    if (el.inputCustomPin) {
      el.inputCustomPin.value = '';
    }
    if (el.btnSaveCustomPin && el.inputCustomPin) {
      el.btnSaveCustomPin.addEventListener('click', () => {
        const newPin = el.inputCustomPin.value.trim();
        if (!newPin || newPin.length < 4) {
          if (el.pinChangeStatus) {
            el.pinChangeStatus.style.display = 'block';
            el.pinChangeStatus.style.background = 'rgba(239, 68, 68, 0.15)';
            el.pinChangeStatus.style.color = '#ef4444';
            el.pinChangeStatus.textContent = '⚠️ PIN minimal terdiri dari 4 karakter.';
          }
          return;
        }

        localStorage.setItem(STORAGE_KEY_PIN_HASH, hashPinSync(newPin));
        el.inputCustomPin.value = '';
        if (el.pinChangeStatus) {
          el.pinChangeStatus.style.display = 'block';
          el.pinChangeStatus.style.background = 'rgba(16, 185, 129, 0.15)';
          el.pinChangeStatus.style.color = '#10b981';
          el.pinChangeStatus.textContent = '✓ PIN Akses Portal berhasil diperbarui dan dienkripsi!';
        }
        showSecurityToast('PIN Akses Portal berhasil diperbarui!', 'success');
      });
    }
  }

  // ==========================================
  // FITUR TEMA GELAP / TERANG (DARK MODE)
  // ==========================================
  const STORAGE_KEY_THEME = 'cpns_cat_theme';

  function setupThemeToggle() {
    const savedTheme = localStorage.getItem(STORAGE_KEY_THEME);
    const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
    const initialTheme = savedTheme || (prefersDark ? 'dark' : 'light');

    applyTheme(initialTheme);

    if (el.btnThemeToggle) {
      el.btnThemeToggle.addEventListener('click', () => {
        const isCurrentDark = document.documentElement.getAttribute('data-theme') === 'dark';
        const newTheme = isCurrentDark ? 'light' : 'dark';
        applyTheme(newTheme);
        localStorage.setItem(STORAGE_KEY_THEME, newTheme);
      });
    }
  }

  function applyTheme(theme) {
    if (theme === 'dark') {
      document.documentElement.setAttribute('data-theme', 'dark');
      if (el.btnThemeToggle) {
        el.btnThemeToggle.innerHTML = '☀️ Terang';
        el.btnThemeToggle.title = 'Ganti ke Mode Terang';
      }
    } else {
      document.documentElement.removeAttribute('data-theme');
      if (el.btnThemeToggle) {
        el.btnThemeToggle.innerHTML = '🌙 Gelap';
        el.btnThemeToggle.title = 'Ganti ke Mode Gelap';
      }
    }
  }

  // ==========================================
  // FITUR AKSESIBILITAS & TAMPILAN
  // ==========================================
  function setupAccessibilityControls() {
    el.fontSizeInc.addEventListener('click', () => {
      if (state.fontSize < 24) {
        state.fontSize += 2;
        document.documentElement.style.setProperty('--font-base-size', `${state.fontSize}px`);
      }
    });

    el.fontSizeDec.addEventListener('click', () => {
      if (state.fontSize > 13) {
        state.fontSize -= 2;
        document.documentElement.style.setProperty('--font-base-size', `${state.fontSize}px`);
      }
    });

    el.fontSizeReset.addEventListener('click', () => {
      state.fontSize = 16;
      document.documentElement.style.setProperty('--font-base-size', '16px');
    });

    el.btnFullscreen.addEventListener('click', () => {
      if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch((err) => {
          console.warn('Gagal masuk mode fullscreen:', err);
        });
      } else {
        document.exitFullscreen().catch((err) => {
          console.warn('Gagal keluar mode fullscreen:', err);
        });
      }
    });
  }

  // ==========================================
  // SISTEM TAB DASHBOARD
  // ==========================================
  function setupTabNavigation() {
    el.tabBtns.forEach((btn) => {
      btn.addEventListener('click', () => {
        el.tabBtns.forEach((b) => b.classList.remove('active'));
        el.tabContents.forEach((c) => c.classList.remove('active'));

        btn.classList.add('active');
        const targetId = btn.dataset.tab;
        const targetContent = document.getElementById(targetId);
        if (targetContent) targetContent.classList.add('active');

        if (targetId === 'tab-history') renderHistoryDashboard();
        if (targetId === 'tab-manage') renderBankSummary();
      });
    });
  }

  // ==========================================
  // PEMILIHAN KATEGORI & INSTANSI
  // ==========================================
  function setupCategoryAndInstansiSelection() {
    // Toggle SKD vs SKB
    el.btnCatSkd.addEventListener('click', () => {
      el.btnCatSkd.classList.add('active');
      el.btnCatSkb.classList.remove('active');
      el.viewCatSkd.style.display = 'block';
      el.viewCatSkb.style.display = 'none';
      state.packetKey = 'skd';
    });

    el.btnCatSkb.addEventListener('click', () => {
      el.btnCatSkb.classList.add('active');
      el.btnCatSkd.classList.remove('active');
      el.viewCatSkd.style.display = 'none';
      el.viewCatSkb.style.display = 'block';

      // Pastikan ada instansi yang terpilih default
      let selectedInstansi = document.querySelector('.instansi-card.selected');
      if (!selectedInstansi) {
        selectedInstansi = el.instansiCards[0];
        if (selectedInstansi) selectedInstansi.classList.add('selected');
      }
      if (selectedInstansi) state.packetKey = selectedInstansi.dataset.packet;
    });

    // Pilihan Kartu SKD
    el.packetCards.forEach((card) => {
      card.addEventListener('click', () => {
        el.packetCards.forEach((c) => c.classList.remove('selected'));
        card.classList.add('selected');
        state.packetKey = card.dataset.packet;
      });
    });

    // Pilihan Kartu Instansi SKB
    el.instansiCards.forEach((card) => {
      card.addEventListener('click', () => {
        el.instansiCards.forEach((c) => c.classList.remove('selected'));
        card.classList.add('selected');
        state.packetKey = card.dataset.packet;
      });
    });

    // Pilihan Mode Latihan (Simulasi vs Belajar Mandiri)
    if (el.modeCards && el.modeCards.length > 0) {
      el.modeCards.forEach((card) => {
        card.addEventListener('click', () => {
          setExamMode(card.dataset.mode || 'simulasi');
        });
      });
    }

    // Tombol Mulai
    el.btnStart.addEventListener('click', () => {
      startNewExam(state.packetKey, {
        mode: state.mode,
        shuffleQuestions: el.optShuffleQuestions.checked,
        shuffleOptions: el.optShuffleOptions.checked
      });
    });
  }

  function setExamMode(mode) {
    state.mode = mode;
    if (el.modeCards) {
      el.modeCards.forEach((c) => c.classList.remove('selected'));
    }

    if (mode === 'simulasi') {
      if (el.modeCardSimulasi) el.modeCardSimulasi.classList.add('selected');
      if (el.btnStart) el.btnStart.textContent = 'Mulai Simulasi CAT Sekarang »';
      if (el.rulesBoxTitle) el.rulesBoxTitle.textContent = 'Ketentuan & Petunjuk Ujian (Mode Simulasi):';
      if (el.rulesBoxList) {
        el.rulesBoxList.innerHTML = `
          <li>Gunakan tombol <strong>Simpan & Lanjutkan</strong> untuk menyimpan jawaban dan berpindah ke soal berikutnya.</li>
          <li>Gunakan tombol <strong>Ragu-Ragu</strong> (kuning) jika Anda belum yakin dengan jawaban yang dipilih.</li>
          <li>Warna pada grid nomor soal: <strong>Hijau</strong> (Sudah dijawab), <strong>Kuning</strong> (Ragu-ragu), <strong>Abu-abu</strong> (Belum dijawab).</li>
          <li>Progres pengerjaan Anda otomatis disimpan. Jika browser tertutup tidak sengaja, ujian dapat dilanjutkan kembali.</li>
        `;
      }
    } else {
      if (el.modeCardBelajar) el.modeCardBelajar.classList.add('selected');
      if (el.btnStart) el.btnStart.textContent = '📖 Mulai Mode Belajar Mandiri Sekarang »';
      if (el.rulesBoxTitle) el.rulesBoxTitle.textContent = 'Ketentuan & Petunjuk (Mode Belajar Mandiri):';
      if (el.rulesBoxList) {
        el.rulesBoxList.innerHTML = `
          <li>Pilih salah satu opsi jawaban A–E, status <strong>Benar (Hijau)</strong> atau <strong>Salah (Merah)</strong> langsung terlihat seketika.</li>
          <li>Kunci jawaban resmi dan pembahasan lengkap (beserta rujukan hukum/standar) langsung terbuka di bawah soal.</li>
          <li>Warna pada grid nomor: <strong>Hijau</strong> (Jawaban Benar), <strong>Merah</strong> (Jawaban Salah), <strong>Abu-abu</strong> (Belum Dikerjakan).</li>
          <li>Tidak ada batasan waktu, Anda dapat belajar santai dan berpindah soal sesuka hati.</li>
        `;
      }
    }
  }

  // ==========================================
  // AUTO-SAVE & RESUME SESSION
  // ==========================================
  function checkSavedSession() {
    const raw = localStorage.getItem(STORAGE_KEY_SESSION);
    if (!raw) {
      el.resumeBanner.style.display = 'none';
      return;
    }

    try {
      const saved = JSON.parse(raw);
      if (saved && saved.activeQuestions && saved.activeQuestions.length > 0) {
        const isBelajar = saved.mode === 'belajar';
        const remainingMin = Math.ceil((saved.timerSeconds || 0) / 60);
        const timeInfo = isBelajar ? 'Mode Belajar Mandiri' : `Sisa Waktu: ${remainingMin} Menit`;
        el.resumeInfoText.textContent = `Paket: ${saved.packetTitle || 'Ujian'} • ${timeInfo} • Terjawab: ${Object.keys(saved.answers || {}).length}/${saved.activeQuestions.length} Soal.`;
        el.resumeBanner.style.display = 'flex';

        el.btnResumeSession.onclick = () => resumeExamSession(saved);
        el.btnDiscardSession.onclick = () => {
          localStorage.removeItem(STORAGE_KEY_SESSION);
          el.resumeBanner.style.display = 'none';
        };
      } else {
        el.resumeBanner.style.display = 'none';
      }
    } catch (e) {
      console.error('Sesi tersimpan tidak valid:', e);
      el.resumeBanner.style.display = 'none';
    }
  }

  function saveCurrentSession() {
    if (!state.activeQuestions || state.activeQuestions.length === 0) return;
    const sessionData = {
      packetKey: state.packetKey,
      packetTitle: state.packetData ? state.packetData.title : 'Ujian',
      mode: state.mode || 'simulasi',
      activeQuestions: state.activeQuestions,
      currentIndex: state.currentIndex,
      answers: state.answers,
      doubts: Array.from(state.doubts),
      timerSeconds: state.timerSeconds,
      startTime: state.startTime,
      updatedAt: new Date().toISOString()
    };
    localStorage.setItem(STORAGE_KEY_SESSION, JSON.stringify(sessionData));
  }

  function clearCurrentSession() {
    localStorage.removeItem(STORAGE_KEY_SESSION);
    el.resumeBanner.style.display = 'none';
  }

  function resumeExamSession(saved) {
    state.packetKey = saved.packetKey;
    state.packetData = window.BANK_SOAL[saved.packetKey];
    state.mode = saved.mode || 'simulasi';
    state.activeQuestions = saved.activeQuestions;
    state.currentIndex = saved.currentIndex || 0;
    state.answers = saved.answers || {};
    state.doubts = new Set(saved.doubts || []);
    state.timerSeconds = saved.timerSeconds || 0;
    state.startTime = saved.startTime || new Date().toISOString();

    el.resumeBanner.style.display = 'none';
    el.screenWelcome.style.display = 'none';
    el.screenResult.style.display = 'none';
    el.screenExam.style.display = 'grid';
    el.timerContainer.style.display = 'flex';
    document.body.classList.add('in-exam');
    if (el.mobileExamBar) el.mobileExamBar.style.display = 'flex';

    if (state.mode === 'belajar') {
      el.examTitle.textContent = `[Mode Belajar] ${state.packetData ? state.packetData.title : 'Belajar Mandiri'}`;
      if (el.btnFinish) el.btnFinish.textContent = 'Selesai Belajar & Lihat Ringkasan';
      if (el.btnDoubt) el.btnDoubt.style.display = 'none';
      if (el.legendItemWrong) el.legendItemWrong.style.display = 'flex';
      if (el.legendItemDoubt) el.legendItemDoubt.style.display = 'none';
      if (el.legendLabelAnswered) el.legendLabelAnswered.textContent = 'Jawaban Benar';
      el.timerDisplay.textContent = '📖 Belajar Mandiri';
      el.timerDisplay.classList.remove('timer-danger');
    } else {
      el.examTitle.textContent = state.packetData ? state.packetData.title : 'Simulasi Ujian';
      if (el.btnFinish) el.btnFinish.textContent = 'Selesai Ujian';
      if (el.btnDoubt) el.btnDoubt.style.display = 'inline-block';
      if (el.legendItemWrong) el.legendItemWrong.style.display = 'none';
      if (el.legendItemDoubt) el.legendItemDoubt.style.display = 'flex';
      if (el.legendLabelAnswered) el.legendLabelAnswered.textContent = 'Sudah Dijawab';
      startTimer();
    }

    if (el.quickJumpContainer) {
      el.quickJumpContainer.style.display = state.packetKey === 'skd' ? 'flex' : 'none';
    }

    renderGrid();
    loadQuestion(state.currentIndex);
  }

  // ==========================================
  // MULAI UJIAN BARU
  // ==========================================
  function startNewExam(packetKey, options = {}) {
    state.packetKey = packetKey;
    state.packetData = window.BANK_SOAL[packetKey];
    state.mode = options.mode || state.mode || 'simulasi';
    if (!state.packetData) return;

    let clonedQuestions = JSON.parse(JSON.stringify(state.packetData.questions));

    // Acak Urutan Soal & Sampling Standar Ujian
    if (options.shuffleQuestions) {
      if (packetKey === 'skd') {
        const twk = clonedQuestions.filter((q) => q.category === 'TWK');
        const tiu = clonedQuestions.filter((q) => q.category === 'TIU');
        const tkp = clonedQuestions.filter((q) => q.category === 'TKP');
        shuffleArray(twk);
        shuffleArray(tiu);
        shuffleArray(tkp);
        
        // Sampling persis standar CAT BKN (30 TWK, 35 TIU, 45 TKP) dari bank soal yang lebih besar
        const sampleTwk = twk.length > 30 ? twk.slice(0, 30) : twk;
        const sampleTiu = tiu.length > 35 ? tiu.slice(0, 35) : tiu;
        const sampleTkp = tkp.length > 45 ? tkp.slice(0, 45) : tkp;
        clonedQuestions = [...sampleTwk, ...sampleTiu, ...sampleTkp];
      } else {
        shuffleArray(clonedQuestions);
        // Sampling persis standar SKB BKN (100 Soal) dari bank soal yang lebih besar
        if (clonedQuestions.length > 100) {
          clonedQuestions = clonedQuestions.slice(0, 100);
        }
      }
    } else {
      // Jika mode simulasi (bukan belajar mandiri) dan shuffle tidak dicentang, batasi ke standar resmi 110 (SKD) atau 100 (SKB)
      if (state.mode === 'simulasi') {
        if (packetKey === 'skd') {
          const twk = clonedQuestions.filter((q) => q.category === 'TWK').slice(0, 30);
          const tiu = clonedQuestions.filter((q) => q.category === 'TIU').slice(0, 35);
          const tkp = clonedQuestions.filter((q) => q.category === 'TKP').slice(0, 45);
          clonedQuestions = [...twk, ...tiu, ...tkp];
        } else if (clonedQuestions.length > 100) {
          clonedQuestions = clonedQuestions.slice(0, 100);
        }
      }
      // Jika mode belajar mandiri dan shuffle tidak dicentang: tampilkan seluruh bank soal (160 SKD / 101 SKB) untuk dipelajari tuntas
    }

    // Acak Pilihan Opsi A-E bila diminta
    if (options.shuffleOptions) {
      clonedQuestions.forEach((q) => {
        q.options = shuffleQuestionOptions(q);
      });
    }

    state.activeQuestions = clonedQuestions;
    state.currentIndex = 0;
    state.answers = {};
    state.doubts.clear();
    state.timerSeconds = state.packetData.timeMinutes * 60;
    state.startTime = new Date().toISOString();

    el.resumeBanner.style.display = 'none';
    el.screenWelcome.style.display = 'none';
    el.screenResult.style.display = 'none';
    el.screenExam.style.display = 'grid';
    el.timerContainer.style.display = 'flex';
    document.body.classList.add('in-exam');
    if (el.mobileExamBar) el.mobileExamBar.style.display = 'flex';

    if (state.mode === 'belajar') {
      el.examTitle.textContent = `[Mode Belajar] ${state.packetData.title}`;
      if (el.btnFinish) el.btnFinish.textContent = 'Selesai Belajar & Lihat Ringkasan';
      if (el.btnDoubt) el.btnDoubt.style.display = 'none';
      if (el.legendItemWrong) el.legendItemWrong.style.display = 'flex';
      if (el.legendItemDoubt) el.legendItemDoubt.style.display = 'none';
      if (el.legendLabelAnswered) el.legendLabelAnswered.textContent = 'Jawaban Benar';
      el.timerDisplay.textContent = '📖 Belajar Mandiri';
      el.timerDisplay.classList.remove('timer-danger');
    } else {
      el.examTitle.textContent = state.packetData.title;
      if (el.btnFinish) el.btnFinish.textContent = 'Selesai Ujian';
      if (el.btnDoubt) el.btnDoubt.style.display = 'inline-block';
      if (el.legendItemWrong) el.legendItemWrong.style.display = 'none';
      if (el.legendItemDoubt) el.legendItemDoubt.style.display = 'flex';
      if (el.legendLabelAnswered) el.legendLabelAnswered.textContent = 'Sudah Dijawab';
      startTimer();
    }

    if (el.quickJumpContainer) {
      el.quickJumpContainer.style.display = state.packetKey === 'skd' ? 'flex' : 'none';
    }

    renderGrid();
    loadQuestion(state.currentIndex);
    saveCurrentSession();
  }

  function shuffleArray(arr) {
    for (let i = arr.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    return arr;
  }

  function shuffleQuestionOptions(q) {
    const letters = ['A', 'B', 'C', 'D', 'E'];
    const qAns = getQuestionAnswer(q);
    const qPts = getQuestionPoints(q);
    const currentEntries = letters.map((k) => ({
      key: k,
      text: q.options[k],
      point: qPts ? qPts[k] : (k === qAns ? 5 : 0)
    }));

    shuffleArray(currentEntries);

    const newOptions = {};
    const newPoints = {};
    let newCorrectKey = 'A';

    currentEntries.forEach((entry, idx) => {
      const newKey = letters[idx];
      newOptions[newKey] = entry.text;
      newPoints[newKey] = entry.point;
      if (entry.key === qAns) {
        newCorrectKey = newKey;
      }
    });

    setQuestionPoints(q, newPoints);
    setQuestionAnswer(q, newCorrectKey);
    return newOptions;
  }

  // ==========================================
  // NAVIGASI & PENYAJIAN SOAL
  // ==========================================
  function setupExamActionHandlers() {
    el.btnPrev.addEventListener('click', () => navigateQuestion(-1));
    el.btnNext.addEventListener('click', () => navigateQuestion(1));
    el.btnDoubt.addEventListener('click', toggleDoubt);

    el.btnFinish.addEventListener('click', showModalFinish);
    el.btnModalCancel.addEventListener('click', hideModalFinish);
    el.btnModalConfirm.addEventListener('click', () => {
      hideModalFinish();
      finishExam();
    });

    // Hentikan Sesi
    if (el.btnAbortSession) {
      el.btnAbortSession.addEventListener('click', showModalAbort);
    }
    if (el.btnModalAbortCancel) {
      el.btnModalAbortCancel.addEventListener('click', hideModalAbort);
    }
    if (el.btnModalAbortConfirm) {
      el.btnModalAbortConfirm.addEventListener('click', () => {
        hideModalAbort();
        abortCurrentSession();
      });
    }

    if (el.jumpTwk) el.jumpTwk.addEventListener('click', () => jumpToCategoryIndex('TWK'));
    if (el.jumpTiu) el.jumpTiu.addEventListener('click', () => jumpToCategoryIndex('TIU'));
    if (el.jumpTkp) el.jumpTkp.addEventListener('click', () => jumpToCategoryIndex('TKP'));

    // Mobile Bottom Bar Actions & Drawer Sheet
    if (el.mobileBtnPrev) el.mobileBtnPrev.addEventListener('click', () => navigateQuestion(-1));
    if (el.mobileBtnNext) el.mobileBtnNext.addEventListener('click', () => navigateQuestion(1));
    if (el.mobileBtnSheet) el.mobileBtnSheet.addEventListener('click', toggleMobileSheet);
    if (el.btnCloseSidebar) el.btnCloseSidebar.addEventListener('click', closeMobileSheet);
    if (el.navSidebarBackdrop) el.navSidebarBackdrop.addEventListener('click', closeMobileSheet);
  }

  function openMobileSheet() {
    if (el.navSidebar) el.navSidebar.classList.add('open');
    if (el.navSidebarBackdrop) el.navSidebarBackdrop.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function closeMobileSheet() {
    if (el.navSidebar) el.navSidebar.classList.remove('open');
    if (el.navSidebarBackdrop) el.navSidebarBackdrop.classList.remove('open');
    document.body.style.overflow = '';
  }

  function toggleMobileSheet() {
    if (el.navSidebar && el.navSidebar.classList.contains('open')) {
      closeMobileSheet();
    } else {
      openMobileSheet();
    }
  }

  function showModalAbort() {
    closeMobileSheet();
    if (el.modalAbort) el.modalAbort.style.display = 'flex';
  }

  function hideModalAbort() {
    if (el.modalAbort) el.modalAbort.style.display = 'none';
  }

  function abortCurrentSession() {
    if (state.timerId) clearInterval(state.timerId);
    clearCurrentSession();
    document.body.classList.remove('in-exam');
    if (el.mobileExamBar) el.mobileExamBar.style.display = 'none';
    closeMobileSheet();

    el.screenExam.style.display = 'none';
    el.timerContainer.style.display = 'none';
    el.screenWelcome.style.display = 'block';
    renderBankSummary();
    renderHistoryDashboard();
  }

  function jumpToCategoryIndex(category) {
    const idx = state.activeQuestions.findIndex((q) => q.category === category);
    if (idx !== -1) {
      loadQuestion(idx);
      closeMobileSheet();
    }
  }

  function renderGrid() {
    el.questionGrid.innerHTML = '';
    const questions = state.activeQuestions;

    questions.forEach((q, idx) => {
      const btn = document.createElement('button');
      btn.className = 'grid-btn';
      btn.textContent = idx + 1;
      btn.dataset.index = idx;

      btn.addEventListener('click', () => {
        loadQuestion(idx);
        closeMobileSheet();
      });

      el.questionGrid.appendChild(btn);
    });

    updateGridStatus();
  }

  function updateGridStatus() {
    const buttons = el.questionGrid.querySelectorAll('.grid-btn');
    const questions = state.activeQuestions;
    const isStudyMode = state.mode === 'belajar';

    buttons.forEach((btn, idx) => {
      const q = questions[idx];
      btn.classList.remove('current', 'answered', 'doubt', 'wrong');

      if (idx === state.currentIndex) {
        btn.classList.add('current');
        if (el.questionGrid) {
          const gridTop = el.questionGrid.scrollTop;
          const gridHeight = el.questionGrid.clientHeight;
          const btnTop = btn.offsetTop - el.questionGrid.offsetTop;
          const btnBottom = btnTop + btn.offsetHeight;
          if (btnTop < gridTop) {
            el.questionGrid.scrollTo({ top: Math.max(0, btnTop - 8), behavior: 'smooth' });
          } else if (btnBottom > gridTop + gridHeight - 12) {
            el.questionGrid.scrollTo({ top: btnBottom - gridHeight + 20, behavior: 'smooth' });
          }
        }
      }

      if (isStudyMode) {
        const userAns = state.answers[q.id];
        const qAns = getQuestionAnswer(q);
        const qPts = getQuestionPoints(q);
        if (userAns) {
          if (q.category === 'TKP') {
            const pt = qPts ? (qPts[userAns] || 0) : 0;
            if (pt >= 4) btn.classList.add('answered');
            else btn.classList.add('wrong');
          } else {
            if (userAns === qAns) {
              btn.classList.add('answered');
            } else {
              btn.classList.add('wrong');
            }
          }
        }
      } else {
        if (state.doubts.has(q.id)) {
          btn.classList.add('doubt');
        } else if (state.answers[q.id]) {
          btn.classList.add('answered');
        }
      }
    });
  }

  function loadQuestion(index) {
    const questions = state.activeQuestions;
    if (index < 0 || index >= questions.length) return;

    state.currentIndex = index;
    const q = questions[index];

    // Info header soal
    el.qIndexBadge.textContent = `Soal No. ${index + 1} dari ${questions.length}`;
    
    // Tag Instansi
    const instansiName = q.instansi || (state.packetData ? state.packetData.instansi : 'Nasional');
    if (el.qInstansiTag) {
      el.qInstansiTag.textContent = `🏛️ ${instansiName}`;
    }

    el.qCategoryTag.textContent = q.category;
    el.qSubcategoryTag.textContent = q.subcategory || '';

    el.qCategoryTag.className = 'tag';
    if (q.category === 'TWK') el.qCategoryTag.classList.add('tag-twk');
    else if (q.category === 'TIU') el.qCategoryTag.classList.add('tag-tiu');
    else if (q.category === 'TKP') el.qCategoryTag.classList.add('tag-tkp');
    else el.qCategoryTag.classList.add('tag-skb');

    el.qText.textContent = q.question;

    el.optionsContainer.innerHTML = '';
    const selectedAnswer = state.answers[q.id];
    const isStudyMode = state.mode === 'belajar';
    const hasAnswered = Boolean(selectedAnswer);

    const isTkp = q.category === 'TKP';
    const qAns = getQuestionAnswer(q);
    const qPts = getQuestionPoints(q);
    const qExp = getQuestionExplanation(q);

    let bestTkpKey = 'A';
    if (isTkp && qPts) {
      let maxPt = -1;
      ['A', 'B', 'C', 'D', 'E'].forEach((k) => {
        if ((qPts[k] || 0) > maxPt) {
          maxPt = qPts[k];
          bestTkpKey = k;
        }
      });
    }

    ['A', 'B', 'C', 'D', 'E'].forEach((optKey) => {
      if (!q.options[optKey]) return;
      const optItem = document.createElement('div');
      optItem.className = 'option-item';

      let badgeHtml = '';

      if (isStudyMode && hasAnswered) {
        if (!isTkp) {
          // Non-TKP Standard Feedback
          if (optKey === selectedAnswer && optKey === qAns) {
            optItem.classList.add('study-correct');
            badgeHtml = '<span class="option-study-badge badge-correct">✓ Jawaban Anda Benar (+5)</span>';
          } else if (optKey === selectedAnswer && optKey !== qAns) {
            optItem.classList.add('study-wrong');
            badgeHtml = '<span class="option-study-badge badge-wrong">✗ Pilihan Anda (Salah)</span>';
          } else if (optKey === qAns) {
            optItem.classList.add('study-key');
            badgeHtml = '<span class="option-study-badge badge-key">✓ Kunci Jawaban Benar</span>';
          }
        } else {
          // TKP Feedback
          const pt = qPts ? (qPts[optKey] || 0) : 0;
          if (optKey === selectedAnswer) {
            optItem.classList.add('selected');
            badgeHtml = `<span class="option-study-badge ${pt === 5 ? 'badge-correct' : 'badge-tkp-pts'}">Pilihan Anda: <strong>${pt} Poin</strong></span>`;
          } else if (optKey === bestTkpKey) {
            optItem.classList.add('study-key');
            badgeHtml = '<span class="option-study-badge badge-tkp-max">★ Bobot 5 Poin (Maksimal)</span>';
          } else {
            badgeHtml = `<span class="option-study-badge badge-tkp-pts">${pt} Poin</span>`;
          }
        }
      } else {
        if (selectedAnswer === optKey) {
          optItem.classList.add('selected');
        }
      }

      optItem.innerHTML = `
        <span class="option-letter">${optKey}</span>
        <span class="option-text">${q.options[optKey]}</span>
        ${badgeHtml}
      `;

      optItem.addEventListener('click', () => {
        state.answers[q.id] = optKey;
        loadQuestion(state.currentIndex);
        updateGridStatus();
        saveCurrentSession();
      });

      el.optionsContainer.appendChild(optItem);
    });

    // Tampilkan / Sembunyikan Box Pembahasan di Mode Belajar
    if (el.studyExpCard) {
      if (isStudyMode && hasAnswered) {
        el.studyExpCard.style.display = 'block';
        if (el.studyCorrectBadge) {
          el.studyCorrectBadge.textContent = isTkp ? `Poin 5: ${bestTkpKey}` : `Kunci: ${qAns}`;
        }
        if (el.studyExpContent) {
          el.studyExpContent.innerHTML = formatExplanationText(qExp);
        }
      } else {
        el.studyExpCard.style.display = 'none';
      }
    }

    el.btnPrev.disabled = index === 0;
    el.btnNext.textContent = index === questions.length - 1 
      ? (isStudyMode ? 'Selesai Belajar' : 'Simpan') 
      : (isStudyMode ? 'Soal Berikutnya »' : 'Simpan & Lanjutkan »');

    if (el.mobileSheetProgress) {
      el.mobileSheetProgress.textContent = `${index + 1} / ${questions.length}`;
    }
    if (el.mobileBtnPrev) {
      el.mobileBtnPrev.disabled = index === 0;
    }
    if (el.mobileBtnNext) {
      el.mobileBtnNext.textContent = index === questions.length - 1 
        ? (isStudyMode ? 'Selesai' : 'Simpan') 
        : 'Next »';
    }

    if (state.doubts.has(q.id)) {
      el.btnDoubt.classList.add('active');
      el.btnDoubt.textContent = '★ Tandai Yakin';
    } else {
      el.btnDoubt.classList.remove('active');
      el.btnDoubt.textContent = '⚠ Ragu-Ragu';
    }

    updateGridStatus();
  }

  function formatExplanationText(text) {
    if (!text) return 'Belum ada penjelasan untuk butir soal ini.';
    return text
      .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
      .replace(/\n\n/g, '<br><br>')
      .replace(/\n/g, '<br>');
  }

  function navigateQuestion(direction) {
    const newIdx = state.currentIndex + direction;
    if (newIdx >= 0 && newIdx < state.activeQuestions.length) {
      loadQuestion(newIdx);
      saveCurrentSession();
    }
  }

  function toggleDoubt() {
    const q = state.activeQuestions[state.currentIndex];
    if (state.doubts.has(q.id)) {
      state.doubts.delete(q.id);
    } else {
      state.doubts.add(q.id);
    }
    loadQuestion(state.currentIndex);
    saveCurrentSession();
  }

  // ==========================================
  // PENGELOLA WAKTU (TIMER)
  // ==========================================
  function startTimer() {
    if (state.timerId) clearInterval(state.timerId);

    function tick() {
      const minutes = Math.floor(state.timerSeconds / 60);
      const seconds = state.timerSeconds % 60;
      el.timerDisplay.textContent = `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;

      if (state.timerSeconds <= 300) {
        el.timerDisplay.classList.add('timer-danger');
      } else {
        el.timerDisplay.classList.remove('timer-danger');
      }

      if (state.timerSeconds <= 0) {
        clearInterval(state.timerId);
        alert('Waktu ujian telah berakhir! Jawaban Anda akan dihitung secara otomatis.');
        finishExam();
      } else {
        state.timerSeconds--;
        if (state.timerSeconds % 5 === 0) {
          saveCurrentSession();
        }
      }
    }

    tick();
    state.timerId = setInterval(tick, 1000);
  }

  // ==========================================
  // MODAL SELESAI UJIAN
  // ==========================================
  function showModalFinish() {
    closeMobileSheet();
    const questions = state.activeQuestions;
    let answeredCount = 0;
    let doubtCount = 0;
    let unansweredCount = 0;

    questions.forEach((q) => {
      const isAnswered = !!state.answers[q.id];
      const isDoubt = state.doubts.has(q.id);

      if (isDoubt) doubtCount++;
      if (isAnswered) answeredCount++;
      if (!isAnswered) unansweredCount++;
    });

    el.recapAnswered.textContent = answeredCount;
    el.recapDoubt.textContent = doubtCount;
    el.recapUnanswered.textContent = unansweredCount;

    el.modalFinish.style.display = 'flex';
  }

  function hideModalFinish() {
    el.modalFinish.style.display = 'none';
  }

  // ==========================================
  // KALKULASI SKOR, PEMBAHASAN & SIMPAN RIWAYAT
  // ==========================================
  function finishExam() {
    if (state.timerId) clearInterval(state.timerId);
    clearCurrentSession();
    document.body.classList.remove('in-exam');
    if (el.mobileExamBar) el.mobileExamBar.style.display = 'none';
    closeMobileSheet();

    el.timerContainer.style.display = 'none';
    el.screenExam.style.display = 'none';
    el.screenResult.style.display = 'block';

    calculateAndRenderScore();
  }

  function calculateAndRenderScore() {
    const isSkd = state.packetKey === 'skd';
    const questions = state.activeQuestions;

    let scoreTWK = 0, correctTWK = 0, totalTWK = 0;
    let scoreTIU = 0, correctTIU = 0, totalTIU = 0;
    let scoreTKP = 0, totalTKP = 0;
    let scoreSKB = 0, correctSKB = 0, totalSKB = 0;

    questions.forEach((q) => {
      const userAns = state.answers[q.id];
      const qAns = getQuestionAnswer(q);
      const qPts = getQuestionPoints(q);
      const pts = userAns ? (qPts ? qPts[userAns] || 0 : (userAns === qAns ? 5 : 0)) : 0;

      if (isSkd) {
        if (q.category === 'TWK') {
          totalTWK++;
          scoreTWK += pts;
          if (pts > 0) correctTWK++;
        } else if (q.category === 'TIU') {
          totalTIU++;
          scoreTIU += pts;
          if (pts > 0) correctTIU++;
        } else if (q.category === 'TKP') {
          totalTKP++;
          scoreTKP += pts;
        }
      } else {
        totalSKB++;
        scoreSKB += pts;
        if (pts > 0) correctSKB++;
      }
    });

    let passStatus = false;
    let totalScore = 0;
    const packetTitle = state.packetData ? state.packetData.title : 'Ujian CAT';
    const instansiName = state.packetData ? state.packetData.instansi : 'Nasional';

    // Jika dalam Mode Belajar Mandiri, tampilkan ringkasan belajar khusus
    if (state.mode === 'belajar') {
      const answeredCount = Object.keys(state.answers).length;
      let correctCount = 0;
      let wrongCount = 0;

      questions.forEach((q) => {
        const userAns = state.answers[q.id];
        const qAns = getQuestionAnswer(q);
        const qPts = getQuestionPoints(q);
        if (userAns) {
          if (q.category === 'TKP') {
            const pt = qPts ? (qPts[userAns] || 0) : 0;
            if (pt >= 4) correctCount++;
            else wrongCount++;
          } else {
            if (userAns === qAns) correctCount++;
            else wrongCount++;
          }
        }
      });

      renderResultCardStudy({
        isSkd,
        packetTitle,
        instansiName,
        totalQuestions: questions.length,
        answeredCount,
        correctCount,
        wrongCount,
        questions
      });
      return;
    }

    if (isSkd) {
      const pg = state.packetData.passingGrades;
      const passTWK = scoreTWK >= pg.twk;
      const passTIU = scoreTIU >= pg.tiu;
      const passTKP = scoreTKP >= pg.tkp;
      passStatus = passTWK && passTIU && passTKP;
      totalScore = scoreTWK + scoreTIU + scoreTKP;

      saveExamToHistory({
        date: new Date().toLocaleString('id-ID'),
        packet: `${packetTitle} (${instansiName})`,
        twk: scoreTWK,
        tiu: scoreTIU,
        tkp: scoreTKP,
        total: totalScore,
        passed: passStatus
      });

      renderResultCardSKD({
        totalScore, passStatus, pg,
        scoreTWK, correctTWK, totalTWK, passTWK,
        scoreTIU, correctTIU, totalTIU, passTIU,
        scoreTKP, totalTKP, passTKP,
        questions, packetTitle, instansiName
      });
    } else {
      totalScore = scoreSKB;
      passStatus = true;

      saveExamToHistory({
        date: new Date().toLocaleString('id-ID'),
        packet: `${packetTitle} (${instansiName})`,
        twk: '-',
        tiu: '-',
        tkp: '-',
        total: totalScore,
        passed: true
      });

      renderResultCardSKB({
        scoreSKB, correctSKB, totalSKB, questions, packetTitle, instansiName
      });
    }
  }

  function renderResultCardStudy(d) {
    const accuracy = d.answeredCount > 0 ? Math.round((d.correctCount / d.answeredCount) * 100) : 0;
    const completionRate = Math.round((d.answeredCount / d.totalQuestions) * 100);

    el.resultContainer.innerHTML = `
      <div class="result-card">
        <div class="result-header">
          <span class="result-badge pass" style="background:#d1fae5; color:#065f46; border:1px solid #6ee7b7;">
            📖 RINGKASAN MODE BELAJAR MANDIRI
          </span>
          <h2 style="font-size: 1.85rem; color: #065f46; margin-top: 6px;">${d.packetTitle}</h2>
          <p style="color: var(--text-muted); margin-top: 4px;">Instansi: <strong>${d.instansiName}</strong> • Evaluasi Pembahasan Mandiri</p>
        </div>

        <div class="score-cards-grid">
          <div class="score-card">
            <div class="score-card-title">Soal Telah Dipelajari</div>
            <div class="score-card-value">${d.answeredCount} <span style="font-size:1rem; color:#64748b;">/ ${d.totalQuestions}</span></div>
            <div class="score-card-pg">Progres Sesi: ${completionRate}%</div>
            <div style="font-size: 0.75rem; color: #64748b; margin-top: 4px;">Dapat diulang kapan saja</div>
          </div>

          <div class="score-card">
            <div class="score-card-title" style="color:#059669;">Jawaban Tepat / Benar</div>
            <div class="score-card-value" style="color:#059669;">${d.correctCount}</div>
            <div class="score-card-pg" style="color:#059669;">Tingkat Akurasi: ${accuracy}%</div>
            <div style="font-size: 0.75rem; color: #059669; margin-top: 4px;">Pemahaman materi baik</div>
          </div>

          <div class="score-card">
            <div class="score-card-title" style="color:#dc2626;">Perlu Dievaluasi (Salah)</div>
            <div class="score-card-value" style="color:#dc2626;">${d.wrongCount}</div>
            <div class="score-card-pg" style="color:#dc2626;">Gunakan filter di bawah untuk fokus</div>
            <div style="font-size: 0.75rem; color: #dc2626; margin-top: 4px;">Tinjau rujukan & tips</div>
          </div>
        </div>

        <div style="display:flex; justify-content:center; gap: 14px; margin-bottom: 24px;">
          <button id="btn-restart" class="btn-nav" style="background:#059669; color:#fff; border:none; padding:10px 22px;">Ulangi Belajar Paket Ini</button>
          <button id="btn-switch-packet" class="btn-nav" style="padding:10px 22px;">Kembali ke Menu Utama</button>
        </div>

        ${renderReviewSectionHTML(d.questions)}
      </div>
    `;

    setupReviewInteractions(d.questions);
  }

  function renderResultCardSKD(d) {
    el.resultContainer.innerHTML = `
      <div class="result-card">
        <div class="result-header">
          <span class="result-badge ${d.passStatus ? 'pass' : 'fail'}">
            ${d.passStatus ? '✓ MEMENUHI PASSING GRADE (LOLOS)' : '✕ BELUM MEMENUHI PASSING GRADE'}
          </span>
          <h2 style="font-size: 1.85rem; color: var(--primary); margin-top: 6px;">Total Skor SKD: ${d.totalScore}</h2>
          <p style="color: var(--text-muted); margin-top: 4px;">Instansi: <strong>${d.instansiName}</strong> • Standar Resmi KepmenPAN-RB</p>
        </div>

        <div class="score-cards-grid">
          <div class="score-card">
            <div class="score-card-title">Tes Wawasan Kebangsaan (TWK)</div>
            <div class="score-card-value">${d.scoreTWK}</div>
            <div class="score-card-pg">Ambang Batas: ${d.pg.twk} (${d.passTWK ? '<strong style="color:var(--success)">Lolos</strong>' : '<strong style="color:var(--danger)">Tidak Lolos</strong>'})</div>
            <div style="font-size: 0.75rem; color: #64748b; margin-top: 4px;">Benar: ${d.correctTWK} / ${d.totalTWK}</div>
          </div>

          <div class="score-card">
            <div class="score-card-title">Tes Inteligensia Umum (TIU)</div>
            <div class="score-card-value">${d.scoreTIU}</div>
            <div class="score-card-pg">Ambang Batas: ${d.pg.tiu} (${d.passTIU ? '<strong style="color:var(--success)">Lolos</strong>' : '<strong style="color:var(--danger)">Tidak Lolos</strong>'})</div>
            <div style="font-size: 0.75rem; color: #64748b; margin-top: 4px;">Benar: ${d.correctTIU} / ${d.totalTIU}</div>
          </div>

          <div class="score-card">
            <div class="score-card-title">Tes Karakteristik Pribadi (TKP)</div>
            <div class="score-card-value">${d.scoreTKP}</div>
            <div class="score-card-pg">Ambang Batas: ${d.pg.tkp} (${d.passTKP ? '<strong style="color:var(--success)">Lolos</strong>' : '<strong style="color:var(--danger)">Tidak Lolos</strong>'})</div>
            <div style="font-size: 0.75rem; color: #64748b; margin-top: 4px;">Skala Skor 1-5 (${d.totalTKP} soal)</div>
          </div>
        </div>

        <div style="display:flex; justify-content:center; gap: 14px; margin-bottom: 24px;">
          <button id="btn-restart" class="btn-nav" style="background:var(--primary); color:#fff; border:none;">Ulangi Ujian Ini</button>
          <button id="btn-switch-packet" class="btn-nav">Menu Utama Dashboard</button>
        </div>

        ${renderReviewSectionHTML(d.questions)}
      </div>
    `;

    setupReviewInteractions(d.questions);
  }

  function renderResultCardSKB(d) {
    el.resultContainer.innerHTML = `
      <div class="result-card">
        <div class="result-header">
          <span class="result-badge pass">SELESAI MENGERJAKAN SKB INSTANSI</span>
          <h2 style="font-size: 1.85rem; color: var(--primary); margin-top: 6px;">Skor ${d.packetTitle}: ${d.scoreSKB}</h2>
          <p style="color: var(--text-muted); margin-top: 4px;">Instansi: <strong>${d.instansiName}</strong> • Menjawab benar: ${d.correctSKB} dari ${d.totalSKB} soal (${Math.round((d.correctSKB / d.totalSKB) * 100)}%)</p>
        </div>

        <div style="display:flex; justify-content:center; gap: 14px; margin-bottom: 24px;">
          <button id="btn-restart" class="btn-nav" style="background:var(--primary); color:#fff; border:none;">Ulangi Ujian Ini</button>
          <button id="btn-switch-packet" class="btn-nav">Pilih Instansi Lain</button>
        </div>

        ${renderReviewSectionHTML(d.questions)}
      </div>
    `;

    setupReviewInteractions(d.questions);
  }

  function renderReviewSectionHTML(questions) {
    return `
      <div class="review-section">
        <div class="review-toolbar">
          <div class="filter-buttons-group">
            <button class="btn-filter active" data-filter="all">Semua (${questions.length})</button>
            <button class="btn-filter" data-filter="wrong">Jawaban Salah</button>
            <button class="btn-filter" data-filter="correct">Jawaban Benar</button>
            <button class="btn-filter" data-filter="doubt">Ragu-Ragu</button>
          </div>
          <input type="text" id="review-search-input" class="search-review-input" placeholder="🔍 Cari pembahasan soal...">
        </div>

        <div id="review-items-container">
          <!-- Rendered by filter logic -->
        </div>
      </div>
    `;
  }

  function setupReviewInteractions(questions) {
    document.getElementById('btn-restart').addEventListener('click', () => {
      startNewExam(state.packetKey);
    });

    document.getElementById('btn-switch-packet').addEventListener('click', () => {
      el.screenResult.style.display = 'none';
      el.screenWelcome.style.display = 'block';
      renderHistoryDashboard();
    });

    const filterBtns = document.querySelectorAll('.btn-filter');
    const searchInput = document.getElementById('review-search-input');

    filterBtns.forEach((btn) => {
      btn.addEventListener('click', () => {
        filterBtns.forEach((b) => b.classList.remove('active'));
        btn.classList.add('active');
        state.reviewFilter = btn.dataset.filter;
        renderFilteredReviewItems(questions);
      });
    });

    if (searchInput) {
      searchInput.addEventListener('input', (e) => {
        state.reviewSearchQuery = e.target.value.toLowerCase();
        renderFilteredReviewItems(questions);
      });
    }

    renderFilteredReviewItems(questions);
  }

  function renderFilteredReviewItems(questions) {
    const container = document.getElementById('review-items-container');
    if (!container) return;

    let filtered = questions.filter((q) => {
      const userAns = state.answers[q.id];
      const qAns = getQuestionAnswer(q);
      const qPts = getQuestionPoints(q);
      const qExp = getQuestionExplanation(q);
      const isTkp = q.category === 'TKP';
      const isCorrect = isTkp ? (userAns && qPts && qPts[userAns] === 5) : (userAns === qAns);
      const isDoubt = state.doubts.has(q.id);

      if (state.reviewFilter === 'wrong' && isCorrect) return false;
      if (state.reviewFilter === 'correct' && !isCorrect) return false;
      if (state.reviewFilter === 'doubt' && !isDoubt) return false;

      if (state.reviewSearchQuery) {
        const textToMatch = `${q.question} ${q.instansi || ''} ${q.category} ${q.subcategory || ''} ${qExp}`.toLowerCase();
        if (!textToMatch.includes(state.reviewSearchQuery)) return false;
      }

      return true;
    });

    if (filtered.length === 0) {
      container.innerHTML = `<div style="text-align:center; padding:30px; color:#94a3b8;">Tidak ada soal yang sesuai dengan filter atau kata kunci pencarian.</div>`;
      return;
    }

    let html = '';
    filtered.forEach((q) => {
      const origIdx = questions.findIndex((item) => item.id === q.id);
      const userAns = state.answers[q.id];
      const qAns = getQuestionAnswer(q);
      const qPts = getQuestionPoints(q);
      const qExp = getQuestionExplanation(q);
      const isTkp = q.category === 'TKP';
      const isCorrect = isTkp ? (userAns && qPts && qPts[userAns] === 5) : (userAns === qAns);

      const itemClass = isCorrect ? 'is-correct' : 'is-wrong';

      html += `
        <div class="review-item ${itemClass}">
          <div style="display:flex; justify-content:space-between; margin-bottom: 8px; flex-wrap:wrap; gap:6px;">
            <span style="font-weight:700; font-size:0.95rem; color:var(--primary);">
              No. ${origIdx + 1} - [${q.instansi || 'Nasional'}] ${q.category} (${q.subcategory || ''})
            </span>
            <span style="font-weight:700; font-size:0.85rem; color: ${isCorrect ? 'var(--success)' : 'var(--danger)'};">
              ${isCorrect ? '✓ Benar / Poin 5' : '✕ ' + (userAns ? 'Kurang Tepat' : 'Tidak Dijawab')}
            </span>
          </div>

          <p style="font-size: 0.95rem; line-height: 1.6; margin-bottom: 12px; white-space: pre-line;">${q.question}</p>

          <div style="font-size: 0.85rem; margin-bottom: 10px;">
            <div style="margin-bottom: 4px;">
              <strong>Jawaban Anda:</strong> 
              <span style="color: ${isCorrect ? 'var(--success)' : 'var(--danger)'}; font-weight:700;">
                ${userAns ? `${userAns}. ${q.options[userAns]}` : '(Tidak menjawab)'}
                ${isTkp && userAns && qPts ? ` (Poin: ${qPts[userAns]})` : ''}
              </span>
            </div>
            <div>
              <strong>Kunci Jawaban Terbaik:</strong> 
              <span style="color: var(--success); font-weight:700;">
                ${qAns ? `${qAns}. ${q.options[qAns]}` : '(Cek rincian poin opsi)'}
              </span>
            </div>
          </div>

          <div class="review-explanation">
            <strong>Pembahasan:</strong><br>
            ${qExp || 'Belum ada penjelasan tambahan.'}
          </div>
        </div>
      `;
    });

    container.innerHTML = html;
  }

  // ==========================================
  // MANAJEMEN RIWAYAT (HISTORY & ANALYTICS)
  // ==========================================
  function getHistory() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY_HISTORY);
      return raw ? JSON.parse(raw) : [];
    } catch (e) {
      return [];
    }
  }

  function saveExamToHistory(record) {
    const history = getHistory();
    history.unshift(record);
    localStorage.setItem(STORAGE_KEY_HISTORY, JSON.stringify(history));
  }

  function renderHistoryDashboard() {
    const history = getHistory();

    const total = history.length;
    el.statTotalExams.textContent = total;

    if (total === 0) {
      el.statAvgScore.textContent = '0';
      el.statPassRate.textContent = '0%';
      el.statHighestScore.textContent = '0';
      el.historyTableBody.innerHTML = `<tr><td colspan="7" style="text-align:center; color:#94a3b8; padding: 24px;">Belum ada riwayat pengerjaan ujian.</td></tr>`;
      return;
    }

    const totalScoreSum = history.reduce((acc, h) => acc + (typeof h.total === 'number' ? h.total : 0), 0);
    const avgScore = Math.round(totalScoreSum / total);
    const highestScore = Math.max(...history.map((h) => (typeof h.total === 'number' ? h.total : 0)));
    const passedCount = history.filter((h) => h.passed).length;
    const passRate = Math.round((passedCount / total) * 100);

    el.statAvgScore.textContent = avgScore;
    el.statHighestScore.textContent = highestScore;
    el.statPassRate.textContent = `${passRate}%`;

    let rowsHtml = '';
    history.forEach((item) => {
      rowsHtml += `
        <tr>
          <td>${item.date}</td>
          <td><strong>${item.packet}</strong></td>
          <td>${item.twk}</td>
          <td>${item.tiu}</td>
          <td>${item.tkp}</td>
          <td><strong style="color:var(--primary);">${item.total}</strong></td>
          <td>
            <span style="font-weight:700; color:${item.passed ? 'var(--success)' : 'var(--danger)'};">
              ${item.passed ? '✓ Lolos' : '✕ Belum Lolos'}
            </span>
          </td>
        </tr>
      `;
    });

    el.historyTableBody.innerHTML = rowsHtml;
  }

  el.btnClearHistory.addEventListener('click', () => {
    if (confirm('Apakah Anda yakin ingin menghapus seluruh riwayat pengerjaan ujian?')) {
      localStorage.removeItem(STORAGE_KEY_HISTORY);
      renderHistoryDashboard();
    }
  });

  // ==========================================
  // MANAJEMEN BANK SOAL (CRUD, IMPORT & EXPORT)
  // ==========================================
  function loadCustomQuestionsIntoBank() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY_CUSTOM_QUESTIONS);
      if (!raw) return;
      const customList = JSON.parse(raw);

      customList.forEach((q) => {
        const targetPacket = q.targetPacket || 'skd';
        if (window.BANK_SOAL && window.BANK_SOAL[targetPacket]) {
          const exists = window.BANK_SOAL[targetPacket].questions.some((existing) => existing.id === q.id);
          if (!exists) {
            window.BANK_SOAL[targetPacket].questions.push(q);
          }
        }
      });
    } catch (e) {
      console.warn('Gagal memuat soal kustom:', e);
    }
  }

  function renderBankSummary() {
    if (!window.BANK_SOAL) return;
    
    let html = '';
    let grandTotal = 0;

    Object.keys(window.BANK_SOAL).forEach((key) => {
      const p = window.BANK_SOAL[key];
      const count = p.questions ? p.questions.length : 0;
      grandTotal += count;
      html += `<li><strong>[${p.instansi || 'Nasional'}] ${p.title}:</strong> ${count} Soal</li>`;
    });

    html += `<li style="margin-top:8px; border-top:1px dashed #cbd5e1; padding-top:6px;"><strong>Total Keseluruhan Bank Soal:</strong> ${grandTotal} Soal</li>`;
    el.bankSummaryList.innerHTML = html;
  }

  function setupAddQuestionModal() {
    el.btnOpenAddModal.addEventListener('click', () => {
      el.formAddQuestion.reset();
      toggleTkpAnswerInputs();
      el.modalAddQuestion.style.display = 'flex';
    });

    el.btnCancelAddQ.addEventListener('click', () => {
      el.modalAddQuestion.style.display = 'none';
    });

    el.inputCategory.addEventListener('change', toggleTkpAnswerInputs);

    function toggleTkpAnswerInputs() {
      const isTkp = el.inputCategory.value === 'TKP';
      el.sectionAnswerStandard.style.display = isTkp ? 'none' : 'block';
      el.sectionAnswerTkp.style.display = isTkp ? 'block' : 'none';
    }

    el.formAddQuestion.addEventListener('submit', (e) => {
      e.preventDefault();
      const targetPacket = el.inputTargetPacket.value;
      const category = el.inputCategory.value;
      const isTkp = category === 'TKP';

      const targetData = window.BANK_SOAL[targetPacket];
      const instansi = targetData ? targetData.instansi : 'Umum';

      const newQ = {
        id: `custom_${Date.now()}`,
        targetPacket: targetPacket,
        instansi: instansi,
        category: category,
        subcategory: el.inputSubcategory.value.trim() || 'Umum',
        question: el.inputQuestionText.value.trim(),
        options: {
          A: el.inputOptA.value.trim(),
          B: el.inputOptB.value.trim(),
          C: el.inputOptC.value.trim(),
          D: el.inputOptD.value.trim(),
          E: el.inputOptE.value.trim()
        },
        answer: isTkp ? 'A' : el.inputCorrectOpt.value,
        points: isTkp ? {
          A: parseInt(el.tkpPtsA.value) || 5,
          B: parseInt(el.tkpPtsB.value) || 4,
          C: parseInt(el.tkpPtsC.value) || 3,
          D: parseInt(el.tkpPtsD.value) || 2,
          E: parseInt(el.tkpPtsE.value) || 1
        } : {
          A: el.inputCorrectOpt.value === 'A' ? 5 : 0,
          B: el.inputCorrectOpt.value === 'B' ? 5 : 0,
          C: el.inputCorrectOpt.value === 'C' ? 5 : 0,
          D: el.inputCorrectOpt.value === 'D' ? 5 : 0,
          E: el.inputCorrectOpt.value === 'E' ? 5 : 0
        },
        explanation: el.inputExplanation.value.trim()
      };

      // Simpan ke memory aktif dengan enkripsi proteksi
      if (window.BANK_SOAL && window.BANK_SOAL[targetPacket]) {
        protectBankSoal({ temp: { questions: [newQ] } });
        window.BANK_SOAL[targetPacket].questions.push(newQ);
      }

      // Simpan ke LocalStorage agar permanen
      try {
        const raw = localStorage.getItem(STORAGE_KEY_CUSTOM_QUESTIONS);
        const list = raw ? JSON.parse(raw) : [];
        list.push(newQ);
        localStorage.setItem(STORAGE_KEY_CUSTOM_QUESTIONS, JSON.stringify(list));
      } catch (err) {
        console.error(err);
      }

      el.modalAddQuestion.style.display = 'none';
      renderBankSummary();
      alert('Soal baru berhasil ditambahkan ke bank soal!');
    });
  }

  function setupImportExport() {
    // Ekspor JSON (Didecode ke format standar terbuka untuk backup)
    el.btnExportJson.addEventListener('click', () => {
      const exportData = JSON.parse(JSON.stringify(window.BANK_SOAL));
      Object.keys(exportData).forEach((k) => {
        const pkt = exportData[k];
        if (pkt && Array.isArray(pkt.questions)) {
          pkt.questions.forEach((q) => {
            q.answer = getQuestionAnswer(q);
            q.explanation = getQuestionExplanation(q);
            q.points = getQuestionPoints(q);
            delete q._secAns;
            delete q._secExp;
            delete q._secPts;
          });
        }
      });

      const dataStr = 'data:text/json;charset=utf-8,' + encodeURIComponent(JSON.stringify(exportData, null, 2));
      const downloadAnchor = document.createElement('a');
      downloadAnchor.setAttribute('href', dataStr);
      downloadAnchor.setAttribute('download', `bank_soal_multi_instansi_${Date.now()}.json`);
      document.body.appendChild(downloadAnchor);
      downloadAnchor.click();
      downloadAnchor.remove();
    });

    // Impor JSON (Otomatis diamankan kembali)
    el.inputImportJson.addEventListener('change', (e) => {
      const file = e.target.files[0];
      if (!file) return;

      const reader = new FileReader();
      reader.onload = (event) => {
        try {
          const imported = JSON.parse(event.target.result);
          if (imported && typeof imported === 'object') {
            protectBankSoal(imported);
            Object.assign(window.BANK_SOAL, imported);
            renderBankSummary();
            alert('Bank soal multi-instansi berhasil diimpor!');
          } else {
            alert('Format file JSON tidak sesuai struktur bank soal.');
          }
        } catch (err) {
          alert('Gagal membaca file JSON: ' + err.message);
        }
      };
      reader.readAsText(file);
    });
  }

  // Mulai saat DOM siap
  document.addEventListener('DOMContentLoaded', init);
})();
