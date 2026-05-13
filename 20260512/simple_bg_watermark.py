#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
为PDF文件添加背景水印 - 水印在文字背后，不影响阅读
"""

import os
import sys

try:
    from pypdf import PdfReader, PdfWriter
    HAS_PYPDF = True
except ImportError:
    print("错误: 需要安装 pypdf")
    print("请运行: pip install pypdf")
    sys.exit(1)

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from io import BytesIO

def create_bg_watermark(width, height, text="blade.zhang.301"):
    """
    创建背景水印 - 整个页面背景为浅灰色
    """
    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=(width, height))

    # 整个页面填充浅灰色背景（浅灰色10%透明度）
    c.setFillColorRGB(0.97, 0.97, 0.97)

    # 居中绘制水印文字 - 深灰色（5%透明度）
    c.saveState()
    c.translate(width/2, height/2)
    c.rotate(45)
    c.setFont("Helvetica", 72)
    text_width = pdfmetrics.stringWidth(text, "Helvetica", 72)
    c.setFillColorRGB(0.05, 0.05, 0.05)  # 5%透明度，深灰色
    c.drawString(-text_width/2, 0, text)

    c.restoreState()

    c.save()
    packet.seek(0)
    return packet

def add_bg_watermark_to_pdf(input_pdf, output_pdf):
    """
    为PDF的每一页添加背景水印 - 水印在文字背后
    """
    print(f"正在读取PDF: {input_pdf}")
    print(f"输出到: {output_pdf}")

    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    page_count = len(reader.pages)
    print(f"总页数: {page_count}")

    for page_num, page in enumerate(reader.pages):
        # 获取页面尺寸
        width = float(page.mediabox[2] - page.mediabox[0])
        height = float(page.mediabox[3] - page.mediabox[1])

        # 创建背景水印页
        bg_page = create_bg_watermark(width, height)

        # 读取水印页
        bg_reader = PdfReader(bg_page)
        bg = bg_reader.pages[0]

        # 合并：背景水印在底层（over=False）,原始页在上层
        page.merge_page(bg, over=False)
        writer.add_page(page)

        print(f"已处理第 {page_num + 1}/{page_count} 页")

    with open(output_pdf, "wb") as f:
        writer.write(f)

    print(f"\n水印PDF已保存到: {output_pdf}")
    print(f"总页数: {page_count}")
    print(f"\n说明: 水印在文字后面，浅灰色背景（10%透明度）")
    print(f"   水印内容: {text}")
    print(f"   旋转角度: 45度")
    print(f"   字体大小: 72点")

def main():
    # 输入PDF文件路径（根据实际情况调整）
    input_pdf = r"E:\work\projs\neft\paper\20260504\非平衡能量场论：基于熵产、耗散与拓扑的宇宙统一描述-20260501_cited_figure.html"

    # 输出文件名
    output_pdf = r"E:\work\projs\neft\paper\20260504\非平衡能量场论：基于熵产、耗散与拓扑的宇宙统一描述-20260501_cited_figure_watermarked.pdf"

    # 检查文件是否存在
    if not os.path.exists(input_pdf):
        print(f"错误: 输入文件不存在")
        print(f"路径: {input_pdf}")
        return

    print("\n开始处理...")

    try:
        add_bg_watermark_to_pdf(input_pdf, output_pdf)
    except Exception as e:
        print(f"\n发生错误: {e}")

if __name__ == "__main__":
    main()
