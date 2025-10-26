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

## Sécurité
- Authentification simple mono-utilisateur (Flask-Login)
- Hachage des mots de passe (Werkzeug PBKDF2)
- **Chiffrement des données de santé** (Fernet AES-128 + HMAC)
- 17 champs sensibles chiffrés en base de données
- Clé de chiffrement configurable via ENCRYPTION_KEY
- Conformité RGPD pour la protection des données personnelles
- Base de données SQLite
- Session locale sécurisée
- Variables d'environnement pour credentials (ADMIN_USERNAME, ADMIN_PASSWORD)
