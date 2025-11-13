"""
Script de création de données démonstration complètes pour KALONJI
==================================================================
5 patients représentant chacun un type de calcul spécifique avec 
tous les champs médicaux remplis de manière réaliste
==================================================================
"""
from backend import db
from backend.models import User, Patient, Episode, Imagerie, Biologie
from backend.utils.patient_code import generate_unique_patient_code
from datetime import datetime, timedelta
import os

def drop_and_recreate(app):
    """Supprime et recrée toutes les tables
    
    Args:
        app: Instance Flask avec contexte d'application actif
    """
    print("=" * 80)
    print("SUPPRESSION ET RECRÉATION DU SCHÉMA")
    print("=" * 80)
    
    db.drop_all()
    db.create_all()
    db.session.commit()
    print("✓ Schéma recréé avec succès\n")

def create_admin(app):
    """Crée l'utilisateur administrateur avec tous les privilèges
    
    Args:
        app: Instance Flask avec contexte d'application actif
    """
    print("=" * 80)
    print("CRÉATION UTILISATEUR ADMIN")
    print("=" * 80)
    
    admin = User(username='admin')
    admin.set_password('admin123')
    admin.role = 'admin'
    admin.can_manage_patients = True
    admin.can_manage_episodes = True
    admin.can_export_data = True
    admin.can_manage_users = True
    db.session.add(admin)
    db.session.commit()
    print("✓ Utilisateur admin créé avec tous les privilèges\n")

