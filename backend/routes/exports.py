from flask import Blueprint, request, jsonify, send_file
from flask_login import login_required
from backend.models import Patient
from backend.inference import InferenceEngine
from backend.routes.search import search_patients
from datetime import datetime
import csv
import io
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors

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
    doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=2*cm, leftMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm)
    
    story = []
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle('CustomTitle', parent=styles['Heading1'], fontSize=16, textColor=colors.HexColor('#1e40af'))
    
    story.append(Paragraph(f"Dossier Patient - {patient.nom} {patient.prenom}", title_style))
    story.append(Spacer(1, 0.5*cm))
    
    patient_data = [
        ['Nom', f"{patient.nom} {patient.prenom}"],
        ['Date de naissance', patient.date_naissance.strftime('%d/%m/%Y')],
        ['Sexe', patient.sexe],
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
    
    t = Table(patient_data, colWidths=[5*cm, 10*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.grey),
        ('TEXTCOLOR', (0, 0), (0, -1), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey)
    ]))
    story.append(t)
    story.append(Spacer(1, 0.5*cm))
    
    if any([patient.antecedents_personnels, patient.antecedents_familiaux, patient.antecedents_chirurgicaux, patient.allergies, patient.traitements_chroniques]):
        story.append(Paragraph("Antécédents médicaux", styles['Heading2']))
        story.append(Spacer(1, 0.2*cm))
        if patient.antecedents_personnels:
            story.append(Paragraph(f"<b>Antécédents personnels:</b> {patient.antecedents_personnels}", styles['Normal']))
        if patient.antecedents_familiaux:
            story.append(Paragraph(f"<b>Antécédents familiaux:</b> {patient.antecedents_familiaux}", styles['Normal']))
        if patient.antecedents_chirurgicaux:
            story.append(Paragraph(f"<b>Antécédents chirurgicaux:</b> {patient.antecedents_chirurgicaux}", styles['Normal']))
        if patient.allergies:
            story.append(Paragraph(f"<b>Allergies:</b> {patient.allergies}", styles['Normal']))
        if patient.traitements_chroniques:
            story.append(Paragraph(f"<b>Traitements chroniques:</b> {patient.traitements_chroniques}", styles['Normal']))
        story.append(Spacer(1, 0.5*cm))
    
    if any([patient.hydratation_jour, patient.regime_alimentaire, patient.petit_dejeuner, patient.dejeuner, patient.diner]):
        story.append(Paragraph("Habitudes de vie & Alimentation", styles['Heading2']))
        story.append(Spacer(1, 0.2*cm))
        if patient.hydratation_jour:
            story.append(Paragraph(f"<b>Hydratation:</b> {patient.hydratation_jour} L/jour", styles['Normal']))
        if patient.regime_alimentaire:
            story.append(Paragraph(f"<b>Régime alimentaire:</b> {patient.regime_alimentaire}", styles['Normal']))
        if patient.petit_dejeuner:
            story.append(Paragraph(f"<b>Petit déjeuner:</b> {patient.petit_dejeuner}", styles['Normal']))
        if patient.dejeuner:
            story.append(Paragraph(f"<b>Déjeuner:</b> {patient.dejeuner}", styles['Normal']))
        if patient.diner:
            story.append(Paragraph(f"<b>Dîner:</b> {patient.diner}", styles['Normal']))
        if patient.grignotage:
            story.append(Paragraph(f"<b>Grignotage:</b> {patient.grignotage}", styles['Normal']))
        if patient.autres_consommations:
            story.append(Paragraph(f"<b>Autres consommations:</b> {patient.autres_consommations}", styles['Normal']))
        story.append(Spacer(1, 0.5*cm))
    
    if patient.episodes:
        story.append(Paragraph("Épisodes récents", styles['Heading2']))
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
                
                story.append(Paragraph(f"<b>Nature morpho-constitutionnelle:</b> {composition_detail}", styles['Normal']))
                story.append(Paragraph(f"<b>Type:</b> {composition_type}", styles['Normal']))
                story.append(Paragraph(f"<b>Score:</b> {result['top_1_score']}/20", styles['Normal']))
                story.append(Paragraph(f"<b>Calculé le:</b> {episode.calculated_at.strftime('%d/%m/%Y %H:%M') if episode.calculated_at else '-'}", styles['Normal']))
                story.append(Paragraph(f"<b>LEC éligible:</b> {'Oui' if result.get('lec_eligible') else 'Non'}", styles['Normal']))
                story.append(Paragraph(f"<b>Voie de traitement:</b> {result.get('voie_traitement', '-')}", styles['Normal']))
                
                if result.get('prevention'):
                    story.append(Paragraph("<b>Prévention:</b>", styles['Normal']))
                    for conseil in result['prevention'][:3]:
                        story.append(Paragraph(f"• {conseil}", styles['Normal']))
                
                story.append(Paragraph(f"<b>Top 3 types probables:</b>", styles['Normal']))
                for type_calcul, score in result['top_3']:
                    story.append(Paragraph(f"  {type_calcul}: {score}/20", styles['Normal']))
            
            story.append(Spacer(1, 0.3*cm))
    
    doc.build(story)
    buffer.seek(0)
    
    return send_file(
        buffer,
        mimetype='application/pdf',
        as_attachment=True,
        download_name=f'dossier_{patient.nom}_{patient.prenom}_{datetime.now().strftime("%Y%m%d")}.pdf'
    )
