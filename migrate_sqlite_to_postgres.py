import os
import sys
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

sys.path.insert(0, os.path.dirname(__file__))

from backend.models import Patient, Episode, Imagerie, Biologie, User
from backend import db

def migrate_data():
    print("=" * 80)
    print("MIGRATION SQLITE vers PostgreSQL")
    print("=" * 80)
    
    sqlite_uri = 'sqlite:///lithiase.db'
    postgres_uri = os.environ.get('DATABASE_URL')
    
    if not postgres_uri:
        print("ERREUR: DATABASE_URL non défini dans les variables d'environnement")
        return False
    
    if '?' not in postgres_uri:
        postgres_uri += '?sslmode=require'
    elif 'sslmode' not in postgres_uri:
        postgres_uri += '&sslmode=require'
    
    print(f"Source SQLite: {sqlite_uri}")
    print(f"Destination PostgreSQL: {postgres_uri[:30]}...")
    print()
    
    if not os.path.exists('lithiase.db'):
        print("ERREUR: Fichier lithiase.db introuvable")
        return False
    
    sqlite_engine = create_engine(sqlite_uri)
    postgres_engine = create_engine(postgres_uri)
    
    SqliteSession = sessionmaker(bind=sqlite_engine)
    PostgresSession = sessionmaker(bind=postgres_engine)
    
    sqlite_session = SqliteSession()
    postgres_session = PostgresSession()
    
    try:
        print("1. Migration des utilisateurs...")
        users = sqlite_session.query(User).all()
        for user in users:
            existing = postgres_session.query(User).filter_by(username=user.username).first()
            if not existing:
                new_user = User(
                    id=user.id,
                    username=user.username,
                    password_hash=user.password_hash
                )
                postgres_session.add(new_user)
        postgres_session.commit()
        print(f"   ✓ {len(users)} utilisateur(s) migré(s)")
        
        print("2. Migration des patients...")
        patients = sqlite_session.query(Patient).all()
        migrated_patients = 0
        for patient in patients:
            existing = postgres_session.query(Patient).filter_by(id=patient.id).first()
            if not existing:
                new_patient = Patient()
                new_patient.id = patient.id
                new_patient.code_patient = patient.code_patient
                
                new_patient._nom = patient._nom
                new_patient._prenom = patient._prenom
                new_patient.date_naissance = patient.date_naissance
                new_patient.sexe = patient.sexe
                new_patient._telephone = patient._telephone
                new_patient._email = patient._email
                new_patient._adresse = patient._adresse
                new_patient._antecedents_personnels = patient._antecedents_personnels
                new_patient._antecedents_familiaux = patient._antecedents_familiaux
                new_patient._antecedents_chirurgicaux = patient._antecedents_chirurgicaux
                new_patient._allergies = patient._allergies
                new_patient._traitements_chroniques = patient._traitements_chroniques
                new_patient.hydratation_jour = patient.hydratation_jour
                new_patient.regime_alimentaire = patient.regime_alimentaire
                new_patient.poids = patient.poids
                new_patient.taille = patient.taille
                new_patient._groupe_ethnique = patient._groupe_ethnique
                new_patient._petit_dejeuner = patient._petit_dejeuner
                new_patient._dejeuner = patient._dejeuner
                new_patient._diner = patient._diner
                new_patient._grignotage = patient._grignotage
                new_patient._autres_consommations = patient._autres_consommations
                new_patient._asp_resultats = patient._asp_resultats
                new_patient._echographie_resultats = patient._echographie_resultats
                new_patient._uroscanner_resultats = patient._uroscanner_resultats
                new_patient._sediment_urinaire = patient._sediment_urinaire
                new_patient._ecbu_resultats = patient._ecbu_resultats
                new_patient.ph_urinaire = patient.ph_urinaire
                new_patient.densite_urinaire = patient.densite_urinaire
                new_patient.nombre_calculs = patient.nombre_calculs
                new_patient._topographie_calcul = patient._topographie_calcul
                new_patient.diametre_longitudinal = patient.diametre_longitudinal
                new_patient.diametre_transversal = patient.diametre_transversal
                new_patient._forme_calcul = patient._forme_calcul
                new_patient._contour_calcul = patient._contour_calcul
                new_patient.densite_noyau = patient.densite_noyau
                new_patient._densites_couches = patient._densites_couches
                new_patient._calcifications_autres = patient._calcifications_autres
                new_patient.fichier_imagerie = patient.fichier_imagerie
                new_patient.fichier_laboratoire = patient.fichier_laboratoire
                new_patient.fichier_ordonnance = patient.fichier_ordonnance
                new_patient._notes = patient._notes
                new_patient.created_at = patient.created_at
                new_patient.updated_at = patient.updated_at
                
                postgres_session.add(new_patient)
                migrated_patients += 1
        postgres_session.commit()
        print(f"   ✓ {migrated_patients} patient(s) migré(s)")
        
        print("3. Migration des épisodes...")
        episodes = sqlite_session.query(Episode).all()
        migrated_episodes = 0
        for episode in episodes:
            existing = postgres_session.query(Episode).filter_by(id=episode.id).first()
            if not existing:
                new_episode = Episode()
                new_episode.id = episode.id
                new_episode.patient_id = episode.patient_id
                new_episode.date_episode = episode.date_episode
                new_episode._motif = episode._motif
                new_episode._diagnostic = episode._diagnostic
                new_episode.douleur = episode.douleur
                new_episode.fievre = episode.fievre
                new_episode.infection_urinaire = episode.infection_urinaire
                new_episode._germe = episode._germe
                new_episode.urease_positif = episode.urease_positif
                new_episode.lateralite = episode.lateralite
                new_episode._siege_douloureux = episode._siege_douloureux
                new_episode._symptomes_associes = episode._symptomes_associes
                new_episode._traitement_medical = episode._traitement_medical
                new_episode._traitement_interventionnel = episode._traitement_interventionnel
                new_episode.date_traitement = episode.date_traitement
                new_episode._notes = episode._notes
                new_episode.calculated_stone_type = episode.calculated_stone_type
                new_episode.calculated_stone_type_data = episode.calculated_stone_type_data
                new_episode.created_at = episode.created_at
                new_episode.updated_at = episode.updated_at
                
                postgres_session.add(new_episode)
                migrated_episodes += 1
        postgres_session.commit()
        print(f"   ✓ {migrated_episodes} épisode(s) migré(s)")
        
        print("4. Migration des imageries...")
        imageries = sqlite_session.query(Imagerie).all()
        migrated_imageries = 0
        for imagerie in imageries:
            existing = postgres_session.query(Imagerie).filter_by(id=imagerie.id).first()
            if not existing:
                new_imagerie = Imagerie()
                new_imagerie.id = imagerie.id
                new_imagerie.episode_id = imagerie.episode_id
                new_imagerie.date_examen = imagerie.date_examen
                new_imagerie.type_examen = imagerie.type_examen
                new_imagerie.taille_mm = imagerie.taille_mm
                new_imagerie.densite_uh = imagerie.densite_uh
                new_imagerie.densite_noyau = imagerie.densite_noyau
                new_imagerie._densites_couches = imagerie._densites_couches
                new_imagerie._topographie_calcul = imagerie._topographie_calcul
                new_imagerie._forme_calcul = imagerie._forme_calcul
                new_imagerie._contour_calcul = imagerie._contour_calcul
                new_imagerie._morphologie = imagerie._morphologie
                new_imagerie.radio_opacite = imagerie.radio_opacite
                new_imagerie._calcifications_autres = imagerie._calcifications_autres
                new_imagerie._commentaires = imagerie._commentaires
                new_imagerie.created_at = imagerie.created_at
                
                postgres_session.add(new_imagerie)
                migrated_imageries += 1
        postgres_session.commit()
        print(f"   ✓ {migrated_imageries} imagerie(s) migrée(s)")
        
        print("5. Migration des biologies...")
        biologies = sqlite_session.query(Biologie).all()
        migrated_biologies = 0
        for biologie in biologies:
            existing = postgres_session.query(Biologie).filter_by(id=biologie.id).first()
            if not existing:
                new_biologie = Biologie()
                new_biologie.id = biologie.id
                new_biologie.episode_id = biologie.episode_id
                new_biologie.date_examen = biologie.date_examen
                new_biologie.ph_urinaire = biologie.ph_urinaire
                new_biologie.densite_urinaire = biologie.densite_urinaire
                new_biologie._sediment_urinaire = biologie._sediment_urinaire
                new_biologie._ecbu_resultats = biologie._ecbu_resultats
                new_biologie.hyperoxalurie = biologie.hyperoxalurie
                new_biologie.hypercalciurie = biologie.hypercalciurie
                new_biologie.hyperuricurie = biologie.hyperuricurie
                new_biologie.cystinurie = biologie.cystinurie
                new_biologie.hypercalcemie = biologie.hypercalcemie
                new_biologie.oxalurie_valeur = biologie.oxalurie_valeur
                new_biologie.calciurie_valeur = biologie.calciurie_valeur
                new_biologie.uricurie_valeur = biologie.uricurie_valeur
                new_biologie.calciemie_valeur = biologie.calciemie_valeur
                new_biologie.t3 = biologie.t3
                new_biologie.t4 = biologie.t4
                new_biologie.tsh = biologie.tsh
                new_biologie.infection_urinaire = biologie.infection_urinaire
                new_biologie._germe = biologie._germe
                new_biologie.urease_positif = biologie.urease_positif
                new_biologie._commentaires = biologie._commentaires
                new_biologie.created_at = biologie.created_at
                
                postgres_session.add(new_biologie)
                migrated_biologies += 1
        postgres_session.commit()
        print(f"   ✓ {migrated_biologies} biologie(s) migrée(s)")
        
        print()
        print("=" * 80)
        print("MIGRATION TERMINÉE AVEC SUCCÈS")
        print("=" * 80)
        print(f"Total: {migrated_patients} patients, {migrated_episodes} épisodes, {migrated_imageries} imageries, {migrated_biologies} biologies")
        print()
        print("IMPORTANT: Vous pouvez maintenant supprimer lithiase.db et redémarrer l'application")
        print()
        
        return True
        
    except Exception as e:
        print(f"ERREUR lors de la migration: {e}")
        postgres_session.rollback()
        import traceback
        traceback.print_exc()
        return False
        
    finally:
        sqlite_session.close()
        postgres_session.close()

if __name__ == '__main__':
    if not migrate_data():
        sys.exit(1)
