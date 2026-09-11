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

# Let's inspect the 4 subfolders provided by Eli:
# 1. 1de0ngIawdOD_KPBjJLoqweMNWlW_n-ve
# 2. 14QZ3ZrSY53vkx3G17e4W8HJuHNtSelMM
# 3. 1qgWO44wNX2uj_SSKEllgiYyodM0b6a7l
# 4. 18j2zxDR6iby78biu8U8UMN1P__Ii70bh

folder_ids = [
    '1de0ngIawdOD_KPBjJLoqweMNWlW_n-ve',
    '14QZ3ZrSY53vkx3G17e4W8HJuHNtSelMM',
    '1qgWO44wNX2uj_SSKEllgiYyodM0b6a7l',
    '18j2zxDR6iby78biu8U8UMN1P__Ii70bh'
]

for fid in folder_ids:
    url = f"https://www.googleapis.com/drive/v3/files/{fid}?fields=id,name,mimeType"
    r = requests.get(url, headers=headers)
    print(f"Folder {fid}: {r.status_code} -> {r.json().get('name')}")
    # Make sure permission is public
    requests.post(f'https://www.googleapis.com/drive/v3/files/{fid}/permissions?supportsAllDrives=true',
                  headers={'Authorization': f'Bearer {access_token}', 'Content-Type': 'application/json'},
                  json=payload_perm)
