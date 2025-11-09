SEXE_CHOICES = [
    ('M', 'Masculin'),
    ('F', 'Féminin')
]

LATERALITE_CHOICES = [
    ('Gauche', 'Gauche'),
    ('Droite', 'Droite'),
    ('Bilateral', 'Bilatéral')
]

FORME_CALCUL_CHOICES = [
    ('Arrondie', 'Arrondie'),
    ('Ovale', 'Ovale'),
    ('Irreguliere', 'Irrégulière'),
    ('Coralliforme', 'Coralliforme'),
    ('Spiculee', 'Spiculée')
]

CONTOUR_CALCUL_CHOICES = [
    ('Lisse', 'Lisse'),
    ('Irregulier', 'Irrégulier'),
    ('Spicule', 'Spiculé')
]

TOPOGRAPHIE_CALCUL_CHOICES = [
    ('Rein droit', 'Rein droit'),
    ('Rein gauche', 'Rein gauche'),
    ('Uretère droit', 'Uretère droit'),
    ('Uretère gauche', 'Uretère gauche'),
    ('Vessie', 'Vessie'),
    ('Urètre', 'Urètre')
]

MORPHOLOGIE_CHOICES = [
    ('spherique_lisse', 'Sphérique lisse'),
    ('irreguliere_spiculee', 'Irrégulière spiculée'),
    ('coralliforme', 'Coralliforme'),
    ('crayeuse', 'Crayeuse'),
    ('heterogene', 'Hétérogène')
]

RADIO_OPACITE_CHOICES = [
    ('opaque', 'Opaque'),
    ('transparent', 'Transparent'),
    ('inconnu', 'Inconnu')
]

GERME_CHOICES = [
    ('E. coli', 'E. coli'),
    ('Proteus mirabilis', 'Proteus mirabilis'),
    ('Klebsiella', 'Klebsiella'),
    ('Pseudomonas', 'Pseudomonas'),
    ('Enterococcus', 'Enterococcus'),
    ('Staphylococcus', 'Staphylococcus'),
    ('Autre', 'Autre'),
    ('Culture negative', 'Culture négative')
]

REGIME_ALIMENTAIRE_CHOICES = [
    ('Omnivore', 'Omnivore'),
    ('Vegetarien', 'Végétarien'),
    ('Vegan', 'Vegan'),
    ('Hyperproteine', 'Hyperprotéiné'),
    ('Pauvre en sel', 'Pauvre en sel'),
    ('Autre', 'Autre')
]

GROUPE_ETHNIQUE_CHOICES = [
    ('Caucasien', 'Caucasien'),
    ('Africain', 'Africain'),
    ('Asiatique', 'Asiatique'),
    ('Maghrebin', 'Maghrébin'),
    ('Autre', 'Autre'),
    ('Non precise', 'Non précisé')
]

HYDRATATION_CHOICES = [
    ('Moins de 1L', 'Moins de 1L'),
    ('1 a 1.5L', '1 à 1,5L'),
    ('1.5 a 2L', '1,5 à 2L'),
    ('2 a 3L', '2 à 3L'),
    ('Plus de 3L', 'Plus de 3L')
]

TYPE_CALCUL_CHOICES = [
    ('Whewellite', 'Whewellite (oxalate de calcium monohydraté)'),
    ('Weddellite', 'Weddellite (oxalate de calcium dihydraté)'),
    ('Carbapatite', 'Carbapatite (phosphate de calcium)'),
    ('Brushite', 'Brushite (phosphate de calcium hydraté)'),
    ('Struvite', 'Struvite (phosphate ammoniaco-magnésien)'),
    ('Cystine', 'Cystine'),
    ('Acide urique', 'Acide urique'),
    ('Urate ammonium', 'Urate d\'ammonium')
]

COMPOSITION_TYPE_CHOICES = [
    ('Pur', 'Pur'),
    ('Mixte', 'Mixte')
]

VOIE_TRAITEMENT_CHOICES = [
    ('Traitement medical', 'Traitement médical'),
    ('Surveillance', 'Surveillance'),
    ('LEC', 'LEC (Lithotritie extracorporelle)'),
    ('URS', 'URS (Urétéroscopie)'),
    ('PCNL', 'PCNL (Néphrolithotomie percutanée)'),
    ('Chirurgie ouverte', 'Chirurgie ouverte')
]

def get_choice_label(choices, value):
    for choice_value, choice_label in choices:
        if choice_value == value:
            return choice_label
    return value

def get_choice_values(choices):
    return [choice[0] for choice in choices]

def get_choice_dict(choices):
    return dict(choices)
