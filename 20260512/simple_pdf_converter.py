#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple PDF Converter with Watermark
"""

import sys
import os
import re

try:
    from pypdf import PdfReader, PdfWriter
    HAS_PYPDF = True
except ImportError:
    print("Error: Need to install pypdf")
    print("Run: pip install pypdf")
    sys.exit(1)

from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from io import BytesIO

def create_watermark(page_width, page_height, text="blade.zhang.301"):
    """
    Create a watermark page
    """
    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=(page_width, page_height))

    c.setFont("Helvetica", 24)
    text_width = pdfmetrics.stringWidth(text, "Helvetica", 24)

    # Draw watermark in center with 45 degree rotation
    c.saveState()
    c.translate(page_width/2, page_height/2)
    c.rotate(45)
    c.setFillColorRGB(0.9, 0.9, 0.9)  # Light gray (10% opacity)
    c.drawString(-text_width/2, 0, text)
    c.restoreState()

    c.save()
    packet.seek(0)
    return packet

def html_to_platypus(html):
    """Convert HTML to paragraphs"""
    styles = getSampleStyleSheet()
    paragraphs = []

    # Remove HTML tags
    for tag in ['<h1>', '<h2>', '<h3>', '<h4>', '</h1>', '</h2>', '</h3>', '</h4>']:
        html = html.replace(tag, '')

    # Extract text (simple approach)
    text_only = re.sub(r'<[^>]+>', '', html)
    lines = text_only.split('\n')

    current_para = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            if current_para:
                para_text = ' '.join(current_para)
                paragraphs.append(Paragraph(para_text, styles['Normal']))
                current_para = []
        elif stripped.startswith('<img'):
            pass
        elif stripped.startswith('<') and stripped.endswith('>'):
            pass
        else:
            current_para.append(stripped)

    if current_para:
        paragraphs.append(Paragraph(' '.join(current_para), styles['Normal']))

    return paragraphs

def main():
    html_file = r"E:\work\projs\neft\paper\20260504\neft_20260504_cited_figure.html"
    output_pdf = r"E:\work\projs\neft\paper\20260504\neft_20260504_cited_figure_watermarked.pdf"

    print("Step 1: Converting HTML to temporary PDF...")
    print("Note: This is a simplified conversion")
    print("For best results, please use the manual method in the instructions file")

    # Read HTML file
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Create temp PDF
    doc = SimpleDocTemplate("neft_temp.pdf", pagesize=A4)
    paragraphs = html_to_platypus(html_content)

    # Build story with watermark every 3 paragraphs
    story = []
    for i, para in enumerate(paragraphs):
        story.append(para)
        if (i + 1) % 3 == 0 and i > 0:
            # Add watermark
            story.append(PageBreak())

    doc.build(story)

    # Read temp PDF and add proper watermark
    temp_pdf = "neft_temp.pdf"
    if not os.path.exists(temp_pdf):
        print("Error: Temporary PDF not created")
        print("\nPlease use the manual method instead")
        print("\nManual method:")
        print("1. Open in browser: " + html_file)
        print("2. Press Ctrl+P to print")
        print("3. Check 'Background graphics' in print settings")
        print("4. Save as PDF")
        print("5. Save as: " + output_pdf)
        return

    print("\nStep 2: Adding watermark to each page...")
    reader = PdfReader(temp_pdf)
    writer = PdfWriter()

    for page_num, page in enumerate(reader.pages):
        page_width = float(page.mediabox[2] - page.mediabox[0])
        page_height = float(page.mediabox[3] - page.mediabox[1])

        watermark_page = create_watermark(page_width, page_height)
        watermark_reader = PdfReader(watermark_page)
        watermark = watermark_reader.pages[0]

        page.merge_page(watermark, over=True)
        writer.add_page(page)

        print(f"Processed page {page_num + 1}/{len(reader.pages)}")

    with open(output_pdf, "wb") as f:
        writer.write(f)

    # Clean up
    try:
        os.remove(temp_pdf)
    except:
        pass

    print(f"\nWatermarked PDF saved to: {output_pdf}")

if __name__ == "__main__":
    main()
