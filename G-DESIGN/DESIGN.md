# DESIGN — Dispatch (journal)

> Tenu par Claude. Versions datées, jamais écrasées.

## V1 — 2026-11-18 · Exploration du style (page principale « Jeu »)

**Statut** : en attente de validation de Gaia (étape B du brief). Rien n'est décliné tant qu'une direction n'est pas choisie.

### Livré
- `PAGES.md` : 4 pages proposées (Post, Jeu, Carte de fin, Séries & classement) et 3 questions produit ouvertes.
- `REFS.md` : Baseten et Cron ouverts et décodés.
- `planches/v1/01-control-room.html`, `02-departure-board.html`, `03-signal-plan.html` : 3 directions sur le Jeu, chacune en desktop 1440 × 900 (vue étendue dans la fenêtre modale du post) et mobile 390 × 844 (plein écran).

### Données de démo
Vraie partie du **2026-12-09** sortie de `generateDispatch` : 4 ordres, solution unique. État figé : 3 trains placés (express P1, local P3, overnight P4), freight sélectionné, survol du quai 2, chrono 01:42, série 6.

### Décisions V1
- **Trains différenciés par un code mono à 3 lettres** (EXP, FRT, LOC, OVN, SHT) et pas par une couleur : une seule couleur d'accent par direction, et plus d'emoji (le code actuel en utilise, interdit par le brief).
- **L'accent ne marque que le présent** : train sélectionné, itinéraire en cours, série.
- **Aiguillage allumé = quai occupé**, sans validation des ordres (question 1 de `PAGES.md`).
- **Bouton d'envoi** inactif avant 5/5 mais lisible : il montre la progression.
- **Polices** : piles système dans les planches. Une police libre embarquée (CSP Devvit : aucune requête externe) sera choisie au tour C.
- **Cadre Reddit** neutre (formes grises, sans logo ni marque) ; le sous-reddit de démo `r/gameday_dispatch` est un nom provisoire.

### Remarques hors design (pour Gaia, non traitées)
- Le générateur produit des parties très faciles : sur 2026-12-09 et 2026-12-10, 3 ou 4 ordres sur 4 sont des placements directs (« X sits on platform N »), et le mélange par `sort(() => rand() - 0.5)` est biaisé (la solution du 09/12 est l'ordre alphabétique).
- `clueText` renvoie « the express… » en minuscule ; les planches affichent la majuscule.

## V2 — 2026-11-18 · Direction 03 retenue, gamifiée (« Diorama »)

**Statut** : en revue. Gaia a retenu la direction **03 Signal Plan** et demandé de la gamifier à partir des refs `narratif-jeu` et `3d-matiere` du dépôt hackatons.

### Livré
- `planches/v2/03-signal-plan-diorama.html` (desktop + mobile, mêmes données et même état que la V1). Planches V1 conservées.
- `REFS.md` : section V2 (refs lues sur capture, retenues et écartées).

### Changements par rapport à la V1 (03)
1. **Maquette** : le plan est incliné à 30° en CSS 3D, avec une épaisseur de carton, une ombre sur la table et une lumière unique en haut à gauche. Les voies ont maintenant leurs traverses.
2. **Les trains deviennent des volumes** : blocs extrudés à l'encre. Le train en main (rouge) oscille sur la voie d'entrée ; au survol d'un quai, son **fantôme flotte au-dessus** du quai visé.
3. **Griffonnage** rouge autour du quai visé + flèche « DROP IT HERE » : affordance de survol, pas un tutoriel.
4. **Stickers** : les trains de la liste ont une ombre dure. Celui en main se soulève et pivote de −3°, un train posé s'aplatit à l'encre (« On P1 »).
5. **Bouton d'arcade** : cinq lampes (une par train posé) et un capuchon qui s'enfonce de 5 px, éteint avant 5/5.
6. **Narration** : la ligne radio « Control: FRT freight inbound — pick its platform » remplace la règle statique. « Orders from control » remplace « Orders ».
7. **Série** : un ticket poinçonné (une perforation par jour, 7 visibles) et un titre en relief.

### Ce qui ne change pas
Une seule couleur d'accent (rouge signal, réservée au train en main et à l'itinéraire), toujours aucune validation des ordres pendant le placement (question 1 de `PAGES.md` toujours ouverte), et aucune feature ajoutée.

### Points à surveiller au passage en code
- La 3D en CSS (`preserve-3d`) se casse si un parent a `overflow:hidden` à l'intérieur de la scène : à isoler dans un composant.
- `prefers-reduced-motion` : couper l'oscillation, le flottement du fantôme et les pointillés animés.

## V2.1 — 2026-11-18 · Style validé, déclinaison (étape C)

**Statut** : Jeu **validé** par Gaia (« Valider, décliner »). Post et Carte de fin **en revue**. Séries & classement **non dessinée**, bloquée par la question 2 de `PAGES.md` (aucun score communautaire n'est stocké aujourd'hui).

### Livré
- `STYLE.md` : palette (10 tokens, un seul accent), échelle typo, grille par container query, 8 composants avec leurs états, lumière/ombres, mouvement, règles d'états, interdits.
- `planches/v2/01-post.html` : le post dans le feed, desktop + mobile.
- `planches/v2/03-carte-de-fin.html` : gagné en desktop + mobile, deadlock en mobile.
- `_src/` : les générateurs des planches, pour les prochains `/delta` (optionnels : les `.html` restent autonomes).

