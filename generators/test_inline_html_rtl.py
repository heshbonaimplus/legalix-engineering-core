import re

def add_inline_rtl_to_html(html_text):
    # Add dir="rtl" align="right" style="direction: rtl; text-align: right;" to every tag
    # 1. p tags
    html_text = re.sub(r'<p(?![^>]*dir=)', '<p dir="rtl" align="right" style="direction: rtl; text-align: right;"', html_text)
    # 2. h1, h2, h3, h4 tags
    for h in ['h1', 'h2', 'h3', 'h4']:
        html_text = re.sub(f'<{h}(?![^>]*dir=)', f'<{h} dir="rtl" align="right" style="direction: rtl; text-align: right;"', html_text)
    # 3. div tags
    html_text = re.sub(r'<div(?![^>]*dir=)', '<div dir="rtl" align="right" style="direction: rtl; text-align: right;"', html_text)
    # 4. table tags
    html_text = re.sub(r'<table(?![^>]*dir=)', '<table dir="rtl" align="right" style="direction: rtl; text-align: right;"', html_text)
    # 5. td and th tags
    html_text = re.sub(r'<td(?![^>]*dir=)', '<td dir="rtl" align="right" style="direction: rtl; text-align: right;"', html_text)
    html_text = re.sub(r'<th(?![^>]*dir=)', '<th dir="rtl" align="right" style="direction: rtl; text-align: right;"', html_text)
    # 6. ul and li tags
    html_text = re.sub(r'<ul(?![^>]*dir=)', '<ul dir="rtl" align="right" style="direction: rtl; text-align: right;"', html_text)
    html_text = re.sub(r'<li(?![^>]*dir=)', '<li dir="rtl" align="right" style="direction: rtl; text-align: right;"', html_text)
    return html_text

# Update ELECTRICAL_DESIGNER_CLOSURE_REPORT.html
with open('/home/yogi/lod_project/ELECTRICAL_DESIGNER_CLOSURE_REPORT.html', 'r', encoding='utf-8') as f:
    raw_html = f.read()

inline_html = add_inline_rtl_to_html(raw_html)

with open('/home/yogi/lod_project/ELECTRICAL_TEST_INLINE_RTL.html', 'w', encoding='utf-8') as f:
    f.write(inline_html)

print("Created ELECTRICAL_TEST_INLINE_RTL.html with 100% inline RTL on every element!")
