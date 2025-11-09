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
        ['Email', patient.email or '-']
    ]
    
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
    
    if patient.episodes:
        story.append(Paragraph("Épisodes récents", styles['Heading2']))
        story.append(Spacer(1, 0.3*cm))
        
        for episode in sorted(patient.episodes, key=lambda x: x.date_episode, reverse=True)[:3]:
            story.append(Paragraph(f"<b>Épisode du {episode.date_episode.strftime('%d/%m/%Y')}</b>", styles['Normal']))
            story.append(Paragraph(f"Motif: {episode.motif or '-'}", styles['Normal']))
            story.append(Paragraph(f"Diagnostic: {episode.diagnostic or '-'}", styles['Normal']))
            
            if episode.imageries:
                latest_imaging = max(episode.imageries, key=lambda x: x.date_examen)
                story.append(Paragraph(f"<b>Imagerie:</b> Densité {latest_imaging.densite_uh or latest_imaging.densite_noyau or '-'} UH, Taille {latest_imaging.taille_mm or latest_imaging.diametre_longitudinal or '-'} mm", styles['Normal']))
                if latest_imaging.nombre_calculs:
                    story.append(Paragraph(f"Nombre de calculs: {latest_imaging.nombre_calculs}", styles['Normal']))
                if latest_imaging.topographie_calcul:
                    story.append(Paragraph(f"Topographie: {latest_imaging.topographie_calcul}", styles['Normal']))
                if latest_imaging.forme_calcul:
                    story.append(Paragraph(f"Forme: {latest_imaging.forme_calcul}", styles['Normal']))
            
            if episode.biologies:
                latest_biology = max(episode.biologies, key=lambda x: x.date_examen)
                story.append(Paragraph(f"<b>Biologie:</b> pH {latest_biology.ph_urinaire or '-'}", styles['Normal']))
                if latest_biology.sediment_urinaire:
                    story.append(Paragraph(f"Sédiment: {latest_biology.sediment_urinaire}", styles['Normal']))
            
            if episode.calculated_stone_type and episode.calculated_stone_type_data:
                import json
                result = json.loads(episode.calculated_stone_type_data)
                
                story.append(Paragraph(f"<b>Type de calcul:</b> {result['top_1']} (score: {result['top_1_score']}/20)", styles['Normal']))
                story.append(Paragraph(f"<b>Calculé le:</b> {episode.calculated_at.strftime('%d/%m/%Y %H:%M') if episode.calculated_at else '-'}", styles['Normal']))
                story.append(Paragraph(f"<b>LEC éligible:</b> {'Oui' if result.get('lec_eligible') else 'Non'}", styles['Normal']))
                story.append(Paragraph(f"<b>Voie de traitement:</b> {result.get('voie_traitement', '-')}", styles['Normal']))
                
                if result.get('prevention'):
                    story.append(Paragraph("<b>Prévention:</b>", styles['Normal']))
                    for conseil in result['prevention'][:3]:
                        story.append(Paragraph(f"• {conseil}", styles['Normal']))
                
                story.append(Paragraph(f"<b>Top 3:</b>", styles['Normal']))
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
