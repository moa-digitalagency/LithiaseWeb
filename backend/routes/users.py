from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend import db
from backend.models import User
from functools import wraps

bp = Blueprint('users', __name__)

def require_permission(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.has_permission(permission):
                return jsonify({'error': 'Permission refusée'}), 403
            return f(*args, **kwargs)
        return decorated_function
    return decorator

@bp.route('/api/users', methods=['GET'])
@login_required
@require_permission('can_manage_users')
def get_users():
    users = User.query.all()
    return jsonify([{
        'id': u.id,
        'username': u.username,
        'role': u.role,
        'can_manage_patients': u.can_manage_patients,
        'can_manage_episodes': u.can_manage_episodes,
        'can_export_data': u.can_export_data,
        'can_manage_users': u.can_manage_users,
        'created_at': u.created_at.isoformat() if u.created_at else None
    } for u in users])

@bp.route('/api/users', methods=['POST'])
@login_required
@require_permission('can_manage_users')
def create_user():
    data = request.json
    
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'error': 'Ce nom d\'utilisateur existe déjà'}), 400
    
    user = User(
        username=data['username'],
        role=data.get('role', 'medecin'),
        can_manage_patients=data.get('can_manage_patients', True),
        can_manage_episodes=data.get('can_manage_episodes', True),
        can_export_data=data.get('can_export_data', True),
        can_manage_users=data.get('can_manage_users', False)
    )
    user.set_password(data['password'])
    
    db.session.add(user)
    db.session.commit()
    
    return jsonify({
        'id': user.id,
        'username': user.username,
        'role': user.role,
        'can_manage_patients': user.can_manage_patients,
        'can_manage_episodes': user.can_manage_episodes,
        'can_export_data': user.can_export_data,
        'can_manage_users': user.can_manage_users
    }), 201

@bp.route('/api/users/<int:user_id>', methods=['PUT'])
@login_required
@require_permission('can_manage_users')
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.json
    
    if current_user.id == user_id and not data.get('can_manage_users', True):
        return jsonify({'error': 'Vous ne pouvez pas retirer vos propres permissions d\'admin'}), 400
    
    if 'username' in data and data['username'] != user.username:
        if User.query.filter_by(username=data['username']).first():
            return jsonify({'error': 'Ce nom d\'utilisateur existe déjà'}), 400
        user.username = data['username']
    
    if 'password' in data and data['password']:
        user.set_password(data['password'])
    
    if 'role' in data:
        user.role = data['role']
    
    user.can_manage_patients = data.get('can_manage_patients', user.can_manage_patients)
    user.can_manage_episodes = data.get('can_manage_episodes', user.can_manage_episodes)
    user.can_export_data = data.get('can_export_data', user.can_export_data)
    user.can_manage_users = data.get('can_manage_users', user.can_manage_users)
    
    db.session.commit()
    
    return jsonify({
        'id': user.id,
        'username': user.username,
        'role': user.role,
        'can_manage_patients': user.can_manage_patients,
        'can_manage_episodes': user.can_manage_episodes,
        'can_export_data': user.can_export_data,
        'can_manage_users': user.can_manage_users
    })

@bp.route('/api/users/<int:user_id>', methods=['DELETE'])
@login_required
@require_permission('can_manage_users')
def delete_user(user_id):
    if current_user.id == user_id:
        return jsonify({'error': 'Vous ne pouvez pas supprimer votre propre compte'}), 400
    
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    
    return jsonify({'message': 'Utilisateur supprimé avec succès'})

@bp.route('/api/users/current', methods=['GET'])
@login_required
def get_current_user():
    return jsonify({
        'id': current_user.id,
        'username': current_user.username,
        'role': current_user.role,
        'can_manage_patients': current_user.can_manage_patients,
        'can_manage_episodes': current_user.can_manage_episodes,
        'can_export_data': current_user.can_export_data,
        'can_manage_users': current_user.can_manage_users
    })
