from flask import Blueprint, request, jsonify
from flask_login import login_required
from backend import db
from backend.models import Patient, Episode, Biologie
from backend.services import calculate_metabolic_booleans
from backend.utils.patient_code import generate_unique_patient_code
from datetime import datetime, date

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
        
        def code_exists(code):
            return Patient.query.filter_by(code_patient=code).first() is not None
        
        patient.code_patient = generate_unique_patient_code(code_exists)
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
        patient.tension_arterielle_systolique = data.get('tension_arterielle_systolique')
        patient.tension_arterielle_diastolique = data.get('tension_arterielle_diastolique')
        patient.frequence_cardiaque = data.get('frequence_cardiaque')
        patient.temperature = data.get('temperature')
        patient.frequence_respiratoire = data.get('frequence_respiratoire')
        patient.petit_dejeuner = data.get('petit_dejeuner')
        patient.dejeuner = data.get('dejeuner')
        patient.diner = data.get('diner')
        patient.grignotage = data.get('grignotage')
        patient.autres_consommations = data.get('autres_consommations')
        patient.asp_resultats = data.get('asp_resultats')
        patient.echographie_resultats = data.get('echographie_resultats')
        patient.uroscanner_resultats = data.get('uroscanner_resultats')
        patient.sediment_urinaire = data.get('sediment_urinaire')
        patient.ecbu_resultats = data.get('ecbu_resultats')
        patient.ph_urinaire = data.get('ph_urinaire')
        patient.densite_urinaire = data.get('densite_urinaire')
        patient.nombre_calculs = data.get('nombre_calculs')
        patient.topographie_calcul = data.get('topographie_calcul')
        patient.diametre_longitudinal = data.get('diametre_longitudinal')
        patient.diametre_transversal = data.get('diametre_transversal')
        patient.forme_calcul = data.get('forme_calcul')
        patient.contour_calcul = data.get('contour_calcul')
        patient.densite_noyau = data.get('densite_noyau')
        patient.densites_couches = data.get('densites_couches')
        patient.calcifications_autres = data.get('calcifications_autres')
        patient.notes = data.get('notes')
        
        db.session.add(patient)
        db.session.flush()
        
        has_biological_data = any([
            data.get('t3'), data.get('t4'), data.get('tsh'),
            data.get('calciurie'), data.get('calciemie'), data.get('oxalurie'),
            data.get('uree'), data.get('creatinine'),
            data.get('infection_urinaire')
        ])
        
        if has_biological_data:
            episode = Episode()
            episode.patient_id = patient.id
            episode.date_episode = date.today()
            episode.motif = "Bilan initial"
            episode.diagnostic = "Évaluation initiale"
            db.session.add(episode)
            db.session.flush()
            
            biologie = Biologie()
            biologie.episode_id = episode.id
            biologie.date_examen = date.today()
            biologie.ph_urinaire = data.get('ph_urinaire')
            biologie.densite_urinaire = data.get('densite_urinaire')
            
            biologie.t3 = data.get('t3')
            biologie.t4 = data.get('t4')
            biologie.tsh = data.get('tsh')
            
            biologie.oxalurie_valeur = data.get('oxalurie')
            biologie.calciurie_valeur = data.get('calciurie')
            biologie.calciemie_valeur = data.get('calciemie')
            
            biologie.uree = data.get('uree')
            biologie.creatinine = data.get('creatinine')
            
            calculate_metabolic_booleans(biologie, data.get('sexe', 'M'))
            
            biologie.infection_urinaire = data.get('infection_urinaire', False)
            biologie.sediment_urinaire = data.get('sediment_urinaire')
            biologie.ecbu_resultats = data.get('ecbu_resultats')
            
            db.session.add(biologie)
        
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
            'asp_resultats': patient.asp_resultats,
            'echographie_resultats': patient.echographie_resultats,
            'uroscanner_resultats': patient.uroscanner_resultats,
            'sediment_urinaire': patient.sediment_urinaire,
            'ecbu_resultats': patient.ecbu_resultats,
            'ph_urinaire': patient.ph_urinaire,
            'densite_urinaire': patient.densite_urinaire,
            'nombre_calculs': patient.nombre_calculs,
            'topographie_calcul': patient.topographie_calcul,
            'diametre_longitudinal': patient.diametre_longitudinal,
            'diametre_transversal': patient.diametre_transversal,
            'forme_calcul': patient.forme_calcul,
            'contour_calcul': patient.contour_calcul,
            'densite_noyau': patient.densite_noyau,
            'densites_couches': patient.densites_couches,
            'calcifications_autres': patient.calcifications_autres,
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
        if 'asp_resultats' in data:
            patient.asp_resultats = data['asp_resultats']
        if 'echographie_resultats' in data:
            patient.echographie_resultats = data['echographie_resultats']
        if 'uroscanner_resultats' in data:
            patient.uroscanner_resultats = data['uroscanner_resultats']
        if 'sediment_urinaire' in data:
            patient.sediment_urinaire = data['sediment_urinaire']
        if 'ecbu_resultats' in data:
            patient.ecbu_resultats = data['ecbu_resultats']
        if 'ph_urinaire' in data:
            patient.ph_urinaire = data['ph_urinaire']
        if 'densite_urinaire' in data:
            patient.densite_urinaire = data['densite_urinaire']
        if 'nombre_calculs' in data:
            patient.nombre_calculs = data['nombre_calculs']
        if 'topographie_calcul' in data:
            patient.topographie_calcul = data['topographie_calcul']
        if 'diametre_longitudinal' in data:
            patient.diametre_longitudinal = data['diametre_longitudinal']
        if 'diametre_transversal' in data:
            patient.diametre_transversal = data['diametre_transversal']
        if 'forme_calcul' in data:
            patient.forme_calcul = data['forme_calcul']
        if 'contour_calcul' in data:
            patient.contour_calcul = data['contour_calcul']
        if 'densite_noyau' in data:
            patient.densite_noyau = data['densite_noyau']
        if 'densites_couches' in data:
            patient.densites_couches = data['densites_couches']
        if 'calcifications_autres' in data:
            patient.calcifications_autres = data['calcifications_autres']
        if 'notes' in data:
            patient.notes = data['notes']
        
        db.session.commit()
        return jsonify({'message': 'Patient mis à jour avec succès'})
    
    elif request.method == 'DELETE':
        db.session.delete(patient)
        db.session.commit()
        return jsonify({'message': 'Patient supprimé avec succès'})
