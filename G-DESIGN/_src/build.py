#!/usr/bin/env python3
"""Assemble the 3 V1 boards (standalone HTML) for Dispatch. Output only; boards need no build to open."""
import sys, pathlib

OUT = pathlib.Path(sys.argv[1])

BASE_CSS = r"""
*{box-sizing:border-box;margin:0;padding:0}
html,body{background:var(--board-bg);color:var(--board-ink)}
body{width:1440px;margin:0 auto;font-family:var(--sans);-webkit-font-smoothing:antialiased}
button{font:inherit;color:inherit;background:none;border:0;cursor:pointer}
.sheet{height:900px;padding:26px 48px 22px;display:flex;flex-direction:column;gap:18px}
.sheet-head{display:flex;justify-content:space-between;align-items:flex-end;gap:40px;border-bottom:1px solid var(--board-line);padding-bottom:16px}
.sh-k{font:500 11px/1 var(--mono);letter-spacing:.14em;text-transform:uppercase;color:var(--board-mute)}
.sh-t{font:600 26px/1.1 var(--sans);letter-spacing:-.015em;margin-top:9px}
.sh-d{font-size:13px;line-height:1.45;color:var(--board-mute);margin-top:6px;max-width:640px}
.spec{display:flex;gap:28px;align-items:flex-end}
.sw{display:flex;gap:8px}
.sw div{display:flex;flex-direction:column;gap:5px;font:500 9px/1 var(--mono);color:var(--board-mute);letter-spacing:.04em}
.sw i{width:40px;height:30px;border:1px solid var(--board-line);display:block}
.ty{display:flex;flex-direction:column;gap:4px;font-size:11px;color:var(--board-mute)}
.ty b{font:var(--ty-a);color:var(--board-ink)} .ty code{font:500 15px/1 var(--mono);color:var(--board-ink)}
.frames{display:flex;gap:40px;justify-content:center;align-items:flex-start}
.cap{font:500 10px/1 var(--mono);color:var(--board-mute);letter-spacing:.12em;text-transform:uppercase;margin-bottom:8px;display:flex;justify-content:space-between}
.scaled{position:relative;overflow:hidden;outline:1px solid var(--board-line)}
.scaled>.inner{position:absolute;top:0;left:0;transform-origin:0 0}
.notes{display:grid;grid-template-columns:repeat(4,1fr);gap:28px;border-top:1px solid var(--board-line);padding-top:14px;margin-top:auto}
.note{font-size:12px;line-height:1.45;color:var(--board-mute)}
.note b{display:block;color:var(--board-ink);font:600 10px/1 var(--mono);letter-spacing:.12em;text-transform:uppercase;margin-bottom:6px}
.note b span{color:var(--accent)}

/* ---------- Reddit-like frame, deliberately neutral (no brand) ---------- */
.dsk{width:1440px;height:900px;position:relative;background:var(--feed-bg);font-family:system-ui,sans-serif;overflow:hidden}
.topbar{height:56px;border-bottom:1px solid var(--feed-line);display:flex;align-items:center;padding:0 20px;gap:14px}
.topbar .lg{width:32px;height:32px;border-radius:50%;background:var(--feed-mute)}
.topbar .lgt{width:72px;height:12px;border-radius:6px;background:var(--feed-mute)}
.topbar .se{width:560px;height:38px;border-radius:19px;background:var(--feed-card);margin-left:330px}
.topbar .av{width:32px;height:32px;border-radius:50%;background:var(--feed-card);margin-left:auto}
.rail{position:absolute;left:0;top:56px;width:272px;bottom:0;border-right:1px solid var(--feed-line);padding:24px}
.rail i{display:block;height:10px;border-radius:5px;background:var(--feed-card);margin:0 0 22px;width:68%}
.rail i:nth-child(3n){width:48%} .rail i:nth-child(4n){width:80%}
.col{position:absolute;left:400px;top:80px;width:740px}
.pc{border-bottom:1px solid var(--feed-line);padding:18px 0 22px}
.pc i{display:block;height:10px;border-radius:5px;background:var(--feed-card);width:30%;margin-bottom:14px}
.pc i+i{height:16px;width:70%}
.pc em{display:block;height:300px;border-radius:14px;background:var(--feed-card)}
.scrim{position:absolute;inset:0;background:var(--scrim)}
.modal{position:absolute;left:240px;top:40px;width:960px;height:820px;border-radius:14px;overflow:hidden;background:var(--g-bg);box-shadow:0 24px 80px rgba(0,0,0,.45)}
.bar{height:46px;display:flex;align-items:center;gap:10px;padding:0 16px;background:var(--feed-bg);border-bottom:1px solid var(--feed-line);color:var(--feed-ink);font-size:13px}
.bar .ic{width:22px;height:22px;border-radius:50%;background:var(--feed-mute)}
.bar small{color:var(--feed-mute2);font-size:12px}
.bar .x{margin-left:auto;width:28px;height:28px;border-radius:50%;background:var(--feed-card);position:relative}
.bar .x:before,.bar .x:after{content:"";position:absolute;left:8px;top:13px;width:12px;height:1.5px;background:var(--feed-ink);transform:rotate(45deg)}
.bar .x:after{transform:rotate(-45deg)}
.dsk .wv{height:774px}
.mob{width:390px;height:844px;background:var(--feed-bg);display:flex;flex-direction:column;overflow:hidden;font-family:system-ui,sans-serif}
.sbar{height:44px;display:flex;align-items:center;justify-content:space-between;padding:0 26px 0 30px;font:600 15px/1 system-ui,sans-serif;color:var(--feed-ink)}
.sbar span+span{width:64px;height:11px;border-radius:3px;background:var(--feed-mute)}
.mob .bar{border-top:0}
.mob .bar .x{margin-left:0}
.mob .wv{flex:1}
.wv{container-type:inline-size;position:relative;overflow:hidden}
.game{height:100%}
"""

