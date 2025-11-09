# Algorithme d'inférence - Classification de Daudon

## 📊 Vue d'ensemble

Le moteur d'inférence de l'application **Algorithme Lithiase KALONJI** est basé sur la **classification morpho-constitutionnelle de Daudon**, référence internationale pour l'analyse des calculs rénaux. L'algorithme utilise un système de notation sur **21 points maximum** (incluant 1 point bonus pour les malformations urinaires) pour déterminer le type de calcul le plus probable parmi 8 types couverts.

## 🎯 Objectifs médicaux

1. Identifier le type de calcul avec précision
2. Proposer un traitement adapté selon la taille et la composition
3. Recommander des mesures de prévention personnalisées
4. Détecter les calculs éligibles à la lithotripsie extracorporelle (LEC)
5. Identifier les infections lithogènes (Struvite, Carbapatite)

## 🧮 Système de notation (21 points)

### Distribution des points

| Critère | Points max | Description |
|---------|------------|-------------|
| **Densité scanner (UH)** | 6 | Plage typique pour chaque type |
| **Morphologie** | 3 | Forme caractéristique ou compatible |
| **pH urinaire** | 3 | Plage préférentielle selon le type |
| **Marqueurs métaboliques** | 4 | Hyperoxalurie, hypercalciurie, etc. |
| **Infection urinaire** | 3 | Favorable ou défavorable selon le type |
| **Radio-opacité** | 1 | Opaque ou transparent |
| **Malformations urinaires** | 1 | Facteur de risque lithogène |
| **TOTAL** | 21 | Score maximum (20 + 1 bonus) |

### 1. Densité scanner (6 points)

La densité mesurée en unités Hounsfield (UH) est le critère le plus discriminant.

**Attribution des points :**
- **6 points** : Densité dans la plage typique du type
- **4 points** : Densité proche de la plage (±100 UH)
- **2 points** : Densité éloignée de la plage (±200 UH)
- **0 point** : Densité hors plage typique

**Exemple :**
```python
# Pour un calcul de Whewellite (plage : 1200-1700 UH)
densite_uh = 1250  # → 6 points (dans la plage)
densite_uh = 1100  # → 4 points (proche, -100 UH)
densite_uh = 1000  # → 2 points (éloigné, -200 UH)
densite_uh = 800   # → 0 point (hors plage)
```

### 2. Morphologie (3 points)

Forme caractéristique du calcul visible à l'imagerie.

**Attribution des points :**
- **3 points** : Morphologie signature du type
- **1 point** : Morphologie compatible avec le type
- **0 point** : Morphologie non caractéristique

**Morphologies reconnues :**
- `spherique_lisse` : Surface lisse, forme régulière
- `irreguliere_spiculee` : Surface rugueuse, spicules
- `crayeuse` : Aspect friable, surface crayeuse
- `coralliforme` : Forme en corail, ramifications
- `heterogene` : Composition mixte, aspect hétérogène

### 3. pH urinaire (3 points)

Le pH urinaire est crucial pour certains types de calculs.

**Attribution des points :**
- **3 points** : pH dans la plage préférentielle
- **1 point** : pH proche de la plage (±0.5)
- **0 point** : pH hors plage préférentielle

**Plages caractéristiques :**
- **pH acide (5.0-5.8)** : Whewellite, Weddellite, Cystine, Acide urique
- **pH neutre/alcalin (6.8-7.5)** : Carbapatite, Struvite, Urate d'ammonium
- **pH intermédiaire (6.0-6.8)** : Brushite

### 4. Marqueurs métaboliques (4 points + bonus)

Présence de troubles métaboliques spécifiques.

**Attribution des points de base :**
- **4 points** : Marqueur signature présent
- **0 point** : Marqueur signature absent ou non applicable

**Marqueurs par type :**
- **Hyperoxalurie** → Whewellite
- **Hypercalciurie** → Weddellite, Carbapatite, Brushite
- **Hyperuricurie** → Acide urique
- **Cystinurie** → Cystine

