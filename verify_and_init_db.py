"""
Script de vérification et d'initialisation automatique de la base de données KALONJI
====================================================================================
Ce script:
1. Vérifie que tous les champs requis sont présents dans le schéma de la base de données
2. Charge automatiquement les données de démonstration si la base est vide
3. S'exécute automatiquement au démarrage de l'application
====================================================================================
"""
import sys
import os
from backend import create_app, db
from backend.models import User, Patient, Episode, Imagerie, Biologie, Document
from sqlalchemy import inspect
from datetime import datetime

def verify_database_schema():
    """Vérifie que tous les champs requis existent dans les tables"""
    print("=" * 80)
    print("VÉRIFICATION DU SCHÉMA DE LA BASE DE DONNÉES")
    print("=" * 80)
    
    app = create_app()
    with app.app_context():
        inspector = inspect(db.engine)
        
        # Vérifier que toutes les tables existent
        required_tables = ['users', 'patients', 'episodes', 'imageries', 'biologies', 'documents']
        existing_tables = inspector.get_table_names()
        
        missing_tables = [table for table in required_tables if table not in existing_tables]
        
        if missing_tables:
            print(f"⚠️  Tables manquantes: {', '.join(missing_tables)}")
            print("Création des tables manquantes...")
            db.create_all()
            print("✓ Tables créées avec succès")
        else:
            print("✓ Toutes les tables requises existent")
        
        # Vérifier les colonnes de chaque table
        table_models = {
            'users': User,
            'patients': Patient,
            'episodes': Episode,
            'imageries': Imagerie,
            'biologies': Biologie,
            'documents': Document
        }
        
        all_columns_ok = True
        for table_name, model in table_models.items():
            if table_name in existing_tables:
                columns = {col['name'] for col in inspector.get_columns(table_name)}
                expected_columns = {col.name for col in model.__table__.columns}
                
                missing_columns = expected_columns - columns
                if missing_columns:
                    print(f"⚠️  Table '{table_name}' - Colonnes manquantes: {', '.join(missing_columns)}")
                    all_columns_ok = False
                else:
                    print(f"✓ Table '{table_name}' - Toutes les colonnes présentes ({len(columns)} colonnes)")
        
        if not all_columns_ok:
            print("\n⚠️  ATTENTION: Des colonnes sont manquantes!")
            print("Recréation du schéma complet...")
            db.create_all()
            db.session.commit()
            print("✓ Schéma mis à jour avec succès")
        
        print("=" * 80)
        return True

def check_if_database_empty():
    """Vérifie si la base de données contient des données"""
    app = create_app()
    with app.app_context():
        user_count = User.query.count()
        patient_count = Patient.query.count()
        
        print(f"📊 Utilisateurs: {user_count}, Patients: {patient_count}")
        
        # Retourne True si pas de patients (même s'il y a un admin)
        return patient_count == 0

def load_demo_data_if_empty():
    """Charge les données de démonstration si la base est vide (MODE DÉVELOPPEMENT UNIQUEMENT)"""
    if check_if_database_empty():
        print("\n" + "=" * 80)
        print("PAS DE PATIENTS - CHARGEMENT DES DONNÉES DE DÉMONSTRATION")
        print("⚠️  MODE DÉVELOPPEMENT - Ne jamais utiliser en production!")
        print("=" * 80)
        
        # Importer et exécuter init_demo_data sans confirmation
        try:
            # Exécuter init_demo_data programmatiquement
            import init_demo_data
            app = init_demo_data.app
            
            with app.app_context():
                # Vérifier si l'admin existe déjà
                admin = User.query.filter_by(username='admin').first()
                if not admin:
                    print("\n📝 Création de l'utilisateur admin DE DÉVELOPPEMENT...")
                    print("⚠️  SÉCURITÉ: Credentials par défaut utilisés (admin/admin123)")
                    print("⚠️  NE JAMAIS utiliser ces credentials en production!")
                    admin = User(username='admin')
                    admin.set_password('admin123')
                    db.session.add(admin)
                    db.session.commit()
                    print("✓ Utilisateur admin créé (username: admin, password: admin123)")
                else:
                    print("\n✓ Utilisateur admin existe déjà")
                
                # Créer les données demo
                print("\n📝 Création des 5 patients de démonstration...")
                init_demo_data.create_comprehensive_demo_data()
                
                print("\n" + "=" * 80)
                print("✅ DONNÉES DE DÉMONSTRATION CHARGÉES AVEC SUCCÈS")
                print("=" * 80)
                print("• 5 patients avec données complètes créés")
                print("• Connexion DEV: admin / admin123")
                print("⚠️  PRODUCTION: Configurer ADMIN_USERNAME et ADMIN_PASSWORD!")
                print("=" * 80)
        
        except Exception as e:
            print(f"\n❌ Erreur lors du chargement des données de démonstration: {str(e)}")
            import traceback
            traceback.print_exc()
            return False
    else:
        print("\n✓ Base de données contient déjà des patients, chargement ignoré")
    
    return True

def main():
    """Fonction principale"""
    print("\n")
    print("╔" + "=" * 78 + "╗")
    print("║" + " " * 15 + "VÉRIFICATION ET INITIALISATION AUTOMATIQUE" + " " * 21 + "║")
    print("║" + " " * 30 + "KALONJI" + " " * 42 + "║")
    print("╚" + "=" * 78 + "╝")
    print()
    
    try:
        # Étape 1: Vérifier le schéma
        if not verify_database_schema():
            print("\n❌ Échec de la vérification du schéma")
            return False
        
        # Étape 2: Charger les données de démo si nécessaire
        if not load_demo_data_if_empty():
            print("\n❌ Échec du chargement des données de démonstration")
            return False
        
        print("\n" + "=" * 80)
        print("✅ VÉRIFICATION ET INITIALISATION TERMINÉES AVEC SUCCÈS")
        print("=" * 80)
        print()
        
        return True
    
    except Exception as e:
        print(f"\n❌ ERREUR: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
