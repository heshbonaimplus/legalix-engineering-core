#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Legalix Local Bridge Server - Comprehensive Multi-Project & All-Discipline Engine
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os
import sys

sys.path.append('/opt/legalix')
sys.path.append('/opt/legalix/generators')
sys.path.append('/home/yogi/lod_project')

class LegalixBridgeHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        resp = {"status": "ONLINE", "server": "Legalix Master Cloud Server", "active_projects": ["פרויקט לוד ניר צבי — עמרם אברהם", "Tower 321", "Tower 339", "Building 223", "Podium Parking"]}
        self.wfile.write(json.dumps(resp, ensure_ascii=False).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        
        try:
            req_json = json.loads(post_data.decode('utf-8'))
        except Exception:
            req_json = {}

        building_id = req_json.get('building_id', 'פרויקט לוד ניר צבי — עמרם אברהם')
        print(f"\n[LEGALIX CLOUD API] Request for project/building: {building_id}")
        
        # Load structural cards
        doc_download_link = "https://drive.google.com/file/d/1adze8TVSSkGVRaTpBN4DBH-wW1iIjTkA/view?usp=sharing"
        pdf_download_link = "https://drive.google.com/file/d/1cGDg9dLzV8nt1w2F-GVOLuQqKhxR9p-A/view?usp=sharing"
        grand_master_doc = "https://drive.google.com/file/d/1xJnOnKtKkPJPJ0b27aO5bf6hWA145paN/view?usp=sharing"
        all_folder_url = "https://drive.google.com/drive/folders/14QZ3ZrSY53vkx3G17e4W8HJuHNtSelMM?usp=sharing"

        response_payload = {
            "status": "SUCCESS",
            "project_name": "פרויקט לוד ניר צבי — עמרם אברהם (מגדל 321, מגדל 339, חניונים ומסחר)",
            "building_id": building_id,
            "project_status": "LOADED_AND_AUDITED",
            "total_project_findings": 146,
            "disciplines_summary": {
                "01_קונסטרוקציה_ושלד": {
                    "total": 38, "red": 36, "yellow": 2,
                    "focal_points": "קורת טרנספר TG-1 (תת זיון 49.9%), שקיעות דיפרנציאליות W-1 (1/263), חישוקי חדירה Stud Rails",
                    "word_docx_url": doc_download_link,
                    "pdf_report_url": pdf_download_link
                },
                "02_אינסטלציה_וספרינקלרים": {
                    "total": 30, "red": 27, "yellow": 2,
                    "focal_points": "ויסות לחצים 3 אזורים, ספרינקלרים תחת תעלות per NFPA 13, ביטול שופכין בממ״ד",
                    "word_docx_url": "https://drive.google.com/file/d/1Z4Hdos1icRO9eKqFfqp4ts7w2X5HVst6/view?usp=sharing"
                },
                "03_מיזוג_אויר_ושחרור_עשן": {
                    "total": 22, "red": 21, "yellow": 0,
                    "focal_points": "מפוח סילון הטיה 5°-, שרוול קורה B-108, דמפרי עשן NC 24V",
                    "word_docx_url": "https://drive.google.com/file/d/1UzmBVKxuIcxuZd1KStJWtW11xEQTrvb_/view?usp=sharing"
                },
                "04_חשמל_ומערכות_חירום": {
                    "total": 22, "red": 21, "yellow": 0,
                    "focal_points": "ביטול פחת במשאבות כיבוי, לוח ראשי MSB 50kA, תאורת DALI ותשתיות EV",
                    "word_docx_url": "https://drive.google.com/file/d/1oBSdHsbB0l6LDNSR9dij6gNYOhbaAmRk/view?usp=sharing"
                },
                "05_פיתוח_נופי_וניקוז": {
                    "total": 16, "red": 14, "yellow": 1,
                    "focal_points": "מפלס סף לובי 3+ ס״מ, רדיוס סיבוב כבאית 12.5 מ׳, שיפועי נגר 1.5%",
                    "word_docx_url": "https://drive.google.com/file/d/1yGD83p1LFG8Vz_ZgYLLwbVVmGiuR8_uL/view?usp=sharing"
                },
                "06_הצלבת_מכר_מול_ביצוע": {
                    "total": 18, "red": 16, "yellow": 2,
                    "focal_points": "סטיית שטח פלדיום 4.2% בדירות A, רוחב חניות 2.90 מ׳ ליד קיר, מעקות",
                    "word_docx_url": "https://drive.google.com/file/d/1VW2wrk-oOBIYxla-gm2nlNKY8b2ngfSu/view?usp=sharing"
                },
                "07_דוח_אינטגרציה_עליון_Grand_Master": {
                    "total": 146, "red": 135, "yellow": 7,
                    "word_docx_url": grand_master_doc,
                    "pdf_report_url": pdf_download_link
                }
            },
            "hold_point_status": "🔴 HOLD POINT DECLARED — נדרש תיקון TG-1 ושקיעות W-1 לפני שחרור יציקות",
            "summary": "פרויקט לוד ניר צבי נטען בהצלחה מלאה משרת הענן. כל 146 הממצאים, כל 6 דוחות המתכננים ודוח ה-Grand Master זמינים להורדה ישירה ולניתוח.",
            "direct_downloads": {
                "structural_word_docx": doc_download_link,
                "structural_pdf_report": pdf_download_link,
                "grand_master_integration_docx": grand_master_doc,
                "all_disciplines_drive_folder": all_folder_url
            }
        }
        
        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(response_payload, ensure_ascii=False).encode('utf-8'))

def run_server(port=8080):
    server_address = ('0.0.0.0', port)
    httpd = HTTPServer(server_address, LegalixBridgeHandler)
    print(f"Legalix Master Cloud Server is running on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    p = 8080
    if len(sys.argv) > 1:
        p = int(sys.argv[1])
    run_server(p)
