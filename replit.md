# Webapp Lithiase - Application médicale de gestion de calculs rénaux

## Vue d'ensemble
Application web mono-médecin pour la gestion des dossiers patients souffrant de lithiase (calculs rénaux). L'application permet de saisir des dossiers complets, d'obtenir des propositions de type de calcul via un moteur d'inférence, et de générer des rapports PDF.

## Architecture
- **Backend**: Flask (Python 3.11) avec SQLAlchemy ORM
- **Chiffrement**: Cryptography (Fernet) pour données de santé
- **Frontend**: HTML/CSS avec Tailwind CSS + JavaScript vanilla
- **Base de données**: SQLite
- **Exports**: PDF (ReportLab) et CSV

## Structure du projet
```
/
├── app.py                     # Point d'entrée Flask
├── backend/                   # Backend organisé
│   ├── __init__.py           # Initialisation Flask + blueprints
│   ├── inference.py          # Moteur d'inférence
│   ├── models/               # Modèles avec chiffrement
│   │   └── __init__.py      # Patient, Episode, Imagerie, Biologie
│   ├── routes/               # Routes par domaine
│   │   ├── auth.py          # Authentification
│   │   ├── patients.py      # CRUD patients
│   │   ├── episodes.py      # CRUD épisodes + inférence
│   │   ├── imageries.py     # CRUD imageries
│   │   ├── biologies.py     # CRUD biologies
│   │   ├── search.py        # Recherche avancée
│   │   └── exports.py       # Exports PDF/CSV
│   └── utils/                # Utilitaires
│       └── crypto.py         # Gestionnaire chiffrement Fernet
├── templates/                # Templates HTML
├── static/                   # Fichiers statiques
├── uploads/                  # Documents uploadés
├── requirements.txt          # Dépendances Python
├── PROJECT_TRACKING.md       # Suivi complet du projet
├── TESTS.md                  # Tests d'acceptation
└── lithiase.db              # Base de données SQLite
```

## Fonctionnalités principales
1. **Gestion des patients**: Fiche complète (identité, antécédents, traitements)
2. **Épisodes médicaux**: Coliques néphrétiques, suivi, récidives
3. **Examens**: Imagerie (scanner) et biologie
4. **Moteur d'inférence**: Classification automatique du type de calcul (8 types couverts)
5. **Recherche avancée**: Filtres multiples (pH, UH, type, infection, etc.)
6. **Exports**: PDF (rapport patient) et CSV (données filtrées)

## Types de calculs couverts
- Oxalate de calcium (Whewellite, Weddellite)
- Phosphates calciques (Carbapatite, Brushite)
- Struvite (infectieux)
- Cystine
- Acide urique
- Urate d'ammonium

## Changements récents
- **✅ COMPLÉTÉ** (09/11/2025): Enrichissement complet de l'algorithme d'inférence et documentation
  - **Type de calcul persistant** : Le résultat de l'inférence est maintenant sauvegardé dans la base de données
    - Nouveaux champs dans Episode : `calculated_stone_type`, `calculated_stone_type_data` (JSON), `calculated_at`
    - Plus besoin de recalculer le type à chaque affichage ou export
    - Migration SQLite automatique pour ajouter les colonnes
  - **Algorithme d'inférence enrichi** : Intégration de tous les nouveaux champs
    - Forme du calcul (sphérique lisse, irrégulière spiculée, crayeuse, coralliforme)
    - Contour du calcul (régulier, irrégulier)
    - Nombre de calculs
    - Topographie précise
    - Sédiment urinaire
    - Résultats ECBU
  - **Affichage enrichi** : Toutes les pages patient affichent maintenant les données détaillées
    - Nombre de calculs, topographie, forme, contour
    - Sédiment urinaire, ECBU
    - Détails ASP, échographie, uro-scanner
  - **Export PDF amélioré** : Rapport complet avec toutes les données
    - Utilisation du type de calcul persistant (pas de recalcul)
    - Affichage de la date de calcul
    - Top 3 des types de calculs avec scores
    - Nouveaux champs d'imagerie et biologie
  - **Documentation complète** : Dossier docs/ créé avec 3 fichiers
    - **README.md** : Vue d'ensemble, fonctionnalités, cas d'usage
    - **TECHNIQUE.md** : Architecture, technologies, modèle de données, API, sécurité
    - **ALGORITHME.md** : Explication détaillée du moteur d'inférence (système de notation, types de calculs, exemples)
  - **Navigation améliorée** : Lien "➕ Nouveau Patient" ajouté dans tous les menus
  - **Validation** : Architecture complète validée par architect (PASS)

