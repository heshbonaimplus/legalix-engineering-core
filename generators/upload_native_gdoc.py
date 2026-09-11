import os, json
from test_gdocs_api import get_google_services
from googleapiclient.http import MediaFileUpload

docs_s, drive_s = get_google_services()

# 1. Target HTML file to upload and convert to Google Doc
html_path = '/home/yogi/lod_project/ELECTRICAL_DESIGNER_CLOSURE_REPORT.html'

file_metadata = {
    'name': 'דוח הנחיות וסגירת ממצאים למתכנן החשמל — Legalix Designer Closure Report',
    'mimeType': 'application/vnd.google-apps.document'
}

media = MediaFileUpload(html_path, mimetype='text/html', resumable=True)

# Create the file in Google Drive (Google converts HTML with dir="rtl" to a native RTL Google Doc!)
file = drive_s.files().create(body=file_metadata, media_body=media, fields='id, webViewLink').execute()
file_id = file.get('id')
web_link = file.get('webViewLink')

print(f"File created on Google Drive with ID: {file_id}")
print(f"Direct Web Link: {web_link}")

# 2. Make it publicly accessible for viewing (anyone with the link can view)
permission = {
    'type': 'anyone',
    'role': 'reader'
}
drive_s.permissions().create(fileId=file_id, body=permission).execute()
print("Public sharing permission set to ANYONE WITH LINK CAN VIEW!")

# 3. Move it to the project folder
# Let's find the folder ID for '03_בקרת_תכן_QA_השוואת_תקנים'
res = drive_s.files().list(q="name='03_בקרת_תכן_QA_השוואת_תקנים' and mimeType='application/vnd.google-apps.folder'", fields='files(id, name)').execute()
folders = res.get('files', [])
if folders:
    folder_id = folders[0]['id']
    # Move file to folder
    drive_s.files().update(fileId=file_id, addParents=folder_id, fields='id, parents').execute()
    print(f"Moved file to folder '03_בקרת_תכן_QA_השוואת_תקנים' (ID: {folder_id})")

print(f"\nSUCCESS! Direct Open URL: https://docs.google.com/document/d/{file_id}/edit?usp=sharing")
