# Webapp Lithiase

Application web de gestion de calculs rénaux pour médecins.

## Installation

1. Installer les dépendances:
```bash
pip install -r requirements.txt
```

2. Lancer l'application:
```bash
python app.py
```

3. Accéder à l'application:
- URL: http://localhost:5000
- Utilisateur par défaut: `admin`
- Mot de passe par défaut: `admin123`

## Configuration

### Sécurité - Credentials administrateur

Pour sécuriser l'application, configurez les credentials via des variables d'environnement:

```bash
export ADMIN_USERNAME=votre_username
export ADMIN_PASSWORD=votre_mot_de_passe_securise
python app.py
```

**Important:** Ne jamais utiliser les credentials par défaut en production !

### Secret Key

Pour la production, changez également la clé secrète Flask dans `app.py`:
```python
app.config['SECRET_KEY'] = 'votre-cle-secrete-aleatoire-longue-et-complexe'
```

## Fonctionnalités

### 1. Gestion des patients
- Création/modification/suppression de fiches patients
- Informations complètes (identité, antécédents, allergies, traitements)
- Historique des épisodes

### 2. Épisodes médicaux
- Enregistrement des coliques néphrétiques
- Suivi des symptômes (douleur, fièvre, infection)
- Traçabilité des traitements

### 3. Examens
- **Imagerie (scanner):** taille, densité UH, morphologie, localisation
- **Biologie:** pH urinaire, marqueurs métaboliques, infections

### 4. Moteur d'inférence
- Classification automatique du type de calcul (8 types)
- Système de scoring transparent et explicable
- Proposition de voie de traitement
- Conseils de prévention personnalisés

### 5. Recherche avancée
- Filtres multiples (pH, UH, infection, type)
- Export CSV des résultats

### 6. Exports
- **PDF:** Dossier patient complet avec inférence et conseils
- **CSV:** Données de recherche pour analyse

## Types de calculs couverts

1. **Oxalate de calcium**
   - Whewellite (monohydrate)
   - Weddellite (dihydrate)

2. **Phosphates calciques**
   - Carbapatite
   - Brushite

3. **Autres types**
   - Struvite (infectieux)
   - Cystine
   - Acide urique
   - Urate d'ammonium

## Moteur d'inférence

Le moteur calcule un score sur 20 points pour chaque type de calcul:

- **Densité UH** (0-6 pts): Plage typique du type
- **Morphologie** (0-3 pts): Signature caractéristique
- **pH urinaire** (0-3 pts): Plage acide/alcaline préférentielle
- **Marqueurs métaboliques** (0-4 pts): Hyperoxalurie, hypercalciurie, etc.
- **Infection** (-1 à +3 pts): Présence/absence selon le type
- **Radio-opacité** (0-1 pt): Concordance opaque/transparent

### Badge d'incertitude
Si la différence de score entre le Top 1 et le Top 2 est < 2 points, l'application affiche un badge "Résultat incertain" et suggère de compléter la biologie ou l'imagerie.

## Structure de la base de données

- **Patient:** Identité, antécédents, facteurs de risque
- **Episode:** Date, motif, diagnostic, symptômes
- **Imagerie:** Taille, densité, morphologie, localisation
- **Biologie:** pH, marqueurs métaboliques, infection
- **User:** Authentification

## Tests

Voir le fichier `TESTS.md` pour les critères d'acceptation et scénarios de test.

## Sécurité

- Authentification mono-utilisateur
- Sessions sécurisées (Flask-Login)
- Base de données SQLite locale
- Hachage des mots de passe (Werkzeug)

## Déploiement

**Cette version est une application de développement.**

Pour un déploiement en production:
1. Utiliser un serveur WSGI (Gunicorn, uWSGI)
2. Configurer HTTPS avec un certificat SSL
3. Changer les credentials et la clé secrète
4. Utiliser une base de données plus robuste (PostgreSQL)
5. Mettre en place des sauvegardes régulières
6. Restreindre l'accès réseau

## Support

Application développée selon le cahier des charges "Webapp Lithiase (mono-médecin)".
