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
- **Automatic IMC Calculation**: Body Mass Index calculation with color-coded classification.
- **Dashboard Analytics**: Real-time statistics including hypercalciuria prevalence tracking.
- **Role-Based Access Control**: Three-tier user role system (Admin, Médecin, Assistant) with granular permissions, automatic role presets, and security features.
- **Automated Database Management**: Automatic verification and initialization of the database schema, including auto-loading of comprehensive demo data in development mode.
- **Structured Field Input Infrastructure**: Centralized API for predefined medical options and client-side transformation of input fields into checkboxes/selects.
- **Enhanced Production Security**: Secure handling of admin account creation and warnings for default credentials.

## External Dependencies
- **Flask**: Web framework
- **SQLAlchemy**: ORM for database interaction
- **Cryptography (Fernet)**: Data encryption
- **Tailwind CSS**: Frontend styling
- **ReportLab**: PDF generation
- **SQLite**: Database
- **Werkzeug**: Password hashing (PBKDF2)
- **Flask-Login**: User authentication