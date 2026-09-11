import re, os

def force_ultra_strict_rtl(html_path):
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Replace head style with explicit universal RTL
    universal_css = """
<style>
    * {
        direction: rtl !important;
        text-align: right !important;
        unicode-bidi: embed !important;
        font-family: 'David', 'Arial', sans-serif !important;
    }
    body {
        direction: rtl !important;
        text-align: right !important;
        font-size: 13pt;
        line-height: 1.6;
        color: #222222;
        padding: 30px;
        background-color: #ffffff;
    }
    h1, h2, h3, h4, p, div, span, ul, li, table, tr, td, th {
        direction: rtl !important;
        text-align: right !important;
    }
    table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 15px;
        margin-bottom: 25px;
    }
    th {
        background-color: #102c57 !important;
        color: #ffffff !important;
        font-weight: bold;
        padding: 10px 12px;
        border: 1px solid #102c57;
    }
    td {
        padding: 10px 12px;
        border: 1px solid #cccccc;
        vertical-align: top;
        background-color: #ffffff;
    }
    .card-box {
        border: 1px solid #d0d7de;
        border-radius: 6px;
        margin-bottom: 30px;
        padding: 18px;
        background-color: #ffffff;
    }
</style>
"""
    html = re.sub(r'<style>.*?</style>', universal_css, html, flags=re.DOTALL)

    # 2. Inject dir="rtl" align="right" style="direction: rtl !important; text-align: right !important;" into EVERY tag
    for tag in ['p', 'h1', 'h2', 'h3', 'h4', 'div', 'table', 'td', 'th', 'ul', 'li']:
        # Replace existing tag attributes or add them
        def repl(m):
            tag_name = m.group(1)
            rest = m.group(2)
            # clean old dir/align/style
            rest = re.sub(r'dir="[^"]*"', '', rest)
            rest = re.sub(r'align="[^"]*"', '', rest)
            rest = re.sub(r'style="[^"]*"', '', rest)
            return f'<{tag_name} dir="rtl" align="right" style="direction: rtl !important; text-align: right !important;" {rest}>'
            
        html = re.sub(rf'<({tag})\b([^>]*)>', repl, html)

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Ultra-strict RTL enforced on: {html_path}")

# Apply to Landscape and Marketing HTMLs
force_ultra_strict_rtl('/home/yogi/lod_project/LANDSCAPE_DESIGNER_CLOSURE_REPORT.html')
force_ultra_strict_rtl('/home/yogi/lod_project/MARKETING_DESIGNER_CLOSURE_REPORT.html')
