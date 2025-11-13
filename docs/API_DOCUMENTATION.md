# Documentation API - KALONJI

## Vue d'ensemble
Cette API fournit des endpoints pour gérer les patients, les épisodes de lithiase urinaire, les imageries, les analyses biologiques et l'export de données.

## Authentification
Toutes les routes API nécessitent une authentification via Flask-Login.

---

## 📋 Patients

### GET /api/patients
Liste tous les patients

**Réponse:**
```json
[
  {
    "id": 1,
    "code_patient": "uuid-string",
    "nom": "Nom",
    "prenom": "Prénom",
    "date_naissance": "YYYY-MM-DD",
    "sexe": "M|F"
  }
]
```

### POST /api/patients
Crée un nouveau patient

**Corps de la requête:**
```json
{
  "nom": "string",
  "prenom": "string",
  "date_naissance": "YYYY-MM-DD",
  "sexe": "M|F",
  "telephone": "string (optionnel)",
  "email": "string (optionnel)",
  "adresse": "string (optionnel)",
  "poids": number (optionnel),
  "taille": number (optionnel)
}
```

**Réponse:** Patient créé avec code_patient généré automatiquement

### GET /api/patients/{id}
Récupère les détails d'un patient

**Réponse:**
```json
{
  "id": number,
  "code_patient": "uuid",
  "nom": "string",
  "prenom": "string",
  "date_naissance": "YYYY-MM-DD",
  "sexe": "M|F",
  "episodes": [...],
  ...
}
```

### PUT /api/patients/{id}
Met à jour un patient

**Corps de la requête:** Mêmes champs que POST (tous optionnels)

### DELETE /api/patients/{id}
Supprime un patient

**Réponse:** Status 204 No Content

---

## 📅 Épisodes

### GET /api/patients/{patient_id}/episodes
Liste tous les épisodes d'un patient

### POST /api/patients/{patient_id}/episodes
Crée un nouvel épisode

**Corps de la requête:**
```json
{
  "date_episode": "YYYY-MM-DD",
  "motif": "string",
  "diagnostic": "string (optionnel)",
  "douleur": boolean,
  "fievre": boolean,
  "infection_urinaire": boolean,
  "germe": "string (optionnel)"
}
```

### GET /api/episodes/{id}
Récupère les détails d'un épisode

### PUT /api/episodes/{id}
Met à jour un épisode

### DELETE /api/episodes/{id}
Supprime un épisode

---

## 🔬 Imageries

### POST /api/episodes/{episode_id}/imageries
Crée une imagerie pour un épisode

**Corps de la requête:**
```json
{
  "date_examen": "YYYY-MM-DD",
  "taille_mm": number,
  "densite_uh": number (optionnel),
  "densite_noyau": number (optionnel),
  "densites_couches": "string (optionnel)",
  "morphologie": "string",
  "radio_opacite": "string",
  "nombre_calculs": number,
  "topographie_calcul": "string",
  "diametre_longitudinal": number (optionnel),
  "diametre_transversal": number (optionnel),
  "forme_calcul": "string (optionnel)",
  "contour_calcul": "string (optionnel)",
  "asp_resultats": "string (optionnel)",
  "echographie_resultats": "string (optionnel)",
  "uroscanner_resultats": "string (optionnel)"
}
```

### GET /api/imageries/{id}
Récupère une imagerie

### PUT /api/imageries/{id}
Met à jour une imagerie

### DELETE /api/imageries/{id}
Supprime une imagerie

---

## 🧪 Biologies

### POST /api/episodes/{episode_id}/biologies
Crée une analyse biologique pour un épisode

**Corps de la requête:**
```json
{
  "date_examen": "YYYY-MM-DD",
  "ph_urinaire": number,
  "densite_urinaire": number (optionnel),
  "sediment_urinaire": "string (optionnel)",
  "ecbu_resultats": "string (optionnel)",
  "infection_urinaire": boolean,
  "germe": "string (optionnel)",
  "hyperoxalurie": boolean,
  "oxalurie_valeur": number (optionnel),
  "hypercalciurie": boolean,
  "calciurie_valeur": number (optionnel),
  "hyperuricurie": boolean,
  "uricurie_valeur": number (optionnel),
  "cystinurie": boolean,
  "hypercalcemie": boolean,
  "calciemie_valeur": number (optionnel),
  "tsh": number (optionnel),
  "t3": number (optionnel),
  "t4": number (optionnel)
}
```

