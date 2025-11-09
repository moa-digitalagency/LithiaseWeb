# Documentation Technique - Webapp Lithiase

## 🏗️ Architecture

### Vue d'ensemble

L'application suit une architecture MVC (Model-View-Controller) classique avec Flask :

```
webapp-lithiase/
├── app.py                      # Point d'entrée Flask
├── backend/                    # Backend organisé
│   ├── __init__.py            # Initialisation Flask + blueprints
│   ├── inference.py           # Moteur d'inférence
│   ├── models/                # Modèles SQLAlchemy
│   │   └── __init__.py       # Patient, Episode, Imagerie, Biologie
│   ├── routes/                # Routes par domaine
│   │   ├── auth.py           # Authentification
│   │   ├── patients.py       # CRUD patients
│   │   ├── episodes.py       # CRUD épisodes + inférence
│   │   ├── imageries.py      # CRUD imageries
│   │   ├── biologies.py      # CRUD biologies
│   │   ├── search.py         # Recherche avancée
│   │   ├── exports.py        # Exports PDF/CSV
│   │   └── settings.py       # Paramètres utilisateur
│   └── utils/                 # Utilitaires
│       └── crypto.py          # Gestionnaire chiffrement Fernet
├── templates/                 # Templates HTML
├── static/                    # Fichiers statiques
│   └── css/
│       └── myoneart.css      # CSS personnalisé
├── uploads/                   # Documents uploadés
├── requirements.txt           # Dépendances Python
└── lithiase.db               # Base de données SQLite
```

## 🛠️ Technologies

### Backend
- **Framework** : Flask 2.3.x
- **ORM** : SQLAlchemy 2.0
- **Base de données** : SQLite 3
- **Chiffrement** : Cryptography (Fernet AES-128 + HMAC)
- **Authentification** : Flask-Login
- **PDF** : ReportLab
- **Python** : 3.11

### Frontend
- **Template Engine** : Jinja2
- **CSS Framework** : Tailwind CSS (CDN)
- **JavaScript** : Vanilla JS (Fetch API)
- **Design System** : MyOneArt (indigo-purple)

## 📊 Modèle de données

### Patient
Champs chiffrés :
- `nom`, `prenom`, `telephone`, `email`, `adresse`
- `antecedents_personnels`, `antecedents_familiaux`, `antecedents_chirurgicaux`
- `allergies`, `traitements_chroniques`
- `groupe_ethnique`
- `petit_dejeuner`, `dejeuner`, `diner`, `grignotage`, `autres_consommations`
- `asp_resultats`, `echographie_resultats`, `uroscanner_resultats`
- `sediment_urinaire`, `ecbu_resultats`
- `topographie_calcul`, `forme_calcul`, `contour_calcul`
- `densites_couches`, `calcifications_autres`
- `notes`

Champs non chiffrés :
- `date_naissance`, `sexe`
- `poids`, `taille`, `hydratation_jour`, `regime_alimentaire`
- `ph_urinaire`, `densite_urinaire`
- `nombre_calculs`, `diametre_longitudinal`, `diametre_transversal`
- `densite_noyau`
- Timestamps : `created_at`, `updated_at`

### Episode
Représente un épisode médical (colique néphrétique, consultation, récidive).

Relations :
- `patient_id` → Patient
- `imageries` → Liste d'imageries
- `biologies` → Liste de biologies

Champs chiffrés :
- `motif`, `diagnostic`, `germe`
- `lateralite`, `siege_douloureux`, `symptomes_associes`
- `traitement_medical`, `centre_traitement`, `resultat_traitement`
- `notes`

Champs non chiffrés :
- `date_episode`
- `douleur`, `fievre`, `infection_urinaire`, `urease_positif`
- `traitement_interventionnel`, `date_traitement`
- Timestamps

### Imagerie
Examens d'imagerie associés à un épisode.

Champs chiffrés :
- `asp_resultats`, `echographie_resultats`, `uroscanner_resultats`
- `situation_calcul`, `topographie_calcul`
- `forme_calcul`, `contour_calcul`
- `densites_couches`, `calcifications_autres`
- `commentaires`

Champs non chiffrés :
- `date_examen`
- `taille_mm`, `densite_uh`, `densite_ecart_type`, `densite_noyau`
- `morphologie`, `radio_opacite`, `localisation`
- `nombre`, `nombre_estime`, `nombre_calculs`
- `diametre_longitudinal`, `diametre_transversal`
- Timestamps

### Biologie
Résultats biologiques associés à un épisode.

Champs chiffrés :
- `sediment_urinaire`, `ecbu_resultats`
- `germe`
- `commentaires`

Champs non chiffrés :
- `date_examen`
- `ph_urinaire`, `densite_urinaire`
- `hyperoxalurie`, `hypercalciurie`, `hyperuricurie`, `cystinurie`
- `oxalurie_valeur`, `calciurie_valeur`, `uricurie_valeur`
- `infection_urinaire`, `urease_positif`
- Timestamps

## 🔐 Système de chiffrement

### Principe
- **Algorithme** : Fernet (AES-128 CBC + HMAC SHA256)
- **Clé** : Générée et stockée dans variable d'environnement `ENCRYPTION_KEY`
- **Transparence** : Properties Python pour chiffrement/déchiffrement automatique

