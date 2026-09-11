import os

# Let's ensure the 4 HTML reports are standalone, responsive and optimized for mobile browser opening!
html_files = [
    '/home/yogi/lod_project/PLUMBING_DESIGNER_CLOSURE_REPORT.html',
    '/home/yogi/lod_project/HVAC_DESIGNER_CLOSURE_REPORT.html',
    '/home/yogi/lod_project/ELECTRICAL_DESIGNER_CLOSURE_REPORT.html',
    '/home/yogi/lod_project/STRUCTURE_DESIGNER_CLOSURE_REPORT.html'
]

for hf in html_files:
    if os.path.exists(hf):
        with open(hf, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Ensure viewport meta tag is present for mobile responsiveness
        if '<meta name="viewport"' not in content:
            content = content.replace('<head>', '<head>\n<meta name="viewport" content="width=device-width, initial-scale=1.0">', 1)
            
        with open(hf, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Mobile viewport added to: {hf}")
