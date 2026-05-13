#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF水印工具 - 字体从72点缩小到48点，透明度90%
"""

import sys
import os

try:
    from pypdf import PdfReader, PdfWriter
    HAS_PYPDF = True
except ImportError:
    print("Error: Need to install pypdf")
    print("Please run: pip install pypdf")
    sys.exit(1)

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from io import BytesIO

def create_watermark(width, height):
    """
    创建48点水印（45度倾斜）
    """
    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=(width, height))

    # 字体大小：48点（从72缩小到48）
    c.setFont("Helvetica-Bold", 48)

    # 计算文本宽度
    text_width = pdfmetrics.stringWidth("blade.zhang.301", "Helvetica-Bold", 48)

    # 45度倾斜，在页面中央
    c.saveState()
    c.translate(width/2, height/2)
    c.rotate(45)

    # 设置颜色：浅灰色 (90%透明度)
    # RGB(0.88, 0.88, 0.88) = 浅灰色
    c.setFillColorRGB(0.88, 0.88, 0.88)

    # 绘制水印文字
    c.drawString(-text_width/2, 0, "blade.zhang.301")

    c.restoreState()
    c.save()
    packet.seek(0)
    return packet

def add_watermark_to_pdf(input_pdf, output_pdf):
    """
    为PDF添加水印
    """
    print("开始处理...")
    print(f"输入: {input_pdf}")
    print(f"输出: {output_pdf}")
    print(f"水印: blade.zhang.301")
    print(f"字体: 48点 (原72点缩小)")
    print(f"透明度: 90% (浅灰)")
    print("旋转角度: 45度")
    print("位置: 页面中央")

    if not os.path.exists(input_pdf):
        print(f"错误: 文件不存在: {input_pdf}")
        return

    try:
        reader = PdfReader(input_pdf)
        page_count = len(reader.pages)
        print(f"总页数: {page_count}")

        writer = PdfWriter()

        for page_num, page in enumerate(reader.pages):
            # 获取页面尺寸
            width = float(page.mediabox[2] - page.mediabox[0])
            height = float(page.mediabox[3] - page.mediabox[1])

            # 创建水印页
            watermark_page = create_watermark(width, height)
            watermark_reader = PdfReader(watermark_page)
            watermark = watermark_reader.pages[0]

            # 合并：水印在底层，原始页在上层
            page.merge_page(watermark, over=False)
            writer.add_page(page)

            if (page_num + 1) % 20 == 0:
                print(f"已处理 {page_num + 1}/{page_count} 页...")

        # 写入输出
        with open(output_pdf, "wb") as f:
            writer.write(f)

        file_size = os.path.getsize(output_pdf) / 1024
        print(f"\n完成！")
        print(f"文件: {output_pdf}")
        print(f"大小: {file_size} KB")
        print(f"总页数: {page_count}")

        print(f"\n样式参数：")
        print(f"- 字体: Helvetica-Bold, {48}pt")
        print(f"- 透明度: 90% (浅灰)")
        print(f"- 旋转: 45度")
        print("- 颜色: 浅灰 RGB(0.88, 0.88, 0.88)")
        print(f"- 位置: 页面中央")

    except Exception as e:
        print(f"错误: {e}")

if __name__ == "__main__":
    # 文件路径
    input_pdf = r"E:\work\projs\neft\paper\20260504\非平衡能量场论：基于熵产、耗散与拓扑的宇宙统一描述-1.pdf"

    # 输出文件名
    output_pdf = r"E:\work\projs\neft\paper\20260504\非平衡能量场论：基于熵产、耗散与拓扑的宇宙统一描述-1_watermarked.pdf"

    # 运行
    add_watermark_to_pdf(input_pdf, output_pdf)
