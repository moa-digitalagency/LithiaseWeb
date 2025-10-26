# Webapp Lithiase - Application médicale de gestion de calculs rénaux

## Vue d'ensemble
Application web mono-médecin pour la gestion des dossiers patients souffrant de lithiase (calculs rénaux). L'application permet de saisir des dossiers complets, d'obtenir des propositions de type de calcul via un moteur d'inférence, et de générer des rapports PDF.

## Architecture
- **Backend**: Flask (Python 3.11) avec SQLAlchemy ORM
- **Frontend**: HTML/CSS avec Tailwind CSS + JavaScript vanilla
- **Base de données**: SQLite
- **Exports**: PDF (ReportLab) et CSV

## Structure du projet
```
/
├── app.py              # Application Flask principale
├── models.py           # Modèles de base de données SQLAlchemy
├── inference.py        # Moteur d'inférence pour classification des calculs
├── static/            # Fichiers statiques (CSS, JS)
├── templates/         # Templates HTML
├── uploads/           # Documents uploadés
├── requirements.txt   # Dépendances Python
└── lithiase.db       # Base de données SQLite
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

## Sécurité
- Authentification simple mono-utilisateur
- Base de données SQLite
- Session locale sécurisée
