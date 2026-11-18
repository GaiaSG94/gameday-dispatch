# STYLE — Dispatch · « Signal Plan · Diorama »

> **Style verrouillé le 2026-11-18 (/lock)**, après validation par Gaia des 4 pages (V2, direction 03 gamifiée, + matière V3). Plus d'exploration : seuls des `/delta` ciblés restent possibles. Source de vérité pour toutes les planches et pour le passage en code.
> Les valeurs ci-dessous sont celles des planches `planches/v3/*.html` (V2 + couche matière V3, `_src/material.py`). Leurs générateurs sont dans `G-DESIGN/_src/`.

## 1. Idée en une phrase

Une gare en maquette de carton posée sur une table : papier, encre, une seule lumière en haut à gauche, et un rouge signal réservé à **ce qui se passe maintenant**.

## 2. Palette

| Token | Hex | Rôle |
|---|---|---|
| `--paper` | `#f1eee6` | Fond du jeu, surface de la maquette |
| `--paper-hi` | `#fbfaf6` | Stickers, cartes, pastilles (un cran au-dessus du papier) |
| `--table` | `#e7e2d6` | Table sous la maquette, socle du bouton d'arcade |
| `--edge` | `#cfc8b8` → `#bdb5a3` | Tranche du carton (dégradé vertical) |
| `--line` | `#cbc4b4` | Filets, traverses, aiguillages au repos |
| `--ink` | `#1c2128` | Texte, traits, trains posés, ombres dures |
| `--ink-deep` | `#0b0e12` | Face avant des blocs-trains |
| `--mute` | `#6c6f73` | Étiquettes mono, texte secondaire |
| `--signal` | `#d4402b` | **Seul accent.** Train en main, itinéraire en cours, série, bouton actif |
| `--signal-deep` | `#97291a` | Face avant / socle des éléments rouges |

Règles :
- Le rouge n'apparaît **que** pour le présent : le train en main, l'itinéraire survolé, la série du jour, le bouton qui peut être appuyé, le tampon de victoire. Une erreur (deadlock) est à l'**encre**, avec seulement le point de blocage en rouge.
- Pas de dégradé de couleur. Les seuls dégradés sont des **dégradés de lumière** dans une même teinte (reflet en haut à gauche).
- Le cadre Reddit autour reste neutre : le jeu ne pose jamais de couleur hors de sa webview.

## 3. Typographie

Deux familles, une seule échelle.

- **Sans** (titres, texte des ordres, boutons) : en planche, pile système `ui-sans-serif, system-ui…`. En prod, embarquer une linéale libre (OFL) dans le bundle, car la CSP Devvit interdit toute requête externe. Candidates : Inter ou Manrope, à trancher au build.
- **Mono** (codes trains, quais, horloge, étiquettes) : pile `ui-monospace…` en planche. En prod, JetBrains Mono ou IBM Plex Mono (OFL), embarquée.

| Rôle | Mobile (< 600 px) | Desktop (≥ 600 px) | Style |
|---|---|---|---|
| Titre « Dispatch » | 25 px / 800 | 40 px / 800 | sans, −0,035em, **relief** (voir §6) |
| Chiffre héros (horloge, série, temps) | 14–20 px / 700–800 | 22–28 px | mono |
| Texte des ordres | 12,5 px / 400 | 13,5 px | sans, interligne 1,35 |
| Bouton | 13 px / 750 | 15–16 px | sans |
| Code train sur sticker | 12 px / 800 | 15 px | mono, +0,04em |
| Ligne radio | 10 px / 500 | 12 px | mono |
| Étiquette (`TRAINS`, `CLOCK`…) | 7,5–9 px / 600 | 8,5–10 px | mono, CAPITALES, +0,14em, `--mute` |

Texte d'UI en anglais. Phrases au présent, sans point d'exclamation.

## 4. Grille et cadres

