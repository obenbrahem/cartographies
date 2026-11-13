# KEEL — Cartographies ACHEEL

Application autonome reconstruite à partir des données des cinq cartographies. Les anciennes interfaces ne sont pas intégrées à l’application : les vues, cartes, filtres, fiches et interactions sont rendus par le même code natif. Les documents d’origine restent disponibles uniquement comme sources téléchargeables.

Le langage visuel reprend Keel : barre latérale bleu marine `#081F4D`, bleu `#1E96FC`, typographies Montserrat et JetBrains Mono, tableaux, onglets et fiches structurées. Aucun composant métier, profil ou stockage de l’application GRC Keel n’est utilisé.

## Construire la livraison

Depuis la racine du dépôt :

```sh
python3 cartographies-keel/build.py
```

Cette commande utilise uniquement la bibliothèque standard Python. Elle produit `dist/acheel-cartographies.html` et `dist/acheel-cartographies.zip`. Le ZIP contient le HTML, le guide d’utilisation et les licences des polices. L’application livrée fonctionne sans Python, Node, serveur ni connexion réseau.

## Organisation

| Fichier | Rôle |
| --- | --- |
| `data.json` | Données, relations, contexte documentaire et sources originales intégrées. |
| `core.js` | Référentiel commun, navigation, recherche documentaire et états de vue. |
| `views.js` | Tableau de bord, exploration métier, matrices, catalogues, tableaux, comparateurs et glossaires. |
| `graph.js` | Cartes SVG natives, sélection, zoom, déplacement, clavier et adaptation mobile. |
| `reinsurance.js` | Schémas BtoBtoC et sans partenaire, correspondances documentaires, choix de lecture et export SVG. |
| `details.js` | Fiches, liens, données sources et rendu sûr des rubriques documentaires. |
| `events.js` | Interactions, exports, favoris, restauration et accessibilité des panneaux. |
| `app.css` | Interface et adaptations aux écrans. |
| `fonts.css` | Polices intégrées et licences. |
| `index.template.html` | Structure commune de l’application. |
| `MANIFEST.json` | Empreinte du jeu de données et des cinq documents sources. |

## Périmètre documentaire

Le référentiel comprend 1 140 objets, dont 102 processus, 14 fonctions, 6 chaînes de valeur, 7 produits, 16 acteurs produits, 10 parcours, 19 formules Santé, 36 partenaires, 105 offres, 145 rubriques de convention, 242 flux partenaires, 206 acteurs de partenaires, 46 outils, 36 flux SI, 52 rubriques Omega, 15 personnes citées, 7 points d’attention source, 28 termes du glossaire outils, 5 interfaces sans fiche outil, 12 libellés de réassureurs ou de panel et 28 lignes de synthèse de réassurance. Les trois entités du fonctionnement sont également conservées.

Les relations sont documentaires. Les mentions d’outils et les rapprochements proposés restent à confirmer lorsqu’ils sont ainsi qualifiés dans les sources. Les parts de réassurance ne sont pas agrégées ; le panel placé par Guy Carpenter conserve sa part globale, sans répartition inventée entre ses membres. Les dates et statuts ne sont pas actualisés par déduction. Le module de qualification des points de contrôle n’est pas intégré ; les descriptions métier des sources sont conservées.

`data.json` est la base normalisée de cette livraison. Une mise à jour doit préserver les identifiants utiles, les références et les pièces sources. Après une modification intentionnelle du jeu de données, actualiser le manifeste et régénérer la livraison. Le stockage local `acheel-cartographies-keel-v1` contient uniquement les favoris et les éléments récemment ouverts ; les annotations ne modifient pas le référentiel.

## Vérifications

Le rapport à la racine du dépôt décrit la vérification de la livraison. Les tests de navigation peuvent être exécutés avec Node, Playwright et un Chromium disponible :

```sh
npm --prefix cartographies-keel install
CHROMIUM_PATH=/usr/bin/chromium node cartographies-keel/tests/audit.cjs
```

Ces dépendances servent uniquement au développement et aux tests. Les tests chargent le HTML autonome depuis une adresse interceptée, avec le contexte navigateur hors ligne. La politique du navigateur cloud bloque la navigation directe `file://` ; aucune politique n’est désactivée pour les tests.

## Schémas de réassurance — édition 1.1

Deux vues permettent de représenter les acteurs d’une ligne de synthèse :

- BtoBtoC : Réassureur → Acheel SA → Acheel France → Partenaire → Produit/programme.
- Sans partenaire : Réassureur → Acheel SA → Acheel France → Produit/programme.

Les 28 lignes sont sélectionnables dans chaque vue. Les traits décrivent les modèles de lecture demandés ; ils ne représentent pas des paiements et ne déterminent pas le canal réel d’un traité. Les blocs ouvrent les fiches en gardant le schéma à l’écran. Les lignes et réassureurs ont aussi des raccourcis vers les deux schémas. L’export SVG conserve la part, la période, la référence et les réserves de lecture.

`data.json.reinsuranceSchemes` contient 12 rapprochements documentaires explicités et leurs références ; ils sont distincts des 1 251 relations sources. Les rapprochements ne certifient pas l’identité d’un contrat. Les lignes non rapprochées restent sans partenaire par défaut ; un choix manuel de partenaire est marqué comme choix de lecture à confirmer et n’est pas enregistré dans le référentiel. La nouvelle génération Genius/Senior n’est pas attribuée automatiquement à SpVie. Les rôles Auvray/FMA restent distincts ; la divergence Groupe Mutualia / Harmonie Mutuelle est signalée.

Test dédié : `npm --prefix cartographies-keel run test:reassurance`. Il couvre les 56 combinaisons de ligne/circuit, les liens de fiche, les choix de partenaire, les exports SVG et le mobile.
