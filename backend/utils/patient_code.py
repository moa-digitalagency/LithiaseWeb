import random
import string

def generate_patient_code():
    """
    Génère un code patient alphanumérique unique de 6 caractères.
    Format: Combinaison de lettres majuscules et chiffres
    Exemple: A3B7K9, X1Y2Z3
    """
    characters = string.ascii_uppercase + string.digits
    code = ''.join(random.choices(characters, k=6))
    return code

def generate_unique_patient_code(existing_codes_check=None):
    """
    Génère un code patient unique en vérifiant qu'il n'existe pas déjà.
    
    Args:
        existing_codes_check: Une fonction qui vérifie si un code existe déjà (optionnel)
    
    Returns:
        Un code patient unique de 6 caractères
    """
    max_attempts = 100
    for _ in range(max_attempts):
        code = generate_patient_code()
        if existing_codes_check is None or not existing_codes_check(code):
            return code
    raise ValueError("Impossible de générer un code patient unique après {} tentatives".format(max_attempts))
