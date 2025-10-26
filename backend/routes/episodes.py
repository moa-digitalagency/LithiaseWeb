from flask import Blueprint, request, jsonify
from flask_login import login_required
from backend import db
from backend.models import Patient, Episode
from backend.inference import InferenceEngine
from datetime import datetime

bp = Blueprint('episodes', __name__)

@bp.route('/api/patients/<int:patient_id>/episodes', methods=['GET', 'POST'])
@login_required
def episodes(patient_id):
    patient = Patient.query.get_or_404(patient_id)
    
    if request.method == 'POST':
        data = request.json
        
        try:
            date_episode = datetime.strptime(data['date_episode'], '%Y-%m-%d').date()
        except:
            return jsonify({'error': 'Date d\'épisode invalide'}), 400
        
        episode = Episode()
        episode.patient_id = patient_id
        episode.date_episode = date_episode
        episode.motif = data.get('motif')
        episode.diagnostic = data.get('diagnostic')
        episode.douleur = data.get('douleur', False)
        episode.fievre = data.get('fievre', False)
        episode.infection_urinaire = data.get('infection_urinaire', False)
        episode.germe = data.get('germe')
        episode.urease_positif = data.get('urease_positif')
        episode.lateralite = data.get('lateralite')
        episode.siege_douloureux = data.get('siege_douloureux')
        episode.symptomes_associes = data.get('symptomes_associes')
        episode.traitement_medical = data.get('traitement_medical')
        episode.traitement_interventionnel = data.get('traitement_interventionnel')
        episode.notes = data.get('notes')
        
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

@bp.route('/api/episodes/<int:episode_id>', methods=['GET', 'PUT', 'DELETE'])
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
        
        if 'motif' in data:
            episode.motif = data['motif']
        if 'diagnostic' in data:
            episode.diagnostic = data['diagnostic']
        if 'douleur' in data:
            episode.douleur = data['douleur']
        if 'fievre' in data:
            episode.fievre = data['fievre']
        if 'infection_urinaire' in data:
            episode.infection_urinaire = data['infection_urinaire']
        if 'germe' in data:
            episode.germe = data['germe']
        if 'urease_positif' in data:
            episode.urease_positif = data['urease_positif']
        if 'lateralite' in data:
            episode.lateralite = data['lateralite']
        if 'siege_douloureux' in data:
            episode.siege_douloureux = data['siege_douloureux']
        if 'symptomes_associes' in data:
            episode.symptomes_associes = data['symptomes_associes']
        if 'traitement_medical' in data:
            episode.traitement_medical = data['traitement_medical']
        if 'traitement_interventionnel' in data:
            episode.traitement_interventionnel = data['traitement_interventionnel']
        if 'centre_traitement' in data:
            episode.centre_traitement = data['centre_traitement']
        if 'resultat_traitement' in data:
            episode.resultat_traitement = data['resultat_traitement']
        if 'notes' in data:
            episode.notes = data['notes']
        
        db.session.commit()
        return jsonify({'message': 'Épisode mis à jour avec succès'})
    
    elif request.method == 'DELETE':
        db.session.delete(episode)
        db.session.commit()
        return jsonify({'message': 'Épisode supprimé avec succès'})

@bp.route('/api/episodes/<int:episode_id>/inference', methods=['POST'])
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
