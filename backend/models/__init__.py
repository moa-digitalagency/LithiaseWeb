from backend import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from backend.utils.crypto import encryption_manager
from flask_login import UserMixin
import uuid

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), default='medecin', nullable=False)
    
    can_manage_patients = db.Column(db.Boolean, default=True)
    can_manage_episodes = db.Column(db.Boolean, default=True)
    can_export_data = db.Column(db.Boolean, default=True)
    can_manage_users = db.Column(db.Boolean, default=False)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def has_permission(self, permission):
        return getattr(self, permission, False)

class Patient(db.Model):
    __tablename__ = 'patients'
    id = db.Column(db.Integer, primary_key=True)
    code_patient = db.Column(db.String(6), unique=True, nullable=True)
    
    _nom = db.Column('nom', db.Text, nullable=False)
    _prenom = db.Column('prenom', db.Text, nullable=False)
    date_naissance = db.Column(db.Date, nullable=True)
    sexe = db.Column(db.String(1), nullable=True)
    _telephone = db.Column('telephone', db.Text)
    _email = db.Column('email', db.Text)
    _adresse = db.Column('adresse', db.Text)
    
    _antecedents_personnels = db.Column('antecedents_personnels', db.Text)
    _antecedents_familiaux = db.Column('antecedents_familiaux', db.Text)
    _antecedents_chirurgicaux = db.Column('antecedents_chirurgicaux', db.Text)
    _allergies = db.Column('allergies', db.Text)
    _traitements_chroniques = db.Column('traitements_chroniques', db.Text)
    
    hydratation_jour = db.Column(db.Float)
    regime_alimentaire = db.Column(db.String(200))
    
    poids = db.Column(db.Float)
    taille = db.Column(db.Float)
    _groupe_ethnique = db.Column('groupe_ethnique', db.Text)
    
    tension_arterielle_systolique = db.Column(db.Float)
    tension_arterielle_diastolique = db.Column(db.Float)
    frequence_cardiaque = db.Column(db.Float)
    temperature = db.Column(db.Float)
    frequence_respiratoire = db.Column(db.Float)
    
    province = db.Column(db.String(100))
    ville = db.Column(db.String(100))
    profession = db.Column(db.String(100))
    niveau_education = db.Column(db.String(50))
    statut_matrimonial = db.Column(db.String(50))
    
    _petit_dejeuner = db.Column('petit_dejeuner', db.Text)
    _dejeuner = db.Column('dejeuner', db.Text)
    _diner = db.Column('diner', db.Text)
    _grignotage = db.Column('grignotage', db.Text)
    _autres_consommations = db.Column('autres_consommations', db.Text)
    
    _asp_resultats = db.Column('asp_resultats', db.Text)
    _echographie_resultats = db.Column('echographie_resultats', db.Text)
    _uroscanner_resultats = db.Column('uroscanner_resultats', db.Text)
    
    _sediment_urinaire = db.Column('sediment_urinaire', db.Text)
    _ecbu_resultats = db.Column('ecbu_resultats', db.Text)
    ph_urinaire = db.Column(db.Float)
    densite_urinaire = db.Column(db.Float)
    
    nombre_calculs = db.Column(db.Integer)
    _topographie_calcul = db.Column('topographie_calcul', db.Text)
    diametre_longitudinal = db.Column(db.Float)
    diametre_transversal = db.Column(db.Float)
    _forme_calcul = db.Column('forme_calcul', db.Text)
    _contour_calcul = db.Column('contour_calcul', db.Text)
    densite_noyau = db.Column(db.Integer)
    _densites_couches = db.Column('densites_couches', db.Text)
    _calcifications_autres = db.Column('calcifications_autres', db.Text)
    
    fichier_imagerie = db.Column(db.String(255))
    fichier_laboratoire = db.Column(db.String(255))
    fichier_ordonnance = db.Column(db.String(255))
    
    _notes = db.Column('notes', db.Text)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    episodes = db.relationship('Episode', backref='patient', lazy=True, cascade='all, delete-orphan')
    
    @property
    def nom(self):
        return encryption_manager.decrypt(self._nom)
    
    @nom.setter
    def nom(self, value):
        self._nom = encryption_manager.encrypt(value)
    
    @property
    def prenom(self):
        return encryption_manager.decrypt(self._prenom)
    
    @prenom.setter
    def prenom(self, value):
        self._prenom = encryption_manager.encrypt(value)
    
    @property
    def telephone(self):
        return encryption_manager.decrypt(self._telephone)
    
    @telephone.setter
    def telephone(self, value):
        self._telephone = encryption_manager.encrypt(value)
    
    @property
    def email(self):
        return encryption_manager.decrypt(self._email)
    
    @email.setter
    def email(self, value):
        self._email = encryption_manager.encrypt(value)
    
    @property
    def adresse(self):
        return encryption_manager.decrypt(self._adresse)
    
    @adresse.setter
    def adresse(self, value):
        self._adresse = encryption_manager.encrypt(value)
    
    @property
    def antecedents_personnels(self):
        return encryption_manager.decrypt(self._antecedents_personnels)
    
    @antecedents_personnels.setter
    def antecedents_personnels(self, value):
        self._antecedents_personnels = encryption_manager.encrypt(value)
    
    @property
    def antecedents_familiaux(self):
        return encryption_manager.decrypt(self._antecedents_familiaux)
    
    @antecedents_familiaux.setter
    def antecedents_familiaux(self, value):
        self._antecedents_familiaux = encryption_manager.encrypt(value)
    
    @property
    def antecedents_chirurgicaux(self):
        return encryption_manager.decrypt(self._antecedents_chirurgicaux)
    
    @antecedents_chirurgicaux.setter
    def antecedents_chirurgicaux(self, value):
        self._antecedents_chirurgicaux = encryption_manager.encrypt(value)
    
    @property
    def allergies(self):
        return encryption_manager.decrypt(self._allergies)
    
    @allergies.setter
    def allergies(self, value):
        self._allergies = encryption_manager.encrypt(value)
    
    @property
    def traitements_chroniques(self):
        return encryption_manager.decrypt(self._traitements_chroniques)
    
    @traitements_chroniques.setter
    def traitements_chroniques(self, value):
        self._traitements_chroniques = encryption_manager.encrypt(value)
    
    @property
    def notes(self):
        return encryption_manager.decrypt(self._notes)
    
    @notes.setter
    def notes(self, value):
        self._notes = encryption_manager.encrypt(value)
    
    @property
    def groupe_ethnique(self):
        return encryption_manager.decrypt(self._groupe_ethnique)
    
    @groupe_ethnique.setter
    def groupe_ethnique(self, value):
        self._groupe_ethnique = encryption_manager.encrypt(value)
    
    @property
    def petit_dejeuner(self):
        return encryption_manager.decrypt(self._petit_dejeuner)
    
    @petit_dejeuner.setter
    def petit_dejeuner(self, value):
        self._petit_dejeuner = encryption_manager.encrypt(value)
    
    @property
    def dejeuner(self):
        return encryption_manager.decrypt(self._dejeuner)
    
    @dejeuner.setter
    def dejeuner(self, value):
        self._dejeuner = encryption_manager.encrypt(value)
    
    @property
    def diner(self):
        return encryption_manager.decrypt(self._diner)
    
    @diner.setter
    def diner(self, value):
        self._diner = encryption_manager.encrypt(value)
    
    @property
    def grignotage(self):
        return encryption_manager.decrypt(self._grignotage)
    
    @grignotage.setter
    def grignotage(self, value):
        self._grignotage = encryption_manager.encrypt(value)
    
    @property
    def autres_consommations(self):
        return encryption_manager.decrypt(self._autres_consommations)
    
    @autres_consommations.setter
    def autres_consommations(self, value):
        self._autres_consommations = encryption_manager.encrypt(value)
    
    @property
    def asp_resultats(self):
        return encryption_manager.decrypt(self._asp_resultats)
    
    @asp_resultats.setter
    def asp_resultats(self, value):
        self._asp_resultats = encryption_manager.encrypt(value)
    
    @property
    def echographie_resultats(self):
        return encryption_manager.decrypt(self._echographie_resultats)
    
    @echographie_resultats.setter
    def echographie_resultats(self, value):
        self._echographie_resultats = encryption_manager.encrypt(value)
    
    @property
    def uroscanner_resultats(self):
        return encryption_manager.decrypt(self._uroscanner_resultats)
    
    @uroscanner_resultats.setter
    def uroscanner_resultats(self, value):
        self._uroscanner_resultats = encryption_manager.encrypt(value)
    
    @property
    def sediment_urinaire(self):
        return encryption_manager.decrypt(self._sediment_urinaire)
    
    @sediment_urinaire.setter
    def sediment_urinaire(self, value):
        self._sediment_urinaire = encryption_manager.encrypt(value)
    
    @property
    def ecbu_resultats(self):
        return encryption_manager.decrypt(self._ecbu_resultats)
    
    @ecbu_resultats.setter
    def ecbu_resultats(self, value):
        self._ecbu_resultats = encryption_manager.encrypt(value)
    
    @property
    def topographie_calcul(self):
        return encryption_manager.decrypt(self._topographie_calcul)
    
    @topographie_calcul.setter
    def topographie_calcul(self, value):
        self._topographie_calcul = encryption_manager.encrypt(value)
    
    @property
    def forme_calcul(self):
        return encryption_manager.decrypt(self._forme_calcul)
    
    @forme_calcul.setter
    def forme_calcul(self, value):
        self._forme_calcul = encryption_manager.encrypt(value)
    
    @property
    def contour_calcul(self):
        return encryption_manager.decrypt(self._contour_calcul)
    
    @contour_calcul.setter
    def contour_calcul(self, value):
        self._contour_calcul = encryption_manager.encrypt(value)
    
    @property
    def densites_couches(self):
        return encryption_manager.decrypt(self._densites_couches)
    
    @densites_couches.setter
    def densites_couches(self, value):
        self._densites_couches = encryption_manager.encrypt(value)
    
    @property
    def calcifications_autres(self):
        return encryption_manager.decrypt(self._calcifications_autres)
    
    @calcifications_autres.setter
    def calcifications_autres(self, value):
        self._calcifications_autres = encryption_manager.encrypt(value)

