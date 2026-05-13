#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF水印选项脚本 - 可调整透明度、字体大小和字体粗细
提供多种水印样式选择
"""

import sys
import os

try:
    from pypdf import PdfReader, PdfWriter
    from pypdf import PageObject
    HAS_PYPDF = True
except ImportError:
    print("Error: Need to install pypdf")
    print("Run: pip install pypdf")
    sys.exit(1)

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from io import BytesIO

# ============== 水印样式配置 ==============

# 预设样式
STYLES = {
    "标准浅灰-半透明": {
        "opacity": 0.15,  # 15%不透明度
        "color": [0.95, 0.95, 0.95],
        "font_size": 60,
        "font_weight": "Bold",
        "description": "标准样式：半透明浅灰，中等字体"
    },
    "浅灰-半透明": {
        "opacity": 0.25,  # 25%不透明度
        "color": [0.9, 0.9, 0.9],
        "font_size": 60,
        "font_weight": "Bold",
        "description": "浅灰：半透明，中等字体"
    },
    "中等灰-半透明": {
        "opacity": 0.35,  # 35%不透明度
        " "color": [0.85, 0.85, 0.85],
        "font_size": 60,
        "font_weight": "Bold",
        "description": "中灰：半透明，中等字体"
    },
    "深灰-半透明": {
        "opacity": 0.15,  # 15%不透明度
        "color": [0.6, 0.6, 0.6],
        "font_size": 60,
        "font_weight": "Bold",
        "description": "深灰：半透明，中等字体"
    },
    "浅灰-30%透明": {
        "opacity": 0.30,  # 30%不透明度
        "color": [0.95, 0.95, 0.95],
        "font_size": 60,
        "font_weight": "Bold",
        "建议": "浅灰：较透明，中等字体"
    },
    "细字体-半透明": {
        "opacity": 0.25,
        "color": [0.9, 0.9, 0.9],
        "font_size": 48,  # 更细字体
        "font_weight": "Bold",
        "description": "细字体：半透明，易读"
    },
    "超细字体-半透明": {
        "opacity": 0.25,
        "color": [0.9, 0.9, 0.9],
        "font_size": 36,  # 超细字体
        "font_weight": "Bold",
        "description": "超细字体：半透明，最易读"
    },
    "细字体-30%透明": {
        "opacity": 0.30,
        "color": [0.9, 0.9, 0.9],
        "font_size": 48,
        "font_weight": "Bold",
        "description": "细字体：30%透明，易读"
    }
}

def create_watermark(width, height, style_name="浅灰-半透明"):
    """
    根据样式配置创建水印页
    """
    s = STYLES[style_name]
    opacity = s["opacity"]
    color = s["color"]

    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=(width, height))

    c.setFont("Helvetica", s["font_size"])

    # 计算文本宽度
    text_width = pdfmetrics.stringWidth("blade.zhang.301", "Helvetica", s["font_size"])

    # 在中央位置绘制水印
    c.saveState()
    c.translate(width/2, height/2)
    c.rotate(45)  # 45度倾斜

    # 设置颜色和透明度
    c.setFillColorRGB(color[0], color[1], color[2])

    # 绘制水印文字
    c.drawString(-text_width/2, 0, "blade.zhang.301")

    c.restoreState()

    c.save()
    packet.seek(0)
    return packet

def add_watermark_to_pdf(input_pdf, output_pdf, style_name="浅灰-半透明"):
    """
    为PDF的每一页添加水印
    """
    print(f"正在处理PDF: {input_pdf}")
    print(f"样式: {STYLES[style_name]['description']}")

    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    for page_num, page in enumerate(reader.pages):
        width = float(page.mediabox[2]) - page.mediabox[0])
        height = float(page.mediabox[3]) - page.mediabox[1])

        # 创建水印页
        watermark_page = create_watermark(width, height, style_name=style_name)
        watermark_reader = PdfReader(watermark_page)
        watermark = watermark_reader.pages[0]

        # 合并原始页和水印页
        page.merge_page(watermark, over=True)

        # 添加到写入器
        writer.add_page(page)

        if (page_num + 1) % 20 == 0:
            print(f"已处理 {page_num + 1}/{len(reader.pages)} 页...")

    # 写入输出PDF
    with open(output_pdf, "wb") as f:
        writer.write(f)

    print(f"\n水印PDF已保存到: {output_pdf}")
    print(f"总页数: {len(reader.pages)}")
    print(f"水印样式: {STYLES[style_name]['description']}")
    print(f"透明度: {STYLES[style_name]['opacity'] * 100}%")
    print(f"字体大小: {STYLES[style_name]['font_size']}点")
    print(f"字体粗细: {STYLES[style_name]['font_weight']}")
    print(f"颜色: {STYLES[style_name]['color']}")

def print_available_styles():
    """打印所有可用样式"""
    print("\n" + "=" * 60)
    print("水印样式选项：")
    print("=" * 60)

    for name, s in STYLES.items():
        print(f"\n{name}:")
        print(f"  - {s['description']}")
        print(f"  - 透明度: {s['opacity'] * 100}%")
        print(f"  - 字体大小: {s['font_size']}点")
        print(f"  - 字体粗细: {s['font_weight']}")
        print(f"  - 颜色: RGB{s['color']}")

    print("\n=" * 60)
    print("使用方法：")
    print("python watermark_options.py \"<style>\" \"<input_pdf>\" \"<output_pdf>\"")
    print("\n可用样式：")
    for i, name in enumerate(STYLES.keys(), 1):
        print(f"{i}. {name}")
    print()
    print("说明：")
    print("- "默认样式是'浅灰-半透明'（15%透明度，60点Bold字体）")
    print("- 推荐使用'细字体-半透明'（48点字体，更易读）")
    print("- 如果水印仍然遮挡文字，请选择'超细字体-半透明'（36点字体）")

def main():
    import argparse

    parser = argparse.ArgumentParser(description="PDF水印工具")
    parser.add_argument("input", help="输入PDF文件路径", required=True)
    parser.add_argument("-o", "--output", help="输出PDF文件路径（默认：input_pdf_watermarked.pdf）", default=None)
    parser.add_argument("-s", "--style", help=f"水印样式（默认：浅灰-半透明）\n可用样式：" + ", ". ".join([f"{i}. {name}" for i in STYLES.keys()]), default="浅灰-半透明")
    parser.add_argument("--list-styles", help="列出所有可用的水印样式", action="store_true", default=False)

    args = parser.parse_args()

    if args.list_styles:
        print_available_styles()
        return

    # 设置路径
    if args.output is None:
        input_path = args.input
        base_name = os.path.splitext(input_path)[0]
        output_path = f"{base_name}_watermarked.pdf"
    else:
        output_path = args.output

    # 检查输入文件是否存在
    if not os.path.exists(args.input):
        print(f"错误：输入文件不存在")
        print(f"路径: {args.input}")
        return

    add_watermark_to_pdf(args.input, output_path, args.style)

if __name__ == "__main__":
    main()
