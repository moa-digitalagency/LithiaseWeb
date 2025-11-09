# ALGORITHME KALONJI - VERSION CLINICIENS


**Document destiné aux professionnels de santé - Présentation conceptuelle sans implémentation technique**

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


**Exemple clinique**:

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


**Exemple clinique**:

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

**Hypercalcémie** (+1 point pour calculs calciques):

### 4.5 Critère 5 - Infection urinaire (-1 à +3 points)

**Justification scientifique**: Les infections urinaires à germes uréasiques favorisent les calculs infectieux. Leur absence rend ces calculs improbables.

#### Attribution des points


### 4.6 Critère 6 - Radio-opacité (0-1 point)

**Justification scientifique**: La radio-opacité à l'ASP reflète la teneur en calcium du calcul.

#### Attribution des points

| Type | Radio-opacité attendue | Points si concordance |
|------|------------------------|----------------------|
| Whewellite, Weddellite, Brushite, Carbapatite | Opaque | +1 |
| Struvite, Cystine, Acide urique, Urate ammonium | Transparent | +1 |


### 4.7 Critère 7 - Malformations urinaires (0-1 point)

**Justification scientifique**: Les malformations urinaires (duplicité, ectasie, reflux) favorisent la stase urinaire et les infections, prédisposant aux calculs infectieux.

#### Attribution des points


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


### 6.2 Étape 2 - Calcul du score pour chaque type

**Algorithme de scoring**:


**Détail des fonctions de scoring**:


### 6.3 Étape 3 - Classement et sélection


### 6.4 Étape 4 - Détection d'incertitude diagnostique


### 6.5 Étape 5 - Détermination du type de composition


### 6.6 Étape 6 - Génération des recommandations thérapeutiques

#### Éligibilité à la lithotripsie extracorporelle (LEC)


#### Voie de traitement recommandée


### 6.7 Étape 7 - Conseils de prévention personnalisés


---

## 7. Interprétation des résultats

### 7.1 Rapport d'inférence type

Le rapport généré par l'algorithme contient:

#### Section 1 - Résultat principal


#### Section 2 - Justifications détaillées


#### Section 3 - Top 3 types probables


#### Section 4 - Conduite à tenir


#### Section 5 - Prévention


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


#### Cas 2: Score faible pour tous les types (<10)

**Exemple**: Meilleur score 8 pts (Carbapatite)


#### Cas 3: Incohérence flagrante

**Exemple**: Densité 1400 UH + Radio-opacité transparente


---

## 8. Conduite à tenir thérapeutique

### 8.1 Arbre décisionnel thérapeutique


### 8.2 Dissolution médicale (calculs radiotransparents)

#### Acide urique

**Indications**:
- Calcul <15mm
- Radiotransparent confirmé (ASP + scanner <500 UH)
- Fonction rénale préservée
- Absence d'obstruction complète

**Protocole d'alcalinisation**:

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


#### ÉTAPE 1: Collecte des données


#### ÉTAPE 2: Grille de notation

Reproduire cette grille pour chacun des 8 types:


#### ÉTAPE 3: Récapitulatif des scores


#### ÉTAPE 4: Interprétation


#### ÉTAPE 5: Conduite à tenir


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