class Episode(db.Model):
    __tablename__ = 'episodes'
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    
    date_episode = db.Column(db.Date, nullable=False)
    _motif = db.Column('motif', db.Text)
    _diagnostic = db.Column('diagnostic', db.Text)
    douleur = db.Column(db.Boolean, default=False)
    fievre = db.Column(db.Boolean, default=False)
    infection_urinaire = db.Column(db.Boolean, default=False)
    _germe = db.Column('germe', db.Text)
    urease_positif = db.Column(db.Boolean)
    germe_urease = db.Column(db.String(100))
    
    _lateralite = db.Column('lateralite', db.Text)
    _siege_douloureux = db.Column('siege_douloureux', db.Text)
    _symptomes_associes = db.Column('symptomes_associes', db.Text)
    
    _traitement_medical = db.Column('traitement_medical', db.Text)
    traitement_interventionnel = db.Column(db.String(100))
    date_traitement = db.Column(db.Date)
    _centre_traitement = db.Column('centre_traitement', db.Text)
    _resultat_traitement = db.Column('resultat_traitement', db.Text)
    
    _notes = db.Column('notes', db.Text)
    
    calculated_stone_type = db.Column(db.String(100))
    calculated_stone_type_data = db.Column(db.Text)
    calculated_at = db.Column(db.DateTime)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    imageries = db.relationship('Imagerie', backref='episode', lazy=True, cascade='all, delete-orphan')
    biologies = db.relationship('Biologie', backref='episode', lazy=True, cascade='all, delete-orphan')
    
    @property
    def motif(self):
        return encryption_manager.decrypt(self._motif)
    
    @motif.setter
    def motif(self, value):
        self._motif = encryption_manager.encrypt(value)
    
    @property
    def diagnostic(self):
        return encryption_manager.decrypt(self._diagnostic)
    
    @diagnostic.setter
    def diagnostic(self, value):
        self._diagnostic = encryption_manager.encrypt(value)
    
    @property
    def germe(self):
        return encryption_manager.decrypt(self._germe)
    
    @germe.setter
    def germe(self, value):
        self._germe = encryption_manager.encrypt(value)
    
    @property
    def lateralite(self):
        return encryption_manager.decrypt(self._lateralite)
    
    @lateralite.setter
    def lateralite(self, value):
        self._lateralite = encryption_manager.encrypt(value)
    
    @property
    def siege_douloureux(self):
        return encryption_manager.decrypt(self._siege_douloureux)
    
    @siege_douloureux.setter
    def siege_douloureux(self, value):
        self._siege_douloureux = encryption_manager.encrypt(value)
    
    @property
    def symptomes_associes(self):
        return encryption_manager.decrypt(self._symptomes_associes)
    
    @symptomes_associes.setter
    def symptomes_associes(self, value):
        self._symptomes_associes = encryption_manager.encrypt(value)
    
    @property
    def traitement_medical(self):
        return encryption_manager.decrypt(self._traitement_medical)
    
    @traitement_medical.setter
    def traitement_medical(self, value):
        self._traitement_medical = encryption_manager.encrypt(value)
    
    @property
    def centre_traitement(self):
        return encryption_manager.decrypt(self._centre_traitement)
    
    @centre_traitement.setter
    def centre_traitement(self, value):
        self._centre_traitement = encryption_manager.encrypt(value)
    
    @property
    def resultat_traitement(self):
        return encryption_manager.decrypt(self._resultat_traitement)
    
    @resultat_traitement.setter
    def resultat_traitement(self, value):
        self._resultat_traitement = encryption_manager.encrypt(value)
    
    @property
    def notes(self):
        return encryption_manager.decrypt(self._notes)
    
    @notes.setter
    def notes(self, value):
        self._notes = encryption_manager.encrypt(value)

