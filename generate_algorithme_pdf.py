"""
Script de génération PDF du document scientifique ALGORITHME_SCIENTIFIQUE_KALONJI.md
Utilise ReportLab pour créer un PDF professionnel et bien formaté
"""
import re
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
from datetime import datetime

def parse_markdown_to_pdf(md_file_path, pdf_file_path):
    """
    Convertit le fichier markdown en PDF professionnel
    """
    # Lire le fichier markdown
    with open(md_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Configuration du document PDF
    doc = SimpleDocTemplate(
        pdf_file_path,
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )
    
    # Styles
    styles = getSampleStyleSheet()
    
    # Styles personnalisés
    title_style = ParagraphStyle(
        'ScientificTitle',
        parent=styles['Heading1'],
        fontSize=20,
        textColor=colors.HexColor('#1F2937'),
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    h2_style = ParagraphStyle(
        'ScientificH2',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.HexColor('#4F46E5'),
        spaceAfter=10,
        spaceBefore=16,
        fontName='Helvetica-Bold'
    )
    
    h3_style = ParagraphStyle(
        'ScientificH3',
        parent=styles['Heading3'],
        fontSize=14,
        textColor=colors.HexColor('#6366F1'),
        spaceAfter=8,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    
    h4_style = ParagraphStyle(
        'ScientificH4',
        parent=styles['Heading4'],
        fontSize=12,
        textColor=colors.HexColor('#4338CA'),
        spaceAfter=6,
        spaceBefore=10,
        fontName='Helvetica-Bold'
    )
    
    body_style = ParagraphStyle(
        'ScientificBody',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        alignment=TA_JUSTIFY,
        spaceAfter=6,
        fontName='Helvetica'
    )
    
    code_style = ParagraphStyle(
        'CodeBlock',
        parent=styles['Code'],
        fontSize=8,
        leading=10,
        fontName='Courier',
        leftIndent=10,
        rightIndent=10,
        spaceAfter=8,
        spaceBefore=8,
        backColor=colors.HexColor('#F3F4F6')
    )
    
    bullet_style = ParagraphStyle(
        'BulletStyle',
        parent=styles['Normal'],
        fontSize=10,
        leading=13,
        leftIndent=20,
        spaceAfter=4,
        fontName='Helvetica'
    )
    
    reference_style = ParagraphStyle(
        'ReferenceStyle',
        parent=styles['Normal'],
        fontSize=9,
        leading=12,
        spaceAfter=6,
        fontName='Helvetica',
        leftIndent=10
    )
    
    # Construire le story
    story = []
    
    # Diviser le contenu en lignes
    lines = content.split('\n')
    
    in_code_block = False
    code_buffer = []
    in_table = False
    table_buffer = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Code blocks
        if line.startswith('```'):
            if in_code_block:
                # Fin du bloc de code
                if code_buffer:
                    code_text = '\n'.join(code_buffer)
                    story.append(Paragraph(f'<pre>{code_text}</pre>', code_style))
                    story.append(Spacer(1, 0.3*cm))
                code_buffer = []
                in_code_block = False
            else:
                in_code_block = True
            i += 1
            continue
        
        if in_code_block:
            code_buffer.append(line)
            i += 1
            continue
        
        # Tables (simple detection)
        if '|' in line and line.strip().startswith('|'):
            if not in_table:
                in_table = True
                table_buffer = []
            table_buffer.append(line)
            i += 1
            continue
        elif in_table:
            # Fin de la table
            if table_buffer:
                story.extend(create_table_from_md(table_buffer))
                story.append(Spacer(1, 0.4*cm))
            table_buffer = []
            in_table = False
        
        # Titres
        if line.startswith('# ') and not line.startswith('##'):
            text = line[2:].strip()
            story.append(Paragraph(text, title_style))
            story.append(Spacer(1, 0.5*cm))
        elif line.startswith('## '):
            text = line[3:].strip()
            story.append(Paragraph(text, h2_style))
        elif line.startswith('### '):
            text = line[4:].strip()
            story.append(Paragraph(text, h3_style))
        elif line.startswith('#### '):
            text = line[5:].strip()
            story.append(Paragraph(text, h4_style))
        # Listes
        elif line.strip().startswith('- ') or line.strip().startswith('* '):
            text = line.strip()[2:]
            text = format_markdown_text(text)
            story.append(Paragraph(f'• {text}', bullet_style))
        elif re.match(r'^\d+\.\s+', line.strip()):
            text = re.sub(r'^\d+\.\s+', '', line.strip())
            text = format_markdown_text(text)
            num = re.match(r'^(\d+)\.', line.strip()).group(1)
            story.append(Paragraph(f'{num}. {text}', reference_style))
        # Séparateurs
        elif line.strip() == '---':
            story.append(Spacer(1, 0.5*cm))
        # Lignes vides
        elif line.strip() == '':
            story.append(Spacer(1, 0.2*cm))
        # Texte normal
        else:
            if line.strip():
                text = format_markdown_text(line.strip())
                story.append(Paragraph(text, body_style))
        
        i += 1
    
    # Générer le PDF
    doc.build(story)
    print(f"✅ PDF généré avec succès: {pdf_file_path}")

def format_markdown_text(text):
    """
    Formate le texte markdown pour ReportLab
    """
    # Gras **texte**
    text = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', text)
    # Italique *texte*
    text = re.sub(r'\*([^*]+)\*', r'<i>\1</i>', text)
    # Échapper les caractères spéciaux XML
    text = text.replace('&', '&amp;')
    text = text.replace('<b>', '<b>').replace('</b>', '</b>')
    text = text.replace('<i>', '<i>').replace('</i>', '</i>')
    
    return text

def create_table_from_md(table_lines):
    """
    Crée un tableau ReportLab à partir de lignes markdown
    """
    elements = []
    
    # Filtrer les lignes de séparation
    data_lines = [line for line in table_lines if not all(c in '|-: ' for c in line)]
    
    if not data_lines:
        return elements
    
    # Parser les données
    table_data = []
    for line in data_lines:
        cells = [cell.strip() for cell in line.split('|')[1:-1]]
        table_data.append(cells)
    
    if not table_data:
        return elements
    
    # Créer le tableau
    table = Table(table_data)
    
    # Style du tableau
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4F46E5')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ])
    
    table.setStyle(style)
    elements.append(table)
    
    return elements

if __name__ == '__main__':
    input_file = 'docs/ALGORITHME_SCIENTIFIQUE_KALONJI.md'
    output_file = 'docs/ALGORITHME_SCIENTIFIQUE_KALONJI.pdf'
    
    print("🔄 Génération du PDF du document scientifique KALONJI...")
    print(f"📄 Fichier source: {input_file}")
    print(f"📊 Fichier cible: {output_file}")
    print()
    
    parse_markdown_to_pdf(input_file, output_file)
    
    print()
    print("✨ Document PDF scientifique généré avec succès!")
    print(f"📍 Emplacement: {output_file}")
