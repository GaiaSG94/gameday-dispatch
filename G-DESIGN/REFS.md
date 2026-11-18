# REFS — Dispatch

> Références ouvertes le 2026-11-18 dans le navigateur (pas de mémoire). On prend des **principes**, jamais un layout, un texte, un asset, une police ou une marque.

## Baseten — baseten.co

Ce que j'ai vu : fond blanc, grille de points très fine en fond de page, sections séparées par des filets 1 px. Titres sans-serif grands mais légers (≈ 72 px, graisse 400, interlettrage négatif), texte courant petit. Étiquettes de section en mono capitales dans un petit bandeau noir (`:: LABEL`). Les chiffres clés (« 160ms », « 6x ») sont gros, suivis d'une légende mono minuscule en capitales. Une seule couleur vive (vert) utilisée en aplat sur un bloc à la fois.

Ce que j'en retiens :
- **Densité par les filets, pas par les boîtes** : on sépare avec des traits 1 px et des grilles, presque jamais avec des ombres ou des cartes arrondies.
- **Le mono comme étiquette** : petit, capitales, interlettré, toujours sur une donnée ou un nom de section.
- **Chiffre gros + légende mono minuscule** : pour le chrono, la série, le compteur n/5.
- **Un seul accent, en aplat, rarement** : il marque l'état actif, rien d'autre.

## Cron — cron.com

Ce que j'ai vu : la page redirige désormais vers l'annonce de son rachat, mais la vitrine est toujours là. Fond noir **chaud** (≈ `#161412`), texte gris clair, un titre énorme et très serré, puis le **produit lui-même** (la grille calendaire, dense, en sombre) comme image héros, et un seul accent chaud (orange) réservé à l'action et au « maintenant ». À noter : contrairement au brief, la page n'utilise **pas** de mono (sans-serif seule) ; la « texture » vient de la grille horaire elle-même.

Ce que j'en retiens :
- **La donnée est le héros** : chez nous, le schéma de voies (ou le tableau des départs) occupe le centre et la plus grande surface, pas un titre.
- **Le sombre chaud** plutôt que le noir bleuté : plus calme, plus « objet » (exploité dans la direction 02).
- **L'accent = le présent** : la couleur ne sert qu'à « ce qui se passe maintenant » (train sélectionné, aiguillage en cours).
- **La grille horaire comme texture** : les quais numérotés et les horaires alignés font le décor ; pas d'illustration ajoutée.

## Ce que je ne prends pas

- Les layouts marketing (héros + logos clients, grands paragraphes).
- La couleur orange de Cron et le vert de Baseten tels quels.
- Les polices propriétaires des deux sites : les planches utilisent les piles système (`system-ui`, `ui-monospace`) ; le choix d'une police embarquée sous licence libre se fera au tour C.

---

## V2 — 2026-11-18 · Gamification de la direction 03

Source : `REFERENCES-DESIGN.md` du dépôt hackatons-pipeline (version V2 sur `origin/main`, 60 refs ; la copie locale est en retard), captures `REFERENCES-CAPTURES/narratif-jeu/` et `3d-matiere/` lues une par une. Deux catégories voisines, conformément à la règle « 2-3 refs de catégories proches ». Tout est reproductible en CSS pur (transformations 3D, ombres) : aucune scène WebGL.

### narratif-jeu
- **Dairy Food Bulgaria** : le produit présenté comme une **maquette posée dans le vide**, vue de trois quarts, avec ombre portée. → la gare devient une maquette en carton inclinée à 30°, avec son épaisseur et son ombre sur la table.
- **Don't Look Up (jeu)** : dessin à l'encre sur papier, boutons cerclés noirs avec **ombre dure décalée**, bulles de texte. → les trains deviennent des stickers cerclés d'encre à ombre dure ; ligne radio « Control: … inbound ».
- **Gapsy Studio** : lettres en **relief** éclairées par une lumière dirigée, **griffonnages main** (étoile, flèche) posés par-dessus la 3D. → titre « Dispatch » en relief (lumière en haut à gauche) ; griffonnage rouge autour du quai visé + « DROP IT HERE ».
- **MemoryQuest** : la borne d'arcade et ses **boutons physiques** éclairés. → l'envoi devient un bouton d'arcade qu'on enfonce, avec cinq lampes (une par train posé).
- Écartées : Experience Funtech, Sponge, Merci Studio (néon, créature 3D, dégradé) : hors de la famille papier/encre ; Matchball, Gemeos, Raben Rifaie : principe déjà couvert.

### 3d-matiere
- **Igloo** : matière **mate**, lumière qui vient d'un côté, ombres douces. → blocs-trains mats à l'encre, reflet léger en haut à gauche, ombres portées à droite. Une seule source de lumière pour tout l'écran.
- Écartées : Noon, Giallo, Noddal, Yogi Suria, Psychoactive (néon, fond noir, rendu WebGL) : incompatibles avec la direction claire et le budget CSS.
