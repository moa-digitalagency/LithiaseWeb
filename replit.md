# Algorithme Lithiase KALONJI - Application médicale de gestion de calculs rénaux

## Overview
Algorithme Lithiase KALONJI is a single-physician web application designed for managing patient records related to lithiasis (kidney stones). The application facilitates comprehensive patient data entry, utilizes an inference engine to propose kidney stone types, and generates detailed PDF reports. Its core purpose is to streamline the management and analysis of kidney stone cases, offering a robust tool for medical professionals. The project aims to provide a comprehensive, secure, and user-friendly system for medical data management with advanced analytical capabilities, including business vision, market potential, and project ambitions for a medical data management system with advanced analytical capabilities.

## User Preferences
I want iterative development.
Ask before making major changes.
I prefer detailed explanations.
Do not make changes to the folder `Z`.
Do not make changes to the file `Y`.

## System Architecture
The application uses a Flask (Python 3.11) backend with SQLAlchemy ORM for database interactions. The frontend is built with HTML/CSS, styled using Tailwind CSS, and enhanced with vanilla JavaScript. Data security is paramount, employing Cryptography (Fernet AES-128 + HMAC) for encrypting over 25 sensitive health data fields. The system integrates a sophisticated inference engine capable of classifying 8 types of kidney stones, distinguishing between "Pure" and "Mixed" compositions based on detailed scoring, including hyperthyroidism and hypercalcemia impact. UI/UX follows the MyOneArt design system, featuring an indigo-purple palette, rounded borders, and friendly emojis for a modern and professional appearance.

### Key Features
- **Complete Patient CRUD**: Full create, read, update, and delete operations for patient records with comprehensive data management.
- **Medical Episode Tracking**: Ability to create and manage multiple medical episodes per patient with complete biological and imaging data.
- **Advanced Biological Data Management**: Per-episode tracking of thyroid hormones (T3, T4, TSH) and calcium metabolism (calciuria, calciemia, oxaluria) with automatic threshold-based flagging and hyperthyroidism detection.
- **Intelligent Metabolic Calculation**: Automatic derivation of metabolic abnormalities (hyperoxalurie, hypercalciurie, hypercalcemie) from numeric lab values using gender-specific medical thresholds.
- **Enhanced Inference Algorithm**: 8 kidney stone type classification with Pure vs. Mixed composition distinction, detailed justification, and scoring bonuses based on metabolic and endocrine status.
- **Advanced Search & Export**: Search functionality across patient data and generation of detailed PDF reports (with professional layout, color-coded sections, and radial structure information) and CSV exports.
- **Automatic Age & IMC Calculation**: Automatic calculation of patient age from date of birth and Body Mass Index with color-coded classification.
- **Dashboard Analytics**: Real-time statistics including hypercalciuria prevalence tracking.
- **Role-Based Access Control**: Three-tier user role system (Admin, Médecin, Assistant) with granular permissions, automatic role presets, and security features. Admin users have full access to user management settings.
- **Automated Database Management**: Automatic verification and initialization of the database schema with intelligent table detection and creation, including auto-loading of comprehensive demo data in development mode. Automatic admin privilege assignment and upgrade for existing users.
- **Structured Field Input Infrastructure**: Centralized API for predefined medical options and client-side transformation of input fields into checkboxes/selects.
- **Enhanced Production Security**: Secure handling of admin account creation and warnings for default credentials.
- **Privacy-Focused Patient Display**: Patient information displays name and calculated age prominently while protecting sensitive demographic data (birth date and gender removed from main display).

## External Dependencies
- **Flask**: Web framework
- **SQLAlchemy**: ORM for database interaction with PostgreSQL
- **Cryptography (Fernet)**: Data encryption for sensitive health data
- **Tailwind CSS**: Frontend styling
- **ReportLab**: PDF generation
- **PostgreSQL (Neon)**: Production database
- **Werkzeug**: Password hashing (PBKDF2)
- **Flask-Login**: User authentication
- **psycopg2-binary**: PostgreSQL adapter

## Recent Changes (November 13, 2025)

### UI/UX Improvements
- **Patient Information Display**: Reorganized personal information section to prominently display full name and calculated age at the top
- **Privacy Enhancement**: Removed gender and birth date from main patient information display for better privacy protection
- **Age Calculation**: Implemented automatic age calculation from birth date with accurate leap year handling

### Admin Access & Permissions
- **Admin Privileges**: Fixed admin user creation to ensure `can_manage_users` permission is properly set
- **Automatic Privilege Upgrade**: Added intelligent detection and upgrade of existing admin users who lack proper permissions
- **User Management Access**: Admin users now have full access to user management settings in the application

### Database Management
- **Comprehensive Table Verification**: Enhanced `verify_and_init_db.py` to check all current tables and create missing ones automatically
- **Smart Admin Management**: Improved admin user creation and privilege assignment across all initialization scripts
- **Startup Permission Check**: Added `verify_and_fix_admin_permissions()` function that runs at every startup to ensure admin privileges are always correct
- **Demo Data Enhancement**: Updated demo data loading to ensure proper admin role and permissions assignment
- **Schema Flexibility**: Made `date_naissance` and `sexe` fields nullable in the database to support privacy-focused data collection

### Security & Encryption
- **Encryption Key Migration**: Migrated encryption key management from file-based (`.encryption_key`) to Replit Secrets
- **Secure Key Storage**: Application now uses `ENCRYPTION_KEY` secret from Replit for production-ready security
- **Migration Support**: Temporary file backup during migration to prevent data loss
- **Clear Instructions**: Enhanced startup messages guide users through secret configuration process

### Deployment Improvements
- **Automatic Privilege Enforcement**: Admin permissions are now verified and corrected at every application startup
- **Permission Visibility**: All admin permissions are logged at startup for transparency and debugging
- **Robust Initialization**: Multi-step verification process ensures database schema, admin privileges, and demo data are all correctly configured