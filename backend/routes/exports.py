from flask import Blueprint, request, jsonify, send_file
from flask_login import login_required
from backend.models import Patient
from backend.services import InferenceEngine
from backend.routes.search import search_patients
from datetime import datetime
import csv
import io
import qrcode
from reportlab.lib.pagesizes import A4, letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT

bp = Blueprint('exports', __name__)

@bp.route('/api/export/csv', methods=['POST'])
@login_required
def export_csv():
    filters = request.json
    response = search_patients()
    results = response.get_json()
    
    output = io.StringIO()
    writer = csv.writer(output)
    
    writer.writerow(['Patient', 'Date Naissance', 'Date Épisode', 'pH', 'Densité UH', 'Taille mm', 'Infection'])
    
    for result in results:
        writer.writerow([
            result['patient_nom'],
            result['date_naissance'],
            result['date_episode'],
            result['ph_urinaire'],
            result['densite_uh'],
            result['taille_mm'],
            'Oui' if result['infection'] else 'Non'
        ])
    
    output.seek(0)
    return send_file(
        io.BytesIO(output.getvalue().encode('utf-8')),
        mimetype='text/csv',
        as_attachment=True,
        download_name=f'lithiase_export_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
    )

@bp.route('/api/export/patients-csv', methods=['POST'])
@login_required
def export_patients_csv():
    patients = Patient.query.all()
    
    output = io.StringIO()
    writer = csv.writer(output)
    
    writer.writerow(['Code Patient', 'Nom', 'Prénom', 'Date Naissance', 'Sexe', 'Téléphone', 'Email', 'Nombre Épisodes'])
    
    for patient in patients:
        writer.writerow([
            patient.code_patient or '',
            patient.nom,
            patient.prenom,
            patient.date_naissance.strftime('%d/%m/%Y'),
            patient.sexe,
            patient.telephone or '',
            patient.email or '',
            len(patient.episodes)
        ])
    
    output.seek(0)
    return send_file(
        io.BytesIO(output.getvalue().encode('utf-8')),
        mimetype='text/csv',
        as_attachment=True,
        download_name=f'patients_liste_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
    )

