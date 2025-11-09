# Algorithme Lithiase KALONJI - Application médicale de gestion de calculs rénaux

## Overview
Algorithme Lithiase KALONJI is a single-physician web application designed for managing patient records related to lithiasis (kidney stones). The application facilitates comprehensive patient data entry, utilizes an inference engine to propose kidney stone types, and generates detailed PDF reports. Its core purpose is to streamline the management and analysis of kidney stone cases, offering a robust tool for medical professionals. The project aims to provide a comprehensive, secure, and user-friendly system for medical data management with advanced analytical capabilities.

## User Preferences
I want iterative development.
Ask before making major changes.
I prefer detailed explanations.
Do not make changes to the folder `Z`.
Do not make changes to the file `Y`.

## System Architecture
The application uses a Flask (Python 3.11) backend with SQLAlchemy ORM for database interactions. The frontend is built with HTML/CSS, styled using Tailwind CSS, and enhanced with vanilla JavaScript. Data security is paramount, employing Cryptography (Fernet AES-128 + HMAC) for encrypting over 25 sensitive health data fields. The system integrates a sophisticated inference engine capable of classifying 8 types of kidney stones, distinguishing between "Pure" and "Mixed" compositions based on detailed scoring. UI/UX follows the MyOneArt design system, featuring an indigo-purple palette, rounded borders, and friendly emojis for a modern and professional appearance.

### Key Features
- **Complete Patient CRUD**: Full create, read, update, and delete operations for patient records with comprehensive data management
- **Medical Episode Tracking**: Ability to create and manage multiple medical episodes per patient with complete biological and imaging data
- **Advanced Biological Data Management**: Per-episode tracking of:
  - Thyroid hormones (T3, T4, TSH) with hyperthyroidism detection
  - Calcium metabolism (calciuria, calciemia, oxaluria) with automatic threshold-based flagging
  - Urinary infection status with germ identification
- **Intelligent Metabolic Calculation**: Automatic derivation of metabolic abnormalities (hyperoxalurie, hypercalciurie, hypercalcemie) from numeric lab values using gender-specific medical thresholds
- **Enhanced Inference Algorithm**: 
  - 8 kidney stone type classification with Pure vs. Mixed composition distinction
  - Hyperthyroidism impact on hypercalciuria scoring (+1 bonus)
  - Hypercalcemia bonus for calcium-related stone types
  - Detailed justification with metabolic markers and endocrine status
- **Advanced Search**: Search functionality across patient data
- **PDF/CSV Export**: Generate detailed PDF reports with thyroid/metabolic data and CSV exports
- **Automatic IMC Calculation**: Body Mass Index calculation with color-coded classification
- **Dashboard Analytics**: Real-time statistics including hypercalciuria prevalence tracking

### Recent Changes (November 2025)

#### Core Application Features
- Application renamed from "Lithiase" to "Algorithme Lithiase KALONJI" across all templates and documentation
- Implemented complete patient editing functionality with modal containing ALL patient fields (~30+ attributes)
- Added patient deletion functionality with confirmation modal and cascade deletion of related data
- Enhanced patient detail page (patient.html) with Edit and Delete buttons
- Validated full data persistence in edit operations with no field loss

#### Imaging & Inference Enhancements (Nov 9)
- **Enhanced Imaging Data**: Extended imaging API to include all new fields (densite_noyau, densites_couches, topographie_calcul, forme_calcul, contour_calcul, calcifications_autres, etc.) in both list and detail endpoints
- **Inference Algorithm Enhancement**: Modified inference engine to detect and explain radial structure in mixed stones, displaying nucleus and layer densities in justification (e.g., "Structure radiaire détectée: noyau 980 UH, couches périphériques (720 UH, 640 UH)")
- **Demo Data Upgrade**: Created comprehensive demo dataset with 5 patients including new patient "Pierre Rousseau" showcasing mixed stone with radial structure, all patients now include complete imaging data with nucleus/layer densities
- **Professional PDF Design**: Complete redesign with color-coded sections (blue: personal info, yellow: medical history, green: lifestyle, purple: analysis results), structured tables, and comprehensive result display including radial structure information

#### Biological Data & Metabolic Markers Integration (Nov 9 - Latest)
- **Thyroid Hormone Tracking**: Added per-episode tracking of T3, T4, and TSH levels in Biologie model
- **Calcium Metabolism Markers**: Integrated calciuria (mg/24h), calciemia (mmol/L), and oxaluria (mg/24h) numeric values with automatic threshold-based calculation
- **Automatic Metabolic Boolean Derivation**: Created centralized utility (backend/utils/biologies.py) that automatically calculates hyperoxalurie, hypercalciurie, and hypercalcemie flags based on gender-specific thresholds:
  - Hyperoxalurie: >45 mg/24h
  - Hypercalciurie: >300 mg/24h (men), >250 mg/24h (women)
  - Hypercalcemia: >2.6 mmol/L
- **Hyperthyroidism Detection**: Enhanced inference algorithm with detect_hyperthyroidism() function that identifies thyroid dysfunction (TSH <0.4 AND (T3 >2.0 OR T4 >12.0))
- **Inference Scoring Bonuses**: Algorithm now awards +1 point for hypercalciuria when hyperthyroidism is detected, and +1 point when hypercalcemia is present with calcium-related stone types
- **Patient Registration Enhancement**: Modified patient creation workflow to automatically create initial episode ("Bilan initial") and biologie entry when biological data is provided during registration
- **UI Updates**: Enhanced patient.html and nouveau-patient.html forms to collect thyroid hormones and metabolic markers with appropriate units and hints
- **PDF Export Enhancement**: Updated PDF reports to include thyroid hormone data and numeric metabolic values alongside boolean flags
- **Dashboard Statistics**: Added new "Hypercalciurie" statistic card showing number of patients with elevated urinary calcium
- **Demo Data Enrichment**: All 5 demo patients now include complete thyroid and metabolic data with realistic clinical values

## External Dependencies
- **Flask**: Web framework
- **SQLAlchemy**: ORM for database interaction
- **Cryptography (Fernet)**: Data encryption
- **Tailwind CSS**: Frontend styling
- **ReportLab**: PDF generation
- **SQLite**: Database
- **Werkzeug**: Password hashing (PBKDF2)
- **Flask-Login**: User authentication