**Points bonus (jusqu'à +2 points supplémentaires) :**
- **Hyperthyroïdie détectée** : +1 point si calcul calcique (favorise hypercalciurie)
  - TSH < 0.4 mUI/L ET (T3 > 2.0 pg/mL OU T4 > 12.0 ng/dL)
- **Hypercalcémie** : +1 point si marqueur = hypercalciurie
  - Calciémie > 2.6 mmol/L

### 5. Infection urinaire (3 points)

Certains calculs sont favorisés par les infections.

**Attribution des points :**
- **+3 points** : Infection présente (favorable pour le type)
- **-1 point** : Absence d'infection (défavorable pour le type)
- **0 point** : Infection non caractéristique ou neutre

**Types infectieux :**
- **Struvite** : Toujours associé à une infection à germe uréase+
- **Carbapatite** : Souvent associé à une infection
- **Urate d'ammonium** : Favorisé par les infections

### 6. Radio-opacité (1 point)

Visibilité du calcul à la radiographie simple (ASP).

**Attribution des points :**
- **1 point** : Radio-opacité concordante
- **0 point** : Radio-opacité non concordante

**Classification :**
- **Opaques** : Oxalate de calcium, Phosphates calciques
- **Transparents** : Acide urique, Cystine, Struvite, Urate d'ammonium

### 7. Malformations urinaires (1 point bonus)

Les malformations des voies urinaires favorisent la stase urinaire et les infections récurrentes, augmentant le risque de calculs infectieux.

**Attribution des points :**
- **+1 point** : Présence d'une malformation lithogène ET calcul de type infectieux (Struvite, Carbapatite, Urate d'ammonium)
- **0 point** : Absence de malformation ou type de calcul non infectieux

**Malformations lithogènes reconnues :**
- Sténose de la jonction pyélo-urétérale (JPU)
- Syndrome de la jonction urétéro-vésicale (JUV)
- Mégauretère
- Reflux vésico-urétéral
- Duplicité urétérale
- Urétérocèle
- Valve de l'urètre postérieur
- Diverticule caliciel

**Justification médicale :**
Les malformations urinaires créent des zones de stase où l'urine stagne, favorisant :
1. La concentration des sels minéraux
2. Le développement de biofilms bactériens
3. Les infections urinaires récidivantes
4. La formation de calculs infectieux (Struvite notamment)

## 🔀 Détermination : Calcul Pur ou Mixte

Après le calcul du score pour chaque type de calcul, l'algorithme détermine si la composition est **Pure** ou **Mixte** :

### Calcul Pur
Un calcul est considéré comme **Pur** lorsqu'un type domine clairement :
- **Critère** : La différence de score entre le type le plus probable et le deuxième type > 4 points
- **Interprétation** : Le calcul est composé principalement d'un seul type
- **Affichage** : "Whewellite pur", "Struvite pur", etc.

**Exemple :**
```
Score de base Whewellite : 14/20
Score de base Weddellite : 8/20
Différence : 6 points → Calcul PUR (Whewellite pur)

Note: Scores de base (hors bonus malformations)
Avec bonus malformations si applicable: +1 point possible
```

### Calcul Mixte
Un calcul est considéré comme **Mixte** lorsque plusieurs types ont des scores proches :
- **Critère** : La différence de score entre le type le plus probable et le deuxième type ≤ 4 points
- **Interprétation** : Le calcul est composé d'un mélange de plusieurs types
- **Affichage** : "Whewellite + Weddellite (mixte)", "Carbapatite + Struvite (mixte)", etc.

**Exemple :**
```
Score de base Whewellite : 12/20
Score de base Weddellite : 10/20
Score de base Brushite : 9/20
Différence : 2 points → Calcul MIXTE (Whewellite + Weddellite + Brushite)

Note: Scores de base (hors bonus malformations)
Avec bonus malformations si applicable: +1 point possible pour types infectieux
```

### Signification clinique

