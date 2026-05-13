#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
为PDF文件添加背景水印 - 水印在文字背后
"""

import sys
import os

try:
    from pypdf import PdfReader, PdfWriter, PageObject, Transformation
    HAS_PYPDF = True
except ImportError:
    print("错误: 需要安装 pypdf")
    print("请运行: pip install pypdf")
    sys.exit(1)

def create_bg_watermark(width, height, text="blade.zhang.301"):
    """
    创建一个背景水印页
    """
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import mm
    from reportlab.pdfbase import pdfmetrics
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.pdfbase.ttfonts import TTFont
    from io import BytesIO

    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=(width, height))

    # 填充整个页面浅灰色背景 (90%不透明度)
    c.setFillColorRGB(0.95, 0.95, 0.95)

    # 绘制水印文字 - 45度倾斜，居中位置
    c.setFont("Helvetica-Bold", 24)
    c.saveState()
    c.translate(width/2, height/2)
    c.rotate(45)
    c.setFillColorRGB(0.1, 0.1, 0.1)  # 较深灰色 (10%透明度)

    # 居中位置
    text_width = pdfmetrics.stringWidth(text, "Helvetica-Bold", 24)
    c.drawString(-text_width/2, 0, text)

    c.restoreState()
    c.save()
    packet.seek(0)
    return packet

def add_bg_watermark(input_pdf, output_pdf):
    """
    为PDF的每一页添加背景水印
    """
    print(f"正在读取PDF: {input_pdf}")
    print(f"输出到: {output_pdf}")

    # 读取输入PDF
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    total = len(reader.pages)
    print(f"总页数: {total}")

    # 为每一页添加背景水印
    for i, page in enumerate(reader.pages):
        # 获取页面尺寸
        width = float(page.mediabox[2] - page.mediabox[0])
        height = float(page.mediabox[3] - page.mediabox[1])

        # 创建背景水印页
        bg_page = create_bg_watermark(width, height)

        # 读取水印页
        bg_reader = PdfReader(bg_page)
        bg = bg_reader.pages[0]

        # 合并原始页和背景水印
        page.merge_page(bg, over=False)  # False = 作为子层（在下面）

        # 添加到写入器
        writer.add_page(page)

        if (i + 1) % 10 == 0:
            print(f"已处理 {i+1}/{total} 页")

    # 写入输出PDF
    with open(output_pdf, "wb") as f:
        writer.write(f)

    print(f"\n完成！水印PDF已保存到: {output_pdf}")

def main():
    # 使用完整路径
    input_pdf = r"E:\work\projs\neft\paper\20260504\非平衡能量场论：基于熵产、耗散与拓扑的宇宙统一描述1.pdf"
    output_pdf = r"E:\work\projs\neft\paper\20260504\非平衡能量场论：基于熵产、耗散与拓扑的宇宙统一描述1_watermarked.pdf"

    add_bg_watermark(input_pdf, output_pdf)

if __name__ == "__main__":
    main()
