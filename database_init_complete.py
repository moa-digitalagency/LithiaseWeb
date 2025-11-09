"""
Script d'initialisation complète et consolidée de la base de données KALONJI
===============================================================================
Ce script unique remplace tous les anciens scripts d'initialisation et migrations.

Il effectue les opérations suivantes:
1. Suppression de toutes les tables existantes (DROP ALL)
2. Création du schéma complet de la base de données
3. Création de l'utilisateur administrateur
4. Création de patients de démonstration avec données complètes

Utilisation: python database_init_complete.py
===============================================================================
"""
from backend import create_app, db
from backend.models import User, Patient, Episode, Imagerie, Biologie, Document
from backend.utils.patient_code import generate_unique_patient_code
from datetime import datetime, timedelta
import random
import os

app = create_app()

def drop_all_tables():
    """
    Supprime toutes les tables de la base de données PostgreSQL
    Attention: Cette opération est irréversible!
    """
    print("=" * 80)
    print("🗑️  SUPPRESSION DE TOUTES LES DONNÉES EXISTANTES")
    print("=" * 80)
    
    with app.app_context():
        try:
            db.drop_all()
            db.session.commit()
            print("✓ Toutes les tables ont été supprimées avec succès")
            print()
        except Exception as e:
            print(f"❌ Erreur lors de la suppression des tables: {e}")
            raise

def create_all_tables():
    """
    Crée toutes les tables du schéma de base de données
    Tables créées:
    - users: Authentification et gestion des utilisateurs
    - patients: Données patients (chiffrées avec Fernet AES-128)
    - episodes: Épisodes médicaux liés aux patients
    - imageries: Résultats d'imagerie médicale (ASP, échographie, uro-scanner)
    - biologies: Marqueurs biologiques, métaboliques et thyroïdiens
    - documents: Documents et pièces jointes
    """
    print("=" * 80)
    print("🏗️  CRÉATION DU SCHÉMA DE BASE DE DONNÉES")
    print("=" * 80)
    print("Tables à créer:")
    print("  - users (authentification)")
    print("  - patients (données chiffrées avec Fernet AES-128)")
    print("  - episodes (épisodes médicaux)")
    print("  - imageries (résultats d'imagerie)")
    print("  - biologies (marqueurs métaboliques et thyroïdiens)")
    print("  - documents (pièces jointes)")
    print("=" * 80)
    
    with app.app_context():
        try:
            db.create_all()
            db.session.commit()
            
            print("✓ Schéma de base de données initialisé avec succès")
            print("✓ Toutes les tables ont été créées")
            print("✓ Relations et contraintes d'intégrité référentielle établies")
            print("✓ Cascade delete configuré pour les relations parent-enfant")
            print("=" * 80)
            
            table_count = len(db.metadata.tables)
            print(f"📊 Total: {table_count} tables créées dans la base de données")
            print("=" * 80)
            print()
        except Exception as e:
            print(f"❌ Erreur lors de la création des tables: {e}")
            raise

def create_admin_user():
    """
    Crée l'utilisateur administrateur par défaut
    Utilise les variables d'environnement ADMIN_USERNAME et ADMIN_PASSWORD si définies
    Sinon utilise les valeurs par défaut: admin / admin123
    """
    print("=" * 80)
    print("👤 CRÉATION DE L'UTILISATEUR ADMINISTRATEUR")
    print("=" * 80)
    
    with app.app_context():
        try:
            admin_username = os.environ.get('ADMIN_USERNAME', 'admin')
            admin_password = os.environ.get('ADMIN_PASSWORD', 'admin123')
            
            existing_admin = User.query.filter_by(username=admin_username).first()
            if existing_admin:
                print(f"⚠️  L'utilisateur {admin_username} existe déjà, passage de cette étape")
                print()
                return
            
            admin = User(username=admin_username)
            admin.set_password(admin_password)
            db.session.add(admin)
            db.session.commit()
            
            print(f"✓ Utilisateur admin créé (username: {admin_username})")
            if admin_password == 'admin123':
                print("⚠️  ATTENTION: Utilisez les variables d'environnement ADMIN_USERNAME")
                print("   et ADMIN_PASSWORD pour sécuriser les credentials en production")
            print("=" * 80)
            print()
        except Exception as e:
            db.session.rollback()
            print(f"❌ Erreur lors de la création de l'utilisateur admin: {e}")
            raise

