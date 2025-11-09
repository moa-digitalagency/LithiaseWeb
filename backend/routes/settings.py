from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from backend import db
from backend.models import User
from werkzeug.security import check_password_hash
import os

bp = Blueprint('settings', __name__)

@bp.route('/parametres')
@login_required
def parametres():
    return render_template('parametres.html')

@bp.route('/api/settings/password', methods=['POST'])
@login_required
def change_password():
    data = request.json
    
    current_password = data.get('current_password')
    new_password = data.get('new_password')
    confirm_password = data.get('confirm_password')
    
    if not all([current_password, new_password, confirm_password]):
        return jsonify({'error': 'Tous les champs sont requis'}), 400
    
    if new_password != confirm_password:
        return jsonify({'error': 'Les nouveaux mots de passe ne correspondent pas'}), 400
    
    if len(new_password) < 6:
        return jsonify({'error': 'Le mot de passe doit contenir au moins 6 caractères'}), 400
    
    if not current_user.check_password(current_password):
        return jsonify({'error': 'Mot de passe actuel incorrect'}), 401
    
    current_user.set_password(new_password)
    db.session.commit()
    
    return jsonify({'message': 'Mot de passe modifié avec succès'}), 200

@bp.route('/api/settings/profile', methods=['GET', 'PUT'])
@login_required
def profile():
    if request.method == 'GET':
        return jsonify({
            'username': current_user.username,
            'encryption_key_exists': os.path.exists('.encryption_key')
        })
    
    elif request.method == 'PUT':
        data = request.json
        new_username = data.get('username')
        
        if not new_username:
            return jsonify({'error': 'Le nom d\'utilisateur est requis'}), 400
        
        if new_username != current_user.username:
            existing_user = User.query.filter_by(username=new_username).first()
            if existing_user:
                return jsonify({'error': 'Ce nom d\'utilisateur existe déjà'}), 400
            
            current_user.username = new_username
            db.session.commit()
            
        return jsonify({'message': 'Profil mis à jour avec succès'}), 200
