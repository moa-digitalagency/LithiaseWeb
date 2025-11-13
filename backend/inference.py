class InferenceEngine:
    
    STONE_TYPES = {
        'Whewellite': {
            'uh_range': (1200, 1700),
            'ph_preferred': (5.0, 5.8),
            'morphology_signatures': ['spherique_lisse'],
            'morphology_compatible': ['irreguliere_spiculee'],
            'radio_opacite': 'opaque',
            'metabolic_marker': 'hyperoxalurie',
            'infection_favorable': False
        },
        'Weddellite': {
            'uh_range': (1000, 1450),
            'ph_preferred': (5.0, 5.8),
            'morphology_signatures': ['irreguliere_spiculee'],
            'morphology_compatible': ['spherique_lisse', 'heterogene'],
            'radio_opacite': 'opaque',
            'metabolic_marker': 'hypercalciurie',
            'infection_favorable': False
        },
        'Carbapatite': {
            'uh_range': (1300, 1400),
            'ph_preferred': (6.8, 7.5),
            'morphology_signatures': ['crayeuse'],
            'morphology_compatible': ['spherique_lisse', 'heterogene'],
            'radio_opacite': 'opaque',
            'metabolic_marker': 'hypercalciurie',
            'infection_favorable': True
        },
        'Brushite': {
            'uh_range': (1550, 2000),
            'ph_preferred': (6.0, 6.8),
            'morphology_signatures': ['irreguliere_spiculee'],
            'morphology_compatible': ['heterogene'],
            'radio_opacite': 'opaque',
            'metabolic_marker': 'hypercalciurie',
            'infection_favorable': False
        },
        'Struvite': {
            'uh_range': (550, 950),
            'ph_preferred': (6.8, 7.5),
            'morphology_signatures': ['coralliforme', 'irreguliere_spiculee'],
            'morphology_compatible': ['crayeuse', 'heterogene'],
            'radio_opacite': 'transparent',
            'metabolic_marker': None,
            'infection_favorable': True
        },
        'Cystine': {
            'uh_range': (650, 850),
            'ph_preferred': (5.0, 5.8),
            'morphology_signatures': ['spherique_lisse'],
            'morphology_compatible': ['heterogene'],
            'radio_opacite': 'transparent',
            'metabolic_marker': 'cystinurie',
            'infection_favorable': False
        },
        'Acide urique': {
            'uh_range': (350, 650),
            'ph_preferred': (5.0, 5.8),
            'morphology_signatures': ['spherique_lisse'],
            'morphology_compatible': ['irreguliere_spiculee', 'heterogene'],
            'radio_opacite': 'transparent',
            'metabolic_marker': 'hyperuricurie',
            'infection_favorable': False
        },
        'Urate ammonium': {
            'uh_range': (150, 300),
            'ph_preferred': (6.8, 7.5),
            'morphology_signatures': ['spherique_lisse'],
            'morphology_compatible': ['heterogene'],
            'radio_opacite': 'transparent',
            'metabolic_marker': None,
            'infection_favorable': True
        }
    }
    
    LEC_ELIGIBILITY = {
        'Weddellite': True,
        'Carbapatite': True,
        'Struvite': True,
        'Whewellite': False,
        'Brushite': False,
        'Cystine': False,
        'Acide urique': False,
        'Urate ammonium': False
    }
    
    PREVENTION_ADVICE = {
        'Acide urique': [
            'Augmenter l\'hydratation (2-3L/jour)',
            'Alcalinisation des urines (citrate de potassium)',
            'Réduire les protéines animales',
            'Limiter les purines (abats, fruits de mer)'
        ],
        'Whewellite': [
            'Hydratation abondante (2-3L/jour)',
            'Réduire les aliments riches en oxalates (épinards, rhubarbe, chocolat, thé)',
            'Apport calcique normal avec les repas',
            'Traiter l\'hyperoxalurie si présente'
        ],
        'Weddellite': [
            'Hydratation abondante (2-3L/jour)',
            'Réduire le sel',
            'Apport calcique normal (1000mg/jour)',
            'Limiter les oxalates',
            'Traiter l\'hypercalciurie si présente'
        ],
        'Struvite': [
            'Contrôle strict des infections urinaires',
            'Antibiothérapie adaptée',
            'Traitement complet du calcul',
            'Suivi urologique régulier'
        ],
        'Carbapatite': [
            'Contrôle des infections urinaires',
            'Hydratation régulière',
            'Bilan phospho-calcique',
            'Éviter l\'alcalinisation excessive'
        ],
        'Brushite': [
            'Hydratation abondante',
            'Bilan parathyroïdien',
            'Contrôle du phosphore',
            'Suivi métabolique rapproché'
        ],
        'Cystine': [
            'Hydratation très abondante (>3L/jour)',
            'Alcalinisation des urines (pH>7.5)',
            'Réduire le sel et les protéines',
            'Traitement spécifique (thiopronine si nécessaire)'
        ],
        'Urate ammonium': [
            'Contrôle des infections urinaires',
            'Traitement des diarrhées chroniques si présentes',
            'Hydratation régulière',
            'Suivi urologique'
        ]
    }
    
    @staticmethod
    def score_density(uh, stone_type):
        if uh is None:
            return 0, "Densité non renseignée"
        
        config = InferenceEngine.STONE_TYPES[stone_type]
        min_uh, max_uh = config['uh_range']
        
        if min_uh <= uh <= max_uh:
            return 6, f"Densité {uh} UH dans la plage typique [{min_uh}-{max_uh}]"
        
        delta = min(abs(uh - min_uh), abs(uh - max_uh))
        if delta <= 100:
            return 4, ""
        elif delta <= 200:
            return 2, ""
        else:
            return 0, ""
    
    @staticmethod
    def score_morphology(morphology, stone_type):
        if morphology is None:
            return 0, "Morphologie non renseignée"
        
        config = InferenceEngine.STONE_TYPES[stone_type]
        
        if morphology in config['morphology_signatures']:
            return 3, f"Morphologie signature ({morphology})"
        elif morphology in config['morphology_compatible']:
            return 1, f"Morphologie compatible ({morphology})"
        else:
            return 0, f"Morphologie non caractéristique"
    
    @staticmethod
    def score_ph(ph, stone_type):
        if ph is None:
            return 0, "pH non renseigné"
        
        config = InferenceEngine.STONE_TYPES[stone_type]
        min_ph, max_ph = config['ph_preferred']
        
        if min_ph <= ph <= max_ph:
            return 3, f"pH {ph} dans la plage préférentielle [{min_ph}-{max_ph}]"
        
        delta = min(abs(ph - min_ph), abs(ph - max_ph))
        if delta <= 0.5:
            return 1, ""
        else:
            return 0, ""
    
    @staticmethod
    def detect_hyperthyroidism(t3, t4, tsh):
        if tsh is None:
            return False, None
        
        if tsh < 0.4:
            if t3 is not None and t3 > 2.0:
                return True, "Hyperthyroïdie détectée (TSH bas, T3 élevé)"
            elif t4 is not None and t4 > 12.0:
                return True, "Hyperthyroïdie détectée (TSH bas, T4 élevé)"
        
        return False, None
    
    @staticmethod
    def score_metabolic(markers, stone_type, thyroid_data=None, calciemie=None):
        if markers is None:
            return 0, "Marqueurs métaboliques non renseignés"
        
        config = InferenceEngine.STONE_TYPES[stone_type]
        metabolic_marker = config['metabolic_marker']
        
        if metabolic_marker is None:
            base_score = 0
            reasons = []
        elif markers.get(metabolic_marker):
            base_score = 4
            reasons = [f"Marqueur signature présent ({metabolic_marker})"]
        else:
            base_score = 0
            reasons = []
        
        bonus_score = 0
        if thyroid_data and thyroid_data.get('tsh') is not None:
            is_hyperthyroid, thyroid_reason = InferenceEngine.detect_hyperthyroidism(
                thyroid_data.get('t3'), thyroid_data.get('t4'), thyroid_data.get('tsh')
            )
            if is_hyperthyroid and metabolic_marker == 'hypercalciurie':
                bonus_score += 1
                reasons.append(f"{thyroid_reason} → favorise hypercalciurie")
            elif thyroid_data.get('tsh') is not None and metabolic_marker == 'hypercalciurie':
                tsh_val = thyroid_data.get('tsh')
                t3_val = thyroid_data.get('t3')
                t4_val = thyroid_data.get('t4')
                thyroid_status = f"Hormones thyroïdiennes: TSH={tsh_val}"
                if t3_val:
                    thyroid_status += f", T3={t3_val}"
                if t4_val:
                    thyroid_status += f", T4={t4_val}"
                thyroid_status += " (normales)"
                reasons.append(thyroid_status)
        
        if calciemie and calciemie > 2.6 and metabolic_marker == 'hypercalciurie':
            bonus_score += 1
            reasons.append(f"Hypercalcémie détectée ({calciemie} mmol/L) → risque accru")
        
        total_score = base_score + bonus_score
        reason_text = "; ".join(reasons) if reasons else "Marqueur signature absent"
        
        return total_score, reason_text
    
    @staticmethod
    def score_infection(infection, stone_type):
        if infection is None:
            return 0, "Information infection non renseignée"
        
        config = InferenceEngine.STONE_TYPES[stone_type]
        
        if config['infection_favorable']:
            if infection:
                return 3, "Infection présente (favorable pour ce type)"
            else:
                return -1, "Absence d'infection (défavorable pour ce type)"
        else:
            if infection:
                return 0, "Infection présente (non caractéristique)"
            else:
                return 0, "Absence d'infection (neutre)"
    
    @staticmethod
    def score_radio_opacity(radio_opacity, stone_type):
        if radio_opacity is None or radio_opacity == 'inconnu':
            return 0, "Radio-opacité non renseignée"
        
        config = InferenceEngine.STONE_TYPES[stone_type]
        
        if radio_opacity.lower() == config['radio_opacite'].lower():
            return 1, f"Radio-opacité concordante ({radio_opacity})"
        else:
            return 0, f"Radio-opacité non concordante"
    
    @staticmethod
    def analyze_multilayer_structure(densite_noyau, densites_couches):
        from backend.services.inference_service import InferenceEngine as IE
        return IE.analyze_multilayer_structure(densite_noyau, densites_couches)
    
    @staticmethod
    def _identify_layer_composition(densite_uh):
        from backend.services.inference_service import InferenceEngine as IE
        return IE._identify_layer_composition(densite_uh)
    
    @staticmethod
    def infer_stone_type(imaging_data, biology_data):
        from backend.services.inference_service import InferenceEngine as IE
        return IE.infer_stone_type(imaging_data, biology_data)
    
    @staticmethod
    def _determine_treatment_route(taille, stone_type, uh, lec_eligible):
        if taille is None:
            return "Taille non renseignée - impossible de déterminer la voie"
        
        if taille < 10:
            routes = ["Traitement médical", "Surveillance"]
            if lec_eligible and uh and uh < 1000:
                routes.append("URS possible")
            elif lec_eligible:
                routes.append("LEC possible")
            return " / ".join(routes)
        
        elif 10 <= taille <= 20:
            if lec_eligible and uh and uh < 1500:
                return "LEC (première intention) / URS si échec"
            else:
                return "URS (première intention)"
        
        else:
            if 'coralliforme' in str(stone_type).lower():
                return "PCNL (calcul coralliforme)"
            else:
                return "PCNL / URS selon localisation"
