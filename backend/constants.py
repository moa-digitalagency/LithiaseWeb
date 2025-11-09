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

GERMES_UREASE_CHOICES = [
    ('Aucun', 'Aucun'),
    ('Proteus mirabilis', 'Proteus mirabilis (uréase +)'),
    ('Proteus vulgaris', 'Proteus vulgaris (uréase +)'),
    ('Klebsiella pneumoniae', 'Klebsiella pneumoniae (uréase +)'),
    ('Pseudomonas aeruginosa', 'Pseudomonas aeruginosa (uréase +)'),
    ('Staphylococcus saprophyticus', 'Staphylococcus saprophyticus (uréase +)'),
    ('Ureaplasma urealyticum', 'Ureaplasma urealyticum (uréase +)'),
    ('Morganella morganii', 'Morganella morganii (uréase +)'),
    ('Providencia rettgeri', 'Providencia rettgeri (uréase +)'),
    ('Autre germe urease+', 'Autre germe à uréase')
]

MALFORMATIONS_CHOICES = [
    ('Aucune', 'Aucune'),
    ('Stenose JPU', 'Sténose de la jonction pyélo-urétérale (JPU)'),
    ('Syndrome JUV', 'Syndrome de la jonction urétéro-vésicale'),
    ('Megauretere', 'Mégauretère'),
    ('Reflux vesico-ureteral', 'Reflux vésico-urétéral'),
    ('Rein fer cheval', 'Rein en fer à cheval'),
    ('Ectopie renale', 'Ectopie rénale'),
    ('Duplicite ureterale', 'Duplicité urétérale'),
    ('Ureterocele', 'Urétérocèle'),
    ('Valve uretre posterieur', 'Valve de l\'urètre postérieur'),
    ('Diverticule caliciel', 'Diverticule caliciel'),
    ('Kyste renal', 'Kyste rénal'),
    ('Polykystose renale', 'Polykystose rénale'),
    ('Autre malformation', 'Autre malformation')
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
    ('Luba', 'Luba'),
    ('Mongo', 'Mongo'),
    ('Kongo', 'Kongo'),
    ('Azande', 'Azande'),
    ('Bangi', 'Bangi et Ngale'),
    ('Rundi', 'Rundi'),
    ('Teke', 'Teke'),
    ('Boa', 'Boa'),
    ('Chokwe', 'Chokwe'),
    ('Lugbara', 'Lugbara'),
    ('Banda', 'Banda'),
    ('Ngombe', 'Ngombe'),
    ('Ngbandi', 'Ngbandi'),
    ('Ngbaka', 'Ngbaka'),
    ('Mbuun', 'Mbuun'),
    ('Yansi', 'Yansi'),
    ('Tetela', 'Tetela'),
    ('Kuba', 'Kuba'),
    ('Lunda', 'Lunda'),
    ('Songe', 'Songe'),
    ('Bembe', 'Bembe'),
    ('Shi', 'Shi'),
    ('Hunde', 'Hunde'),
    ('Nande', 'Nande'),
    ('Nyanga', 'Nyanga'),
    ('Hemba', 'Hemba'),
    ('Tabwa', 'Tabwa'),
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

PROVINCE_CHOICES = [
    ('Kinshasa', 'Kinshasa'),
    ('Kongo-Central', 'Kongo-Central'),
    ('Kwango', 'Kwango'),
    ('Kwilu', 'Kwilu'),
    ('Mai-Ndombe', 'Mai-Ndombe'),
    ('Kasai', 'Kasaï'),
    ('Kasai-Central', 'Kasaï-Central'),
    ('Kasai-Oriental', 'Kasaï-Oriental'),
    ('Lomami', 'Lomami'),
    ('Sankuru', 'Sankuru'),
    ('Maniema', 'Maniema'),
    ('Sud-Kivu', 'Sud-Kivu'),
    ('Nord-Kivu', 'Nord-Kivu'),
    ('Ituri', 'Ituri'),
    ('Haut-Uele', 'Haut-Uélé'),
    ('Tshopo', 'Tshopo'),
    ('Bas-Uele', 'Bas-Uélé'),
    ('Nord-Ubangi', 'Nord-Ubangi'),
    ('Sud-Ubangi', 'Sud-Ubangi'),
    ('Mongala', 'Mongala'),
    ('Equateur', 'Équateur'),
    ('Tshuapa', 'Tshuapa'),
    ('Tanganyika', 'Tanganyika'),
    ('Haut-Lomami', 'Haut-Lomami'),
    ('Lualaba', 'Lualaba'),
    ('Haut-Katanga', 'Haut-Katanga'),
    ('Autre', 'Autre')
]

VILLE_CHOICES = [
    ('Kinshasa', 'Kinshasa'),
    ('Lubumbashi', 'Lubumbashi'),
    ('Mbuji-Mayi', 'Mbuji-Mayi'),
    ('Kananga', 'Kananga'),
    ('Kisangani', 'Kisangani'),
    ('Goma', 'Goma'),
    ('Bukavu', 'Bukavu'),
    ('Likasi', 'Likasi'),
    ('Kolwezi', 'Kolwezi'),
    ('Tshikapa', 'Tshikapa'),
    ('Kikwit', 'Kikwit'),
    ('Mbandaka', 'Mbandaka'),
    ('Matadi', 'Matadi'),
    ('Bunia', 'Bunia'),
    ('Uvira', 'Uvira'),
    ('Beni', 'Beni'),
    ('Butembo', 'Butembo'),
    ('Kalemie', 'Kalemie'),
    ('Isiro', 'Isiro'),
    ('Bandundu', 'Bandundu'),
    ('Gemena', 'Gemena'),
    ('Kindu', 'Kindu'),
    ('Kamina', 'Kamina'),
    ('Boma', 'Boma'),
    ('Autre', 'Autre')
]

PROFESSION_CHOICES = [
    ('Agriculteur', 'Agriculteur'),
    ('Commercant', 'Commerçant'),
    ('Enseignant', 'Enseignant'),
    ('Fonctionnaire', 'Fonctionnaire'),
    ('Medecin', 'Médecin'),
    ('Infirmier', 'Infirmier'),
    ('Ingenieur', 'Ingénieur'),
    ('Chauffeur', 'Chauffeur'),
    ('Artisan', 'Artisan'),
    ('Etudiant', 'Étudiant'),
    ('Militaire', 'Militaire'),
    ('Policier', 'Policier'),
    ('Mineur', 'Mineur'),
    ('Ouvrier', 'Ouvrier'),
    ('Menagere', 'Ménagère'),
    ('Retraite', 'Retraité'),
    ('Chomeur', 'Chômeur'),
    ('Travailleur independant', 'Travailleur indépendant'),
    ('Autre', 'Autre'),
    ('Non precise', 'Non précisé')
]

NIVEAU_EDUCATION_CHOICES = [
    ('Aucun', 'Aucun'),
    ('Primaire', 'Primaire'),
    ('Secondaire', 'Secondaire'),
    ('Superieur', 'Supérieur'),
    ('Universitaire', 'Universitaire'),
    ('Non precise', 'Non précisé')
]

STATUT_MATRIMONIAL_CHOICES = [
    ('Celibataire', 'Célibataire'),
    ('Marie', 'Marié(e)'),
    ('Divorce', 'Divorcé(e)'),
    ('Veuf', 'Veuf/Veuve'),
    ('Union libre', 'Union libre'),
    ('Non precise', 'Non précisé')
]

ANTECEDENTS_MEDICAUX_CHOICES = [
    ('Hypertension', 'Hypertension'),
    ('Diabete', 'Diabète'),
    ('Obesite', 'Obésité'),
    ('Goutte', 'Goutte'),
    ('Hyperparathyroidie', 'Hyperparathyroïdie'),
    ('Maladie inflammatoire intestinale', 'Maladie inflammatoire intestinale'),
    ('Infection urinaire recurrente', 'Infection urinaire récurrente'),
    ('Malformation renale', 'Malformation rénale'),
    ('Chirurgie digestive', 'Chirurgie digestive'),
    ('Autre', 'Autre'),
    ('Aucun', 'Aucun')
]

# Constantes additionnelles pour l'algorithme d'inférence
# Justification: Le niveau d'activité physique influence le métabolisme calcique et le risque lithiasique

ACTIVITE_PHYSIQUE_CHOICES = [
    ('Sedentaire', 'Sédentaire (< 30 min/semaine)'),
    ('Legere', 'Légère (30 min à 2h/semaine)'),
    ('Moderee', 'Modérée (2-4h/semaine)'),
    ('Active', 'Active (4-7h/semaine)'),
    ('Tres active', 'Très active (> 7h/semaine)')
]

# Justification: Les habitudes de consommation de sel influencent la calciurie et la natriurie

CONSOMMATION_SEL_CHOICES = [
    ('Faible', 'Faible (< 5g/jour)'),
    ('Normale', 'Normale (5-10g/jour)'),
    ('Elevee', 'Élevée (> 10g/jour)'),
    ('Non precise', 'Non précisé')
]

# Justification: La consommation de protéines animales augmente l'excrétion d'acide urique et de calcium

CONSOMMATION_PROTEINES_CHOICES = [
    ('Faible', 'Faible (< 0.8g/kg/jour)'),
    ('Normale', 'Normale (0.8-1.2g/kg/jour)'),
    ('Elevee', 'Élevée (> 1.2g/kg/jour)'),
    ('Non precise', 'Non précisé')
]

# Justification: Le statut IMC corrèle avec le risque lithiasique (syndrome métabolique)

CATEGORIE_IMC_CHOICES = [
    ('Insuffisance ponderale', 'Insuffisance pondérale (< 18.5)'),
    ('Poids normal', 'Poids normal (18.5-24.9)'),
    ('Surpoids', 'Surpoids (25-29.9)'),
    ('Obesite classe I', 'Obésité classe I (30-34.9)'),
    ('Obesite classe II', 'Obésité classe II (35-39.9)'),
    ('Obesite classe III', 'Obésité classe III (≥ 40)')
]

# Justification: L'exposition professionnelle à la chaleur augmente le risque de déshydratation

EXPOSITION_CHALEUR_CHOICES = [
    ('Aucune', 'Aucune'),
    ('Occasionnelle', 'Occasionnelle'),
    ('Reguliere', 'Régulière (travail extérieur)'),
    ('Intensive', 'Intensive (four, fonderie, etc.)')
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