def create_comprehensive_demo_data():
    """
    Crée 5 patients de démonstration avec données complètes
    Chaque patient représente un type de calcul spécifique
    
    Note: Cette fonction suppose qu'elle est appelée dans un contexte d'application actif
    """
    print("=" * 80)
    print("CRÉATION DES 5 PATIENTS DÉMONSTRATION")
    print("=" * 80)
    
    # Patient 1: Whewellite (Oxalate de calcium monohydraté)
    patient1 = Patient()
    patient1.code_patient = generate_unique_patient_code(lambda c: Patient.query.filter_by(code_patient=c).first() is not None)
    patient1.nom = "Kabongo"
    patient1.prenom = "Joseph"
    patient1.date_naissance = datetime(1968, 5, 12).date()
    patient1.sexe = "M"
    patient1.telephone = "+243815234567"
    patient1.email = "j.kabongo@email.cd"
    patient1.adresse = "Avenue du Commerce N°45, Commune de Gombe, Kinshasa"
    patient1.province = "Kinshasa"
    patient1.ville = "Kinshasa"
    patient1.groupe_ethnique = "Luba"
    patient1.profession = "Fonctionnaire"
    patient1.niveau_education = "Universitaire"
    patient1.statut_matrimonial = "Marie"
        
    # Anthropométrie et constantes vitales
    patient1.poids = 78.5
    patient1.taille = 172.0
    patient1.tension_arterielle_systolique = 142
    patient1.tension_arterielle_diastolique = 88
    patient1.frequence_cardiaque = 76
    patient1.temperature = 37.1
    patient1.frequence_respiratoire = 16
        
    # Antécédents
    patient1.antecedents_personnels = "Hypertension artérielle traitée depuis 2015. Goutte diagnostiquée en 2020. Calcul rénal traité par LEC en 2019."
    patient1.antecedents_familiaux = "Père: lithiase récidivante avec néphrectomie gauche à 65 ans. Mère: diabète type 2. Frère: hypertension."
    patient1.antecedents_chirurgicaux = "Appendicectomie 1992. Cholécystectomie laparoscopique 2018."
    patient1.allergies = "Pénicilline (éruption cutanée), iode (réaction anaphylactique)"
    patient1.traitements_chroniques = "Losartan 50mg/jour, Allopurinol 300mg/jour, Atorvastatine 20mg/jour"
        
    # Habitudes de vie
    patient1.tabac = "Non-fumeur"
    patient1.alcool = "Occasionnel (2-3 verres de vin/semaine)"
    patient1.hydratation_jour = 1.5
    patient1.regime_alimentaire = "Omnivore, consommation élevée de protéines animales"
    patient1.petit_dejeuner = "Café noir, pain beurré, omelette, jus d'orange frais"
    patient1.dejeuner = "Viande rouge ou poisson, fufu ou riz, légumes verts, fruits"
    patient1.diner = "Poulet grillé ou poisson, chikwangue, sauce tomate, légumes"
    patient1.grignotage = "Cacahuètes salées, biscuits, chocolat noir"
    patient1.autres_consommations = "Café 4-5 tasses/jour, thé vert 1-2 tasses/jour, chocolat chaud le soir"
        
    db.session.add(patient1)
    db.session.flush()
        
    # Épisode patient 1
    episode1 = Episode()
    episode1.patient_id = patient1.id
    episode1.date_episode = datetime(2025, 10, 15).date()
    episode1.motif = "Colique néphrétique droite récidivante, hématurie macroscopique"
    episode1.diagnostic = "Lithiase rénale droite de type whewellite avec hyperoxalurie primaire"
    episode1.douleur = True
    episode1.hematurie = True
    episode1.fievre = False
    episode1.infection_urinaire = False
        
    db.session.add(episode1)
    db.session.flush()
        
    # Imagerie patient 1
    img1 = Imagerie()
    img1.episode_id = episode1.id
    img1.date_examen = datetime(2025, 10, 15).date()
    img1.taille_mm = 9
    img1.densite_uh = 1450
    img1.densite_noyau = 1450
    img1.densites_couches = "Homogène, haute densité"
    img1.morphologie = "spherique_lisse"
    img1.radio_opacite = "opaque"
    img1.localisation = "Calice inférieur droit"
    img1.nombre_calculs = 1
    img1.topographie_calcul = "Calice inférieur droit"
    img1.diametre_longitudinal = 9.2
    img1.diametre_transversal = 8.5
    img1.forme_calcul = "Arrondie"
    img1.contour_calcul = "Lisse"
    img1.calcifications_autres = "Néphrocalcinose médullaire bilatérale discrète"
        
    # Retentissement rein gauche
    img1.rein_gauche_cranio_caudal = 108.5
    img1.rein_gauche_antero_posterieur = 52.3
    img1.rein_gauche_transversal = 48.1
    img1.rein_gauche_volume = 146.2
    img1.epaisseur_cortex_renal_gauche = 9.5
    img1.diametre_pyelon_gauche = 6.2
    img1.diametre_uretere_amont_gauche = 3.1
        
    # Retentissement rein droit
    img1.rein_droit_cranio_caudal = 112.8
    img1.rein_droit_antero_posterieur = 54.7
    img1.rein_droit_transversal = 50.3
    img1.rein_droit_volume = 162.5
    img1.epaisseur_cortex_renal_droit = 8.8
    img1.diametre_pyelon_droit = 12.5
    img1.diametre_uretere_amont_droit = 5.8
    img1.malformations_urinaires = "Aucune"
        
    db.session.add(img1)
        
    # Biologie patient 1
    bio1 = Biologie()
    bio1.episode_id = episode1.id
    bio1.date_examen = datetime(2025, 10, 15).date()
    bio1.ph_urinaire = 5.4
    bio1.densite_urinaire = 1.028
    bio1.sediment_urinaire = "Nombreux cristaux d'oxalate de calcium monohydraté en forme d'enveloppe, absence de cristaux d'acide urique"
    bio1.ecbu_resultats = "Stérile, leucocytes <10/mm³, hématies 50-100/mm³"
    bio1.infection_urinaire = False
        
    # Marqueurs métaboliques
    bio1.hyperoxalurie = True
    bio1.hypercalciurie = False
    bio1.hyperuricurie = False
    bio1.cystinurie = False
    bio1.hypercalcemie = False
    bio1.oxalurie_valeur = 62.0
    bio1.calciurie_valeur = 245.0
    bio1.uricurie_valeur = 450.0
    bio1.calciemie_valeur = 2.42
        
    # Hormones thyroïdiennes
    bio1.tsh = 1.8
    bio1.t3 = 1.6
    bio1.t4 = 10.2
    bio1.uree = 0.38
    bio1.creatinine = 95.0
        
    db.session.add(bio1)
        
    print(f"  ✓ Patient 1: {patient1.prenom} {patient1.nom} - Whewellite (hyperoxalurie)")
        
    # Patient 2: Struvite (Phosphate ammoniaco-magnésien)
    patient2 = Patient()
    patient2.code_patient = generate_unique_patient_code(lambda c: Patient.query.filter_by(code_patient=c).first() is not None)
    patient2.nom = "Mwamba"
    patient2.prenom = "Françoise"
    patient2.date_naissance = datetime(1985, 9, 28).date()
    patient2.sexe = "F"
    patient2.telephone = "+243826789012"
    patient2.email = "f.mwamba@email.cd"
    patient2.adresse = "Boulevard Lumumba N°123, Commune de Lubumbashi, Lubumbashi"
    patient2.province = "Haut-Katanga"
    patient2.ville = "Lubumbashi"
    patient2.groupe_ethnique = "Bembe"
    patient2.profession = "Enseignant"
    patient2.niveau_education = "Universitaire"
    patient2.statut_matrimonial = "Marie"
        
    patient2.poids = 68.0
    patient2.taille = 162.0
    patient2.tension_arterielle_systolique = 125
    patient2.tension_arterielle_diastolique = 78
    patient2.frequence_cardiaque = 82
    patient2.temperature = 38.5
    patient2.frequence_respiratoire = 20
        
    patient2.antecedents_personnels = "Infections urinaires récidivantes (8-10 épisodes/an depuis 2020). Reflux vésico-urétéral grade II diagnostiqué dans l'enfance. Diabète gestationnel en 2015."
    patient2.antecedents_familiaux = "Mère: infections urinaires récidivantes. Sœur: polykystose rénale."
    patient2.antecedents_chirurgicaux = "Césarienne 2015 et 2018. Cure de reflux vésico-urétéral en 1995."
    patient2.allergies = "Sulfamides (syndrome de Stevens-Johnson)"
    patient2.traitements_chroniques = "Prophylaxie antibiotique: Nitrofurantoïne 50mg/jour"
        
    patient2.tabac = "Non-fumeuse"
    patient2.alcool = "Non-consommatrice"
    patient2.hydratation_jour = 2.2
    patient2.regime_alimentaire = "Omnivore équilibré"
    patient2.petit_dejeuner = "Thé au lait, pain complet, confiture, yaourt"
    patient2.dejeuner = "Poisson ou poulet, riz, légumes variés, fruits frais"
    patient2.diner = "Soupe de légumes, pondu (feuilles de manioc), fufu, poisson"
    patient2.grignotage = "Fruits secs, noix de cajou"
    patient2.autres_consommations = "Eau plate principalement (2-3L/jour), infusions de plantes"
        
    db.session.add(patient2)
    db.session.flush()
        
    episode2 = Episode()
    episode2.patient_id = patient2.id
    episode2.date_episode = datetime(2025, 10, 20).date()
    episode2.motif = "Douleur lombaire gauche, fièvre 39°C, frissons, pyurie"
    episode2.diagnostic = "Pyélonéphrite aiguë sur calcul coralliforme gauche à Proteus mirabilis"
    episode2.douleur = True
    episode2.hematurie = False
    episode2.fievre = True
    episode2.infection_urinaire = True
    episode2.germe = "Proteus mirabilis"
    episode2.urease_positif = True
        
    db.session.add(episode2)
    db.session.flush()
        
    img2 = Imagerie()
    img2.episode_id = episode2.id
    img2.date_examen = datetime(2025, 10, 20).date()
    img2.taille_mm = 45
    img2.densite_uh = 720
    img2.densite_noyau = 720
    img2.densites_couches = "Hétérogène, aspect stratifié"
    img2.morphologie = "coralliforme"
    img2.radio_opacite = "transparent"
    img2.localisation = "Bassinet et calices gauches"
    img2.nombre_calculs = 1
    img2.topographie_calcul = "Calcul coralliforme occupant tout le système pyélocaliciel gauche"
    img2.diametre_longitudinal = 45.0
    img2.diametre_transversal = 32.0
    img2.forme_calcul = "Coralliforme"
    img2.contour_calcul = "Irregulier"
    img2.calcifications_autres = "Aucune calcification extra-rénale"
        
    img2.rein_gauche_cranio_caudal = 125.3
    img2.rein_gauche_antero_posterieur = 68.5
    img2.rein_gauche_transversal = 62.1
    img2.rein_gauche_volume = 278.4
    img2.epaisseur_cortex_renal_gauche = 6.2
    img2.diametre_pyelon_gauche = 28.5
    img2.diametre_uretere_amont_gauche = 4.8
        
    img2.rein_droit_cranio_caudal = 105.2
    img2.rein_droit_antero_posterieur = 51.8
    img2.rein_droit_transversal = 47.3
    img2.rein_droit_volume = 133.5
    img2.epaisseur_cortex_renal_droit = 9.8
    img2.diametre_pyelon_droit = 5.5
    img2.diametre_uretere_amont_droit = 2.9
    img2.malformations_urinaires = "Reflux vesico-ureteral"
        
    db.session.add(img2)
        
    bio2 = Biologie()
    bio2.episode_id = episode2.id
    bio2.date_examen = datetime(2025, 10, 20).date()
    bio2.ph_urinaire = 7.8
    bio2.densite_urinaire = 1.015
    bio2.sediment_urinaire = "Cristaux de phosphate ammoniaco-magnésien en forme de couvercle de cercueil, pyurie massive (>100 leucocytes/champ)"
    bio2.ecbu_resultats = "Culture positive: Proteus mirabilis >10^5 UFC/mL, sensible à Ceftriaxone"
    bio2.infection_urinaire = True
    bio2.germe = "Proteus mirabilis"
    bio2.urease_positif = True
        
    bio2.hyperoxalurie = False
    bio2.hypercalciurie = False
    bio2.hyperuricurie = False
    bio2.cystinurie = False
    bio2.hypercalcemie = False
    bio2.oxalurie_valeur = 28.0
    bio2.calciurie_valeur = 180.0
    bio2.uricurie_valeur = 380.0
    bio2.calciemie_valeur = 2.35
        
    bio2.tsh = 2.1
    bio2.t3 = 1.5
    bio2.t4 = 9.8
    bio2.uree = 0.52
    bio2.creatinine = 115.0
        
    db.session.add(bio2)
        
    print(f"  ✓ Patient 2: {patient2.prenom} {patient2.nom} - Struvite (infection à Proteus)")
        
    # Patient 3: Acide urique
    patient3 = Patient()
    patient3.code_patient = generate_unique_patient_code(lambda c: Patient.query.filter_by(code_patient=c).first() is not None)
    patient3.nom = "Tshilombo"
    patient3.prenom = "Marcel"
    patient3.date_naissance = datetime(1973, 3, 5).date()
    patient3.sexe = "M"
    patient3.telephone = "+243843210987"
    patient3.email = "m.tshilombo@email.cd"
    patient3.adresse = "Avenue Mobutu N°78, Commune de Kananga, Kananga"
    patient3.province = "Kasai-Central"
    patient3.ville = "Kananga"
    patient3.groupe_ethnique = "Lunda"
    patient3.profession = "Commercant"
    patient3.niveau_education = "Secondaire"
    patient3.statut_matrimonial = "Marie"
        
    patient3.poids = 102.0
    patient3.taille = 175.0
    patient3.tension_arterielle_systolique = 158
    patient3.tension_arterielle_diastolique = 95
    patient3.frequence_cardiaque = 88
    patient3.temperature = 37.0
    patient3.frequence_respiratoire = 18
        
    patient3.antecedents_personnels = "Syndrome métabolique avec obésité (IMC 33.3). Goutte sévère depuis 2015 avec crises articulaires fréquentes. Hypertension artérielle non contrôlée. Dyslipidémie mixte. Stéatose hépatique."
    patient3.antecedents_familiaux = "Père: infarctus du myocarde à 55 ans. Mère: diabète type 2. Oncle paternel: goutte et lithiase."
    patient3.antecedents_chirurgicaux = "Aucune intervention chirurgicale"
    patient3.allergies = "Aucune allergie connue"
    patient3.traitements_chroniques = "Allopurinol 300mg/jour (observance médiocre), Amlodipine 10mg/jour, Fénofibrate 160mg/jour"
        
    patient3.tabac = "Ancien fumeur (arrêt 2020, 20 paquets-années)"
    patient3.alcool = "Consommation excessive: 5-6 bières/jour + alcool fort le weekend"
    patient3.hydratation_jour = 0.7
    patient3.regime_alimentaire = "Hyperprotéiné, riche en purines, pauvre en fibres"
    patient3.petit_dejeuner = "Café sucré, pain blanc avec margarine, saucisses"
    patient3.dejeuner = "Viande rouge quotidienne (chèvre, bœuf), fufu, sauce grasse, peu de légumes"
    patient3.diner = "Poisson salé frit ou poulet rôti, chikwangue, haricots"
    patient3.grignotage = "Cacahuètes salées, chips, beignets frits"
    patient3.autres_consommations = "5-6 bières/jour, sodas sucrés (2-3 bouteilles/jour), café très sucré 4x/jour"
        
    db.session.add(patient3)
    db.session.flush()
        
    episode3 = Episode()
    episode3.patient_id = patient3.id
    episode3.date_episode = datetime(2025, 10, 25).date()
    episode3.motif = "Colique néphrétique bilatérale, oligurie, insuffisance rénale aiguë"
    episode3.diagnostic = "Lithiase urique bilatérale obstructive compliquée d'insuffisance rénale aiguë"
    episode3.douleur = True
    episode3.hematurie = True
    episode3.fievre = False
    episode3.infection_urinaire = False
        
    db.session.add(episode3)
    db.session.flush()
        
    img3 = Imagerie()
    img3.episode_id = episode3.id
    img3.date_examen = datetime(2025, 10, 25).date()
    img3.taille_mm = 18
    img3.densite_uh = 480
    img3.densite_noyau = 480
    img3.densites_couches = "Homogène, faible densité"
    img3.morphologie = "spherique_lisse"
    img3.radio_opacite = "transparent"
    img3.localisation = "Uretère lombaire droit + bassinet gauche"
    img3.nombre_calculs = 3
    img3.topographie_calcul = "Calcul uretéral droit 18mm, calcul bassinet gauche 12mm, calcul caliciel inférieur droit 8mm"
    img3.diametre_longitudinal = 18.5
    img3.diametre_transversal = 15.2
    img3.forme_calcul = "Irreguliere"
    img3.contour_calcul = "Lisse"
    img3.calcifications_autres = "Néphrocalcinose médullaire bilatérale diffuse, calcifications vasculaires aortiques"
        
    img3.rein_gauche_cranio_caudal = 118.5
    img3.rein_gauche_antero_posterieur = 62.8
    img3.rein_gauche_transversal = 58.3
    img3.rein_gauche_volume = 225.8
    img3.epaisseur_cortex_renal_gauche = 7.5
    img3.diametre_pyelon_gauche = 22.5
    img3.diametre_uretere_amont_gauche = 7.2
        
    img3.rein_droit_cranio_caudal = 122.3
    img3.rein_droit_antero_posterieur = 65.2
    img3.rein_droit_transversal = 60.5
    img3.rein_droit_volume = 251.3
    img3.epaisseur_cortex_renal_droit = 7.1
    img3.diametre_pyelon_droit = 28.8
    img3.diametre_uretere_amont_droit = 12.5
    img3.malformations_urinaires = "Aucune"
        
    db.session.add(img3)
        
    bio3 = Biologie()
    bio3.episode_id = episode3.id
    bio3.date_examen = datetime(2025, 10, 25).date()
    bio3.ph_urinaire = 5.0
    bio3.densite_urinaire = 1.035
    bio3.sediment_urinaire = "Très nombreux cristaux d'acide urique en rosette et en tonnelet, cristaux d'urate amorphe abondants"
    bio3.ecbu_resultats = "Stérile, hématies 20-30/mm³, leucocytes <5/mm³"
    bio3.infection_urinaire = False
        
    bio3.hyperoxalurie = False
    bio3.hypercalciurie = False
    bio3.hyperuricurie = True
    bio3.cystinurie = False
    bio3.hypercalcemie = False
    bio3.oxalurie_valeur = 32.0
    bio3.calciurie_valeur = 285.0
    bio3.uricurie_valeur = 1250.0
    bio3.calciemie_valeur = 2.48
        
    bio3.tsh = 2.5
    bio3.t3 = 1.4
    bio3.t4 = 9.2
    bio3.uree = 1.85
    bio3.creatinine = 285.0
        
    db.session.add(bio3)
        
    print(f"  ✓ Patient 3: {patient3.prenom} {patient3.nom} - Acide urique (syndrome métabolique)")
        
    # Patient 4: Weddellite (Oxalate de calcium dihydraté)
    patient4 = Patient()
    patient4.code_patient = generate_unique_patient_code(lambda c: Patient.query.filter_by(code_patient=c).first() is not None)
    patient4.nom = "Kasongo"
    patient4.prenom = "Marie"
    patient4.date_naissance = datetime(1992, 11, 18).date()
    patient4.sexe = "F"
    patient4.telephone = "+243857896543"
    patient4.email = "m.kasongo@email.cd"
    patient4.adresse = "Rue de la Paix N°56, Commune de Bukavu, Bukavu"
    patient4.province = "Sud-Kivu"
    patient4.ville = "Bukavu"
    patient4.groupe_ethnique = "Shi"
    patient4.profession = "Infirmier"
    patient4.niveau_education = "Superieur"
    patient4.statut_matrimonial = "Celibataire"
        
    patient4.poids = 52.0
    patient4.taille = 158.0
    patient4.tension_arterielle_systolique = 108
    patient4.tension_arterielle_diastolique = 68
    patient4.frequence_cardiaque = 68
    patient4.temperature = 36.8
    patient4.frequence_respiratoire = 14
        
    patient4.antecedents_personnels = "Maladie de Crohn diagnostiquée en 2015, évolution par poussées. Résection iléale de 80cm en 2017 pour sténose serrée. Diarrhée chronique. Malabsorption. Anémie ferriprive chronique."
    patient4.antecedents_familiaux = "Mère: maladie cœliaque. Frère: maladie de Crohn."
    patient4.antecedents_chirurgicaux = "Résection iléo-caecale 2017 avec iléo-colostomie termino-terminale"
    patient4.allergies = "Lactose (intolérance sévère)"
    patient4.traitements_chroniques = "Azathioprine 150mg/jour, Mésalazine 4g/jour, Supplémentation fer 200mg/jour, Vitamine D 100000UI/mois, Calcium 1g/jour"
        
    patient4.tabac = "Non-fumeuse"
    patient4.alcool = "Non-consommatrice"
    patient4.hydratation_jour = 2.5
    patient4.regime_alimentaire = "Régime pauvre en fibres, sans lactose, enrichi en protéines"
    patient4.petit_dejeuner = "Thé nature, pain blanc grillé, compote de pommes"
    patient4.dejeuner = "Poulet bouilli ou poisson vapeur, riz blanc, carottes cuites"
    patient4.diner = "Soupe de légumes mixée, purée de pommes de terre, yaourt sans lactose"
    patient4.grignotage = "Bananes bien mûres, compotes"
    patient4.autres_consommations = "Eau plate exclusivement (2.5-3L/jour), tisanes digestives"
        
    db.session.add(patient4)
    db.session.flush()
        
    episode4 = Episode()
    episode4.patient_id = patient4.id
    episode4.date_episode = datetime(2025, 11, 1).date()
    episode4.motif = "Lithiase récidivante, 4e épisode en 2 ans, multiples calculs bilatéraux"
    episode4.diagnostic = "Lithiase calcique récidivante secondaire à hyperoxalurie entérique post-résection iléale"
    episode4.douleur = True
    episode4.hematurie = True
    episode4.fievre = False
    episode4.infection_urinaire = False
        
    db.session.add(episode4)
    db.session.flush()
        
    img4 = Imagerie()
    img4.episode_id = episode4.id
    img4.date_examen = datetime(2025, 11, 1).date()
    img4.taille_mm = 6
    img4.densite_uh = 1180
    img4.densite_noyau = 1180
    img4.densites_couches = "Homogène"
    img4.morphologie = "irreguliere_spiculee"
    img4.radio_opacite = "opaque"
    img4.localisation = "Multiples calculs bilatéraux"
    img4.nombre_calculs = 12
    img4.topographie_calcul = "Rein droit: 5 calculs (calices sup, moy, inf). Rein gauche: 7 calculs (calices inf x3, moy x2, sup x2)"
    img4.diametre_longitudinal = 6.5
    img4.diametre_transversal = 5.2
    img4.forme_calcul = "Irreguliere"
    img4.contour_calcul = "Irregulier"
    img4.calcifications_autres = "Néphrocalcinose corticale et médullaire diffuse bilatérale"
        
    img4.rein_gauche_cranio_caudal = 98.5
    img4.rein_gauche_antero_posterieur = 48.2
    img4.rein_gauche_transversal = 44.5
    img4.rein_gauche_volume = 109.2
    img4.epaisseur_cortex_renal_gauche = 8.5
    img4.diametre_pyelon_gauche = 7.8
    img4.diametre_uretere_amont_gauche = 3.5
        
    img4.rein_droit_cranio_caudal = 102.3
    img4.rein_droit_antero_posterieur = 50.1
    img4.rein_droit_transversal = 46.8
    img4.rein_droit_volume = 122.8
    img4.epaisseur_cortex_renal_droit = 8.2
    img4.diametre_pyelon_droit = 8.5
    img4.diametre_uretere_amont_droit = 3.8
    img4.malformations_urinaires = "Aucune"
        
    db.session.add(img4)
        
    bio4 = Biologie()
    bio4.episode_id = episode4.id
    bio4.date_examen = datetime(2025, 11, 1).date()
    bio4.ph_urinaire = 5.6
    bio4.densite_urinaire = 1.022
    bio4.sediment_urinaire = "Cristaux d'oxalate de calcium dihydraté (weddellite) en bipyramide quadratique, quelques cristaux d'oxalate monohydraté"
    bio4.ecbu_resultats = "Stérile, hématies 15-20/mm³"
    bio4.infection_urinaire = False
        
    bio4.hyperoxalurie = True
    bio4.hypercalciurie = True
    bio4.hyperuricurie = False
    bio4.cystinurie = False
    bio4.hypercalcemie = False
    bio4.oxalurie_valeur = 95.0
    bio4.calciurie_valeur = 380.0
    bio4.uricurie_valeur = 420.0
    bio4.calciemie_valeur = 2.28
        
    bio4.tsh = 1.9
    bio4.t3 = 1.5
    bio4.t4 = 9.5
    bio4.uree = 0.42
    bio4.creatinine = 88.0
        
    db.session.add(bio4)
        
    print(f"  ✓ Patient 4: {patient4.prenom} {patient4.nom} - Weddellite (hyperoxalurie entérique)")
        
    # Patient 5: Brushite (Phosphate de calcium)
    patient5 = Patient()
    patient5.code_patient = generate_unique_patient_code(lambda c: Patient.query.filter_by(code_patient=c).first() is not None)
    patient5.nom = "Ngoy"
    patient5.prenom = "Pierre"
    patient5.date_naissance = datetime(1965, 2, 14).date()
    patient5.sexe = "M"
    patient5.telephone = "+243869876543"
    patient5.email = "p.ngoy@email.cd"
    patient5.adresse = "Avenue Kasa-Vubu N°234, Commune de Kisangani, Kisangani"
    patient5.province = "Tshopo"
    patient5.ville = "Kisangani"
    patient5.groupe_ethnique = "Mongo"
    patient5.profession = "Retraite"
    patient5.niveau_education = "Secondaire"
    patient5.statut_matrimonial = "Veuf"
        
    patient5.poids = 71.0
    patient5.taille = 168.0
    patient5.tension_arterielle_systolique = 135
    patient5.tension_arterielle_diastolique = 82
    patient5.frequence_cardiaque = 74
    patient5.temperature = 37.3
    patient5.frequence_respiratoire = 16
        
    patient5.antecedents_personnels = "Hyperparathyroïdie primaire sur adénome parathyroïdien diagnostiquée en 2023. Ostéoporose sévère avec fractures vertébrales (T12, L1). Lithiase rénale récidivante depuis 2020. Ulcère gastrique en 2018."
    patient5.antecedents_familiaux = "Père: décédé à 68 ans d'insuffisance rénale. Mère: ostéoporose sévère."
    patient5.antecedents_chirurgicaux = "Parathyroïdectomie prévue en 2026"
    patient5.allergies = "Aucune allergie connue"
    patient5.traitements_chroniques = "Oméprazole 20mg/jour, Calcium 1g/jour, Vitamine D 800UI/jour, Paracétamol selon besoin"
        
    patient5.tabac = "Ancien fumeur (arrêt 2010, 30 paquets-années)"
    patient5.alcool = "Occasionnel (1-2 verres de vin traditionnel/semaine)"
    patient5.hydratation_jour = 1.8
    patient5.regime_alimentaire = "Omnivore, consommation élevée de produits laitiers"
    patient5.petit_dejeuner = "Café au lait, pain beurré, fromage"
    patient5.dejeuner = "Viande ou poisson, riz ou fufu, légumes, fruits"
    patient5.diner = "Soupe, pondu, chikwangue, sardines"
    patient5.grignotage = "Lait caillé, fruits"
    patient5.autres_consommations = "Lait 2-3 verres/jour, café au lait 3x/jour"
        
    db.session.add(patient5)
    db.session.flush()
        
    episode5 = Episode()
    episode5.patient_id = patient5.id
    episode5.date_episode = datetime(2025, 11, 5).date()
    episode5.motif = "Lithiase récidivante rapide, 3e récidive en 18 mois malgré traitement"
    episode5.diagnostic = "Lithiase brushite récidivante sur hyperparathyroïdie primaire avec hypercalcémie et hypercalciurie sévères"
    episode5.douleur = True
    episode5.hematurie = False
    episode5.fievre = False
    episode5.infection_urinaire = False
        
    db.session.add(episode5)
    db.session.flush()
        
    img5 = Imagerie()
    img5.episode_id = episode5.id
    img5.date_examen = datetime(2025, 11, 5).date()
    img5.taille_mm = 14
    img5.densite_uh = 1750
    img5.densite_noyau = 1750
    img5.densites_couches = "Très haute densité, homogène"
    img5.morphologie = "irreguliere_spiculee"
    img5.radio_opacite = "opaque"
    img5.localisation = "Calice moyen droit"
    img5.nombre_calculs = 2
    img5.topographie_calcul = "Calcul caliciel moyen droit 14mm, calcul bassinet gauche 7mm"
    img5.diametre_longitudinal = 14.2
    img5.diametre_transversal = 11.8
    img5.forme_calcul = "Irreguliere"
    img5.contour_calcul = "Irregulier"
    img5.calcifications_autres = "Néphrocalcinose médullaire bilatérale, calcifications vasculaires rénales, déminéralisation osseuse diffuse"
        
    img5.rein_gauche_cranio_caudal = 104.5
    img5.rein_gauche_antero_posterieur = 49.8
    img5.rein_gauche_transversal = 46.2
    img5.rein_gauche_volume = 124.5
    img5.epaisseur_cortex_renal_gauche = 8.8
    img5.diametre_pyelon_gauche = 9.2
    img5.diametre_uretere_amont_gauche = 3.2
        
    img5.rein_droit_cranio_caudal = 107.8
    img5.rein_droit_antero_posterieur = 52.3
    img5.rein_droit_transversal = 48.5
    img5.rein_droit_volume = 142.8
    img5.epaisseur_cortex_renal_droit = 8.5
    img5.diametre_pyelon_droit = 10.5
    img5.diametre_uretere_amont_droit = 3.5
    img5.malformations_urinaires = "Aucune"
        
    db.session.add(img5)
        
    bio5 = Biologie()
    bio5.episode_id = episode5.id
    bio5.date_examen = datetime(2025, 11, 5).date()
    bio5.ph_urinaire = 6.4
    bio5.densite_urinaire = 1.018
    bio5.sediment_urinaire = "Cristaux de phosphate de calcium en forme de rosette et d'étoile, absence de cristaux d'acide urique"
    bio5.ecbu_resultats = "Stérile, hématies <5/mm³"
    bio5.infection_urinaire = False
        
    bio5.hyperoxalurie = False
    bio5.hypercalciurie = True
    bio5.hyperuricurie = False
    bio5.cystinurie = False
    bio5.hypercalcemie = True
    bio5.oxalurie_valeur = 35.0
    bio5.calciurie_valeur = 520.0
    bio5.uricurie_valeur = 410.0
    bio5.calciemie_valeur = 2.98
        
    bio5.tsh = 2.2
    bio5.t3 = 1.6
    bio5.t4 = 10.1
    bio5.uree = 0.48
    bio5.creatinine = 105.0
        
    # Marqueurs parathyroïdiens
    bio5.pth = 185.0  # Très élevée (N: 10-65 pg/mL)
    bio5.phosphoremie = 0.68  # Basse (N: 0.8-1.5 mmol/L)
        
    db.session.add(bio5)
        
    print(f"  ✓ Patient 5: {patient5.prenom} {patient5.nom} - Brushite (hyperparathyroïdie)")
        
    db.session.commit()
    print(f"\n✅ 5 patients démonstration créés avec succès!")
    print("=" * 80)

