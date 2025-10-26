from backend import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from backend.utils.crypto import encryption_manager
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Patient(db.Model):
    __tablename__ = 'patients'
    id = db.Column(db.Integer, primary_key=True)
    
    _nom = db.Column('nom', db.Text, nullable=False)
    _prenom = db.Column('prenom', db.Text, nullable=False)
    date_naissance = db.Column(db.Date, nullable=False)
    sexe = db.Column(db.String(1), nullable=False)
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
    
    _lateralite = db.Column('lateralite', db.Text)
    _siege_douloureux = db.Column('siege_douloureux', db.Text)
    _symptomes_associes = db.Column('symptomes_associes', db.Text)
    
    _traitement_medical = db.Column('traitement_medical', db.Text)
    traitement_interventionnel = db.Column(db.String(100))
    date_traitement = db.Column(db.Date)
    _centre_traitement = db.Column('centre_traitement', db.Text)
    _resultat_traitement = db.Column('resultat_traitement', db.Text)
    
    _notes = db.Column('notes', db.Text)
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
    
    _commentaires = db.Column('commentaires', db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    @property
    def commentaires(self):
        return encryption_manager.decrypt(self._commentaires)
    
    @commentaires.setter
    def commentaires(self, value):
        self._commentaires = encryption_manager.encrypt(value)

class Biologie(db.Model):
    __tablename__ = 'biologies'
    id = db.Column(db.Integer, primary_key=True)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)
    
    date_examen = db.Column(db.Date, nullable=False)
    ph_urinaire = db.Column(db.Float)
    
    hyperoxalurie = db.Column(db.Boolean, default=False)
    hypercalciurie = db.Column(db.Boolean, default=False)
    hyperuricurie = db.Column(db.Boolean, default=False)
    cystinurie = db.Column(db.Boolean, default=False)
    
    oxalurie_valeur = db.Column(db.Float)
    calciurie_valeur = db.Column(db.Float)
    uricurie_valeur = db.Column(db.Float)
    
    infection_urinaire = db.Column(db.Boolean, default=False)
    _germe = db.Column('germe', db.Text)
    urease_positif = db.Column(db.Boolean)
    
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
    def commentaires(self):
        return encryption_manager.decrypt(self._commentaires)
    
    @commentaires.setter
    def commentaires(self, value):
        self._commentaires = encryption_manager.encrypt(value)

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
