#!/usr/bin/env python3
"""Script pour créer un patient de test avec toutes les données complètes"""

import requests
import json

BASE_URL = "http://127.0.0.1:5000"

# 1. Se connecter
login_response = requests.post(
    f"{BASE_URL}/login",
    json={"username": "admin", "password": "admin123"},
    headers={"Content-Type": "application/json"}
)

if not login_response.json().get('success'):
    print("❌ Échec de la connexion")
    exit(1)

# Récupérer le cookie de session
session_cookie = login_response.cookies

print("✅ Connexion réussie")

# 2. Créer un patient de test avec TOUTES les données
patient_data = {
    "nom": "Dupont",
    "prenom": "Jean",
    "date_naissance": "1975-05-15",
    "sexe": "M",
    "telephone": "01 23 45 67 89",
    "email": "jean.dupont@example.com",
    "adresse": "123 rue de la République, 75001 Paris",
    "antecedents_personnels": "HTA depuis 2010, Diabète type 2 depuis 2015, Episodes récurrents de lithiase depuis 2018",
    "antecedents_familiaux": "Père et frère avec lithiase calcique récurrente",
    "antecedents_chirurgicaux": "Appendicectomie 1995, Cholécystectomie 2012",
    "allergies": "Pénicilline, Aspirine",
    "traitements_chroniques": "Ramipril 10mg/j, Metformine 1000mg x2/j, Atorvastatine 20mg/j",
    "hydratation_jour": 1.5,
    "regime_alimentaire": "Riche en protéines animales, consommation excessive de sel",
    "notes": "Patient très anxieux concernant ses calculs rénaux. Demande un suivi rapproché. Profession: cuisinier (exposition à la chaleur, déshydratation fréquente)."
}

create_response = requests.post(
    f"{BASE_URL}/api/patients",
    json=patient_data,
    cookies=session_cookie,
    headers={"Content-Type": "application/json"}
)

if create_response.status_code == 201:
    result = create_response.json()
    patient_id = result['id']
    print(f"✅ Patient créé avec succès (ID: {patient_id})")
    print(f"\n🔗 Ouvrez cette URL pour voir le dossier complet:")
    print(f"   {BASE_URL}/patient/{patient_id}")
else:
    print(f"❌ Erreur lors de la création: {create_response.text}")
    exit(1)

# 3. Créer un deuxième patient avec des données partielles
patient_data_partial = {
    "nom": "Martin",
    "prenom": "Sophie",
    "date_naissance": "1988-12-20",
    "sexe": "F",
    "telephone": "06 12 34 56 78",
    "email": "sophie.martin@example.com",
    # Pas d'adresse
    "antecedents_personnels": "Première lithiase en 2023",
    # Pas d'antécédents familiaux
    # Pas d'antécédents chirurgicaux
    "allergies": "Aucune allergie connue",
    # Pas de traitements chroniques
    "hydratation_jour": 2.0,
    # Pas de régime alimentaire spécifique
    # Pas de notes
}

create_response2 = requests.post(
    f"{BASE_URL}/api/patients",
    json=patient_data_partial,
    cookies=session_cookie,
    headers={"Content-Type": "application/json"}
)

if create_response2.status_code == 201:
    result2 = create_response2.json()
    patient_id2 = result2['id']
    print(f"✅ Patient avec données partielles créé (ID: {patient_id2})")
    print(f"\n🔗 Ouvrez cette URL pour voir le dossier partiel:")
    print(f"   {BASE_URL}/patient/{patient_id2}")
else:
    print(f"❌ Erreur lors de la création: {create_response2.text}")
