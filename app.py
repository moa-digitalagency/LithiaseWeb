from backend import create_app
import os
import sys

# Note: La vérification et l'initialisation de la base de données
# sont gérées automatiquement par backend/__init__.py dans create_app()
# via initialize_database() et verify_and_init_db est appelé de là si nécessaire

if os.environ.get('FLASK_ENV') != 'development' and os.environ.get('ENABLE_AUTO_DEMO_DATA') != 'true':
    print("ℹ️  Chargement automatique des données demo désactivé (mode production)")

app = create_app()

if __name__ == '__main__':
    # En mode développement par défaut
    os.environ.setdefault('FLASK_ENV', 'development')
    app.run(host='0.0.0.0', port=5000, debug=True)
