"""
Options prédéfinies pour les champs du formulaire patient
=========================================================
Ce fichier définit toutes les options possibles pour les champs à choix unique ou multiple
Utilisé par le frontend (listes déroulantes, cases à cocher) et le backend (validation)
=========================================================
"""

# Antécédents familiaux (lithiase) - Cases à cocher (choix multiple)
ANTECEDENTS_FAMILIAUX_OPTIONS = [
    "Lithiase rénale récidivante",
    "Néphrectomie pour lithiase",
    "Insuffisance rénale chronique",
    "Diabète type 2",
    "Hypertension artérielle",
    "Goutte",
    "Hyperparathyroïdie",
    "Polykystose rénale",
    "Maladie de Crohn / RCH",
    "Aucun antécédent familial"
]

# Antécédents personnels - Cases à cocher (choix multiple)
ANTECEDENTS_PERSONNELS_OPTIONS = [
    "Lithiase rénale antérieure",
    "Hypertension artérielle",
    "Diabète type 1",
    "Diabète type 2",
    "Goutte",
    "Syndrome métabolique",
    "Obésité (IMC > 30)",
    "Infections urinaires récidivantes",
    "Reflux vésico-urétéral",
    "Hyperparathyroïdie",
    "Hyperthyroïdie",
    "Hypothyroïdie",
    "Maladie de Crohn",
    "Rectocolite hémorragique",
    "Résection intestinale",
    "Malabsorption",
    "Stéatose hépatique",
    "Cirrhose hépatique",
    "Sarcoïdose",
    "Tuberculose",
    "VIH/SIDA",
    "Aucun antécédent personnel"
]

# Antécédents chirurgicaux - Cases à cocher (choix multiple)
ANTECEDENTS_CHIRURGICAUX_OPTIONS = [
    "Lithotripsie extracorporelle (LEC)",
    "Urétéroscopie",
    "Néphrolithotomie percutanée (NLPC)",
    "Néphrectomie",
    "Résection iléale",
    "Résection iléo-caecale",
    "Colectomie",
    "Bypass gastrique",
    "Sleeve gastrectomie",
    "Cholécystectomie",
    "Appendicectomie",
    "Césarienne",
    "Cure de reflux vésico-urétéral",
    "Cure d'adénome parathyroïdien",
    "Thyroïdectomie",
    "Aucune chirurgie"
]

# Allergies connues - Cases à cocher (choix multiple)
ALLERGIES_OPTIONS = [
    "Pénicilline",
    "Céphalosporines",
    "Sulfamides",
    "Quinolones",
    "Aminosides",
    "Iode (produits de contraste)",
    "Latex",
    "Anesthésiques locaux",
    "Anti-inflammatoires (AINS)",
    "Aspirine",
    "Morphiniques",
    "Lactose",
    "Gluten",
    "Fruits de mer",
    "Arachides",
    "Aucune allergie connue"
]

# Traitements chroniques - Cases à cocher (choix multiple)
TRAITEMENTS_CHRONIQUES_OPTIONS = [
    "Antihypertenseurs (IEC/ARA2)",
    "Antihypertenseurs (Diurétiques thiazidiques)",
    "Antihypertenseurs (Inhibiteurs calciques)",
    "Antihypertenseurs (Bêta-bloquants)",
    "Antidiabétiques oraux (Metformine)",
    "Insuline",
    "Allopurinol",
    "Fébuxostat",
    "Statines",
    "Fibrates",
    "Anticoagulants (AVK)",
    "Anticoagulants (AOD)",
    "Antiagrégants plaquettaires",
    "Lévothyroxine (hypothyroïdie)",
    "Antithyroïdiens de synthèse",
    "Corticothérapie au long cours",
    "Immunosuppresseurs (Azathioprine, etc.)",
    "Suppléments de calcium",
    "Suppléments de vitamine D",
    "Suppléments de fer",
    "Citrate de potassium",
    "Bicarbonate de sodium",
    "Antibioprophylaxie (infections urinaires)",
    "Aucun traitement chronique"
]

# Habitudes - Tabac
TABAC_OPTIONS = [
    "Non-fumeur",
    "Fumeur actif (<10 cigarettes/jour)",
    "Fumeur actif (10-20 cigarettes/jour)",
    "Fumeur actif (>20 cigarettes/jour)",
    "Ancien fumeur (arrêt <1 an)",
    "Ancien fumeur (arrêt 1-5 ans)",
    "Ancien fumeur (arrêt >5 ans)"
]

