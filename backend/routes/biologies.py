from flask import Blueprint, request, jsonify
from flask_login import login_required
from backend import db
from backend.models import Episode, Biologie
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
        biologie.oxalurie_valeur = data.get('oxalurie_valeur')
        biologie.calciurie_valeur = data.get('calciurie_valeur')
        biologie.uricurie_valeur = data.get('uricurie_valeur')
        biologie.infection_urinaire = data.get('infection_urinaire', False)
        biologie.germe = data.get('germe')
        biologie.urease_positif = data.get('urease_positif')
        biologie.commentaires = data.get('commentaires')
        
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
        if 'oxalurie_valeur' in data:
            biologie.oxalurie_valeur = data['oxalurie_valeur']
        if 'calciurie_valeur' in data:
            biologie.calciurie_valeur = data['calciurie_valeur']
        if 'uricurie_valeur' in data:
            biologie.uricurie_valeur = data['uricurie_valeur']
        if 'infection_urinaire' in data:
            biologie.infection_urinaire = data['infection_urinaire']
        if 'germe' in data:
            biologie.germe = data['germe']
        if 'urease_positif' in data:
            biologie.urease_positif = data['urease_positif']
        if 'commentaires' in data:
            biologie.commentaires = data['commentaires']
        
        db.session.commit()
        return jsonify({'message': 'Biologie mise à jour avec succès'})
    
    elif request.method == 'DELETE':
        db.session.delete(biologie)
        db.session.commit()
        return jsonify({'message': 'Biologie supprimée avec succès'})