@bp.route('/api/export/patients-list-pdf', methods=['POST'])
@login_required
def export_patients_list_pdf():
    patients = Patient.query.all()
    
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=1.5*cm, leftMargin=1.5*cm, topMargin=1.5*cm, bottomMargin=1.5*cm)
    
    story = []
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle('ListTitle', parent=styles['Heading1'], fontSize=18, textColor=colors.HexColor('#4F46E5'), spaceAfter=12, alignment=TA_CENTER)
    subtitle_style = ParagraphStyle('ListSubtitle', parent=styles['Normal'], fontSize=10, textColor=colors.HexColor('#6B7280'), spaceAfter=16, alignment=TA_CENTER)
    table_cell_style = ParagraphStyle('ListTableCell', parent=styles['Normal'], fontSize=8, leading=10, wordWrap='CJK')
    
    def wrap_text(text, style=table_cell_style):
        if text is None or text == '':
            return Paragraph('-', style)
        return Paragraph(str(text), style)
    
    story.append(Paragraph("📊 LISTE DES PATIENTS", title_style))
    story.append(Paragraph(f"Généré le {datetime.now().strftime('%d/%m/%Y à %H:%M')}", subtitle_style))
    story.append(Paragraph(f"Total: {len(patients)} patients", subtitle_style))
    story.append(Spacer(1, 0.5*cm))
    
    table_data = [[
        wrap_text('Code', table_cell_style),
        wrap_text('Nom', table_cell_style),
        wrap_text('Prénom', table_cell_style),
        wrap_text('Date naissance', table_cell_style),
        wrap_text('Sexe', table_cell_style),
        wrap_text('Téléphone', table_cell_style),
        wrap_text('Épisodes', table_cell_style)
    ]]
    
    for patient in patients:
        age = ''
        if patient.date_naissance:
            from datetime import date
            today = date.today()
            age_years = today.year - patient.date_naissance.year - ((today.month, today.day) < (patient.date_naissance.month, patient.date_naissance.day))
            age = f"{patient.date_naissance.strftime('%d/%m/%Y')} ({age_years} ans)"
        
        table_data.append([
            wrap_text(patient.code_patient or '-'),
            wrap_text(patient.nom),
            wrap_text(patient.prenom),
            wrap_text(age),
            wrap_text('♂' if patient.sexe == 'M' else '♀'),
            wrap_text(patient.telephone or '-'),
            wrap_text(str(len(patient.episodes)))
        ])
    
    t = Table(table_data, colWidths=[2.5*cm, 3.5*cm, 3.5*cm, 3.5*cm, 1*cm, 3*cm, 1.5*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4F46E5')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (4, 0), (4, -1), 'CENTER'),
        ('ALIGN', (6, 0), (6, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#C7D2FE')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F5F3FF')]),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
    ]))
    story.append(t)
    
    doc.build(story)
    buffer.seek(0)
    
    return send_file(
        buffer,
        mimetype='application/pdf',
        as_attachment=True,
        download_name=f'liste_patients_{datetime.now().strftime("%Y%m%d_%H%M%S")}.pdf'
    )

@bp.route('/api/patients/<int:patient_id>/export/pdf', methods=['GET'])
@login_required
def export_patient_pdf(patient_id):
    patient = Patient.query.get_or_404(patient_id)
    
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=1.5*cm, leftMargin=1.5*cm, topMargin=1.5*cm, bottomMargin=1.5*cm)
    
    story = []
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle('CustomTitle', parent=styles['Heading1'], fontSize=22, textColor=colors.HexColor('#4F46E5'), spaceAfter=6, alignment=TA_CENTER)
    subtitle_style = ParagraphStyle('Subtitle', parent=styles['Normal'], fontSize=11, textColor=colors.HexColor('#6B7280'), spaceAfter=12, alignment=TA_CENTER)
    section_title_style = ParagraphStyle('SectionTitle', parent=styles['Heading2'], fontSize=14, textColor=colors.HexColor('#1F2937'), spaceAfter=8, spaceBefore=12, leftIndent=10)
    code_style = ParagraphStyle('CodeStyle', parent=styles['Normal'], fontSize=9, textColor=colors.HexColor('#6B7280'), alignment=TA_CENTER, spaceAfter=4)
    table_cell_style = ParagraphStyle('TableCell', parent=styles['Normal'], fontSize=9, leading=11, wordWrap='CJK')
    table_cell_bold_style = ParagraphStyle('TableCellBold', parent=styles['Normal'], fontSize=9, leading=11, fontName='Helvetica-Bold', wordWrap='CJK')
    
    def wrap_text(text, style=table_cell_style):
        """Helper function to wrap text in Paragraph for proper word wrapping in tables"""
        if text is None or text == '':
            return Paragraph('-', style)
        return Paragraph(str(text), style)
    
    TABLE_WIDTH = 17*cm
    COL1_WIDTH = 6*cm
    COL2_WIDTH = 11*cm
    
    story.append(Paragraph("DOSSIER MÉDICAL PATIENT", title_style))
    story.append(Paragraph(f"{patient.nom} {patient.prenom}", subtitle_style))
    
    if patient.code_patient:
        qr = qrcode.QRCode(version=1, box_size=3, border=1)
        qr.add_data(patient.code_patient)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white")
        
        qr_buffer = io.BytesIO()
        qr_img.save(qr_buffer, format='PNG')
        qr_buffer.seek(0)
        
        qr_image = Image(qr_buffer, width=2.5*cm, height=2.5*cm)
        
        qr_data = [[qr_image, [Paragraph(f"<b>Code Patient</b>", code_style), 
                                Paragraph(f"{patient.code_patient}", code_style)]]]
        qr_table = Table(qr_data, colWidths=[3*cm, TABLE_WIDTH-3*cm])
        qr_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (0, 0), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('ALIGN', (1, 0), (1, 0), 'LEFT')
        ]))
        story.append(qr_table)
    
    story.append(Spacer(1, 0.3*cm))
    
    story.append(Paragraph("📋 INFORMATIONS PERSONNELLES", section_title_style))
    patient_data = [
        [wrap_text('Nom complet', table_cell_bold_style), wrap_text(f"{patient.nom} {patient.prenom}")],
        [wrap_text('Date de naissance', table_cell_bold_style), wrap_text(patient.date_naissance.strftime('%d/%m/%Y'))],
        [wrap_text('Sexe', table_cell_bold_style), wrap_text('Masculin' if patient.sexe == 'M' else 'Féminin')],
        [wrap_text('Téléphone', table_cell_bold_style), wrap_text(patient.telephone or '-')],
        [wrap_text('Email', table_cell_bold_style), wrap_text(patient.email or '-')],
        [wrap_text('Adresse', table_cell_bold_style), wrap_text(patient.adresse or '-')]
    ]
    
    if patient.poids:
        patient_data.append([wrap_text('Poids', table_cell_bold_style), wrap_text(f"{patient.poids} kg")])
    if patient.taille:
        patient_data.append([wrap_text('Taille', table_cell_bold_style), wrap_text(f"{patient.taille} cm")])
        if patient.poids:
            bmi = patient.poids / ((patient.taille/100) ** 2)
            patient_data.append([wrap_text('IMC', table_cell_bold_style), wrap_text(f"{bmi:.1f}")])
    if patient.groupe_ethnique:
        patient_data.append([wrap_text('Groupe ethnique', table_cell_bold_style), wrap_text(patient.groupe_ethnique)])
    
    t = Table(patient_data, colWidths=[COL1_WIDTH, COL2_WIDTH])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#EEF2FF')),
        ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor('#4338CA')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#C7D2FE')),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
    ]))
    story.append(t)
    story.append(Spacer(1, 0.5*cm))
    
    if any([patient.tension_arterielle_systolique, patient.tension_arterielle_diastolique, patient.frequence_cardiaque, patient.temperature, patient.frequence_respiratoire]):
        story.append(Paragraph("🩺 CONSTANTES VITALES", section_title_style))
        constantes_data = []
        if patient.tension_arterielle_systolique or patient.tension_arterielle_diastolique:
            ta_value = ''
            if patient.tension_arterielle_systolique and patient.tension_arterielle_diastolique:
                ta_value = f"{patient.tension_arterielle_systolique}/{patient.tension_arterielle_diastolique} mmHg"
            elif patient.tension_arterielle_systolique:
                ta_value = f"{patient.tension_arterielle_systolique} mmHg (systolique)"
            elif patient.tension_arterielle_diastolique:
                ta_value = f"{patient.tension_arterielle_diastolique} mmHg (diastolique)"
            constantes_data.append([wrap_text('Tension artérielle', table_cell_bold_style), wrap_text(ta_value)])
        if patient.frequence_cardiaque:
            constantes_data.append([wrap_text('Fréquence cardiaque', table_cell_bold_style), wrap_text(f"{patient.frequence_cardiaque} bpm")])
        if patient.temperature:
            constantes_data.append([wrap_text('Température', table_cell_bold_style), wrap_text(f"{patient.temperature} °C")])
        if patient.frequence_respiratoire:
            constantes_data.append([wrap_text('Fréquence respiratoire', table_cell_bold_style), wrap_text(f"{patient.frequence_respiratoire} /min")])
        
        t = Table(constantes_data, colWidths=[COL1_WIDTH, COL2_WIDTH])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#E0F2FE')),
            ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor('#075985')),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('TOPPADDING', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#7DD3FC')),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
        ]))
        story.append(t)
        story.append(Spacer(1, 0.5*cm))
    
    if any([patient.antecedents_personnels, patient.antecedents_familiaux, patient.antecedents_chirurgicaux, patient.allergies, patient.traitements_chroniques]):
        story.append(Paragraph("🏥 ANTÉCÉDENTS MÉDICAUX", section_title_style))
        medical_data = []
        if patient.antecedents_personnels:
            medical_data.append([wrap_text('Antécédents personnels', table_cell_bold_style), wrap_text(patient.antecedents_personnels)])
        if patient.antecedents_familiaux:
            medical_data.append([wrap_text('Antécédents familiaux', table_cell_bold_style), wrap_text(patient.antecedents_familiaux)])
        if patient.antecedents_chirurgicaux:
            medical_data.append([wrap_text('Antécédents chirurgicaux', table_cell_bold_style), wrap_text(patient.antecedents_chirurgicaux)])
        if patient.allergies:
            medical_data.append([wrap_text('Allergies', table_cell_bold_style), wrap_text(patient.allergies)])
        if patient.traitements_chroniques:
            medical_data.append([wrap_text('Traitements chroniques', table_cell_bold_style), wrap_text(patient.traitements_chroniques)])
        
        t = Table(medical_data, colWidths=[COL1_WIDTH, COL2_WIDTH])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#FEF3C7')),
            ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor('#92400E')),
            ('ALIGN', (0, 0), (0, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 9),
            ('TOPPADDING', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#FCD34D')),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
        ]))
        story.append(t)
        story.append(Spacer(1, 0.5*cm))
    
    if any([patient.hydratation_jour, patient.regime_alimentaire, patient.petit_dejeuner, patient.dejeuner, patient.diner]):
        story.append(Paragraph("🍽️ HABITUDES DE VIE & ALIMENTATION", section_title_style))
        lifestyle_data = []
        if patient.hydratation_jour:
            lifestyle_data.append([wrap_text('Hydratation', table_cell_bold_style), wrap_text(f"{patient.hydratation_jour} L/jour")])
        if patient.regime_alimentaire:
            lifestyle_data.append([wrap_text('Régime alimentaire', table_cell_bold_style), wrap_text(patient.regime_alimentaire)])
        if patient.petit_dejeuner:
            lifestyle_data.append([wrap_text('Petit déjeuner', table_cell_bold_style), wrap_text(patient.petit_dejeuner)])
        if patient.dejeuner:
            lifestyle_data.append([wrap_text('Déjeuner', table_cell_bold_style), wrap_text(patient.dejeuner)])
        if patient.diner:
            lifestyle_data.append([wrap_text('Dîner', table_cell_bold_style), wrap_text(patient.diner)])
        if patient.grignotage:
            lifestyle_data.append([wrap_text('Grignotage', table_cell_bold_style), wrap_text(patient.grignotage)])
        if patient.autres_consommations:
            lifestyle_data.append([wrap_text('Autres consommations', table_cell_bold_style), wrap_text(patient.autres_consommations)])
        
        t = Table(lifestyle_data, colWidths=[COL1_WIDTH, COL2_WIDTH])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#D1FAE5')),
            ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor('#065F46')),
            ('ALIGN', (0, 0), (0, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 9),
            ('TOPPADDING', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#6EE7B7')),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
        ]))
        story.append(t)
        story.append(Spacer(1, 0.5*cm))
    
    if patient.episodes:
        story.append(Paragraph("📊 ÉPISODES RÉCENTS", section_title_style))
        story.append(Spacer(1, 0.3*cm))
        
        for episode in sorted(patient.episodes, key=lambda x: x.date_episode, reverse=True):
            story.append(Paragraph(f"<b>Épisode du {episode.date_episode.strftime('%d/%m/%Y')}</b>", styles['Heading3']))
            story.append(Spacer(1, 0.2*cm))
            
            episode_data = []
            if episode.motif:
                episode_data.append([wrap_text('Motif:', table_cell_bold_style), wrap_text(episode.motif)])
            if episode.diagnostic:
                episode_data.append([wrap_text('Diagnostic:', table_cell_bold_style), wrap_text(episode.diagnostic)])
            
            if episode.douleur or episode.fievre or episode.infection_urinaire:
                symptoms = []
                if episode.douleur:
                    symptoms.append("Douleur")
                if episode.fievre:
                    symptoms.append("Fièvre")
                if episode.infection_urinaire:
                    symptoms.append("Infection urinaire")
                episode_data.append([wrap_text('Symptômes:', table_cell_bold_style), wrap_text(', '.join(symptoms))])
            
            if episode_data:
                t = Table(episode_data, colWidths=[COL1_WIDTH, COL2_WIDTH])
                t.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#DBEAFE')),
                    ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor('#1E40AF')),
                    ('ALIGN', (0, 0), (0, -1), 'LEFT'),
                    ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
                    ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
                    ('FONTSIZE', (0, 0), (-1, -1), 9),
                    ('TOPPADDING', (0, 0), (-1, -1), 8),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
                    ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#93C5FD')),
                    ('VALIGN', (0, 0), (-1, -1), 'TOP')
                ]))
                story.append(t)
                story.append(Spacer(1, 0.3*cm))
            
            if episode.imageries:
                story.append(Paragraph("<b>Imageries:</b>", styles['Heading4']))
                story.append(Spacer(1, 0.2*cm))
                for imaging in episode.imageries:
                    imaging_data = []
                    imaging_data.append([wrap_text('Date examen:', table_cell_bold_style), wrap_text(imaging.date_examen.strftime('%d/%m/%Y'))])
                    if imaging.asp_resultats:
                        imaging_data.append([wrap_text('ASP:', table_cell_bold_style), wrap_text(imaging.asp_resultats)])
                    if imaging.echographie_resultats:
                        imaging_data.append([wrap_text('Échographie:', table_cell_bold_style), wrap_text(imaging.echographie_resultats)])
                    if imaging.uroscanner_resultats:
                        imaging_data.append([wrap_text('Uro-scanner:', table_cell_bold_style), wrap_text(imaging.uroscanner_resultats)])
                    if imaging.nombre_calculs:
                        imaging_data.append([wrap_text('Nombre de calculs:', table_cell_bold_style), wrap_text(str(imaging.nombre_calculs))])
                    if imaging.topographie_calcul:
                        imaging_data.append([wrap_text('Topographie:', table_cell_bold_style), wrap_text(imaging.topographie_calcul)])
                    if imaging.diametre_longitudinal or imaging.diametre_transversal:
                        imaging_data.append([wrap_text('Dimensions:', table_cell_bold_style), wrap_text(f"{imaging.diametre_longitudinal or '-'} x {imaging.diametre_transversal or '-'} mm")])
                    if imaging.taille_mm:
                        imaging_data.append([wrap_text('Taille:', table_cell_bold_style), wrap_text(f"{imaging.taille_mm} mm")])
                    if imaging.forme_calcul:
                        imaging_data.append([wrap_text('Forme:', table_cell_bold_style), wrap_text(imaging.forme_calcul)])
                    if imaging.contour_calcul:
                        imaging_data.append([wrap_text('Contour:', table_cell_bold_style), wrap_text(imaging.contour_calcul)])
                    if imaging.densite_uh:
                        imaging_data.append([wrap_text('Densité:', table_cell_bold_style), wrap_text(f"{imaging.densite_uh} UH")])
                    if imaging.densite_noyau:
                        imaging_data.append([wrap_text('Densité noyau:', table_cell_bold_style), wrap_text(f"{imaging.densite_noyau} UH")])
                    if imaging.densites_couches:
                        imaging_data.append([wrap_text('Densités couches:', table_cell_bold_style), wrap_text(imaging.densites_couches)])
                    if imaging.morphologie:
                        imaging_data.append([wrap_text('Morphologie:', table_cell_bold_style), wrap_text(imaging.morphologie)])
                    if imaging.radio_opacite:
                        imaging_data.append([wrap_text('Radio-opacité:', table_cell_bold_style), wrap_text(imaging.radio_opacite)])
                    
                    if imaging_data:
                        t = Table(imaging_data, colWidths=[COL1_WIDTH, COL2_WIDTH])
                        t.setStyle(TableStyle([
                            ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#FEF3C7')),
                            ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor('#92400E')),
                            ('ALIGN', (0, 0), (0, -1), 'LEFT'),
                            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
                            ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
                            ('FONTSIZE', (0, 0), (-1, -1), 8),
                            ('TOPPADDING', (0, 0), (-1, -1), 6),
                            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
                            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#FDE68A')),
                            ('VALIGN', (0, 0), (-1, -1), 'TOP')
                        ]))
                        story.append(t)
                        story.append(Spacer(1, 0.2*cm))
                    
                    if any([imaging.rein_gauche_cranio_caudal, imaging.rein_gauche_volume, imaging.rein_droit_cranio_caudal, imaging.rein_droit_volume, imaging.epaisseur_cortex_renal_gauche, imaging.epaisseur_cortex_renal_droit, imaging.diametre_pyelon_gauche, imaging.diametre_pyelon_droit, imaging.diametre_uretere_amont_gauche, imaging.diametre_uretere_amont_droit]):
                        story.append(Paragraph("<b>Mesures uroscanner - Retentissement haut appareil:</b>", styles['Heading4']))
                        story.append(Spacer(1, 0.1*cm))
                        reins_data = [[wrap_text('Paramètre', table_cell_bold_style), wrap_text('Rein gauche', table_cell_bold_style), wrap_text('Rein droit', table_cell_bold_style)]]
                        if imaging.rein_gauche_cranio_caudal or imaging.rein_droit_cranio_caudal:
                            reins_data.append([wrap_text('Cranio-caudal'), wrap_text(f"{imaging.rein_gauche_cranio_caudal or '-'} mm"), wrap_text(f"{imaging.rein_droit_cranio_caudal or '-'} mm")])
                        if imaging.rein_gauche_antero_posterieur or imaging.rein_droit_antero_posterieur:
                            reins_data.append([wrap_text('Antéro-postérieur'), wrap_text(f"{imaging.rein_gauche_antero_posterieur or '-'} mm"), wrap_text(f"{imaging.rein_droit_antero_posterieur or '-'} mm")])
                        if imaging.rein_gauche_transversal or imaging.rein_droit_transversal:
                            reins_data.append([wrap_text('Transversal'), wrap_text(f"{imaging.rein_gauche_transversal or '-'} mm"), wrap_text(f"{imaging.rein_droit_transversal or '-'} mm")])
                        if imaging.rein_gauche_volume or imaging.rein_droit_volume:
                            reins_data.append([wrap_text('Volume'), wrap_text(f"{imaging.rein_gauche_volume or '-'} cm³"), wrap_text(f"{imaging.rein_droit_volume or '-'} cm³")])
                        if imaging.epaisseur_cortex_renal_gauche or imaging.epaisseur_cortex_renal_droit:
                            reins_data.append([wrap_text('Épaisseur cortex'), wrap_text(f"{imaging.epaisseur_cortex_renal_gauche or '-'} mm"), wrap_text(f"{imaging.epaisseur_cortex_renal_droit or '-'} mm")])
                        if imaging.diametre_pyelon_gauche or imaging.diametre_pyelon_droit:
                            reins_data.append([wrap_text('Diamètre pyélon'), wrap_text(f"{imaging.diametre_pyelon_gauche or '-'} mm"), wrap_text(f"{imaging.diametre_pyelon_droit or '-'} mm")])
                        if imaging.diametre_uretere_amont_gauche or imaging.diametre_uretere_amont_droit:
                            reins_data.append([wrap_text('Diamètre uretère amont'), wrap_text(f"{imaging.diametre_uretere_amont_gauche or '-'} mm"), wrap_text(f"{imaging.diametre_uretere_amont_droit or '-'} mm")])
                        
                        if len(reins_data) > 1:
                            t_reins = Table(reins_data, colWidths=[5*cm, 5*cm, 5*cm])
                            t_reins.setStyle(TableStyle([
                                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#A78BFA')),
                                ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                ('FONTSIZE', (0, 0), (-1, -1), 8),
                                ('TOPPADDING', (0, 0), (-1, -1), 6),
                                ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
                                ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#C4B5FD'))
                            ]))
                            story.append(Spacer(1, 0.1*cm))
                            story.append(t_reins)
                        
                        if imaging.malformations_urinaires:
                            story.append(wrap_text(f"    Malformations: {imaging.malformations_urinaires}"))
            
            if episode.biologies:
                story.append(Paragraph("<b>Biologies:</b>", styles['Heading4']))
                story.append(Spacer(1, 0.2*cm))
                for biology in episode.biologies:
                    biology_data = []
                    biology_data.append([wrap_text('Date examen:', table_cell_bold_style), wrap_text(biology.date_examen.strftime('%d/%m/%Y'))])
                    if biology.ph_urinaire:
                        biology_data.append([wrap_text('pH urinaire:', table_cell_bold_style), wrap_text(str(biology.ph_urinaire))])
                    if biology.densite_urinaire:
                        biology_data.append([wrap_text('Densité urinaire:', table_cell_bold_style), wrap_text(str(biology.densite_urinaire))])
                    if biology.sediment_urinaire:
                        biology_data.append([wrap_text('Sédiment:', table_cell_bold_style), wrap_text(biology.sediment_urinaire)])
                    if biology.ecbu_resultats:
                        biology_data.append([wrap_text('ECBU:', table_cell_bold_style), wrap_text(biology.ecbu_resultats)])
                    
                    markers = []
                    if biology.hyperoxalurie:
                        markers.append(f"Hyperoxalurie{' (' + str(biology.oxalurie_valeur) + ' mg/24h)' if biology.oxalurie_valeur else ''}")
                    if biology.hypercalciurie:
                        markers.append(f"Hypercalciurie{' (' + str(biology.calciurie_valeur) + ' mg/24h)' if biology.calciurie_valeur else ''}")
                    if biology.hyperuricurie:
                        markers.append("Hyperuricurie")
                    if biology.cystinurie:
                        markers.append("Cystinurie")
                    if biology.hypercalcemie:
                        markers.append(f"Hypercalcémie{' (' + str(biology.calciemie_valeur) + ' mmol/L)' if biology.calciemie_valeur else ''}")
                    if markers:
                        biology_data.append([wrap_text('Marqueurs métaboliques:', table_cell_bold_style), wrap_text(', '.join(markers))])
                    
                    thyroid = []
                    if biology.tsh is not None:
                        thyroid.append(f"TSH: {biology.tsh} mUI/L")
                    if biology.t3:
                        thyroid.append(f"T3: {biology.t3} pg/mL")
                    if biology.t4:
                        thyroid.append(f"T4: {biology.t4} ng/dL")
                    if thyroid:
                        biology_data.append([wrap_text('Hormones thyroïdiennes:', table_cell_bold_style), wrap_text(', '.join(thyroid))])
                    
                    renal = []
                    if biology.uree is not None:
                        renal.append(f"Urée: {biology.uree} g/L")
                    if biology.creatinine is not None:
                        renal.append(f"Créatinine: {biology.creatinine} mg/L")
                    if renal:
                        biology_data.append([wrap_text('Fonction rénale:', table_cell_bold_style), wrap_text(', '.join(renal))])
                    
                    if biology.infection_urinaire:
                        infection_parts = ["Oui"]
                        if biology.germe:
                            infection_parts.append(f"Germe: {biology.germe}")
                        if biology.germe_urease:
                            infection_parts.append(f"Germe à uréase: {biology.germe_urease}")
                        biology_data.append([wrap_text('Infection urinaire:', table_cell_bold_style), wrap_text(' - '.join(infection_parts))])
                    
                    if biology_data:
                        t = Table(biology_data, colWidths=[COL1_WIDTH, COL2_WIDTH])
                        t.setStyle(TableStyle([
                            ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#D1FAE5')),
                            ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor('#065F46')),
                            ('ALIGN', (0, 0), (0, -1), 'LEFT'),
                            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
                            ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
                            ('FONTSIZE', (0, 0), (-1, -1), 8),
                            ('TOPPADDING', (0, 0), (-1, -1), 6),
                            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
                            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#6EE7B7')),
                            ('VALIGN', (0, 0), (-1, -1), 'TOP')
                        ]))
                        story.append(t)
                        story.append(Spacer(1, 0.3*cm))
            
            if episode.calculated_stone_type and episode.calculated_stone_type_data:
                import json
                result = json.loads(episode.calculated_stone_type_data)
                
                composition_type = result.get('composition_type', 'Non déterminé')
                composition_detail = result.get('composition_detail', result['top_1'])
                
                result_data = [
                    [wrap_text('RÉSULTAT D\'ANALYSE (ALGORITHME KALONJI)', table_cell_bold_style), wrap_text('')],
                    [wrap_text('Nature morpho-constitutionnelle', table_cell_bold_style), wrap_text(composition_detail)],
                    [wrap_text('Type de composition', table_cell_bold_style), wrap_text(composition_type)],
                    [wrap_text('Score de confiance', table_cell_bold_style), wrap_text(f"{result['top_1_score']}/20")],
                    [wrap_text('LEC éligible', table_cell_bold_style), wrap_text('Oui' if result.get('lec_eligible') else 'Non')],
                    [wrap_text('Voie de traitement', table_cell_bold_style), wrap_text(result.get('voie_traitement', '-'))],
                ]
                
                t = Table(result_data, colWidths=[COL1_WIDTH, COL2_WIDTH])
                t.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#7C3AED')),
                    ('BACKGROUND', (0, 1), (0, -1), colors.HexColor('#EDE9FE')),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                    ('TEXTCOLOR', (0, 1), (0, -1), colors.HexColor('#5B21B6')),
                    ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
                    ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('FONTNAME', (0, 1), (0, -1), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 0), (-1, 0), 11),
                    ('FONTSIZE', (0, 1), (-1, -1), 9),
                    ('TOPPADDING', (0, 0), (-1, -1), 10),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
                    ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#A78BFA')),
                    ('SPAN', (0, 0), (-1, 0)),
                    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
                ]))
                story.append(t)
                story.append(Spacer(1, 0.2*cm))
                
                if result.get('top_3'):
                    top3_data = [[wrap_text('Top 3 types probables', table_cell_bold_style), wrap_text('Score', table_cell_bold_style)]]
                    for type_calcul, score, reasons in result['top_3']:
                        top3_data.append([wrap_text(type_calcul), wrap_text(f"{score}/20")])
                    
                    t2 = Table(top3_data, colWidths=[COL2_WIDTH, COL1_WIDTH])
                    t2.setStyle(TableStyle([
                        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#A78BFA')),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                        ('ALIGN', (1, 0), (1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('FONTSIZE', (0, 0), (-1, -1), 9),
                        ('TOPPADDING', (0, 0), (-1, -1), 8),
                        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
                        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#C4B5FD'))
                    ]))
                    story.append(t2)
                
                if result.get('prevention'):
                    story.append(Spacer(1, 0.2*cm))
                    story.append(wrap_text("<b>Conseils de prévention:</b>"))
                    for conseil in result['prevention'][:5]:
                        story.append(wrap_text(f"  • {conseil}"))
            
            story.append(Spacer(1, 0.3*cm))
    
    doc.build(story)
    buffer.seek(0)
    
    return send_file(
        buffer,
        mimetype='application/pdf',
        as_attachment=True,
        download_name=f'dossier_{patient.nom}_{patient.prenom}_{datetime.now().strftime("%Y%m%d")}.pdf'
    )
