import json, os, requests
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# Extract credentials from rclone.conf
def get_google_services():
    rclone_conf_path = os.path.expanduser('~/.config/rclone/rclone.conf')
    with open(rclone_conf_path, 'r') as f:
        lines = f.readlines()
        
    token_json_str = ""
    for line in lines:
        if line.strip().startswith('token = '):
            token_json_str = line.strip().replace('token = ', '')
            break
            
    token_data = json.loads(token_json_str)
    
    creds = Credentials(
        token=token_data['access_token'],
        refresh_token=token_data.get('refresh_token'),
        token_uri="https://oauth2.googleapis.com/token",
        client_id=None, # uses standard google flow
        client_secret=None
    )
    
    # Refresh token if needed
    if creds.expired or not creds.valid:
        from google.auth.transport.requests import Request
        creds.refresh(Request())
        
    docs_service = build('docs', 'v1', credentials=creds)
    drive_service = build('drive', 'v3', credentials=creds)
    return docs_service, drive_service

docs_s, drive_s = get_google_services()
print("Connected to Google Docs and Google Drive API successfully!")