- Bascule de mise en page par **container query** sur la webview : `< 600 px` = une colonne (mobile, post inline) ; `≥ 600 px` = deux colonnes `1.42fr / 1fr` (maquette à gauche, trains + ordres à droite), gouttière 28 px.
- Marges internes : 12–16 px en mobile, 22–32 px en desktop. Espacement vertical sur 4 px (8 / 12 / 16 / 22).
- **Tout tient dans la hauteur de la webview sans défilement** : 756 px utiles en mobile plein écran, ~440 px pour le post inline.
- La maquette est dimensionnée en `cqw` (unités de conteneur) : elle s'adapte à la largeur et garde ses proportions (360 × 262).

## 5. Composants

| Composant | Anatomie | États |
|---|---|---|
| **Maquette** | Plan papier pointillé incliné `rotateX(30deg)`, perspective `150cqw`, tranche de carton 3,2 cqw, ombre sur la table. Voies = 2 rails encre + traverses `--line`. Lampes numérotées en tête de voie. | Quai libre : cadre pointillé « OPEN ». Quai visé : cadre rouge + fantôme du train + griffonnage. Quai occupé : bloc encre, lampe pleine, aiguillage tracé à l'encre. |
| **Bloc-train** | Face supérieure (dégradé encre, code mono), face avant `--ink-deep` (épaisseur 3,6 cqw), ombre floue décalée vers le bas à droite. | Posé (encre) · en main (rouge, oscille) · fantôme (rouge 50 %, flotte à 9 cqw) · bloqué (gris `#3a3f47`). |
| **Sticker train** | Carte `--paper-hi`, contour encre 1,5 px, rayon 9 px, ombre dure 2,5 px. Code, nom, statut. | En attente · en main (rouge, −3°, soulevé, ombre 4/6 px) · posé (encre, aplati, « On Pn »). |
| **Ticket de série** | Ticket encoché, contour encre, ombre dure 3 px, incliné +2°, chiffre rouge, 7 perforations. | Une perforation pleine par jour de série. |
| **Ligne radio** | Point rouge qui respire + phrase mono entre deux filets. | Une phrase par moment : arrivée, quai à choisir, gare dégagée, signaux bloqués. |
| **Bouton d'arcade** | Socle `--table` + capuchon arrondi 10 px, contour encre, socle de 5 px. Variante avec 5 lampes. | Éteint (papier, texte gris, `disabled`) · allumé (rouge) · enfoncé (translateY 5 px, socle à 0) · sombre (encre, action secondaire « Back to the yard »). |
| **Carte de fin** | Carte `--paper-hi`, ombre dure 4/5 px, tampon incliné −4°, 2-3 pastilles de chiffres, aperçu du commentaire, bouton, compte à rebours. | Gagné (tampon rouge) · Deadlock (tampon encre). |
| **Jauge en voie** | 50 traverses entre deux rails encre ; la part réussie en rouge, le reste en `--line`. | Une seule jauge par écran (score du jour). |
| **Barres 7 gares** | Barres encre arrondies en haut, valeur mono au-dessus, date mono dessous. | Aujourd'hui en rouge, les autres à l'encre. |
| **Cases jours** | 7 cases encre arrondies 7 px, ombre dure. | Réussi (encre) · aujourd'hui (rouge, −3°) · manqué (pointillé, vide). |
| **Griffonnage** | Tracé rouge à main levée (SVG), flèche et « DROP IT HERE » en mono. | Visible uniquement au survol d'un quai libre. |

## 6. Lumière, relief, ombres

- **Une seule source de lumière, en haut à gauche, pour tout l'écran.** Les reflets vont en haut à gauche, les ombres en bas à droite.
- **Ombre dure** (stickers, tickets, cartes, boutons) : décalage plein encre, sans flou. C'est la signature « objet découpé ».
- **Ombre douce** (blocs-trains, maquette) : floue, `rgba(28,33,40,.32–.38)`, réservée aux volumes posés sur la table.
- **Relief du titre** : `text-shadow` en trois paliers de `--edge` (1, 2, 3 px), plus une ombre douce.