class Imagerie(db.Model):
    __tablename__ = 'imageries'
    id = db.Column(db.Integer, primary_key=True)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)
    
    date_examen = db.Column(db.Date, nullable=False)
    taille_mm = db.Column(db.Integer)
    densite_uh = db.Column(db.Integer)
    densite_ecart_type = db.Column(db.Integer)
    
    morphologie = db.Column(db.String(50))
    radio_opacite = db.Column(db.String(20))
    localisation = db.Column(db.String(100))
    nombre = db.Column(db.String(20))
    nombre_estime = db.Column(db.Integer)
    
    _asp_resultats = db.Column('asp_resultats', db.Text)
    _echographie_resultats = db.Column('echographie_resultats', db.Text)
    _uroscanner_resultats = db.Column('uroscanner_resultats', db.Text)
    
    nombre_calculs = db.Column(db.Integer)
    _situation_calcul = db.Column('situation_calcul', db.Text)
    _topographie_calcul = db.Column('topographie_calcul', db.Text)
    diametre_longitudinal = db.Column(db.Float)
    diametre_transversal = db.Column(db.Float)
    _forme_calcul = db.Column('forme_calcul', db.Text)
    _contour_calcul = db.Column('contour_calcul', db.Text)
    densite_noyau = db.Column(db.Integer)
    _densites_couches = db.Column('densites_couches', db.Text)
    _calcifications_autres = db.Column('calcifications_autres', db.Text)
    
    rein_gauche_cranio_caudal = db.Column(db.Float)
    rein_gauche_antero_posterieur = db.Column(db.Float)
    rein_gauche_transversal = db.Column(db.Float)
    rein_gauche_volume = db.Column(db.Float)
    
    rein_droit_cranio_caudal = db.Column(db.Float)
    rein_droit_antero_posterieur = db.Column(db.Float)
    rein_droit_transversal = db.Column(db.Float)
    rein_droit_volume = db.Column(db.Float)
    
    epaisseur_cortex_renal_gauche = db.Column(db.Float)
    epaisseur_cortex_renal_droit = db.Column(db.Float)
    diametre_pyelon_gauche = db.Column(db.Float)
    diametre_pyelon_droit = db.Column(db.Float)
    diametre_uretere_amont_gauche = db.Column(db.Float)
    diametre_uretere_amont_droit = db.Column(db.Float)
    _malformations_urinaires = db.Column('malformations_urinaires', db.Text)
    
    _commentaires = db.Column('commentaires', db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    @property
    def commentaires(self):
        return encryption_manager.decrypt(self._commentaires)
    
    @commentaires.setter
    def commentaires(self, value):
        self._commentaires = encryption_manager.encrypt(value)
    
    @property
    def asp_resultats(self):
        return encryption_manager.decrypt(self._asp_resultats)
    
    @asp_resultats.setter
    def asp_resultats(self, value):
        self._asp_resultats = encryption_manager.encrypt(value)
    
    @property
    def echographie_resultats(self):
        return encryption_manager.decrypt(self._echographie_resultats)
    
    @echographie_resultats.setter
    def echographie_resultats(self, value):
        self._echographie_resultats = encryption_manager.encrypt(value)
    
    @property
    def uroscanner_resultats(self):
        return encryption_manager.decrypt(self._uroscanner_resultats)
    
    @uroscanner_resultats.setter
    def uroscanner_resultats(self, value):
        self._uroscanner_resultats = encryption_manager.encrypt(value)
    
    @property
    def situation_calcul(self):
        return encryption_manager.decrypt(self._situation_calcul)
    
    @situation_calcul.setter
    def situation_calcul(self, value):
        self._situation_calcul = encryption_manager.encrypt(value)
    
    @property
    def topographie_calcul(self):
        return encryption_manager.decrypt(self._topographie_calcul)
    
    @topographie_calcul.setter
    def topographie_calcul(self, value):
        self._topographie_calcul = encryption_manager.encrypt(value)
    
    @property
    def forme_calcul(self):
        return encryption_manager.decrypt(self._forme_calcul)
    
    @forme_calcul.setter
    def forme_calcul(self, value):
        self._forme_calcul = encryption_manager.encrypt(value)
    
    @property
    def contour_calcul(self):
        return encryption_manager.decrypt(self._contour_calcul)
    
    @contour_calcul.setter
    def contour_calcul(self, value):
        self._contour_calcul = encryption_manager.encrypt(value)
    
    @property
    def densites_couches(self):
        return encryption_manager.decrypt(self._densites_couches)
    
    @densites_couches.setter
    def densites_couches(self, value):
        self._densites_couches = encryption_manager.encrypt(value)
    
    @property
    def calcifications_autres(self):
        return encryption_manager.decrypt(self._calcifications_autres)
    
    @calcifications_autres.setter
    def calcifications_autres(self, value):
        self._calcifications_autres = encryption_manager.encrypt(value)
    
    @property
    def malformations_urinaires(self):
        return encryption_manager.decrypt(self._malformations_urinaires)
    
    @malformations_urinaires.setter
    def malformations_urinaires(self, value):
        self._malformations_urinaires = encryption_manager.encrypt(value)

class Biologie(db.Model):
    __tablename__ = 'biologies'
    id = db.Column(db.Integer, primary_key=True)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)
    
    date_examen = db.Column(db.Date, nullable=False)
    ph_urinaire = db.Column(db.Float)
    densite_urinaire = db.Column(db.Float)
    
    _sediment_urinaire = db.Column('sediment_urinaire', db.Text)
    _ecbu_resultats = db.Column('ecbu_resultats', db.Text)
    
    hyperoxalurie = db.Column(db.Boolean, default=False)
    hypercalciurie = db.Column(db.Boolean, default=False)
    hyperuricurie = db.Column(db.Boolean, default=False)
    cystinurie = db.Column(db.Boolean, default=False)
    hypercalcemie = db.Column(db.Boolean, default=False)
    
    oxalurie_valeur = db.Column(db.Float)
    calciurie_valeur = db.Column(db.Float)
    uricurie_valeur = db.Column(db.Float)
    calciemie_valeur = db.Column(db.Float)
    
    t3 = db.Column(db.Float)
    t4 = db.Column(db.Float)
    tsh = db.Column(db.Float)
    
    uree = db.Column(db.Float)
    creatinine = db.Column(db.Float)
    _autres_parametres = db.Column('autres_parametres', db.Text)
    
    infection_urinaire = db.Column(db.Boolean, default=False)
    _germe = db.Column('germe', db.Text)
    urease_positif = db.Column(db.Boolean)
    germe_urease = db.Column(db.String(100))
    
    _commentaires = db.Column('commentaires', db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    @property
    def germe(self):
        return encryption_manager.decrypt(self._germe)
    
    @germe.setter
    def germe(self, value):
        self._germe = encryption_manager.encrypt(value)
    
    @property
    def sediment_urinaire(self):
        return encryption_manager.decrypt(self._sediment_urinaire)
    
    @sediment_urinaire.setter
    def sediment_urinaire(self, value):
        self._sediment_urinaire = encryption_manager.encrypt(value)
    
    @property
    def ecbu_resultats(self):
        return encryption_manager.decrypt(self._ecbu_resultats)
    
    @ecbu_resultats.setter
    def ecbu_resultats(self, value):
        self._ecbu_resultats = encryption_manager.encrypt(value)
    
    @property
    def commentaires(self):
        return encryption_manager.decrypt(self._commentaires)
    
    @commentaires.setter
    def commentaires(self, value):
        self._commentaires = encryption_manager.encrypt(value)
    
    @property
    def autres_parametres(self):
        return encryption_manager.decrypt(self._autres_parametres)
    
    @autres_parametres.setter
    def autres_parametres(self, value):
        self._autres_parametres = encryption_manager.encrypt(value)

class Document(db.Model):
    __tablename__ = 'documents'
    id = db.Column(db.Integer, primary_key=True)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)
    
    nom_fichier = db.Column(db.String(255), nullable=False)
    chemin_fichier = db.Column(db.String(500), nullable=False)
    type_document = db.Column(db.String(50))
    _description = db.Column('description', db.Text)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    episode = db.relationship('Episode', backref='documents')
    
    @property
    def description(self):
        return encryption_manager.decrypt(self._description)
    
    @description.setter
    def description(self, value):
        self._description = encryption_manager.encrypt(value)
