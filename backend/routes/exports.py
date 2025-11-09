from flask import Blueprint, request, jsonify, send_file
from flask_login import login_required
from backend.models import Patient
from backend.inference import InferenceEngine
from backend.routes.search import search_patients
from datetime import datetime
import csv
import io
from reportlab.lib.pagesizes import A4, letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
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
    
    story.append(Paragraph("DOSSIER MÉDICAL PATIENT", title_style))
    story.append(Paragraph(f"{patient.nom} {patient.prenom}", subtitle_style))
    story.append(Spacer(1, 0.3*cm))
    
    story.append(Paragraph("📋 INFORMATIONS PERSONNELLES", section_title_style))
    patient_data = [
        ['Nom complet', f"{patient.nom} {patient.prenom}"],
        ['Date de naissance', patient.date_naissance.strftime('%d/%m/%Y')],
        ['Sexe', 'Masculin' if patient.sexe == 'M' else 'Féminin'],
        ['Téléphone', patient.telephone or '-'],
        ['Email', patient.email or '-'],
        ['Adresse', patient.adresse or '-']
    ]
    
    if patient.poids:
        patient_data.append(['Poids', f"{patient.poids} kg"])
    if patient.taille:
        patient_data.append(['Taille', f"{patient.taille} cm"])
        if patient.poids:
            bmi = patient.poids / ((patient.taille/100) ** 2)
            patient_data.append(['IMC', f"{bmi:.1f}"])
    if patient.groupe_ethnique:
        patient_data.append(['Groupe ethnique', patient.groupe_ethnique])
    
    t = Table(patient_data, colWidths=[6*cm, 11*cm])
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
    
    if any([patient.antecedents_personnels, patient.antecedents_familiaux, patient.antecedents_chirurgicaux, patient.allergies, patient.traitements_chroniques]):
        story.append(Paragraph("🏥 ANTÉCÉDENTS MÉDICAUX", section_title_style))
        medical_data = []
        if patient.antecedents_personnels:
            medical_data.append(['Antécédents personnels', patient.antecedents_personnels])
        if patient.antecedents_familiaux:
            medical_data.append(['Antécédents familiaux', patient.antecedents_familiaux])
        if patient.antecedents_chirurgicaux:
            medical_data.append(['Antécédents chirurgicaux', patient.antecedents_chirurgicaux])
        if patient.allergies:
            medical_data.append(['Allergies', patient.allergies])
        if patient.traitements_chroniques:
            medical_data.append(['Traitements chroniques', patient.traitements_chroniques])
        
        t = Table(medical_data, colWidths=[6*cm, 11*cm])
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
            lifestyle_data.append(['Hydratation', f"{patient.hydratation_jour} L/jour"])
        if patient.regime_alimentaire:
            lifestyle_data.append(['Régime alimentaire', patient.regime_alimentaire])
        if patient.petit_dejeuner:
            lifestyle_data.append(['Petit déjeuner', patient.petit_dejeuner])
        if patient.dejeuner:
            lifestyle_data.append(['Déjeuner', patient.dejeuner])
        if patient.diner:
            lifestyle_data.append(['Dîner', patient.diner])
        if patient.grignotage:
            lifestyle_data.append(['Grignotage', patient.grignotage])
        if patient.autres_consommations:
            lifestyle_data.append(['Autres consommations', patient.autres_consommations])
        
        t = Table(lifestyle_data, colWidths=[6*cm, 11*cm])
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
            if episode.motif:
                story.append(Paragraph(f"<b>Motif:</b> {episode.motif}", styles['Normal']))
            if episode.diagnostic:
                story.append(Paragraph(f"<b>Diagnostic:</b> {episode.diagnostic}", styles['Normal']))
            
            if episode.douleur or episode.fievre or episode.infection_urinaire:
                symptoms = []
                if episode.douleur:
                    symptoms.append("Douleur")
                if episode.fievre:
                    symptoms.append("Fièvre")
                if episode.infection_urinaire:
                    symptoms.append("Infection urinaire")
                story.append(Paragraph(f"<b>Symptômes:</b> {', '.join(symptoms)}", styles['Normal']))
            
            if episode.imageries:
                story.append(Paragraph("<b>Imageries:</b>", styles['Normal']))
                for imaging in episode.imageries:
                    story.append(Paragraph(f"  • Date: {imaging.date_examen.strftime('%d/%m/%Y')}", styles['Normal']))
                    if imaging.asp_resultats:
                        story.append(Paragraph(f"    ASP: {imaging.asp_resultats}", styles['Normal']))
                    if imaging.echographie_resultats:
                        story.append(Paragraph(f"    Échographie: {imaging.echographie_resultats}", styles['Normal']))
                    if imaging.uroscanner_resultats:
                        story.append(Paragraph(f"    Uro-scanner: {imaging.uroscanner_resultats}", styles['Normal']))
                    if imaging.nombre_calculs:
                        story.append(Paragraph(f"    Nombre de calculs: {imaging.nombre_calculs}", styles['Normal']))
                    if imaging.topographie_calcul:
                        story.append(Paragraph(f"    Topographie: {imaging.topographie_calcul}", styles['Normal']))
                    if imaging.diametre_longitudinal or imaging.diametre_transversal:
                        story.append(Paragraph(f"    Dimensions: {imaging.diametre_longitudinal or '-'} x {imaging.diametre_transversal or '-'} mm", styles['Normal']))
                    if imaging.taille_mm:
                        story.append(Paragraph(f"    Taille: {imaging.taille_mm} mm", styles['Normal']))
                    if imaging.forme_calcul:
                        story.append(Paragraph(f"    Forme: {imaging.forme_calcul}", styles['Normal']))
                    if imaging.contour_calcul:
                        story.append(Paragraph(f"    Contour: {imaging.contour_calcul}", styles['Normal']))
                    if imaging.densite_uh or imaging.densite_noyau:
                        story.append(Paragraph(f"    Densité: {imaging.densite_uh or imaging.densite_noyau} UH", styles['Normal']))
                    if imaging.densites_couches:
                        story.append(Paragraph(f"    Densités couches: {imaging.densites_couches}", styles['Normal']))
                    if imaging.morphologie:
                        story.append(Paragraph(f"    Morphologie: {imaging.morphologie}", styles['Normal']))
                    if imaging.radio_opacite:
                        story.append(Paragraph(f"    Radio-opacité: {imaging.radio_opacite}", styles['Normal']))
            
            if episode.biologies:
                story.append(Paragraph("<b>Biologies:</b>", styles['Normal']))
                for biology in episode.biologies:
                    story.append(Paragraph(f"  • Date: {biology.date_examen.strftime('%d/%m/%Y')}", styles['Normal']))
                    if biology.ph_urinaire:
                        story.append(Paragraph(f"    pH urinaire: {biology.ph_urinaire}", styles['Normal']))
                    if biology.densite_urinaire:
                        story.append(Paragraph(f"    Densité urinaire: {biology.densite_urinaire}", styles['Normal']))
                    if biology.sediment_urinaire:
                        story.append(Paragraph(f"    Sédiment: {biology.sediment_urinaire}", styles['Normal']))
                    if biology.ecbu_resultats:
                        story.append(Paragraph(f"    ECBU: {biology.ecbu_resultats}", styles['Normal']))
                    
                    markers = []
                    if biology.hyperoxalurie:
                        markers.append("Hyperoxalurie")
                    if biology.hypercalciurie:
                        markers.append("Hypercalciurie")
                    if biology.hyperuricurie:
                        markers.append("Hyperuricurie")
                    if biology.cystinurie:
                        markers.append("Cystinurie")
                    if markers:
                        story.append(Paragraph(f"    Marqueurs métaboliques: {', '.join(markers)}", styles['Normal']))
                    
                    if biology.infection_urinaire:
                        story.append(Paragraph(f"    Infection urinaire: Oui{' (' + biology.germe + ')' if biology.germe else ''}", styles['Normal']))
            
            if episode.calculated_stone_type and episode.calculated_stone_type_data:
                import json
                result = json.loads(episode.calculated_stone_type_data)
                
                composition_type = result.get('composition_type', 'Non déterminé')
                composition_detail = result.get('composition_detail', result['top_1'])
                
                result_data = [
                    ['RÉSULTAT D\'ANALYSE (ALGORITHME KALONJI)', ''],
                    ['Nature morpho-constitutionnelle', composition_detail],
                    ['Type de composition', composition_type],
                    ['Score de confiance', f"{result['top_1_score']}/20"],
                    ['LEC éligible', 'Oui' if result.get('lec_eligible') else 'Non'],
                    ['Voie de traitement', result.get('voie_traitement', '-')],
                ]
                
                t = Table(result_data, colWidths=[7*cm, 10*cm])
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
                    top3_data = [['Top 3 types probables', 'Score']]
                    for type_calcul, score in result['top_3']:
                        top3_data.append([type_calcul, f"{score}/20"])
                    
                    t2 = Table(top3_data, colWidths=[12*cm, 5*cm])
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
                    story.append(Paragraph("<b>Conseils de prévention:</b>", styles['Normal']))
                    for conseil in result['prevention'][:5]:
                        story.append(Paragraph(f"  • {conseil}", styles['Normal']))
            
            story.append(Spacer(1, 0.3*cm))
    
    doc.build(story)
    buffer.seek(0)
    
    return send_file(
        buffer,
        mimetype='application/pdf',
        as_attachment=True,
        download_name=f'dossier_{patient.nom}_{patient.prenom}_{datetime.now().strftime("%Y%m%d")}.pdf'
    )
