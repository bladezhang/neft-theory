import os
from playwright.sync_api import sync_playwright

html_path = r"E:\work\projs\neft\paper\20260512\neft_20260514.html"
pdf_path = r"E:\work\projs\neft\paper\20260512\neft_20260514.pdf"

html_url = "file:///" + html_path.replace("\\", "/")

edge_path = r"C:\Program Files (x86)\Microsoft\EdgeCore\148.0.3967.54\msedge.exe"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, executable_path=edge_path)
    page = browser.new_page()
    page.goto(html_url, wait_until="load", timeout=120000)
    page.wait_for_timeout(30000)  # wait for MathJax rendering
    page.pdf(
        path=pdf_path,
        format="A4",
        print_background=True,
        margin={"top": "15mm", "bottom": "15mm", "left": "20mm", "right": "20mm"},
    )
    browser.close()

size_mb = os.path.getsize(pdf_path) / (1024 * 1024)
print(f"PDF generated: {pdf_path} ({size_mb:.1f} MB)")
