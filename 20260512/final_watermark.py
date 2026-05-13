#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
为PDF文件添加背景水印 - 水印在文字背后，不影响阅读
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
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase.ttfonts import TTFont
from io import BytesIO

def create_bg_watermark(width, height, text="blade.zhang.301"):
    """
    创建带浅灰色背景的水印页 - 水印在中央
    """
    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=(width, height))

    # 整页填充浅灰色（90%白色=10%灰色）
    c.setFillColorRGB(0.96, 0.96, 0.96)

    # 水印文字 - 深灰色
    c.setFont("Helvetica-Bold", 72)
    text_width = pdfmetrics.stringWidth(text, "Helvetica-Bold", 72)

    # 在页面中央，45度倾斜，深灰色
    c.saveState()
    c.translate(width/2, height/2)
    c.rotate(45)
    c.setFillColorRGB(0.05, 0.05, 0.05)  # 深灰色 (5% 灰度)
    c.drawString(-text_width/2, 0, text)

    c.restoreState()
    c.save()
    packet.seek(0)
    return packet

def add_bg_watermark_to_pdf(input_pdf, output_pdf, watermark_text="blade.zhang.301"):
    """
    为PDF的每一页添加背景水印（在内容之后，不影响阅读）
    """
    print(f"正在读取PDF: {input_pdf}")
    print(f"输出到: {output_pdf}")

    try:
        reader = PdfReader(input_pdf)
        writer = PdfWriter()

        total_pages = len(reader.pages)
        print(f"总页数: {total_pages}")

        for page_num, page in enumerate(reader.pages):
            # 获取页面尺寸
            x1, y1 = page.mediabox[0:2], page.mediabox[1:2]  # x1,y1 是左下角
            width = float(page.mediabox[2] - x1)
            height = float(page.mediabox[3] - y1)

            # 创建背景水印页（带灰色背景）
            bg_page = create_bg_watermark(width, height)

            # 读取水印页
            bg_reader = PdfReader(bg_page)
            bg = bg_reader.pages[0]

            # 先合并水印页（让背景先显示）
            temp_writer = PdfWriter()
            temp_writer.add_page(bg)

            # 然后合并原始页和带背景的水印页
            page.merge_page(bg, over=False)  # 原始内容在上层

            # 读取合并后的页
            merged_reader = PdfReader(temp_writer)
            merged_page = merged_reader.pages[0]

            # 添加到最终写入器
            writer.add_page(merged_page)

            print(f"已处理第 {page_num + 1}/{total_pages} 页")

        # 写入输出PDF
        with open(output_pdf, "wb") as output:
            writer.write(output)

        file_size = os.path.getsize(output_pdf) / 1024
        print(f"\n完成！水印PDF已保存到: {output_pdf}")
        print(f"文件大小: {file_size/1024:.1f} KB")
        print(f"总页数: {total_pages}")

    except Exception as e:
        print(f"\n发生错误: {e}")
        import traceback
        traceback.print_exc()

def main():
    # 输入HTML文件
    input_html = r"E:\work\projs\neft\paper\20260504\neft_20260504_cited_figure.html"

    # 尝试转换为PDF
    # 注意：需要wkhtmltopdf或pdfkit
    print("=" * 60)
    print("第一步：将HTML转换为PDF")
    temp_pdf = r"E:\work\projs\neft\paper\20260504\temp_no_watermark.pdf"

    try:
        import pdfkit
        pdfkit.from_file(input_html, temp_pdf, options={
            'encoding': 'UTF-8',
            'enable-local-file-access': None,
            'no-stop-slow-scripts': None
        })
        print(f"转换成功！临时PDF: {temp_pdf}")
        print(f"大小: {os.path.getsize(temp_pdf)/1024:.1f} KB")
    except ImportError:
        print("pdfkit未找到")
        print("\n使用浏览器方法手动转换...")

        print("\n手动转换方法：")
        print("1. 在浏览器中打开HTML文件:")
        print(f"   {input_html}")
        print("2. 按 Ctrl+P 打印")
        print("3. 在打印设置中：")
        print("   - 选择 '打印到PDF' 或 'Microsoft Print to PDF'")
        print("4. 点击 '更多设置'")
        print("   - 确保'背景图形'被勾选")
        print("5. 保存文件为:")
        print(f"   {output_pdf}")
        print("\n保存后手动使用此脚本添加水印：")
        print("python final_watermark.py")
        print(f"  temp_no_watermark.pdf {output_pdf}")

if __name__ == "__main__":
    main()
