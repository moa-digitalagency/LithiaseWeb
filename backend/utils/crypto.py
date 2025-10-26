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
            encryption_key = Fernet.generate_key()
            print("=" * 80)
            print("ATTENTION: Aucune clé de chiffrement trouvée!")
            print(f"Clé générée automatiquement: {encryption_key.decode()}")
            print("Pour la production, définissez ENCRYPTION_KEY dans les variables d'environnement")
            print("=" * 80)
            with open('.encryption_key', 'wb') as f:
                f.write(encryption_key)
        else:
            encryption_key = encryption_key.encode()
        
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
