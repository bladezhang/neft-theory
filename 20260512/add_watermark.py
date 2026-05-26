import fitz
import math
import os

src_path = r"E:\work\projs\neft\paper\20260512\neft_20260514.pdf"
out_path = r"E:\work\projs\neft\paper\20260512\neft_20260514_watermark.pdf"
wm_temp = r"E:\work\projs\neft\paper\20260512\_wm_overlay.pdf"

watermark_text = "blade.zhang.301"
font_size = 75

font = fitz.Font("helv")
text_width = font.text_length(watermark_text, fontsize=font_size)
text_height = font_size

# Create a single watermark overlay page
wm_doc = fitz.open()
wm_page = wm_doc.new_page(width=text_width + 40, height=text_height + 40)
tw = fitz.TextWriter(wm_page.rect)
tw.append((10, text_height + 5), watermark_text, font=font, fontsize=font_size)
tw.write_text(wm_page, color=(0.82, 0.82, 0.82))
wm_doc.save(wm_temp)
wm_doc.close()

# Overlay on each page: single watermark, positioned from bottom-left toward top-right
wm_src = fitz.open(wm_temp)
doc = fitz.open(src_path)

for page_num in range(len(doc)):
    page = doc[page_num]
    rect = page.rect
    w, h = rect.width, rect.height

    # Position: center the watermark, rotated -45 degrees (bottom-left to top-right)
    # Calculate target rect centered on page
    angle_rad = math.radians(-45)
    cos_a = abs(math.cos(angle_rad))
    sin_a = abs(math.sin(angle_rad))

    # The watermark page dimensions
    src_w = text_width + 40
    src_h = text_height + 40

    # Place at page center
    page.show_pdf_page(
        fitz.Rect(0, 0, w, h),
        wm_src,
        0,
        overlay=True,
        rotate=-45,
    )

doc.save(out_path)
doc.close()
wm_src.close()
os.remove(wm_temp)

size_mb = os.path.getsize(out_path) / (1024 * 1024)
pages = fitz.open(out_path).page_count
print(f"Watermark PDF: {out_path} ({size_mb:.1f} MB, {pages} pages)")
