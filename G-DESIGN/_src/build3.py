#!/usr/bin/env python3
"""Step C boards: 01 Post, 03 End card. Strict continuation of V2 Diorama (reuses its CSS + JS helpers)."""
import sys, pathlib
HERE = pathlib.Path(__file__).parent
b2 = (HERE / "build2.py").read_text()
ns = {"__name__": "lib", "__file__": str(HERE / "build2.py"), "sys": sys}
exec(b2.split("d = dict(")[0].replace("OUT = pathlib.Path(sys.argv[1])", ""), ns)
BASE_CSS, PAGE, swatches, notes, CSS2, JS2 = ns["BASE_CSS"], ns["PAGE"], ns["swatches"], ns["notes"], ns["CSS"], ns["JS"]
HELPERS = JS2.split("function feed()")[0]
OUT = pathlib.Path(sys.argv[1])

EXTRA_CSS = r"""
/* ---------- shared yard variants ---------- */
.plane.done .lamp{fill:var(--ink)} .plane.done .lamp-t{fill:var(--g-bg)}
.plane.jam .sw-jam{stroke:var(--red);stroke-width:2;fill:none;stroke-dasharray:2 3}
.plane.jam .car .top{background:linear-gradient(140deg,#4a4f57,#3a3f47)}
.xmark{fill:none;stroke:var(--red);stroke-width:2.4;stroke-linecap:round}
.wait{position:absolute;display:flex;gap:1.4cqw;left:50%;transform:translateX(-50%) translateZ(0);bottom:-1cqw}
/* ---------- feed post (Post page) ---------- */
.dsk.feedonly .col{top:72px}
.post{background:var(--feed-bg);border-bottom:1px solid var(--feed-line);padding:12px 0 14px}
.ph{display:flex;align-items:center;gap:8px;font:600 12px/1 system-ui,sans-serif;color:var(--feed-ink);margin-bottom:8px}
.ph .ic{width:24px;height:24px;border-radius:50%;background:var(--feed-mute)}
.ph small{font-weight:400;color:var(--feed-mute2)}
.pt{font:600 18px/1.25 system-ui,sans-serif;color:var(--feed-ink);margin-bottom:10px}
.inl{border-radius:16px;overflow:hidden;border:1px solid var(--feed-line);container-type:inline-size;position:relative}
.dsk .inl{height:460px}
.mob .inl{height:440px;border-radius:0;border-left:0;border-right:0}
.pa{display:flex;gap:8px;margin-top:10px}
.pa i{display:block;height:32px;border-radius:16px;background:var(--feed-card);width:92px}
.pa i:nth-child(2){width:64px}.pa i:nth-child(3){width:76px}
.mob .post{padding:12px 0 0}.mob .ph,.mob .pt{padding:0 12px}.mob .pa{padding:0 12px 12px}.mob .pt{font-size:16px}
.mob .feedtop{height:48px;border-bottom:1px solid var(--feed-line);display:flex;align-items:center;gap:10px;padding:0 14px}
.mob .feedtop i{display:block;width:28px;height:28px;border-radius:50%;background:var(--feed-mute)}
.mob .feedtop b{display:block;width:120px;height:12px;border-radius:6px;background:var(--feed-card)}
.mob .feedtop i:last-child{margin-left:auto;background:var(--feed-card)}
.mob .ghostpost{padding:14px 12px}.mob .ghostpost i{display:block;height:10px;width:40%;border-radius:5px;background:var(--feed-card);margin-bottom:10px}
.mob .ghostpost em{display:block;height:160px;border-radius:12px;background:var(--feed-card)}
/* splash */
.splash{height:100%;background:var(--g-bg);color:var(--ink);display:flex;flex-direction:column;gap:9px;padding:12px 14px 14px;font-family:var(--sans)}
.splash .g-head{align-items:flex-start}
.splash .yard{padding:1cqw 19cqw 5cqw;flex:1;display:flex;flex-direction:column;justify-content:center}
.splash .radio{font-size:10px}
.go{display:flex;flex-direction:column;align-items:stretch;gap:8px}
.go .btn-cap{flex:none}
.go .btn-cap{color:#fff;background:linear-gradient(#e2553f,#d4402b);box-shadow:0 5px 0 var(--red2),0 5px 0 1.5px var(--ink),0 9px 10px rgba(28,33,40,.2);cursor:pointer;height:44px}
.go .btn-cap small{color:#fde3dc}
.hi{text-align:center;font:500 10px/1.3 var(--mono);color:var(--mute);letter-spacing:.02em}
@container (min-width:600px){
 .splash{display:grid;grid-template-columns:1.25fr 1fr;grid-template-rows:auto 1fr auto;column-gap:26px;row-gap:12px;padding:22px 26px 24px}
 .splash .g-head{grid-column:1/-1}
 .splash .yard{grid-row:2/4;padding:1cqw 5cqw 5cqw}
 .splash .brand{font-size:40px}
 .splash .info{display:flex;flex-direction:column;gap:14px;justify-content:center}
 .splash .radio{font-size:12px}
 .splash .go{flex-direction:column;align-items:stretch}
 .splash .go .btn-cap{height:54px;font-size:16px}
 .splash .hi{font-size:11px}
}
.facts{display:flex;gap:6px}
.facts span{flex:1;border:1.5px solid var(--ink);border-radius:8px;padding:6px 8px;background:#fbfaf6;box-shadow:2px 2px 0 var(--ink);display:flex;flex-direction:column;gap:4px}
.facts i{font:600 7.5px/1 var(--mono);font-style:normal;letter-spacing:.14em;text-transform:uppercase;color:var(--mute)}
.facts b{font:800 15px/1 var(--mono)}
@container (min-width:600px){.facts b{font-size:20px}.facts i{font-size:8.5px}.facts span{padding:9px 10px}}
/* ---------- end card ---------- */
.end{position:relative;background:#fbfaf6;border:1.5px solid var(--ink);border-radius:12px;box-shadow:4px 5px 0 var(--ink);padding:16px 14px 14px;display:flex;flex-direction:column;gap:12px}
.stamp{align-self:flex-start;transform:rotate(-4deg);border:2.5px solid currentColor;border-radius:6px;padding:6px 12px 5px;font:800 22px/1 var(--sans);letter-spacing:.04em;text-transform:uppercase;color:var(--red);
 -webkit-mask:radial-gradient(circle at 30% 40%,#000 60%,rgba(0,0,0,.82) 61%) ;opacity:.95}
.end.lost .stamp{color:var(--ink)}
.end p{font-size:12.5px;line-height:1.4}
.end .facts b{font-size:18px}
.end .facts .up{color:var(--red)}
.share{display:flex;flex-direction:column;gap:8px;border-top:1px dashed var(--line);padding-top:12px}
.share h3{margin:0}
.preview{font:500 11px/1.4 var(--mono);background:var(--g-bg);border:1px solid var(--line);border-radius:6px;padding:8px 10px;color:var(--ink)}
.end .btn-cap{color:#fff;background:linear-gradient(#e2553f,#d4402b);box-shadow:0 5px 0 var(--red2),0 5px 0 1.5px var(--ink),0 9px 10px rgba(28,33,40,.2);cursor:pointer;height:44px;flex:none}
.end .btn-cap small{color:#fde3dc}
.end.lost .btn-cap{background:linear-gradient(#2b313a,#1c2128);box-shadow:0 5px 0 #000,0 5px 0 1.5px var(--ink),0 9px 10px rgba(28,33,40,.2)}
.end.lost .btn-cap small{color:#b8b3a6}
.next{display:flex;justify-content:space-between;align-items:center;font:600 9px/1 var(--mono);letter-spacing:.14em;text-transform:uppercase;color:var(--mute)}
.next b{font:700 13px/1 var(--mono);color:var(--ink);letter-spacing:.04em}
.link{font:650 12px/1 var(--sans);color:var(--ink);text-decoration:underline;text-underline-offset:3px;align-self:center;padding:4px}
.endwrap{display:flex;flex-direction:column;gap:12px;flex:1;min-height:0}
.endwrap .yard{padding:1cqw 16cqw 6cqw}
@container (min-width:600px){
 .endwrap{display:grid;grid-template-columns:1.3fr 1fr;gap:28px;align-items:center}
 .endwrap .yard{padding:2cqw 4cqw 6cqw}
 .stamp{font-size:30px}
 .end{padding:22px 20px 18px;gap:14px}
 .end p{font-size:14px}
 .end .facts b{font-size:24px}
 .preview{font-size:12px}
 .end .btn-cap{height:52px}
}
.f3{display:flex;gap:28px;justify-content:center;align-items:flex-start}
"""

