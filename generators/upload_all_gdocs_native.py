import os, json
from test_gdocs_api import get_google_services
from googleapiclient.http import MediaFileUpload

docs_s, drive_s = get_google_services()

# Find folder ID for '03_בקרת_תכן_QA_השוואת_תקנים'
res = drive_s.files().list(q="name='03_בקרת_תכן_QA_השוואת_תקנים' and mimeType='application/vnd.google-apps.folder'", fields='files(id, name)').execute()
folders = res.get('files', [])
folder_id = folders[0]['id'] if folders else None

reports_to_upload = [
    ("ELECTRICAL_DESIGNER_CLOSURE_REPORT.html", "דוח הנחיות וסגירת ממצאים למתכנן החשמל — Legalix Designer Closure Report"),
    ("PLUMBING_DESIGNER_CLOSURE_REPORT.html", "דוח הנחיות וסגירת ממצאים למתכנן האינסטלציה והכיבוי — Legalix Designer Closure Report"),
    ("HVAC_DESIGNER_CLOSURE_REPORT.html", "דוח הנחיות וסגירת ממצאים למתכנן המיזוג ושחרור עשן — Legalix Designer Closure Report"),
    ("STRUCTURE_DESIGNER_CLOSURE_REPORT.html", "דוח הנחיות וסגירת ממצאים למתכנן הקונסטרוקציה — Legalix Designer Closure Report")
]

created_links = {}

for fn, doc_name in reports_to_upload:
    html_p = os.path.join('/home/yogi/lod_project', fn)
    if os.path.exists(html_p):
        file_metadata = {
            'name': doc_name,
            'mimeType': 'application/vnd.google-apps.document'
        }
        if folder_id:
            file_metadata['parents'] = [folder_id]
            
        media = MediaFileUpload(html_p, mimetype='text/html', resumable=True)
        file = drive_s.files().create(body=file_metadata, media_body=media, fields='id, webViewLink').execute()
        file_id = file.get('id')
        
        # Set public permission
        drive_s.permissions().create(fileId=file_id, body={'type': 'anyone', 'role': 'reader'}).execute()
        
        open_link = f"https://docs.google.com/document/d/{file_id}/edit?usp=sharing"
        created_links[fn] = open_link
        print(f"Created Google Doc for {fn} -> {open_link}")

with open('/home/yogi/lod_project/gdocs_links.json', 'w', encoding='utf-8') as f:
    json.dump(created_links, f, ensure_ascii=False, indent=2)
print("All Google Docs links saved successfully!")
