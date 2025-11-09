"""
API pour les options de champs du formulaire patient
====================================================
Fournit les options prédéfinies au frontend
====================================================
"""
from flask import Blueprint, jsonify
from backend.field_options import get_all_options_as_dict

bp = Blueprint('field_options', __name__, url_prefix='/api')

@bp.route('/field-options', methods=['GET'])
def get_field_options():
    """Retourne toutes les options de champs en JSON"""
    return jsonify(get_all_options_as_dict())