# Habitudes - Alcool
ALCOOL_OPTIONS = [
    "Non-consommateur",
    "Occasionnel (<1 verre/semaine)",
    "Modéré (1-7 verres/semaine)",
    "Régulier (8-14 verres/semaine)",
    "Excessif (>14 verres/semaine)",
    "Dépendance alcoolique"
]

# Aliments courants - Petit déjeuner (Cases à cocher - choix multiple)
PETIT_DEJEUNER_OPTIONS = [
    "Café noir",
    "Café au lait",
    "Thé noir",
    "Thé vert",
    "Chocolat chaud",
    "Jus d'orange frais",
    "Jus de fruits industriels",
    "Pain blanc",
    "Pain complet",
    "Biscuits",
    "Céréales sucrées",
    "Céréales complètes",
    "Œufs",
    "Charcuterie",
    "Fromage",
    "Yaourt",
    "Beurre",
    "Margarine",
    "Confiture",
    "Miel",
    "Fruits frais",
    "Pas de petit-déjeuner"
]

# Aliments courants - Déjeuner (Cases à cocher - choix multiple)
DEJEUNER_OPTIONS = [
    "Viande rouge (bœuf, chèvre)",
    "Viande blanche (poulet)",
    "Poisson",
    "Poisson salé/fumé",
    "Abats (foie, rognons)",
    "Charcuterie",
    "Œufs",
    "Fufu (manioc)",
    "Riz blanc",
    "Riz complet",
    "Pâtes",
    "Pommes de terre",
    "Igname",
    "Patate douce",
    "Haricots/légumineuses",
    "Légumes verts (pondu, etc.)",
    "Légumes crus (salade)",
    "Sauce tomate",
    "Sauce grasse/huileuse",
    "Sauce arachide",
    "Fruits frais"
]

# Aliments courants - Dîner (Cases à cocher - choix multiple)
DINER_OPTIONS = [
    "Viande rouge",
    "Poulet/volaille",
    "Poisson frais",
    "Poisson salé/séché",
    "Chikwangue",
    "Fufu",
    "Riz",
    "Pâtes",
    "Pain",
    "Soupe de légumes",
    "Légumes verts",
    "Légumes cuits",
    "Haricots",
    "Œufs",
    "Fromage",
    "Yaourt",
    "Fruits",
    "Repas léger",
    "Pas de dîner"
]

# Grignotage et goûters (Cases à cocher - choix multiple)
GRIGNOTAGE_OPTIONS = [
    "Cacahuètes salées",
    "Noix de cajou",
    "Amandes",
    "Noix",
    "Fruits secs (dattes, figues)",
    "Chips",
    "Beignets frits",
    "Biscuits sucrés",
    "Chocolat noir",
    "Chocolat au lait",
    "Bonbons",
    "Glaces",
    "Fruits frais",
    "Bananes",
    "Compotes",
    "Barres céréales",
    "Pas de grignotage"
]

# Autres consommations (Cases à cocher - choix multiple)
AUTRES_CONSOMMATIONS_OPTIONS = [
    "Eau plate (>2L/jour)",
    "Eau plate (1-2L/jour)",
    "Eau plate (<1L/jour)",
    "Eau gazeuse",
    "Bière (1-2/jour)",
    "Bière (3-5/jour)",
    "Bière (>5/jour)",
    "Alcool fort (whisky, gin)",
    "Vin rouge",
    "Vin blanc",
    "Sodas sucrés (1-2/jour)",
    "Sodas sucrés (>3/jour)",
    "Boissons énergisantes",
    "Café (1-2 tasses/jour)",
    "Café (3-4 tasses/jour)",
    "Café (>5 tasses/jour)",
    "Thé (1-2 tasses/jour)",
    "Thé (>3 tasses/jour)",
    "Infusions de plantes",
    "Jus de fruits frais",
    "Jus de fruits industriels"
]

# ASP - Abdomen Sans Préparation (Cases à cocher - choix multiple)
ASP_OPTIONS = [
    "Calcul radio-opaque visible",
    "Calculs multiples bilatéraux",
    "Calcul unique",
    "Néphrocalcinose",
    "Calcifications vasculaires",
    "Calcifications ganglionnaires",
    "Dilatation des cavités pyélocalicielles",
    "Pas d'anomalie visible",
    "Examen non réalisé"
]

# Échographie rénale (Cases à cocher - choix multiple)
ECHOGRAPHIE_OPTIONS = [
    "Calcul(s) hyperéchogène(s) avec cône d'ombre",
    "Calculs multiples bilatéraux",
    "Calcul coralliforme",
    "Dilatation pyélocalicielle",
    "Hydronéphrose",
    "Atrophie corticale",
    "Néphrocalcinose médullaire",
    "Néphrocalcinose corticale",
    "Kyste rénal simple",
    "Polykystose rénale",
    "Masse rénale",
    "Rein de taille normale",
    "Reins augmentés de volume",
    "Reins diminués de volume",
    "Pas d'anomalie",
    "Examen non réalisé"
]