- **✅ COMPLÉTÉ** (09/11/2025): Patients de démonstration et page de paramètres
  - **Script de démonstration** : create_demo_patients.py crée 4 patients avec données complètes
    - Jean Dupont (M, 48 ans) : Oxalate de calcium, récidivant, mauvaise observance
    - Sophie Martin (F, 37 ans) : Oxalate + infections urinaires, maladie de Crohn
    - Karim Benali (M, 43 ans) : Acide urique, syndrome métabolique, pH acide
    - Claire Lefebvre (F, 30 ans) : Cystinurie homozygote, suivi excellent
  - **Section "Objectifs de l'analyse"** : Ajoutée dans patient.html avec design indigo/purple
    - 5 objectifs clés selon classification Daudon
    - Visible sur toutes les fiches patients
  - **Page Paramètres** : /parametres complète et fonctionnelle
    - Modification du profil utilisateur
    - Changement de mot de passe sécurisé
    - Statut du chiffrement des données
    - Informations système
    - Zone de danger avec sauvegarde/export (en développement)
  - **Navigation** : Lien "⚙️ Paramètres" ajouté dans toutes les pages
  - **Backend** : Route backend/routes/settings.py avec API JSON sécurisée

## Changements récents (Archive)
- 2025-10-26: Création initiale du projet
- Configuration de l'environnement Python 3.11
- Structure de base du projet
- Implémentation complète du backend Flask avec SQLAlchemy
- Création du moteur d'inférence avec 8 types de calculs
- Interface utilisateur complète avec Tailwind CSS
- Système d'export PDF et CSV
- Authentification sécurisée avec variables d'environnement
- Correction du bug de filtrage des patients (SQLAlchemy query filter)
- **NOUVEAU**: Refactorisation backend en architecture modulaire (backend/routes, backend/models, backend/utils)
- **NOUVEAU**: Chiffrement des données de santé (Fernet) - 17 champs sensibles chiffrés
- **NOUVEAU**: Gestionnaire de chiffrement avec clé d'environnement (ENCRYPTION_KEY)
- **NOUVEAU**: Properties Python pour chiffrement/déchiffrement transparent
- **NOUVEAU**: Documentation complète (PROJECT_TRACKING.md avec 400+ lignes)
- **✅ COMPLÉTÉ**: Migration vers le système de design MyOneArt
  - Centralization CSS complète dans static/css/myoneart.css (renommé depuis mysindic.css)
  - Palette indigo-purple avec gradients (#667eea → #764ba2)
  - Bordures arrondies (1-2rem) et boutons transparents avec contours colorés
  - Utilisation d'emojis amicaux pour l'interface
  - Suppression totale des styles inline des templates
  - Pattern "btn btn-{variant}" appliqué à tous les boutons
  - Classes modales standardisées (modal-md, modal-lg, modal-sm)
  - Tables de données stylisées avec classe data-table
  - Design moderne et production-ready validé par architect
- **✅ COMPLÉTÉ**: Formulaire patient complet dans le dashboard
  - Tous les champs du cahier des charges implémentés
  - Antécédents familiaux, chirurgicaux
  - Traitements chroniques avec posologies
  - Régime alimentaire
  - Notes libres
- **✅ COMPLÉTÉ**: Page patient avec dossier médical complet
  - Section informations personnelles (identité, contacts, adresse)
  - Section antécédents médicaux complets (personnels, familiaux, chirurgicaux, allergies, traitements)
  - Section facteurs de risque & hygiène de vie (hydratation, régime)
  - Section notes (affichage conditionnel)
  - Affichage conditionnel de toutes les sections (ne montre que les champs remplis)
  - Intégration harmonieuse avec les épisodes, imageries, biologies et moteur d'inférence
- **✅ COMPLÉTÉ** (08/11/2025): Extensions pour analyse par IA des calculs rénaux
  - **Modèle Patient étendu** : 9 nouveaux champs chiffrés (poids, taille, groupe ethnique, petit_dejeuner, dejeuner, diner, grignotage, autres_consommations)
  - **Modèle Imagerie étendu** : 13 nouveaux champs (asp_resultats, echographie_resultats, uroscanner_resultats, nombre_calculs, situation_calculs, topographie_calculs, dimensions_calculs, forme_calculs, contours_calculs, densite_noyau, densite_couches, calcifications_autres)
  - **Modèle Biologie étendu** : 3 nouveaux champs chiffrés (densite_urinaire, sediment_urinaire, ecbu_resultats)
  - **Dashboard amélioré** : Statistiques temps réel (total patients, épisodes, IMC moyen, dossiers prêts pour IA)
  - **Formulaire patient enrichi** : Intégration complète des nouvelles données anthropométriques et alimentaires
  - **Page patient augmentée** : Affichage IMC automatique, détails alimentaires complets, informations imagerie détaillées
  - **Système d'explication** : Documentation intégrée du système de notation de l'algorithme d'inférence (20 points)
  - **Total champs chiffrés** : 25+ champs sensibles protégés par Fernet AES-128
  - **Validation** : Architecture revue et approuvée par architect (PASS)
- **✅ COMPLÉTÉ** (08/11/2025): Transformation du formulaire patient en page complète
  - **Page dédiée** : nouveau-patient.html - formulaire complet sur une page dédiée (plus de modal popup)
  - **Navigation** : Lien "Nouveau Patient" dans le dashboard redirige vers /nouveau-patient
  - **Extension modèle Patient** : Tous les champs imagerie et laboratoire directement dans le modèle Patient (asp_resultats, echographie_resultats, uroscanner_resultats, sediment_urinaire, ecbu_resultats, ph_urinaire, densite_urinaire, nombre_calculs, topographie_calcul, diametre_longitudinal, diametre_transversal, forme_calcul, contour_calcul, densite_noyau, densites_couches, calcifications_autres)
  - **Sections organisées** : Informations personnelles, anthropométrie, antécédents médicaux, habitudes alimentaires, imagerie médicale, résultats de laboratoire, détails des calculs
  - **Styling** : Border-radius réduit à 0.5rem pour tous les champs de formulaire
  - **Backend** : Routes /nouveau-patient (GET) et /api/patients (POST/GET/PUT) gèrent tous les nouveaux champs
  - **Chiffrement** : Tous les champs sensibles sont chiffrés avec Fernet AES-128
  - **Tests** : Création et récupération de patient avec tous les champs validés en end-to-end
  - **Validation** : Architecture complète validée par architect (PASS)
- **✅ COMPLÉTÉ** (08/11/2025): Refonte UX/UI du formulaire patient selon classification Daudon
  - **Section Objectifs** : Nouveau bloc en haut du formulaire expliquant les 5 objectifs de l'analyse (classification Daudon, détection anomalies, régime adapté, traitement scientifique, gestion infections)
  - **Système de couleurs par section** : Chaque section a une couleur distinctive (bleu=infos personnelles, vert=anthropométrie, rouge=antécédents, jaune=alimentation, violet=imagerie, turquoise=laboratoire, gris=notes)
  - **Réorganisation des blocs** : Groupe ethnique déplacé dans Informations personnelles, Hydratation déplacée dans Habitudes alimentaires
  - **Calcul IMC automatique** : JavaScript calcule et affiche l'IMC en temps réel avec classification colorée (sous-poids=bleu, normal=vert, surpoids=jaune, obésité=rouge)
  - **Intégration Uro-scanner** : Détails des calculs rénaux (dimensions, forme, contour, densités) intégrés directement dans la section Uro-scanner
  - **Fusion topographie** : Suppression du champ `situation_calcul` au profit d'un champ unique `topographie_calcul` incluant rein + localisation
  - **Renommage terminologie** : "Traitements chroniques" → "Traitements en cours" pour refléter l'état actuel
  - **Pièces jointes (préparation)** : 3 nouvelles colonnes dans le modèle (fichier_imagerie, fichier_laboratoire, fichier_ordonnance) pour implémentation future de l'upload de documents
  - **Tests end-to-end** : Création/récupération de patients validées avec nouveau schéma
  - **Validation** : Architecture complète validée par architect (PASS)

## Sécurité
- Authentification simple mono-utilisateur (Flask-Login)
- Hachage des mots de passe (Werkzeug PBKDF2)
- **Chiffrement des données de santé** (Fernet AES-128 + HMAC)
- **25+ champs sensibles chiffrés** en base de données (données personnelles, médicales, anthropométriques, alimentaires)
- Clé de chiffrement configurable via ENCRYPTION_KEY
- Conformité RGPD pour la protection des données personnelles
- Base de données SQLite avec colonnes chiffrées
- Session locale sécurisée
- Variables d'environnement pour credentials (ADMIN_USERNAME, ADMIN_PASSWORD)