**Calculs purs :**
- Étiologie unique et bien identifiée
- Traitement préventif ciblé plus efficace
- Récidive prévisible si la cause n'est pas traitée

**Calculs mixtes :**
- Étiologies multiples ou évolutives
- Traitement préventif doit couvrir plusieurs facteurs
- Indication d'un déséquilibre métabolique complexe
- Nécessite un suivi métabolique approfondi

## 📋 Types de calculs couverts

### 1. Oxalate de calcium - Whewellite (CaC₂O₄·H₂O)

**Caractéristiques :**
- Densité UH : 1200-1700
- pH préférentiel : 5.0-5.8 (acide)
- Morphologie signature : Sphérique lisse
- Radio-opacité : Opaque
- Marqueur : Hyperoxalurie
- Infection : Non favorable

**Prévention :**
- Hydratation abondante (2-3L/jour)
- Réduire les oxalates (épinards, rhubarbe, chocolat, thé)
- Apport calcique normal avec les repas
- Traiter l'hyperoxalurie si présente

### 2. Oxalate de calcium - Weddellite (CaC₂O₄·2H₂O)

**Caractéristiques :**
- Densité UH : 1000-1450
- pH préférentiel : 5.0-5.8 (acide)
- Morphologie signature : Irrégulière spiculée
- Radio-opacité : Opaque
- Marqueur : Hypercalciurie
- Infection : Non favorable
- **Éligible LEC** : Oui

**Prévention :**
- Hydratation abondante (2-3L/jour)
- Réduire le sel
- Apport calcique normal (1000mg/jour)
- Limiter les oxalates
- Traiter l'hypercalciurie si présente

### 3. Phosphate de calcium - Carbapatite (Ca₁₀(PO₄)₆(OH)₂)

**Caractéristiques :**
- Densité UH : 1300-1400
- pH préférentiel : 6.8-7.5 (alcalin)
- Morphologie signature : Crayeuse
- Radio-opacité : Opaque
- Marqueur : Hypercalciurie
- Infection : **Favorable**
- **Éligible LEC** : Oui

**Prévention :**
- Contrôle des infections urinaires
- Hydratation régulière
- Bilan phospho-calcique
- Éviter l'alcalinisation excessive

### 4. Phosphate de calcium - Brushite (CaHPO₄·2H₂O)

**Caractéristiques :**
- Densité UH : 1550-2000
- pH préférentiel : 6.0-6.8 (neutre)
- Morphologie signature : Irrégulière spiculée
- Radio-opacité : Opaque
- Marqueur : Hypercalciurie
- Infection : Non favorable

**Prévention :**
- Hydratation abondante
- Bilan parathyroïdien
- Contrôle du phosphore
- Suivi métabolique rapproché

### 5. Struvite (MgNH₄PO₄·6H₂O)

**Caractéristiques :**
- Densité UH : 550-950
- pH préférentiel : 6.8-7.5 (alcalin)
- Morphologie signature : Coralliforme, irrégulière spiculée
- Radio-opacité : Transparent
- Marqueur : Aucun (infectieux)
- Infection : **Toujours présente** (germe uréase+)
- **Éligible LEC** : Oui

**Prévention :**
- Contrôle strict des infections urinaires
- Antibiothérapie adaptée
- Traitement complet du calcul
- Suivi urologique régulier

### 6. Cystine

**Caractéristiques :**
- Densité UH : 650-850
- pH préférentiel : 5.0-5.8 (acide)
- Morphologie signature : Sphérique lisse
- Radio-opacité : Transparent
- Marqueur : **Cystinurie** (maladie génétique)
- Infection : Non favorable

**Prévention :**
- Hydratation très abondante (>3L/jour)
- Alcalinisation des urines (pH>7.5)
- Réduire le sel et les protéines
- Traitement spécifique (thiopronine si nécessaire)

### 7. Acide urique

**Caractéristiques :**
- Densité UH : 350-650
- pH préférentiel : 5.0-5.8 (acide)
- Morphologie signature : Sphérique lisse
- Radio-opacité : Transparent
- Marqueur : Hyperuricurie
- Infection : Non favorable

