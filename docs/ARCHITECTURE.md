# Architecture de l'application KALONJI

## Vue d'ensemble

L'application **Algorithme Lithiase KALONJI** est une application web médicale développée avec Flask (Python) pour la gestion et l'analyse des calculs rénaux. Elle utilise une architecture moderne et modulaire avec des services séparés, un algorithme d'inférence sophistiqué, et des fonctionnalités de sécurité avancées.

## Stack technique

### Backend
- **Framework**: Flask 3.0.0
- **ORM**: SQLAlchemy avec Flask-SQLAlchemy 3.1.1
- **Base de données**: PostgreSQL (via Replit Neon)
- **Authentification**: Flask-Login 0.6.3
- **Sécurité CSRF**: Flask-WTF 1.2.2
- **Chiffrement**: Cryptography (Fernet AES-128 + HMAC)
- **Export PDF**: ReportLab 4.0.7
- **QR Codes**: qrcode[pil]
- **Driver PostgreSQL**: psycopg2-binary 2.9.11

### Frontend
- **Templates**: Jinja2
- **Styling**: Tailwind CSS (CDN)
- **JavaScript**: Vanilla JS
- **Design system**: MyOneArt (indigo-purple palette)

## Structure des dossiers

```
project/
├── backend/
│   ├── __init__.py                 # Factory Flask avec configuration DB/CSRF
│   ├── constants.py                # Constantes et choix de formulaires
│   ├── models/
│   │   └── __init__.py            # Modèles SQLAlchemy (User, Patient, Episode, etc.)
│   ├── routes/
│   │   ├── auth.py                # Routes d'authentification
│   │   ├── patients.py            # CRUD patients
│   │   ├── episodes.py            # CRUD épisodes médicaux
│   │   ├── imageries.py           # Gestion données d'imagerie
│   │   ├── biologies.py           # Gestion données biologiques
│   │   ├── search.py              # Recherche avancée
│   │   ├── exports.py             # Export PDF/CSV
│   │   └── settings.py            # Paramètres utilisateur
│   ├── services/
│   │   ├── __init__.py
│   │   ├── inference_service.py   # Moteur d'inférence des types de calculs
│   │   └── biology_service.py     # Calculs métaboliques automatiques
│   ├── database/
│   │   ├── __init__.py
│   │   └── init.py                # Initialisation schéma DB
│   └── utils/
│       └── crypto.py              # Gestionnaire de chiffrement Fernet
├── static/
│   ├── css/
│   │   └── myoneart.css          # Styles personnalisés
│   ├── js/                        # Scripts JavaScript (future utilisation)
│   └── images/
│       ├── favicon.png
│       └── logo.png
├── templates/
│   ├── login.html
│   ├── dashboard.html
│   ├── nouveau-patient.html
│   ├── patient.html
│   ├── liste-patients.html
│   ├── search.html
│   └── parametres.html
├── docs/
│   ├── ARCHITECTURE.md            # Ce fichier
│   ├── API_DOCUMENTATION.md       # Documentation API REST
│   └── DEPLOYMENT.md              # Guide de déploiement
├── app.py                         # Point d'entrée de l'application
├── requirements.txt               # Dépendances Python
└── migrate_sqlite_to_postgres.py  # Script de migration de données

```

## Modèles de données

### 1. User
- Gestion des utilisateurs avec hash PBKDF2
- Un seul utilisateur admin par défaut

### 2. Patient
- **Données chiffrées** (25+ champs sensibles): nom, prénom, téléphone, email, adresse, antécédents, notes médicales, etc.
- Calcul automatique de l'IMC (poids/taille²)
- Code patient unique (UUID) avec génération QR Code
- Relations: 1-N avec Episode

### 3. Episode
- Représente une consultation ou un événement médical
- Données chiffrées: motif, diagnostic, traitement, notes
- Stockage du résultat d'inférence (JSON)
- Relations: 1-N avec Imagerie et Biologie

### 4. Imagerie
- Scanner, échographie, ASP
- Densité UH, taille, morphologie, topographie
- Support structure radiaire (noyau + couches périphériques)
- Données chiffrées: commentaires, topographie, forme

### 5. Biologie
- pH urinaire, densité, ECBU
- Marqueurs métaboliques: hyperoxalurie, hypercalciurie, hyperuricurie, cystinurie
- Hormones thyroïdiennes: T3, T4, TSH
- Calcul automatique des marqueurs booléens à partir des valeurs numériques
- Seuils genrés (hommes vs femmes)

## Services métier

### Inference Service
Moteur d'inférence pour déterminer le type de calcul rénal:
- **8 types de calculs** supportés (Whewellite, Weddellite, Carbapatite, Brushite, Struvite, Cystine, Acide urique, Urate ammonium)
- **Système de scoring** multi-critères:
  - Densité UH (0-6 points)
  - Morphologie (0-3 points)
  - pH urinaire (0-3 points)
  - Marqueurs métaboliques (0-5 points avec bonus thyroïde/calcium)
  - Infection (0-3 points)
  - Radio-opacité (0-1 point)
- **Distinction Pur vs Mixte**: basée sur l'écart de score entre les 3 premiers candidats
- **Détection structure radiaire**: analyse noyau + couches périphériques
- **Recommandations**: voie de traitement (LEC/URS/PCNL) et prévention personnalisée

### Biology Service
Calculs métaboliques automatiques:
- **Hyperoxalurie**: oxalurie > 45 mg/24h
- **Hypercalciurie**: calciurie > 300 mg/24h (homme) ou > 250 mg/24h (femme)
- **Hypercalcémie**: calcémie > 2.6 mmol/L
- **Hyperthyroïdie**: TSH < 0.4 ET (T3 > 2.0 OU T4 > 12.0)

