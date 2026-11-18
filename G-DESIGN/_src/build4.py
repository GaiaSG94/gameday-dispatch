#!/usr/bin/env python3
"""Step C board: 04 Series & community (% of players who cleared). Same style, reuses build3."""
import sys, pathlib
HERE = pathlib.Path(__file__).parent
b3 = (HERE / "build3.py").read_text()
ns = {"__name__": "lib", "__file__": str(HERE / "build3.py"), "sys": sys}
exec(b3.split("post = page(")[0].replace("OUT = pathlib.Path(sys.argv[1])", ""), ns)
page, JS = ns["page"], ns["JS"]
OUT = pathlib.Path(sys.argv[1])

CSS = r"""
.stats{display:flex;flex-direction:column;gap:12px;flex:1;min-height:0}
.panel{background:#fbfaf6;border:1.5px solid var(--ink);border-radius:12px;box-shadow:4px 5px 0 var(--ink);padding:14px;display:flex;flex-direction:column;gap:12px}
.panel h3{margin:0}
.pct{display:flex;align-items:flex-end;gap:10px}
.pct b{font:800 52px/.85 var(--mono);letter-spacing:-.04em;color:var(--red)}
.pct b small{font-size:.45em;letter-spacing:0}
.pct span{font:500 11px/1.35 var(--sans);color:var(--ink);padding-bottom:3px}
.pct span em{display:block;font:600 8px/1 var(--mono);font-style:normal;letter-spacing:.14em;text-transform:uppercase;color:var(--mute);margin-top:5px}
/* gauge = a stretch of track: 50 sleepers, cleared share in red */
.gauge{position:relative;height:22px;display:flex;justify-content:space-between;align-items:center;padding:0 2px}
.gauge:before,.gauge:after{content:"";position:absolute;left:0;right:0;height:1px;background:var(--ink)}
.gauge:before{top:7px}.gauge:after{bottom:7px}
.gauge i{width:2.5px;height:22px;background:var(--line);border-radius:1px}
.gauge i.on{background:var(--red)}
.gauge .you{position:absolute;top:-17px;transform:translateX(-50%);font:700 8px/1 var(--mono);letter-spacing:.12em;color:var(--red);white-space:nowrap}
.gauge .you:after{content:"";position:absolute;left:50%;top:11px;width:1.5px;height:7px;background:var(--red)}
.week{display:grid;grid-template-columns:repeat(7,1fr);gap:6px;align-items:end;height:92px}
.wk{display:flex;flex-direction:column;align-items:center;gap:5px;height:100%;justify-content:flex-end}
.wk .bar{width:100%;max-width:26px;background:var(--ink);border-radius:3px 3px 0 0;box-shadow:inset .3em .3em 0 rgba(255,255,255,.08)}
.wk.today .bar{background:var(--red)}
.wk b{font:700 9px/1 var(--mono)}
.wk.today b{color:var(--red)}
.wk span{font:600 7.5px/1 var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--mute)}
.days{display:grid;grid-template-columns:repeat(7,1fr);gap:6px}
.day{aspect-ratio:1/1.15;border:1.5px solid var(--ink);border-radius:7px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;background:var(--g-bg);position:relative}
.day b{font:700 12px/1 var(--mono)} .day span{font:600 7px/1 var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--mute)}
.day.ok{background:var(--ink);color:var(--g-bg);box-shadow:2px 2px 0 #a69e8c}
.day.ok span{color:#b8b3a6}
.day.today{background:var(--red);border-color:var(--red);color:#fff;box-shadow:2px 3px 0 var(--ink);transform:rotate(-3deg)}
.day.today span{color:#fde3dc}
.day.miss{border-style:dashed;color:var(--mute)}
.day.ok:after,.day.today:after{content:"";position:absolute;top:4px;right:4px;width:5px;height:5px;border-radius:50%;background:var(--g-bg)}
.streakhead{display:flex;justify-content:space-between;align-items:center}
.streakhead .ticket{transform:rotate(-2deg)}
.streakhead p{font:500 11px/1.4 var(--sans);color:var(--ink);max-width:56%}
.back{display:flex;gap:10px;align-items:center}
.back .btn-cap{flex:1;height:44px;color:#fff;background:linear-gradient(#2b313a,#1c2128);box-shadow:0 5px 0 #000,0 5px 0 1.5px var(--ink),0 9px 10px rgba(28,33,40,.2);cursor:pointer}
.back .btn-cap small{color:#b8b3a6}
.note-hyp{font:500 9px/1.35 var(--mono);color:var(--mute)}
@container (min-width:600px){
 .stats{display:grid;grid-template-columns:1.15fr 1fr;gap:28px;align-items:stretch}
 .back{margin-top:auto}
 .col1>.panel:last-child{flex:1}
 .stats .col2{display:flex;flex-direction:column;gap:22px}
 .panel{padding:20px 20px 18px;gap:16px}
 .pct b{font-size:84px} .pct span{font-size:14px}
 .week{height:auto;flex:1;min-height:150px} .wk b{font-size:11px} .wk span{font-size:9px}
 .day b{font-size:16px} .day span{font-size:8.5px}
 .streakhead p{font-size:13px}
 .back .btn-cap{height:52px;font-size:15px}
}
"""