COMMON_JS = r"""
const D={
  date:'09 Dec',clock:'01:42',streak:6,
  trains:[['express','EXP'],['freight','FRT'],['local','LOC'],['overnight','OVN'],['shuttle','SHT']],
  assign:['express',null,'local','overnight',null], active:'freight', hover:1,
  orders:['The express sits on platform 1.','The overnight sits on platform 4.','The local sits on platform 3.','The local and the freight share adjacent platforms.']
};
D.placed=D.assign.filter(Boolean).length;
const code=id=>D.trains.find(t=>t[0]===id)[1];
const pad=n=>String(n).padStart(2,'0');
function chips(){return D.trains.map(([id,c])=>{const p=D.assign.indexOf(id);const placed=p>-1;const act=id===D.active;
  return `<button class="chip${placed?' is-placed':''}${act?' is-active':''}"><span class="c-code">${c}</span><span class="c-name">${id}</span><span class="c-pl">${placed?'P'+(p+1):act?'Selected':'Waiting'}</span></button>`}).join('')}
function orders(){return D.orders.map((o,i)=>`<li><span class="o-n">${pad(i+1)}</span><span class="o-t">${o}</span></li>`).join('')}
function gameHTML(){return `
<div class="game">
  <header class="g-head">
    <div class="brand">Dispatch<small>${LABEL.sub}</small></div>
    <div class="meta">
      <div class="m"><i>Station</i><b>${D.date}</b></div>
      <div class="m"><i>Clock</i><b>${D.clock}</b></div>
      <div class="m m-s"><i>Streak</i><b>${D.streak}</b></div>
    </div>
  </header>
  <p class="rule">Pick a train, then tap its platform. Every order must hold.</p>
  <div class="body">
    <section class="yard">${yard()}</section>
    <div class="side">
      <section class="queue"><h3>${LABEL.queue}</h3><div class="chips">${chips()}</div></section>
      <section class="orders"><h3>${LABEL.orders} <span>${pad(D.orders.length)}</span></h3><ol>${orders()}</ol></section>
    </div>
  </div>
  <button class="cta" disabled style="--p:${D.placed/5}"><span>Clear the signals</span><span class="cta-n">${cta()}</span></button>
</div>`}
function feed(){return `<div class="topbar"><span class="lg"></span><span class="lgt"></span><span class="se"></span><span class="av"></span></div>
<div class="rail">${'<i></i>'.repeat(14)}</div><div class="col">${'<div class="pc"><i></i><i></i><em></em></div>'.repeat(2)}</div>`}
const barHTML=`<span class="ic"></span><span>r/gameday_dispatch</span><small>· Dispatch · 09 Dec</small><span class="x"></span>`;
document.getElementById('dsk').innerHTML=`<div class="dsk">${feed()}<div class="scrim"></div><div class="modal"><div class="bar">${barHTML}</div><div class="wv">${gameHTML()}</div></div></div>`;
document.getElementById('mob').innerHTML=`<div class="mob"><div class="sbar"><span>9:41</span><span></span></div><div class="bar"><span class="x"></span><span>r/gameday_dispatch</span><small>· Dispatch</small></div><div class="wv">${gameHTML()}</div></div>`;
"""

PAGE = r"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=1440">
<title>Dispatch · V1 · __NUM__ __NAME__</title>
<style>
:root{--sans:ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
--mono:ui-monospace,"SF Mono","JetBrains Mono",Menlo,Consolas,"DejaVu Sans Mono","Liberation Mono",monospace;}
__BASE__
__CSS__
</style></head>
<body>
<div class="sheet">
  <div class="sheet-head">
    <div>
      <div class="sh-k">Dispatch · Planche V1 · __NUM__ / 03 · Page principale « Jeu » · 2026-11-18</div>
      <div class="sh-t">__NUM__ — __NAME__</div>
      <div class="sh-d">__DESC__</div>
    </div>
    <div class="spec">
      <div class="sw">__SWATCHES__</div>
      <div class="ty"><b>Dispatch</b><code>01:42 · P3</code><span>__TYPE__</span></div>
    </div>
  </div>
  <div class="frames">
    <div><div class="cap"><span>Desktop · 1440 × 900 · vue étendue</span><span>× 0.62</span></div>
      <div class="scaled" style="width:893px;height:558px"><div class="inner" id="dsk" style="transform:scale(.62)"></div></div></div>
    <div><div class="cap"><span>Mobile · 390 × 844</span><span>× 0.661</span></div>
      <div class="scaled" style="width:258px;height:558px"><div class="inner" id="mob" style="transform:scale(.6611)"></div></div></div>
  </div>
  <div class="notes">__NOTES__</div>
