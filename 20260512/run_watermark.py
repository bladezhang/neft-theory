#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF水印工具 - 线条细、半透明、45度倾斜
简单、可靠，不依赖复杂PDF转换
"""

import sys
import os

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

def create_watermark_fine(width, height):
    """
    创建45度倾斜的细线水印
    """
    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=(width, height))

    # 设置更细的字体 - 48点（原72点）
    c.setFont("Helvetica-Bold", 48)
    text_width = pdfmetrics.stringWidth("blade.zhang.301", "Helvetica-Bold", 48)

    # 45度倾斜水印 - 在页面中央
    c.saveState()
    c.translate(width/2, height/2)
    c.rotate(45)

    # 颜色：浅灰色 (15%不透明度) - 更易读
    c.setFillColorRGB(0.88, 0.88, 0.88)  # 增加到90%不透明度

    # 居中绘制水印文字
    c.drawString(-text_width/2, 0, "blade.zhang.301")

    c.restoreState()

    c.save()
    packet.seek(0)
    return packet

def add_watermark_to_pdf(input_pdf, output_pdf):
    """
    为PDF的每一页添加背景水印
    """
    print(f"正在处理: {input_pdf}")
    print(f"输出到: {output_pdf}")
    print(f"水印: blade.zhang.301")
    print(f"字体: 48点 (原72点)")
    print(f"透明度: 90% (原10%)")

    reader = PdfReader(input_pdf)
    page_count = len(reader.pages)
    print(f"总页数: {page_count}")

    writer = PdfWriter()

    # 为每一页添加水印
    for page_num, page in enumerate(reader.pages):
        # 获取页面尺寸
        width = float(page.mediabox[2] - page.mediabox[0])
        height = float(page.mediabox[3] - page.mediabox[1])

        # 创建水印页
        watermark_page = create_watermark_fine(width, height)

        # 读取水印页
        watermark_reader = PdfReader(watermark_page)
        watermark = watermark_reader.pages[0]

        # 合并：原始页 + 水印在底层（文本在前）
        # over=False 表示水印在下面（在原始内容上面）
        page.merge_page(watermark, over=False)

        # 添加到写入器
        writer.add_page(page)

        if (page_num + 1) % 20 == 0:
            print(f"已处理 {page_num + 1}/{page_count} 页")

    # 写入输出PDF
    with open(output_pdf, "wb") as f:
        writer.write(f)

    file_size = os.path.getsize(output_pdf) / 1024
    print(f"\n完成！水印PDF已保存到: {output_pdf}")
    print(f"文件大小: {file_size:.1f} KB")
    print(f"总页数: {page_count}")
    print(f"\n说明:")
    print("- 水印在文字后面（底层）")
    print("- 透明度: 90% (比之前的10%更浅，易读)")
    print("- 字体: 48点 (原72点，更细)")

def main():
    input_pdf = r"E:\work\projs\neft\paper\20260504\非平衡能量场论：基于熵产、耗散与拓扑的宇宙统一描述-20260501.html"
    output_pdf = r"E:\work\projs\neft\paper\20260504\非平衡能量场论：基于熵产、耗散与拓扑的宇宙统一描述-20260501_fine_watermarked.pdf"

    if not os.path.exists(input_pdf):
        print(f"错误: 输入文件不存在")
        print(f"路径: {input_pdf}")
        print("\n手动方法（最可靠）:")
        print("1. 在浏览器中打开HTML文件")
        print("2. 按Ctrl+P打印")
        print("3. 勾选 '背景图形'")
        print("4. 保存为PDF")
        return

    add_watermark_to_pdf(input_pdf, output_pdf)

if __name__ == "__main__":
    main()