JS = HELPERS + r"""
const SOL=['express','freight','local','overnight','shuttle'];
const BAD=['express','shuttle','local','overnight','freight'];
function yardState(assign,mode){
 let s='';
 X.forEach((x,i)=>{const t=assign[i];
  for(let y=TOP+4;y<BOT;y+=8)s+=`<line class="sl" x1="${x-7}" y1="${y}" x2="${x+7}" y2="${y}"/>`;
  s+=`<line class="rl" x1="${x-3.5}" y1="${TOP}" x2="${x-3.5}" y2="${BOT}"/><line class="rl" x1="${x+3.5}" y1="${TOP}" x2="${x+3.5}" y2="${BOT}"/>`;
  const jam=mode==='jam'&&(i===2||i===4);
  s+=`<path class="${jam?'sw-jam':t?'sw-on':'sw-off'}" d="M180 ${THROAT} L180 ${THROAT-8} L${x} ${BOT+12} L${x} ${BOT}"/>`;
  if(!t)s+=`<rect class="slot" x="${x-15}" y="${TOP+20}" width="30" height="110" rx="3"/><text class="slot-t" x="${x}" y="${TOP+78}" text-anchor="middle">OPEN</text>`;
 });
 for(let y=THROAT+4;y<PH;y+=8)s+=`<line class="sl" x1="173" y1="${y}" x2="187" y2="${y}"/>`;
 s+=`<line class="rl" x1="176.5" y1="${THROAT}" x2="176.5" y2="${PH}"/><line class="rl" x1="183.5" y1="${THROAT}" x2="183.5" y2="${PH}"/>`;
 if(mode==='jam')s+=`<path class="xmark" d="M168 ${THROAT-30} l24 22 M192 ${THROAT-30} l-24 22"/>`;
 let cars=islands()+posts(assign,-1,mode);assign.forEach((t,i)=>{if(t)cars+=car(X[i]-15,TOP+20,30,110,code(t))});
 if(mode==='open'){cars+=car(165,THROAT+10,30,38,'5','act')}
 return `<div class="stage"><div class="plane ${mode}"><i class="cast"></i><svg viewBox="0 0 ${PW} ${PH}">${s}</svg>${cars}</div></div>`;
}
const ticket=(n)=>`<div class="tk"><div class="ticket"><b>${n}</b><span>Day streak<span class="holes">${Array.from({length:7},(_,i)=>`<i class="${i<n?'on':''}"></i>`).join('')}</span></span></div></div>`;
const bar=`<span class="ic"></span><span>r/gameday_dispatch</span><small>· Dispatch · 09 Dec</small><span class="x"></span>`;
function feedTop(){return `<div class="topbar"><span class="lg"></span><span class="lgt"></span><span class="se"></span><span class="av"></span></div><div class="rail">${'<i></i>'.repeat(14)}</div>`}
"""

