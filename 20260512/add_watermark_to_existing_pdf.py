#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
为现有PDF文件添加水印 - 每页45度倾斜、72点字体
"""

import sys
import os

try:
    from pypdf import PdfReader, PdfWriter, Transformation
    from pypdf.generic import SimpleNameObject
    HAS_PYPDF = True
except ImportError:
    print("错误: 需要安装 pypdf")
    print("请运行: pip install pypdf")
    sys.exit(1)

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch, mm
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase.ttfonts import TTFont
from io import BytesIO

def create_watermark_45deg(width, height, text="blade.zhang.301"):
    """
    创建45度倾斜的水印页
    """
    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=(width, height))

    # 注册中文字体
    c.setFont("SimSun", 72)

    # 计算文本宽度
    text_width = pdfmetrics.stringWidth(text, "SimSun", 72)

    # 45度倾斜水印 - 放在页面中央
    c.saveState()
    c.translate(width/2, height/2)
    c.rotate(45)

    # 使用浅灰色 (10% 透明度对应 alpha=0.9)
    c.setFillColorRGB(0.9, 0.9, 0.9)

    # 居中绘制水印文字
    c.drawString(-text_width/2, 0, text)

    c.restoreState()

    c.save()
    packet.seek(0)
    return packet

def add_watermark_to_pdf(input_pdf, output_pdf):
    """
    为PDF的每一页添加45度倾斜水印
    """
    print(f"正在读取PDF: {input_pdf}")
    print(f"输出到: {output_pdf}")

    # 读取输入PDF
    reader = PdfReader(input_pdf)

    # 检查页数
    print(f"总页数: {len(reader.pages)}")

    # 创建写入器
    writer = PdfWriter()

    # 为每一页添加水印
    for page_num, page in enumerate(reader.pages):
        # 获取页面尺寸
        x1, y1, x2, y2 = page.mediabox

        page_width = x2 - x1
        page_height = y2 - y1

        # 创建45度倾斜水印
        watermark_page = create_watermark_45deg(page_width, page_height)

        # 读取水印页
        watermark_reader = PdfReader(watermark_page)
        watermark = watermark_reader.pages[0]

        # 合并原始页和水印页
        page.merge_page(watermark, over=True)

        # 添加到写入器
        writer.add_page(page)

        print(f"已处理第 {page_num + 1}/{len(reader.pages)} 页")

    # 写入输出PDF
    with open(output_pdf, "wb") as output:
        writer.write(output)

    print(f"\n水印PDF已保存到: {output_pdf}")
    print(f"文件大小: {os.path.getsize(output_pdf)} 字节")

def main():
    input_pdf = r"E:\work\projs\neft\paper\20260504\非平衡能量场论：基于熵产、耗散与拓扑的宇宙统一描述-1.pdf"
    output_pdf = r"E:\work\projs\neft\paper\20260504\非平衡能量场论：基于熵产、耗散与拓扑的宇宙统一描述-1_watermarked.pdf"

    if not os.path.exists(input_pdf):
        print(f"错误: 输入文件不存在")
        print(f"请检查文件路径: {input_pdf}")
        return

    add_watermark_to_pdf(input_pdf, output_pdf)

if __name__ == "__main__":
    main()