### Implémentation
```python
# backend/utils/crypto.py
class EncryptionManager:
    def __init__(self, key):
        self.cipher = Fernet(key)
    
    def encrypt(self, data):
        if data is None or data == '':
            return None
        return self.cipher.encrypt(data.encode()).decode()
    
    def decrypt(self, encrypted_data):
        if encrypted_data is None or encrypted_data == '':
            return None
        return self.cipher.decrypt(encrypted_data.encode()).decode()
```

### Utilisation dans les modèles
```python
class Patient(db.Model):
    _nom = db.Column('nom', db.Text, nullable=False)
    
    @property
    def nom(self):
        return encryption_manager.decrypt(self._nom)
    
    @nom.setter
    def nom(self, value):
        self._nom = encryption_manager.encrypt(value)
```

## 🧠 Moteur d'inférence

Le moteur d'inférence est documenté en détail dans [ALGORITHME.md](ALGORITHME.md).

Principe :
- Système de notation sur 20 points
- Comparaison avec 8 types de calculs
- Top 3 résultats retournés
- Indication d'incertitude si scores proches

## 🌐 API REST

### Endpoints patients
- `GET /api/patients` - Liste tous les patients
- `POST /api/patients` - Crée un nouveau patient
- `GET /api/patients/<id>` - Récupère un patient
- `PUT /api/patients/<id>` - Met à jour un patient
- `GET /api/patients/<id>/export/pdf` - Exporte en PDF

### Endpoints épisodes
- `GET /api/patients/<id>/episodes` - Liste les épisodes d'un patient
- `POST /api/patients/<id>/episodes` - Crée un épisode
- `GET /api/episodes/<id>` - Récupère un épisode
- `POST /api/episodes/<id>/inference` - Lance l'inférence

### Endpoints imageries
- `POST /api/episodes/<id>/imageries` - Ajoute une imagerie

### Endpoints biologies
- `POST /api/episodes/<id>/biologies` - Ajoute une biologie

### Endpoints recherche
- `POST /api/search` - Recherche avancée
- `POST /api/search/export/csv` - Export CSV

### Endpoints paramètres
- `GET /api/settings/profile` - Récupère le profil
- `PUT /api/settings/profile` - Met à jour le profil
- `PUT /api/settings/password` - Change le mot de passe

## 📝 Format des réponses JSON

### Patient
```json
{
  "id": 1,
  "nom": "Dupont",
  "prenom": "Jean",
  "date_naissance": "1975-03-15",
  "sexe": "M",
  "poids": 75.5,
  "taille": 175,
  "telephone": "0123456789",
  "email": "jean.dupont@example.com",
  ...
}
```

### Résultat d'inférence
```json
{
  "top_1": "Whewellite",
  "top_1_score": 14,
  "top_1_reasons": [
    "Densité 1250 UH dans la plage typique [1200-1700]",
    "pH 5.5 dans la plage préférentielle [5.0-5.8]",
    "Marqueur signature présent (hyperoxalurie)"
  ],
  "top_3": [
    ["Whewellite", 14],
    ["Weddellite", 9],
    ["Acide urique", 5]
  ],
  "uncertain": false,
  "lec_eligible": false,
  "voie_traitement": "URS (première intention)",
  "prevention": [
    "Hydratation abondante (2-3L/jour)",
    "Réduire les aliments riches en oxalates",
    "Apport calcique normal avec les repas",
    "Traiter l'hyperoxalurie si présente"
  ]
}
```

## 🎨 Design System

### Palette de couleurs
- **Primaire** : Dégradé indigo-purple (#667eea → #764ba2)
- **Succès** : Vert (#10B981)
- **Danger** : Rouge (#EF4444)
- **Info** : Bleu (#3B82F6)

### Classes CSS personnalisées
- `.gradient-bg` : Fond dégradé pour navigation
- `.card` : Carte avec ombre et bordure arrondie
- `.btn btn-{variant}` : Boutons stylisés
- `.input-field` : Champs de formulaire
- `.data-table` : Tables de données
- `.modal-backdrop`, `.modal-content` : Modals

### Border radius
- Formulaires : 0.5rem
- Cartes : 1-2rem
- Boutons : 1-1.5rem

## 🔄 Workflow de développement

1. **Modification du modèle** → Mise à jour de la base de données SQLite
2. **Ajout de route** → Création du blueprint dans `backend/routes/`
3. **Modification du template** → Édition dans `templates/`
4. **Ajout de champ chiffré** → Property dans le modèle + colonne `_nom_champ`
5. **Tests** → Vérification manuelle de toutes les fonctionnalités

## 🚀 Déploiement

### Prérequis
- Python 3.11+
- Variables d'environnement :
  - `ADMIN_USERNAME` : Nom d'utilisateur admin
  - `ADMIN_PASSWORD` : Mot de passe admin
  - `ENCRYPTION_KEY` : Clé de chiffrement Fernet
  - `SECRET_KEY` : Clé secrète Flask

### Installation
```bash
pip install -r requirements.txt
python app.py
```

### Base de données
Création automatique au premier lancement avec utilisateur admin.

## 📈 Performance

- **Temps de chiffrement/déchiffrement** : < 1ms par champ
- **Requête patient complète** : < 50ms
- **Inférence** : < 10ms
- **Génération PDF** : < 500ms

## 🔮 Évolutions futures

- Upload de fichiers d'imagerie (DICOM)
- Analyse d'images avec IA
- Graphiques d'évolution (pH, densité, IMC)
- Export FHIR
- API externe pour laboratoires
- Application mobile
