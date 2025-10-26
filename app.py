from flask import Flask, render_template, request, jsonify, redirect, url_for, session, send_file
from models import db, User, Patient, Episode, Imagerie, Biologie, Document
from inference import InferenceEngine
from datetime import datetime, date
import os
import csv
import io
from werkzeug.utils import secure_filename
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'lithiase-secret-key-change-in-production'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lithiase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

db.init_app(app)

ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
@login_required
def index():
    return render_template('dashboard.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.json
        user = User.query.filter_by(username=data['username']).first()
        
        if user and user.check_password(data['password']):
            session['user_id'] = user.id
            session['username'] = user.username
            return jsonify({'success': True})
        else:
            return jsonify({'success': False, 'message': 'Identifiants incorrects'}), 401
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/api/patients', methods=['GET', 'POST'])
@login_required
def patients():
    if request.method == 'POST':
        data = request.json
        
        try:
            date_naissance = datetime.strptime(data['date_naissance'], '%Y-%m-%d').date()
        except:
            return jsonify({'error': 'Date de naissance invalide'}), 400
        
        patient = Patient(
            nom=data['nom'],
            prenom=data['prenom'],
            date_naissance=date_naissance,
            sexe=data['sexe'],
            telephone=data.get('telephone'),
            email=data.get('email'),
            adresse=data.get('adresse'),
            antecedents_personnels=data.get('antecedents_personnels'),
            antecedents_familiaux=data.get('antecedents_familiaux'),
            antecedents_chirurgicaux=data.get('antecedents_chirurgicaux'),
            allergies=data.get('allergies'),
            traitements_chroniques=data.get('traitements_chroniques'),
            hydratation_jour=data.get('hydratation_jour'),
            regime_alimentaire=data.get('regime_alimentaire'),
            notes=data.get('notes')
        )
        
        db.session.add(patient)
        db.session.commit()
        
        return jsonify({'id': patient.id, 'message': 'Patient créé avec succès'}), 201
    
    else:
        search = request.args.get('search', '')
        if search:
            patients = Patient.query.filter(
                (Patient.nom.contains(search)) | 
                (Patient.prenom.contains(search)) |
                (Patient.telephone.contains(search))
            ).all()
        else:
            patients = Patient.query.all()
        
        return jsonify([{
            'id': p.id,
            'nom': p.nom,
            'prenom': p.prenom,
            'date_naissance': p.date_naissance.isoformat(),
            'sexe': p.sexe,
            'telephone': p.telephone,
            'email': p.email,
            'nb_episodes': len(p.episodes)
        } for p in patients])

@app.route('/api/patients/<int:patient_id>', methods=['GET', 'PUT', 'DELETE'])
@login_required
def patient_detail(patient_id):
    patient = Patient.query.get_or_404(patient_id)
    
    if request.method == 'GET':
        return jsonify({
            'id': patient.id,
            'nom': patient.nom,
            'prenom': patient.prenom,
            'date_naissance': patient.date_naissance.isoformat(),
            'sexe': patient.sexe,
            'telephone': patient.telephone,
            'email': patient.email,
            'adresse': patient.adresse,
            'antecedents_personnels': patient.antecedents_personnels,
            'antecedents_familiaux': patient.antecedents_familiaux,
            'antecedents_chirurgicaux': patient.antecedents_chirurgicaux,
            'allergies': patient.allergies,
            'traitements_chroniques': patient.traitements_chroniques,
            'hydratation_jour': patient.hydratation_jour,
            'regime_alimentaire': patient.regime_alimentaire,
            'notes': patient.notes,
            'episodes': [{
                'id': e.id,
                'date_episode': e.date_episode.isoformat(),
                'motif': e.motif,
                'diagnostic': e.diagnostic
            } for e in patient.episodes]
        })
    
    elif request.method == 'PUT':
        data = request.json
        
        if 'date_naissance' in data:
            try:
                patient.date_naissance = datetime.strptime(data['date_naissance'], '%Y-%m-%d').date()
            except:
                return jsonify({'error': 'Date de naissance invalide'}), 400
        
        for field in ['nom', 'prenom', 'sexe', 'telephone', 'email', 'adresse',
                     'antecedents_personnels', 'antecedents_familiaux', 'antecedents_chirurgicaux',
                     'allergies', 'traitements_chroniques', 'hydratation_jour', 'regime_alimentaire', 'notes']:
            if field in data:
                setattr(patient, field, data[field])
        
        db.session.commit()
        return jsonify({'message': 'Patient mis à jour avec succès'})
    
    elif request.method == 'DELETE':
        db.session.delete(patient)
        db.session.commit()
        return jsonify({'message': 'Patient supprimé avec succès'})

@app.route('/api/patients/<int:patient_id>/episodes', methods=['GET', 'POST'])
@login_required
def episodes(patient_id):
    patient = Patient.query.get_or_404(patient_id)
    
    if request.method == 'POST':
        data = request.json
        
        try:
            date_episode = datetime.strptime(data['date_episode'], '%Y-%m-%d').date()
        except:
            return jsonify({'error': 'Date d\'épisode invalide'}), 400
        
        episode = Episode(
            patient_id=patient_id,
            date_episode=date_episode,
            motif=data.get('motif'),
            diagnostic=data.get('diagnostic'),
            douleur=data.get('douleur', False),
            fievre=data.get('fievre', False),
            infection_urinaire=data.get('infection_urinaire', False),
            germe=data.get('germe'),
            urease_positif=data.get('urease_positif'),
            lateralite=data.get('lateralite'),
            siege_douloureux=data.get('siege_douloureux'),
            symptomes_associes=data.get('symptomes_associes'),
            traitement_medical=data.get('traitement_medical'),
            traitement_interventionnel=data.get('traitement_interventionnel'),
            notes=data.get('notes')
        )
        
        if data.get('date_traitement'):
            try:
                episode.date_traitement = datetime.strptime(data['date_traitement'], '%Y-%m-%d').date()
            except:
                pass
        
        db.session.add(episode)
        db.session.commit()
        
        return jsonify({'id': episode.id, 'message': 'Épisode créé avec succès'}), 201
    
    else:
        return jsonify([{
            'id': e.id,
            'date_episode': e.date_episode.isoformat(),
            'motif': e.motif,
            'diagnostic': e.diagnostic,
            'douleur': e.douleur,
            'fievre': e.fievre,
            'infection_urinaire': e.infection_urinaire,
            'nb_imageries': len(e.imageries),
            'nb_biologies': len(e.biologies)
        } for e in patient.episodes])

@app.route('/api/episodes/<int:episode_id>', methods=['GET', 'PUT', 'DELETE'])
@login_required
def episode_detail(episode_id):
    episode = Episode.query.get_or_404(episode_id)
    
    if request.method == 'GET':
        return jsonify({
            'id': episode.id,
            'patient_id': episode.patient_id,
            'date_episode': episode.date_episode.isoformat(),
            'motif': episode.motif,
            'diagnostic': episode.diagnostic,
            'douleur': episode.douleur,
            'fievre': episode.fievre,
            'infection_urinaire': episode.infection_urinaire,
            'germe': episode.germe,
            'urease_positif': episode.urease_positif,
            'lateralite': episode.lateralite,
            'siege_douloureux': episode.siege_douloureux,
            'symptomes_associes': episode.symptomes_associes,
            'traitement_medical': episode.traitement_medical,
            'traitement_interventionnel': episode.traitement_interventionnel,
            'date_traitement': episode.date_traitement.isoformat() if episode.date_traitement else None,
            'centre_traitement': episode.centre_traitement,
            'resultat_traitement': episode.resultat_traitement,
            'notes': episode.notes,
            'imageries': [{
                'id': i.id,
                'date_examen': i.date_examen.isoformat(),
                'taille_mm': i.taille_mm,
                'densite_uh': i.densite_uh,
                'morphologie': i.morphologie,
                'localisation': i.localisation
            } for i in episode.imageries],
            'biologies': [{
                'id': b.id,
                'date_examen': b.date_examen.isoformat(),
                'ph_urinaire': b.ph_urinaire,
                'hyperoxalurie': b.hyperoxalurie,
                'hypercalciurie': b.hypercalciurie,
                'hyperuricurie': b.hyperuricurie,
                'cystinurie': b.cystinurie
            } for b in episode.biologies]
        })
    
    elif request.method == 'PUT':
        data = request.json
        
        if 'date_episode' in data:
            try:
                episode.date_episode = datetime.strptime(data['date_episode'], '%Y-%m-%d').date()
            except:
                return jsonify({'error': 'Date invalide'}), 400
        
        for field in ['motif', 'diagnostic', 'douleur', 'fievre', 'infection_urinaire',
                     'germe', 'urease_positif', 'lateralite', 'siege_douloureux', 'symptomes_associes',
                     'traitement_medical', 'traitement_interventionnel', 'centre_traitement',
                     'resultat_traitement', 'notes']:
            if field in data:
                setattr(episode, field, data[field])
        
        db.session.commit()
        return jsonify({'message': 'Épisode mis à jour avec succès'})
    
    elif request.method == 'DELETE':
        db.session.delete(episode)
        db.session.commit()
        return jsonify({'message': 'Épisode supprimé avec succès'})

@app.route('/api/episodes/<int:episode_id>/imageries', methods=['GET', 'POST'])
@login_required
def imageries(episode_id):
    episode = Episode.query.get_or_404(episode_id)
    
    if request.method == 'POST':
        data = request.json
        
        try:
            date_examen = datetime.strptime(data['date_examen'], '%Y-%m-%d').date()
        except:
            return jsonify({'error': 'Date d\'examen invalide'}), 400
        
        imagerie = Imagerie(
            episode_id=episode_id,
            date_examen=date_examen,
            taille_mm=data.get('taille_mm'),
            densite_uh=data.get('densite_uh'),
            densite_ecart_type=data.get('densite_ecart_type'),
            morphologie=data.get('morphologie'),
            radio_opacite=data.get('radio_opacite'),
            localisation=data.get('localisation'),
            nombre=data.get('nombre'),
            nombre_estime=data.get('nombre_estime'),
            commentaires=data.get('commentaires')
        )
        
        db.session.add(imagerie)
        db.session.commit()
        
        return jsonify({'id': imagerie.id, 'message': 'Imagerie créée avec succès'}), 201
    
    else:
        return jsonify([{
            'id': i.id,
            'date_examen': i.date_examen.isoformat(),
            'taille_mm': i.taille_mm,
            'densite_uh': i.densite_uh,
            'morphologie': i.morphologie,
            'localisation': i.localisation
        } for i in episode.imageries])

@app.route('/api/imageries/<int:imagerie_id>', methods=['GET', 'PUT', 'DELETE'])
@login_required
def imagerie_detail(imagerie_id):
    imagerie = Imagerie.query.get_or_404(imagerie_id)
    
    if request.method == 'GET':
        return jsonify({
            'id': imagerie.id,
            'episode_id': imagerie.episode_id,
            'date_examen': imagerie.date_examen.isoformat(),
            'taille_mm': imagerie.taille_mm,
            'densite_uh': imagerie.densite_uh,
            'densite_ecart_type': imagerie.densite_ecart_type,
            'morphologie': imagerie.morphologie,
            'radio_opacite': imagerie.radio_opacite,
            'localisation': imagerie.localisation,
            'nombre': imagerie.nombre,
            'nombre_estime': imagerie.nombre_estime,
            'commentaires': imagerie.commentaires
        })
    
    elif request.method == 'PUT':
        data = request.json
        
        if 'date_examen' in data:
            try:
                imagerie.date_examen = datetime.strptime(data['date_examen'], '%Y-%m-%d').date()
            except:
                return jsonify({'error': 'Date invalide'}), 400
        
        for field in ['taille_mm', 'densite_uh', 'densite_ecart_type', 'morphologie',
                     'radio_opacite', 'localisation', 'nombre', 'nombre_estime', 'commentaires']:
            if field in data:
                setattr(imagerie, field, data[field])
        
        db.session.commit()
        return jsonify({'message': 'Imagerie mise à jour avec succès'})
    
    elif request.method == 'DELETE':
        db.session.delete(imagerie)
        db.session.commit()
        return jsonify({'message': 'Imagerie supprimée avec succès'})

@app.route('/api/episodes/<int:episode_id>/biologies', methods=['GET', 'POST'])
@login_required
def biologies(episode_id):
    episode = Episode.query.get_or_404(episode_id)
    
    if request.method == 'POST':
        data = request.json
        
        try:
            date_examen = datetime.strptime(data['date_examen'], '%Y-%m-%d').date()
        except:
            return jsonify({'error': 'Date d\'examen invalide'}), 400
        
        biologie = Biologie(
            episode_id=episode_id,
            date_examen=date_examen,
            ph_urinaire=data.get('ph_urinaire'),
            hyperoxalurie=data.get('hyperoxalurie', False),
            hypercalciurie=data.get('hypercalciurie', False),
            hyperuricurie=data.get('hyperuricurie', False),
            cystinurie=data.get('cystinurie', False),
            oxalurie_valeur=data.get('oxalurie_valeur'),
            calciurie_valeur=data.get('calciurie_valeur'),
            uricurie_valeur=data.get('uricurie_valeur'),
            infection_urinaire=data.get('infection_urinaire', False),
            germe=data.get('germe'),
            urease_positif=data.get('urease_positif'),
            commentaires=data.get('commentaires')
        )
        
        db.session.add(biologie)
        db.session.commit()
        
        return jsonify({'id': biologie.id, 'message': 'Biologie créée avec succès'}), 201
    
    else:
        return jsonify([{
            'id': b.id,
            'date_examen': b.date_examen.isoformat(),
            'ph_urinaire': b.ph_urinaire,
            'hyperoxalurie': b.hyperoxalurie,
            'hypercalciurie': b.hypercalciurie,
            'hyperuricurie': b.hyperuricurie,
            'cystinurie': b.cystinurie
        } for b in episode.biologies])

@app.route('/api/biologies/<int:biologie_id>', methods=['GET', 'PUT', 'DELETE'])
@login_required
def biologie_detail(biologie_id):
    biologie = Biologie.query.get_or_404(biologie_id)
    
    if request.method == 'GET':
        return jsonify({
            'id': biologie.id,
            'episode_id': biologie.episode_id,
            'date_examen': biologie.date_examen.isoformat(),
            'ph_urinaire': biologie.ph_urinaire,
            'hyperoxalurie': biologie.hyperoxalurie,
            'hypercalciurie': biologie.hypercalciurie,
            'hyperuricurie': biologie.hyperuricurie,
            'cystinurie': biologie.cystinurie,
            'oxalurie_valeur': biologie.oxalurie_valeur,
            'calciurie_valeur': biologie.calciurie_valeur,
            'uricurie_valeur': biologie.uricurie_valeur,
            'infection_urinaire': biologie.infection_urinaire,
            'germe': biologie.germe,
            'urease_positif': biologie.urease_positif,
            'commentaires': biologie.commentaires
        })
    
    elif request.method == 'PUT':
        data = request.json
        
        if 'date_examen' in data:
            try:
                biologie.date_examen = datetime.strptime(data['date_examen'], '%Y-%m-%d').date()
            except:
                return jsonify({'error': 'Date invalide'}), 400
        
        for field in ['ph_urinaire', 'hyperoxalurie', 'hypercalciurie', 'hyperuricurie', 'cystinurie',
                     'oxalurie_valeur', 'calciurie_valeur', 'uricurie_valeur',
                     'infection_urinaire', 'germe', 'urease_positif', 'commentaires']:
            if field in data:
                setattr(biologie, field, data[field])
        
        db.session.commit()
        return jsonify({'message': 'Biologie mise à jour avec succès'})
    
    elif request.method == 'DELETE':
        db.session.delete(biologie)
        db.session.commit()
        return jsonify({'message': 'Biologie supprimée avec succès'})

@app.route('/api/episodes/<int:episode_id>/inference', methods=['POST'])
@login_required
def infer(episode_id):
    episode = Episode.query.get_or_404(episode_id)
    
    if not episode.imageries:
        return jsonify({'error': 'Aucune imagerie disponible pour cet épisode'}), 400
    
    latest_imaging = max(episode.imageries, key=lambda x: x.date_examen)
    
    imaging_data = {
        'densite_uh': latest_imaging.densite_uh,
        'morphologie': latest_imaging.morphologie,
        'radio_opacite': latest_imaging.radio_opacite,
        'taille_mm': latest_imaging.taille_mm
    }
    
    biology_data = {}
    if episode.biologies:
        latest_biology = max(episode.biologies, key=lambda x: x.date_examen)
        biology_data = {
            'ph_urinaire': latest_biology.ph_urinaire,
            'infection_urinaire': latest_biology.infection_urinaire,
            'hyperoxalurie': latest_biology.hyperoxalurie,
            'hypercalciurie': latest_biology.hypercalciurie,
            'hyperuricurie': latest_biology.hyperuricurie,
            'cystinurie': latest_biology.cystinurie
        }
    
    result = InferenceEngine.infer_stone_type(imaging_data, biology_data)
    
    return jsonify(result)

@app.route('/api/search', methods=['POST'])
@login_required
def search_patients():
    filters = request.json
    
    query = db.session.query(Patient).join(Episode, Patient.id == Episode.patient_id, isouter=True)
    
    if 'search' in filters and filters['search']:
        search_term = f"%{filters['search']}%"
        query = query.filter(
            (Patient.nom.like(search_term)) |
            (Patient.prenom.like(search_term)) |
            (Patient.telephone.like(search_term))
        )
    
    query = query.distinct()
    patients = query.all()
    
    results = []
    for patient in patients:
        for episode in patient.episodes:
            for imagerie in episode.imageries:
                for biologie in episode.biologies:
                    match = True
                    
                    if 'ph_min' in filters and filters['ph_min']:
                        if not biologie.ph_urinaire or biologie.ph_urinaire < float(filters['ph_min']):
                            match = False
                    
                    if 'ph_max' in filters and filters['ph_max']:
                        if not biologie.ph_urinaire or biologie.ph_urinaire > float(filters['ph_max']):
                            match = False
                    
                    if 'uh_min' in filters and filters['uh_min']:
                        if not imagerie.densite_uh or imagerie.densite_uh < int(filters['uh_min']):
                            match = False
                    
                    if 'uh_max' in filters and filters['uh_max']:
                        if not imagerie.densite_uh or imagerie.densite_uh > int(filters['uh_max']):
                            match = False
                    
                    if 'infection' in filters and filters['infection'] is not None:
                        if biologie.infection_urinaire != filters['infection']:
                            match = False
                    
                    if match:
                        results.append({
                            'patient_id': patient.id,
                            'patient_nom': f"{patient.nom} {patient.prenom}",
                            'date_naissance': patient.date_naissance.isoformat(),
                            'episode_id': episode.id,
                            'date_episode': episode.date_episode.isoformat(),
                            'ph_urinaire': biologie.ph_urinaire,
                            'densite_uh': imagerie.densite_uh,
                            'taille_mm': imagerie.taille_mm,
                            'infection': biologie.infection_urinaire
                        })
    
    return jsonify(results)

@app.route('/api/export/csv', methods=['POST'])
@login_required
def export_csv():
    filters = request.json
    response = search_patients()
    results = response.get_json()
    
    output = io.StringIO()
    writer = csv.writer(output)
    
    writer.writerow(['Patient', 'Date Naissance', 'Date Épisode', 'pH', 'Densité UH', 'Taille mm', 'Infection'])
    
    for result in results:
        writer.writerow([
            result['patient_nom'],
            result['date_naissance'],
            result['date_episode'],
            result['ph_urinaire'],
            result['densite_uh'],
            result['taille_mm'],
            'Oui' if result['infection'] else 'Non'
        ])
    
    output.seek(0)
    return send_file(
        io.BytesIO(output.getvalue().encode('utf-8')),
        mimetype='text/csv',
        as_attachment=True,
        download_name=f'lithiase_export_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
    )

@app.route('/api/patients/<int:patient_id>/export/pdf', methods=['GET'])
@login_required
def export_patient_pdf(patient_id):
    patient = Patient.query.get_or_404(patient_id)
    
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=2*cm, leftMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm)
    
    story = []
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle('CustomTitle', parent=styles['Heading1'], fontSize=16, textColor=colors.HexColor('#1e40af'))
    
    story.append(Paragraph(f"Dossier Patient - {patient.nom} {patient.prenom}", title_style))
    story.append(Spacer(1, 0.5*cm))
    
    patient_data = [
        ['Nom', f"{patient.nom} {patient.prenom}"],
        ['Date de naissance', patient.date_naissance.strftime('%d/%m/%Y')],
        ['Sexe', patient.sexe],
        ['Téléphone', patient.telephone or '-'],
        ['Email', patient.email or '-']
    ]
    
    t = Table(patient_data, colWidths=[5*cm, 10*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.grey),
        ('TEXTCOLOR', (0, 0), (0, -1), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey)
    ]))
    story.append(t)
    story.append(Spacer(1, 0.5*cm))
    
    if patient.episodes:
        story.append(Paragraph("Épisodes récents", styles['Heading2']))
        story.append(Spacer(1, 0.3*cm))
        
        for episode in sorted(patient.episodes, key=lambda x: x.date_episode, reverse=True)[:3]:
            story.append(Paragraph(f"<b>Épisode du {episode.date_episode.strftime('%d/%m/%Y')}</b>", styles['Normal']))
            story.append(Paragraph(f"Motif: {episode.motif or '-'}", styles['Normal']))
            
            if episode.imageries and episode.biologies:
                latest_imaging = max(episode.imageries, key=lambda x: x.date_examen)
                latest_biology = max(episode.biologies, key=lambda x: x.date_examen)
                
                imaging_data = {
                    'densite_uh': latest_imaging.densite_uh,
                    'morphologie': latest_imaging.morphologie,
                    'radio_opacite': latest_imaging.radio_opacite,
                    'taille_mm': latest_imaging.taille_mm
                }
                
                biology_data = {
                    'ph_urinaire': latest_biology.ph_urinaire,
                    'infection_urinaire': latest_biology.infection_urinaire,
                    'hyperoxalurie': latest_biology.hyperoxalurie,
                    'hypercalciurie': latest_biology.hypercalciurie,
                    'hyperuricurie': latest_biology.hyperuricurie,
                    'cystinurie': latest_biology.cystinurie
                }
                
                result = InferenceEngine.infer_stone_type(imaging_data, biology_data)
                
                story.append(Paragraph(f"<b>Type proposé:</b> {result['top_1']} (score: {result['top_1_score']}/20)", styles['Normal']))
                story.append(Paragraph(f"<b>LEC éligible:</b> {'Oui' if result['lec_eligible'] else 'Non'}", styles['Normal']))
                story.append(Paragraph(f"<b>Voie de traitement:</b> {result['voie_traitement']}", styles['Normal']))
                
                if result['prevention']:
                    story.append(Paragraph("<b>Prévention:</b>", styles['Normal']))
                    for conseil in result['prevention'][:3]:
                        story.append(Paragraph(f"• {conseil}", styles['Normal']))
            
            story.append(Spacer(1, 0.3*cm))
    
    doc.build(story)
    buffer.seek(0)
    
    return send_file(
        buffer,
        mimetype='application/pdf',
        as_attachment=True,
        download_name=f'dossier_{patient.nom}_{patient.prenom}_{datetime.now().strftime("%Y%m%d")}.pdf'
    )

@app.route('/patient/<int:patient_id>')
@login_required
def patient_page(patient_id):
    return render_template('patient.html', patient_id=patient_id)

@app.route('/search')
@login_required
def search_page():
    return render_template('search.html')

with app.app_context():
    db.create_all()
    
    if not User.query.first():
        admin_username = os.environ.get('ADMIN_USERNAME', 'admin')
        admin_password = os.environ.get('ADMIN_PASSWORD', 'admin123')
        admin = User(username=admin_username)
        admin.set_password(admin_password)
        db.session.add(admin)
        db.session.commit()
        print(f"Utilisateur admin créé (username: {admin_username})")
        if admin_password == 'admin123':
            print("ATTENTION: Utilisez les variables d'environnement ADMIN_USERNAME et ADMIN_PASSWORD pour sécuriser les credentials")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
