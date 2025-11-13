from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend import db
from backend.models import Patient, Episode
from backend.services import InferenceEngine
from datetime import datetime

bp = Blueprint('episodes', __name__)

@bp.route('/api/patients/<int:patient_id>/episodes', methods=['GET', 'POST'])
@login_required
def episodes(patient_id):
    patient = Patient.query.get_or_404(patient_id)
    
    if request.method == 'POST':
        if not current_user.has_permission('can_manage_episodes'):
            return jsonify({'error': 'Permission refusée'}), 403
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
        import json as json_lib
        calculated_data = None
        if episode.calculated_stone_type_data:
            try:
                calculated_data = json_lib.loads(episode.calculated_stone_type_data)
            except:
                calculated_data = None
        
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
            'calculated_stone_type': episode.calculated_stone_type,
            'calculated_at': episode.calculated_at.isoformat() if episode.calculated_at else None,
            'calculated_data': calculated_data,
            'imageries': [{
                'id': i.id,
                'date_examen': i.date_examen.isoformat(),
                'taille_mm': i.taille_mm,
                'densite_uh': i.densite_uh,
                'densite_noyau': i.densite_noyau,
                'densites_couches': i.densites_couches,
                'morphologie': i.morphologie,
                'localisation': i.localisation,
                'radio_opacite': i.radio_opacite,
                'nombre_calculs': i.nombre_calculs,
                'topographie_calcul': i.topographie_calcul,
                'diametre_longitudinal': i.diametre_longitudinal,
                'diametre_transversal': i.diametre_transversal,
                'forme_calcul': i.forme_calcul,
                'contour_calcul': i.contour_calcul,
                'calcifications_autres': i.calcifications_autres,
                'malformations_urinaires': i.malformations_urinaires,
                'asp_resultats': i.asp_resultats,
                'echographie_resultats': i.echographie_resultats,
                'uroscanner_resultats': i.uroscanner_resultats,
                'nombre': i.nombre
            } for i in episode.imageries],
            'biologies': [{
                'id': b.id,
                'date_examen': b.date_examen.isoformat(),
                'ph_urinaire': b.ph_urinaire,
                'densite_urinaire': b.densite_urinaire,
                'sediment_urinaire': b.sediment_urinaire,
                'ecbu_resultats': b.ecbu_resultats,
                'hyperoxalurie': b.hyperoxalurie,
                'hypercalciurie': b.hypercalciurie,
                'hyperuricurie': b.hyperuricurie,
                'cystinurie': b.cystinurie,
                'hypercalcemie': b.hypercalcemie,
                'oxalurie_valeur': b.oxalurie_valeur,
                'calciurie_valeur': b.calciurie_valeur,
                'uricurie_valeur': b.uricurie_valeur,
                'calciemie_valeur': b.calciemie_valeur,
                't3': b.t3,
                't4': b.t4,
                'tsh': b.tsh,
                'infection_urinaire': b.infection_urinaire,
                'germe': b.germe,
                'urease_positif': b.urease_positif
            } for b in episode.biologies]
        })
    
    elif request.method == 'PUT':
        if not current_user.has_permission('can_manage_episodes'):
            return jsonify({'error': 'Permission refusée'}), 403
            
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
        if not current_user.has_permission('can_manage_episodes'):
            return jsonify({'error': 'Permission refusée'}), 403
            
        db.session.delete(episode)
        db.session.commit()
        return jsonify({'message': 'Épisode supprimé avec succès'})

@bp.route('/api/episodes/<int:episode_id>/inference', methods=['POST'])
@login_required
def infer(episode_id):
    import json
    
    episode = Episode.query.get_or_404(episode_id)
    
    if not episode.imageries:
        return jsonify({'error': 'Aucune imagerie disponible pour cet épisode'}), 400
    
    latest_imaging = max(episode.imageries, key=lambda x: x.date_examen)
    
    imaging_data = {
        'densite_uh': latest_imaging.densite_uh,
        'densite_noyau': latest_imaging.densite_noyau,
        'densites_couches': latest_imaging.densites_couches,
        'morphologie': latest_imaging.morphologie,
        'radio_opacite': latest_imaging.radio_opacite,
        'taille_mm': latest_imaging.taille_mm,
        'diametre_longitudinal': latest_imaging.diametre_longitudinal,
        'forme_calcul': latest_imaging.forme_calcul,
        'contour_calcul': latest_imaging.contour_calcul,
        'nombre_calculs': latest_imaging.nombre_calculs,
        'topographie_calcul': latest_imaging.topographie_calcul,
        'calcifications_autres': latest_imaging.calcifications_autres,
        'malformations_urinaires': latest_imaging.malformations_urinaires
    }
    
    biology_data = {}
    if episode.biologies:
        latest_biology = max(episode.biologies, key=lambda x: x.date_examen)
        biology_data = {
            'ph_urinaire': latest_biology.ph_urinaire,
            'infection_urinaire': latest_biology.infection_urinaire,
            'sediment_urinaire': latest_biology.sediment_urinaire,
            'ecbu_resultats': latest_biology.ecbu_resultats,
            'hyperoxalurie': latest_biology.hyperoxalurie,
            'hypercalciurie': latest_biology.hypercalciurie,
            'hyperuricurie': latest_biology.hyperuricurie,
            'cystinurie': latest_biology.cystinurie
        }
    
    result = InferenceEngine.infer_stone_type(imaging_data, biology_data)
    
    episode.calculated_stone_type = result['top_1']
    episode.calculated_stone_type_data = json.dumps(result)
    episode.calculated_at = datetime.utcnow()
    db.session.commit()
    
    return jsonify(result)
