"""Migration pour ajouter le champ code_patient à la table patients"""
import sqlite3
import uuid

# Connexion à la base de données
conn = sqlite3.connect('lithiase.db')
cursor = conn.cursor()

try:
    # Vérifier si la colonne existe déjà
    cursor.execute("PRAGMA table_info(patients)")
    columns = [col[1] for col in cursor.fetchall()]
    
    if 'code_patient' not in columns:
        print("Ajout de la colonne code_patient...")
        cursor.execute("ALTER TABLE patients ADD COLUMN code_patient VARCHAR(36)")
        
        # Générer des UUIDs pour tous les patients existants
        cursor.execute("SELECT id FROM patients WHERE code_patient IS NULL OR code_patient = ''")
        patient_ids = cursor.fetchall()
        
        print(f"Mise à jour de {len(patient_ids)} patients...")
        for (patient_id,) in patient_ids:
            code = str(uuid.uuid4())
            cursor.execute("UPDATE patients SET code_patient = ? WHERE id = ?", (code, patient_id))
            print(f"  - Patient ID {patient_id}: {code}")
        
        conn.commit()
        print("\n✅ Migration réussie!")
    else:
        print("✓ La colonne code_patient existe déjà")
        
except Exception as e:
    print(f"❌ Erreur: {e}")
    conn.rollback()
finally:
    conn.close()
