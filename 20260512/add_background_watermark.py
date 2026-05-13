#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
为PDF文件添加背景水印 - 水印在文字背后
"""

import sys
import os

try:
    from pypdf import PdfReader, PdfWriter
    HAS_PYPDF = True
except ImportError:
    print("Error: Need to install pypdf")
    sys.exit(1)

def add_watermark_background(input_pdf, output_pdf, watermark_text="blade.zhang.301"):
    """
    为PDF的每一页添加背景水印
    """
    print(f"Processing: {input_pdf}")

    try:
        reader = PdfReader(input_pdf)
        writer = PdfWriter()

        total = len(reader.pages)
        print(f"Total pages: {total}")

        for page_num, page in enumerate(reader.pages):
            # Get page dimensions
            x0 = float(page.mediabox[0])
            y0 = float(page.mediabox[1])
            width = float(page.mediabox[2] - page.mediabox[0])
            height = float(page.mediabox[3] - page.mediabox[1])

            # Calculate center position for watermark (right-bottom corner)
            # Move watermark slightly from center to right-bottom corner
            cx = x0 + width * 0.7  # 70% from left edge
            cy = y0 + height * 0.1  # 10% from bottom edge

            # Page number watermark
            watermark = f"{page_num + 1}"

            # Add page with watermark
            writer.add_page()

            # Create watermark at position
            watermark = writer.add_watermark(
                text=watermark_text,
                x=cx,
                y=cy,
                width=200,
                height=60,
                fontname="Helvetica",
                fontsize=24,
                color=rgba(0, 0, 0, 0.2),  # Dark gray
                opacity=0.08,  # 8% transparency
                angle=45,  # Rotate 45 degrees
                valign="middle"
            )

            # Merge original page on top
            page.add_page(page)

            print(f"Processed {page_num + 1}/{total}")

        # Write output
        with open(output_pdf, "wb") as f:
            writer.write(f)

        file_size = os.path.getsize(output_pdf) / 1024
        print(f"Complete! Output: {output_pdf}")
        print(f"File size: {file_size} bytes ({file_size/1024:.2f} KB)")

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    input_pdf = r"E:\work\projs\neft\paper\20260504\非平衡能量场论：基于熵产、耗散与拓扑的宇宙统一描述-1.pdf"
    output_pdf = r"E:\work\projs\neft\paper\20260504\非平衡能量场论：基于熵产、耗散与拓扑的宇宙统一描述-1_watermarked.pdf"

    add_watermark_background(input_pdf, output_pdf)
