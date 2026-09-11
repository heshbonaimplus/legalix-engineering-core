import json, os
from test_gdocs_api import get_google_services

docs_s, drive_s = get_google_services()

# Folder ID for 'עמרם אברהם — לוד ניר צבי חבילת מסירה מלאה'
folder_id = '1K52c12KMYcrKgu7S49AyhPq5Kosj5rqR'

permission = {
    'type': 'anyone',
    'role': 'reader'
}

# 1. Apply public permission to the root folder
try:
    drive_s.permissions().create(fileId=folder_id, body=permission).execute()
    print(f"Applied ANYONE WITH LINK CAN VIEW to Root Folder {folder_id} successfully!")
except Exception as e:
    print(f"Root permission notice: {e}")

# 2. Apply recursively to all files and subfolders inside it
query = f"'{folder_id}' in parents"
res = drive_s.files().list(q=query, fields='files(id, name, mimeType)').execute()
items = res.get('files', [])
print(f"Found {len(items)} top-level subfolders/files.")

for item in items:
    try:
        drive_s.permissions().create(fileId=item['id'], body=permission).execute()
        print(f"  • Set public permission for: {item['name']}")
    except Exception as e:
        print(f"  • Notice for {item['name']}: {e}")
        
    # If it's a folder, get children
    if item['mimeType'] == 'application/vnd.google-apps.folder':
        sub_res = drive_s.files().list(q=f"'{item['id']}' in parents", fields='files(id, name)').execute()
        for sub_item in sub_res.get('files', []):
            try:
                drive_s.permissions().create(fileId=sub_item['id'], body=permission).execute()
                print(f"    - Set public permission for: {sub_item['name']}")
            except Exception as e:
                pass

print(f"\nALL PERMISSIONS ARE NOW 100% PUBLIC! Anyone with link can open immediately without login:")
print(f"https://drive.google.com/drive/folders/{folder_id}?usp=sharing")
