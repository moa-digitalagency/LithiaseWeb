from flask import Blueprint, render_template, request, jsonify, redirect, url_for, session
from flask_login import login_user, logout_user, login_required
from backend.models import User

bp = Blueprint('auth', __name__)

@bp.route('/')
@login_required
def index():
    return render_template('dashboard.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.json
        user = User.query.filter_by(username=data['username']).first()
        
        if user and user.check_password(data['password']):
            login_user(user)
            session['user_id'] = user.id
            session['username'] = user.username
            return jsonify({'success': True})
        else:
            return jsonify({'success': False, 'message': 'Identifiants incorrects'}), 401
    
    return render_template('login.html')

@bp.route('/logout')
def logout():
    logout_user()
    session.clear()
    return redirect(url_for('auth.login'))

@bp.route('/patient/<int:patient_id>')
@login_required
def patient_page(patient_id):
    return render_template('patient.html', patient_id=patient_id)

@bp.route('/search')
@login_required
def search_page():
    return render_template('search.html')

@bp.route('/nouveau-patient')
@login_required
def nouveau_patient_page():
    return render_template('nouveau-patient.html')
