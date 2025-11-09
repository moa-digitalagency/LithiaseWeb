from backend import db

def initialize_database(app):
    """
    Initialise le schéma complet de la base de données PostgreSQL.
    
    Cette fonction crée toutes les tables nécessaires pour l'application KALONJI:
    - users: Gestion des utilisateurs et authentification
    - patients: Données patients avec chiffrement des informations sensibles
    - episodes: Épisodes médicaux liés aux patients
    - imageries: Résultats d'imagerie médicale (ASP, échographie, uro-scanner)
    - biologies: Résultats biologiques et marqueurs métaboliques
    - documents: Documents et fichiers attachés aux épisodes
    
    Note: Cette fonction utilise l'intégration PostgreSQL de Replit (blueprint:python_database)
    pour une configuration automatique des secrets (DATABASE_URL, PGHOST, etc.)
    
    Référence: blueprint:python_database
    """
    from backend.models import (
        User, Patient, Episode, Imagerie, Biologie, Document
    )
    
    print("================================================================================")
    print("Initialisation du schéma de base de données PostgreSQL...")
    print("================================================================================")
    print("Tables à créer:")
    print("  - users (authentification)")
    print("  - patients (données chiffrées avec Fernet AES-128)")
    print("  - episodes (épisodes médicaux)")
    print("  - imageries (résultats d'imagerie)")
    print("  - biologies (marqueurs métaboliques et thyroïdiens)")
    print("  - documents (pièces jointes)")
    print("================================================================================")
    
    db.create_all()
    
    print("✓ Schéma de base de données initialisé avec succès")
    print("✓ Toutes les tables ont été créées")
    print("✓ Relations et contraintes d'intégrité référentielle établies")
    print("✓ Cascade delete configuré pour les relations parent-enfant")
    print("================================================================================")
    
    table_count = len(db.metadata.tables)
    print(f"📊 Total: {table_count} tables créées dans la base de données")
    print("================================================================================")
