from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
import os

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__, 
                template_folder='../templates',
                static_folder='../static')
    
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'lithiase-secret-key-change-in-production')
    
    database_url = os.environ.get('DATABASE_URL')
    if not database_url:
        raise ValueError("DATABASE_URL environment variable is required. PostgreSQL database must be configured.")
    
    if '?' not in database_url:
        database_url += '?sslmode=require'
    elif 'sslmode' not in database_url:
        database_url += '&sslmode=require'
    
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
        'pool_recycle': 300,
        'pool_pre_ping': True,
    }
    app.config['UPLOAD_FOLDER'] = 'uploads'
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
    
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    csrf.init_app(app)
    
    @app.context_processor
    def inject_csrf_token():
        from flask_wtf.csrf import generate_csrf
        return dict(csrf_token=generate_csrf)
    
    with app.app_context():
        from backend.models import User
        from backend.routes import auth, patients, episodes, imageries, biologies, search, exports, settings, field_options_api
        from backend.database.init import initialize_database
        
        app.register_blueprint(auth.bp)
        app.register_blueprint(patients.bp)
        app.register_blueprint(episodes.bp)
        app.register_blueprint(imageries.bp)
        app.register_blueprint(biologies.bp)
        app.register_blueprint(search.bp)
        app.register_blueprint(exports.bp)
        app.register_blueprint(settings.bp)
        app.register_blueprint(field_options_api.bp)
        
        if os.environ.get('SKIP_DB_INIT') != 'true':
            initialize_database(app)
        
        if not User.query.first():
            admin_username = os.environ.get('ADMIN_USERNAME', 'admin')
            admin_password = os.environ.get('ADMIN_PASSWORD', 'admin123')
            admin = User(username=admin_username)
            admin.set_password(admin_password)
            db.session.add(admin)
            db.session.commit()
            print(f"Utilisateur admin créé (username: {admin_username})")
            if admin_password == 'admin123':
                print("ATTENTION: Utilisez les variables d'environnement ADMIN_USERNAME et ADMIN_PASSWORD pour sécuriser les credentials")
    
    @login_manager.user_loader
    def load_user(user_id):
        from backend.models import User
        return User.query.get(int(user_id))
    
    return app
