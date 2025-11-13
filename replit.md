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

#### Database & Form Enhancements (Nov 9 - Current Session)
- **Database Migration Consolidation**: Consolidated multiple migration scripts into a single `init_db.py` that drops and recreates the entire schema with demo data
  - Single command execution: `python init_db.py`
  - Clears all existing tables and data
  - Seeds 5 comprehensive demo patients with complete medical data
  - Ensures clean development environment setup
- **Ethnic Group Cleanup**: Removed "Rwanda" from ethnic group dropdown options in patient registration forms
- **Enhanced Form Dropdowns**: Added consistent dropdown menus with predefined options for:
  - Stone morphology (Ia, Ib, IIa, IIb, IIIa, IIIb, IVa, IVb)
  - Stone contour (Lisse, Rugueux, Mamelonné, Hérissé)
  - Radio-opacity levels (Faible, Modérée, Forte, Très forte)
  - Malformation types (Rein en fer à cheval, Duplicité urétérale, Sténose jonction pyélo-urétérale, etc.)
- **Flexible Topography Input**: Changed topography field from restrictive dropdown to text input with datalist suggestions
  - Preserves legacy values like "Calice inférieur droit" that exist in demo data
  - Suggests common anatomical locations while allowing free-text entry
  - Prevents data loss during patient editing
- **PDF Text Wrapping**: Applied comprehensive `wrap_text()` helper to all PDF table cells
  - Personal information section with Paragraph wrapping
  - Vital signs data with proper line breaks
  - Medical history and lifestyle factors
  - Analysis results and inference justifications
  - Prevents text overflow in long addresses, medical narratives, and imaging descriptions

#### PDF Export Enhancements (Nov 13 - Current Session)
- **Professional PDF Header Redesign**: 
  - Main title "DOSSIER MÉDICAL PATIENT" now prominently displayed at top (fontSize 20, centered, indigo color)
  - Two-column layout below title: QR Code (4cm) + patient information (13cm)
  - QR Code sized at 2.8cm to fit properly with padding (8pt)
  - Patient info includes name, age, and latest inference result in green
  - Complete bordered frame for professional appearance
- **Standardized Table Widths**:
  - All PDF tables now use consistent TABLE_WIDTH (17cm) for perfect alignment
  - Uroscanner measurements table uses equal column distribution (17cm ÷ 3)
  - Two-column tables maintain COL1_WIDTH (6cm) + COL2_WIDTH (11cm)
- **Comprehensive Inference Justification Tables**:
  - General justification table displays main reasoning (yellow background)
  - Detailed Top 3 tables show complete reasoning for each stone type prediction
  - Each Top 3 entry includes stone name, score, and bulleted list of all reasons
  - Purple color-coded design for inference sections
- **Always-Visible Fallback Tables**:
  - "Malformations urinaires" table always displayed (moved outside uroscanner conditional)
  - "Conseils de prévention" table always displayed regardless of data availability
  - Both show "Information pas disponible" when data is missing
  - Ensures complete and consistent PDF structure across all patient reports

#### Demo Data & Documentation Enhancement (Nov 9 - Latest)
- **Comprehensive Demo Dataset**: Created `init_demo_data.py` with 5 highly detailed patient cases
  - **Joseph Kabongo** - Whewellite (hyperoxalurie primaire, densité 1450 UH, pH 5.4)
  - **Françoise Mwamba** - Struvite (infection Proteus mirabilis, calcul coralliforme 45mm, pH 7.8)
  - **Marcel Tshilombo** - Acide urique (syndrome métabolique, obésité IMC 33, hyperuricurie 1250 mg/24h, pH 5.0)
  - **Marie Kasongo** - Weddellite (hyperoxalurie entérique post-résection iléale, 12 calculs bilatéraux, oxalurie 95 mg/24h)
  - **Pierre Ngoy** - Brushite (hyperparathyroïdie primaire, hypercalcémie 2.98 mmol/L, PTH 185 pg/mL)
  - All patients include complete demographics, vital signs, medical history, lifestyle habits, imaging results, and biological markers
  - Each patient represents a specific clinical archetype with coherent pathophysiology
- **Professional PDF Generator**: Created `generate_scientific_pdf.py` for scientific documentation
  - **FIXED**: Corrected format_text() function to eliminate ALL markdown artifacts (**, `, emojis)
  - Uses temporary markers (__BOLD_START__, etc.) to avoid XML escaping conflicts
  - Extended emoji removal pattern for comprehensive Unicode symbol cleanup
  - Professional ReportLab PLATYPUS formatting with custom styles
  - Structured page layout with title page, section headings (H2-H4), and page numbers
  - Color-coded tables with professional styling
  - Bibliography references formatted with bold numbering
  - No conflicts with existing ReportLab styles (all custom styles prefixed with "Custom")
- **Scientific Bibliography**: 40 peer-reviewed references with DOIs organized in 10 thematic categories
  - Composition and classification (5 refs)
  - CT density and imaging (5 refs)
  - Pathophysiology and risk factors (5 refs)
  - Biological and metabolic markers (5 refs)
  - Infections and struvite stones (3 refs)
  - Cystine stones (2 refs)
  - Clinical and therapeutic guidelines (4 refs)
  - Prevention and dietetics (4 refs)
  - Epidemiology (3 refs)
  - Thyroid and lithiasis (2 refs)
  - Malformations and uropathies (2 refs)

#### Automated Database Management & Field Enhancements (Nov 9 - Current Session)
- **Automatic Database Verification System** (`verify_and_init_db.py`)
  - Runs automatically at startup to verify complete database schema
  - Checks all 6 tables (users, patients, episodes, imageries, biologies, documents)
  - Validates presence of all columns (56 patient columns, 25 episode columns, etc.)
  - **Auto-loads demo data** if database is empty (5 comprehensive patient records)
  - **PRODUCTION SECURITY**: Gated behind FLASK_ENV='development' or ENABLE_AUTO_DEMO_DATA='true'
  - Never exposes default credentials in production environment
  
- **Structured Field Input Infrastructure**
  - **Field Options API** (`backend/field_options.py` + `backend/routes/field_options_api.py`)
    - Centralized constants for all predefined medical options
    - 14 checkbox fields (multi-select): antécédents familiaux, personnels, chirurgicaux, allergies, etc.
    - 2 select fields (single choice): regime_alimentaire, autres_consommations
    - RESTful endpoint `/api/field-options` for dynamic field configuration
  - **Client-Side Field Transformer** (`static/js/form-field-enhancer.js`)
    - Automatically transforms text inputs into checkboxes/selects based on server configuration
    - Preserves existing data during transformation
    - Handles semicolon-delimited multi-select values
    - Applied to patient registration form (`templates/nouveau-patient.html`)
  
- **Enhanced Production Security**
  - Default admin account creation ONLY in development mode
  - Production deployments require manual admin account creation
  - Clear warnings when default credentials are used
  - Environment variable override: ADMIN_USERNAME and ADMIN_PASSWORD

## External Dependencies
- **Flask**: Web framework
- **SQLAlchemy**: ORM for database interaction
- **Cryptography (Fernet)**: Data encryption
- **Tailwind CSS**: Frontend styling
- **ReportLab**: PDF generation
- **SQLite**: Database
- **Werkzeug**: Password hashing (PBKDF2)
- **Flask-Login**: User authentication