def main():
    """Fonction principale pour l'exécution en standalone - crée sa propre app"""
    print("\n")
    print("╔" + "=" * 78 + "╗")
    print("║" + " " * 10 + "CRÉATION DES DONNÉES DÉMONSTRATION COMPLÈTES - KALONJI" + " " * 11 + "║")
    print("╚" + "=" * 78 + "╝")
    print("\n")
    
    input("⚠️  Cette opération va SUPPRIMER TOUTES LES DONNÉES existantes.\n    Appuyez sur Entrée pour continuer ou Ctrl+C pour annuler... ")
    print()
    
    # Importer create_app uniquement ici (pas au niveau du module)
    from backend import create_app
    
    # Créer l'app uniquement pour l'exécution standalone
    app = create_app()
    
    with app.app_context():
        drop_and_recreate(app)
        create_admin(app)
        create_comprehensive_demo_data()
    
    print("╔" + "=" * 78 + "╗")
    print("║" + " " * 20 + "✅ INITIALISATION TERMINÉE AVEC SUCCÈS" + " " * 19 + "║")
    print("╚" + "=" * 78 + "╝")
    print()
    print("📝 5 Patients démonstration créés:")
    print("   1. Joseph Kabongo - Whewellite (hyperoxalurie primaire)")
    print("   2. Françoise Mwamba - Struvite (infection à Proteus mirabilis)")
    print("   3. Marcel Tshilombo - Acide urique (syndrome métabolique)")
    print("   4. Marie Kasongo - Weddellite (hyperoxalurie entérique post-chirurgie)")
    print("   5. Pierre Ngoy - Brushite (hyperparathyroïdie primaire)")
    print()
    print("🔐 Connexion: admin / admin123")
    print()

if __name__ == '__main__':
    main()