</div>
<script>
__YARD__
__COMMON__
</script>
</body></html>
"""

def swatches(items):
    return "".join(f'<div><i style="background:{h}"></i>{n}<br>{h}</div>' for n, h in items)

def notes(items):
    return "".join(f'<div class="note"><b><span>{i+1:02d}</span> · {t}</b>{d}</div>' for i, (t, d) in enumerate(items))

# =====================================================================
# 01 — CONTROL ROOM
# =====================================================================
D1 = dict(num="01", name="Control Room",
 desc="La direction de départ, tenue serrée. Nuit bleue, un seul vert signal, le schéma de voies en héros : l'entrée à gauche, cinq aiguillages qui s'allument quand un quai est occupé. Filets 1 px et étiquettes mono (Baseten), la donnée au centre (Cron).",
 type="Sans pour les titres · mono pour quais, horaires, codes",
 swatches=[("Nuit","#0e1626"),("Panneau","#132036"),("Rail","#3b4a63"),("Signal","#34d399"),("Attente","#f5b942")],
 notes=[("Sélection","Le train choisi (FRT) attend sur la voie d'entrée, contour vert pulsé. Les trains placés passent en grisé avec leur quai."),
        ("Survol du quai 2","L'itinéraire se dessine en pointillé ambre depuis l'entrée : on voit où le train va avant de toucher."),
        ("Quai occupé","L'aiguillage et le feu restent allumés en vert. C'est une information de placement, pas une validation des ordres."),
        ("Envoi","Bouton inactif tant que 3/5 ; la jauge interne montre la progression. À 5/5 il passe en aplat vert.")],
 css=r"""