# Topographie du calcul (Cases à cocher - choix multiple)
TOPOGRAPHIE_CALCUL_OPTIONS = [
    "Calice supérieur droit",
    "Calice moyen droit",
    "Calice inférieur droit",
    "Bassinet droit",
    "Jonction pyélo-urétérale droite",
    "Uretère lombaire droit",
    "Uretère iliaque droit",
    "Uretère pelvien droit",
    "Méat urétéral droit",
    "Calice supérieur gauche",
    "Calice moyen gauche",
    "Calice inférieur gauche",
    "Bassinet gauche",
    "Jonction pyélo-urétérale gauche",
    "Uretère lombaire gauche",
    "Uretère iliaque gauche",
    "Uretère pelvien gauche",
    "Méat urétéral gauche",
    "Vessie",
    "Urètre",
    "Calcul coralliforme bilatéral",
    "Calculs multiples bilatéraux"
]

# Autres calcifications visibles (Cases à cocher - choix multiple)
CALCIFICATIONS_AUTRES_OPTIONS = [
    "Néphrocalcinose médullaire bilatérale",
    "Néphrocalcinose corticale",
    "Calcifications de la paroi aortique",
    "Calcifications artères iliaques",
    "Calcifications artères rénales",
    "Calcifications ganglionnaires",
    "Score calcique coronaire élevé",
    "Calcifications prostatiques",
    "Calcifications spléniques",
    "Calcifications pancréatiques",
    "Calcifications hépatiques",
    "Calcifications vésicule biliaire",
    "Phlébolithes pelviens",
    "Aucune calcification extra-rénale"
]

# Forme du calcul (Liste déroulante - choix unique)
FORME_CALCUL_OPTIONS = [
    "",  # Option vide par défaut
    "Arrondie",
    "Ovale",
    "Irrégulière",
    "Spiculée",
    "Coralliforme",
    "Lamellaire",
    "En rosette"
]

# Contour du calcul (Liste déroulante - choix unique)
CONTOUR_CALCUL_OPTIONS = [
    "",  # Option vide par défaut
    "Lisse",
    "Régulier",
    "Irrégulier",
    "Spiculé",
    "Lobulé",
    "Mamelonné"
]

# Morphologie du calcul (uroscanner)
MORPHOLOGIE_CALCUL_OPTIONS = [
    "",
    "spherique_lisse",
    "irreguliere_spiculee",
    "coralliforme",
    "ovale_lisse",
    "lamellaire"
]

# Radio-opacité
RADIO_OPACITE_OPTIONS = [
    "",
    "opaque",
    "transparent",
    "semi_opaque"
]

# Fonction pour convertir les listes en format JSON pour JavaScript
def get_all_options_as_dict():
    """Retourne toutes les options sous forme de dictionnaire pour JSON"""
    return {
        'antecedents_familiaux': ANTECEDENTS_FAMILIAUX_OPTIONS,
        'antecedents_personnels': ANTECEDENTS_PERSONNELS_OPTIONS,
        'antecedents_chirurgicaux': ANTECEDENTS_CHIRURGICAUX_OPTIONS,
        'allergies': ALLERGIES_OPTIONS,
        'traitements_chroniques': TRAITEMENTS_CHRONIQUES_OPTIONS,
        'tabac': TABAC_OPTIONS,
        'alcool': ALCOOL_OPTIONS,
        'petit_dejeuner': PETIT_DEJEUNER_OPTIONS,
        'dejeuner': DEJEUNER_OPTIONS,
        'diner': DINER_OPTIONS,
        'grignotage': GRIGNOTAGE_OPTIONS,
        'autres_consommations': AUTRES_CONSOMMATIONS_OPTIONS,
        'asp_resultats': ASP_OPTIONS,
        'echographie_resultats': ECHOGRAPHIE_OPTIONS,
        'topographie_calcul': TOPOGRAPHIE_CALCUL_OPTIONS,
        'calcifications_autres': CALCIFICATIONS_AUTRES_OPTIONS,
        'forme_calcul': FORME_CALCUL_OPTIONS,
        'contour_calcul': CONTOUR_CALCUL_OPTIONS,
        'morphologie': MORPHOLOGIE_CALCUL_OPTIONS,
        'radio_opacite': RADIO_OPACITE_OPTIONS
    }
