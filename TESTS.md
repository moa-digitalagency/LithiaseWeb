# Guide de tests - Algorithme Lithiase KALONJI

## Accès à l'application
- URL: http://localhost:5000
- Utilisateur: `admin`
- Mot de passe: `admin123`

## Critères d'acceptation à vérifier

### 1. Création patient/épisode/examens
- [ ] Créer un nouveau patient avec toutes les informations obligatoires
- [ ] Ajouter un épisode à ce patient
- [ ] Ajouter une imagerie à l'épisode
- [ ] Ajouter une biologie à l'épisode

### 2. Test d'inférence #1: Whewellite
**Données:**
- UH = 1650
- pH = 5.3
- Hyperoxalurie = Oui

**Résultat attendu:**
- Type proposé: Whewellite (Top 1)
- LEC éligible: Non

**Étapes:**
1. Créer un patient
2. Créer un épisode
3. Ajouter imagerie: taille=8mm, UH=1650, morphologie=sphérique lisse
4. Ajouter biologie: pH=5.3, hyperoxalurie=coché
5. Cliquer sur "Calculer le type de calcul"
6. Vérifier le résultat

### 3. Test d'inférence #2: Weddellite
**Données:**
- UH = 1100
- Morphologie = spiculée
- pH = 5.6
- Hypercalciurie = Oui

**Résultat attendu:**
- Type proposé: Weddellite (Top 1)
- LEC éligible: Oui

**Étapes:**
1. Créer un patient
2. Créer un épisode
3. Ajouter imagerie: taille=12mm, UH=1100, morphologie=irrégulière spiculée
4. Ajouter biologie: pH=5.6, hypercalciurie=coché
5. Cliquer sur "Calculer le type de calcul"
6. Vérifier le résultat

### 4. Test d'inférence #3: Carbapatite
**Données:**
- UH = 1320
- pH = 7.2
- Infection = Oui

**Résultat attendu:**
- Type proposé: Carbapatite (Top 1)
- LEC éligible: Oui

**Étapes:**
1. Créer un patient
2. Créer un épisode
3. Ajouter imagerie: taille=15mm, UH=1320, morphologie=crayeuse
4. Ajouter biologie: pH=7.2, infection_urinaire=coché
5. Cliquer sur "Calculer le type de calcul"
6. Vérifier le résultat

### 5. Test d'inférence #4: Struvite
**Données:**
- UH = 600
- pH = 7.0
- Infection (uréase +) = Oui

**Résultat attendu:**
- Type proposé: Struvite (Top 1)
- LEC éligible: Oui

**Étapes:**
1. Créer un patient
2. Créer un épisode
3. Ajouter imagerie: taille=25mm, UH=600, morphologie=coralliforme
4. Ajouter biologie: pH=7.0, infection_urinaire=coché
5. Cliquer sur "Calculer le type de calcul"
6. Vérifier le résultat

### 6. Test d'inférence #5: Acide urique
**Données:**
- UH = 450
- pH = 5.2
- Hyperuricurie = Oui

**Résultat attendu:**
- Type proposé: Acide urique (Top 1)
- LEC éligible: Non

**Étapes:**
1. Créer un patient
2. Créer un épisode
3. Ajouter imagerie: taille=10mm, UH=450, morphologie=sphérique lisse, radio-opacité=transparent
4. Ajouter biologie: pH=5.2, hyperuricurie=coché
5. Cliquer sur "Calculer le type de calcul"
6. Vérifier le résultat

### 7. Export PDF
- [ ] Ouvrir un patient
- [ ] Cliquer sur "Exporter PDF"
- [ ] Vérifier que le PDF contient: identité, épisodes, inférence, conseils

### 8. Export CSV
- [ ] Aller dans "Recherche avancée"
- [ ] Appliquer des filtres (ex: pH entre 5.0 et 6.0)
- [ ] Cliquer sur "Exporter CSV"
- [ ] Vérifier que le CSV contient les données filtrées

### 9. Recherche par filtres
- [ ] Tester le filtre par pH (min/max)
- [ ] Tester le filtre par UH (min/max)
- [ ] Tester le filtre par infection (Oui/Non)
- [ ] Vérifier que les résultats correspondent aux filtres

## Tests fonctionnels supplémentaires

### Interface Dashboard
- [ ] Liste des patients affichée correctement
- [ ] Recherche en temps réel fonctionne
- [ ] Bouton "Nouveau Patient" ouvre le modal
- [ ] Validation des champs obligatoires

### Interface Fiche Patient
- [ ] Informations patient affichées correctement
- [ ] Liste des épisodes visible
- [ ] Clic sur épisode ouvre le détail
- [ ] Navigation entre onglets fluide

### Moteur d'inférence
- [ ] Top 3 des types affichés
- [ ] Justification détaillée visible
- [ ] Badge "incertain" si scores proches
- [ ] Conseils de prévention personnalisés
- [ ] Détermination de la voie de traitement

## Bugs potentiels à vérifier
- [ ] Dates au format français (JJ/MM/AAAA)
- [ ] Gestion des champs vides
- [ ] Messages d'erreur clairs
- [ ] Responsive design (mobile/tablet)