POST_JS = JS + r"""
function splash(){return `<div class="splash">
 <header class="g-head"><div class="brand">Dispatch<small>Station of ${D.date}</small></div>${ticket(D.streak)}</header>
 <section class="yard">${yardState([null,null,null,null,null],'open')}</section>
 <div class="info">
  <div class="radio"><span>Control: <b>5 trains</b> inbound <em>— ${D.orders.length} orders, one clean timetable</em></span></div>
  <div class="facts"><span><i>Trains</i><b>5</b></span><span><i>Platforms</i><b>5</b></span><span><i>Orders</i><b>${pad(D.orders.length)}</b></span></div>
  <div class="go"><button class="btn-cap"><span>Signal the yard</span><small>Play</small></button><span class="hi">Hi operator — same station for everyone today.</span></div>
 </div></div>`}
function post(){return `<div class="post"><div class="ph"><span class="ic"></span>r/gameday_dispatch <small>· 2h</small></div><div class="pt">Dispatch — Station of 09 Dec</div><div class="inl">${splash()}</div><div class="pa"><i></i><i></i><i></i></div></div>`}
document.getElementById('dsk').innerHTML=`<div class="dsk feedonly">${feedTop()}<div class="col">${post()}<div class="pc"><i></i><i></i><em></em></div></div></div>`;
document.getElementById('mob').innerHTML=`<div class="mob"><div class="sbar"><span>9:41</span><span></span></div><div class="feedtop"><i></i><b></b><i></i></div>${post()}<div class="ghostpost"><i></i><em></em></div></div>`;
"""