## 6 bis. Matière (V3)

Retour de Gaia : pas assez de 3D ni de matière. Tout reste en CSS (aucune image, aucun WebGL) :

- **Grain** : bruit SVG `feTurbulence` en data URI sur la table et la maquette, et une fibre de papier sur les objets en carton. Aucune requête externe.
- **Épaisseur de carton** : les objets papier (stickers, cartes, pastilles, cases jours) ont une tranche de 3 à 6 px en paliers beige, puis un trait d'encre et une ombre douce. Trois variantes : papier (`--slab`), encre (`--slab-ink`), rouge (`--slab-red`).
- **Panneaux posés** : la carte de fin et les panneaux de la page 4 sont légèrement inclinés (`rotateX(2.5deg)`), comme posés sur la table.
- **Maquette** : inclinée à 40°, socle de carton ondulé de 6 cqw, quais en relief entre les voies, trains en vrais volumes (dessus, avant, deux flancs, fenêtres, reflet), poteaux de signal debout à tête de verre numérotée, éclairée quand le quai est occupé ou rouge quand il est visé.
- **Matériel d'arcade** : socle creusé dans la table, capuchon bombé avec 7 paliers d'épaisseur et un reflet spéculaire, lampes en verre (rouges et lumineuses quand elles sont allumées).
- **Données en volume** : les barres des 7 gares sont des colonnes 3D (dessus et flanc obliques), les traverses de la jauge ont une épaisseur, le % du jour est en relief rouge.
- Le ticket de série est un vrai talon de papier : son épaisseur passe par des `drop-shadow` empilés, parce que le masque des encoches couperait un `box-shadow`.

## 7. Mouvement

| Quoi | Durée | Courbe | Note |
|---|---|---|---|
| Train en main qui oscille | 1,6 s, boucle | ease-in-out | translateZ 0 → 0,8 cqw |
| Fantôme au survol | 1,6 s, boucle | ease-in-out | flotte au-dessus du quai visé |
| Itinéraire survolé | 1 s, boucle | linear | pointillés qui défilent vers le quai |
| Point radio | 1,4 s, boucle | ease-in-out | halo qui respire |
| Sticker pris en main | 150 ms | ease-out | soulèvement + rotation −3° |
| Train posé | 250 ms | ease-out (léger rebond) | le fantôme descend sur le quai, la lampe s'allume |
| Bouton enfoncé | 80 ms | linear | le capuchon descend de 7 px (paliers d'épaisseur à 0) |
| Tampon de fin | 300 ms | ease-out | arrive à 1,2× puis se pose à 1× et −4° |

`prefers-reduced-motion` : couper toutes les boucles. Les changements d'état restent, sans animation.

## 8. Règles d'états (écran Jeu)

1. **Aucune validation des ordres pendant le placement** (question 1 de `PAGES.md` toujours ouverte).
2. Il y a toujours **un** train en main tant qu'il en reste à poser. Après une pose, le suivant passe en main automatiquement (comportement actuel du code).
3. Le bouton reste éteint tant que les 5 trains ne sont pas posés, puis s'allume.
4. Chargement : la maquette vide s'affiche, la ligne radio dit « Switching the yard… », et rien n'est cliquable. Erreur : la ligne radio passe à l'encre avec le message, avec un bouton sombre pour réessayer.
5. Déjà joué aujourd'hui (`solvedToday`) : afficher directement la carte de fin gagnée. Le comportement exact est à confirmer en code.

## 9. Interdits propres à ce style

- Une deuxième couleur d'accent, du néon, un fond sombre.
- Des emoji dans l'UI (le code actuel en utilise, à retirer).
- Des ombres dures et douces sur un même objet.
- Une lumière qui viendrait d'ailleurs que du haut gauche.
- Tout ce qui dévoile la solution dans le post ou dans le commentaire partagé.
