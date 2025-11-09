"""Script pour ajouter des codes UUID aux patients existants"""
from backend import create_app, db
from backend.models import Patient
import uuid

app = create_app()

with app.app_context():
    patients_sans_code = Patient.query.filter(
        (Patient.code_patient == None) | (Patient.code_patient == '')
    ).all()
    
    if not patients_sans_code:
        print("✓ Tous les patients ont déjà un code unique")
    else:
        print(f"Mise à jour de {len(patients_sans_code)} patients...")
        for patient in patients_sans_code:
            patient.code_patient = str(uuid.uuid4())
            print(f"  - {patient.prenom} {patient.nom}: {patient.code_patient}")
        
        db.session.commit()
        print(f"\n✅ {len(patients_sans_code)} patients mis à jour avec succès!")
