# PAGES — Dispatch

> Statuts : à dessiner / en revue / validée. **Style verrouillé le 2026-11-18 (/lock)** : **03 Signal Plan · Diorama**, V2 + matière V3, formalisé dans `STYLE.md`.
> Chaque planche montre les deux cadres côte à côte : desktop 1440 × 900 et mobile 390 × 844 (§6 du brief).
> Données de démo = vraie partie du 2026-12-09 générée par `src/shared/puzzle.ts` (4 ordres, solution unique).

| # | Page | Rôle | Contenu clé | Statut |
|---|------|------|-------------|--------|
| 1 | **Post** | Vue dans le feed (splash inline, `splash.html`) : donner envie d'ouvrir la gare du jour | En-tête du post, nom du jeu, date de la gare, série du joueur, maquette vide, bouton « Signal the yard » | **validée** 2026-11-18 · `planches/v3/01-post.html` |
| 2 | **Jeu** | Écran principal (`game.html`, vue étendue). Une seule règle : « Pick a train, then tap its platform. Every order must hold. » | Maquette des 5 quais, 5 trains (express, freight, local, overnight, shuttle), train en main, ordres du jour (4 à 6), chrono, série, bouton « Clear the signals » | **validée** 2026-11-18 · `planches/v3/03-signal-plan-diorama.html` |
| 3 | **Carte de fin** | Résultat + boucle quotidienne + accroche commentaire | Gagné (« All trains out ») / perdu (« Deadlock »), temps, série, commentaire sans spoiler en un tap, prochaine gare | **validée** 2026-11-18 · `planches/v3/03-carte-de-fin.html` |
| 4 | **Séries & communauté** | Montrer la série et la communauté | % de joueurs qui ont dégagé la gare (jour + 7 dernières gares), série perso et ses 7 derniers jours | **validée** 2026-11-18 · `planches/v3/04-series.html` |

## Ce que la liste ne contient pas (volontairement)

- Pas d'écran tutoriel : la règle tient en une ligne dans le Jeu.
- Pas d'écran de chargement / erreur dédié : ce sont des **états** du Jeu, définis dans `STYLE.md` §8.

## Questions produit ouvertes (non tranchées — à toi)

> Elles ne bloquent pas le style verrouillé : ce sont des décisions de jeu et de données à trancher avant ou pendant le build.

1. **Ordres « allumés » en direct ?** Le code actuel ne dit rien avant la soumission. Allumer chaque ordre satisfait pendant le placement rendrait le jeu plus vivant mais plus facile. Les planches n'allument que les **aiguillages des quais occupés** (simple information de placement, aucune validation). Oui / non ?
2. ~~Scores de la communauté~~ → **tranché le 2026-11-18 : % de joueurs qui ont réussi.** Pas de classement au temps.
3. **Après un « Deadlock »** : le code permet de rejouer immédiatement, sans limite. Garde-t-on des essais illimités (et compte-t-on les essais dans le score) ?
4. **Commentaire en un tap** (Carte de fin) : poster le commentaire au nom du joueur (`reddit.submitComment` côté serveur) ou seulement le préremplir et laisser le joueur l'envoyer ? La planche suppose le premier cas.
5. **Titre du post** : `post.ts` crée aujourd'hui un post titré `<% name %>`. La planche Post propose « Dispatch — Station of 09 Dec ».
6. **Dénominateur du %** : la planche compte « joueurs ayant envoyé au moins une fois aujourd'hui ». Alternative : tous ceux qui ont ouvert la gare (plus bas, mais plus honnête sur l'abandon). À confirmer.
7. **Accès à la page 4** : rien n'y mène aujourd'hui. Je propose un lien « Station board » sous la carte de fin (ajout au prochain `/delta` si tu valides).
