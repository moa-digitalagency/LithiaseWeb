from flask import Blueprint, request, jsonify
from flask_login import login_required
from backend import db
from backend.models import Episode, Biologie
from backend.services import calculate_metabolic_booleans
from datetime import datetime

bp = Blueprint('biologies', __name__)

@bp.route('/api/episodes/<int:episode_id>/biologies', methods=['GET', 'POST'])
@login_required
def biologies(episode_id):
    episode = Episode.query.get_or_404(episode_id)
    
    if request.method == 'POST':
        data = request.json
        
        try:
            date_examen = datetime.strptime(data['date_examen'], '%Y-%m-%d').date()
        except:
            return jsonify({'error': 'Date d\'examen invalide'}), 400
        
        biologie = Biologie()
        biologie.episode_id = episode_id
        biologie.date_examen = date_examen
        biologie.ph_urinaire = data.get('ph_urinaire')
        biologie.hyperoxalurie = data.get('hyperoxalurie', False)
        biologie.hypercalciurie = data.get('hypercalciurie', False)
        biologie.hyperuricurie = data.get('hyperuricurie', False)
        biologie.cystinurie = data.get('cystinurie', False)
        biologie.hypercalcemie = data.get('hypercalcemie', False)
        biologie.oxalurie_valeur = data.get('oxalurie_valeur')
        biologie.calciurie_valeur = data.get('calciurie_valeur')
        biologie.uricurie_valeur = data.get('uricurie_valeur')
        biologie.calciemie_valeur = data.get('calciemie_valeur')
        biologie.t3 = data.get('t3')
        biologie.t4 = data.get('t4')
        biologie.tsh = data.get('tsh')
        biologie.uree = data.get('uree')
        biologie.creatinine = data.get('creatinine')
        biologie.infection_urinaire = data.get('infection_urinaire', False)
        biologie.germe = data.get('germe')
        biologie.germe_urease = data.get('germe_urease')
        biologie.urease_positif = data.get('urease_positif')
        biologie.densite_urinaire = data.get('densite_urinaire')
        biologie.sediment_urinaire = data.get('sediment_urinaire')
        biologie.ecbu_resultats = data.get('ecbu_resultats')
        biologie.commentaires = data.get('commentaires')
        
        episode_patient = Episode.query.get(episode_id)
        patient_sexe = episode_patient.patient.sexe if episode_patient else 'M'
        calculate_metabolic_booleans(biologie, patient_sexe)
        
        db.session.add(biologie)
        db.session.commit()
        
        return jsonify({'id': biologie.id, 'message': 'Biologie créée avec succès'}), 201
    
    else:
        return jsonify([{
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
            'uree': b.uree,
            'creatinine': b.creatinine,
            'infection_urinaire': b.infection_urinaire,
            'germe': b.germe,
            'germe_urease': b.germe_urease,
            'urease_positif': b.urease_positif,
            'commentaires': b.commentaires
        } for b in episode.biologies])

@bp.route('/api/biologies/<int:biologie_id>', methods=['GET', 'PUT', 'DELETE'])
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
            'hypercalcemie': biologie.hypercalcemie,
            'oxalurie_valeur': biologie.oxalurie_valeur,
            'calciurie_valeur': biologie.calciurie_valeur,
            'uricurie_valeur': biologie.uricurie_valeur,
            'calciemie_valeur': biologie.calciemie_valeur,
            't3': biologie.t3,
            't4': biologie.t4,
            'tsh': biologie.tsh,
            'uree': biologie.uree,
            'creatinine': biologie.creatinine,
            'infection_urinaire': biologie.infection_urinaire,
            'germe': biologie.germe,
            'germe_urease': biologie.germe_urease,
            'urease_positif': biologie.urease_positif,
            'densite_urinaire': biologie.densite_urinaire,
            'sediment_urinaire': biologie.sediment_urinaire,
            'ecbu_resultats': biologie.ecbu_resultats,
            'commentaires': biologie.commentaires
        })
    
    elif request.method == 'PUT':
        data = request.json
        
        if 'date_examen' in data:
            try:
                biologie.date_examen = datetime.strptime(data['date_examen'], '%Y-%m-%d').date()
            except:
                return jsonify({'error': 'Date invalide'}), 400
        
        if 'ph_urinaire' in data:
            biologie.ph_urinaire = data['ph_urinaire']
        if 'hyperoxalurie' in data:
            biologie.hyperoxalurie = data['hyperoxalurie']
        if 'hypercalciurie' in data:
            biologie.hypercalciurie = data['hypercalciurie']
        if 'hyperuricurie' in data:
            biologie.hyperuricurie = data['hyperuricurie']
        if 'cystinurie' in data:
            biologie.cystinurie = data['cystinurie']
        if 'hypercalcemie' in data:
            biologie.hypercalcemie = data['hypercalcemie']
        if 'oxalurie_valeur' in data:
            biologie.oxalurie_valeur = data['oxalurie_valeur']
        if 'calciurie_valeur' in data:
            biologie.calciurie_valeur = data['calciurie_valeur']
        if 'uricurie_valeur' in data:
            biologie.uricurie_valeur = data['uricurie_valeur']
        if 'calciemie_valeur' in data:
            biologie.calciemie_valeur = data['calciemie_valeur']
        if 't3' in data:
            biologie.t3 = data['t3']
        if 't4' in data:
            biologie.t4 = data['t4']
        if 'tsh' in data:
            biologie.tsh = data['tsh']
        if 'uree' in data:
            biologie.uree = data['uree']
        if 'creatinine' in data:
            biologie.creatinine = data['creatinine']
        if 'infection_urinaire' in data:
            biologie.infection_urinaire = data['infection_urinaire']
        if 'germe' in data:
            biologie.germe = data['germe']
        if 'germe_urease' in data:
            biologie.germe_urease = data['germe_urease']
        if 'urease_positif' in data:
            biologie.urease_positif = data['urease_positif']
        if 'densite_urinaire' in data:
            biologie.densite_urinaire = data['densite_urinaire']
        if 'sediment_urinaire' in data:
            biologie.sediment_urinaire = data['sediment_urinaire']
        if 'ecbu_resultats' in data:
            biologie.ecbu_resultats = data['ecbu_resultats']
        if 'commentaires' in data:
            biologie.commentaires = data['commentaires']
        
        episode_patient = Episode.query.get(biologie.episode_id)
        patient_sexe = episode_patient.patient.sexe if episode_patient else 'M'
        calculate_metabolic_booleans(biologie, patient_sexe)
        
        db.session.commit()
        return jsonify({'message': 'Biologie mise à jour avec succès'})
    
    elif request.method == 'DELETE':
        db.session.delete(biologie)
        db.session.commit()
        return jsonify({'message': 'Biologie supprimée avec succès'})
