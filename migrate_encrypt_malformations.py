"""Migration pour chiffrer les données malformations_urinaires existantes en texte clair"""
from backend import create_app, db
from backend.utils.crypto import encryption_manager
from backend.models import Imagerie

app = create_app()

with app.app_context():
    print("=" * 80)
    print("🔐 Migration: Chiffrement des données malformations_urinaires")
    print("=" * 80)
    
    try:
        imageries = Imagerie.query.all()
        encrypted_count = 0
        skipped_count = 0
        
        for imagerie in imageries:
            if imagerie._malformations_urinaires:
                try:
                    decrypted = encryption_manager.decrypt(imagerie._malformations_urinaires)
                    print(f"   ✓ Imagerie ID {imagerie.id} - déjà chiffré")
                    skipped_count += 1
                except Exception:
                    print(f"   🔒 Imagerie ID {imagerie.id} - chiffrement en cours...")
                    plaintext = imagerie._malformations_urinaires
                    imagerie._malformations_urinaires = encryption_manager.encrypt(plaintext)
                    encrypted_count += 1
        
        if encrypted_count > 0:
            db.session.commit()
            print(f"\n✅ Migration terminée avec succès!")
            print(f"   - {encrypted_count} enregistrement(s) chiffré(s)")
            print(f"   - {skipped_count} enregistrement(s) déjà chiffré(s)")
        else:
            print(f"\n✓ Aucune donnée à chiffrer (tous les enregistrements sont déjà chiffrés)")
            print(f"   - {skipped_count} enregistrement(s) déjà chiffré(s)")
        
    except Exception as e:
        db.session.rollback()
        print(f"\n❌ Erreur lors de la migration: {e}")
        raise
