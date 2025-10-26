from flask import Blueprint, request, jsonify
from flask_login import login_required
from backend import db
from backend.models import Patient, Episode

bp = Blueprint('search', __name__)

@bp.route('/api/search', methods=['POST'])
@login_required
def search_patients():
    filters = request.json
    
    query = db.session.query(Patient).join(Episode, Patient.id == Episode.patient_id, isouter=True)
    
    query = query.distinct()
    patients = query.all()
    
    results = []
    for patient in patients:
        for episode in patient.episodes:
            for imagerie in episode.imageries:
                for biologie in episode.biologies:
                    match = True
                    
                    if 'search' in filters and filters['search']:
                        search_term = filters['search'].lower()
                        if not (search_term in (patient.nom or '').lower() or
                                search_term in (patient.prenom or '').lower() or
                                search_term in (patient.telephone or '').lower()):
                            match = False
                    
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
