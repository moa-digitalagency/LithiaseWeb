# Algorithme Lithiase KALONJI - Application Médicale Sécurisée

Application web de gestion de calculs rénaux pour médecins avec **chiffrement des données de santé**.

## 🔒 Sécurité - Chiffrement des Données

### Données chiffrées (conformité RGPD)
Toutes les données personnelles et médicales sensibles sont **chiffrées en base de données** :
- **Identité patient**: nom, prénom, téléphone, email, adresse
- **Antécédents**: personnels, familiaux, chirurgicaux, allergies, traitements
- **Données cliniques**: motif, diagnostic, germe, symptômes, traitements
- **Notes médicales**: tous les champs de notes et commentaires

### Configuration du chiffrement

**Pour la première utilisation:**
Une clé de chiffrement est générée automatiquement et sauvegardée dans `.encryption_key`.

**Pour la production (OBLIGATOIRE):**
```bash
# Générer une clé sécurisée
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"

# Définir la variable d'environnement
export ENCRYPTION_KEY="votre_cle_generee_ici"

# Lancer l'application
python app.py
```

⚠️ **IMPORTANT**: Sans la clé de chiffrement, les données chiffrées sont **irrécupérables** !

## 📁 Structure du Projet (Architecture Backend)

```
webapp-lithiase/
├── app.py                      # Point d'entrée de l'application
├── backend/                    # Backend structuré
│   ├── __init__.py            # Initialisation Flask + blueprints
│   ├── inference.py           # Moteur d'inférence (8 types de calculs)
│   ├── models/                # Modèles avec chiffrement
│   │   └── __init__.py        # Patient, Episode, Imagerie, Biologie, etc.
│   ├── routes/                # Routes organisées par domaine
│   │   ├── auth.py           # Authentification
│   │   ├── patients.py       # CRUD patients
│   │   ├── episodes.py       # CRUD épisodes + inférence
│   │   ├── imageries.py      # CRUD imageries (scanner)
│   │   ├── biologies.py      # CRUD biologies
│   │   ├── search.py         # Recherche avancée
│   │   └── exports.py        # Exports PDF/CSV
│   └── utils/                 # Utilitaires
│       └── crypto.py          # Gestionnaire de chiffrement Fernet
├── templates/                  # Templates HTML
│   ├── login.html
│   ├── dashboard.html
│   ├── patient.html
│   └── search.html
├── static/                     # Fichiers statiques
├── uploads/                    # Documents uploadés
├── requirements.txt
├── README.md
├── PROJECT_TRACKING.md         # Suivi détaillé du projet
└── TESTS.md                    # Critères d'acceptation
```

## 🚀 Installation

### 1. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 2. Configurer les variables d'environnement (optionnel)

**Credentials admin:**
```bash
export ADMIN_USERNAME=votre_username
export ADMIN_PASSWORD=votre_mot_de_passe_securise
```

**Clé de chiffrement:**
```bash
export ENCRYPTION_KEY=votre_cle_de_chiffrement_fernet
```

**Clé secrète Flask:**
```bash
export SECRET_KEY=votre_cle_secrete_flask
```

### 3. Lancer l'application
```bash
python app.py
```

### 4. Accéder à l'application
- **URL**: http://localhost:5000
- **Username par défaut**: `admin`
- **Password par défaut**: `admin123`

⚠️ **Changez les credentials en production !**

## 📋 Fonctionnalités

### Gestion Complète des Patients
- ✅ **Fiche patient** avec identité, antécédents, allergies, traitements
- ✅ **Épisodes médicaux** (coliques néphrétiques, récidives)
- ✅ **Examens** (imagerie scanner + biologie)
- ✅ **Timeline chronologique** des événements
- ✅ **Traçabilité** (dates création/modification)

### Moteur d'Inférence Intelligent
- ✅ **8 types de calculs** couverts
- ✅ **Analyse multicouche** ⭐ NOUVEAU: Détection et analyse des structures radiaires (noyau + couches périphériques)
- ✅ **Identification par couche**: Composition probable de chaque couche basée sur la densité UH
- ✅ **Système de scoring** transparent (0-20 points) avec bonus multicouche (+2 pts)
- ✅ **Top 3** des types les plus probables
- ✅ **Justification détaillée** avec règles explicites et analyse structurelle
- ✅ **Badge d'incertitude** si scores proches
- ✅ **Éligibilité LEC** (lithotripsie)
- ✅ **Voie de traitement** recommandée
- ✅ **Conseils de prévention** personnalisés

### Recherche & Exports
- ✅ **Recherche avancée** avec filtres multiples
- ✅ **Export PDF** (dossier patient complet)
- ✅ **Export CSV** (données filtrées)

## 🏥 Types de Calculs Couverts

1. **Oxalate de calcium**
   - Whewellite (monohydrate)
   - Weddellite (dihydrate)

