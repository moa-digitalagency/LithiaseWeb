# Algorithme Lithiase KALONJI - Documentation

## 📋 Vue d'ensemble

**Algorithme Lithiase KALONJI** est une application web médicale destinée aux médecins pour la gestion complète des patients souffrant de lithiase rénale (calculs rénaux). L'application intègre un moteur d'inférence basé sur la classification morpho-constitutionnelle de Daudon pour aider au diagnostic et au traitement.

## 🎯 Objectifs médicaux

1. **Déterminer la nature morpho-constitutionnelle** du calcul selon la classification de Daudon
2. **Détecter les anomalies** dans les habitudes du patient favorisant la formation des calculs
3. **Proposer un régime alimentaire adapté** pour prévenir les récidives
4. **Recommander un traitement médical** fondé sur les dernières données scientifiques
5. **Proposer un traitement adapté** en cas d'infection urinaire associée selon la nature du germe isolé

## 🔑 Fonctionnalités principales

### Gestion des patients
- Création et modification de fiches patient complètes
- Données personnelles (identité, contacts, anthropométrie)
- Antécédents médicaux (personnels, familiaux, chirurgicaux)
- Allergies et traitements en cours
- Habitudes alimentaires détaillées (petit-déjeuner, déjeuner, dîner, grignotages)
- Données anthropométriques (poids, taille, IMC automatique)

### Gestion des épisodes médicaux
- Suivi des épisodes lithiasiques (coliques néphrétiques, récidives)
- Association d'examens d'imagerie et de biologie à chaque épisode
- Historique complet pour chaque patient

### Examens d'imagerie
- **ASP** (Abdomen Sans Préparation)
- **Échographie**
- **Uro-scanner** avec détails complets :
  - Nombre de calculs
  - Topographie précise
  - Dimensions (longitudinal, transversal)
  - Forme et contour
  - Densité du noyau et des couches (UH)
  - Morphologie
  - Radio-opacité
  - Autres calcifications

### Examens biologiques
- pH urinaire
- Densité urinaire
- Sédiment urinaire
- ECBU (Examen Cytobactériologique Urinaire)
- Marqueurs métaboliques :
  - Hyperoxalurie
  - Hypercalciurie
  - Hyperuricurie
  - Cystinurie
- Détection d'infections urinaires

### Moteur d'inférence
- Classification automatique du type de calcul sur un système de notation sur 20 points
- **Nature morpho-constitutionnelle** : Spécifie si le calcul est **Pur** ou **Mixte**
  - **Pur** : Un seul type dominant (différence de score > 4 points)
  - **Mixte** : Combinaison de plusieurs types (scores proches)
- 8 types de calculs couverts :
  - Oxalate de calcium (Whewellite, Weddellite)
  - Phosphates calciques (Carbapatite, Brushite)
  - Struvite (infectieux)
  - Cystine
  - Acide urique
  - Urate d'ammonium
- Indication sur l'incertitude du diagnostic
- Éligibilité à la LEC (Lithotripsie Extra-Corporelle)
- Proposition de voie de traitement selon la taille et le type
- Conseils de prévention personnalisés

### Recherche et export
- **Recherche avancée** : filtrage par critères médicaux (pH, densité UH, infection, etc.)
- **Export PDF** : rapport patient complet avec toutes les données et résultats d'inférence
- **Export CSV** : données filtrées pour analyse statistique

### Sécurité
- Chiffrement des données de santé (Fernet AES-128 + HMAC)
- 25+ champs sensibles chiffrés en base de données
- Conformité RGPD
- Authentification sécurisée
- Gestion sécurisée des mots de passe

## 📖 Documentation

- [Guide technique](TECHNIQUE.md) : Architecture, technologies et implémentation
- [Algorithme médical](ALGORITHME.md) : Détails du moteur d'inférence et classification de Daudon
- [Guide d'utilisation](USAGE.md) : Manuel utilisateur pour les médecins

## 🚀 Démarrage rapide

1. **Connexion** : Utilisez vos identifiants médicaux
2. **Patients de démonstration** : 4 patients complets sont pré-chargés pour découvrir l'application
3. **Nouveau patient** : Cliquez sur "➕ Nouveau Patient" dans le menu
4. **Ajout d'épisode** : Depuis la fiche patient, ajoutez des épisodes avec imagerie et biologie
5. **Inférence** : Cliquez sur "🧮 Calculer le type de calcul" pour obtenir une analyse par algorithme

## 💡 Cas d'usage typique

1. **Création du dossier patient** avec toutes les informations médicales
2. **Ajout d'un épisode** lors d'une colique néphrétique ou consultation
3. **Saisie des résultats d'imagerie** (uro-scanner avec tous les détails)
4. **Saisie des résultats biologiques** (pH, marqueurs métaboliques, ECBU)
5. **Calcul automatique** du type de calcul probable
6. **Consultation des recommandations** de traitement et prévention
7. **Export PDF** pour archivage ou partage avec le patient

## 🔐 Sécurité et confidentialité

- Toutes les données médicales sensibles sont chiffrées
- Conformité RGPD pour la protection des données personnelles
- Base de données SQLite sécurisée
- Session utilisateur avec timeout automatique

## 📊 Statistiques

Le tableau de bord affiche en temps réel :
- Nombre total de patients
- Nombre d'épisodes enregistrés
- IMC moyen des patients
- Nombre de dossiers prêts pour l'analyse par algorithme (avec données complètes)

## 🤝 Support

Pour toute question médicale ou technique, consultez la documentation complète dans le dossier `/docs`.
