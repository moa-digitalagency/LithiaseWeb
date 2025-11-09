from backend import db

def initialize_database(app):
    from backend.models import (
        User, Patient, Episode, Imagerie, Biologie
    )
    
    print("Initialisation du schéma de base de données...")
    db.create_all()
    print("Schéma de base de données initialisé avec succès")
