import os, json, time
from test_gdocs_api import get_google_services
from googleapiclient.http import MediaFileUpload

docs_s, drive_s = get_google_services()

# 1. Create a dedicated Master Folder for Or Amram
folder_metadata = {
    'name': 'פרויקט לוד ניר צבי — עמרם אברהם | חבילת בקרת תכן ואינטגרציה מלאה (Rev 01)',
    'mimeType': 'application/vnd.google-apps.folder'
}

folder = drive_s.files().create(body=folder_metadata, fields='id, webViewLink').execute()
master_folder_id = folder.get('id')
print(f"Master Delivery Folder Created with ID: {master_folder_id}")

# Make Master Folder Public (Anyone with link can view)
permission = {'type': 'anyone', 'role': 'reader'}
drive_s.permissions().create(fileId=master_folder_id, body=permission).execute()
print("Master Folder Permission set to: ANYONE WITH LINK CAN VIEW")

# 2. Create sub-folders
sub_folders = [
    "01_דוח_אינטגרציה_וסופרפוזיציה_עליון_Grand_Master",
    "02_דוחות_מתכננים_וסגירת_ממצאים_Google_Docs",
    "03_קבצי_BCF_לטעינה_ברוויט_Revit_BIM",
    "04_דוחות_PDF_רשמיים_לחתימה",
    "05_ספריות_חוקי_תכן_ומפרטי_נתונים_Rules_Engine"
]

sub_folder_ids = {}
for sf_name in sub_folders:
    sf_meta = {
        'name': sf_name,
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': [master_folder_id]
    }
    sf = drive_s.files().create(body=sf_meta, fields='id').execute()
    sub_folder_ids[sf_name] = sf.get('id')
    print(f"Created sub-folder: {sf_name}")

# 3. Upload & Convert all HTML reports to Native Google Docs into Sub-folder 02
reports_map = [
    ("GRAND_MASTER_CLOSURE_REPORT.html", "🏆 דוח אינטגרציה וסופרפוזיציה עליון — Grand Master", sub_folder_ids["01_דוח_אינטגרציה_וסופרפוזיציה_עליון_Grand_Master"]),
    ("ELECTRICAL_DESIGNER_CLOSURE_REPORT.html", "⚡ דוח הנחיות וסגירת ממצאים — חשמל ומתח נמוך", sub_folder_ids["02_דוחות_מתכננים_וסגירת_ממצאים_Google_Docs"]),
    ("PLUMBING_DESIGNER_CLOSURE_REPORT.html", "🚰 דוח הנחיות וסגירת ממצאים — אינסטלציה וכיבוי אש", sub_folder_ids["02_דוחות_מתכננים_וסגירת_ממצאים_Google_Docs"]),
    ("HVAC_DESIGNER_CLOSURE_REPORT.html", "❄️ דוח הנחיות וסגירת ממצאים — מיזוג אוויר ושחרור עשן", sub_folder_ids["02_דוחות_מתכננים_וסגירת_ממצאים_Google_Docs"]),
    ("STRUCTURE_DESIGNER_CLOSURE_REPORT.html", "🏗️ דוח הנחיות וסגירת ממצאים — קונסטרוקציה ושלד", sub_folder_ids["02_דוחות_מתכננים_וסגירת_ממצאים_Google_Docs"]),
    ("LANDSCAPE_DESIGNER_CLOSURE_REPORT.html", "🌳 דוח הנחיות וסגירת ממצאים — פיתוח נופי וניקוז חצר", sub_folder_ids["02_דוחות_מתכננים_וסגירת_ממצאים_Google_Docs"]),
    ("MARKETING_DESIGNER_CLOSURE_REPORT.html", "📐 דוח הנחיות וסגירת ממצאים — הצלבת מכר מול ביצוע", sub_folder_ids["02_דוחות_מתכננים_וסגירת_ממצאים_Google_Docs"])
]

# Generate missing HTMLs for Grand Master, Landscape and Marketing
from build_html_gdocs import generate_html_report_for_gdocs
from build_ls_data import get_all_16_landscape_designer_cards
from build_mkt_data import get_all_18_marketing_designer_cards

