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

# Target subfolders
folder_02_id = '14QZ3ZrSY53vkx3G17e4W8HJuHNtSelMM' # 02_דוחות_מתכננים_Google_Docs
folder_01_id = '1de0ngIawdOD_KPBjJLoqweMNWlW_n-ve' # 01_דוח_אינטגרציה_עליון_Grand_Master

# Clean existing items in folder 02 to remove non-opening / docx imports
list_02 = requests.get(f"https://www.googleapis.com/drive/v3/files?q='{folder_02_id}' in parents and trashed=false&fields=files(id, name)", headers=headers).json().get('files', [])
for it in list_02:
    requests.delete(f"https://www.googleapis.com/drive/v3/files/{it['id']}", headers=headers)
    print(f"Cleaned old file in 02: {it['name']}")

list_01 = requests.get(f"https://www.googleapis.com/drive/v3/files?q='{folder_01_id}' in parents and trashed=false&fields=files(id, name)", headers=headers).json().get('files', [])
for it in list_01:
    requests.delete(f"https://www.googleapis.com/drive/v3/files/{it['id']}", headers=headers)
    print(f"Cleaned old file in 01: {it['name']}")

# Reports to upload via the PROVEN HTML -> Google Doc method
reports_to_upload = [
    ("/home/yogi/lod_project/ELECTRICAL_DESIGNER_CLOSURE_REPORT.html", "01_דוח_מתכנן_חשמל_ומתח_נמוך (Google Doc)", folder_02_id),
    ("/home/yogi/lod_project/PLUMBING_DESIGNER_CLOSURE_REPORT.html", "02_דוח_מתכנן_אינסטלציה_וספרינקלרים (Google Doc)", folder_02_id),
    ("/home/yogi/lod_project/HVAC_DESIGNER_CLOSURE_REPORT.html", "03_דוח_מתכנן_מיזוג_אויר_ושחרור_עשן (Google Doc)", folder_02_id),
    ("/home/yogi/lod_project/STRUCTURE_DESIGNER_CLOSURE_REPORT.html", "04_דוח_מתכנן_קונסטרוקציה_ושלד (Google Doc)", folder_02_id),
    ("/home/yogi/lod_project/LANDSCAPE_DESIGNER_CLOSURE_REPORT.html", "05_דוח_מתכנן_פיתוח_נופי_וניקוז (Google Doc)", folder_02_id),
    ("/home/yogi/lod_project/MARKETING_DESIGNER_CLOSURE_REPORT.html", "06_דוח_הצלבת_מכר_מול_ביצוע (Google Doc)", folder_02_id),
    ("/home/yogi/lod_project/GRAND_MASTER_CLOSURE_REPORT.html", "00_דוח_אינטגרציה_וסופרפוזיציה_עליון_Grand_Master (Google Doc)", folder_01_id)
]

# Generate Grand Master HTML
from build_html_gdocs import generate_html_report_for_gdocs
from gen_full_45_st_cards import get_full_45_structural_cards
from build_designer_action_closure_report import plumbing_designer_cards
from build_designer_hvac_action_report import hvac_designer_cards
from build_el_data import get_all_22_electrical_designer_cards
from build_ls_data import get_all_16_landscape_designer_cards
from build_mkt_data import get_all_18_marketing_designer_cards

all_findings = []
all_findings.extend(get_full_45_structural_cards())
all_findings.extend(plumbing_designer_cards)
all_findings.extend(hvac_designer_cards)
all_findings.extend(get_all_22_electrical_designer_cards())
all_findings.extend(get_all_16_landscape_designer_cards())
all_findings.extend(get_all_18_marketing_designer_cards())

html_gm = generate_html_report_for_gdocs(
    "דוח אינטגרציה וסופרפוזיציה הנדסית עליון — Grand Master",
    "בקרת תכן רב-תחומית מאוחדת: שלד, אינסטלציה, כיבוי אש, מיזוג, חשמל, פיתוח ומכר",
    all_findings,
    {"model": "כלל מודלי הפרויקט המשולבים (255 יח״ד)", "p1_count": "90", "p2_count": "28", "p3_count": "24", "p4_count": "4"}
)
with open('/home/yogi/lod_project/GRAND_MASTER_CLOSURE_REPORT.html', 'w', encoding='utf-8') as f:
    f.write(html_gm)

uploaded_gdocs = {}

for html_p, doc_title, p_id in reports_to_upload:
    if os.path.exists(html_p):
        metadata = {
            'name': doc_title,
            'mimeType': 'application/vnd.google-apps.document',
            'parents': [p_id]
        }
        
        with open(html_p, 'rb') as f:
            file_bytes = f.read()
            
        files_upload = {
            'data': ('metadata', json.dumps(metadata), 'application/json; charset=UTF-8'),
            'file': (os.path.basename(html_p), file_bytes, 'text/html; charset=UTF-8')
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
            uploaded_gdocs[doc_title] = glink
            print(f"SUCCESS: {doc_title} -> {glink}")
        else:
            print(f"FAILED: {doc_title} -> {r.status_code} {r.text[:120]}")
        time.sleep(1)

print("\n--- ALL 7 NATIVE GOOGLE DOCS READY (100% RTL RIGHT-ALIGNED) ---")
for k, v in uploaded_gdocs.items():
    print(f"  • {k}: {v}")
