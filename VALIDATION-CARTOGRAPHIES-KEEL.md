# Vérification de la refonte des cartographies

La livraison reconstruit les cinq cartographies dans une application native au langage visuel de Keel. Les anciennes pages ne sont pas imbriquées dans l’interface. Le HTML autonome contient les données, les polices, les documents sources et le code applicatif.

## Données

- 1 140 objets natifs et identifiants uniques ; 1 251 relations dont les deux extrémités existent.
- Collections comparées aux données d’origine : 102 processus, 14 fonctions, 6 chaînes de valeur, 3 entités, 7 produits, 16 acteurs produits, 10 parcours, 105 offres, 36 partenaires, 145 rubriques de convention, 242 flux partenaires et 206 acteurs de partenaires.
- 46 outils et 36 flux SI identiques aux collections de la pièce finale ; conservation des 6 statuts « à confirmer » et des 5 flux portant des précisions ouvertes dans leur détail. Le graphe comporte 31 nœuds ; les 5 interfaces sans fiche outil ne sont pas ajoutées au compteur des outils.
- 52 rubriques Omega, 15 personnes citées, 7 points d’attention de la source outils et 19 formules Santé conservés.
- Les 28 lignes de Synthese_Traites.xlsx ont été comparées aux données extraites du classeur, notamment les parts, périodes et commissions. Les 12 libellés de réassureurs ou de panel restent distincts ; les parts ne sont pas agrégées ni réparties au sein du panel.
- Les cinq documents sources ont été vérifiés par empreinte et comparaison binaire. Le classeur téléchargé depuis l’outil est identique au fichier fourni.

## Navigation et interfaces

Vérifications dans Chromium avec Playwright, contexte navigateur hors ligne :

- 26 vues des cinq univers ouvertes sans erreur JavaScript.
- Restitution des trois rubriques Fiche, Liens et Source pour les 1 140 objets : 3 420 rendus contrôlés.
- Ouverture réelle dans le panneau et navigation entre les trois rubriques pour les 22 types d’objets.
- Navigation par chaîne de valeur, dépliage des fonctions, sélection des processus, filtres de texte, entité, type et statut, réinitialisation et états sans résultat.
- Cartes SVG : sélection d’un nœud et d’un flux, zoom, ajustement, déplacement, mode agrandi, commandes clavier et conservation du niveau de lecture sur mobile.
- Matrices Partenaires et Réassureurs : ouverture des résultats filtrés correspondant exactement à la case choisie.
- Recherche globale et par univers, navigation clavier dans les résultats et ouverture de la fiche trouvée.
- Comparateur produits, choix des formules Santé et recherche de garantie.
- Ajout et retrait de favoris, persistance après rechargement, sauvegarde et restauration.
- Navigation précédent/suivant du navigateur et lien d’accès direct au contenu.
- Aide, raccourci Ctrl K, recherche limitée à un univers, tri, pagination du catalogue et des tableaux, ouverture des nœuds SVG accessibles et gestion d’un fichier de favoris invalide.

## Exports et fichier autonome

- CSV des résultats filtrés, CSV du comparateur et CSV des garanties Santé.
- Export JSON d’une fiche, contenu de commission conservé.
- Export et import des favoris.
- Téléchargement du classeur source, empreinte et octets identiques à l’original.
- Téléchargement de la copie HTML depuis l’outil, puis réouverture et navigation dans cette copie.
- Aucune iframe dans l’interface, aucune requête externe ni erreur JavaScript dans les parcours contrôlés.

## Mobile

Les cinq univers, l’accueil et les sources ont été contrôlés à 390 × 844 px. Aucun débordement horizontal du document ; les grandes matrices et tableaux défilent à l’intérieur de leur conteneur. Le menu se ferme après sélection. Les fiches occupent la largeur du téléphone, libèrent la navigation après fermeture et gèrent Échap. Les cartes s’ouvrent à un zoom lisible et se déplacent au doigt.

## Portée des vérifications

Les contrôles confirment la migration documentaire et les parcours techniques décrits ; ils ne certifient pas les informations métier ni le statut actuel des conventions ou traités. Les tests chargent le HTML complet depuis une adresse locale interceptée en mode hors ligne : la politique du navigateur cloud bloque `file://`. Aucune politique de sécurité n’a été désactivée. Le code source de la livraison contient les tests de navigation réexécutables.

## Schémas de réassurance ajoutés

Les 28 lignes de synthèse ont été visualisées dans chacun des deux circuits, soit 56 schémas. Les cinq blocs BtoBtoC et les quatre blocs sans partenaire sont générés avec les libellés du référentiel. La sélection d’une ligne, l’ouverture des fiches sans quitter le schéma, les liens directs, le choix manuel et le rétablissement de la correspondance source ont été contrôlés.

Les références des 12 rapprochements documentaires et des 7 ensembles de produits de référence existent dans le référentiel. Les 1 140 objets et les 1 251 relations sources restent inchangés. Les programmes sans correspondance restent sans partenaire par défaut ; les choix manuels sont explicitement qualifiés. Les rôles Auvray/FMA et la divergence Mutualia/Harmonie ont fait l’objet d’assertions dédiées.

Les deux exports SVG ont été téléchargés et validés comme XML SVG ; ils contiennent les polices et leurs licences, les parts, les périodes et les réserves de lecture. Les vues ont été contrôlées à 390 px, y compris l’ouverture et la fermeture des fiches et la libération de la navigation. Aucune erreur JavaScript ni requête externe observée. Le manifeste du jeu de données a été actualisé ; les documents originaux restent identiques.
