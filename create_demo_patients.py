from backend import create_app, db
from backend.models import Patient, Episode, Imagerie, Biologie
from datetime import datetime, timedelta
import random
import uuid

app = create_app()

with app.app_context():
    demo_patients = [
        {
            "nom": "Dupont",
            "prenom": "Jean",
            "date_naissance": datetime(1975, 3, 15).date(),
            "sexe": "M",
            "telephone": "0612345678",
            "email": "jean.dupont@email.com",
            "adresse": "15 rue de la République, 75001 Paris",
            "groupe_ethnique": "Caucasien",
            "poids": 82.5,
            "taille": 178.0,
            "antecedents_personnels": "Hypertension artérielle depuis 2015, Diabète de type 2 depuis 2018",
            "antecedents_familiaux": "Père ayant eu des calculs rénaux récidivants, Mère hypertendue",
            "antecedents_chirurgicaux": "Appendicectomie en 2000",
            "allergies": "Pénicilline",
            "traitements_chroniques": "Metformine 1000mg 2x/jour, Ramipril 5mg 1x/jour",
            "hydratation_jour": 1.2,
            "regime_alimentaire": "Régime hyperprotéiné, consommation élevée de produits laitiers",
            "petit_dejeuner": "Café au lait, pain blanc avec beurre et confiture, yaourt",
            "dejeuner": "Viande rouge 4-5x/semaine, fromage quotidien, peu de légumes",
            "diner": "Souvent charcuterie ou reste du midi, fromage",
            "grignotage": "Cacahuètes salées, chips",
            "autres_consommations": "2-3 verres de vin rouge par jour, café 5x/jour",
            "asp_resultats": "Calcul radio-opaque de 8mm au niveau du rein droit",
            "echographie_resultats": "Calcul hyperéchogène de 8x6mm dans le calice inférieur droit avec cône d'ombre postérieur",
            "uroscanner_resultats": "Calcul de 8mm densité 950 UH, localisation calicielle inférieure droite, pas de dilatation des cavités pyélocalicielles",
            "sediment_urinaire": "Cristaux d'oxalate de calcium monohydraté (whewellite) nombreux",
            "ecbu_resultats": "Stérile, absence de leucocytes",
            "ph_urinaire": 5.8,
            "densite_urinaire": 1.025,
            "nombre_calculs": 1,
            "topographie_calcul": "Calice inférieur droit",
            "diametre_longitudinal": 8.2,
            "diametre_transversal": 6.1,
            "forme_calcul": "Ovoïde",
            "contour_calcul": "Régulier, surface lisse",
            "densite_noyau": 950,
            "densites_couches": "Homogène, pas de stratification visible",
            "calcifications_autres": "Pas d'autres calcifications",
            "notes": "Patient récidivant (3ème épisode en 5 ans). Mauvaise observance des conseils diététiques. Hydratation insuffisante chronique."
        },
        {
            "nom": "Martin",
            "prenom": "Sophie",
            "date_naissance": datetime(1988, 7, 22).date(),
            "sexe": "F",
            "telephone": "0687654321",
            "email": "sophie.martin@email.com",
            "adresse": "42 avenue des Champs, 69002 Lyon",
            "groupe_ethnique": "Caucasienne",
            "poids": 58.0,
            "taille": 165.0,
            "antecedents_personnels": "Infections urinaires récidivantes (5-6 par an), Maladie de Crohn diagnostiquée en 2015",
            "antecedents_familiaux": "Mère avec lithiase urinaire",
            "antecedents_chirurgicaux": "Résection intestinale partielle en 2016 pour maladie de Crohn",
            "allergies": "Aucune allergie connue",
            "traitements_chroniques": "Azathioprine 150mg/jour, Mésalazine 3g/jour, Compléments en vitamine D et calcium",
            "hydratation_jour": 1.8,
            "regime_alimentaire": "Régime pauvre en fibres, faible consommation de produits laitiers",
            "petit_dejeuner": "Thé, biscottes, compote",
            "dejeuner": "Viande blanche ou poisson, riz ou pâtes, compote",
            "diner": "Soupe, jambon, purée de légumes",
            "grignotage": "Biscuits secs",
            "autres_consommations": "Eau plate principalement, thé vert 2-3x/jour",
            "asp_resultats": "Multiple petits calculs radio-opaques au niveau du rein gauche",
            "echographie_resultats": "Multiples microlithiases bilatérales, la plus volumineuse mesurant 5mm au pôle inférieur gauche",
            "uroscanner_resultats": "Multiples calculs bilatéraux de 2-5mm, densité 1200-1400 UH, distribution corticale et médullaire",
            "sediment_urinaire": "Cristaux d'oxalate de calcium dihydraté (weddellite) abondants, quelques cristaux de phosphate",
            "ecbu_resultats": "E. coli > 100000 UFC/ml, sensible à Fosfomycine",
            "ph_urinaire": 6.5,
            "densite_urinaire": 1.018,
            "nombre_calculs": 8,
            "topographie_calcul": "Bilatérale, prédominance calices inférieurs",
            "diametre_longitudinal": 5.0,
            "diametre_transversal": 4.2,
            "forme_calcul": "Arrondie",
            "contour_calcul": "Régulier",
            "densite_noyau": 1300,
            "densites_couches": "Homogène",
            "calcifications_autres": "Calcifications vasculaires mineures",
            "notes": "Hyperoxalurie secondaire à la malabsorption intestinale (maladie de Crohn). Infections urinaires favorisées par les calculs. Bon suivi diététique mais difficulté à augmenter l'apport calcique oral."
        },
        {
            "nom": "Benali",
            "prenom": "Karim",
            "date_naissance": datetime(1982, 11, 8).date(),
            "sexe": "M",
            "telephone": "0623456789",
            "email": "k.benali@email.com",
            "adresse": "8 boulevard Saint-Michel, 13001 Marseille",
            "groupe_ethnique": "Nord-Africain",
            "poids": 95.0,
            "taille": 172.0,
            "antecedents_personnels": "Obésité (IMC 32), Goutte depuis 2019, Stéatose hépatique",
            "antecedents_familiaux": "Père diabétique, oncle maternel avec lithiase",
            "antecedents_chirurgicaux": "Aucune chirurgie",
            "allergies": "Allergie aux AINS (urticaire)",
            "traitements_chroniques": "Allopurinol 300mg/jour, Atorvastatine 20mg/jour",
            "hydratation_jour": 0.8,
            "regime_alimentaire": "Alimentation riche en purines (viandes, fruits de mer), consommation excessive de sodas",
            "petit_dejeuner": "Café sucré, viennoiseries",
            "dejeuner": "Viande rouge quotidienne, frites ou pâtes, dessert sucré, soda",
            "diner": "Pizza ou fast-food 3-4x/semaine, bière le weekend",
            "grignotage": "Biscuits, chocolat, sodas entre les repas",
            "autres_consommations": "2-3 canettes de soda par jour, 3-4 bières le weekend",
            "asp_resultats": "Calcul faiblement radio-opaque de 12mm au niveau du bassinet gauche",
            "echographie_resultats": "Calcul de 12x10mm dans le bassinet gauche avec discrète dilatation pyélocalicielle",
            "uroscanner_resultats": "Calcul de 12mm densité 450 UH (faible densité évoquant acide urique), dilatation grade 1 des cavités pyélocalicielles gauches",
            "sediment_urinaire": "Nombreux cristaux d'acide urique en rosette",
            "ecbu_resultats": "Stérile",
            "ph_urinaire": 5.2,
            "densite_urinaire": 1.032,
            "nombre_calculs": 1,
            "topographie_calcul": "Bassinet gauche",
            "diametre_longitudinal": 12.0,
            "diametre_transversal": 10.5,
            "forme_calcul": "Mamelonnée",
            "contour_calcul": "Irrégulier, aspect spiculé",
            "densite_noyau": 450,
            "densites_couches": "Densité faible et homogène",
            "calcifications_autres": "Néphrocalcinose médullaire débutante",
            "notes": "Lithiase urique pure favorisée par pH urinaire acide chronique, hyperuricurie, déshydratation et surpoids. Syndrome métabolique associé. Nécessité d'alcalinisation des urines et modification drastique du régime alimentaire."
        },
        {
            "nom": "Lefebvre",
            "prenom": "Claire",
            "date_naissance": datetime(1995, 2, 14).date(),
            "sexe": "F",
            "telephone": "0756789012",
            "email": "claire.lefebvre@email.com",
            "adresse": "23 rue du Commerce, 33000 Bordeaux",
            "groupe_ethnique": "Caucasienne",
            "poids": 52.0,
            "taille": 168.0,
            "antecedents_personnels": "Cystinurie diagnostiquée à l'âge de 12 ans, Hypothyroïdie",
            "antecedents_familiaux": "Frère également atteint de cystinurie",
            "antecedents_chirurgicaux": "3 lithotritie extracorporelles entre 2007 et 2020, Néphrolithotomie percutanée en 2018",
            "allergies": "Aucune",
            "traitements_chroniques": "Tiopronine 800mg/jour, Levothyroxine 75µg/jour, Citrate de potassium 30mEq/jour",
            "hydratation_jour": 3.5,
            "regime_alimentaire": "Régime pauvre en méthionine, faible en protéines animales",
            "petit_dejeuner": "Thé, céréales, fruits frais, jus d'orange",
            "dejeuner": "Poisson ou volaille (portions limitées), légumes abondants, féculents",
            "diner": "Légumineuses, salade, fruits",
            "grignotage": "Fruits secs non salés, fruits frais",
            "autres_consommations": "Eau alcaline 3-4L/jour, tisanes",
            "asp_resultats": "Multiples calculs faiblement radio-opaques bilatéraux",
            "echographie_resultats": "Multiples calculs bilatéraux, le plus volumineux de 15mm au niveau du bassinet droit",
            "uroscanner_resultats": "Calculs multiples bilatéraux de densité homogène 600-700 UH (typique de la cystine), le plus gros mesurant 15mm dans le bassinet droit",
            "sediment_urinaire": "Cristaux hexagonaux pathognomoniques de cystine en grande quantité",
            "ecbu_resultats": "Stérile",
            "ph_urinaire": 7.2,
            "densite_urinaire": 1.010,
            "nombre_calculs": 12,
            "topographie_calcul": "Bilatérale, bassinet et calices",
            "diametre_longitudinal": 15.0,
            "diametre_transversal": 14.0,
            "forme_calcul": "Ronde, aspect cireux",
            "contour_calcul": "Lisse, régulier",
            "densite_noyau": 650,
            "densites_couches": "Homogène, densité intermédiaire",
            "calcifications_autres": "Pas d'autres calcifications",
            "notes": "Cystinurie homozygote. Excellente observance thérapeutique et diététique. Malgré traitement optimal, récidives fréquentes dues à la nature génétique de la maladie. Surveillance rapprochée tous les 6 mois."
        },
        {
            "nom": "Rousseau",
            "prenom": "Pierre",
            "date_naissance": datetime(1968, 9, 30).date(),
            "sexe": "M",
            "telephone": "0698765432",
            "email": "p.rousseau@email.com",
            "adresse": "56 rue Pasteur, 59000 Lille",
            "groupe_ethnique": "Caucasien",
            "poids": 78.0,
            "taille": 175.0,
            "antecedents_personnels": "Hyperparathyroïdie primaire diagnostiquée en 2020, Infections urinaires occasionnelles",
            "antecedents_familiaux": "Mère avec lithiase calcique récidivante",
            "antecedents_chirurgicaux": "Parathyroïdectomie partielle en 2021",
            "allergies": "Aucune",
            "traitements_chroniques": "Calcium + Vitamine D3 500mg/400UI, Surveillance PTH/calcémie trimestrielle",
            "hydratation_jour": 1.5,
            "regime_alimentaire": "Régime équilibré, consommation modérée de produits laitiers",
            "petit_dejeuner": "Café, pain complet, fromage blanc, fruits",
            "dejeuner": "Viande ou poisson, légumes verts, féculents complets",
            "diner": "Salade composée, œufs ou volaille, yaourt",
            "grignotage": "Fruits frais, noix",
            "autres_consommations": "Eau minérale 1.5L/jour, thé vert",
            "asp_resultats": "Calcul radio-opaque de 10mm au niveau de l'uretère proximal droit avec structure stratifiée",
            "echographie_resultats": "Calcul de 10mm bloqué à la jonction pyélo-urétérale droite avec dilatation modérée des cavités",
            "uroscanner_resultats": "Calcul de 10mm avec structure radiaire caractéristique: densité centrale 980 UH, couches périphériques de densité décroissante (720 et 640 UH), suggestif de composition mixte",
            "sediment_urinaire": "Cristaux mixtes d'oxalate de calcium monohydraté et dihydraté, quelques cristaux de phosphate de calcium",
            "ecbu_resultats": "Quelques leucocytes 15/mm3, culture négative",
            "ph_urinaire": 6.2,
            "densite_urinaire": 1.022,
            "nombre_calculs": 1,
            "topographie_calcul": "Jonction pyélo-urétérale droite",
            "diametre_longitudinal": 10.5,
            "diametre_transversal": 9.8,
            "forme_calcul": "Ovoïde stratifiée",
            "contour_calcul": "Régulier avec stratifications visibles",
            "densite_noyau": 980,
            "densites_couches": "Couche 1: 980 UH, couche 2: 720 UH, couche 3: 640 UH",
            "calcifications_autres": "Discrètes calcifications médullaires bilatérales",
            "notes": "Calcul mixte post-hyperparathyroïdie avec structure radiaire typique. Noyau probablement Whewellite pur formé en période d'hypercalciurie sévère, couches externes Weddellite formées après parathyroïdectomie. Infection urinaire subclinique possible favorisant formation de couche phosphatée externe."
        }
    ]
    
    print("Création des patients de démonstration...")
    
    for patient_data in demo_patients:
        existing = Patient.query.filter_by(
            _nom=patient_data['nom'],
            _prenom=patient_data['prenom']
        ).first()
        
        if existing:
            print(f"Patient {patient_data['nom']} {patient_data['prenom']} existe déjà, passage au suivant...")
            continue
        
        patient = Patient()
        patient.code_patient = str(uuid.uuid4())
        for key, value in patient_data.items():
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
        episode.fievre = patient_data.get('sexe') == 'F' and 'Martin' in patient_data.get('nom', '')
        episode.infection_urinaire = patient_data.get('sexe') == 'F' and 'Martin' in patient_data.get('nom', '')
        
        if episode.infection_urinaire:
            episode.germe = "E. coli"
            episode.urease_positif = False
        
        db.session.add(episode)
        db.session.flush()
        
        imagerie = Imagerie()
        imagerie.episode_id = episode.id
        imagerie.date_examen = episode_date
        imagerie.taille_mm = int(patient_data.get('diametre_longitudinal', 8))
        imagerie.densite_uh = patient_data.get('densite_noyau', 900)
        imagerie.densite_noyau = patient_data.get('densite_noyau', 900)
        imagerie.densites_couches = patient_data.get('densites_couches', '')
        imagerie.morphologie = patient_data.get('forme_calcul', 'Ronde')
        imagerie.radio_opacite = "Opaque" if patient_data.get('densite_noyau', 900) > 500 else "Faiblement opaque"
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
        imagerie.asp_resultats = patient_data.get('asp_resultats', '')
        imagerie.echographie_resultats = patient_data.get('echographie_resultats', '')
        imagerie.uroscanner_resultats = patient_data.get('uroscanner_resultats', '')
        
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
            biologie.germe = "E. coli"
            biologie.urease_positif = False
        
        if 'Benali' in patient_data.get('nom', ''):
            biologie.hyperuricurie = True
            biologie.uricurie_valeur = 850.0
            biologie.calciurie_valeur = 280.0
            biologie.oxalurie_valeur = 35.0
            biologie.calciemie_valeur = 2.45
            biologie.tsh = 1.8
            biologie.t3 = 1.5
            biologie.t4 = 9.5
        elif 'Martin' in patient_data.get('nom', ''):
            biologie.hyperoxalurie = True
            biologie.oxalurie_valeur = 65.0
            biologie.calciurie_valeur = 220.0
            biologie.calciemie_valeur = 2.3
            biologie.tsh = 2.1
            biologie.t3 = 1.6
            biologie.t4 = 10.2
        elif 'Dupont' in patient_data.get('nom', ''):
            biologie.hypercalciurie = True
            biologie.calciurie_valeur = 320.0
            biologie.oxalurie_valeur = 38.0
            biologie.calciemie_valeur = 2.55
            biologie.tsh = 1.2
            biologie.t3 = 1.7
            biologie.t4 = 11.0
        elif 'Lefebvre' in patient_data.get('nom', ''):
            biologie.cystinurie = True
            biologie.oxalurie_valeur = 30.0
            biologie.calciurie_valeur = 180.0
            biologie.calciemie_valeur = 2.35
            biologie.tsh = 3.5
            biologie.t3 = 1.2
            biologie.t4 = 8.5
        elif 'Rousseau' in patient_data.get('nom', ''):
            biologie.hypercalciurie = True
            biologie.hypercalcemie = True
            biologie.calciurie_valeur = 340.0
            biologie.oxalurie_valeur = 42.0
            biologie.calciemie_valeur = 2.75
            biologie.tsh = 0.3
            biologie.t3 = 2.4
            biologie.t4 = 13.5
        
        db.session.add(biologie)
        
        print(f"✓ Patient créé: {patient_data['prenom']} {patient_data['nom']}")
    
    db.session.commit()
    print(f"\n{len(demo_patients)} patients de démonstration créés avec succès!")
    print("Vous pouvez maintenant vous connecter avec admin/admin123 pour les consulter.")
