# ACHEEL — Cartographies · Interface et navigation

[**Télécharger le ZIP**](dist/acheel-cartographies.zip), extraire l’archive puis ouvrir `acheel-cartographies.html` dans Chrome ou Edge. Le [HTML seul](dist/acheel-cartographies.html) est aussi disponible. [Aperçu de l’accueil](dist/apercu-cartographies.png).

## Cinq cartographies, une navigation commune

- Fonctionnement : 102 processus répartis dans 14 fonctions.
- Produits : 7 produits documentés.
- Partenaires : 36 libellés de partenaires présents dans les données intégrées, y compris les éléments complémentaires à Deemeter.
- Outils : 46 outils avec leurs flux et circuits.
- Réassureurs : 28 lignes de synthèse, 12 libellés de réassureurs ou de panel et 8 périmètres.

L’accueil, le menu latéral, les raccourcis, la recherche globale et la recherche par cartographie permettent d’ouvrir directement les fiches. Le mode agrandi donne davantage de place aux cartes ; Échap rétablit le menu. Sur mobile, la navigation est accessible par le bouton ☰. Le téléchargement HTML enregistre une copie autonome complète.

L’habillage reprend le logo, le bleu #1E96FC, les titres Outfit et les textes Nunito observables sur le [site ACHEEL](https://v2.acheel.com/). Les polices et le logo sont intégrés au fichier pour le fonctionnement hors ligne. Les cinq cartographies partagent cet habillage. Il ne s’agit pas d’une certification de conformité à un manuel de marque interne non fourni.

## Corrections de fonctionnement

Les liens internes restent dans la cartographie au lieu de charger une seconde copie du portail dans son cadre. La navigation Fonctionnement utilise une URL locale explicite, compatible avec l’intégration autonome. Les boutons ouvrant une fiche ou un acteur ne réinitialisent plus la vue. Les anciennes fiches produits externes sont remplacées par le dépliage de la fiche intégrée. Les vues participent à l’historique précédent/suivant du navigateur.

Cette version n’intègre pas le module de qualification des points de contrôle. Les mentions métier présentes dans les cartographies sources sont conservées.

## Sources et réassurance

Fonctionnement, produits et partenaires : cartographies originales intégrées à la livraison V2 du dépôt. Outils : version finale de la cartographie des outils ACHEEL. Réassureurs : `Synthese_Traites.xlsx`, feuille Synthèse, cellules A2:F29. Les données du classeur sont accessibles dans les fiches avec référence à la ligne d’origine. La carte propose filtres, tableau, export CSV filtré et téléchargement du classeur exact.

Le panel placé par Guy Carpenter reste groupé. Aucune quote-part par membre n’est inventée. Les périodes sont reproduites sans présumer du statut actuel des traités ; les quotes-parts de lignes différentes ne sont pas additionnées. Les codes P1 à P8 ne sont pas rapprochés arbitrairement de produits. Les conditions de commission sont conservées telles que fournies.

## Vérifications

Contrôles navigateur sous Chromium : onglets des cartographies ; destination des 233 entrées détaillées de la recherche (14 fonctions, 102 processus, 7 produits, 36 partenaires, 46 outils, 28 lignes de réassurance) ; fiches acteur, étape, produit et aide ; historique précédent/suivant ; recherche globale et locale ; mode agrandi ; téléchargement et réouverture de la copie HTML. Les 28 périodes, parts et commissions de réassurance ont été comparées aux données extraites du classeur. Le CSV filtré et l’identité binaire du classeur téléchargé ont été vérifiés. Les cinq univers et l’accueil ont été vérifiés à 390 px. Aucune requête externe ni erreur JavaScript observée pendant les parcours testés hors ligne.

La navigation `file://` est bloquée par la politique du navigateur cloud : le HTML autonome a été testé depuis une adresse locale interceptée, avec réseau hors ligne. L’ouverture directe du fichier reste soumise aux règles du poste utilisateur. Les vérifications techniques ne valident pas les informations métier.

Les fichiers sont ajoutés au dépôt public avec l’autorisation explicite de son propriétaire. Aucun site n’est déployé.