# Landscape HTML
html_ls = generate_html_report_for_gdocs(
    "דוח הנחיות תיקון, חלופות וסגירת ממצאים למתכנן הנוף והפיתוח",
    "פיתוח נופי, ניקוז חצר, מפלסי פיתוח וקירות תמך חוץ",
    get_all_16_landscape_designer_cards(),
    {"model": "LOD_ALL_LG_R24.rvt", "p1_count": "10", "p2_count": "4", "p3_count": "1", "p4_count": "1"}
)
with open('/home/yogi/lod_project/LANDSCAPE_DESIGNER_CLOSURE_REPORT.html', 'w', encoding='utf-8') as f:
    f.write(html_ls)

# Marketing HTML
html_mkt = generate_html_report_for_gdocs(
    "דוח הנחיות תיקון, חלופות וסגירת ממצאים לשיווק ולמתכנן",
    "הצלבת תוכניות מכר מול מודלי ביצוע והתאמת שטחים",
    get_all_18_marketing_designer_cards(),
    {"model": "חבילת מכר מול 3D-Marketing / Lod_AR / Lod_ST (1.82GB)", "p1_count": "15", "p2_count": "3", "p3_count": "0", "p4_count": "0"}
)
with open('/home/yogi/lod_project/MARKETING_DESIGNER_CLOSURE_REPORT.html', 'w', encoding='utf-8') as f:
    f.write(html_mkt)

gdoc_links = {}

for fn, doc_name, parent_id in reports_map:
    html_p = os.path.join('/home/yogi/lod_project', fn)
    if os.path.exists(html_p):
        file_metadata = {
            'name': doc_name,
            'mimeType': 'application/vnd.google-apps.document',
            'parents': [parent_id]
        }
        media = MediaFileUpload(html_p, mimetype='text/html', resumable=True)
        file = drive_s.files().create(body=file_metadata, media_body=media, fields='id').execute()
        file_id = file.get('id')
        
        # Set public permission
        drive_s.permissions().create(fileId=file_id, body=permission).execute()
        link_url = f"https://docs.google.com/document/d/{file_id}/edit?usp=sharing"
        gdoc_links[doc_name] = link_url
        print(f"Uploaded Google Doc: {doc_name} -> {link_url}")
        time.sleep(1)

# 4. Upload BCF files to Sub-folder 03
bcf_files = [
    '/home/yogi/lod_project/LOD_Structure_Audit_Issues.bcfzip',
    '/home/yogi/lod_project/LOD_Plumbing_Audit_Issues.bcfzip',
    '/home/yogi/lod_project/LOD_HVAC_Audit_Issues.bcfzip'
]

for bp in bcf_files:
    if os.path.exists(bp):
        b_meta = {
            'name': os.path.basename(bp),
            'parents': [sub_folder_ids["03_קבצי_BCF_לטעינה_ברוויט_Revit_BIM"]]
        }
        media = MediaFileUpload(bp, resumable=True)
        drive_s.files().create(body=b_meta, media_body=media).execute()
        print(f"Uploaded BCF: {os.path.basename(bp)}")

# 5. Upload PDFs to Sub-folder 04
pdf_files = [f for f in os.listdir('/home/yogi/lod_project') if f.endswith('.pdf')]
for pf in pdf_files:
    p_path = os.path.join('/home/yogi/lod_project', pf)
    p_meta = {
        'name': pf,
        'parents': [sub_folder_ids["04_דוחות_PDF_רשמיים_לחתימה"]]
    }
    media = MediaFileUpload(p_path, mimetype='application/pdf', resumable=True)
    drive_s.files().create(body=p_meta, media_body=media).execute()
    print(f"Uploaded PDF: {pf}")

print(f"\nALL ASSETS UPLOADED! Master Folder Link: https://drive.google.com/drive/folders/{master_folder_id}?usp=sharing")

with open('/home/yogi/lod_project/master_delivery_links.json', 'w', encoding='utf-8') as f:
    json.dump({"master_folder": f"https://drive.google.com/drive/folders/{master_folder_id}?usp=sharing", "docs": gdoc_links}, f, ensure_ascii=False, indent=2)