**Prévention :**
- Augmenter l'hydratation (2-3L/jour)
- Alcalinisation des urines (citrate de potassium)
- Réduire les protéines animales
- Limiter les purines (abats, fruits de mer)

### 8. Urate d'ammonium

**Caractéristiques :**
- Densité UH : 150-300
- pH préférentiel : 6.8-7.5 (alcalin)
- Morphologie signature : Sphérique lisse
- Radio-opacité : Transparent
- Marqueur : Aucun
- Infection : Favorable

**Prévention :**
- Contrôle des infections urinaires
- Traitement des diarrhées chroniques si présentes
- Hydratation régulière
- Suivi urologique

## 🔬 Processus d'inférence

### Étape 1 : Extraction des données

L'algorithme récupère les données d'imagerie et de biologie :

**Imagerie :**
- Densité UH (densite_uh ou densite_noyau)
- Morphologie
- Radio-opacité
- Taille (taille_mm ou diametre_longitudinal)
- Forme du calcul
- Contour du calcul
- Nombre de calculs
- Topographie

**Biologie :**
- pH urinaire
- Densité urinaire
- Marqueurs métaboliques (hyperoxalurie, hypercalciurie, hyperuricurie, cystinurie)
- Valeurs des marqueurs (oxalurie, calciurie, uricurie, calciémie)
- Hormones thyroïdiennes (TSH, T3, T4) pour détecter hyperthyroïdie
- Infection urinaire
- Sédiment urinaire
- ECBU

### Étape 2 : Calcul des scores

Pour chaque type de calcul, l'algorithme calcule un score en additionnant les points obtenus pour chaque critère.

```python
score_total = (
    score_densite +       # 0-6 points
    score_morphologie +   # 0-3 points
    score_ph +            # 0-3 points
    score_metabolique +   # 0-6 points (base 0-4 + bonus 0-2)
    score_infection +     # -1 à +3 points
    score_radio_opacite + # 0-1 point
    score_malformations   # 0-1 point (bonus pour calculs infectieux)
)
# Score maximum de base : 21 points (20 + 1 bonus malformations)
# Score maximum théorique avec tous les bonus métaboliques : 23 points
```

### Étape 3 : Classement

Les 8 types de calculs sont classés par score décroissant. Le Top 3 est retourné.

### Étape 4 : Détection d'incertitude

Si la différence entre le 1er et le 2ème est < 2 points, le résultat est marqué comme **incertain**. Une alerte est affichée pour demander des examens complémentaires.

### Étape 5 : Recommandations

En fonction du type proposé et de la taille :

#### Éligibilité LEC
- **Oui** : Weddellite, Carbapatite, Struvite
- **Non** : Whewellite, Brushite, Cystine, Acide urique, Urate d'ammonium

#### Voie de traitement

**Taille < 10mm :**
- Traitement médical / Surveillance
- URS possible si LEC éligible et UH < 1000
- LEC possible si LEC éligible

**Taille 10-20mm :**
- LEC en première intention si éligible et UH < 1500
- URS en première intention sinon

**Taille > 20mm :**
- PCNL si calcul coralliforme
- PCNL / URS selon localisation

## 📈 Exemple d'inférence

### Cas clinique

**Patient :** Homme, 48 ans, récidivant

**Imagerie :**
- Densité : 1250 UH
- Taille : 12 mm
- Morphologie : Sphérique lisse
- Radio-opacité : Opaque
- Localisation : Rein droit, calice inférieur

**Biologie :**
- pH : 5.5
- Hyperoxalurie : Oui
- Hypercalciurie : Non
- Infection : Non

### Calcul des scores

**Note:** Les scores ci-dessous sont des scores de base (sur 20 points). Le bonus malformations (+1 point) s'applique uniquement aux calculs de type infectieux (Struvite, Carbapatite, Urate d'ammonium) en présence de malformations urinaires lithogènes.

