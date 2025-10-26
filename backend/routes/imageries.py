from flask import Blueprint, request, jsonify
from flask_login import login_required
from backend import db
from backend.models import Episode, Imagerie
from datetime import datetime

bp = Blueprint('imageries', __name__)

@bp.route('/api/episodes/<int:episode_id>/imageries', methods=['GET', 'POST'])
@login_required
def imageries(episode_id):
    episode = Episode.query.get_or_404(episode_id)
    
    if request.method == 'POST':
        data = request.json
        
        try:
            date_examen = datetime.strptime(data['date_examen'], '%Y-%m-%d').date()
        except:
            return jsonify({'error': 'Date d\'examen invalide'}), 400
        
        imagerie = Imagerie()
        imagerie.episode_id = episode_id
        imagerie.date_examen = date_examen
        imagerie.taille_mm = data.get('taille_mm')
        imagerie.densite_uh = data.get('densite_uh')
        imagerie.densite_ecart_type = data.get('densite_ecart_type')
        imagerie.morphologie = data.get('morphologie')
        imagerie.radio_opacite = data.get('radio_opacite')
        imagerie.localisation = data.get('localisation')
        imagerie.nombre = data.get('nombre')
        imagerie.nombre_estime = data.get('nombre_estime')
        imagerie.commentaires = data.get('commentaires')
        
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

@bp.route('/api/imageries/<int:imagerie_id>', methods=['GET', 'PUT', 'DELETE'])
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
        
        if 'taille_mm' in data:
            imagerie.taille_mm = data['taille_mm']
        if 'densite_uh' in data:
            imagerie.densite_uh = data['densite_uh']
        if 'densite_ecart_type' in data:
            imagerie.densite_ecart_type = data['densite_ecart_type']
        if 'morphologie' in data:
            imagerie.morphologie = data['morphologie']
        if 'radio_opacite' in data:
            imagerie.radio_opacite = data['radio_opacite']
        if 'localisation' in data:
            imagerie.localisation = data['localisation']
        if 'nombre' in data:
            imagerie.nombre = data['nombre']
        if 'nombre_estime' in data:
            imagerie.nombre_estime = data['nombre_estime']
        if 'commentaires' in data:
            imagerie.commentaires = data['commentaires']
        
        db.session.commit()
        return jsonify({'message': 'Imagerie mise à jour avec succès'})
    
    elif request.method == 'DELETE':
        db.session.delete(imagerie)
        db.session.commit()
        return jsonify({'message': 'Imagerie supprimée avec succès'})
