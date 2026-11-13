# KEEL — Nouvel outil des cartographies ACHEEL

Les cinq cartographies sont reconstruites dans une application commune au design de Keel : navigation bleu marine, typographies Montserrat et JetBrains Mono, tableaux, filtres, cartes interactives et fiches latérales. Les anciennes interfaces ne sont plus les écrans de l’outil.

**[Télécharger le ZIP](dist/acheel-cartographies.zip)**, l’extraire puis ouvrir **acheel-cartographies.html** dans Chrome ou Edge. Aucune installation ni connexion nécessaire. Le [HTML seul](dist/acheel-cartographies.html) est également disponible.

## Aperçus

- [Tableau de bord](dist/apercu-cartographies.png)
- [Nouvelle carte Produits](dist/apercu-carte-produits.png)
- [Fiche latérale et source produit](dist/apercu-fiche-cartographie.png)
- [Nouvelle cartographie Réassureurs](dist/apercu-reassureurs.png)

## Explorer les cinq univers

- **Fonctionnement** : entrer par une chaîne de valeur, déplier les fonctions, ouvrir un processus. Les 102 processus et leurs rubriques restent consultables.
- **Produits** : cartes d’acteurs par produit, zoom et déplacement, catalogue, 10 parcours détaillés, comparateur et 19 formules Santé.
- **Partenaires** : matrice interactive par famille, 36 partenaires, 105 offres, conventions et flux documentés.
- **Outils** : carte native du SI et des flux, zoom, déplacement, sélection, catalogue de 46 outils, rubriques Omega et référents.
- **Réassureurs** : matrice par périmètre et accès aux 28 lignes de synthèse, avec parts, périodes et commissions.

La recherche commune s’ouvre avec Ctrl K ou ⌘ K. Les filtres affinent la vue courante. Chaque objet ouvre une fiche avec trois rubriques : Fiche, Liens, Source. Les favoris créent des repères locaux sauvegardables. Les exports CSV respectent les filtres ; les fiches sont exportables en JSON. Les cartes peuvent être agrandies, déplacées et zoomées. Sur mobile, le menu est accessible par ☰ et les cartes s’ouvrent à un zoom lisible.

Le module de qualification des points de contrôle n’est pas intégré. Les mentions métier des documents d’origine sont conservées. Les sources et références sont accessibles depuis les fiches ; les documents sources sont téléchargeables dans la bibliothèque. Les relations à confirmer restent signalées, les parts de réassurance ne sont pas agrégées et le panel placé par Guy Carpenter n’est pas réparti arbitrairement entre ses membres.

## Code et vérifications

Le [code source de l’outil](cartographies-keel/README.md) permet de reconstruire le HTML avec Python standard. Les sources comprennent 1 140 objets et 1 251 relations documentaires, sans iframe ni dépendance réseau à l’exécution.

Le [rapport de validation](VALIDATION-CARTOGRAPHIES-KEEL.md) détaille les contrôles réalisés : 24 vues, 3 420 rendus de fiches/liens/sources, navigation, zoom, matrices, filtres, recherche, favoris, exports et mobile. Les collections principales ont été comparées aux données d’origine ; les 28 conditions de réassurance et le classeur exporté ont été vérifiés. Aucune erreur JavaScript ni requête externe observée dans les parcours contrôlés hors ligne.

Cette livraison est ajoutée à la branche dédiée du dépôt public avec l’autorisation de son propriétaire. Aucun site n’est déployé et aucun fichier du dépôt Keel n’est modifié.