def create_demo_patients():
    """
    Crée des patients de démonstration avec données médicales complètes
    pour tester l'algorithme KALONJI
    """
    print("=" * 80)
    print("🏥 CRÉATION DES PATIENTS DE DÉMONSTRATION")
    print("=" * 80)
    
    with app.app_context():
        demo_patients = [
            {
                "nom": "Kalala",
                "prenom": "Jean",
                "date_naissance": datetime(1975, 3, 15).date(),
                "sexe": "M",
                "telephone": "+243812345678",
                "email": "jean.kalala@email.cd",
                "adresse": "Avenue Tombalbaye, Kinshasa",
                "groupe_ethnique": "Luba",
                "poids": 82.5,
                "taille": 178.0,
                "tension_arterielle_systolique": 145,
                "tension_arterielle_diastolique": 92,
                "frequence_cardiaque": 78,
                "temperature": 37.2,
                "frequence_respiratoire": 16,
                "antecedents_personnels": "Hypertension artérielle depuis 2015, Diabète de type 2 depuis 2018",
                "antecedents_familiaux": "Père ayant eu des calculs rénaux récidivants, Mère hypertendue",
                "antecedents_chirurgicaux": "Appendicectomie en 2000",
                "allergies": "Pénicilline",
                "traitements_chroniques": "Metformine 1000mg 2x/jour, Ramipril 5mg 1x/jour",
                "hydratation_jour": 1.2,
                "regime_alimentaire": "Régime hyperprotéiné, consommation élevée de produits laitiers",
                "petit_dejeuner": "Café au lait, pain blanc avec beurre, pondu (haricots)",
                "dejeuner": "Viande rouge 4-5x/semaine, chikwangue, peu de légumes",
                "diner": "Poisson salé, fufu, légumes",
                "grignotage": "Cacahuètes salées, beignets",
                "autres_consommations": "2-3 verres de vin de palme par jour, café 5x/jour",
                "type_calcul": "Whewellite",
                "ph_urinaire": 5.8,
                "densite_urinaire": 1.025,
                "nombre_calculs": 1,
                "topographie_calcul": "Calice inférieur droit",
                "diametre_longitudinal": 8.2,
                "diametre_transversal": 6.1,
                "forme_calcul": "Ovale",
                "contour_calcul": "Lisse",
                "densite_noyau": 950,
                "densites_couches": "Homogène",
                "calcifications_autres": "Pas d'autres calcifications",
                "hypercalciurie": True,
                "calciurie_valeur": 320.0,
                "oxalurie_valeur": 38.0,
                "calciemie_valeur": 2.55,
                "sediment_urinaire": "Cristaux d'oxalate de calcium monohydraté (whewellite) nombreux"
            },
            {
                "nom": "Mukendi",
                "prenom": "Sophie",
                "date_naissance": datetime(1988, 7, 22).date(),
                "sexe": "F",
                "telephone": "+243898765432",
                "email": "sophie.mukendi@email.cd",
                "adresse": "Avenue de la Libération, Lubumbashi",
                "groupe_ethnique": "Lunda",
                "poids": 58.0,
                "taille": 165.0,
                "tension_arterielle_systolique": 118,
                "tension_arterielle_diastolique": 75,
                "frequence_cardiaque": 72,
                "temperature": 37.8,
                "frequence_respiratoire": 18,
                "antecedents_personnels": "Infections urinaires récidivantes (5-6 par an), Maladie inflammatoire intestinale",
                "antecedents_familiaux": "Mère avec lithiase urinaire",
                "antecedents_chirurgicaux": "Résection intestinale partielle en 2016",
                "allergies": "Aucune allergie connue",
                "traitements_chroniques": "Azathioprine 150mg/jour, Mésalazine 3g/jour",
                "hydratation_jour": 1.8,
                "regime_alimentaire": "Régime pauvre en fibres",
                "petit_dejeuner": "Thé, pain, compote",
                "dejeuner": "Viande blanche ou poisson, riz ou pâtes",
                "diner": "Soupe, légumes",
                "grignotage": "Fruits",
                "autres_consommations": "Eau plate principalement, thé vert 2-3x/jour",
                "type_calcul": "Weddellite",
                "ph_urinaire": 6.5,
                "densite_urinaire": 1.018,
                "nombre_calculs": 8,
                "topographie_calcul": "Bilatérale, prédominance calices inférieurs",
                "diametre_longitudinal": 5.0,
                "diametre_transversal": 4.2,
                "forme_calcul": "Arrondie",
                "contour_calcul": "Irregulier",
                "densite_noyau": 1300,
                "densites_couches": "Homogène",
                "calcifications_autres": "Calcifications vasculaires mineures",
                "hyperoxalurie": True,
                "oxalurie_valeur": 65.0,
                "calciurie_valeur": 220.0,
                "calciemie_valeur": 2.3,
                "sediment_urinaire": "Cristaux d'oxalate de calcium dihydraté (weddellite) abondants",
                "infection_urinaire": True,
                "germe": "E. coli"
            },
            {
                "nom": "Tshimanga",
                "prenom": "André",
                "date_naissance": datetime(1982, 11, 8).date(),
                "sexe": "M",
                "telephone": "+243823456789",
                "email": "a.tshimanga@email.cd",
                "adresse": "Boulevard du 30 Juin, Kananga",
                "groupe_ethnique": "Kongo",
                "poids": 95.0,
                "taille": 172.0,
                "tension_arterielle_systolique": 138,
                "tension_arterielle_diastolique": 88,
                "frequence_cardiaque": 85,
                "temperature": 36.9,
                "frequence_respiratoire": 17,
                "antecedents_personnels": "Obésité (IMC 32), Goutte depuis 2019",
                "antecedents_familiaux": "Père diabétique, oncle avec lithiase",
                "antecedents_chirurgicaux": "Aucune chirurgie",
                "allergies": "Allergie aux AINS (urticaire)",
                "traitements_chroniques": "Allopurinol 300mg/jour",
                "hydratation_jour": 0.8,
                "regime_alimentaire": "Alimentation riche en purines (viandes, fruits de mer)",
                "petit_dejeuner": "Café sucré, pain",
                "dejeuner": "Viande rouge quotidienne, fufu, légumes",
                "diner": "Poisson grillé ou poulet",
                "grignotage": "Biscuits, arachides",
                "autres_consommations": "2-3 sodas par jour, bière le weekend",
                "type_calcul": "Acide urique",
                "ph_urinaire": 5.2,
                "densite_urinaire": 1.032,
                "nombre_calculs": 1,
                "topographie_calcul": "Bassinet gauche",
                "diametre_longitudinal": 12.0,
                "diametre_transversal": 10.5,
                "forme_calcul": "Irreguliere",
                "contour_calcul": "Irregulier",
                "densite_noyau": 450,
                "densites_couches": "Densité faible et homogène",
                "calcifications_autres": "Néphrocalcinose médullaire débutante",
                "hyperuricurie": True,
                "uricurie_valeur": 850.0,
                "calciurie_valeur": 280.0,
                "oxalurie_valeur": 35.0,
                "calciemie_valeur": 2.45,
                "sediment_urinaire": "Nombreux cristaux d'acide urique en rosette"
            }
        ]
        
        try:
            for patient_data in demo_patients:
                patient = Patient()
                
                def code_exists(code):
                    return Patient.query.filter_by(code_patient=code).first() is not None
                
                patient.code_patient = generate_unique_patient_code(code_exists)
                
                excluded_keys = [
                    'ph_urinaire', 'densite_urinaire', 'nombre_calculs', 'topographie_calcul',
                    'diametre_longitudinal', 'diametre_transversal', 'forme_calcul', 'contour_calcul',
                    'densite_noyau', 'densites_couches', 'calcifications_autres',
                    'hypercalciurie', 'hyperoxalurie', 'hyperuricurie', 'cystinurie',
                    'calciurie_valeur', 'oxalurie_valeur', 'uricurie_valeur', 'calciemie_valeur',
                    'sediment_urinaire', 'infection_urinaire', 'germe', 'type_calcul'
                ]
                
                for key, value in patient_data.items():
                    if key not in excluded_keys and hasattr(patient, key):
                        setattr(patient, key, value)
                
                db.session.add(patient)
                db.session.flush()
                
                episode_date = datetime.now().date() - timedelta(days=random.randint(10, 90))
                episode = Episode()
                episode.patient_id = patient.id
                episode.date_episode = episode_date
                episode.motif = "Douleur lombaire aiguë avec hématurie"
                episode.diagnostic = "Colique néphrétique avec calcul urinaire"
                episode.douleur = True
                episode.fievre = patient_data.get('sexe') == 'F' and patient_data.get('infection_urinaire', False)
                episode.infection_urinaire = patient_data.get('infection_urinaire', False)
                
                if episode.infection_urinaire:
                    episode.germe = patient_data.get('germe', 'E. coli')
                    episode.urease_positif = patient_data.get('germe', '') == 'Proteus mirabilis'
                
                db.session.add(episode)
                db.session.flush()
                
                imagerie = Imagerie()
                imagerie.episode_id = episode.id
                imagerie.date_examen = episode_date
                imagerie.taille_mm = int(patient_data.get('diametre_longitudinal', 8))
                imagerie.densite_uh = patient_data.get('densite_noyau', 900)
                imagerie.densite_noyau = patient_data.get('densite_noyau', 900)
                imagerie.densites_couches = patient_data.get('densites_couches', '')
                imagerie.morphologie = patient_data.get('forme_calcul', 'Arrondie')
                imagerie.radio_opacite = "opaque" if patient_data.get('densite_noyau', 900) > 500 else "transparent"
                imagerie.localisation = patient_data.get('topographie_calcul', 'Rein')
                imagerie.nombre = str(patient_data.get('nombre_calculs', 1))
                imagerie.nombre_estime = patient_data.get('nombre_calculs', 1)
                imagerie.nombre_calculs = patient_data.get('nombre_calculs', 1)
                imagerie.topographie_calcul = patient_data.get('topographie_calcul', '')
                imagerie.diametre_longitudinal = patient_data.get('diametre_longitudinal', 0)
                imagerie.diametre_transversal = patient_data.get('diametre_transversal', 0)
                imagerie.forme_calcul = patient_data.get('forme_calcul', '')
                imagerie.contour_calcul = patient_data.get('contour_calcul', '')
                imagerie.calcifications_autres = patient_data.get('calcifications_autres', '')
                
                imagerie.rein_gauche_cranio_caudal = round(random.uniform(95.0, 120.0), 1)
                imagerie.rein_gauche_antero_posterieur = round(random.uniform(45.0, 60.0), 1)
                imagerie.rein_gauche_transversal = round(random.uniform(40.0, 55.0), 1)
                imagerie.rein_gauche_volume = round((imagerie.rein_gauche_cranio_caudal * 
                                                     imagerie.rein_gauche_antero_posterieur * 
                                                     imagerie.rein_gauche_transversal * 0.523) / 1000, 1)
                
                imagerie.rein_droit_cranio_caudal = round(random.uniform(95.0, 120.0), 1)
                imagerie.rein_droit_antero_posterieur = round(random.uniform(45.0, 60.0), 1)
                imagerie.rein_droit_transversal = round(random.uniform(40.0, 55.0), 1)
                imagerie.rein_droit_volume = round((imagerie.rein_droit_cranio_caudal * 
                                                    imagerie.rein_droit_antero_posterieur * 
                                                    imagerie.rein_droit_transversal * 0.523) / 1000, 1)
                
                imagerie.epaisseur_cortex_renal_gauche = round(random.uniform(8.0, 12.0), 1)
                imagerie.epaisseur_cortex_renal_droit = round(random.uniform(8.0, 12.0), 1)
                imagerie.diametre_pyelon_gauche = round(random.uniform(3.0, 8.0), 1)
                imagerie.diametre_pyelon_droit = round(random.uniform(3.0, 8.0), 1)
                imagerie.diametre_uretere_amont_gauche = round(random.uniform(2.0, 6.0), 1)
                imagerie.diametre_uretere_amont_droit = round(random.uniform(2.0, 6.0), 1)
                
                if random.random() < 0.2:
                    malformations = ["Ectasie pyélocalicielle modérée", "Atrophie corticale localisée", "Duplicité urétérale"]
                    imagerie.malformations_urinaires = random.choice(malformations)
                
                db.session.add(imagerie)
                
                biologie = Biologie()
                biologie.episode_id = episode.id
                biologie.date_examen = episode_date
                biologie.ph_urinaire = patient_data.get('ph_urinaire', 6.0)
                biologie.densite_urinaire = patient_data.get('densite_urinaire', 1.020)
                biologie.sediment_urinaire = patient_data.get('sediment_urinaire', '')
                biologie.ecbu_resultats = patient_data.get('ecbu_resultats', 'Stérile')
                biologie.infection_urinaire = episode.infection_urinaire
                
                if episode.infection_urinaire:
                    biologie.germe = patient_data.get('germe', 'E. coli')
                    biologie.urease_positif = patient_data.get('germe', '') == 'Proteus mirabilis'
                
                biologie.hypercalciurie = patient_data.get('hypercalciurie', False)
                biologie.hyperoxalurie = patient_data.get('hyperoxalurie', False)
                biologie.hyperuricurie = patient_data.get('hyperuricurie', False)
                biologie.cystinurie = patient_data.get('cystinurie', False)
                biologie.calciurie_valeur = patient_data.get('calciurie_valeur')
                biologie.oxalurie_valeur = patient_data.get('oxalurie_valeur')
                biologie.uricurie_valeur = patient_data.get('uricurie_valeur')
                biologie.calciemie_valeur = patient_data.get('calciemie_valeur')
                
                biologie.tsh = round(random.uniform(0.5, 4.0), 1)
                biologie.t3 = round(random.uniform(1.2, 2.0), 1)
                biologie.t4 = round(random.uniform(8.0, 12.0), 1)
                biologie.uree = round(random.uniform(0.2, 0.5), 2)
                biologie.creatinine = round(random.uniform(7.0, 13.0), 1)
                
                db.session.add(biologie)
                
                print(f"  ✓ Patient créé: {patient_data['prenom']} {patient_data['nom']} (Code: {patient.code_patient})")
            
            db.session.commit()
            print(f"\n✅ {len(demo_patients)} patients de démonstration créés avec succès!")
            print("=" * 80)
            print()
        except Exception as e:
            db.session.rollback()
            print(f"❌ Erreur lors de la création des patients: {e}")
            raise

def main():
    """
    Fonction principale d'initialisation complète de la base de données
    """
    print("\n")
    print("╔" + "=" * 78 + "╗")
    print("║" + " " * 15 + "INITIALISATION COMPLÈTE DE LA BASE DE DONNÉES" + " " * 17 + "║")
    print("║" + " " * 20 + "Algorithme de classification KALONJI" + " " * 21 + "║")
    print("╚" + "=" * 78 + "╝")
    print("\n")
    
    input("⚠️  Cette opération va SUPPRIMER TOUTES LES DONNÉES existantes.\n    Appuyez sur Entrée pour continuer ou Ctrl+C pour annuler... ")
    print()
    
    drop_all_tables()
    create_all_tables()
    create_admin_user()
    create_demo_patients()
    
    print("╔" + "=" * 78 + "╗")
    print("║" + " " * 20 + "✅ INITIALISATION TERMINÉE AVEC SUCCÈS" + " " * 19 + "║")
    print("╚" + "=" * 78 + "╝")
    print()
    print("📝 Informations de connexion:")
    print("  - Nom d'utilisateur: admin")
    print("  - Mot de passe: admin123")
    print()
    print("🚀 Pour démarrer l'application, exécutez: python app.py")
    print()

if __name__ == '__main__':
    main()
