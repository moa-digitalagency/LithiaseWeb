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
        
        imagerie.nombre_calculs = data.get('nombre_calculs')
        imagerie.topographie_calcul = data.get('topographie_calcul')
        imagerie.diametre_longitudinal = data.get('diametre_longitudinal')
        imagerie.diametre_transversal = data.get('diametre_transversal')
        imagerie.forme_calcul = data.get('forme_calcul')
        imagerie.contour_calcul = data.get('contour_calcul')
        imagerie.densite_noyau = data.get('densite_noyau')
        imagerie.densites_couches = data.get('densites_couches')
        imagerie.calcifications_autres = data.get('calcifications_autres')
        imagerie.asp_resultats = data.get('asp_resultats')
        imagerie.echographie_resultats = data.get('echographie_resultats')
        imagerie.uroscanner_resultats = data.get('uroscanner_resultats')
        
        db.session.add(imagerie)
        db.session.commit()
        
        return jsonify({'id': imagerie.id, 'message': 'Imagerie créée avec succès'}), 201
    
    else:
        return jsonify([{
            'id': i.id,
            'date_examen': i.date_examen.isoformat(),
            'taille_mm': i.taille_mm,
            'densite_uh': i.densite_uh,
            'densite_ecart_type': i.densite_ecart_type,
            'morphologie': i.morphologie,
            'radio_opacite': i.radio_opacite,
            'localisation': i.localisation,
            'nombre': i.nombre,
            'nombre_estime': i.nombre_estime,
            'nombre_calculs': i.nombre_calculs,
            'topographie_calcul': i.topographie_calcul,
            'diametre_longitudinal': i.diametre_longitudinal,
            'diametre_transversal': i.diametre_transversal,
            'forme_calcul': i.forme_calcul,
            'contour_calcul': i.contour_calcul,
            'densite_noyau': i.densite_noyau,
            'densites_couches': i.densites_couches,
            'calcifications_autres': i.calcifications_autres,
            'asp_resultats': i.asp_resultats,
            'echographie_resultats': i.echographie_resultats,
            'uroscanner_resultats': i.uroscanner_resultats
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
            'commentaires': imagerie.commentaires,
            'nombre_calculs': imagerie.nombre_calculs,
            'topographie_calcul': imagerie.topographie_calcul,
            'diametre_longitudinal': imagerie.diametre_longitudinal,
            'diametre_transversal': imagerie.diametre_transversal,
            'forme_calcul': imagerie.forme_calcul,
            'contour_calcul': imagerie.contour_calcul,
            'densite_noyau': imagerie.densite_noyau,
            'densites_couches': imagerie.densites_couches,
            'calcifications_autres': imagerie.calcifications_autres,
            'asp_resultats': imagerie.asp_resultats,
            'echographie_resultats': imagerie.echographie_resultats,
            'uroscanner_resultats': imagerie.uroscanner_resultats
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
        if 'nombre_calculs' in data:
            imagerie.nombre_calculs = data['nombre_calculs']
        if 'topographie_calcul' in data:
            imagerie.topographie_calcul = data['topographie_calcul']
        if 'diametre_longitudinal' in data:
            imagerie.diametre_longitudinal = data['diametre_longitudinal']
        if 'diametre_transversal' in data:
            imagerie.diametre_transversal = data['diametre_transversal']
        if 'forme_calcul' in data:
            imagerie.forme_calcul = data['forme_calcul']
        if 'contour_calcul' in data:
            imagerie.contour_calcul = data['contour_calcul']
        if 'densite_noyau' in data:
            imagerie.densite_noyau = data['densite_noyau']
        if 'densites_couches' in data:
            imagerie.densites_couches = data['densites_couches']
        if 'calcifications_autres' in data:
            imagerie.calcifications_autres = data['calcifications_autres']
        if 'asp_resultats' in data:
            imagerie.asp_resultats = data['asp_resultats']
        if 'echographie_resultats' in data:
            imagerie.echographie_resultats = data['echographie_resultats']
        if 'uroscanner_resultats' in data:
            imagerie.uroscanner_resultats = data['uroscanner_resultats']
        
        db.session.commit()
        return jsonify({'message': 'Imagerie mise à jour avec succès'})
    
    elif request.method == 'DELETE':
        db.session.delete(imagerie)
        db.session.commit()
        return jsonify({'message': 'Imagerie supprimée avec succès'})