### GET /api/biologies/{id}
Récupère une analyse biologique

### PUT /api/biologies/{id}
Met à jour une analyse biologique

### DELETE /api/biologies/{id}
Supprime une analyse biologique

---

## 🧮 Inférence (Algorithme KALONJI)

### POST /api/episodes/{episode_id}/calculate
Lance le calcul d'inférence pour déterminer le type de calcul

**Réponse:**
```json
{
  "top_1": "Type de calcul",
  "top_1_score": number,
  "top_1_reasons": ["raison1", "raison2"],
  "top_3": [
    ["Type", score, ["raisons"]],
    ...
  ],
  "composition_type": "Pur|Mixte|Mixte multicouche",
  "composition_detail": "string",
  "radial_structure_analysis": [
    {
      "position": "Noyau central|Couche périphérique N",
      "densite": number,
      "composition_probable": "Type de calcul",
      "layer_number": number
    }
  ],
  "lec_eligible": boolean,
  "voie_traitement": "string",
  "prevention": ["conseil1", "conseil2"],
  "uncertain": boolean
}
```

**Types de composition:**
- **Pur**: Différence de score >4 entre le premier et le deuxième type
- **Mixte**: Différence de score 2-4 entre le premier et le deuxième type
- **Mixte multicouche**: Présence de structure radiaire (noyau + couches périphériques) avec bonus de +2 points

---

## 🔍 Recherche

### GET /api/search/patients
Recherche de patients avec filtres

**Paramètres query:**
- `nom`: string (optionnel)
- `prenom`: string (optionnel)
- `date_naissance_min`: YYYY-MM-DD (optionnel)
- `date_naissance_max`: YYYY-MM-DD (optionnel)
- `sexe`: M|F (optionnel)
- `ph_min`: number (optionnel)
- `ph_max`: number (optionnel)
- `densite_min`: number (optionnel)
- `densite_max`: number (optionnel)
- `taille_min`: number (optionnel)
- `taille_max`: number (optionnel)
- `infection`: boolean (optionnel)

---

## 📤 Exports

### GET /api/patients/{patient_id}/export/pdf
Exporte le dossier patient en PDF

**Réponse:** Fichier PDF téléchargeable

### POST /api/export/csv
Exporte les résultats de recherche en CSV

**Corps de la requête:** Filtres de recherche (mêmes paramètres que /api/search/patients)

**Réponse:** Fichier CSV téléchargeable

### POST /api/export/patients-csv
Exporte la liste complète de tous les patients en CSV

**Corps de la requête:**
```json
{}
```

**Réponse:** Fichier CSV téléchargeable avec colonnes: Code Patient, Nom, Prénom, Date Naissance, Sexe, Téléphone, Email, Nombre Épisodes

---

## 🔐 Authentification

### POST /api/login
Connexion utilisateur

**Corps de la requête:**
```json
{
  "username": "string",
  "password": "string"
}
```

### POST /api/logout
Déconnexion utilisateur

### GET /api/check-auth
Vérifie si l'utilisateur est authentifié

---

## ⚙️ Paramètres

### GET /api/settings
Récupère les paramètres utilisateur

### PUT /api/settings
Met à jour les paramètres utilisateur

---

## Codes d'erreur

- **200 OK**: Requête réussie
- **201 Created**: Ressource créée
- **204 No Content**: Suppression réussie
- **400 Bad Request**: Données invalides
- **401 Unauthorized**: Non authentifié
- **404 Not Found**: Ressource non trouvée
- **500 Internal Server Error**: Erreur serveur

---

## Notes importantes

1. **Chiffrement**: Les données sensibles (nom, prénom, adresse, etc.) sont chiffrées en base de données
2. **Code Patient**: Généré automatiquement (UUID) lors de la création d'un patient
3. **QR Code**: Disponible dans le PDF avec le code patient
4. **Inférence**: L'algorithme KALONJI utilise les données d'imagerie et de biologie pour prédire le type de calcul
5. **Hormones thyroïdiennes**: TSH, T3 et T4 sont pris en compte dans l'analyse métabolique