#### Whewellite
- Densité : **6 pts** (1250 dans [1200-1700])
- Morphologie : **3 pts** (sphérique lisse = signature)
- pH : **3 pts** (5.5 dans [5.0-5.8])
- Métabolique : **4 pts** (hyperoxalurie présente)
- Infection : **0 pt** (non favorable, absence OK)
- Radio-opacité : **1 pt** (opaque = OK)
- Malformations : **0 pt** (non applicable pour calcul non infectieux)
- **TOTAL : 17/20** (score de base) ✅

#### Weddellite
- Densité : **4 pts** (1250 proche de [1000-1450])
- Morphologie : **1 pt** (sphérique lisse = compatible)
- pH : **3 pts** (5.5 dans [5.0-5.8])
- Métabolique : **0 pt** (hypercalciurie absente)
- Infection : **0 pt**
- Radio-opacité : **1 pt**
- Malformations : **0 pt** (non applicable pour calcul non infectieux)
- **TOTAL : 9/20** (score de base)

#### Acide urique
- Densité : **0 pt** (1250 hors [350-650])
- Morphologie : **3 pts** (sphérique lisse = signature)
- pH : **3 pts** (5.5 dans [5.0-5.8])
- Métabolique : **0 pt** (hyperuricurie absente)
- Infection : **0 pt**
- Radio-opacité : **0 pt** (opaque ≠ transparent)
- Malformations : **0 pt** (non applicable pour calcul non infectieux)
- **TOTAL : 6/20** (score de base)

### Résultat

```
🎯 Type proposé : Whewellite
⭐ Score : 17/20 (score de base, bonus malformations non applicable)
📝 Justification :
   - Densité 1250 UH dans la plage typique [1200-1700]
   - Morphologie signature (sphérique lisse)
   - pH 5.5 dans la plage préférentielle [5.0-5.8]
   - Marqueur signature présent (hyperoxalurie)
   - Radio-opacité concordante (opaque)

📊 Top 3 (scores de base sur 20) :
   1. Whewellite : 17/20
   2. Weddellite : 9/20
   3. Acide urique : 6/20

⚡ LEC éligible : Non
🔬 Voie de traitement : URS (première intention)
🛡️ Prévention :
   - Hydratation abondante (2-3L/jour)
   - Réduire les aliments riches en oxalates
   - Apport calcique normal avec les repas
   - Traiter l'hyperoxalurie si présente
```

## 🎓 Références médicales

1. **Daudon M, Bazin D, Letavernier E.** "Randall's plaque as the origin of calcium oxalate kidney stones." Urolithiasis, 2015.

2. **Daudon M, Traxer O, Lechevallier E, Saussine C.** "Épidémiologie des lithiases urinaires." Progrès en Urologie, 2008.

3. **Letavernier E, Daudon M.** "Lithiase urinaire." EMC - Néphrologie, 2014.

4. **Türk C, Petřík A, Sarica K, et al.** "EAU Guidelines on Diagnosis and Conservative Management of Urolithiasis." European Urology, 2016.

5. **Assimos D, Krambeck A, Miller NL, et al.** "Surgical Management of Stones: American Urological Association/Endourological Society Guideline." Journal of Urology, 2016.

## 💡 Limites de l'algorithme

- L'inférence est une **aide au diagnostic**, pas un diagnostic définitif
- L'analyse physicochimique du calcul reste la référence (spectroscopie infrarouge)
- Certains calculs sont mixtes et peuvent correspondre à plusieurs types
- Des examens complémentaires sont nécessaires en cas d'incertitude
- Le contexte clinique et l'expertise médicale restent essentiels

## 🔄 Mise à jour de l'algorithme

L'algorithme peut être enrichi avec :
- Nouveaux critères (forme détaillée, contour, densité des couches)
- Machine learning sur historique de calculs analysés
- Intégration de marqueurs biologiques supplémentaires
- Analyse d'images DICOM avec algorithme avancé
- Corrélation avec analyse physicochimique des calculs expulsés
