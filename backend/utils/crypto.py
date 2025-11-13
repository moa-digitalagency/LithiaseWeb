from cryptography.fernet import Fernet
import os
import base64

class EncryptionManager:
    """
    Gestionnaire de chiffrement pour les données de santé sensibles.
    Utilise Fernet (chiffrement symétrique) pour protéger les données personnelles.
    """
    
    def __init__(self):
        encryption_key = os.environ.get('ENCRYPTION_KEY')
        
        if not encryption_key:
            key_file = '.encryption_key'
            
            if os.path.exists(key_file):
                with open(key_file, 'rb') as f:
                    encryption_key = f.read()
                print("=" * 80)
                print("⚠️  MIGRATION REQUISE: Clé de chiffrement chargée depuis .encryption_key")
                print("=" * 80)
                print("📝 ACTIONS À EFFECTUER:")
                print("   1. Copiez la clé ci-dessous")
                print(f"   2. Ajoutez-la comme secret Replit nommé 'ENCRYPTION_KEY'")
                print(f"   3. Une fois le secret ajouté, supprimez le fichier .encryption_key")
                print("=" * 80)
                print(f"🔑 Clé: {encryption_key.decode()}")
                print("=" * 80)
                print("ℹ️  Le fichier .encryption_key sera ignoré une fois le secret configuré")
                print("=" * 80)
            else:
                encryption_key = Fernet.generate_key()
                print("=" * 80)
                print("⚠️  CONFIGURATION REQUISE: Nouvelle clé de chiffrement générée!")
                print("=" * 80)
                print("📝 ACTIONS À EFFECTUER:")
                print("   1. Copiez la clé ci-dessous")
                print("   2. Ajoutez-la comme secret Replit nommé 'ENCRYPTION_KEY'")
                print("   3. Redémarrez l'application")
                print("=" * 80)
                print(f"🔑 Clé générée: {encryption_key.decode()}")
                print("=" * 80)
                print("⚠️  La clé a été sauvegardée temporairement dans .encryption_key")
                print("⚠️  IMPORTANT: Configurez le secret Replit puis supprimez ce fichier!")
                print("=" * 80)
                # Sauvegarder temporairement pour éviter la perte de données
                with open(key_file, 'wb') as f:
                    f.write(encryption_key)
        else:
            # La clé est déjà en base64, on la convertit en bytes
            encryption_key = encryption_key.encode('utf-8')
            print("=" * 80)
            print("✓ Clé de chiffrement chargée depuis le secret Replit 'ENCRYPTION_KEY'")
            print("=" * 80)
            # Supprimer le fichier temporaire s'il existe
            if os.path.exists('.encryption_key'):
                os.remove('.encryption_key')
                print("✓ Fichier temporaire .encryption_key supprimé")
        
        self.fernet = Fernet(encryption_key)
    
    def encrypt(self, data):
        """
        Chiffre une donnée sensible.
        Args:
            data: La donnée à chiffrer (str ou None)
        Returns:
            La donnée chiffrée en base64 (str) ou None
        """
        if data is None or data == '':
            return None
        
        if isinstance(data, str):
            data = data.encode('utf-8')
        
        encrypted = self.fernet.encrypt(data)
        return base64.b64encode(encrypted).decode('utf-8')
    
    def decrypt(self, encrypted_data):
        """
        Déchiffre une donnée.
        Args:
            encrypted_data: La donnée chiffrée en base64 (str ou None)
        Returns:
            La donnée déchiffrée (str) ou None
        """
        if encrypted_data is None or encrypted_data == '':
            return None
        
        try:
            encrypted_bytes = base64.b64decode(encrypted_data.encode('utf-8'))
            decrypted = self.fernet.decrypt(encrypted_bytes)
            return decrypted.decode('utf-8')
        except Exception as e:
            print(f"Erreur de déchiffrement: {e}")
            return None

encryption_manager = EncryptionManager()
