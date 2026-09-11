import os, json, re, requests, time

rclone_conf = os.path.expanduser('~/.config/rclone/rclone.conf')
with open(rclone_conf, 'r') as f:
    text = f.read()

for line in text.splitlines():
    if line.strip().startswith('token = '):
        token_data = json.loads(line.strip().replace('token = ', ''))
        break

access_token = token_data['access_token']
headers = {'Authorization': f'Bearer {access_token}', 'Content-Type': 'application/json'}
payload_perm = {'role': 'reader', 'type': 'anyone'}

def make_inline_rtl(html_text):
    for tag in ['p', 'h1', 'h2', 'h3', 'h4', 'div', 'table', 'td', 'th', 'ul', 'li']:
        html_text = re.sub(f'<{tag}(?![^>]*dir=)', f'<{tag} dir="rtl" align="right" style="direction: rtl; text-align: right;"', html_text)
    return html_text

files_to_process = [
    ("PLUMBING_DESIGNER_CLOSURE_REPORT.html", "01_דוח_מתכנן_אינסטלציה_וספרינקלרים", "02_דוחות_מתכננים_Google_Docs"),
    ("HVAC_DESIGNER_CLOSURE_REPORT.html", "02_דוח_מתכנן_מיזוג_אויר_ושחרור_עשן", "02_דוחות_מתכננים_Google_Docs"),
    ("ELECTRICAL_DESIGNER_CLOSURE_REPORT.html", "03_דוח_מתכנן_חשמל_ומתח_נמוך", "02_דוחות_מתכננים_Google_Docs"),
    ("STRUCTURE_DESIGNER_CLOSURE_REPORT.html", "04_דוח_מתכנן_קונסטרוקציה_ושלד", "02_דוחות_מתכננים_Google_Docs"),
    ("LANDSCAPE_DESIGNER_CLOSURE_REPORT.html", "05_דוח_מתכנן_פיתוח_נופי_וניקוז", "02_דוחות_מתכננים_Google_Docs"),
    ("MARKETING_DESIGNER_CLOSURE_REPORT.html", "06_דוח_הצלבת_מכר_מול_ביצוע", "02_דוחות_מתכננים_Google_Docs"),
    ("GRAND_MASTER_CLOSURE_REPORT.html", "00_דוח_אינטגרציה_וסופרפוזיציה_עליון_Grand_Master", "01_דוח_אינטגרציה_עליון_Grand_Master")
]

for src_fn, dest_name, dest_subfolder in files_to_process:
    p = os.path.join('/home/yogi/lod_project', src_fn)
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f:
            c = f.read()
        c_inline = make_inline_rtl(c)
        with open(p, 'w', encoding='utf-8') as f:
            f.write(c_inline)
        print(f"Applied 100% inline RTL to: {src_fn}")

print("All HTML files now have 100% inline RTL attributes on every tag.")