END_JS = JS + r"""
function endView(won){
 const assign=won?SOL:BAD;
 const card=won?`<div class="end">
   <span class="stamp">All trains out</span>
   <div class="facts"><span><i>Cleared in</i><b>01:42</b></span><span><i>Streak</i><b class="up">7</b></span><span><i>Orders</i><b>4/4</b></span></div>
   <div class="share"><h3>Tell the yard <span>no spoilers</span></h3>
    <div class="preview">Dispatch · 09 Dec — all trains out in 01:42. Streak 7.</div>
    <button class="btn-cap"><span>Post as a comment</span><small>1 tap</small></button></div>
   <div class="next"><span>Next station</span><b>08:14:22</b></div>
  </div>`:`<div class="end lost">
   <span class="stamp">Deadlock</span>
   <p>Two trains want the same path. Re-shunt and try again.</p>
   <div class="facts"><span><i>Clock</i><b>02:10</b></span><span><i>Streak</i><b>6</b></span></div>
   <button class="btn-cap"><span>Back to the yard</span><small>Re-shunt</small></button>
   <div class="next"><span>Next station</span><b>08:13:54</b></div>
  </div>`;
 return `<div class="game">
  <header class="g-head"><div class="brand">Dispatch<small>Station plan · ${D.date}</small></div>
   <div class="meta"><div class="m"><i>Clock</i><b>${won?'01:42':'02:10'}</b></div>${ticket(won?7:6)}</div></header>
  <div class="radio"><span>${won?'Control: <b>yard clear</b> <em>— every order held</em>':'Control: <b>signals jammed</b> <em>— an order does not hold</em>'}</span></div>
  <div class="endwrap"><section class="yard">${yardState(assign,won?'done':'jam')}</section>${card}</div>
 </div>`}
const frame=(won,mobile)=>mobile?`<div class="mob"><div class="sbar"><span>9:41</span><span></span></div><div class="bar"><span class="x"></span><span>r/gameday_dispatch</span><small>· Dispatch</small></div><div class="wv">${endView(won)}</div></div>`
 :`<div class="dsk">${feedTop()}<div class="col">${'<div class="pc"><i></i><i></i><em></em></div>'.repeat(2)}</div><div class="scrim"></div><div class="modal"><div class="bar">${bar}</div><div class="wv">${endView(won)}</div></div></div>`;
document.getElementById('dsk').innerHTML=frame(true,false);
document.getElementById('mob').innerHTML=frame(true,true);
document.getElementById('mob2').innerHTML=frame(false,true);
"""

SW = swatches([("Papier","#f1eee6"),("Table","#e7e2d6"),("Trait","#cbc4b4"),("Encre","#1c2128"),("Signal","#d4402b")])
REFLINE = '<div class="refs"><span><b>Style verrouillé sur la V2</b> · 03 Signal Plan · Diorama</span><span>Voir STYLE.md : tokens, composants, mouvement, états</span></div>'

