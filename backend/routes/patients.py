from flask import Blueprint, request, jsonify
from flask_login import login_required
from backend import db
from backend.models import Patient
from datetime import datetime

bp = Blueprint('patients', __name__, url_prefix='/api/patients')

@bp.route('', methods=['GET', 'POST'])
@login_required
def patients():
    if request.method == 'POST':
        data = request.json
        
        try:
            date_naissance = datetime.strptime(data['date_naissance'], '%Y-%m-%d').date()
        except:
            return jsonify({'error': 'Date de naissance invalide'}), 400
        
        patient = Patient()
        patient.nom = data['nom']
        patient.prenom = data['prenom']
        patient.date_naissance = date_naissance
        patient.sexe = data['sexe']
        patient.telephone = data.get('telephone')
        patient.email = data.get('email')
        patient.adresse = data.get('adresse')
        patient.antecedents_personnels = data.get('antecedents_personnels')
        patient.antecedents_familiaux = data.get('antecedents_familiaux')
        patient.antecedents_chirurgicaux = data.get('antecedents_chirurgicaux')
        patient.allergies = data.get('allergies')
        patient.traitements_chroniques = data.get('traitements_chroniques')
        patient.hydratation_jour = data.get('hydratation_jour')
        patient.regime_alimentaire = data.get('regime_alimentaire')
        patient.poids = data.get('poids')
        patient.taille = data.get('taille')
        patient.groupe_ethnique = data.get('groupe_ethnique')
        patient.petit_dejeuner = data.get('petit_dejeuner')
        patient.dejeuner = data.get('dejeuner')
        patient.diner = data.get('diner')
        patient.grignotage = data.get('grignotage')
        patient.autres_consommations = data.get('autres_consommations')
        patient.notes = data.get('notes')
        
        db.session.add(patient)
        db.session.commit()
        
        return jsonify({'id': patient.id, 'message': 'Patient créé avec succès'}), 201
    
    else:
        search = request.args.get('search', '')
        if search:
            patients = Patient.query.all()
            filtered_patients = []
            for p in patients:
                if (search.lower() in (p.nom or '').lower() or 
                    search.lower() in (p.prenom or '').lower() or 
                    search.lower() in (p.telephone or '').lower()):
                    filtered_patients.append(p)
        else:
            filtered_patients = Patient.query.all()
        
        return jsonify([{
            'id': p.id,
            'nom': p.nom,
            'prenom': p.prenom,
            'date_naissance': p.date_naissance.isoformat(),
            'sexe': p.sexe,
            'telephone': p.telephone,
            'email': p.email,
            'nb_episodes': len(p.episodes)
        } for p in filtered_patients])

@bp.route('/<int:patient_id>', methods=['GET', 'PUT', 'DELETE'])
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
            'poids': patient.poids,
            'taille': patient.taille,
            'groupe_ethnique': patient.groupe_ethnique,
            'petit_dejeuner': patient.petit_dejeuner,
            'dejeuner': patient.dejeuner,
            'diner': patient.diner,
            'grignotage': patient.grignotage,
            'autres_consommations': patient.autres_consommations,
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
        
        if 'nom' in data:
            patient.nom = data['nom']
        if 'prenom' in data:
            patient.prenom = data['prenom']
        if 'sexe' in data:
            patient.sexe = data['sexe']
        if 'telephone' in data:
            patient.telephone = data['telephone']
        if 'email' in data:
            patient.email = data['email']
        if 'adresse' in data:
            patient.adresse = data['adresse']
        if 'antecedents_personnels' in data:
            patient.antecedents_personnels = data['antecedents_personnels']
        if 'antecedents_familiaux' in data:
            patient.antecedents_familiaux = data['antecedents_familiaux']
        if 'antecedents_chirurgicaux' in data:
            patient.antecedents_chirurgicaux = data['antecedents_chirurgicaux']
        if 'allergies' in data:
            patient.allergies = data['allergies']
        if 'traitements_chroniques' in data:
            patient.traitements_chroniques = data['traitements_chroniques']
        if 'hydratation_jour' in data:
            patient.hydratation_jour = data['hydratation_jour']
        if 'regime_alimentaire' in data:
            patient.regime_alimentaire = data['regime_alimentaire']
        if 'poids' in data:
            patient.poids = data['poids']
        if 'taille' in data:
            patient.taille = data['taille']
        if 'groupe_ethnique' in data:
            patient.groupe_ethnique = data['groupe_ethnique']
        if 'petit_dejeuner' in data:
            patient.petit_dejeuner = data['petit_dejeuner']
        if 'dejeuner' in data:
            patient.dejeuner = data['dejeuner']
        if 'diner' in data:
            patient.diner = data['diner']
        if 'grignotage' in data:
            patient.grignotage = data['grignotage']
        if 'autres_consommations' in data:
            patient.autres_consommations = data['autres_consommations']
        if 'notes' in data:
            patient.notes = data['notes']
        
        db.session.commit()
        return jsonify({'message': 'Patient mis à jour avec succès'})
    
    elif request.method == 'DELETE':
        db.session.delete(patient)
        db.session.commit()
        return jsonify({'message': 'Patient supprimé avec succès'})
