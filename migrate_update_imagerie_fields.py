"""Migration pour corriger les champs du modèle Imagerie"""
from backend import create_app, db

app = create_app()

with app.app_context():
    print("=" * 80)
    print("📊 Migration: Mise à jour des champs du modèle Imagerie")
    print("=" * 80)
    
    connection = db.engine.raw_connection()
    cursor = connection.cursor()
    
    try:
        print("\n1. Vérification et ajout des champs séparés gauche/droit...")
        
        print("   - Ajout epaisseur_cortex_renal_gauche et epaisseur_cortex_renal_droit...")
        cursor.execute("""
            ALTER TABLE imageries 
            ADD COLUMN IF NOT EXISTS epaisseur_cortex_renal_gauche FLOAT,
            ADD COLUMN IF NOT EXISTS epaisseur_cortex_renal_droit FLOAT;
        """)
        
        print("   - Ajout diametre_pyelon_gauche et diametre_pyelon_droit...")
        cursor.execute("""
            ALTER TABLE imageries 
            ADD COLUMN IF NOT EXISTS diametre_pyelon_gauche FLOAT,
            ADD COLUMN IF NOT EXISTS diametre_pyelon_droit FLOAT;
        """)
        
        print("   - Ajout diametre_uretere_amont_gauche et diametre_uretere_amont_droit...")
        cursor.execute("""
            ALTER TABLE imageries 
            ADD COLUMN IF NOT EXISTS diametre_uretere_amont_gauche FLOAT,
            ADD COLUMN IF NOT EXISTS diametre_uretere_amont_droit FLOAT;
        """)
        
        print("\n2. Vérification et migration des données des anciens champs...")
        
        cursor.execute("""
            SELECT column_name 
            FROM information_schema.columns 
            WHERE table_name = 'imageries' 
            AND column_name IN ('epaisseur_cortex_renal', 'diametre_pyelon', 'diametre_uretere_amont');
        """)
        old_columns = [row[0] for row in cursor.fetchall()]
        
        if old_columns:
            print(f"   Anciens champs trouvés: {', '.join(old_columns)}")
            
            if 'epaisseur_cortex_renal' in old_columns:
                print("   - Migration epaisseur_cortex_renal -> epaisseur_cortex_renal_gauche/droit...")
                cursor.execute("""
                    UPDATE imageries 
                    SET epaisseur_cortex_renal_gauche = epaisseur_cortex_renal,
                        epaisseur_cortex_renal_droit = epaisseur_cortex_renal
                    WHERE epaisseur_cortex_renal IS NOT NULL 
                    AND (epaisseur_cortex_renal_gauche IS NULL OR epaisseur_cortex_renal_droit IS NULL);
                """)
            
            if 'diametre_pyelon' in old_columns:
                print("   - Migration diametre_pyelon -> diametre_pyelon_gauche/droit...")
                cursor.execute("""
                    UPDATE imageries 
                    SET diametre_pyelon_gauche = diametre_pyelon,
                        diametre_pyelon_droit = diametre_pyelon
                    WHERE diametre_pyelon IS NOT NULL 
                    AND (diametre_pyelon_gauche IS NULL OR diametre_pyelon_droit IS NULL);
                """)
            
            if 'diametre_uretere_amont' in old_columns:
                print("   - Migration diametre_uretere_amont -> diametre_uretere_amont_gauche/droit...")
                cursor.execute("""
                    UPDATE imageries 
                    SET diametre_uretere_amont_gauche = diametre_uretere_amont,
                        diametre_uretere_amont_droit = diametre_uretere_amont
                    WHERE diametre_uretere_amont IS NOT NULL 
                    AND (diametre_uretere_amont_gauche IS NULL OR diametre_uretere_amont_droit IS NULL);
                """)
        else:
            print("   ✓ Aucun ancien champ à migrer (base déjà à jour)")
        
        connection.commit()
        print("\n✅ Migration terminée avec succès!")
        print("   ✓ Nouveaux champs gauche/droit ajoutés")
        if old_columns:
            print("   ✓ Données migrées depuis les anciens champs uniques")
            print("\nℹ️  Les anciens champs sont conservés pour compatibilité.")
        print()
        
    except Exception as e:
        connection.rollback()
        print(f"\n❌ Erreur lors de la migration: {e}")
        raise
    finally:
        cursor.close()
        connection.close()
