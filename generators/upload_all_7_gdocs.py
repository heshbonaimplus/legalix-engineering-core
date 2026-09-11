import json, os, requests, time

rclone_conf = os.path.expanduser('~/.config/rclone/rclone.conf')
with open(rclone_conf, 'r') as f:
    text = f.read()

for line in text.splitlines():
    if line.strip().startswith('token = '):
        token_data = json.loads(line.strip().replace('token = ', ''))
        break

access_token = token_data['access_token']
headers = {'Authorization': f'Bearer {access_token}'}
payload_perm = {'role': 'reader', 'type': 'anyone'}

folder_id = '1K52c12KMYcrKgu7S49AyhPq5Kosj5rqR'

# List of all 7 reports to convert and upload as Native Google Docs directly into the main folder
gdocs_specs = [
    ("GRAND_MASTER_MULTIDISCIPLINARY_INTEGRATION_REPORT_LOD_NIR_ZVI.docx", "00_דוח_אינטגרציה_וסופרפוזיציה_עליון_Grand_Master (Google Doc)", "docx"),
    ("PLUMBING_DESIGNER_CLOSURE_REPORT.html", "01_דוח_הנחיות_וסגירה_אינסטלציה_וכיבוי_אש (Google Doc)", "html"),
    ("HVAC_DESIGNER_CLOSURE_REPORT.html", "02_דוח_הנחיות_וסגירה_מיזוג_אויר_ושחרור_עשן (Google Doc)", "html"),
    ("ELECTRICAL_DESIGNER_CLOSURE_REPORT.html", "03_דוח_הנחיות_וסגירה_חשמל_ומתח_נמוך (Google Doc)", "html"),
    ("STRUCTURE_DESIGNER_CLOSURE_REPORT.html", "04_דוח_הנחיות_וסגירה_קונסטרוקציה_ושלד (Google Doc)", "html"),
    ("LANDSCAPE_DESIGNER_CLOSURE_REPORT.html", "05_דוח_הנחיות_וסגירה_פיתוח_נופי_וניקוז (Google Doc)", "html"),
    ("MARKETING_DESIGNER_CLOSURE_REPORT.html", "06_דוח_הנחיות_וסגירה_הצלבת_מכר_מול_ביצוע (Google Doc)", "html")
]

direct_links = {}

for fn, doc_title, ftype in gdocs_specs:
    fpath = os.path.join('/home/yogi/lod_project', fn)
    if os.path.exists(fpath):
        mime = 'text/html' if ftype == 'html' else 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        
        # Simple upload with multipart via requests
        metadata = {
            'name': doc_title,
            'mimeType': 'application/vnd.google-apps.document',
            'parents': [folder_id]
        }
        
        with open(fpath, 'rb') as f:
            file_bytes = f.read()
            
        files_upload = {
            'data': ('metadata', json.dumps(metadata), 'application/json; charset=UTF-8'),
            'file': (fn, file_bytes, mime)
        }
        
        r = requests.post(
            'https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart&fields=id,webViewLink',
            headers={'Authorization': f'Bearer {access_token}'},
            files=files_upload
        )
        
        if r.status_code in [200, 201]:
            fid = r.json().get('id')
            # Set public permission
            requests.post(
                f'https://www.googleapis.com/drive/v3/files/{fid}/permissions?supportsAllDrives=true',
                headers={'Authorization': f'Bearer {access_token}', 'Content-Type': 'application/json'},
                json=payload_perm
            )
            glink = f"https://docs.google.com/document/d/{fid}/edit?usp=sharing"
            direct_links[doc_title] = glink
            print(f"Uploaded Google Doc: {doc_title} -> {glink}")
        else:
            print(f"Upload failed for {doc_title}: {r.status_code} {r.text[:100]}")
            
# Also copy all PDFs and DOCX directly via rclone
print("\nDirect Google Docs links ready:")
for k, v in direct_links.items():
    print(f"  • {k}: {v}")

with open('/home/yogi/lod_project/final_gdocs_links.json', 'w', encoding='utf-8') as f:
    json.dump(direct_links, f, ensure_ascii=False, indent=2)