def page(title, kicker, name, desc, js, nts, frames=None):
    h = (PAGE.replace("__BASE__", BASE_CSS).replace("__CSS__", CSS2 + EXTRA_CSS + ns["MATERIAL"])
         .replace("<script>\n__YARD__\n__COMMON__", "<script>\n" + js)
         .replace("Dispatch · V1 · __NUM__ __NAME__", title)
         .replace("Planche V1 · __NUM__ / 03 · Page principale « Jeu »", kicker)
         .replace("__NUM__ — __NAME__", name).replace("__DESC__", desc)
         .replace("__SWATCHES__", SW).replace("__NOTES__", notes(nts))
         .replace('<div class="ty"><b>Dispatch</b><code>01:42 · P3</code><span>__TYPE__</span></div>', REFLINE))
    if frames:
        start = h.index('<div class="frames">'); end = h.index('<div class="notes">')
        h = h[:start] + frames + "\n  " + h[end:]
    assert "__" not in h, [l for l in h.splitlines() if "__" in l][:3]
    return h

post = page("Dispatch · V2 · Post", "Planche V2 · Page 1 / 4 · Post dans le feed", "01 — Post",
 "Le post dans le feed avant d'ouvrir le jeu. La maquette du jour est vide, cinq trains attendent à l'entrée : on comprend le jeu avant de cliquer. Un seul bouton allumé, la série du joueur en ticket, et rien qui dévoile la solution.",
 POST_JS,
 [("Maquette vide","Les 5 quais sont ouverts, les lampes éteintes. Le bloc rouge « 5 » sur la voie d'entrée annonce les cinq trains à placer."),
  ("Accroche","La ligne radio donne le nombre d'ordres du jour (4) ; les cartes rappellent trains, quais et ordres. Pas de meilleur temps : il n'est pas stocké."),
  ("Bouton allumé","Ici le bouton d'arcade est allumé d'emblée : c'est la seule action du post. Il ouvre la vue étendue (requestExpandedMode)."),
  ("Hauteur","Le post inline n'a pas de hauteur fixée dans devvit.json. Maquette calée sur ~460 px en desktop et ~440 px en mobile, à vérifier sur un vrai post.")])

fin_frames = '''<div class="frames">
    <div><div class="cap"><span>Desktop · 1440 × 900 · gagné</span><span>× 0.56</span></div>
      <div class="scaled" style="width:806px;height:504px"><div class="inner" id="dsk" style="transform:scale(.56)"></div></div></div>
    <div><div class="cap"><span>Mobile · gagné</span><span>× 0.597</span></div>
      <div class="scaled" style="width:233px;height:504px"><div class="inner" id="mob" style="transform:scale(.5972)"></div></div></div>
    <div><div class="cap"><span>Mobile · deadlock</span><span>× 0.597</span></div>
      <div class="scaled" style="width:233px;height:504px"><div class="inner" id="mob2" style="transform:scale(.5972)"></div></div></div>
  </div>'''
fin = page("Dispatch · V2 · Carte de fin", "Planche V2 · Page 3 / 4 · Carte de fin", "03 — Carte de fin",
 "Le résultat se lit sur la maquette elle-même : tous les trains à quai et les lampes allumées, ou l'aiguillage bloqué. La carte posée à côté donne le temps, la série, un commentaire sans spoiler en un tap, et le compte à rebours jusqu'à la prochaine gare.",
 END_JS,
 [("Gagné","Tampon rouge « All trains out », les 5 lampes à l'encre, la série passe à 7 (seul chiffre en rouge). Données = solution réelle du 09/12."),
  ("Commentaire","Aperçu du commentaire sans spoiler (date, temps, série), posté en un tap : c'est l'accroche Reddit-y de l'IDEE."),
  ("Deadlock","Tampon à l'encre, aiguillage barré en rouge, trains grisés. On ne dit pas quel ordre casse (le serveur ne le renvoie pas). La série ne bouge pas."),
  ("Prochaine gare","Compte à rebours jusqu'à minuit UTC (la seed change à dayKeyUTC). Présent dans les deux états.")],
 fin_frames)

post = post.replace("Desktop · 1440 × 900 · vue étendue", "Desktop · 1440 × 900 · feed").replace("<span>Mobile · 390 × 844</span>", "<span>Mobile · 390 × 844 · feed</span>")
(OUT / "01-post.html").write_text(post, encoding="utf-8")
(OUT / "03-carte-de-fin.html").write_text(fin, encoding="utf-8")
print("ok")