2. **Phosphates calciques**
   - Carbapatite
   - Brushite

3. **Autres**
   - Struvite (infectieux)
   - Cystine
   - Acide urique
   - Urate d'ammonium

## 🧮 Moteur d'Inférence - Système de Scoring

Le score final (sur 20 points) est calculé selon:

- **Densité UH** (0-6 pts): Plage typique du type de calcul
- **Morphologie** (0-3 pts): Signature caractéristique (spiculée, lisse, coralliforme, etc.)
- **pH urinaire** (0-3 pts): Acide (5.0-5.8) ou alcalin (6.8-7.5)
- **Marqueurs métaboliques** (0-4 pts): Hyperoxalurie, hypercalciurie, etc.
- **Infection** (-1 à +3 pts): Présence/absence selon le type
- **Radio-opacité** (0-1 pt): Opaque ou transparent
- **Bonus multicouche** (+2 pts): Pour chaque type détecté dans les couches analysées ⭐ NOUVEAU

### Analyse Multicouche ⭐ NOUVEAU

Pour les lithiases mixtes avec structure radiaire (noyau + couches périphériques):

**Détection automatique:**
- Le système analyse automatiquement le `densite_noyau` et les `densites_couches`
- Chaque couche est scorée individuellement pour identifier sa composition probable
- Exemple: Noyau 600 UH → Acide urique, Couche 1300 UH → Weddellite

**Types de composition:**
- **Pur**: Un seul type dominant (score_diff > 4)
- **Mixte**: Plusieurs types sans structure radiaire détectée
- **Mixte multicouche**: Structure radiaire avec compositions différentes par couche

**Affichage détaillé:**
```
Composition: Acide urique + Weddellite (structure multicouche)
Analyse multicouche: Noyau central: 600 UH → Acide urique | Couche périphérique 1: 1300 UH → Weddellite
```

## 🧪 Tests d'Acceptation

Voir le fichier `TESTS.md` pour tous les scénarios de test incluant :
- ✅ Test Whewellite (UH=1650, pH=5.3, hyperoxalurie)
- ✅ Test Weddellite (UH=1100, pH=5.6, hypercalciurie)
- ✅ Test Carbapatite (UH=1320, pH=7.2, infection)
- ✅ Test Struvite (UH=600, pH=7.0, infection uréase+)
- ✅ Test Acide urique (UH=450, pH=5.2, hyperuricurie)

## 🔐 Sécurité

### Chiffrement
- **Algorithme**: Fernet (AES 128 bits + HMAC)
- **Stockage**: Base64 en base de données
- **Déchiffrement**: Uniquement en mémoire au moment de l'affichage
- **Clé**: Configurée via `ENCRYPTION_KEY`

### Authentification
- Hachage des mots de passe (Werkzeug PBKDF2)
- Sessions sécurisées (Flask-Login)
- Protection CSRF native

### Protection des données
- Données chiffrées en base
- Aucune donnée sensible loggée
- Protection en cas de vol de base de données

## 🌐 Déploiement Production

### Variables d'environnement requises
```bash
export SECRET_KEY="cle-secrete-aleatoire-longue-64-caracteres-minimum"
export ENCRYPTION_KEY="cle-fernet-base64-44-caracteres"
export ADMIN_USERNAME="votre_username"
export ADMIN_PASSWORD="mot_de_passe_complexe_minimum_16_caracteres"
```

### Recommandations
1. **Serveur WSGI**: Gunicorn ou uWSGI
2. **HTTPS**: Certificat SSL/TLS
3. **Base de données**: PostgreSQL au lieu de SQLite
4. **Sauvegardes**: Quotidiennes automatisées
5. **Monitoring**: Sentry, Prometheus
6. **Firewall**: Restreindre l'accès réseau

### Exemple avec Gunicorn
```bash
pip install gunicorn
gunicorn --bind 0.0.0.0:5000 --workers 4 app:app
```

## 📊 Documentation

- **PROJECT_TRACKING.md**: Suivi complet des fonctionnalités (400+ lignes)
- **TESTS.md**: Scénarios de test et critères d'acceptation
- **replit.md**: Architecture technique du projet

## ⚠️ Avertissements Importants

1. **Clé de chiffrement**: Ne jamais perdre la clé `ENCRYPTION_KEY` - les données seraient irrécupérables
2. **Credentials**: Changer les credentials par défaut avant toute utilisation
3. **Production**: Ne jamais utiliser le serveur de développement Flask en production
4. **Sauvegardes**: Sauvegarder à la fois la base de données ET la clé de chiffrement

## 📞 Support

Pour toute question sur l'utilisation ou le déploiement de l'application, consultez la documentation complète dans `PROJECT_TRACKING.md`.

---

**Version**: 2.0  
**Date**: 26 octobre 2025  
**Statut**: ✅ Fonctionnel avec chiffrement des données de santé
