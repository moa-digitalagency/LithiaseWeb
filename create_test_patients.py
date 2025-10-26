#!/usr/bin/env python3
"""Create test patients directly in the database"""

from backend import create_app
from backend.models import db, Patient
from datetime import date

app = create_app()

with app.app_context():
    # Patient 1: Toutes les données complètes
    patient1 = Patient()
    patient1.nom = "Dupont"
    patient1.prenom = "Jean"
    patient1.date_naissance = date(1975, 5, 15)
    patient1.sexe = "M"
    patient1.telephone = "01 23 45 67 89"
    patient1.email = "jean.dupont@example.com"
    patient1.adresse = "123 rue de la République, 75001 Paris"
    patient1.antecedents_personnels = "HTA depuis 2010, Diabète type 2 depuis 2015, Episodes récurrents de lithiase depuis 2018"
    patient1.antecedents_familiaux = "Père et frère avec lithiase calcique récurrente"
    patient1.antecedents_chirurgicaux = "Appendicectomie 1995, Cholécystectomie 2012"
    patient1.allergies = "Pénicilline, Aspirine"
    patient1.traitements_chroniques = "Ramipril 10mg/j, Metformine 1000mg x2/j, Atorvastatine 20mg/j"
    patient1.hydratation_jour = 1.5
    patient1.regime_alimentaire = "Riche en protéines animales, consommation excessive de sel"
    patient1.notes = "Patient très anxieux concernant ses calculs rénaux. Demande un suivi rapproché. Profession: cuisinier (exposition à la chaleur, déshydratation fréquente)."
    
    db.session.add(patient1)
    db.session.commit()
    
    print(f"✅ Patient complet créé (ID: {patient1.id})")
    print(f"   URL: http://127.0.0.1:5000/patient/{patient1.id}")
    
    # Patient 2: Données partielles uniquement
    patient2 = Patient()
    patient2.nom = "Martin"
    patient2.prenom = "Sophie"
    patient2.date_naissance = date(1988, 12, 20)
    patient2.sexe = "F"
    patient2.telephone = "06 12 34 56 78"
    patient2.email = "sophie.martin@example.com"
    patient2.antecedents_personnels = "Première lithiase en 2023"
    patient2.allergies = "Aucune allergie connue"
    patient2.hydratation_jour = 2.0
    
    db.session.add(patient2)
    db.session.commit()
    
    print(f"✅ Patient partiel créé (ID: {patient2.id})")
    print(f"   URL: http://127.0.0.1:5000/patient/{patient2.id}")
