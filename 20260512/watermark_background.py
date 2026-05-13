#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
为PDF文件添加背景水印 - 水印在文字背后，不影响内容阅读
水印：blade.zhang.301，45度倾斜，72点字体
"""

import sys
import os

try:
    from pypdf import PdfReader, PdfWriter, Transformation
    from pypdf import PageObject
    from pypdf.generic import RectangleObject, DictionaryObject
    HAS_PYPDF = True
except ImportError as e:
    print(f"错误: 需要安装 PyPDF2")
    print("请运行: pip install PyPDF2")
    sys.exit(1)

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from io import BytesIO

def create_watermark_background(width, height, text="blade.zhang.301"):
    """
    创建带水印背景的页 - 水印在底层，上面透明区域供内容
    """
    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=(width, height))

    # 整个页填充浅灰色
    c.setFillColorRGB(0.95, 0.95, 0.95, 0.95)

    # 绘制水印文字
    c.setFont("Helvetica-Bold", 72)
    text_width = pdfmetrics.stringWidth(text, "Helvetica-Bold", 72)

    # 45度旋转，居中偏移到右下
    c.saveState()
    c.translate(width * 0.6, height * 0.4)  # 从右下向左上
    c.rotate(45)

    # 水印文字
    c.setFillColorRGB(0.5, 0.5, 0.5, 0.5)  # 较深的灰色
    c.drawString(0, 0, text)

    c.restoreState()
    c.save()
    packet.seek(0)
    return packet

def main():
    # 文件路径
    input_pdf = r"E:\work\projs\neft\paper\20260504\非平衡能量场论：基于熵产、耗散与拓扑的宇宙统一描述-1.pdf"
    output_pdf = r"E:\work\projs\neft\paper\20260504\非平衡能量场论：基于熵产、耗散与拓扑的宇宙统一描述-1_watermarked.pdf"

    watermark_text = "blade.zhang.301"
    rotation = 45
    font_size = 72

    print("=" * 60)
    print("PDF水印添加工具 - 水印在文字背后")
    print("=" * 60)
    print(f"水印文本: {watermark_text}")
    print(f"旋转角度: {rotation}度")
    print(f"字体大小: {font_size}点")
    print(f"输入文件: {input_pdf}")
    print(f"输出文件: {output_pdf}")
    print("=" * 60)

    if not os.path.exists(input_pdf):
        print(f"错误: 输入文件不存在")
        print(f"路径: {input_pdf}")
        return

    try:
        print("\n正在读取PDF...")
        reader = PdfReader(input_pdf)
        page_count = len(reader.pages)
        print(f"总页数: {page_count}")

        print("\n正在处理每一页...")
        writer = PdfWriter()

        for i, page in enumerate(reader.pages):
            # 获取页面尺寸
            width = float(page.mediabox[2] - page.mediabox[0])
            height = float(page.mediabox[3] - page.mediabox[1])

            # 创建水印背景页
            try:
                watermark_page = create_watermark_background(width, height)
                watermark_reader = PdfReader(watermark_page)
                watermark = watermark_reader.pages[0]

                # 关键：将原始页作为子图层添加到水印页
                # 这样原始内容会在水印"上面"
                page.add_watermark_as_child(watermark)

                # 添加到写入器
                writer.add_page(watermark)
            except Exception as e:
                print(f"处理第 {i+1} 页时出错: {e}")
                # 即使出错也要添加原始页
                writer.add_page(page)

            print(f"已处理 {i+1}/{page_count} 页")

        print("\n正在写入输出PDF...")
        with open(output_pdf, "wb") as f:
            writer.write(f)

        file_size = os.path.getsize(output_pdf) / 1024
        print(f"\n完成！")
        print(f"输出文件: {output_pdf}")
        print(f"文件大小: {file_size:.1f} KB ({file_size} 字节)")

    except Exception as e:
        print(f"\n发生错误: {e}")
        import traceback
        traceback.print_exc()
