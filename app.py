from backend import create_app
import os
import sys

# Importer et exécuter la vérification automatique de la base de données
# SEULEMENT en mode développement (jamais en production pour sécurité)
if os.environ.get('FLASK_ENV') == 'development' or os.environ.get('ENABLE_AUTO_DEMO_DATA') == 'true':
    try:
        import verify_and_init_db
        if not verify_and_init_db.main():
            print("⚠️  La vérification de la base de données a échoué, mais l'application continue...")
    except Exception as e:
        print(f"⚠️  Erreur lors de la vérification automatique de la base de données: {e}")
        print("L'application continue malgré cette erreur...")
else:
    print("ℹ️  Chargement automatique des données demo désactivé (mode production)")

app = create_app()

if __name__ == '__main__':
    # En mode développement par défaut
    os.environ.setdefault('FLASK_ENV', 'development')
    app.run(host='0.0.0.0', port=5000, debug=True)
