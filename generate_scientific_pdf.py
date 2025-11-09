"""
Générateur de PDF professionnel pour le document scientifique KALONJI
======================================================================
Crée un PDF structuré et professionnel sans emojis
Utilise ReportLab PLATYPUS pour une mise en page de qualité publication
======================================================================
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    KeepTogether, Frame, PageTemplate
)
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from datetime import datetime
import re

class NumberedCanvas(canvas.Canvas):
    """Canvas personnalisé avec numérotation des pages"""
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count):
        self.setFont("Helvetica", 9)
        self.setFillColor(colors.grey)
        self.drawRightString(
            A4[0] - 2*cm, 1.5*cm,
            f"Page {self._pageNumber} / {page_count}"
        )
        # Ligne de pied de page
        self.setStrokeColor(colors.HexColor('#4F46E5'))
        self.setLineWidth(0.5)
        self.line(2*cm, 2*cm, A4[0] - 2*cm, 2*cm)

def create_styles():
    """Crée les styles personnalisés pour le document"""
    styles = getSampleStyleSheet()
    
    # Style titre principal
    styles.add(ParagraphStyle(
        name='CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#1F2937'),
        spaceAfter=6*mm,
        spaceBefore=0,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold',
        leading=28
    ))
    
    # Style sous-titre
    styles.add(ParagraphStyle(
        name='CustomSubtitle',
        parent=styles['Normal'],
        fontSize=14,
        textColor=colors.HexColor('#4B5563'),
        spaceAfter=12*mm,
        alignment=TA_CENTER,
        fontName='Helvetica',
        leading=18
    ))
    
    # Style section principale (H2)
    styles.add(ParagraphStyle(
        name='SectionHeading',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.HexColor('#4F46E5'),
        spaceAfter=4*mm,
        spaceBefore=8*mm,
        fontName='Helvetica-Bold',
        leading=20,
        borderWidth=0,
        borderPadding=0,
        borderColor=colors.HexColor('#4F46E5'),
        borderRadius=0,
        leftIndent=0
    ))
    
    # Style sous-section (H3)
    styles.add(ParagraphStyle(
        name='SubsectionHeading',
        parent=styles['Heading3'],
        fontSize=13,
        textColor=colors.HexColor('#6366F1'),
        spaceAfter=3*mm,
        spaceBefore=5*mm,
        fontName='Helvetica-Bold',
        leading=16
    ))
    
    # Style sous-sous-section (H4)
    styles.add(ParagraphStyle(
        name='SubsubsectionHeading',
        parent=styles['Heading4'],
        fontSize=11,
        textColor=colors.HexColor('#4338CA'),
        spaceAfter=2*mm,
        spaceBefore=4*mm,
        fontName='Helvetica-Bold',
        leading=14
    ))
    
    # Style corps de texte
    styles.add(ParagraphStyle(
        name='CustomBodyText',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        alignment=TA_JUSTIFY,
        spaceAfter=3*mm,
        fontName='Helvetica',
        textColor=colors.HexColor('#374151')
    ))
    
    # Style liste à puces
    styles.add(ParagraphStyle(
        name='CustomBulletList',
        parent=styles['Normal'],
        fontSize=10,
        leading=13,
        leftIndent=15,
        spaceAfter=2*mm,
        fontName='Helvetica',
        bulletIndent=5,
        textColor=colors.HexColor('#374151')
    ))
    
    # Style références bibliographiques
    styles.add(ParagraphStyle(
        name='CustomReference',
        parent=styles['Normal'],
        fontSize=9,
        leading=12,
        spaceAfter=3*mm,
        fontName='Helvetica',
        leftIndent=0,
        textColor=colors.HexColor('#1F2937')
    ))
    
    # Style code
    styles.add(ParagraphStyle(
        name='CustomCodeBlock',
        parent=styles['Code'],
        fontSize=8,
        leading=10,
        fontName='Courier',
        leftIndent=10,
        rightIndent=10,
        spaceAfter=4*mm,
        spaceBefore=4*mm,
        backColor=colors.HexColor('#F3F4F6'),
        borderWidth=1,
        borderColor=colors.HexColor('#E5E7EB'),
        borderPadding=5
    ))
    
    # Style encadré
    styles.add(ParagraphStyle(
        name='CustomBoxedText',
        parent=styles['Normal'],
        fontSize=9,
        leading=12,
        fontName='Helvetica',
        leftIndent=10,
        rightIndent=10,
        spaceAfter=4*mm,
        spaceBefore=4*mm,
        backColor=colors.HexColor('#EEF2FF'),
        borderWidth=1,
        borderColor=colors.HexColor('#4F46E5'),
        borderPadding=8
    ))
    
    return styles

def remove_emojis(text):
    """Supprime tous les emojis et symboles Unicode du texte"""
    # Pattern étendu pour tous les emojis et symboles
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symboles & pictogrammes
        u"\U0001F680-\U0001F6FF"  # transport & symboles de carte
        u"\U0001F1E0-\U0001F1FF"  # drapeaux (pays)
        u"\U00002702-\U000027B0"  # Dingbats
        u"\U000024C2-\U0001F251"  # caractères encadrés
        u"\U0001F900-\U0001F9FF"  # symboles supplémentaires
        u"\U0001FA00-\U0001FA6F"  # symboles étendus
        u"\U00002600-\U000026FF"  # symboles divers
        u"\U00002B50"              # étoile
        u"\U0001F004"              # mahjong
        u"\U0001F0CF"              # jouer aux cartes
        u"\U0000200D"              # zero width joiner
        u"\U0000FE0F"              # variation selector
        "]+", flags=re.UNICODE)
    
    # Supprimer aussi les symboles communs : ✓✔✅❌⚠️📊💎🔧🎯etc.
    text = emoji_pattern.sub('', text)
    # Supprimer d'autres symboles problématiques
    text = re.sub(r'[\u2700-\u27BF\u2600-\u26FF\u2300-\u23FF]', '', text)
    
    return text

def format_text(text):
    """Formate le texte pour ReportLab (gras, italique, supprime emojis et markdown)"""
    if not text:
        return ''
    
    # Supprimer les emojis D'ABORD (avant échappement XML)
    text = remove_emojis(text)
    
    # D'abord échapper les caractères spéciaux XML
    text = text.replace('&', '&amp;')
    text = text.replace('<', '&lt;')
    text = text.replace('>', '&gt;')
    
    # Convertir markdown en balises XML ReportLab (sur texte échappé)
    # Gras **texte** 
    text = re.sub(r'\*\*(.+?)\*\*', lambda m: f'__BOLD_START__{m.group(1)}__BOLD_END__', text)
    
    # Italique *texte* (ne pas matcher **)
    text = re.sub(r'(?<!\*)\*([^*]+?)\*(?!\*)', lambda m: f'__ITALIC_START__{m.group(1)}__ITALIC_END__', text)
    
    # Code `texte`
    text = re.sub(r'`([^`]+)`', lambda m: f'__CODE_START__{m.group(1)}__CODE_END__', text)
    
    # Restaurer TOUTES les balises en utilisant des marqueurs temporaires
    text = text.replace('__BOLD_START__', '<b>').replace('__BOLD_END__', '</b>')
    text = text.replace('__ITALIC_START__', '<i>').replace('__ITALIC_END__', '</i>')
    text = text.replace('__CODE_START__', '<font name="Courier" size="9">').replace('__CODE_END__', '</font>')
    
    # Nettoyer les espaces multiples
    text = re.sub(r'\s+', ' ', text)
    
    return text.strip()

def parse_markdown_to_pdf_professional(md_file, pdf_file):
    """
    Parse le fichier markdown et génère un PDF professionnel
    """
    # Lire le fichier markdown
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Configuration du document
    doc = SimpleDocTemplate(
        pdf_file,
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2.5*cm,
        bottomMargin=3*cm,
        title="Algorithme KALONJI - Classification Morpho-Constitutionnelle",
        author="Équipe KALONJI",
        subject="Classification des calculs rénaux"
    )
    
    styles = create_styles()
    story = []
    
    # Page de titre
    story.append(Spacer(1, 1*cm))
    story.append(Paragraph(
        "ALGORITHME KALONJI",
        styles['CustomTitle']
    ))
    story.append(Paragraph(
        "Classification Morpho-Constitutionnelle des Calculs Urinaires<br/>Approche Prédictive Multiparamétrique",
        styles['CustomSubtitle']
    ))
    story.append(Spacer(1, 5*mm))
    
    # Informations du document
    info_data = [
        ["Version", "1.0"],
        ["Date", "Novembre 2025"],
        ["Statut", "Document Scientifique"]
    ]
    info_table = Table(info_data, colWidths=[4*cm, 8*cm])
    info_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#EEF2FF')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#1F2937')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#4F46E5')),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(info_table)
    story.append(PageBreak())
    
    # Parser le contenu
    lines = content.split('\n')
    in_code_block = False
    code_buffer = []
    in_table = False
    table_buffer = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Supprimer les emojis de la ligne
        line = remove_emojis(line)
        
        # Blocs de code
        if line.startswith('```'):
            if in_code_block:
                if code_buffer:
                    code_text = '\n'.join(code_buffer)
                    story.append(Paragraph(f'<pre>{code_text}</pre>', styles['CustomCodeBlock']))
                    story.append(Spacer(1, 2*mm))
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
        
        # Tables
        if '|' in line and line.strip().startswith('|'):
            if not in_table:
                in_table = True
                table_buffer = []
            table_buffer.append(line)
            i += 1
            continue
        elif in_table:
            # Fin de table
            if table_buffer:
                table = create_professional_table(table_buffer)
                if table:
                    story.append(table)
                    story.append(Spacer(1, 3*mm))
            table_buffer = []
            in_table = False
        
        # Titres
        if line.startswith('# ') and not line.startswith('##'):
            # Titre principal - ignorer car déjà dans la page de titre
            i += 1
            continue
        elif line.startswith('## ') and not line.startswith('###'):
            text = format_text(line[3:].strip())
            story.append(Paragraph(text, styles['SectionHeading']))
        elif line.startswith('### ') and not line.startswith('####'):
            text = format_text(line[4:].strip())
            story.append(Paragraph(text, styles['SubsectionHeading']))
        elif line.startswith('#### '):
            text = format_text(line[5:].strip())
            story.append(Paragraph(text, styles['SubsubsectionHeading']))
        # Listes à puces
        elif line.strip().startswith('- ') or line.strip().startswith('* '):
            text = format_text(line.strip()[2:])
            story.append(Paragraph(f'• {text}', styles['CustomBulletList']))
        # Listes numérotées (références)
        elif re.match(r'^\d+\.\s+', line.strip()):
            text = format_text(re.sub(r'^\d+\.\s+', '', line.strip()))
            num = re.match(r'^(\d+)\.', line.strip()).group(1)
            story.append(Paragraph(f'<b>[{num}]</b> {text}', styles['CustomReference']))
        # Séparateurs
        elif line.strip() == '---':
            story.append(Spacer(1, 3*mm))
        # Lignes vides
        elif line.strip() == '':
            story.append(Spacer(1, 2*mm))
        # Texte normal
        else:
            if line.strip():
                text = format_text(line.strip())
                story.append(Paragraph(text, styles['CustomBodyText']))
        
        i += 1
    
    # Générer le PDF
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"✓ PDF professionnel généré: {pdf_file}")

def create_professional_table(table_lines):
    """Crée un tableau professionnel à partir de lignes markdown"""
    # Filtrer les lignes de séparation
    data_lines = [line for line in table_lines if not all(c in '|-: ' for c in line)]
    
    if not data_lines:
        return None
    
    # Parser les données
    table_data = []
    for line in data_lines:
        cells = [remove_emojis(cell.strip()) for cell in line.split('|')[1:-1]]
        table_data.append(cells)
    
    if not table_data:
        return None
    
    # Créer le tableau
    table = Table(table_data)
    
    # Style professionnel
    style = TableStyle([
        # En-tête
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4F46E5')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#9CA3AF')),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        # Alternance de couleurs
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F9FAFB')]),
    ])
    
    table.setStyle(style)
    return table

if __name__ == '__main__':
    input_file = 'docs/ALGORITHME_SCIENTIFIQUE_KALONJI.md'
    output_file = 'docs/ALGORITHME_SCIENTIFIQUE_KALONJI.pdf'
    
    print("=" * 80)
    print("GÉNÉRATION DU PDF SCIENTIFIQUE PROFESSIONNEL")
    print("=" * 80)
    print(f"Fichier source: {input_file}")
    print(f"Fichier cible: {output_file}")
    print()
    
    parse_markdown_to_pdf_professional(input_file, output_file)
    
    print()
    print("=" * 80)
    print("✅ PDF PROFESSIONNEL GÉNÉRÉ AVEC SUCCÈS")
    print("=" * 80)
    print(f"Emplacement: {output_file}")
    print()
