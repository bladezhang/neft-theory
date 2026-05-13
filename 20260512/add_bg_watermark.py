#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
为PDF文件添加背景水印 - 水印在文字背后
"""

import sys
import os

try:
    from pypdf import PdfReader, PdfWriter, PageObject, Transformation, ContentStream
    HAS_PYPDF = True
except ImportError:
    print("Error: Need to install pypdf")
    print("Run: pip install pypdf")
    sys.exit(1)

def add_background_watermark(input_pdf, output_pdf, watermark_text="blade.zhang.301"):
    """
    为PDF添加背景水印 - 水印在文字后面
    """
    print(f"Adding background watermark to: {input_pdf}")
    print(f"Watermark: {watermark_text}")
    print(f"Output: {output_pdf}")

    # Read input PDF
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    print(f"Total pages: {len(reader.pages)}")

    # Add watermark to each page
    for page_num, page in enumerate(reader.pages):
        # Get page dimensions
        width = float(page.mediabox[2] - page.mediabox[0])
        height = float(page.mediabox[3] - page.mediabox[1])

        # Create a watermark background page
        # We'll draw a light gray background on the entire page

        # Create content stream for background
        content = ContentStream("watermark", {
            "background": """
                << /T1 0 -1 {width} {height} rg 0.95 0.95 0.95 0.95 /F1>>
                """
        })

        # Add watermark text in the center
        # First add the background
        writer.add_page(page)

        # Add the watermark text overlay on top
        watermark = """
        /F1 1 0 {width} {height}
            q
        /T1 0 -1 {width} {height} rg 1 0.1 0.9 /F1>>
        """

        # Add the text using a stream with proper positioning
        watermark_text_stream = ContentStream("watermark", {
            "RG 1 0.1 0.9 /F1>>
        """
        << /Type /Font /Helvetica-Bold 72 /Tf 1 0 0 0 Tr />>>
        /Q 0 -12 0 -12 0 0 12 0 /Fl /X 0 10 0 Y
        /Q 1 -12 -12 0 0 12 0 /F1>>
        {watermark_text}
        """
        """)

        # Merge this on top of the page
        page.merge_page(ContentStream("watermark", {
            "XObject": "Watermark",
            "Y": 10,
            "Width": width,
            "Height": 30,
            "Color": "black"
        })

        print(f"Processed page {page_num + 1}/{len(reader.pages)}")

        # Finally add the original page with background
        writer.add_page(page)

    # Write output
    with open(output_pdf, "wb") as f:
        writer.write(f)

    print(f"\nComplete! Output: {output_pdf}")

def main():
    input_pdf = r"E:\work\projs\neft\paper\20260504\非平衡能量场论：基于熵产、耗散与拓扑的宇宙统一描述1.pdf"
    output_pdf = r"E:\work\projs\neft\paper\20260504\非平衡能量场论：基于熵产、耗散与拓扑的宇宙统一描述1_bg_watermarked.pdf"

    add_background_watermark(input_pdf, output_pdf)

if __name__ == "__main__":
    main()
