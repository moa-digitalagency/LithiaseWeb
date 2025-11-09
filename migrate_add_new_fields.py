from backend import create_app, db

app = create_app()

with app.app_context():
    print("📊 Migration: Ajout des nouveaux champs...")
    
    connection = db.engine.raw_connection()
    cursor = connection.cursor()
    
    try:
        print("\n1. Ajout des constantes vitales au modèle Patient...")
        cursor.execute("""
            ALTER TABLE patients 
            ADD COLUMN IF NOT EXISTS tension_arterielle_systolique INTEGER,
            ADD COLUMN IF NOT EXISTS tension_arterielle_diastolique INTEGER,
            ADD COLUMN IF NOT EXISTS frequence_cardiaque INTEGER,
            ADD COLUMN IF NOT EXISTS temperature FLOAT,
            ADD COLUMN IF NOT EXISTS frequence_respiratoire INTEGER;
        """)
        print("   ✓ Constantes vitales ajoutées")
        
        print("\n2. Ajout des mesures uroscanner au modèle Imagerie...")
        cursor.execute("""
            ALTER TABLE imageries 
            ADD COLUMN IF NOT EXISTS rein_gauche_cranio_caudal FLOAT,
            ADD COLUMN IF NOT EXISTS rein_gauche_antero_posterieur FLOAT,
            ADD COLUMN IF NOT EXISTS rein_gauche_transversal FLOAT,
            ADD COLUMN IF NOT EXISTS rein_gauche_volume FLOAT,
            ADD COLUMN IF NOT EXISTS rein_droit_cranio_caudal FLOAT,
            ADD COLUMN IF NOT EXISTS rein_droit_antero_posterieur FLOAT,
            ADD COLUMN IF NOT EXISTS rein_droit_transversal FLOAT,
            ADD COLUMN IF NOT EXISTS rein_droit_volume FLOAT,
            ADD COLUMN IF NOT EXISTS epaisseur_cortex_renal FLOAT,
            ADD COLUMN IF NOT EXISTS diametre_pyelon FLOAT,
            ADD COLUMN IF NOT EXISTS diametre_uretere_amont FLOAT,
            ADD COLUMN IF NOT EXISTS malformations_urinaires TEXT;
        """)
        print("   ✓ Mesures uroscanner ajoutées")
        
        print("\n3. Ajout des paramètres de fonction rénale au modèle Biologie...")
        cursor.execute("""
            ALTER TABLE biologies 
            ADD COLUMN IF NOT EXISTS uree FLOAT,
            ADD COLUMN IF NOT EXISTS creatinine FLOAT;
        """)
        print("   ✓ Paramètres de fonction rénale ajoutés")
        
        connection.commit()
        print("\n✅ Migration terminée avec succès!")
        print("Toutes les nouvelles colonnes ont été ajoutées à la base de données.\n")
        
    except Exception as e:
        connection.rollback()
        print(f"\n❌ Erreur lors de la migration: {e}")
        raise
    finally:
        cursor.close()
        connection.close()
