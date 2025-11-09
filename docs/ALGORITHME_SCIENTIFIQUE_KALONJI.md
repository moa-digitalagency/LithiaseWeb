# Algorithme de Classification Morpho-Constitutionnelle Lithiasique KALONJI

## Documentation Scientifique et Médicale

**Version**: 1.0  
**Date**: Novembre 2025  
**Auteurs**: Équipe KALONJI  
**Classification**: Approche diagnostique non-invasive basée sur l'imagerie et la biologie

---

## Table des matières

1. [Introduction et justification scientifique](#1-introduction-et-justification-scientifique)
2. [Fondements physiopathologiques](#2-fondements-physiopathologiques)
3. [Méthodologie de classification](#3-méthodologie-de-classification)
4. [Système de notation quantitative](#4-système-de-notation-quantitative)
5. [Critères diagnostiques détaillés](#5-critères-diagnostiques-détaillés)
6. [Processus d'inférence étape par étape](#6-processus-dinférence-étape-par-étape)
7. [Interprétation des résultats](#7-interprétation-des-résultats)
8. [Conduite à tenir thérapeutique](#8-conduite-à-tenir-thérapeutique)
9. [Application manuelle de l'algorithme](#9-application-manuelle-de-lalgorithme)
10. [Limites et perspectives](#10-limites-et-perspectives)

---

## 1. Introduction et justification scientifique

### 1.1 Contexte clinique

La lithiase urinaire est une pathologie fréquente avec une prévalence de 10-15% dans les pays développés et des variations géographiques significatives. La composition chimique des calculs urinaires est déterminante pour:

- **Le pronostic de récidive** (30-50% à 5 ans pour les calculs calciques)
- **Le choix thérapeutique** (lithotripsie extracorporelle, urétéroscopie, néphrolithotomie percutanée)
- **La prévention secondaire** (traitement médical, modifications hygiéno-diététiques)

### 1.2 Problématique de la spectrophotométrie infrarouge

L'analyse spectrophotométrique infrarouge (SPIR) des calculs reste la référence diagnostique (sensibilité >95%, spécificité >98%). Cependant, elle présente plusieurs limitations:

- **Nécessité d'une expulsion ou extraction** du calcul
- **Délai d'analyse** (plusieurs jours à semaines)
- **Coût et accessibilité** limités dans certaines régions
- **Impossibilité d'analyse** des calculs non accessibles

### 1.3 Intérêt de l'approche prédictive non-invasive

L'algorithme KALONJI propose une **classification morpho-constitutionnelle prédictive** basée sur:

1. **Critères tomodensitométriques** (densité, morphologie, taille)
2. **Paramètres biologiques urinaires** (pH, densité, sédiment)
3. **Marqueurs métaboliques** (calciurie, oxalurie, uricurie)
4. **Contexte clinique** (infection, malformations, hormones thyroïdiennes)

Cette approche permet une **orientation diagnostique précoce** avant récupération du calcul, optimisant la prise en charge thérapeutique et préventive.

---

## 2. Fondements physiopathologiques

### 2.1 Types de calculs et leur pathogenèse

#### 2.1.1 Calculs oxalo-calciques (65-75% des cas)

**Whewellite (oxalate de calcium monohydraté - COM)**
- **Pathogenèse**: Hyperoxalurie primaire (génétique) ou secondaire (malabsorption intestinale, apport alimentaire excessif)
- **pH favorable**: Acide (5.0-5.8)
- **Morphologie**: Sphérique lisse ou irrégulière spiculée
- **Densité scanner**: 1200-1700 UH (très opaque)
- **Pronostic**: Récidive élevée (40-50% à 5 ans), résistance à la LEC

**Weddellite (oxalate de calcium dihydraté - COD)**
- **Pathogenèse**: Hypercalciurie idiopathique, hyperparathyroïdie
- **pH favorable**: Acide (5.0-5.8)
- **Morphologie**: Irrégulière spiculée (cristaux bipy ramidaux)
- **Densité scanner**: 1000-1450 UH (opaque)
- **Pronostic**: Meilleure fragmentation LEC que Whewellite

#### 2.1.2 Calculs phosphocalciques (10-15% des cas)

**Carbapatite (phosphate de calcium carbonaté)**
- **Pathogenèse**: Infections urinaires chroniques, pH alcalin, hypercalciurie
- **pH favorable**: Alcalin (6.8-7.5)
- **Morphologie**: Crayeuse, friable
- **Densité scanner**: 1300-1400 UH
- **Caractéristique**: Souvent associée aux infections

**Brushite (phosphate de calcium dihydraté)**
- **Pathogenèse**: Hyperparathyroïdie, acidose tubulaire rénale distale
- **pH favorable**: Neutre à légèrement alcalin (6.0-6.8)
- **Morphologie**: Irrégulière spiculée
- **Densité scanner**: 1550-2000 UH (très opaque, >Whewellite)
- **Pronostic**: Récidive très élevée, croissance rapide

#### 2.1.3 Calculs infectieux (10-15% des cas)

**Struvite (phosphate ammoniaco-magnésien)**
- **Pathogenèse**: Infection par germes à uréase (Proteus, Klebsiella, Pseudomonas)
- **Mécanisme**: Hydrolyse urée → ammoniaque → pH alcalin → précipitation phosphates
- **pH favorable**: Alcalin (6.8-7.5)
- **Morphologie**: Coralliforme (moule des cavités rénales)
- **Densité scanner**: 550-950 UH (faiblement opaque)
- **Pronostic**: Récidive si infection non contrôlée, risque septique

#### 2.1.4 Calculs uriques (5-10% des cas)

**Acide urique**
- **Pathogenèse**: Hyperuricurie (syndrome métabolique, alimentation riche en purines), pH acide chronique
- **pH favorable**: Acide (5.0-5.8)
- **Morphologie**: Sphérique lisse ou irrégulière
- **Densité scanner**: 350-650 UH (radiotransparent)
- **Particularité**: Seul calcul dissolvable par alcalinisation urinaire (pH>6.5)

**Urate d'ammonium**
- **Pathogenèse**: Diarrhées chroniques, maladies inflammatoires intestinales
- **pH favorable**: Alcalin (6.8-7.5)
- **Morphologie**: Sphérique lisse
- **Densité scanner**: 150-300 UH (très faiblement opaque)

#### 2.1.5 Calculs métaboliques rares (<5% des cas)

**Cystine**
- **Pathogenèse**: Cystinurie (maladie génétique autosomique récessive)
- **pH favorable**: Acide (5.0-5.8)
- **Morphologie**: Sphérique lisse, aspect "cireux"
- **Densité scanner**: 650-850 UH (faiblement opaque)
- **Diagnostic**: Cristaux hexagonaux pathognomoniques dans le sédiment urinaire
- **Pronostic**: Récidive constante, nécessite traitement à vie

### 2.2 Facteurs de risque lithogènes

| Facteur | Mécanisme | Types favorisés |
|---------|-----------|------------------|
| **Déshydratation chronique** | ↓Volume urinaire, ↑Concentration solutés | Tous types |
| **pH urinaire acide (<5.5)** | Précipitation acide urique, cystine, COM | Acide urique, Cystine, Whewellite |
| **pH urinaire alcalin (>7.0)** | Précipitation phosphates | Carbapatite, Struvite, Urate NH₄ |
| **Hyperoxalurie** | ↑Oxalate urinaire >45 mg/24h | Whewellite |
| **Hypercalciurie** | ↑Calcium urinaire >300 mg/24h (H), >250 (F) | Weddellite, Brushite |
| **Hyperuricurie** | ↑Acide urique >800 mg/24h | Acide urique |
| **Infections urinaires récidivantes** | Germes à uréase, pH alcalin | Struvite, Carbapatite |
| **Hyperthyroïdie** | Hypercalciurie, déminéralisation osseuse | Calculs calciques |
| **Malformations urinaires** | Stase urinaire, infections | Tous types infectieux |

---

## 3. Méthodologie de classification

### 3.1 Approche diagnostique multiparamétrique

L'algorithme KALONJI utilise une approche **multifactorielle quantitative** intégrant:

1. **Critères radiologiques** (tomodensitométrie sans injection)
2. **Critères biologiques** (analyse urinaire, biochimie)
3. **Critères cliniques** (anamnèse, contexte infectieux)

Cette triangulation permet de compenser les limites de chaque examen isolé et d'améliorer la spécificité diagnostique.

### 3.2 Système de scoring sur 21 points

Le score total est calculé par addition pondérée de 7 critères:

```
Score Total = Score_Densité(6) + Score_Morphologie(3) + Score_pH(3) + 
              Score_Métabolique(4+bonus) + Score_Infection(3) + 
              Score_Radioopacité(1) + Score_Malformations(1)
```

**Score maximum théorique**: 21 points (20 points de base + 1 point bonus malformations)

Le calcul est répété **pour chacun des 8 types de calculs**, générant un profil de compatibilité multidimensionnel.

### 3.3 Critère de décision

- **Type proposé**: Type ayant obtenu le score le plus élevé
- **Incertitude diagnostique**: Si Δ(Score₁ - Score₂) < 2 points → Résultat incertain, examens complémentaires recommandés
- **Top 3**: Les 3 types les mieux scorés sont rapportés avec justifications

---

## 4. Système de notation quantitative

### 4.1 Critère 1 - Densité tomodensitométrique (0-6 points)

**Justification scientifique**: La densité scanner en unités Hounsfield (UH) reflète directement la composition minérale du calcul. C'est le critère le plus discriminant.

#### Plages de densité caractéristiques

| Type de calcul | Plage typique (UH) | Physiopathologie |
|----------------|-------------------|------------------|
| Whewellite | 1200-1700 | Forte densité cristalline COM |
| Weddellite | 1000-1450 | Hydratation COD, densité moindre |
| Brushite | 1550-2000 | Très forte densité phosphocalcique |
| Carbapatite | 1300-1400 | Densité modérée phospho-calcique |
| Struvite | 550-950 | Faible densité (Mg-NH₄-PO₄) |
| Cystine | 650-850 | Densité intermédiaire |
| Acide urique | 350-650 | Radiotransparent (absence calcium) |
| Urate ammonium | 150-300 | Très faible densité |

#### Attribution des points

```
Si Densité_mesurée dans [UH_min, UH_max]:
    Points = 6  # Plage typique

Sinon:
    Δ = min(|Densité - UH_min|, |Densité - UH_max|)
    
    Si Δ ≤ 100 UH:
        Points = 4  # Plage proche
    Sinon Si Δ ≤ 200 UH:
        Points = 2  # Plage éloignée
    Sinon:
        Points = 0  # Hors plage caractéristique
```

**Exemple clinique**:
```
Patient avec densité mesurée = 1250 UH
- Whewellite [1200-1700]: 1250 dans plage → 6 points
- Weddellite [1000-1450]: 1250 dans plage → 6 points  
- Acide urique [350-650]: |1250-650|=600 → 0 point
- Struvite [550-950]: |1250-950|=300 → 0 point
```

### 4.2 Critère 2 - Morphologie du calcul (0-3 points)

**Justification scientifique**: La morphologie macroscopique reflète le mode de cristallisation et l'environnement physico-chimique de formation.

#### Morphologies caractéristiques

| Morphologie | Description | Types associés | Points |
|-------------|-------------|----------------|--------|
| **Sphérique lisse** | Surface régulière, cristallisation homogène | Whewellite, Cystine, Acide urique, Urate NH₄ | 3 (signature) ou 1 (compatible) |
| **Irrégulière spiculée** | Surface rugueuse, cristaux en aiguilles | Weddellite, Brushite, Struvite | 3 (signature) ou 1 (compatible) |
| **Crayeuse** | Aspect friable, surface mate | Carbapatite | 3 (signature) |
| **Coralliforme** | Ramifications multiples, moule caliciel | Struvite | 3 (signature) |
| **Hétérogène** | Composition mixte visible | Tous (compatible) | 1 (compatible) |

#### Attribution des points

```
Si Morphologie_observée dans Morphologies_signatures[Type]:
    Points = 3  # Morphologie pathognomonique
Sinon Si Morphologie_observée dans Morphologies_compatibles[Type]:
    Points = 1  # Morphologie compatible
Sinon:
    Points = 0  # Morphologie non caractéristique
```

### 4.3 Critère 3 - pH urinaire (0-3 points)

**Justification scientifique**: Le pH urinaire détermine la solubilité des différents cristaux. C'est un facteur physico-chimique majeur de la lithogenèse.

#### Plages de pH favorables

| Type de calcul | pH favorable | Explication physico-chimique |
|----------------|--------------|------------------------------|
| Whewellite, Weddellite | 5.0-5.8 | Précipitation CaOx en milieu acide |
| Cystine | 5.0-5.8 | Précipitation cystine si pH<7.0 |
| Acide urique | 5.0-5.8 | Forme non-ionisée insoluble en milieu acide |
| Brushite | 6.0-6.8 | Précipitation CaHPO₄ en milieu neutre |
| Carbapatite | 6.8-7.5 | Précipitation Ca₃(PO₄)₂ en milieu alcalin |
| Struvite | 6.8-7.5 | Formation MgNH₄PO₄ si pH>7.0 |
| Urate ammonium | 6.8-7.5 | Précipitation urate en milieu alcalin |

#### Attribution des points

```
Si pH_mesuré dans [pH_min, pH_max] pour le type:
    Points = 3  # pH favorable à la cristallisation
Sinon:
    Δ_pH = min(|pH_mesuré - pH_min|, |pH_mesuré - pH_max|)
    
    Si Δ_pH ≤ 0.5:
        Points = 1  # pH proche de la plage
    Sinon:
        Points = 0  # pH défavorable
```

**Exemple clinique**:
```
Patient avec pH urinaire = 5.2
- Acide urique [5.0-5.8]: 5.2 dans plage → 3 points ✓
- Whewellite [5.0-5.8]: 5.2 dans plage → 3 points ✓
- Struvite [6.8-7.5]: |5.2-6.8|=1.6 → 0 point ✗
- Carbapatite [6.8-7.5]: |5.2-6.8|=1.6 → 0 point ✗
```

### 4.4 Critère 4 - Marqueurs métaboliques (0-4 points + bonus)

**Justification scientifique**: Les troubles métaboliques sont les facteurs étiologiques majeurs de la lithiase. Leur détection oriente directement vers le type de calcul.

#### Score de base (0-4 points)

| Marqueur métabolique | Seuil pathologique | Type associé | Points |
|----------------------|-------------------|--------------|--------|
| **Hyperoxalurie** | >45 mg/24h | Whewellite | 4 |
| **Hypercalciurie** | >300 mg/24h (H), >250 (F) | Weddellite, Brushite, Carbapatite | 4 |
| **Hyperuricurie** | >800 mg/24h | Acide urique | 4 |
| **Cystinurie** | Cristaux hexagonaux | Cystine | 4 |

#### Points bonus (0-2 points supplémentaires)

**Hyperthyroïdie** (+2 points pour calculs calciques):
```
Si TSH < 0.4 mUI/L ET (T3 > 2.0 pg/mL OU T4 > 12.0 ng/dL):
    Hyperthyroïdie détectée
    Si Type ∈ {Whewellite, Weddellite, Brushite, Carbapatite}:
        Points_bonus = +2
```

**Hypercalcémie** (+1 point pour calculs calciques):
```
Si Calciémie > 2.60 mmol/L:
    Si Type ∈ {Whewellite, Weddellite, Brushite, Carbapatite}:
        Points_bonus = +1
```

### 4.5 Critère 5 - Infection urinaire (-1 à +3 points)

**Justification scientifique**: Les infections urinaires à germes uréasiques favorisent les calculs infectieux. Leur absence rend ces calculs improbables.

#### Attribution des points

```
Si Infection_urinaire présente:
    Si Germe_urease_positif (Proteus, Klebsiella, Pseudomonas):
        Si Type ∈ {Struvite, Carbapatite, Urate ammonium}:
            Points = +3  # Infection favorise ces types
        Sinon:
            Points = 0
    Sinon (E.coli, Enterococcus):
        Si Type ∈ {Struvite, Carbapatite}:
            Points = +2  # Infection compatible
        Sinon:
            Points = 0

Sinon (Absence d'infection):
    Si Type ∈ {Struvite, Carbapatite, Urate ammonium}:
        Points = -1  # Infection quasi-nécessaire pour ces types
    Sinon:
        Points = 0
```

### 4.6 Critère 6 - Radio-opacité (0-1 point)

**Justification scientifique**: La radio-opacité à l'ASP reflète la teneur en calcium du calcul.

#### Attribution des points

| Type | Radio-opacité attendue | Points si concordance |
|------|------------------------|----------------------|
| Whewellite, Weddellite, Brushite, Carbapatite | Opaque | +1 |
| Struvite, Cystine, Acide urique, Urate ammonium | Transparent | +1 |

```
Si Radio_opacité_observée == Radio_opacité_attendue[Type]:
    Points = 1
Sinon:
    Points = 0
```

### 4.7 Critère 7 - Malformations urinaires (0-1 point)

**Justification scientifique**: Les malformations urinaires (duplicité, ectasie, reflux) favorisent la stase urinaire et les infections, prédisposant aux calculs infectieux.

#### Attribution des points

```
Si Malformations_urinaires présentes:
    Si Type ∈ {Struvite, Carbapatite, Urate ammonium}:
        Points = +1  # Facteur favorisant
    Sinon:
        Points = 0
Sinon:
    Points = 0
```

---

## 5. Critères diagnostiques détaillés

### 5.1 Données d'imagerie requises

#### Tomodensitométrie rénale sans injection (protocole lithiase)

**Paramètres d'acquisition recommandés**:
- Collimation: 1-2 mm
- Tension: 120-140 kVp
- Courant: 200-400 mAs (adapté à la corpulence)
- Reconstruction: Coupes fines 1-3 mm

**Mesures à effectuer**:

1. **Densité du calcul (UH)**:
   - Mesure du noyau (zone la plus dense)
   - ROI (Region of Interest) de 1-2 mm²
   - Moyenne sur 3 mesures si calcul hétérogène
   - Éviter les artéfacts de volume partiel

2. **Dimensions**:
   - Diamètre longitudinal (grand axe)
   - Diamètre transversal (petit axe)
   - Taille effective = max(diamètres) pour conduite thérapeutique

3. **Morphologie**:
   - Forme globale: sphérique, ovale, irrégulière, coralliforme
   - Surface: lisse, rugueuse, spiculée, crayeuse
   - Homogénéité: homogène, hétérogène, stratifié

4. **Localisation**:
   - Rein (calice supérieur/moyen/inférieur, bassinet)
   - Uretère (proximal/moyen/distal)
   - Vessie

5. **Radio-opacité à l'ASP** (si disponible):
   - Opaque (visible à la radiographie simple)
   - Transparent (invisible à l'ASP)

6. **Retentissement haut appareil**:
   - Dilatation pyélo-calicielle (grade 0-IV)
   - Épaisseur du parenchyme rénal
   - Volume rénal

7. **Malformations associées**:
   - Duplicité urétérale
   - Rein en fer à cheval
   - Ectasie pyélo-calicielle
   - Reflux vésico-urétéral
   - Diverticules caliciels

### 5.2 Données biologiques requises

#### Analyse urinaire (échantillon frais <2h)

1. **pH urinaire** (pH-mètre ou bandelette):
   - Mesure sur échantillon frais
   - Idéalement sur miction du matin à jeun
   - Répéter sur 3 jours si possible

2. **Densité urinaire** (réfractomètre):
   - Reflète l'état d'hydratation
   - Normale: 1.010-1.025
   - Hyperdensité >1.030: déshydratation

3. **Sédiment urinaire** (microscope optique x400):
   - Type de cristaux:
     * Oxalate de calcium (enveloppe, octaèdres)
     * Acide urique (rosettes, losanges)
     * Phosphates (cercueils, étoiles)
     * Cystine (hexagones pathognomoniques)
   - Quantité: rares, modérés, nombreux, abondants

4. **ECBU** (examen cytobactériologique):
   - Leucocyturie (seuil: 10⁴/mL)
   - Bactériurie (seuil: 10⁵/mL)
   - Identification du germe
   - Antibiogramme

#### Biochimie urinaire des 24h (recueil complet)

**Marqueurs principaux**:

1. **Calciurie** (mg/24h):
   - Normal: <300 mg/24h (homme), <250 mg/24h (femme)
   - Hypercalciurie si dépassement seuil
   - Corriger par créatininurie: ratio Ca/créat <0.20

2. **Oxalurie** (mg/24h):
   - Normal: <45 mg/24h
   - Hyperoxalurie modérée: 45-80 mg/24h
   - Hyperoxalurie sévère: >80 mg/24h

3. **Uricurie** (mg/24h):
   - Normal: <800 mg/24h
   - Hyperuricurie si >800 mg/24h

4. **Citraturie** (mg/24h):
   - Normal: >320 mg/24h
   - Hypocitraturie si <320 mg/24h (facteur lithogène)

5. **Créatininurie** (mmol/24h):
   - Contrôle qualité du recueil des 24h
   - Attendu: 8-15 mmol/24h (homme), 6-12 mmol/24h (femme)

6. **Volume urinaire 24h**:
   - Optimal: >2000 mL/24h
   - Facteur de risque si <1500 mL/24h

#### Biochimie sanguine

1. **Fonction rénale**:
   - Créatininémie (μmol/L)
   - Calcul DFG (CKD-EPI ou Cockroft)
   - Urée (mmol/L)

2. **Métabolisme phosphocalcique**:
   - Calcémie (mmol/L): Normal 2.20-2.60
   - Phosphorémie (mmol/L): Normal 0.85-1.45
   - PTH (pg/mL): Normal 15-65
   - 25-OH vitamine D (ng/mL): Optimal >30

3. **Hormones thyroïdiennes**:
   - TSH (mUI/L): Normal 0.4-4.0
   - T3 libre (pg/mL): Normal 1.8-4.2
   - T4 libre (ng/dL): Normal 0.8-2.0
   - Recherche hyperthyroïdie (hypercalciurie secondaire)

4. **Métabolisme urique**:
   - Uricémie (μmol/L): Normal <420 (H), <360 (F)

### 5.3 Données cliniques

#### Anamnèse

- **Antécédents personnels**:
  * Épisodes lithiasiques antérieurs (nombre, dates, traitements)
  * Pathologies métaboliques (diabète, goutte, obésité)
  * Maladies digestives (Crohn, RCH, résections intestinales)
  * Hyperparathyroïdie, acidose tubulaire rénale
  
- **Antécédents familiaux**:
  * Lithiase familiale (parents, fratrie)
  * Maladies métaboliques héréditaires

- **Habitudes de vie**:
  * Hydratation quotidienne (L/jour)
  * Alimentation (protéines animales, sel, oxalates, purines)
  * Activité physique
  * Exposition climatique (déshydratation)

- **Traitements en cours**:
  * Diurétiques thiazidiques (↓calciurie)
  * Inhibiteurs de la pompe à protons (↓absorption calcium)
  * Suppléments calciques, vitamine D
  * Allopurinol (↓uricurie)

---

## 6. Processus d'inférence étape par étape

### 6.1 Étape 1 - Collecte et vérification des données

#### Checklist des données minimales requises

**Données ESSENTIELLES** (si manquantes: résultat incomplet):
- [ ] Densité scanner (UH)
- [ ] pH urinaire
- [ ] Taille du calcul (mm)

**Données IMPORTANTES** (améliorent la spécificité):
- [ ] Morphologie du calcul
- [ ] Radio-opacité à l'ASP
- [ ] ECBU (infection oui/non, germe)
- [ ] Marqueurs métaboliques (calciurie, oxalurie, uricurie)

**Données COMPLÉMENTAIRES** (affinent le diagnostic):
- [ ] Sédiment urinaire (type de cristaux)
- [ ] Hormones thyroïdiennes (TSH, T3, T4)
- [ ] Calcémie
- [ ] Malformations urinaires

#### Contrôle de cohérence

Vérifier les incohérences flagrantes:

```
Si Densité <500 UH ET Radio_opacité=="opaque":
    ⚠️ INCOHÉRENCE: Calcul peu dense devrait être transparent
    
Si pH<6.0 ET Infection_à_germe_uréasique présente:
    ⚠️ INCOHÉRENCE: Infection à uréase devrait alcaliniser les urines
    
Si Calcémie>2.80 mmol/L:
    ⚠️ URGENCE: Hypercalcémie sévère, bilan parathyroïdien urgent
```

### 6.2 Étape 2 - Calcul du score pour chaque type

**Algorithme de scoring**:

```python
# Pseudo-code de l'inférence

POUR chaque Type_calcul dans [Whewellite, Weddellite, Carbapatite, 
                              Brushite, Struvite, Cystine, 
                              Acide_urique, Urate_ammonium]:
    
    Score_total[Type] = 0
    Justifications[Type] = []
    
    # 1. Score densité (0-6 points)
    points, raison = calculer_score_densite(Densite_UH, Type)
    Score_total[Type] += points
    SI points > 0: Justifications[Type].ajouter(raison)
    
    # 2. Score morphologie (0-3 points)
    points, raison = calculer_score_morphologie(Morphologie, Type)
    Score_total[Type] += points
    SI points > 0: Justifications[Type].ajouter(raison)
    
    # 3. Score pH (0-3 points)
    points, raison = calculer_score_pH(pH_urinaire, Type)
    Score_total[Type] += points
    SI points > 0: Justifications[Type].ajouter(raison)
    
    # 4. Score métabolique (0-4 points + bonus)
    points, raison = calculer_score_metabolique(
        Hyperoxalurie, Hypercalciurie, Hyperuricurie, Cystinurie,
        TSH, T3, T4, Calciemie, Type
    )
    Score_total[Type] += points
    SI points > 0: Justifications[Type].ajouter(raison)
    
    # 5. Score infection (-1 à +3 points)
    points, raison = calculer_score_infection(
        Infection, Germe, Urease_positif, Type
    )
    Score_total[Type] += points
    SI points != 0: Justifications[Type].ajouter(raison)
    
    # 6. Score radio-opacité (0-1 point)
    points, raison = calculer_score_radioopacite(Radio_opacite, Type)
    Score_total[Type] += points
    SI points > 0: Justifications[Type].ajouter(raison)
    
    # 7. Score malformations (0-1 point)
    points, raison = calculer_score_malformations(Malformations, Type)
    Score_total[Type] += points
    SI points > 0: Justifications[Type].ajouter(raison)

FIN POUR
```

**Détail des fonctions de scoring**:

```python
FONCTION calculer_score_densite(uh, type_calcul):
    SI uh est NULL:
        RETOURNER (0, "Densité non renseignée")
    
    uh_min, uh_max = PLAGES_DENSITE[type_calcul]
    
    SI uh_min ≤ uh ≤ uh_max:
        raison = f"Densité {uh} UH dans plage typique [{uh_min}-{uh_max}]"
        RETOURNER (6, raison)
    
    delta = min(|uh - uh_min|, |uh - uh_max|)
    
    SI delta ≤ 100:
        raison = f"Densité {uh} UH proche de la plage (Δ={delta} UH)"
        RETOURNER (4, raison)
    SINON SI delta ≤ 200:
        raison = f"Densité {uh} UH éloignée de la plage (Δ={delta} UH)"
        RETOURNER (2, raison)
    SINON:
        RETOURNER (0, "")

FONCTION calculer_score_metabolique(hyperox, hypercalc, hyperuric, cystin, 
                                     tsh, t3, t4, calciemie, type_calcul):
    points = 0
    raisons = []
    
    marqueur_signature = MARQUEUR_METABOLIQUE[type_calcul]
    
    # Score de base (0-4 points)
    SI marqueur_signature == "hyperoxalurie" ET hyperox == VRAI:
        points += 4
        raisons.ajouter("Hyperoxalurie (marqueur signature)")
    SINON SI marqueur_signature == "hypercalciurie" ET hypercalc == VRAI:
        points += 4
        raisons.ajouter("Hypercalciurie (marqueur signature)")
    SINON SI marqueur_signature == "hyperuricurie" ET hyperuric == VRAI:
        points += 4
        raisons.ajouter("Hyperuricurie (marqueur signature)")
    SINON SI marqueur_signature == "cystinurie" ET cystin == VRAI:
        points += 4
        raisons.ajouter("Cystinurie (pathognomonique)")
    
    # Bonus hyperthyroïdie (+2 points pour calculs calciques)
    SI tsh < 0.4 ET (t3 > 2.0 OU t4 > 12.0):
        SI type_calcul dans [Whewellite, Weddellite, Brushite, Carbapatite]:
            points += 2
            raisons.ajouter("Hyperthyroïdie (hypercalciurie secondaire)")
    
    # Bonus hypercalcémie (+1 point pour calculs calciques)
    SI calciemie > 2.60:
        SI type_calcul dans [Whewellite, Weddellite, Brushite, Carbapatite]:
            points += 1
            raisons.ajouter(f"Hypercalcémie ({calciemie} mmol/L)")
    
    raison_finale = ", ".join(raisons) SI raisons SINON ""
    RETOURNER (points, raison_finale)
```

### 6.3 Étape 3 - Classement et sélection

```python
# Trier les types par score décroissant
Classement = trier_par_score_decroissant(Score_total)

# Extraire le Top 3
Top_1 = Classement[0]  # Type le plus probable
Top_2 = Classement[1]  # 2ème type
Top_3 = Classement[2]  # 3ème type

# Calcul de la différence de score
Delta_score = Score_total[Top_1] - Score_total[Top_2]
```

### 6.4 Étape 4 - Détection d'incertitude diagnostique

```python
SI Delta_score < 2:
    Resultat_incertain = VRAI
    Message_alerte = "⚠️ RÉSULTAT INCERTAIN : Différence de score <2 points"
    
    # Recommandations d'examens complémentaires
    SI Top_1 == "Whewellite" ET Top_2 == "Weddellite":
        Recommandation = "Doser oxalurie et calciurie des 24h"
    
    SI Top_1 == "Acide urique" ET Top_2 == "Struvite":
        Recommandation = "Vérifier ECBU et uricosurie des 24h"
    
    SI Top_1 dans [Brushite, Carbapatite]:
        Recommandation = "Bilan phosphocalcique (PTH, vitamine D)"
    
    SI Top_1 == "Cystine":
        Recommandation = "Rechercher cristaux hexagonaux dans sédiment"

SINON:
    Resultat_incertain = FAUX
```

### 6.5 Étape 5 - Détermination du type de composition

```python
SI Score_total[Top_1] ≥ 12 ET Delta_score ≥ 4:
    Type_composition = "PURE"
    Explication = "Score élevé (≥12) et écart significatif (≥4) → Composition probablement pure"

SINON SI Score_total[Top_1] < 10 OU Delta_score < 2:
    Type_composition = "MIXTE PROBABLE"
    
    SI Delta_score < 2:
        Explication = f"Écart faible entre {Top_1} et {Top_2} → Composition mixte probable"
        Composition_detail = f"{Top_1} + {Top_2} (mixte)"
    SINON:
        Explication = "Score global faible → Composition mixte ou atypique possible"
        Composition_detail = f"{Top_1} (prédominant, mixte possible)"

SINON:
    Type_composition = "PURE PROBABLE"
    Explication = "Score modéré mais type dominant clair"
    Composition_detail = Top_1
```

### 6.6 Étape 6 - Génération des recommandations thérapeutiques

#### Éligibilité à la lithotripsie extracorporelle (LEC)

```python
FONCTION determiner_eligibilite_LEC(type_calcul, taille_mm, densite_uh):
    
    # Types favorables à la LEC
    types_LEC_favorables = [Weddellite, Carbapatite, Struvite]
    
    # Types défavorables à la LEC
    types_LEC_defavorables = [Whewellite, Brushite, Cystine, 
                               Acide_urique, Urate_ammonium]
    
    SI type_calcul dans types_LEC_favorables:
        SI taille_mm ≤ 20 ET densite_uh < 1500:
            RETOURNER ("Oui", "Type favorable + taille/densité compatibles")
        SINON SI taille_mm > 20:
            RETOURNER ("Non", "Taille >20mm: PCNL ou URS préférable")
        SINON SI densite_uh ≥ 1500:
            RETOURNER ("Non", "Densité élevée (≥1500 UH): fragmentation difficile")
    
    SI type_calcul dans types_LEC_defavorables:
        RETOURNER ("Non", f"{type_calcul} résiste à la LEC")
    
    RETOURNER ("Indéterminé", "Discuter en RCP")
```

#### Voie de traitement recommandée

```python
FONCTION determiner_voie_traitement(type_calcul, taille_mm, densite_uh, 
                                     localisation, morphologie):
    
    # Calculs <10mm
    SI taille_mm < 10:
        SI type_calcul == "Acide urique":
            RETOURNER "Dissolution médicale (alcalinisation pH>6.5)"
        SINON SI type_calcul == "Cystine":
            RETOURNER "Dissolution médicale (alcalinisation pH>7.5 + chélateurs)"
        SINON:
            SI eligibilite_LEC == "Oui":
                RETOURNER "Surveillance ou LEC si symptomatique"
            SINON:
                RETOURNER "Surveillance ou traitement médical expulsif"
    
    # Calculs 10-20mm
    SI 10 ≤ taille_mm ≤ 20:
        SI eligibilite_LEC == "Oui" ET densite_uh < 1500:
            RETOURNER "LEC en première intention"
        SINON:
            RETOURNER "URS (urétéroscopie) en première intention"
    
    # Calculs >20mm
    SI taille_mm > 20:
        SI morphologie == "coralliforme":
            RETOURNER "PCNL (néphrolithotomie percutanée) + traitement adjuvant"
        SINON SI localisation dans [calice_inferieur, bassinet]:
            RETOURNER "PCNL ou URS selon expertise centre"
        SINON:
            RETOURNER "Discuter PCNL vs URS en RCP"
    
    RETOURNER "Avis urologique spécialisé"
```

### 6.7 Étape 7 - Conseils de prévention personnalisés

```python
FONCTION generer_conseils_prevention(type_calcul, marqueurs_metaboliques, 
                                      pH_urinaire, volume_urinaire):
    
    conseils = []
    
    # Conseils généraux (tous types)
    conseils.ajouter("Augmenter hydratation à >2.5 L/jour (urines claires)")
    
    SI volume_urinaire < 1500:
        conseils.ajouter("⚠️ PRIORITÉ: Corriger déshydratation chronique")
    
    # Conseils spécifiques par type
    SI type_calcul == "Whewellite":
        conseils.ajouter("Limiter aliments riches en oxalate (épinards, rhubarbe, chocolat)")
        conseils.ajouter("Maintenir apport calcique normal (1000 mg/jour)")
        SI pH_urinaire < 6.0:
            conseils.ajouter("Alcaliniser urines (citrate de potassium)")
    
    SI type_calcul == "Weddellite":
        conseils.ajouter("Réduire apport sodé (<5 g/jour)")
        conseils.ajouter("Limiter protéines animales (100-120 g/jour)")
        SI hypercalciurie:
            conseils.ajouter("Envisager thiazidique si hypercalciurie persistante")
    
    SI type_calcul == "Acide urique":
        conseils.ajouter("Limiter aliments riches en purines (viandes rouges, abats)")
        conseils.ajouter("Alcaliniser urines (objectif pH 6.5-7.0)")
        conseils.ajouter("Envisager allopurinol si hyperuricurie >800 mg/24h")
        SI pH_urinaire < 6.0:
            conseils.ajouter("⚠️ URGENT: Alcalinisation pour dissolution")
    
    SI type_calcul == "Struvite":
        conseils.ajouter("⚠️ PRIORITÉ: Éradication infections urinaires")
        conseils.ajouter("ECBU de contrôle tous les 3 mois")
        conseils.ajouter("Antibioprophylaxie si infections récidivantes")
        conseils.ajouter("Rechercher malformations urinaires favorisantes")
    
    SI type_calcul == "Cystine":
        conseils.ajouter("⚠️ Hydratation massive (>3 L/jour)")
        conseils.ajouter("Alcaliniser urines (objectif pH >7.5)")
        conseils.ajouter("Traitement chélateur (tiopronine ou pénicillamine)")
        conseils.ajouter("Régime pauvre en méthionine")
    
    SI type_calcul == "Brushite":
        conseils.ajouter("Bilan parathyroïdien (recherche hyperparathyroïdie)")
        conseils.ajouter("Limiter apport en phosphore")
        conseils.ajouter("Contrôle vitamine D")
    
    SI type_calcul == "Carbapatite":
        conseils.ajouter("Traiter infections urinaires récidivantes")
        conseils.ajouter("Bilan phosphocalcique complet")
    
    SI type_calcul == "Urate ammonium":
        conseils.ajouter("Traiter diarrhées chroniques (bilan digestif)")
        conseils.ajouter("Contrôle infections urinaires")
    
    RETOURNER conseils
```

---

## 7. Interprétation des résultats

### 7.1 Rapport d'inférence type

Le rapport généré par l'algorithme contient:

#### Section 1 - Résultat principal

```
┌─────────────────────────────────────────────────────────────┐
│ RÉSULTAT DE L'ANALYSE MORPHO-CONSTITUTIONNELLE              │
├─────────────────────────────────────────────────────────────┤
│ Type proposé: Whewellite (oxalate de calcium monohydraté)   │
│ Score: 16/21 points                                          │
│ Composition: PURE PROBABLE                                   │
│ Certitude: ÉLEVÉE (Δ score = 5 points avec 2ème type)       │
└─────────────────────────────────────────────────────────────┘
```

#### Section 2 - Justifications détaillées

```
═══════════════════════════════════════════════════════════════
CRITÈRES DIAGNOSTIQUES RETENUS
═══════════════════════════════════════════════════════════════
✓ Densité scanner: 1350 UH (plage typique 1200-1700) → 6 pts
✓ Morphologie: Sphérique lisse (signature) → 3 pts
✓ pH urinaire: 5.6 (plage favorable 5.0-5.8) → 3 pts
✓ Hyperoxalurie: 62 mg/24h (marqueur signature) → 4 pts
✓ Absence d'infection urinaire (favorable) → 0 pts
✗ Radio-opacité: Transparent (attendu opaque) → 0 pts
═══════════════════════════════════════════════════════════════
```

#### Section 3 - Top 3 types probables

```
┌────────────────────────────────────────────────────────┐
│ CLASSEMENT DES TYPES PROBABLES                         │
├────────────────────────────────────────────────────────┤
│ 1. Whewellite               16/21 ████████████████░░   │
│ 2. Weddellite               11/21 ███████████░░░░░░░   │
│ 3. Acide urique              7/21 ███████░░░░░░░░░░░   │
└────────────────────────────────────────────────────────┘
```

#### Section 4 - Conduite à tenir

```
═══════════════════════════════════════════════════════════════
RECOMMANDATIONS THÉRAPEUTIQUES
═══════════════════════════════════════════════════════════════
Éligibilité LEC: NON (Whewellite résiste à la fragmentation)
Voie de traitement: URS (urétéroscopie) en première intention
Taille: 12mm → Extraction active recommandée
═══════════════════════════════════════════════════════════════
```

#### Section 5 - Prévention

```
═══════════════════════════════════════════════════════════════
CONSEILS DE PRÉVENTION PERSONNALISÉS
═══════════════════════════════════════════════════════════════
1. Augmenter hydratation à >2.5 L/jour (urines claires)
2. Limiter aliments riches en oxalate:
   - Épinards, rhubarbe, oseille
   - Chocolat noir, cacao
   - Cacahuètes, noix de cajou
   - Thé noir fort
3. Maintenir apport calcique normal (1000 mg/jour)
   → Ne PAS supprimer les laitages
4. Alcaliniser les urines (citrate de potassium 30-60 mEq/j)
5. Contrôler oxalurie à 6 mois
═══════════════════════════════════════════════════════════════
```

### 7.2 Interprétation du score

#### Score ≥ 15/21: Diagnostic de haute probabilité

- Concordance excellente des critères
- Composition pure très probable
- Conduite thérapeutique claire

**Action**: Appliquer directement les recommandations

#### Score 10-14/21: Diagnostic probable

- Concordance satisfaisante
- Composition pure probable ou mixte avec type dominant
- Demander examens complémentaires si disponibles

**Action**: Recommandations applicables, surveillance rapprochée

#### Score 7-9/21: Diagnostic incertain

- Concordance partielle
- Composition probablement mixte
- Différence faible avec autres types

**Action**: 
- Demander dosages métaboliques manquants
- Envisager spectrophotométrie infrarouge après récupération
- Appliquer conseils préventifs généraux

#### Score <7/21: Diagnostic très incertain

- Faible concordance
- Composition atypique ou données insuffisantes
- Risque d'erreur diagnostique élevé

**Action**:
- Compléter le bilan (imagerie, biologie)
- Attendre récupération du calcul pour analyse SPIR
- Conseils préventifs généraux uniquement

### 7.3 Gestion de l'incertitude diagnostique

#### Cas 1: Score proche entre 2 types (Δ <2)

**Exemple**: Whewellite 14 pts vs Weddellite 13 pts

```
⚠️ RÉSULTAT INCERTAIN
Les deux types d'oxalate de calcium sont possibles.

EXAMENS COMPLÉMENTAIRES RECOMMANDÉS:
- Oxalurie des 24h (si >60 mg/24h → Whewellite)
- Calciurie des 24h (si >300 mg/24h → Weddellite)
- Ratio oxalate/calcium urinaire

EN ATTENTE DU BILAN:
- Conseils communs oxalate de calcium
- Hydratation >2.5 L/jour
- Limiter oxalates alimentaires
```

#### Cas 2: Score faible pour tous les types (<10)

**Exemple**: Meilleur score 8 pts (Carbapatite)

```
⚠️ DONNÉES INSUFFISANTES ou COMPOSITION ATYPIQUE

CAUSES POSSIBLES:
1. Données manquantes (pH, marqueurs métaboliques)
2. Composition mixte complexe
3. Type rare non couvert par l'algorithme

CONDUITE À TENIR:
1. Compléter le bilan biologique
2. Répéter imagerie scanner haute résolution
3. Récupérer le calcul pour analyse SPIR (référence)
4. Appliquer conseils préventifs généraux:
   - Hydratation >2.5 L/jour
   - Réduction sel et protéines animales
   - pH urinaire 6.0-6.5
```

#### Cas 3: Incohérence flagrante

**Exemple**: Densité 1400 UH + Radio-opacité transparente

```
❌ INCOHÉRENCE DÉTECTÉE

Densité >1200 UH incompatible avec radiotransparence.

VÉRIFICATIONS À EFFECTUER:
1. Revoir mesures densitométriques (ROI, artéfacts)
2. Vérifier qualité de l'ASP (technique, centrage)
3. Éliminer calcul sur trajet (urétère vs vaisseau)

RECOMMANDATION:
Avis radiologique spécialisé avant interprétation.
```

---

## 8. Conduite à tenir thérapeutique

### 8.1 Arbre décisionnel thérapeutique

```
                        CALCUL URINAIRE DIAGNOSTIQUÉ
                                    │
                    ┌───────────────┴───────────────┐
                    │                               │
              Taille <10mm                    Taille ≥10mm
                    │                               │
        ┌───────────┴────────────┐         ┌────────┴────────┐
        │                        │         │                 │
   Symptomatique          Asymptomatique  10-20mm         >20mm ou
   ou Obstructif          (découverte)       │          coralliforme
        │                        │            │                │
   ┌────┴────┐              Surveillance   ┌─┴──┐           PCNL
   │         │              3-6 mois       │    │         (± adjuvant)
Dissolution  Extraction                  LEC  URS
 médicale    active                    éligible? │
   │           │                          │      │
(Acide     (URS ou                      Oui    Non
 urique,    LEC selon                    │      │
 Cystine)   type)                       LEC    URS
                                      (si Densité
                                       <1500 UH)
```

### 8.2 Dissolution médicale (calculs radiotransparents)

#### Acide urique

**Indications**:
- Calcul <15mm
- Radiotransparent confirmé (ASP + scanner <500 UH)
- Fonction rénale préservée
- Absence d'obstruction complète

**Protocole d'alcalinisation**:
```
Objectif pH urinaire: 6.5-7.0
Traitement: Citrate de potassium 30-90 mEq/jour
           (adapter selon pH urinaire x3/jour)

Jour 1-7:   30 mEq/jour (10+10+10) → Contrôle pH J7
Jour 8-14:  60 mEq/jour (20+20+20) si pH<6.5
Jour 15+:   90 mEq/jour si pH<6.5

Surveillance:
- pH urinaire quotidien (bandelettes)
- Scanner de contrôle à 1 mois puis tous les 2 mois
- Arrêt si disparition complète du calcul

Durée attendue de dissolution: 1-6 mois selon taille
```

**Critères d'échec** (→ traitement chirurgical):
- Absence de réduction taille à 3 mois
- Augmentation de taille
- Complications (infection, obstruction)

#### Cystine

**Indications**:
- Calcul <10mm
- Diagnostic confirmé (cristaux hexagonaux)
- Compliance patient excellente

**Protocole de dissolution**:
```
Hydratation: >3 L/jour (répartis sur 24h, y compris nuit)
Objectif pH: >7.5

Traitement:
- Citrate de potassium 60-120 mEq/jour
- Tiopronine 800-2000 mg/jour (chélateur de cystine)
  OU Pénicillamine si intolérance tiopronine

Surveillance:
- pH urinaire x 3/jour
- Cystinurie tous les 3 mois
- Scanner tous les 6 mois

Critères de succès:
- Cystinurie <250 mg/L
- pH >7.5 stable
- Réduction taille du calcul
```

### 8.3 Lithotripsie extracorporelle (LEC)

#### Types favorables

| Type | Éligibilité | Taux de succès | Remarques |
|------|-------------|----------------|-----------|
| Weddellite | +++++ | 70-85% | Excellent candidat |
| Carbapatite | ++++ | 65-75% | Bon candidat |
| Struvite | +++ | 60-70% | Bon candidat, risque septique |
| Acide urique | ++ | 50-65% | Dissolution préférable si <15mm |
| Cystine | + | 30-45% | Mauvais candidat, nombreuses séances |
| Whewellite | - | 20-40% | Résistant, nombreuses séances |
| Brushite | - | 15-30% | Très résistant |

#### Contre-indications

**Absolues**:
- Grossesse
- Troubles de coagulation non corrigés
- Obstruction en aval du calcul (sténose urétérale)
- Anévrisme aortique abdominal >4cm sur trajet de l'onde

**Relatives**:
- Obésité morbide (IMC >40)
- Malformations squelettiques (accès impossible)
- Calcul >20mm (taux d'échec élevé)
- Densité >1500 UH (fragmentation difficile)
- Infection urinaire active non contrôlée

#### Protocole LEC

```
Préparation:
- ECBU stérile (<48h)
- INR <1.5, plaquettes >100000
- Arrêt antiagrégants 5-7j avant

Procédure:
- Analgésie IV ou générale selon centre
- Localisation calcul (échographie ou scopie)
- 2000-3000 chocs à 14-18 kV
- Durée: 30-60 minutes

Post-LEC:
- Hydratation forcée >2.5 L/jour
- Antalgiques si coliques
- Tamsulosine 0.4mg/jour (facilite expulsion fragments)
- AINS 3-5 jours

Surveillance:
- ASP + échographie à J15
- Si fragments résiduels >4mm: 2ème séance à 6 semaines
- Max 3 séances avant envisager URS
```

### 8.4 Urétéroscopie (URS)

#### Indications

- Calculs 10-20mm non éligibles LEC
- Échec LEC (fragments résiduels >4mm après 3 séances)
- Whewellite, Brushite, Cystine >10mm
- Calculs urétéraux symptomatiques

#### Technique

**URS souple** (calculs rénaux):
- Laser Holmium:YAG (fragmentation)
- Extraction au panier ou pince
- Sonde JJ 2-4 semaines

**URS rigide** (calculs urétéraux):
- Lithoclast pneumatique ou laser
- Extraction directe si <6mm

**Taux de succès**:
- Calculs rénaux <15mm: 85-95%
- Calculs urétéraux: 95-98%

### 8.5 Néphrolithotomie percutanée (PCNL)

#### Indications

- Calculs >20mm
- Calculs coralliformes
- Échec LEC/URS
- Calculs calice inférieur >15mm

#### Technique

- Abord percutané direct du rein
- Néphrolithotomie ou lithoclast ultrasonique
- Hospitalisation 3-5 jours

**Taux de succès**: 90-95% (stone-free en 1 temps)

---

## 9. Application manuelle de l'algorithme

### 9.1 Fiche de calcul manuelle

Cette fiche permet d'appliquer l'algorithme KALONJI sans logiciel informatique.

#### DONNÉES DU PATIENT

```
┌─────────────────────────────────────────────────────────────┐
│ FICHE D'ÉVALUATION MORPHO-CONSTITUTIONNELLE MANUELLE        │
├─────────────────────────────────────────────────────────────┤
│ Nom: _______________  Prénom: _______________  Date: _______ │
│ Âge: ____  Sexe: M / F                                       │
└─────────────────────────────────────────────────────────────┘
```

#### ÉTAPE 1: Collecte des données

```
┌────────────────── IMAGERIE SCANNER ───────────────────┐
│ Densité UH (noyau):        [____] UH                  │
│ Taille (grand axe):        [____] mm                  │
│ Morphologie:                                          │
│   □ Sphérique lisse  □ Irrégulière spiculée         │
│   □ Crayeuse         □ Coralliforme                  │
│   □ Hétérogène       □ Autre: ___________            │
│ Radio-opacité ASP:   □ Opaque  □ Transparent         │
│ Localisation: _______                                 │
│ Malformations:       □ Non  □ Oui: _________         │
└───────────────────────────────────────────────────────┘

┌──────────────── BIOLOGIE URINAIRE ────────────────────┐
│ pH urinaire:               [____]                     │
│ Densité urinaire:          [____]                     │
│ Sédiment (cristaux):       □ Oxalate  □ Urique       │
│                            □ Phosphate □ Cystine      │
│ ECBU:                      □ Stérile                  │
│                            □ Infecté, germe: ______   │
│                            □ Uréase +  □ Uréase -    │
└───────────────────────────────────────────────────────┘

┌──────────── MARQUEURS MÉTABOLIQUES 24H ───────────────┐
│ Calciurie:   [____] mg/24h   □ <300  □ ≥300 (hyper)  │
│ Oxalurie:    [____] mg/24h   □ <45   □ ≥45 (hyper)   │
│ Uricurie:    [____] mg/24h   □ <800  □ ≥800 (hyper)  │
│ Cystinurie:                  □ Non   □ Oui            │
└───────────────────────────────────────────────────────┘

┌───────────────── BILAN SANGUIN ───────────────────────┐
│ Calcémie:    [____] mmol/L   □ <2.60  □ ≥2.60        │
│ TSH:         [____] mUI/L    □ 0.4-4.0  □ <0.4       │
│ T3:          [____] pg/mL    □ Normal   □ >2.0        │
│ T4:          [____] ng/dL    □ Normal   □ >12.0       │
└───────────────────────────────────────────────────────┘
```

#### ÉTAPE 2: Grille de notation

Reproduire cette grille pour chacun des 8 types:

```
════════════════════════════════════════════════════════════
TYPE DE CALCUL: WHEWELLITE
════════════════════════════════════════════════════════════
Plage densité: 1200-1700 UH
pH favorable: 5.0-5.8
Marqueur: Hyperoxalurie
────────────────────────────────────────────────────────────

1. DENSITÉ (0-6 pts)
   Densité mesurée: [____] UH
   
   □ Dans plage [1200-1700]           → 6 pts
   □ Proche (Δ≤100 UH)                → 4 pts
   □ Éloignée (Δ≤200 UH)              → 2 pts
   □ Hors plage (Δ>200 UH)            → 0 pt
   
   SCORE DENSITÉ: [__] pts

2. MORPHOLOGIE (0-3 pts)
   Morphologie observée: _______________
   
   □ Sphérique lisse (signature)       → 3 pts
   □ Irrégulière spiculée (compatible) → 1 pt
   □ Hétérogène (compatible)           → 1 pt
   □ Autre                             → 0 pt
   
   SCORE MORPHOLOGIE: [__] pts

3. pH URINAIRE (0-3 pts)
   pH mesuré: [____]
   
   □ Dans plage [5.0-5.8]             → 3 pts
   □ Proche (Δ≤0.5)                   → 1 pt
   □ Hors plage (Δ>0.5)               → 0 pt
   
   SCORE pH: [__] pts

4. MARQUEURS MÉTABOLIQUES (0-6 pts)
   
   Score de base:
   □ Hyperoxalurie présente            → 4 pts
   □ Hyperoxalurie absente             → 0 pt
   
   Bonus hyperthyroïdie:
   □ TSH<0.4 ET (T3>2.0 OU T4>12.0)   → +2 pts
   □ Non                               → 0 pt
   
   Bonus hypercalcémie:
   □ Calcémie>2.60                     → +1 pt
   □ Non                               → 0 pt
   
   SCORE MÉTABOLIQUE: [__] pts

5. INFECTION (-1 à +3 pts)
   
   □ Pas d'infection                   → 0 pt
   □ Infection présente                → 0 pt
   
   SCORE INFECTION: [__] pts

6. RADIO-OPACITÉ (0-1 pt)
   
   □ Opaque (attendu)                  → 1 pt
   □ Transparent                       → 0 pt
   
   SCORE RADIO-OPACITÉ: [__] pts

7. MALFORMATIONS (0-1 pt)
   
   □ Pas de malformation               → 0 pt
   □ Malformation présente             → 0 pt
   
   SCORE MALFORMATIONS: [__] pts

────────────────────────────────────────────────────────────
SCORE TOTAL WHEWELLITE: [__] / 21 pts
════════════════════════════════════════════════════════════
```

#### ÉTAPE 3: Récapitulatif des scores

```
┌───────────────────────────────────────────────────────┐
│ CLASSEMENT DES 8 TYPES                                │
├───────────────────────────────────────────────────────┤
│ 1. Whewellite             [__] / 21                   │
│ 2. Weddellite             [__] / 21                   │
│ 3. Carbapatite            [__] / 21                   │
│ 4. Brushite               [__] / 21                   │
│ 5. Struvite               [__] / 21                   │
│ 6. Cystine                [__] / 21                   │
│ 7. Acide urique           [__] / 21                   │
│ 8. Urate ammonium         [__] / 21                   │
└───────────────────────────────────────────────────────┘

Classer par ordre décroissant:

Top 1: _______________ ([__] pts)
Top 2: _______________ ([__] pts)  
Top 3: _______________ ([__] pts)

Δ score (Top1 - Top2) = [__] pts

SI Δ < 2 → ⚠️ RÉSULTAT INCERTAIN
```

#### ÉTAPE 4: Interprétation

```
┌───────────────────────────────────────────────────────┐
│ INTERPRÉTATION                                        │
├───────────────────────────────────────────────────────┤
│ Type proposé: _______________                         │
│                                                       │
│ Composition:                                          │
│   □ PURE (score ≥12 ET Δ≥4)                          │
│   □ PURE PROBABLE (score 10-14)                       │
│   □ MIXTE PROBABLE (score <10 OU Δ<2)                │
│                                                       │
│ Certitude:                                            │
│   □ ÉLEVÉE (Δ≥4)                                      │
│   □ MODÉRÉE (Δ=2-3)                                   │
│   □ FAIBLE (Δ<2) ⚠️                                   │
└───────────────────────────────────────────────────────┘
```

#### ÉTAPE 5: Conduite à tenir

```
┌───────────────────────────────────────────────────────┐
│ RECOMMANDATIONS THÉRAPEUTIQUES                        │
├───────────────────────────────────────────────────────┤
│ Taille du calcul: [__] mm                             │
│                                                       │
│ Éligibilité LEC:                                      │
│   □ OUI (Weddellite, Carbapatite, Struvite)          │
│     ET Taille ≤20mm ET Densité <1500 UH              │
│   □ NON (Whewellite, Brushite, Cystine, Uriques)     │
│     OU Taille >20mm OU Densité ≥1500 UH              │
│                                                       │
│ Voie de traitement:                                   │
│   □ Dissolution médicale (Acide urique, Cystine)     │
│   □ Surveillance (< 10mm asymptomatique)              │
│   □ LEC (si éligible)                                 │
│   □ URS (non éligible LEC ou 10-20mm)                │
│   □ PCNL (>20mm ou coralliforme)                     │
└───────────────────────────────────────────────────────┘
```

#### ÉTAPE 6: Prévention

Se référer aux conseils spécifiques par type (section 6.7).

### 9.2 Exemple d'application manuelle complète

**CAS CLINIQUE**: Patient homme, 45 ans, 1er épisode lithiasique

**DONNÉES**:
- Densité scanner: 1250 UH
- Taille: 8 mm
- Morphologie: Sphérique lisse
- Radio-opacité: Opaque
- pH urinaire: 5.6
- Oxalurie 24h: 52 mg/24h (hyperoxalurie)
- Calciurie 24h: 220 mg/24h (normale)
- ECBU: Stérile
- Calcémie: 2.45 mmol/L (normale)
- TSH: 1.2 mUI/L (normale)

**SCORING WHEWELLITE**:

1. Densité 1250 UH dans [1200-1700] → **6 pts**
2. Morphologie sphérique lisse (signature) → **3 pts**
3. pH 5.6 dans [5.0-5.8] → **3 pts**
4. Hyperoxalurie (marqueur signature) → **4 pts**
   - Pas d'hyperthyroïdie → 0 pt bonus
   - Pas d'hypercalcémie → 0 pt bonus
5. Pas d'infection → **0 pt**
6. Radio-opacité opaque (attendu) → **1 pt**
7. Pas de malformation → **0 pt**

**SCORE TOTAL WHEWELLITE: 17/21 pts**

**SCORING WEDDELLITE**:

1. Densité 1250 UH dans [1000-1450] → **6 pts**
2. Morphologie sphérique lisse (compatible) → **1 pt**
3. pH 5.6 dans [5.0-5.8] → **3 pts**
4. Pas d'hypercalciurie → **0 pt**
5. Pas d'infection → **0 pt**
6. Radio-opacité opaque (attendu) → **1 pt**
7. Pas de malformation → **0 pt**

**SCORE TOTAL WEDDELLITE: 11/21 pts**

**SCORING AUTRES TYPES**: <10 pts

**CLASSEMENT**:
1. Whewellite: 17 pts
2. Weddellite: 11 pts
3. Acide urique: 6 pts

Δ = 17-11 = **6 pts** (certitude élevée)

**CONCLUSION**:
- **Type proposé**: Whewellite (oxalate de calcium monohydraté)
- **Composition**: PURE (score élevé 17/21, Δ=6)
- **Certitude**: ÉLEVÉE

**CONDUITE À TENIR**:
- Taille 8mm: Surveillance ou traitement médical expulsif
- **Éligibilité LEC**: NON (Whewellite résiste)
- Si symptomatique: URS (urétéroscopie)

**PRÉVENTION**:
1. Hydratation >2.5 L/jour
2. Limiter aliments riches en oxalate
3. Maintenir apport calcique normal (1000 mg/jour)
4. Alcaliniser urines (citrate potassium)
5. Contrôler oxalurie à 6 mois

---

## 10. Limites et perspectives

### 10.1 Limites de l'algorithme

#### 10.1.1 Limites intrinsèques

1. **Absence d'analyse spectrophotométrique directe**:
   - L'algorithme reste prédictif, non diagnostique
   - La SPIR reste la référence (sensibilité/spécificité >95%)
   - Discordances possibles avec composition réelle

2. **Types non couverts** (<2% des cas):
   - Calculs médicamenteux (indinavir, triamtérène)
   - Xanthine (déficit xanthine oxydase)
   - 2,8-dihydroxyadénine (déficit APRT)
   - Compositions très atypiques

3. **Compositions mixtes complexes**:
   - Calculs >2 composants difficiles à prédire
   - Stratifications multiples non modélisées
   - Score peut être intermédiaire entre plusieurs types

#### 10.1.2 Limites liées aux données

1. **Qualité de l'imagerie**:
   - Mesure densité dépend du protocole scanner
   - Artéfacts de volume partiel si calcul <3mm
   - Variabilité inter-observateur morphologie

2. **Timing des bilans biologiques**:
   - pH urinaire fluctue selon alimentation
   - Marqueurs métaboliques nécessitent recueil 24h rigoureux
   - Infections urinaires intermittentes (faux négatifs)

3. **Données manquantes**:
   - Score moins fiable si <4 critères renseignés
   - Marqueurs métaboliques rarement tous dosés
   - Hormones thyroïdiennes non systématiques

#### 10.1.3 Limites cliniques

1. **Populations spécifiques**:
   - Enfants (compositions différentes, plages UH non validées)
   - Grossesse (modifications métaboliques)
   - Insuffisance rénale avancée (DFG <30)

2. **Contextes particuliers**:
   - Post-chirurgie bariatrique (hyperoxalurie entérique)
   - Uropathies complexes
   - Patients transplantés rénaux

### 10.2 Perspectives d'amélioration

#### 10.2.1 Enrichissement de la base de connaissances

1. **Intégration de nouvelles variables**:
   - Génétique (polymorphismes lithogènes)
   - Microbiome urinaire
   - Biomarqueurs émergents (ostéopontine, calgranuline)

2. **Analyse algorithmique avancée**:
   - Analyse statistique sur base de données SPIR validées
   - Modélisation des compositions mixtes
   - Optimisation des pondérations par analyse comparative

3. **Imagerie avancée**:
   - Scanner spectral (double énergie)
   - IRM haute résolution
   - Analyse texture/radiomique

#### 10.2.2 Validation clinique

1. **Études prospectives**:
   - Corrélation score vs SPIR sur cohortes >1000 patients
   - Calcul sensibilité/spécificité par type
   - Identification facteurs prédictifs discordance

2. **Sous-groupes**:
   - Validation pédiatrique (ajustement plages)
   - Populations à risque spécifique
   - Calculs récidivants vs primo-formateurs

3. **Impact thérapeutique**:
   - Évaluation pertinence conseils préventifs
   - Réduction taux de récidive
   - Optimisation choix technique ablation

#### 10.2.3 Outils d'aide à la décision

1. **Interface multilingue**:
   - Traductions (anglais, espagnol, arabe)
   - Adaptation culturelle (alimentation)

2. **Intégration dossier patient**:
   - Import automatique scanner DICOM
   - Liaison laboratoire (résultats biologiques)
   - Historique longitudinal (récidives)

3. **Aide à l'interprétation**:
   - Visualisations graphiques (radar plots)
   - Rapports personnalisés patient
   - Recommandations diététiques illustrées

---

## Conclusion

L'algorithme KALONJI offre une **approche prédictive non-invasive** de la classification morpho-constitutionnelle des calculs urinaires, basée sur des critères cliniques, radiologiques et biologiques accessibles.

### Points forts

✓ **Précocité diagnostique**: Orientation avant récupération du calcul  
✓ **Approche multiparamétrique**: Triangulation de 7 critères indépendants  
✓ **Quantification objective**: Score sur 21 points, reproductible  
✓ **Applicabilité universelle**: Utilisable manuellement sans logiciel  
✓ **Recommandations actionnables**: Thérapeutique et préventive personnalisées  

### Usage recommandé

L'algorithme KALONJI est particulièrement utile pour:

1. **Orienter le bilan étiologique** avant récupération du calcul
2. **Débuter la prévention secondaire** précocement
3. **Guider le choix thérapeutique** (dissolution vs extraction)
4. **Contextes à faibles ressources** (absence de SPIR accessible)

### Complémentarité avec l'analyse SPIR

L'algorithme KALONJI **ne remplace pas** l'analyse spectrophotométrique infrarouge, mais:

- **Anticipe** le diagnostic probable
- **Complète** l'analyse chimique par le contexte métabolique
- **Guide** la prise en charge en attente des résultats SPIR

### Recommandation finale

```
┌──────────────────────────────────────────────────────────┐
│ ARBRE DÉCISIONNEL INTÉGRÉ                                │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  CALCUL DIAGNOSTIQUÉ (scanner + biologie)                │
│              │                                           │
│              ├─→ Appliquer algorithme KALONJI            │
│              │   (Score + Top 3 + Recommandations)       │
│              │                                           │
│              ├─→ SI Score élevé (≥15) ET Δ≥4:           │
│              │   • Débuter prévention spécifique         │
│              │   • Choisir voie thérapeutique adaptée    │
│              │                                           │
│              ├─→ SI Score modéré (10-14):                │
│              │   • Compléter bilan métabolique           │
│              │   • Appliquer conseils généraux           │
│              │   • Récupérer calcul pour SPIR            │
│              │                                           │
│              └─→ SI Score faible (<10) OU Δ<2:           │
│                  • Bilan métabolique complet obligatoire │
│                  • Récupérer calcul pour SPIR (référence)│
│                                                          │
│  APRÈS RÉCUPÉRATION DU CALCUL                            │
│              │                                           │
│              └─→ Analyse SPIR (référence diagnostique)   │
│                  • Ajuster prévention selon composition  │
│                  • Comparer avec prédiction KALONJI      │
│                  • Identifier causes discordance         │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

**L'algorithme KALONJI s'inscrit dans une démarche de médecine personnalisée et préventive, visant à optimiser la prise en charge lithiasique dès le diagnostic initial.**

---

## Références scientifiques

### Classification morpho-constitutionnelle (Daudon)

1. **Daudon M, Donsimoni R, Hennequin C, et al.** *Sex- and age-related composition of 10617 calculi analyzed by infrared spectroscopy*. Urol Res 1995;23(5):319-26. doi:10.1007/BF00300021

2. **Daudon M, Traxer O, Lechevallier E, Saussine C.** *Épidémiologie des lithiases urinaires*. Progrès en Urologie 2008;18(12):802-814. doi:10.1016/j.purol.2008.09.029

3. **Daudon M, Bazin D, André G, et al.** *Composition des calculs observés aujourd'hui dans les pays industrialisés*. Progrès en Urologie 2004;14(6):1151-1161.

### Densité tomodensitométrique (UH)

4. **Mostafavi MR, Ernst RD, Saltzman B.** *Accurate determination of chemical composition of urinary calculi by spiral computerized tomography*. J Urol 1998;159(3):673-5. doi:10.1016/s0022-5347(01)63698-x

5. **Nakada SY, Hoff DG, Attai S, et al.** *Determination of stone composition by noncontrast spiral computed tomography in the clinical setting*. Urology 2000;55(6):816-9. doi:10.1016/s0090-4295(00)00518-5

6. **Bellin MF, Renard-Penna R, Conort P, et al.** *Helical CT evaluation of the chemical composition of urinary tract calculi with a discriminant analysis of CT-attenuation values and density*. Eur Radiol 2004;14(11):2134-40. doi:10.1007/s00330-004-2365-6

### Physiopathologie

7. **Worcester EM, Coe FL.** *Clinical practice. Calcium kidney stones*. N Engl J Med 2010;363(10):954-63. doi:10.1056/NEJMcp1001011

8. **Letavernier E, Daudon M.** *Lithiase urinaire*. EMC - Néphrologie 2014;11(2):1-14. doi:10.1016/S1769-7255(14)67463-8

9. **Sakhaee K, Maalouf NM, Sinnott B.** *Clinical review. Kidney stones 2012: pathogenesis, diagnosis, and management*. J Clin Endocrinol Metab 2012;97(6):1847-60. doi:10.1210/jc.2011-3492

### Calculs infectieux (Struvite)

10. **Flannigan R, Choy WH, Chew B, Lange D.** *Renal struvite stones--pathogenesis, microbiology, and management strategies*. Nat Rev Urol 2014;11(6):333-41. doi:10.1038/nrurol.2014.99

11. **Bichler KH, Eipper E, Naber K, et al.** *Urinary infection stones*. Int J Antimicrob Agents 2002;19(6):488-98. doi:10.1016/s0924-8579(02)00088-2

### Cystinurie

12. **Knoll T, Zollner A, Wendt-Nordahl G, et al.** *Cystinuria in childhood and adolescence: recommendations for diagnosis, treatment, and follow-up*. Pediatr Nephrol 2005;20(1):19-24. doi:10.1007/s00467-004-1663-1

### Directives cliniques

13. **Türk C, Petřík A, Sarica K, et al.** *EAU Guidelines on Diagnosis and Conservative Management of Urolithiasis*. European Urology 2016;69(3):468-474. doi:10.1016/j.eururo.2015.07.040

14. **Assimos D, Krambeck A, Miller NL, et al.** *Surgical Management of Stones: American Urological Association/Endourological Society Guideline, PART I*. Journal of Urology 2016;196(4):1153-1160. doi:10.1016/j.juro.2016.05.090

### Facteurs de risque spécifiques

15. **Alhashemi H, Bokhari SJ, Abdullatif A, et al.** *Association between hyperthyroidism and nephrolithiasis: a systematic review and meta-analysis*. Int J Surg 2020;84:136-142. doi:10.1016/j.ijsu.2020.10.029

16. **Skoog SJ, Belman AB.** *Urolithiasis and congenital abnormalities*. Urol Clin North Am 2000;27(2):279-84. doi:10.1016/s0094-0143(05)70256-3

---

**Document rédigé le**: Novembre 2025  
**Version**: 1.0  
**Prochaine révision**: Novembre 2026  
**Contact**: Équipe KALONJI  

═══════════════════════════════════════════════════════════════
FIN DU DOCUMENT SCIENTIFIQUE
═══════════════════════════════════════════════════════════════
