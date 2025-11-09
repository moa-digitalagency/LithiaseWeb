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
- **Medical Episode Tracking**: Ability to create and manage multiple medical episodes per patient
- **Advanced Search**: Search functionality across patient data
- **PDF/CSV Export**: Generate detailed PDF reports and CSV exports
- **Automatic IMC Calculation**: Body Mass Index calculation with color-coded classification
- **Inference Algorithm**: Integrated explanation system for kidney stone type classification

### Recent Changes (November 2025)
- Application renamed from "Lithiase" to "Algorithme Lithiase KALONJI" across all templates and documentation
- Implemented complete patient editing functionality with modal containing ALL patient fields (~30+ attributes)
- Added patient deletion functionality with confirmation modal and cascade deletion of related data
- Enhanced patient detail page (patient.html) with Edit and Delete buttons
- Validated full data persistence in edit operations with no field loss

## External Dependencies
- **Flask**: Web framework
- **SQLAlchemy**: ORM for database interaction
- **Cryptography (Fernet)**: Data encryption
- **Tailwind CSS**: Frontend styling
- **ReportLab**: PDF generation
- **SQLite**: Database
- **Werkzeug**: Password hashing (PBKDF2)
- **Flask-Login**: User authentication