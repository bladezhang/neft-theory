#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
将neft_20260513.html转换为带水印的PDF
使用Playwright进行HTML转换，使用watermark_v3.py添加水印
"""

import os
import sys
import math
from io import BytesIO

try:
    from pypdf import PdfReader, PdfWriter
    HAS_PYPDF = True
except ImportError:
    print("Error: Need to install pypdf")
    print("Run: pip install pypdf")
    sys.exit(1)

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics

# ==================== 水印函数 ====================

def create_tiled_watermark(width, height, text="bladezhang301", font_size=75):
    """
    创建铺满页面的水印（45度倾斜，从左下到右上）
    """
    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=(width, height))

    # 字体大小
    c.setFont("Helvetica-Bold", font_size)

    # 计算文本宽度和高度
    text_width = pdfmetrics.stringWidth(text, "Helvetica-Bold", font_size)
    text_height = font_size  # 近似高度

    # 45度旋转后文本的投影尺寸
    # 旋转后，对角线方向上的间距需要考虑
    diag_spacing = text_width * 0.8  # 水平间距（对角线方向）
    perp_spacing = text_height * 2.5  # 垂直于对角线方向的间距

    # 计算需要覆盖整个页面所需的行列数
    # 旋转45度后，我们需要在一个更大的虚拟网格上绘制
    cols = int((width + height) / diag_spacing) + 3
    rows = int((width + height) / perp_spacing) + 3

    # 保存状态并旋转
    c.saveState()
    c.translate(width/2, height/2)
    c.rotate(45)
    c.translate(-width/2, -height/2)

    # 设置颜色：浅灰色 (90%透明度)
    c.setFillColorRGB(0.85, 0.85, 0.85)

    # 计算起始偏移（确保从页面外开始，保证覆盖）
    start_x = -text_width
    start_y = -text_width

    # 铺满整个页面（在旋转后的坐标系中）
    for row in range(rows + 5):
        for col in range(cols + 5):
            x = start_x + col * diag_spacing
            y = start_y + row * perp_spacing
            c.drawString(x, y, text)

    c.restoreState()
    c.save()
    packet.seek(0)
    return packet

def add_watermark_to_pdf(input_pdf, output_pdf, watermark_text="bladezhang301", font_size=75):
    """
    为PDF添加铺满页面的水印
    """
    print("开始添加水印...")
    print(f"输入: {input_pdf}")
    print(f"输出: {output_pdf}")
    print(f"水印: {watermark_text}")
    print(f"字体: {font_size}点")
    print(f"透明度: 浅灰 (RGB 0.85, 0.85, 0.85)")
    print(f"旋转角度: 45度 (左下到右上)")
    print(f"布局: 铺满页面")

    if not os.path.exists(input_pdf):
        print(f"错误: 文件不存在: {input_pdf}")
        return False

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
            watermark_page = create_tiled_watermark(width, height, watermark_text, font_size)
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

        file_size = os.path.getsize(output_pdf) / (1024 * 1024)
        print(f"\n水印添加完成！")
        print(f"文件: {output_pdf}")
        print(f"大小: {file_size:.2f} MB")
        print(f"总页数: {page_count}")

        return True

    except Exception as e:
        print(f"错误: {e}")
        import traceback
        traceback.print_exc()
        return False

# ==================== HTML转PDF函数 ====================

def html_to_pdf_with_playwright(html_file, pdf_output):
    """
    使用Playwright将HTML转换为PDF
    """
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Error: Need to install playwright")
        print("Run: pip install playwright && playwright install chromium")
        return False

    print("开始HTML转PDF...")

    # Edge路径 - 尝试多个可能的位置
    edge_paths = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files (x86)\Microsoft\EdgeCore\*\msedge.exe",
    ]

    edge_exe = None
    for path in edge_paths:
        if "*" in path:
            import glob
            matches = glob.glob(path)
            if matches:
                edge_exe = matches[0]
                break
        elif os.path.exists(path):
            edge_exe = path
            break

    # 如果找不到Edge，使用Playwright自带的Chromium
    if edge_exe:
        print(f"使用Edge浏览器: {edge_exe}")
        browser_type_args = {"executable_path": edge_exe}
    else:
        print("使用Playwright自带Chromium浏览器")

    html_url = "file:///" + html_file.replace("\\", "/")

    try:
        with sync_playwright() as p:
            if edge_exe:
                browser = p.chromium.launch(headless=True, executable_path=edge_exe)
            else:
                browser = p.chromium.launch(headless=True)

            page = browser.new_page()

            # 加载页面
            print(f"加载页面: {html_file}")
            page.goto(html_url, wait_until="load", timeout=120000)

            # 等待MathJax等渲染完成
            print("等待页面渲染完成...")
            page.wait_for_timeout(30000)  # 30秒

            # 生成PDF
            print("生成PDF...")
            page.pdf(
                path=pdf_output,
                format="A4",
                print_background=True,
                margin={"top": "15mm", "bottom": "15mm", "left": "20mm", "right": "20mm"},
            )

            browser.close()

        size_mb = os.path.getsize(pdf_output) / (1024 * 1024)
        print(f"PDF生成完成: {pdf_output} ({size_mb:.2f} MB)")
        return True

    except Exception as e:
        print(f"HTML转PDF错误: {e}")
        import traceback
        traceback.print_exc()
        return False

# ==================== 主函数 ====================

def main():
    # 文件路径
    html_file = r"E:\work\projs\neft\paper\20260512\neft_20260513.html"
    temp_pdf = r"E:\work\projs\neft\paper\20260512\neft_20260513_temp.pdf"
    final_pdf = r"E:\work\projs\neft\paper\20260512\neft_20260513_watermarked.pdf"

    # 水印配置
    watermark_text = "bladezhang301"  # 不带点号
    font_size = 75  # 75点字体

    print("=" * 60)
    print("NEFT HTML转带水印PDF工具")
    print("=" * 60)

    # 步骤1: HTML转PDF
    print("\n步骤 1/2: HTML转PDF")
    print("-" * 60)
    success = html_to_pdf_with_playwright(html_file, temp_pdf)

    if not success:
        print("\nHTML转PDF失败，无法继续。")
        return

    # 步骤2: 添加水印
    print("\n步骤 2/2: 添加水印")
    print("-" * 60)
    success = add_watermark_to_pdf(temp_pdf, final_pdf, watermark_text, font_size)

    if success:
        # 删除临时文件
        try:
            os.remove(temp_pdf)
            print(f"\n临时文件已删除: {temp_pdf}")
        except:
            pass

        print("\n" + "=" * 60)
        print("全部完成！")
        print(f"最终PDF: {final_pdf}")
        print("=" * 60)
    else:
        print("\n添加水印失败。")
        print(f"临时PDF保存在: {temp_pdf}")

if __name__ == "__main__":
    main()
