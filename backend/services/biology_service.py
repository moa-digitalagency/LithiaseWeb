def calculate_metabolic_booleans(biologie, sexe='M'):
    if biologie.oxalurie_valeur is not None:
        biologie.hyperoxalurie = biologie.oxalurie_valeur > 45
    else:
        biologie.hyperoxalurie = False
    
    if biologie.calciurie_valeur is not None:
        seuil_calciurie = 250 if sexe == 'F' else 300
        biologie.hypercalciurie = biologie.calciurie_valeur > seuil_calciurie
    else:
        biologie.hypercalciurie = False
    
    if biologie.calciemie_valeur is not None:
        biologie.hypercalcemie = biologie.calciemie_valeur > 2.6
    else:
        biologie.hypercalcemie = False
