"""Migration pour convertir les codes patients de 36 caractères (UUID) vers 6 caractères"""
from backend import create_app, db
from backend.models import Patient
from backend.utils.patient_code import generate_unique_patient_code

app = create_app()

with app.app_context():
    print("=" * 80)
    print("🔄 Migration: Conversion des codes patients UUID vers 6 caractères")
    print("=" * 80)
    
    try:
        patients_with_long_codes = Patient.query.filter(
            db.func.length(Patient.code_patient) > 6
        ).all()
        
        if not patients_with_long_codes:
            print("\n✓ Aucun patient avec un code long (> 6 caractères)")
            print("  Tous les codes sont déjà au bon format.\n")
        else:
            print(f"\nConversion de {len(patients_with_long_codes)} patient(s)...\n")
            
            existing_codes = set(p.code_patient for p in Patient.query.all() if p.code_patient and len(p.code_patient) == 6)
            
            def code_exists(code):
                return code in existing_codes
            
            for patient in patients_with_long_codes:
                old_code = patient.code_patient
                new_code = generate_unique_patient_code(code_exists)
                existing_codes.add(new_code)
                patient.code_patient = new_code
                print(f"  - Patient ID {patient.id}: {old_code} → {new_code}")
            
            db.session.commit()
            print(f"\n✅ Migration terminée avec succès!")
            print(f"   {len(patients_with_long_codes)} code(s) patient(s) converti(s) de UUID vers format 6 caractères\n")
        
    except Exception as e:
        db.session.rollback()
        print(f"\n❌ Erreur lors de la migration: {e}")
        raise
