"""V3 material layer: grain, cardboard thickness, one light (top-left), real volumes. Appended LAST on every page."""

GRAIN = ("url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='180' height='180'>"
         "<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/>"
         "<feColorMatrix values='0 0 0 0 .11 0 0 0 0 .12 0 0 0 0 .14 0 0 0 .09 0'/></filter>"
         "<rect width='100%' height='100%' filter='url(%23n)'/></svg>\")")
FIBRE = ("url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='240' height='240'>"
         "<filter id='f'><feTurbulence type='fractalNoise' baseFrequency='.012 .35' numOctaves='2' seed='4'/>"
         "<feColorMatrix values='0 0 0 0 .35 0 0 0 0 .3 0 0 0 0 .22 0 0 0 .10 0'/></filter>"
         "<rect width='100%' height='100%' filter='url(%23f)'/></svg>\")")

MATERIAL = r"""
/* ================= V3 · MATERIAL LAYER ================= */
:root{--grain:__GRAIN__;--fibre:__FIBRE__;
 --slab:inset 1px 1px 0 rgba(255,255,255,.95),1px 1px 0 #ddd6c7,2px 2px 0 #d3cbba,3px 3px 0 #c9c0ad,4px 4px 0 #bfb6a1,5px 5px 0 #b5ab95,6px 6px 0 var(--ink),10px 14px 18px rgba(28,33,40,.26);
 --slab-sm:inset 1px 1px 0 rgba(255,255,255,.95),1px 1px 0 #d3cbba,2px 2px 0 #c4bba7,3px 3px 0 var(--ink),5px 8px 10px rgba(28,33,40,.22);
 --slab-ink:inset 1px 1px 0 rgba(255,255,255,.14),1px 1px 0 #11151a,2px 2px 0 #0b0e12,3px 3px 0 #000,5px 8px 10px rgba(28,33,40,.3);
 --slab-red:inset 1px 1px 0 rgba(255,255,255,.3),1px 1px 0 #b8331f,2px 2px 0 #a52d1b,3px 3px 0 #8f2416,4px 4px 0 var(--ink),8px 12px 14px rgba(151,41,26,.35)}
/* table: grain + one light top-left + vignette bottom-right */
.game,.splash{background:var(--grain),radial-gradient(120% 80% at 0% 0%,rgba(255,255,255,.75),transparent 55%),radial-gradient(120% 120% at 100% 100%,rgba(28,33,40,.13),transparent 60%),var(--g-bg)!important}
.brand{text-shadow:1px 1px 0 #d6cfbf,2px 2px 0 #cdc5b3,3px 3px 0 #c3baa6,4px 4px 0 #b9af99,5px 5px 0 #aea48d,6px 6px 0 #a39981,8px 12px 12px rgba(28,33,40,.3)!important}
.radio{border-color:transparent!important;background:linear-gradient(#e9e3d6,#efeadf);border-radius:8px;padding:7px 10px!important;box-shadow:inset 0 2px 4px rgba(28,33,40,.14),inset 0 -1px 0 rgba(255,255,255,.8)}
.radio:before{background:radial-gradient(circle at 35% 30%,#ffb3a6,#d4402b 45%,#7e2112)!important}
/* paper objects get cardboard thickness */
.chip,.facts span,.panel,.end,.o-n,.preview{background:var(--fibre),linear-gradient(145deg,#fffdf8,#f1ecdf)!important;box-shadow:var(--slab-sm)!important}
.panel,.end{box-shadow:var(--slab)!important;transform:perspective(1400px) rotateX(2.5deg) rotateZ(-.3deg)}
.preview{box-shadow:inset 0 2px 5px rgba(28,33,40,.14),inset 0 -1px 0 #fff!important;border-color:#d3cbba!important}
.o-n{box-shadow:1px 1px 0 #c4bba7,2px 2px 0 var(--ink)!important}
.chip.is-placed{background:var(--fibre),linear-gradient(145deg,#353b45,#1c2128 60%)!important;box-shadow:var(--slab-ink)!important}
.chip.is-active{background:var(--fibre),linear-gradient(145deg,#ee6d57,#d4402b 55%,#c2361f)!important;box-shadow:var(--slab-red),0 18px 22px rgba(28,33,40,.18)!important;transform:translate(-3px,-6px) rotate(-4deg)!important}
/* ticket: real paper stub with stacked thickness (mask-safe via drop-shadows on wrapper) */
.tk{display:inline-block;transform:rotate(2deg);filter:drop-shadow(1px 1px 0 #d3cbba) drop-shadow(1px 1px 0 #c4bba7) drop-shadow(1px 1px 0 #b5ab95) drop-shadow(1px 1px 0 var(--ink)) drop-shadow(5px 9px 8px rgba(28,33,40,.25))}
.tk .ticket{transform:none;box-shadow:none;background:var(--fibre),linear-gradient(150deg,#fffdf7,#efe9db)}
.holes i.on{background:radial-gradient(circle at 40% 35%,#000,#1c2128)!important;box-shadow:inset 0 1px 1px rgba(0,0,0,.6)}
.pct b{text-shadow:1px 1px 0 #b8331f,2px 2px 0 #a52d1b,3px 3px 0 #8f2416,5px 7px 8px rgba(151,41,26,.3)}
.ticket b{text-shadow:1px 1px 0 #8f2416}
/* ---------- diorama: deeper, thicker, standing objects ---------- */
.yard{background:var(--grain),radial-gradient(120% 90% at 15% 0%,rgba(255,255,255,.7),transparent 60%),linear-gradient(#e9e4d8,#ddd6c7)!important;box-shadow:inset 0 2px 6px rgba(28,33,40,.12),inset 0 -1px 0 rgba(255,255,255,.7)}
.stage{perspective:120cqw!important;perspective-origin:50% -40%!important}
.plane{transform:rotateX(40deg)!important;background:var(--grain),radial-gradient(#d0c8b6 1px,transparent 1.3px) 0 0/3.6cqw 3.6cqw,radial-gradient(110% 90% at 10% 0%,#fffdf8,#ebe5d8 70%,#ddd5c4)!important;box-shadow:inset 0 0 0 1px var(--ink),inset 0 0 4cqw rgba(28,33,40,.06)!important}
.plane:after{height:6cqw!important;background:repeating-linear-gradient(90deg,rgba(0,0,0,.07) 0 .5cqw,transparent .5cqw 1.1cqw),linear-gradient(#d5cdbb,#ada38c)!important}
.cast{bottom:-12cqw!important;height:11cqw!important;background:radial-gradient(closest-side,rgba(28,33,40,.42),transparent)!important;filter:blur(2cqw)!important}
.rl{stroke-width:1.1!important}
.sl{stroke:#c2b9a5!important;stroke-width:2.6!important}
.car{--t:5cqw}
.car .sdl,.car .sdr{position:absolute;top:0;bottom:0;width:var(--t)}
.car .sdl{left:0;transform-origin:left center;transform:rotateY(-90deg);background:linear-gradient(90deg,#2b3139,#3d444f)}
.car .sdr{right:0;transform-origin:right center;transform:rotateY(90deg);background:linear-gradient(90deg,#0b0e12,#000)}
.car .fr{background:linear-gradient(#141920,#05070a)!important}
.car .top{overflow:hidden}
.car .top:before{content:"";position:absolute;left:10%;right:10%;top:4%;height:22%;border-radius:1cqw;background:linear-gradient(rgba(255,255,255,.22),transparent)}
.car .top u{height:.7cqw!important;background:repeating-linear-gradient(90deg,rgba(241,238,230,.55) 0 1.4cqw,transparent 1.4cqw 2.2cqw)!important;width:60%!important}
.car .sh{filter:blur(1.6cqw)!important;transform:translate(2.6cqw,1.8cqw)!important;background:rgba(28,33,40,.45)!important}
.car.act .sdl,.car.ghost .sdl{background:linear-gradient(90deg,#c63a25,#e2553f)}
.car.act .sdr,.car.ghost .sdr{background:#7e2112}
.car.act .fr,.car.ghost .fr{background:linear-gradient(#a52d1b,#6d1c10)!important}
.car.ghost{--t:11cqw}
.car.isl{--t:1.8cqw}
.car.isl .top{background:var(--fibre),linear-gradient(145deg,#fffdf8,#ece6d8)!important;box-shadow:inset 0 0 0 .25cqw var(--ink)!important;border-radius:.6cqw}
.car.isl .top:before{display:none}
.car.isl .fr{background:linear-gradient(#cfc7b5,#b3aa94)!important}
.car.isl .sdl{background:#e2dccf}.car.isl .sdr{background:#a89e87}
.car.isl .sh{transform:translate(1cqw,.8cqw)!important;filter:blur(.8cqw)!important;background:rgba(28,33,40,.22)!important}
.plane.jam .car:not(.isl) .top{background:linear-gradient(140deg,#5a5f67,#41464e)!important}
/* standing signal posts */
.sig{position:absolute;transform-style:preserve-3d;transform-origin:50% 100%;transform:rotateX(-50deg);display:flex;flex-direction:column;align-items:center}
.sig b{flex:none;width:100%;aspect-ratio:1;border-radius:50%;display:flex;align-items:center;justify-content:center;font:800 2.8cqw/1 var(--mono);color:var(--ink);
 background:radial-gradient(circle at 35% 30%,#fff 0 12%,#eee8db 40%,#c8bfac);border:.45cqw solid var(--ink);box-shadow:.4cqw .5cqw 0 #8f8670}
.sig i{flex:1;width:1cqw;background:linear-gradient(90deg,#69707a,#1c2128 70%);border-radius:.3cqw}
.sig.on b{background:radial-gradient(circle at 35% 30%,#69707a 0 10%,#2b313a 40%,#0b0e12);color:var(--g-bg)}
.sig.hov b{border-color:var(--red);color:#fff;background:radial-gradient(circle at 35% 30%,#ffd0c7 0 10%,#e2553f 40%,#97291a);box-shadow:0 0 0 .8cqw rgba(212,64,43,.18),0 0 4cqw rgba(212,64,43,.55),.4cqw .5cqw 0 #6d1c10}
/* ---------- arcade hardware ---------- */
.cta{background:var(--grain),linear-gradient(#ddd6c7,#e7e1d4)!important;border-radius:14px!important;box-shadow:inset 0 3px 8px rgba(28,33,40,.22),inset 0 -1px 0 rgba(255,255,255,.8),0 1px 0 rgba(255,255,255,.6)!important}
.lamps i{background:radial-gradient(circle at 35% 30%,#fff 0 18%,#e9e3d6 40%,#b9b09c)!important;box-shadow:0 1px 0 #8f8670,inset 0 -1px 2px rgba(0,0,0,.2)!important}
.lamps i.on{background:radial-gradient(circle at 35% 30%,#ffe2dc 0 14%,#ef6a52 40%,#a52d1b)!important;box-shadow:0 0 0 2px rgba(212,64,43,.15),0 0 10px rgba(212,64,43,.65),0 1px 0 #6d1c10!important;border-color:#6d1c10!important}
.btn-cap{position:relative;border-radius:12px!important;
 background:linear-gradient(#f6f2ea,#ddd6c7)!important;
 box-shadow:inset 0 2px 0 rgba(255,255,255,.95),inset 0 -4px 6px rgba(0,0,0,.08),0 1px 0 #c0b7a3,0 2px 0 #b8ae99,0 3px 0 #afa58f,0 4px 0 #a69c85,0 5px 0 #9d937b,0 6px 0 #948a71,0 7px 0 #8b8168,0 7px 0 1.5px var(--ink),0 14px 16px rgba(28,33,40,.3)!important}
.btn-cap:before{content:"";position:absolute;left:6%;right:6%;top:3px;height:42%;border-radius:9px 9px 14px 14px;background:linear-gradient(rgba(255,255,255,.8),rgba(255,255,255,0));pointer-events:none}
.btn-cap>*{position:relative}
.go .btn-cap,.end:not(.lost) .btn-cap,.lit{background:linear-gradient(#ef6d56,#d4402b 55%,#c2361f)!important;color:#fff!important;
 box-shadow:inset 0 2px 0 rgba(255,255,255,.4),inset 0 -4px 6px rgba(0,0,0,.15),0 1px 0 #bf3622,0 2px 0 #b3321f,0 3px 0 #a72e1c,0 4px 0 #9b2a19,0 5px 0 #8f2616,0 6px 0 #832313,0 7px 0 #772010,0 7px 0 1.5px var(--ink),0 14px 18px rgba(151,41,26,.38)!important}
.go .btn-cap:before,.end:not(.lost) .btn-cap:before{background:linear-gradient(rgba(255,255,255,.45),rgba(255,255,255,0))}
.end.lost .btn-cap,.back .btn-cap{background:linear-gradient(#3d444f,#1c2128 60%)!important;color:#fff!important;
 box-shadow:inset 0 2px 0 rgba(255,255,255,.15),0 1px 0 #15191e,0 2px 0 #11151a,0 3px 0 #0e1116,0 4px 0 #0b0e12,0 5px 0 #08090c,0 6px 0 #050608,0 7px 0 #000,0 7px 0 1.5px var(--ink),0 14px 16px rgba(28,33,40,.35)!important}
.end.lost .btn-cap:before,.back .btn-cap:before{background:linear-gradient(rgba(255,255,255,.16),rgba(255,255,255,0))}
.lit{border-radius:8px!important}
/* ---------- end card ---------- */
.stamp{text-shadow:0 0 .5px currentColor;box-shadow:inset 0 0 0 1px rgba(255,255,255,.25);background:radial-gradient(circle at 70% 40%,rgba(212,64,43,.07),transparent 70%)}
/* ---------- page 4 objects ---------- */
.gauge:before,.gauge:after{background:linear-gradient(#69707a,#1c2128)!important;height:2px!important}
.gauge i{box-shadow:0 2px 0 #a99f89,1px 3px 2px rgba(28,33,40,.2)}
.gauge i.on{background:linear-gradient(#ef6d56,#c2361f)!important;box-shadow:0 2px 0 #7e2112,1px 3px 3px rgba(151,41,26,.35)}
.week{padding:0 8px 0 0}
.wk .bar{position:relative;max-width:22px!important;border-radius:0!important;background:linear-gradient(90deg,#2b313a,#1c2128)!important;box-shadow:6px 8px 10px rgba(28,33,40,.2)!important;margin-top:6px}
.wk .bar:before{content:"";position:absolute;left:0;right:0;top:-6px;height:6px;background:#69707a;transform:skewX(-45deg);transform-origin:bottom left}
.wk .bar:after{content:"";position:absolute;left:100%;top:0;bottom:0;width:6px;background:#05070a;transform:skewY(-45deg);transform-origin:top left}
.wk.today .bar{background:linear-gradient(90deg,#e2553f,#c2361f)!important}
.wk.today .bar:before{background:#f28a77}.wk.today .bar:after{background:#7e2112}
.day{background:var(--fibre),linear-gradient(145deg,#fffdf8,#ece6d8)!important;box-shadow:inset 1px 1px 0 #fff,1px 1px 0 #c4bba7,2px 2px 0 #b5ab95,3px 3px 0 var(--ink),4px 7px 8px rgba(28,33,40,.22)!important}
.day.ok{background:linear-gradient(145deg,#3d444f,#1c2128 60%)!important;box-shadow:inset 1px 1px 0 rgba(255,255,255,.18),1px 1px 0 #0b0e12,2px 2px 0 #000,3px 3px 0 #000,4px 7px 8px rgba(28,33,40,.3)!important}
.day.today{background:linear-gradient(145deg,#ef6d56,#c2361f)!important;box-shadow:var(--slab-red)!important}
""".replace("__GRAIN__", GRAIN).replace("__FIBRE__", FIBRE)

JS_HELPERS = r"""
function car(x,y,w,h,label,cls){const win=h>60&&cls!=='isl';return `<div class="car ${cls||''}" style="left:${L(x)};top:${T(y)};width:${L(w)};height:${T(h)}"><i class="sh"></i><i class="sdl"></i><i class="sdr"></i><b class="top">${win?'<u></u>':''}<span>${label}</span>${win?'<u></u>':''}</b><i class="fr"></i></div>`}
function posts(assign,hover,mode){return X.map((x,i)=>{const t=assign[i];const st=mode==='jam'?'off':t?'on':(i===hover?'hov':'off');return `<div class="sig ${st}" style="left:${L(x-12)};top:${T(-14)};width:${L(24)};height:${T(46)}"><b>${i+1}</b><i></i></div>`}).join('')}
function islands(){return [78,146,214,282].map(x=>car(x-9,TOP+16,18,118,'','isl')).join('')}
"""