## Sécurité

### Chiffrement des données
- **Algorithme**: Fernet (AES-128 en mode CBC + HMAC-SHA256)
- **Clé**: Stockée dans `.encryption_key` (dev) ou variable d'environnement `ENCRYPTION_KEY` (prod)
- **Champs chiffrés**: 25+ colonnes contenant des données sensibles (nom, prénom, antécédents, notes, etc.)
- **Propriétés Python**: Chiffrement/déchiffrement transparent via properties

### Protection CSRF
- **Flask-WTF**: Protection CSRF sur toutes les routes POST/PUT/DELETE
- **Token CSRF**: Généré automatiquement et inclus dans les formulaires via `csrf_token()`
- **Exemption API**: Les endpoints API utilisent l'authentification de session

### Authentification
- **Flask-Login**: Gestion des sessions utilisateur
- **Hash PBKDF2**: Hachage sécurisé des mots de passe
- **Protection des routes**: Décorateur `@login_required` sur toutes les routes sensibles

## Base de données

### Configuration PostgreSQL
- **Pooling**: pool_recycle=300s, pool_pre_ping=True
- **SSL**: sslmode=require pour connexions sécurisées
- **Fallback**: SQLite en dev si DATABASE_URL non défini
- **Initialisation**: Schéma créé automatiquement via `db.create_all()` dans `backend/database/init.py`

### Migration SQLite → PostgreSQL
Script `migrate_sqlite_to_postgres.py` disponible pour migration des données existantes.

## Constantes et choix

Fichier `backend/constants.py` centralise tous les choix de formulaires:
- SEXE_CHOICES
- LATERALITE_CHOICES
- FORME_CALCUL_CHOICES
- CONTOUR_CALCUL_CHOICES
- TOPOGRAPHIE_CALCUL_CHOICES
- MORPHOLOGIE_CHOICES
- RADIO_OPACITE_CHOICES
- GERME_CHOICES
- REGIME_ALIMENTAIRE_CHOICES
- GROUPE_ETHNIQUE_CHOICES
- HYDRATATION_CHOICES
- TYPE_CALCUL_CHOICES
- COMPOSITION_TYPE_CHOICES
- VOIE_TRAITEMENT_CHOICES

Fonctions utilitaires:
- `get_choice_label(choices, value)`: Récupère le label d'un choix
- `get_choice_values(choices)`: Liste des valeurs possibles
- `get_choice_dict(choices)`: Dictionnaire value→label

## API REST

Voir [API_DOCUMENTATION.md](API_DOCUMENTATION.md) pour la documentation complète des endpoints.

### Endpoints principaux
- `POST /login`, `GET /logout` - Authentification
- `GET|POST /api/patients` - CRUD patients
- `GET|POST /api/patients/<id>/episodes` - CRUD épisodes
- `POST /api/export/csv` - Export recherche CSV
- `POST /api/export/patients-csv` - Export liste patients CSV
- `GET /api/patients/<id>/export/pdf` - Export dossier patient PDF

## Déploiement

Voir [DEPLOYMENT.md](DEPLOYMENT.md) pour les instructions complètes.

### Variables d'environnement requises
- `DATABASE_URL`: URI PostgreSQL (fourni automatiquement par Replit)
- `SECRET_KEY`: Clé secrète Flask (obligatoire en production)
- `ENCRYPTION_KEY`: Clé de chiffrement Fernet (obligatoire en production)
- `ADMIN_USERNAME`: Nom d'utilisateur admin (défaut: admin)
- `ADMIN_PASSWORD`: Mot de passe admin (défaut: admin123)
- `SKIP_DB_INIT`: 'true' pour désactiver l'initialisation auto (tests)

### Commandes de démarrage
```bash
# Développement
python app.py

# Production (recommandé)
gunicorn --bind=0.0.0.0:5000 --reuse-port app:app
```

## Workflow de développement

1. **Modifications modèles**: Mettre à jour `backend/models/__init__.py`
2. **Ajout de logique métier**: Créer un service dans `backend/services/`
3. **Nouvelles routes**: Ajouter un blueprint dans `backend/routes/`
4. **Migration DB**: Exécuter `migrate_sqlite_to_postgres.py` si nécessaire
5. **Tests**: Valider avec données de test avant déploiement
6. **Documentation**: Mettre à jour docs/ en conséquence

## Bonnes pratiques

- ✅ Utiliser les constantes de `backend/constants.py` au lieu de chaînes en dur
- ✅ Toujours chiffrer les données sensibles via properties
- ✅ Protéger les routes avec `@login_required`
- ✅ Valider les entrées utilisateur
- ✅ Utiliser les services pour la logique métier complexe
- ✅ Documenter les nouveaux endpoints dans API_DOCUMENTATION.md
- ✅ Tester les migrations sur une copie avant production
- ✅ Utiliser les variables d'environnement pour les secrets
- ✅ Sauvegarder régulièrement la base de données PostgreSQL

## Support et maintenance

- **Logs**: Consultables via le dashboard Replit
- **Sauvegarde DB**: Exporter régulièrement via pgdump ou interface Replit
- **Monitoring**: Surveiller les métriques PostgreSQL (connexions, lenteurs)
- **Mises à jour**: Vérifier régulièrement les dépendances (`pip list --outdated`)

## Versions

- **Version actuelle**: 1.0.0
- **Dernière mise à jour**: Novembre 2025
- **Compatibilité**: Python 3.11+, PostgreSQL 13+