:root{--board-bg:#0a101c;--board-ink:#e6edf7;--board-mute:#7f8ca3;--board-line:#1e2a40;--accent:#34d399;--ty-a:600 22px/1 var(--sans);
--feed-bg:#0e1113;--feed-card:#1d2226;--feed-line:#24292d;--feed-mute:#3a4146;--feed-mute2:#7d878d;--feed-ink:#d7dadc;--scrim:rgba(0,0,0,.6);
--g-bg:#0e1626;--panel:#132036;--rail:#3b4a63;--line:#1f2c44;--ink:#e6edf7;--mute:#8593ab;--sig:#34d399;--warn:#f5b942}
.game{background:var(--g-bg);color:var(--ink);display:flex;flex-direction:column;gap:12px;padding:14px 16px 16px;font-family:var(--sans)}
.g-head{display:flex;justify-content:space-between;align-items:flex-start;border-bottom:1px solid var(--line);padding-bottom:10px}
.brand{font:650 19px/1 var(--sans);letter-spacing:-.01em}
.brand small{display:block;font:500 9px/1 var(--mono);letter-spacing:.16em;text-transform:uppercase;color:var(--mute);margin-top:6px}
.meta{display:flex;gap:16px}
.m{display:flex;flex-direction:column;align-items:flex-end;gap:4px}
.m i{font:500 8.5px/1 var(--mono);font-style:normal;letter-spacing:.16em;text-transform:uppercase;color:var(--mute)}
.m b{font:600 15px/1 var(--mono);letter-spacing:.02em}
.m-s b{color:var(--sig)}
.rule{font-size:13px;line-height:1.35;color:var(--mute)}
.body{display:flex;flex-direction:column;gap:12px;flex:1;min-height:0}
.side{display:flex;flex-direction:column;gap:12px}
.yard{border:1px solid var(--line);background:
 linear-gradient(var(--line) 1px,transparent 1px) 0 0/100% 20px,
 linear-gradient(90deg,var(--line) 1px,transparent 1px) 0 0/20px 100%,var(--g-bg);
 background-blend-mode:normal;position:relative}
.yard:after{content:"";position:absolute;inset:0;background:rgba(14,22,38,.72);pointer-events:none}
.yard svg{display:block;width:100%;height:auto;position:relative;z-index:1}
h3{font:500 9px/1 var(--mono);letter-spacing:.16em;text-transform:uppercase;color:var(--mute);margin-bottom:8px;display:flex;justify-content:space-between}
h3 span{color:var(--ink)}
.chips{display:grid;grid-template-columns:repeat(5,1fr);border:1px solid var(--line)}
.chip{display:flex;flex-direction:column;gap:3px;align-items:flex-start;padding:8px 7px;text-align:left;border-right:1px solid var(--line);position:relative}
.chip:last-child{border-right:0}
.c-code{font:650 13px/1 var(--mono);letter-spacing:.04em}
.c-name{font-size:10px;color:var(--mute);text-transform:capitalize}
.c-pl{font:500 8px/1 var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--mute);margin-top:3px}
.chip.is-placed .c-code,.chip.is-placed .c-name{opacity:.4}
.chip.is-placed .c-pl{color:var(--sig)}
.chip.is-active{background:rgba(52,211,153,.08);box-shadow:inset 0 0 0 1px var(--sig)}
.chip.is-active .c-code,.chip.is-active .c-pl{color:var(--sig)}
.orders ol{list-style:none;border-top:1px solid var(--line)}
.orders li{display:flex;gap:10px;padding:7px 0;border-bottom:1px solid var(--line);font-size:12.5px;line-height:1.35}
.o-n{font:500 10px/1.6 var(--mono);color:var(--mute)}
.cta{margin-top:auto;height:46px;display:flex;justify-content:space-between;align-items:center;padding:0 16px;border:1px solid var(--rail);color:var(--mute);font:600 13px/1 var(--sans);letter-spacing:.02em;position:relative;overflow:hidden;cursor:not-allowed}
.cta:before{content:"";position:absolute;left:0;top:0;bottom:0;width:calc(var(--p)*100%);background:rgba(52,211,153,.10);border-right:1px solid rgba(52,211,153,.5)}
.cta span{position:relative}
.cta-n{font:600 13px/1 var(--mono);color:var(--ink)}
/* svg */
.t-rail{stroke:var(--rail);stroke-width:2;fill:none}
.t-lit{stroke:var(--sig);stroke-width:2;fill:none}
.t-route{stroke:var(--warn);stroke-width:2;fill:none;stroke-dasharray:5 4;animation:dash 1s linear infinite}
@keyframes dash{to{stroke-dashoffset:-18}}
.pl{font:500 9px var(--mono);fill:var(--mute);letter-spacing:.08em}
.car{fill:#1a2a46;stroke:#4a5d7d;stroke-width:1}
.car-t{font:650 10px var(--mono);fill:var(--ink);letter-spacing:.05em}
.car-n{font:400 9px var(--sans);fill:var(--mute)}
.slot{fill:none;stroke:var(--rail);stroke-width:1;stroke-dasharray:3 3}
.slot-t{font:500 8.5px var(--mono);fill:var(--mute);letter-spacing:.14em}
.slot.hov{stroke:var(--warn)} .slot-t.hov{fill:var(--warn)}
.sig-on{fill:var(--sig)} .sig-off{fill:var(--rail)} .sig-wait{fill:var(--warn)}
.halo{fill:none;stroke:var(--sig);stroke-width:1;opacity:.6;animation:halo 1.6s ease-out infinite;transform-box:fill-box;transform-origin:center}
@keyframes halo{from{opacity:.7;transform:scale(1)}to{opacity:0;transform:scale(1.25,1.6)}}
.act{fill:var(--g-bg);stroke:var(--sig);stroke-width:1.5}
.act-t{font:650 10px var(--mono);fill:var(--sig);letter-spacing:.05em}
.lead-t{font:500 7.5px var(--mono);fill:var(--mute);letter-spacing:.14em}
@container (min-width:600px){
 .game{padding:26px 32px 28px;gap:18px}
 .brand{font-size:26px} .m b{font-size:24px} .meta{gap:28px} .m i{font-size:9.5px}
 .rule{font-size:14px}
 .body{display:grid;grid-template-columns:1.5fr 1fr;gap:24px}
 .side{gap:22px}
 .chips{grid-template-columns:1fr}
 .chip{flex-direction:row;align-items:center;gap:10px;border-right:0;border-bottom:1px solid var(--line);padding:9px 12px}
 .chip:last-child{border-bottom:0}
 .c-code{width:38px} .c-name{font-size:12px;flex:1} .c-pl{margin:0}
 .orders li{font-size:13.5px;padding:9px 0}
 .yard{display:flex;align-items:center}
 .cta{height:54px;font-size:15px}
}
""",
 yard=r"""
const LABEL={sub:'Station control',queue:'Approaching',orders:'Orders'};
function cta(){return `${D.placed}/5`}
function yard(){
  const W=360,H=216,lead=110,sx=62,tx=132;let s='';
  s+=`<line class="t-rail" x1="0" y1="${lead}" x2="${sx}" y2="${lead}"/>`;
  s+=`<text class="lead-t" x="2" y="${lead+24}">ENTRY</text>`;
  D.assign.forEach((t,i)=>{const y=28+i*40;const cls=t?'t-lit':(i===D.hover?'t-route':'t-rail');
    s+=`<path class="${cls}" d="M${sx} ${lead} C ${sx+40} ${lead}, ${tx-36} ${y}, ${tx} ${y}"/>`;
    s+=`<line class="${t?'t-lit':'t-rail'}" x1="${tx}" y1="${y}" x2="${W-4}" y2="${y}"/>`;
    s+=`<text class="pl" x="${tx+4}" y="${y-7}">P${i+1}</text>`;
    s+=`<circle class="${t?'sig-on':i===D.hover?'sig-wait':'sig-off'}" cx="${W-10}" cy="${y-8}" r="3"/>`;
    const bx=168,bw=150;
    if(t){s+=`<rect class="car" x="${bx}" y="${y-10}" width="${bw}" height="20" rx="2"/><text class="car-t" x="${bx+9}" y="${y+3.5}">${code(t)}</text><text class="car-n" x="${bx+40}" y="${y+3.5}">${t}</text>`}
    else{const h=i===D.hover?' hov':'';s+=`<rect class="slot${h}" x="${bx}" y="${y-10}" width="${bw}" height="20" rx="2"/><text class="slot-t${h}" x="${bx+bw/2}" y="${y+3}" text-anchor="middle">${h?'ROUTE '+code(D.active)+' HERE':'OPEN'}</text>`}
  });
  s+=`<rect class="halo" x="6" y="${lead-10}" width="44" height="20" rx="2"/><rect class="act" x="6" y="${lead-10}" width="44" height="20" rx="2"/><text class="act-t" x="28" y="${lead+3.5}" text-anchor="middle">${code(D.active)}</text>`;
  return `<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="Track schematic">${s}</svg>`;
}
""")

# =====================================================================
# 02 — DEPARTURE BOARD
# =====================================================================
D2 = dict(num="02", name="Departure Board",
 desc="Le tableau des départs devient le terrain de jeu : chaque quai est une ligne, chaque train s'y affiche en lettres à volets. Noir chaud et ambre (le « maintenant » de Cron), tout en mono, la tension d'un hall de gare la nuit. Lisible en 5 s parce que tout le monde sait lire un tableau.",
 type="Mono partout · sans seulement pour le texte des ordres",
 swatches=[("Hall","#15130f"),("Volet","#25221c"),("Filet","#332e25"),("Crème","#efe7d6"),("Ambre","#f2a93b")],
 notes=[("Sélection","Le prochain train (FREIGHT) est en aplat ambre dans « Next arrivals ». Les trains déjà affichés passent en grisé avec leur quai."),
        ("Survol du quai 2","La ligne 2 prévisualise FREIGHT en volets ambre estompés et le statut passe à « Tap to route »."),
        ("Quai occupé","Les volets tombent (animation de 300 ms à l'arrivée), statut « Boarded ». Aucune validation des ordres avant envoi."),
        ("Envoi","Cinq cases sous le bouton : trois remplies. À 5/5 le bouton passe en aplat ambre.")],
 css=r"""
:root{--board-bg:#0f0d0a;--board-ink:#efe7d6;--board-mute:#958b78;--board-line:#2a261f;--accent:#f2a93b;--ty-a:600 20px/1 var(--mono);
--feed-bg:#0e1113;--feed-card:#1d2226;--feed-line:#24292d;--feed-mute:#3a4146;--feed-mute2:#7d878d;--feed-ink:#d7dadc;--scrim:rgba(0,0,0,.6);
--g-bg:#15130f;--tile:#25221c;--line:#332e25;--ink:#efe7d6;--mute:#958b78;--amb:#f2a93b}
.game{background:var(--g-bg);color:var(--ink);display:flex;flex-direction:column;gap:12px;padding:14px 16px 16px;font-family:var(--mono)}
.g-head{display:flex;justify-content:space-between;align-items:center}
.brand{font:700 17px/1 var(--mono);letter-spacing:.28em;text-transform:uppercase}
.brand small{display:block;font:500 9px/1 var(--mono);letter-spacing:.18em;color:var(--mute);margin-top:6px}
.meta{display:flex;gap:6px}
.m{display:flex;flex-direction:column;align-items:center;gap:4px;background:var(--tile);padding:6px 8px 7px;min-width:52px}
.m i{font:500 7.5px/1 var(--mono);font-style:normal;letter-spacing:.18em;text-transform:uppercase;color:var(--mute)}
.m b{font:700 14px/1 var(--mono)}
.m-s b{color:var(--amb)}
.rule{font:400 13px/1.35 var(--sans);color:var(--mute)}
.body{display:flex;flex-direction:column;gap:12px;flex:1;min-height:0}
.side{display:flex;flex-direction:column;gap:12px}
.yard{border-top:2px solid var(--ink);padding-top:2px}
.bd{display:flex;flex-direction:column}
.br{display:grid;grid-template-columns:30px 1fr 74px;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid var(--line);position:relative}
.br.hd{padding:5px 0;font:500 8px/1 var(--mono);letter-spacing:.18em;text-transform:uppercase;color:var(--mute)}
.bp{font:700 20px/1 var(--mono);text-align:center}
.tiles{display:flex;gap:2px}
.tiles i{font-style:normal;width:19px;height:26px;display:flex;align-items:center;justify-content:center;background:var(--tile);font:700 14px/1 var(--mono);position:relative;text-transform:uppercase}
.tiles i:after{content:"";position:absolute;left:0;right:0;top:50%;height:1px;background:rgba(0,0,0,.55)}
.bs{font:600 8.5px/1.2 var(--mono);letter-spacing:.14em;text-transform:uppercase;color:var(--mute);text-align:right}
.br.set .bs{color:var(--ink)}
.br.hov{box-shadow:inset 3px 0 0 var(--amb);background:rgba(242,169,59,.05)}
.br.hov .bp,.br.hov .bs{color:var(--amb)}
.br.hov .tiles i{color:rgba(242,169,59,.55);animation:blink 1.2s steps(2) infinite}
@keyframes blink{50%{color:rgba(242,169,59,.25)}}
.br.open .tiles i{color:transparent}
h3{font:500 9px/1 var(--mono);letter-spacing:.18em;text-transform:uppercase;color:var(--mute);margin-bottom:8px;display:flex;justify-content:space-between}
h3 span{color:var(--ink)}
.chips{display:flex;gap:6px}
.chip{flex:1;display:flex;flex-direction:column;gap:4px;align-items:center;padding:8px 2px 7px;background:var(--tile)}
.c-code{font:700 13px/1 var(--mono);letter-spacing:.06em}
.c-name{display:none}
.c-pl{font:500 7.5px/1 var(--mono);letter-spacing:.14em;text-transform:uppercase;color:var(--mute)}
.chip.is-placed{background:transparent;box-shadow:inset 0 0 0 1px var(--line)}
.chip.is-placed .c-code{color:var(--mute);text-decoration:line-through;text-decoration-thickness:1px}
.chip.is-active{background:var(--amb);color:#15130f}
.chip.is-active .c-pl{color:#15130f}
.orders ol{list-style:none;display:flex;flex-direction:column;gap:6px}
.orders li{display:flex;gap:10px;font:400 12.5px/1.35 var(--sans)}
.o-n{font:700 10px/1.6 var(--mono);color:var(--amb)}
.cta{margin-top:auto;height:46px;display:flex;justify-content:space-between;align-items:center;padding:0 14px;box-shadow:inset 0 0 0 1px var(--line);color:var(--mute);font:700 12px/1 var(--mono);letter-spacing:.18em;text-transform:uppercase;cursor:not-allowed}
.cta-n{display:flex;gap:3px}
.cta-n i{width:10px;height:10px;background:var(--tile)}
.cta-n i.on{background:var(--amb)}
@container (min-width:600px){
 .game{padding:26px 32px 28px;gap:18px}
 .brand{font-size:24px} .m{min-width:76px;padding:9px 12px} .m b{font-size:20px} .m i{font-size:8.5px}
 .rule{font-size:14px}
 .body{display:grid;grid-template-columns:1.55fr 1fr;gap:28px}
 .side{gap:22px}
 .br{grid-template-columns:48px 1fr 100px;padding:15px 0}
 .bp{font-size:32px}
 .tiles{gap:3px} .tiles i{width:30px;height:46px;font-size:22px}
 .bs{font-size:10px}
 .chips{display:grid;grid-template-columns:repeat(5,1fr)}
 .chip{padding:12px 2px 10px} .c-code{font-size:15px}
 .orders li{font-size:13.5px}
 .cta{height:54px;font-size:13px}
 .cta-n i{width:12px;height:12px}
}
""",
 yard=r"""
const LABEL={sub:'Night departures',queue:'Next arrivals',orders:'Notices'};
function cta(){return Array.from({length:5},(_,i)=>`<i class="${i<D.placed?'on':''}"></i>`).join('')}
function tiles(word){const w=(word||'').toUpperCase().padEnd(9,' ');return `<span class="tiles">${[...w].map(c=>`<i>${c===' '?'&nbsp;':c}</i>`).join('')}</span>`}
function yard(){
  let s=`<div class="bd"><div class="br hd"><span>Plat</span><span>Train</span><span style="text-align:right">Status</span></div>`;
  D.assign.forEach((t,i)=>{const hov=!t&&i===D.hover;const cls=t?'set':hov?'hov':'open';
    s+=`<div class="br ${cls}"><span class="bp">${i+1}</span>${tiles(t||(hov?D.active:''))}<span class="bs">${t?'Boarded':hov?'Tap to<br>route':'Open'}</span></div>`});
  return s+`</div>`;
}
""")

# =====================================================================
# 03 — SIGNAL PLAN (light, off-direction)
# =====================================================================
D3 = dict(num="03", name="Signal Plan",
 desc="L'écart assumé : un plan de voies imprimé, clair, comme un dessin d'ingénieur posé sur la table. Papier, encre, un seul rouge signal. Dans un feed sombre, c'est le post qui ressort ; les voies verticales se lisent comme des quais vus d'en haut et tombent naturellement sous le pouce en mobile.",
 type="Sans serré pour les titres · mono pour cotes, quais, codes",
 swatches=[("Papier","#f1eee6"),("Calque","#e7e2d6"),("Trait","#cbc4b4"),("Encre","#1c2128"),("Signal","#d4402b")],
 notes=[("Sélection","Le train choisi (FRT) est posé en rouge au pied de l'éventail d'aiguillages. Les étiquettes des trains placés passent à l'encre avec leur quai."),
        ("Survol du quai 2","L'itinéraire rouge en pointillé remonte l'aiguillage jusqu'au quai 2 ; le numéro du quai passe en rouge."),
        ("Quai occupé","Le bloc et le numéro passent à l'encre pleine, l'aiguillage reste tracé. Aucune validation des ordres avant envoi."),
        ("Envoi","Bouton au trait tant que 3/5, avec le compte en mono. À 5/5 il passe à l'encre pleine.")],
 css=r"""
:root{--board-bg:#e6e2d8;--board-ink:#1c2128;--board-mute:#6a6c6c;--board-line:#cbc4b4;--accent:#d4402b;--ty-a:750 22px/1 var(--sans);
--feed-bg:#ffffff;--feed-card:#eef0f2;--feed-line:#e3e6e8;--feed-mute:#c9cfd3;--feed-mute2:#6f7a80;--feed-ink:#1a1a1b;--scrim:rgba(0,0,0,.45);
--g-bg:#f1eee6;--paper2:#e7e2d6;--line:#cbc4b4;--ink:#1c2128;--mute:#6c6f73;--red:#d4402b}
.game{background:radial-gradient(#d5cfc1 1px,transparent 1.2px) 0 0/14px 14px,var(--g-bg);color:var(--ink);display:flex;flex-direction:column;gap:12px;padding:14px 16px 16px;font-family:var(--sans)}
.g-head{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:2px solid var(--ink);padding-bottom:9px}
.brand{font:750 22px/1 var(--sans);letter-spacing:-.03em}
.brand small{display:block;font:500 9px/1 var(--mono);letter-spacing:.14em;text-transform:uppercase;color:var(--mute);margin-top:6px}
.meta{display:flex;gap:14px}
.m{display:flex;flex-direction:column;align-items:flex-end;gap:4px}
.m i{font:500 8.5px/1 var(--mono);font-style:normal;letter-spacing:.14em;text-transform:uppercase;color:var(--mute)}
.m b{font:600 15px/1 var(--mono)}
.m-s b{color:var(--red)}
.rule{font-size:13px;line-height:1.35;color:var(--ink)}
.body{display:flex;flex-direction:column;gap:12px;flex:1;min-height:0}
.side{display:flex;flex-direction:column;gap:12px}
.yard{background:var(--g-bg);border:1px solid var(--ink);position:relative}
.yard:before,.yard:after{content:"";position:absolute;width:8px;height:8px;border:1px solid var(--ink);background:var(--g-bg)}
.yard:before{left:-5px;top:-5px} .yard:after{right:-5px;bottom:-5px}
.yard svg{display:block;width:100%;height:auto}
h3{font:600 9px/1 var(--mono);letter-spacing:.14em;text-transform:uppercase;color:var(--mute);margin-bottom:8px;display:flex;justify-content:space-between}
h3 span{color:var(--ink)}
.chips{display:flex;gap:6px}
.chip{flex:1;display:flex;flex-direction:column;gap:3px;align-items:flex-start;padding:7px 7px 7px 16px;background:var(--g-bg);border:1px solid var(--ink);border-radius:2px 8px 8px 2px;position:relative}
.chip:before{content:"";position:absolute;left:5px;top:50%;width:5px;height:5px;margin-top:-2.5px;border:1px solid var(--ink);border-radius:50%}
.c-code{font:700 12px/1 var(--mono);letter-spacing:.04em}
.c-name{font-size:9.5px;color:var(--mute);text-transform:capitalize}
.c-pl{font:500 7.5px/1 var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--mute);margin-top:2px}
.chip.is-placed{background:var(--ink);color:var(--g-bg)}
.chip.is-placed:before{border-color:var(--g-bg)}
.chip.is-placed .c-name,.chip.is-placed .c-pl{color:#b8b3a6}
.chip.is-active{background:var(--red);border-color:var(--red);color:#fff}
.chip.is-active:before{border-color:#fff}
.chip.is-active .c-name,.chip.is-active .c-pl{color:#fbd9d2}
.orders ol{list-style:none;display:flex;flex-direction:column;gap:7px}
.orders li{display:flex;gap:10px;font-size:12.5px;line-height:1.35;align-items:flex-start}
.o-n{flex:none;width:20px;height:20px;border:1px solid var(--ink);border-radius:50%;display:flex;align-items:center;justify-content:center;font:600 9px/1 var(--mono)}
.cta{margin-top:auto;height:46px;display:flex;justify-content:space-between;align-items:center;padding:0 16px;border:1.5px dashed var(--ink);color:var(--ink);font:650 13px/1 var(--sans);cursor:not-allowed;background:var(--g-bg)}
.cta-n{font:600 12px/1 var(--mono);color:var(--mute)}
/* svg */
.tr{stroke:var(--ink);stroke-width:1.5;fill:none}
.sw-off{stroke:var(--line);stroke-width:1.5;fill:none}
.sw-on{stroke:var(--ink);stroke-width:1.5;fill:none}
.sw-route{stroke:var(--red);stroke-width:2;fill:none;stroke-dasharray:5 4;animation:dash 1s linear infinite}
@keyframes dash{to{stroke-dashoffset:-18}}
.tick{stroke:var(--line);stroke-width:1}
.pn{fill:var(--g-bg);stroke:var(--ink);stroke-width:1}
.pn.on{fill:var(--ink)} .pn.hov{stroke:var(--red);stroke-width:1.5}
.pn-t{font:600 9.5px var(--mono);fill:var(--ink)}
.pn-t.on{fill:var(--g-bg)} .pn-t.hov{fill:var(--red)}
.blk{fill:var(--ink)}
.blk-t{font:700 10px var(--mono);fill:var(--g-bg);letter-spacing:.04em}
.slot{fill:rgba(241,238,230,.85);stroke:var(--ink);stroke-width:1;stroke-dasharray:3 3}
.slot.hov{stroke:var(--red);fill:rgba(212,64,43,.06)}
.slot-t{font:600 7.5px var(--mono);fill:var(--mute);letter-spacing:.12em}
.slot-t.hov{fill:var(--red)}
.dim{font:500 7px var(--mono);fill:var(--mute);letter-spacing:.1em}
.act{fill:var(--red)} .act-t{font:700 10px var(--mono);fill:#fff;letter-spacing:.04em}
.halo{fill:none;stroke:var(--red);stroke-width:1;animation:halo 1.6s ease-out infinite;transform-box:fill-box;transform-origin:center}
@keyframes halo{from{opacity:.8;transform:scale(1)}to{opacity:0;transform:scale(1.35,1.7)}}
@container (min-width:600px){
 .game{padding:26px 32px 28px;gap:18px;background-size:18px 18px}
 .brand{font-size:32px} .m b{font-size:24px} .meta{gap:28px} .m i{font-size:9.5px}
 .rule{font-size:14px}
 .body{display:grid;grid-template-columns:1.4fr 1fr;gap:28px}
 .side{gap:22px}
 .yard{display:flex;flex-direction:column;justify-content:center;padding:12px 8px}
 .chips{display:grid;grid-template-columns:1fr 1fr}
 .chip{padding:10px 10px 10px 22px} .chip:before{left:8px}
 .c-code{font-size:14px} .c-name{font-size:11px}
 .orders li{font-size:13.5px}
 .cta{height:54px;font-size:15px}
}
""",
 yard=r"""
const LABEL={sub:'Station plan · Day 09.12',queue:'Trains',orders:'Orders'};
function cta(){return `${D.placed} of 5 routed`}
function yard(){
  const W=360,H=262,top=40,bot=190,throat=226,cx=180;let s='';
  const xs=[44,112,180,248,316];
  // cotes
  s+=`<line class="tick" x1="20" y1="${top}" x2="20" y2="${bot}"/>`;
  for(let y=top;y<=bot;y+=15)s+=`<line class="tick" x1="17" y1="${y}" x2="23" y2="${y}"/>`;
  D.assign.forEach((t,i)=>{const x=xs[i];const hov=!t&&i===D.hover;
    s+=`<path class="${t?'sw-on':hov?'sw-route':'sw-off'}" d="M${cx} ${throat} L${cx} ${throat-6} L${x} ${bot+14} L${x} ${bot}"/>`;
    s+=`<line class="tr" x1="${x}" y1="${top}" x2="${x}" y2="${bot}"/>`;
    for(let y=top+8;y<bot;y+=12)s+=`<line class="tick" x1="${x-5}" y1="${y}" x2="${x+5}" y2="${y}"/>`;
    s+=`<circle class="pn${t?' on':hov?' hov':''}" cx="${x}" cy="20" r="10"/><text class="pn-t${t?' on':hov?' hov':''}" x="${x}" y="23.5" text-anchor="middle">${i+1}</text>`;
    if(t){s+=`<rect class="blk" x="${x-17}" y="${top+18}" width="34" height="112" rx="3"/><text class="blk-t" x="${x}" y="${top+78}" text-anchor="middle">${code(t)}</text>`}
    else{const h=hov?' hov':'';s+=`<rect class="slot${h}" x="${x-17}" y="${top+18}" width="34" height="112" rx="3"/><text class="slot-t${h}" x="${x}" y="${top+78}" text-anchor="middle">${hov?code(D.active):'OPEN'}</text>`}
  });
  s+=`<line class="tr" x1="${cx}" y1="${throat}" x2="${cx}" y2="${H}"/>`;
  s+=`<rect class="halo" x="${cx-20}" y="${throat+6}" width="40" height="18" rx="2"/><rect class="act" x="${cx-20}" y="${throat+6}" width="40" height="18" rx="2"/><text class="act-t" x="${cx}" y="${throat+18.5}" text-anchor="middle">${code(D.active)}</text>`;
  s+=`<text class="dim" x="${cx+28}" y="${throat+18}">ENTRY</text>`;
  return `<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="Station plan">${s}</svg>`;
}
""")

for d, slug in [(D1, "control-room"), (D2, "departure-board"), (D3, "signal-plan")]:
    html = (PAGE.replace("__BASE__", BASE_CSS).replace("__CSS__", d["css"]).replace("__YARD__", d["yard"])
            .replace("__COMMON__", COMMON_JS).replace("__NUM__", d["num"]).replace("__NAME__", d["name"])
            .replace("__DESC__", d["desc"]).replace("__TYPE__", d["type"])
            .replace("__SWATCHES__", swatches(d["swatches"])).replace("__NOTES__", notes(d["notes"])))
    (OUT / f"{d['num']}-{slug}.html").write_text(html, encoding="utf-8")
    print("wrote", d["num"], slug, len(html))
