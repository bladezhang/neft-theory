#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF水印工具 - 提供多种水印样式选择
"""

import sys
import os
import argparse

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
from reportlab.pdfbase.ttfonts import TTFont
from io import BytesIO

STYLES = {
    "浅灰-半透明": {
        "opacity": 0.15,  # 15% 不透明度
        "color": [0.85, 0.85, 0.85],
        "font_size": 60,
        "font_weight": "Bold",
        "description": "浅灰背景 + 半透明度"
    },
    "浅灰-30%透明": {
        "opacity": 0.30,  # 30% 不透明度
        "color": [0.7, 0.7, 0.7],
        "font_size": 60,
        "font_weight": "Bold",
        "description": "浅灰背景 + 30% 透明度"
    },
    "中灰-20%透明": {
        "opacity": 0.20,  # 20% 不透明度
        "color": [0.5, 0.5, 0.5],
        "font_size": 60,
        "font_weight": "Bold",
        "description": "中灰背景 + 20% 透明度"
    },
    "深灰-10%透明": {
        "opacity": 0.10, # 10% 不透明度
        "color": [0.15, 0.15, 0.15],
        "font_size": 60,
        "font_weight": "Bold",
        "description": "深灰背景 + 10% 透明度"
    },
    "浅灰-5%透明": {
        "opacity": 0.05,  # 5% 不透明度
        "color": [0.7, 0.7, 0.7],
        "font_size": 60,
        "font_weight": "Bold",
        "description": "浅灰背景 + 5% 透明度"
    },
    "细字体-半透明": {
        "opacity": 0.20,
        "color": [0.85, 0.85, 0.85],
        "font_size": 48,  # 更细字体
        "font_weight": "Bold",
        "description": "浅灰背景 + 细字体 + 20%透明度"
    },
    "细字体-30%透明": {
        "opacity": 0.30,
        "color": [0.7, 0.7, 0.7],
        "font_size": 48,
        "font_weight": "Bold",
        "description": "浅灰背景 + 细字体 + 30%透明度"
    },
    "细字体-半透明": {
        "opacity": 0.20,
        "color": [0.85, 0.85, 0.85],
        "font_size": 48,
        "font_weight": "Bold",
        "description": "浅灰背景 + 细字体 + 20%透明度"
    },
    "超细字体-半透明": {
        "opacity": 0.20,
        "color": [0.85, 0.85, 0.85],
        "font_size": 36,  # 更细字体
        "font_size": 36,
        "font_weight": "Bold",
        "description": "浅灰背景 + 超细字体 + 20%透明度"
    },
    "中灰-半透明": {
        "opacity": 0.20,
        "color": [0.7, 0.7, 0.7],
        "font_size": 60,
        "font_size": 60,
        "font_weight": "Bold",
        "description": "中灰背景 + 50% 透明度"
    },
    "细字体-50%透明": {
        "opacity": 0.50,
        "color": [0.7, 0., 0.7],
        "font_size": 48,
        "font_size": 48,
        "font_weight": "Bold",
        "description": "细字体 + 50% 透明度"
    }
}

def create_watermark(width, height, style_config):
    """
    根据样式配置创建水印页
    """
    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=(width, height))

    # 设置字体
    c.setFont(style_config["font_size"], style_config["font_weight"])
    text_width = pdfmetrics.stringWidth("blade.zhang.301", style_config["font_size"], "Helvetica-Bold", style_config["font_size"])

    # 绘制浅灰色背景
    c.setFillColorRGB(style_config["color"][0], style_config["color"][1], style_config["color"][2])
    c.rect(0, 0, width, height)

    # 绘制水印文字 - 在页面中央，45度倾斜
    c.saveState()
    c.translate(width/2, height/2)
    c.rotate(45)

    # 设置文字颜色和透明度
    c.setFillColorRGB(style_config["color"][0], style_config["color"][1], style_config["color"][2])

    # 绘制文字
    c.drawString(-text_width/2, 0, "blade.zhang.301")

    c.restoreState()

    c.save()
    packet.seek(0)
    return packet

def add_watermark_to_pdf(input_pdf, output_pdf, style_name="浅灰-30%透明"):
    """
    为PDF的每一页添加水印
    """
    s = STYLES[style_name]

    print("=" * 60)
    print("水印工具 - v2.0")
    print("=" * 60)
    print(f"样式: {style_name}")
    print(f"透明度: {s['opacity'] * 100}%")
    print(f"字体: {s['font_size']}点")
    print(f"颜色: RGB({s['color']})")
    print(f"说明: {s['description']}")
    print("=" * 60)

    # 读取输入PDF
    reader = PdfReader(input_pdf)
    page_count = len(reader.pages)

    print(f"读取PDF: {input_pdf}")
    print(f"总页数: {page_count}")

    writer = PdfWriter()

    # 为每一页添加水印
    for page_num, page in enumerate(reader.pages):
        # 获取页面尺寸
        width = float(page.mediabox[2]) - page.mediabox[0])
        height = float(page.mediabox[3]) - page.mediabox[1])

        # 创建水印
        watermark_page = create_watermark(width, height, s)

        # 读取水印页
        watermark_reader = PdfReader(watermark_page)
        watermark = watermark_reader.pages[0]

        # 合并
        page.merge_page(watermark, over=True)

        # 添加到写入器
        writer.add_page(page)

        if (page_num + 1) % 10 == 0:
            print(f"已处理 {page_num + 1}/{page_count} 页...")

    # 写入输出PDF
    with open(output_pdf, "wb") as f:
        writer.write(f)

    print("\n完成！")
    print(f"输出文件: {output_pdf}")
    print(f"总页数: {page_count}")

def list_available_styles():
    """列出所有可用的水印样式"""
    print("\n" + "=" * 60)
    print("可用的水印样式：")
    print("=" * 60)
    i = 1
    for name, s in STYLES.items():
        print(f"{i}. {name}")
        print(f"   透明度: {s['opacity']}")
        print(f"   字体大小: {s['font_size']}点")
        print(f"   颜色: {s['color']}")
        print(f"   说明: {s['description']}")
        i += 1

def main():
    import argparse

    parser = argparse.ArgumentParser(description="PDF水印添加工具")
    parser.add_argument("input", help="输入PDF文件路径", required=True)
    parser.add_argument("-o", "--output", help="输出PDF文件路径（默认：输入文件名_watermarked.pdf）")
    parser.add_argument("-s", "--style", help=f"水印样式（默认：浅灰-30%透明）\n可选：{', '.join(STYLES.keys())}")
    parser.add_argument("--list-styles", "--list", action="store_true", help="列出所有可用的水印样式")

    args = parser.parse_args()

    if args.list_styles:
        list_available_styles()
        return

    # 设置输出路径
    if args.output:
        output_pdf = args.output
    else:
        base, ext = os.path.splitext(args.input)[0], "1"][-1]
        output_pdf = f"{base}_watermarked{ext}"

    print(f"\n输入文件: {args.input}")
    print(f"输出文件: {output_pdf}")
    print(f"水印样式: {args.style}")
    print(f"\n开始处理...")

    # 获取样式配置
    style = STYLES.get(args.style, STYLES["浅灰-30%透明"])

    add_watermark_to_pdf(args.input, output_pdf, args.style)
