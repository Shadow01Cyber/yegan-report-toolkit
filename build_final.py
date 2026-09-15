#!/usr/bin/env python3
"""
Build script — Generates index.html from reports.json
Each visitor gets a unique random report based on browser fingerprint.
"""

import json, os

# Load reports
with open("reports.json", "r", encoding="utf-8") as f:
    reports = json.load(f)

reports_json = json.dumps(reports, ensure_ascii=False)

html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Report @YeganHjAmir</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{background:#0a0a0f;color:#c9d1d9;font-family:'Courier New',monospace;min-height:100vh;overflow-x:hidden}
.bg-grid{position:fixed;top:0;left:0;width:100%;height:100%;background-image:linear-gradient(rgba(240,136,62,0.03) 1px,transparent 1px),linear-gradient(90deg,rgba(240,136,62,0.03) 1px,transparent 1px);background-size:40px 40px;z-index:0;pointer-events:none}
.scanline{position:fixed;top:0;left:0;width:100%;height:100%;background:repeating-linear-gradient(0deg,transparent,transparent 2px,rgba(240,136,62,0.008) 2px,rgba(240,136,62,0.008) 4px);pointer-events:none;z-index:3}
.container{position:relative;z-index:1;max-width:800px;margin:0 auto;padding:30px 20px}
header{text-align:center;margin-bottom:30px}
header h1{color:#f0883e;font-size:1.5em;letter-spacing:2px;text-shadow:0 0 20px rgba(240,136,62,0.3)}
header .badge{display:inline-block;background:#238636;color:#fff;padding:4px 12px;border-radius:12px;font-size:11px;margin-top:8px;animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.5}}
.info-box{background:rgba(22,27,34,0.95);border:1px solid #f0883e44;border-radius:8px;padding:20px;margin-bottom:20px}
.info-box b{color:#f0883e}
.info-box .row{margin-bottom:6px;font-size:13px}
.progress-box{background:rgba(22,27,34,0.95);border:1px solid #30363d;border-radius:8px;padding:16px;margin-bottom:20px}
.progress-box .label{font-size:12px;color:#8b949e;margin-bottom:8px}
.progress-box .label span{color:#f0883e;font-weight:bold}
.bar{height:6px;background:#21262d;border-radius:3px;overflow:hidden}
.bar .fill{height:100%;background:linear-gradient(90deg,#f0883e,#ff6b35);border-radius:3px;transition:width .5s ease}
.report-card{background:rgba(22,27,34,0.95);border:1px solid #30363d;border-radius:8px;padding:24px;margin-bottom:20px;position:relative;overflow:hidden}
.report-card::before{content:'';position:absolute;top:0;left:0;width:4px;height:100%;background:#f0883e}
.report-id{position:absolute;top:12px;right:16px;color:#30363d;font-size:11px}
.report-subject{color:#f0883e;font-size:14px;font-weight:bold;margin-bottom:16px;line-height:1.5}
.report-body{color:#8b949e;font-size:12px;line-height:1.8;white-space:pre-wrap;max-height:400px;overflow-y:auto;padding-right:8px}
.report-body::-webkit-scrollbar{width:4px}
.report-body::-webkit-scrollbar-thumb{background:#30363d;border-radius:2px}
.btn-row{display:flex;gap:10px;justify-content:center;margin:20px 0;flex-wrap:wrap}
.btn{padding:12px 28px;border-radius:6px;border:none;font-family:'Courier New',monospace;font-size:13px;font-weight:bold;cursor:pointer;transition:all .3s;letter-spacing:1px}
.btn-send{background:#238636;color:#fff}
.btn-send:hover{background:#2ea043;box-shadow:0 0 20px rgba(35,134,54,0.4)}
.btn-copy{background:#1f6feb;color:#fff}
.btn-copy:hover{background:#388bfd;box-shadow:0 0 20px rgba(31,111,235,0.4)}
.btn-next{background:transparent;border:1px solid #30363d;color:#8b949e}
.btn-next:hover{border-color:#f0883e;color:#f0883e}
.toast{position:fixed;bottom:30px;left:50%;transform:translateX(-50%);background:#238636;color:#fff;padding:10px 24px;border-radius:6px;font-size:12px;font-family:'Courier New',monospace;z-index:10;opacity:0;transition:opacity .3s;pointer-events:none}
.toast.show{opacity:1}
.footer{text-align:center;color:#21262d;font-size:10px;margin-top:40px;letter-spacing:2px}
.visitor-id{color:#30363d;font-size:10px;text-align:center;margin-top:4px}
</style>
</head>
<body>
<div class="bg-grid"></div>
<div class="scanline"></div>
<div class="container">
    <header>
        <h1>🔓 Report @YeganHjAmir</h1>
        <div class="badge">UNIQUE REPORT — VERIFIED</div>
        <div class="visitor-id" id="visitorId"></div>
    </header>

    <div class="info-box">
        <div class="row"><b>Channel:</b> @YeganHjAmir (ID: -1002800797699)</div>
        <div class="row"><b>Owner:</b> @ip_1998</div>
        <div class="row"><b>Violation:</b> Non-consensual intimate images + verbal abuse + 5k fake members</div>
        <div class="row"><b>To:</b> abuse@telegram.org, privacy@telegram.org</div>
    </div>

    <div class="progress-box">
        <div class="label">Your Report: <span id="reportNum">—</span> / ''' + str(len(reports)) + '''</div>
        <div class="bar"><div class="fill" id="progressFill" style="width:0%"></div></div>
    </div>

    <div class="report-card">
        <div class="report-id" id="reportId">#</div>
        <div class="report-subject" id="reportSubject"></div>
        <div class="report-body" id="reportBody"></div>
    </div>

    <div class="btn-row">
        <button class="btn btn-send" onclick="sendReport()">📤 Send Report</button>
        <button class="btn btn-copy" onclick="copyReport()">📋 Copy Text</button>
        <button class="btn btn-next" onclick="nextReport()">⏭ Get Different Report</button>
    </div>

    <div class="footer">PHANTOM REPORT TOOLKIT — EACH VISITOR GETS A UNIQUE REPORT</div>
</div>

<div class="toast" id="toast"></div>

<script>
const REPORTS = ''' + reports_json + ''';
const STORAGE_KEY = 'yegan_v8_';
const TO = ['abuse@telegram.org','privacy@telegram.org'];

// ─── Visitor fingerprint (unique per browser) ───
function getVisitorId() {
    let id = localStorage.getItem(STORAGE_KEY + 'vid');
    if (id) return id;
    // Generate from canvas fingerprint
    try {
        const c = document.createElement('canvas');
        const ctx = c.getContext('2d');
        ctx.textBaseline = 'top';
        ctx.font = '14px Arial';
        ctx.fillText('phantom', 2, 2);
        const canvas = c.toDataURL();
        const nav = navigator.userAgent + screen.width + screen.height + Date.now();
        let hash = 0;
        const str = canvas + nav;
        for (let i = 0; i < str.length; i++) {
            hash = ((hash << 5) - hash) + str.charCodeAt(i);
            hash |= 0;
        }
        id = Math.abs(hash).toString(36);
    } catch(e) {
        id = Math.random().toString(36).substr(2, 8);
    }
    localStorage.setItem(STORAGE_KEY + 'vid', id);
    return id;
}

// ─── Pick report based on visitor fingerprint ───
function pickReport() {
    const vid = getVisitorId();
    // Hash visitor ID to pick consistent report
    let hash = 0;
    for (let i = 0; i < vid.length; i++) {
        hash = ((hash << 5) - hash) + vid.charCodeAt(i);
        hash |= 0;
    }
    const idx = Math.abs(hash) % REPORTS.length;
    return REPORTS[idx];
}

// ─── Pick a RANDOM report (for "next" button) ───
function pickRandom() {
    const sent = JSON.parse(localStorage.getItem(STORAGE_KEY + 'sent') || '[]');
    const unsent = REPORTS.filter(r => !sent.includes(r.id));
    if (unsent.length === 0) {
        // All sent — pick any random
        return REPORTS[Math.floor(Math.random() * REPORTS.length)];
    }
    return unsent[Math.floor(Math.random() * unsent.length)];
}

let currentReport = null;

function showReport(r) {
    currentReport = r;
    document.getElementById('reportId').textContent = '#' + r.id;
    document.getElementById('reportSubject').textContent = r.subject;
    document.getElementById('reportBody').textContent = r.body;
    
    const sent = JSON.parse(localStorage.getItem(STORAGE_KEY + 'sent') || '[]');
    document.getElementById('reportNum').textContent = sent.length + 1;
    document.getElementById('progressFill').style.width = ((sent.length / REPORTS.length) * 100) + '%';
    
    // Scroll to top
    window.scrollTo({top: 0, behavior: 'smooth'});
}

function sendReport() {
    if (!currentReport) return;
    
    const subject = encodeURIComponent('Report: @YeganHjAmir — ' + currentReport.subject);
    const body = encodeURIComponent(currentReport.body);
    
    // Open mailto to both addresses
    const mailto = 'mailto:' + TO[0] + '?cc=' + TO[1] + '&subject=' + subject + '&body=' + body;
    window.open(mailto, '_blank');
    
    // Mark as sent
    const sent = JSON.parse(localStorage.getItem(STORAGE_KEY + 'sent') || '[]');
    if (!sent.includes(currentReport.id)) {
        sent.push(currentReport.id);
        localStorage.setItem(STORAGE_KEY + 'sent', JSON.stringify(sent));
    }
    
    showToast('✅ Report #' + currentReport.id + ' opened in email client');
    
    // Update progress
    document.getElementById('reportNum').textContent = sent.length;
    document.getElementById('progressFill').style.width = ((sent.length / REPORTS.length) * 100) + '%';
    
    // Auto-load next report after 2s
    setTimeout(() => nextReport(), 2000);
}

function copyReport() {
    if (!currentReport) return;
    const text = 'Subject: ' + currentReport.subject + '\\n\\n' + currentReport.body;
    navigator.clipboard.writeText(text).then(() => {
        showToast('📋 Report #' + currentReport.id + ' copied to clipboard');
    }).catch(() => {
        // Fallback
        const ta = document.createElement('textarea');
        ta.value = text;
        document.body.appendChild(ta);
        ta.select();
        document.execCommand('copy');
        document.body.removeChild(ta);
        showToast('📋 Report #' + currentReport.id + ' copied to clipboard');
    });
}

function nextReport() {
    const r = pickRandom();
    showReport(r);
}

function showToast(msg) {
    const t = document.getElementById('toast');
    t.textContent = msg;
    t.classList.add('show');
    setTimeout(() => t.classList.remove('show'), 3000);
}

// ─── Init ───
document.getElementById('visitorId').textContent = 'Visitor: ' + getVisitorId();
const initial = pickReport();
showReport(initial);
</script>
</body>
</html>'''

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print(f"✅ Built index.html with {len(reports)} reports")
print(f"   File size: {len(html):,} bytes")