### Décisions
- **Post** : maquette vide (5 quais « OPEN », un bloc rouge « 5 » sur la voie d'entrée), seul élément cliquable = le bouton d'arcade **allumé**. Rien n'y dévoile la solution. Pas de « meilleur temps » : il n'est pas stocké.
- **Carte de fin** : le résultat se lit d'abord sur la maquette (tous les trains à quai et lampes allumées, ou aiguillage barré), la carte vient ensuite. Le tampon de victoire est rouge, celui du deadlock à l'encre. Le commentaire proposé reste sans spoiler : date, temps, série.
- **Deadlock** : on ne dit pas quel ordre casse, puisque le serveur ne renvoie que `won`. Le texte d'erreur reste celui du code actuel. La série ne change pas.
- **Prochaine gare** : compte à rebours jusqu'à minuit UTC (`dayKeyUTC`), affiché dans les deux états.

### À vérifier sur un vrai post
- La hauteur du post inline : rien n'est fixé dans `devvit.json`. Planche calée sur ~460 px en desktop et ~440 px en mobile.

## V2.2 — 2026-11-18 · Page 4 « Séries & communauté »

**Statut** : en revue. Gaia a tranché la question 2 : le score de la communauté est le **% de joueurs qui ont dégagé la gare**.

### Livré
- `planches/v2/04-series.html` (desktop + mobile) ; générateur `_src/build4.py`.
- `STYLE.md` : 3 composants ajoutés (jauge en voie, barres 7 gares, cases jours).

### Décisions
- La page est renommée « Séries & communauté » : il n'y a pas de classement, puisque le score retenu ne range pas les joueurs.
- Le % du jour est le seul chiffre rouge. La jauge est un tronçon de voie (50 traverses, la part réussie en rouge), pour rester dans la maquette.
- Les 7 dernières gares donnent le contexte (« dure aujourd'hui ») sans rien dévoiler.
- Série : ticket + 7 cases jours, calculées depuis les clés `solved:{user}:{day}` déjà écrites par le serveur.
- Données de démo inventées pour la planche : 796 / 1 284 joueurs (62 %) et l'historique des 03-08 Dec.

### Côté code (pour le build, non fait)
- Deux compteurs Redis par jour, à l'envoi : `played:{day}` (premier envoi du joueur) et `cleared:{day}` (première réussite).
- Questions 6 (dénominateur) et 7 (accès à la page) ajoutées dans `PAGES.md`.

## V3 — 2026-11-18 · « Pas assez de 3D, de matière » (/delta)

**Statut** : en revue. Les 4 pages sont régénérées dans `planches/v3/`. Les V1 et V2 sont conservées.

### Changements (communs aux 4 pages, `_src/material.py`, appliqués en dernier)
1. **Grain et fibre** : bruit SVG embarqué sur la table, la maquette et chaque objet papier.
2. **Épaisseur de carton** : tranche en paliers, trait d'encre et ombre douce sur les stickers, cartes, pastilles, cases et tickets. Les panneaux sont posés légèrement inclinés.
3. **Maquette** : plus inclinée (40°), socle ondulé épais, **quais en relief** entre les voies, trains à **4 faces** (dessus, avant, flancs) avec fenêtres et reflet.
4. **Poteaux de signal debout**, à tête de verre numérotée : encre quand le quai est occupé, rouge et lumineuse sur le quai visé. Ils remplacent les lampes plates.
5. **Bouton d'arcade** : socle creusé, capuchon bombé à 7 paliers et reflet. **Lampes de progression en verre**, rouges et lumineuses quand elles sont allumées.
6. **Page 4** : colonnes en 3D, traverses de la jauge en épaisseur, % du jour en relief.

### Corrigé en route
- La classe des poteaux est passée de `.post` à `.sig` : `.post` existait déjà pour la carte de post du feed, que la rotation 3D faisait disparaître.

### Points à surveiller au passage en code
- Coût de rendu : beaucoup d'ombres empilées et de 3D. Tester sur un mobile d'entrée de gamme et, si besoin, réduire les paliers d'ombre à 3.
- Les faces 3D des trains et des poteaux exigent `transform-style: preserve-3d` sans `overflow:hidden` entre la scène et les objets.

## LOCK — 2026-11-18 · Style verrouillé (/lock)

Gaia valide la V3 « matière » et verrouille le style. Les 4 pages sont **validées** :

| Page | Planche de référence |
|---|---|
| Post | `planches/v3/01-post.html` |
| Jeu | `planches/v3/03-signal-plan-diorama.html` |
| Carte de fin | `planches/v3/03-carte-de-fin.html` |
| Séries & communauté | `planches/v3/04-series.html` |

- **Source de vérité pour le build** : `STYLE.md` (tokens, composants, matière, mouvement, états) et les planches V3. La couche matière vit dans `_src/material.py`.
- **Fin des explorations** : plus de `/planches` ni de `/variantes`. Seuls des `/delta` ciblés restent possibles ; chacun ouvre une entrée datée ici.
- **Hors style, encore ouvert** (`PAGES.md`) : Q1 ordres allumés en direct, Q3 essais après deadlock, Q4 commentaire posté ou prérempli, Q5 titre du post, Q6 dénominateur du %, Q7 accès à la page 4.
- **Côté code, rien n'est fait** : retirer les emoji, embarquer les polices OFL, ajouter les compteurs Redis `played:{day}` / `cleared:{day}`, et corriger le générateur (puzzles trop faciles, mélange biaisé).
