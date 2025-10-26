from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
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
    nom = db.Column(db.String(100), nullable=False)
    prenom = db.Column(db.String(100), nullable=False)
    date_naissance = db.Column(db.Date, nullable=False)
    sexe = db.Column(db.String(1), nullable=False)
    telephone = db.Column(db.String(20))
    email = db.Column(db.String(100))
    adresse = db.Column(db.Text)
    
    antecedents_personnels = db.Column(db.Text)
    antecedents_familiaux = db.Column(db.Text)
    antecedents_chirurgicaux = db.Column(db.Text)
    allergies = db.Column(db.Text)
    traitements_chroniques = db.Column(db.Text)
    
    hydratation_jour = db.Column(db.Float)
    regime_alimentaire = db.Column(db.String(200))
    notes = db.Column(db.Text)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    episodes = db.relationship('Episode', backref='patient', lazy=True, cascade='all, delete-orphan')

class Episode(db.Model):
    __tablename__ = 'episodes'
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    
    date_episode = db.Column(db.Date, nullable=False)
    motif = db.Column(db.String(200))
    diagnostic = db.Column(db.String(200))
    douleur = db.Column(db.Boolean, default=False)
    fievre = db.Column(db.Boolean, default=False)
    infection_urinaire = db.Column(db.Boolean, default=False)
    germe = db.Column(db.String(100))
    urease_positif = db.Column(db.Boolean)
    
    lateralite = db.Column(db.String(50))
    siege_douloureux = db.Column(db.String(100))
    symptomes_associes = db.Column(db.Text)
    
    traitement_medical = db.Column(db.Text)
    traitement_interventionnel = db.Column(db.String(100))
    date_traitement = db.Column(db.Date)
    centre_traitement = db.Column(db.String(200))
    resultat_traitement = db.Column(db.Text)
    
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    imageries = db.relationship('Imagerie', backref='episode', lazy=True, cascade='all, delete-orphan')
    biologies = db.relationship('Biologie', backref='episode', lazy=True, cascade='all, delete-orphan')

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
    
    commentaires = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

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
    germe = db.Column(db.String(100))
    urease_positif = db.Column(db.Boolean)
    
    commentaires = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Document(db.Model):
    __tablename__ = 'documents'
    id = db.Column(db.Integer, primary_key=True)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)
    
    nom_fichier = db.Column(db.String(255), nullable=False)
    chemin_fichier = db.Column(db.String(500), nullable=False)
    type_document = db.Column(db.String(50))
    description = db.Column(db.Text)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    episode = db.relationship('Episode', backref='documents')