STATS_JS = JS + r"""
const WEEK=[['03',71],['04',58],['05',80],['06',47],['07',66],['08',74],['09',62]];
const PLAYED=1284, CLEARED=796;
function gauge(p){const n=50,on=Math.round(p/100*n);return `<div class="gauge">${Array.from({length:n},(_,i)=>`<i class="${i<on?'on':''}"></i>`).join('')}</div>`}
function view(){
 const p=Math.round(CLEARED/PLAYED*100);
 const comm=`<section class="panel">
   <h3>Today's yard <span>09 Dec</span></h3>
   <div class="pct"><b>${p}<small>%</small></b><span>of operators cleared the station.<em>${CLEARED.toLocaleString('en-US')} of ${PLAYED.toLocaleString('en-US')} players · you are one of them</em></span></div>
   ${gauge(p)}
  </section>`;
 const week=`<section class="panel">
   <h3>Cleared, last 7 stations <span>% of players</span></h3>
   <div class="week">${WEEK.map(([d,v],i)=>`<div class="wk${i===6?' today':''}"><b>${v}</b><div class="bar" style="height:${v*0.85}%"></div><span>${i===6?'Today':d+' Dec'}</span></div>`).join('')}</div>
  </section>`;
 const mine=`<section class="panel">
   <div class="streakhead">${ticket(7)}<p>Seven stations in a row. Miss a day and the ticket starts over.</p></div>
   <h3>Your week <span>7 / 7</span></h3>
   <div class="days">${WEEK.map(([d],i)=>`<div class="day ${i===6?'today':'ok'}"><b>${d}</b><span>${i===6?'Today':'Clear'}</span></div>`).join('')}</div>
  </section>`;
 return `<div class="game">
  <header class="g-head"><div class="brand">Dispatch<small>Station board · ${D.date}</small></div>
   <div class="meta"><div class="m"><i>Next station</i><b>08:14</b></div></div></header>
  <div class="radio"><span>Control: <b>${p}% of the yard</b> got every train out today</span></div>
  <div class="stats"><div class="col1" style="display:flex;flex-direction:column;gap:inherit">${comm}${week}</div><div class="col2" style="display:flex;flex-direction:column;gap:inherit">${mine}<div class="back"><button class="btn-cap"><span>Back to the result</span><small>Close</small></button></div></div></div>
 </div>`}
const frame=(mobile)=>mobile?`<div class="mob"><div class="sbar"><span>9:41</span><span></span></div><div class="bar"><span class="x"></span><span>r/gameday_dispatch</span><small>· Dispatch</small></div><div class="wv">${view()}</div></div>`
 :`<div class="dsk">${feedTop()}<div class="col">${'<div class="pc"><i></i><i></i><em></em></div>'.repeat(2)}</div><div class="scrim"></div><div class="modal"><div class="bar">${bar}</div><div class="wv">${view()}</div></div></div>`;
document.getElementById('dsk').innerHTML=frame(false);
document.getElementById('mob').innerHTML=frame(true);
"""

h = page("Dispatch · V2 · Séries & communauté", "Planche V2 · Page 4 / 4 · Séries & communauté", "04 — Séries & communauté",
 "Le score de la communauté choisi par Gaia : le pourcentage de joueurs qui ont dégagé la gare. Il est montré comme un tronçon de voie dont les traverses rouges indiquent la part de réussite, puis sur les 7 dernières gares. À droite, la série du joueur sous forme de ticket et ses 7 derniers jours. Pas de classement au temps : ce n'est pas le score retenu.",
 STATS_JS,
 [("Score du jour","% = joueurs qui ont dégagé la gare / joueurs qui ont envoyé au moins une fois aujourd'hui. Seul chiffre en rouge, avec la jauge en traverses (part rouge = réussite)."),
  ("7 dernières gares","Une barre par jour à l'encre, aujourd'hui en rouge. Permet de dire « dure aujourd'hui » sans dévoiler la solution."),
  ("Série","Ticket à 7 perforations et une case par jour : réussi (encre), aujourd'hui (rouge, inclinée), manqué (pointillé)."),
  ("Données à ajouter","Le serveur ne stocke pas encore ces chiffres. Il faudrait deux compteurs Redis par jour (joueurs, réussites) à l'envoi. Les jours du joueur se lisent déjà via solved:user:day.")])
h = h.replace("</style>", CSS + ns["ns"]["MATERIAL"] + "\n</style>")
(OUT / "04-series.html").write_text(h, encoding="utf-8")
print("ok")
