#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Legalix Local Bridge Server - Returns Top Critical Structural Finding Cards by default
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os
import sys

sys.path.append('/opt/legalix')
sys.path.append('/opt/legalix/generators')
sys.path.append('/home/yogi/lod_project')

from legalix_project_matcher import LegalixProjectMatcher
matcher = LegalixProjectMatcher()

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
        resp = {"status": "ONLINE", "server": "Legalix Cloud Master Engine", "ip": "35.242.250.144"}
        self.wfile.write(json.dumps(resp, ensure_ascii=False).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        
        try:
            req_json = json.loads(post_data.decode('utf-8'))
        except Exception:
            req_json = {}

        raw_query = req_json.get('building_id', '') or req_json.get('project_name', '') or 'ניר צבי'
        matched_proj = matcher.match_project(raw_query)
        print(f"\n[LEGALIX DYNAMIC MATCHER] Query: '{raw_query}' ➔ Matched: {matched_proj['canonical_name']}")
        
        # Load all 45 structural cards and send top critical cards with full data
        from gen_full_45_st_cards import get_full_45_structural_cards
        all_cards = get_full_45_structural_cards()
        
        top_cards = []
        for c in all_cards[:6]:
            top_cards.append({
                "id": c['id'],
                "title": c['title'],
                "status": c['status'],
                "prio": c.get('prio', 'P1'),
                "effort": c.get('effort', '15 דקות'),
                "location": c['loc'],
                "element": c['elem'],
                "finding": c['finding'],
                "measured_val": c.get('val_curr') or c.get('val_current', ''),
                "required_threshold": c['req'],
                "delta": c['delta'],
                "impact": c['impact'],
                "standard_source": c['src'],
                "recommended_action": c.get('rec_action') or c.get('action', ''),
                "rev_update_instruction": c.get('rev_update', 'לעדכן במודל רוויט.'),
                "auto_closure_criterion": c.get('closure_crit', 'אימות בבדיקה חוזרת.')
            })

        doc_download_link = matched_proj['word_url']
        pdf_download_link = matched_proj['pdf_url']
        grand_master_doc = matched_proj['grand_master_url']
        all_folder_url = "https://drive.google.com/drive/folders/14QZ3ZrSY53vkx3G17e4W8HJuHNtSelMM?usp=sharing"

        response_payload = {
            "status": "SUCCESS",
            "project_name": matched_proj['canonical_name'],
            "building_id": raw_query,
            "project_status": "LOADED_AND_AUDITED",
            "total_project_findings": 146,
            "structural_summary": {
                "total": 38,
                "red": 36,
                "yellow": 2,
                "hold_point": True,
                "hold_point_focal_points": "קורת טרנספר TG-1 (תת זיון 49.9%), שקיעות דיפרנציאליות W-1 (1/263), חישוקי חדירה Stud Rails"
            },
            "critical_finding_cards": top_cards,
            "downloads": {
                "structural_word_docx": doc_download_link,
                "structural_pdf_report": pdf_download_link,
                "grand_master_integration_docx": grand_master_doc,
                "all_disciplines_drive_folder": all_folder_url
            },
            "summary": f"בקרת תכן שלד למגדל 321 הושלמה (38 ממצאים, 36 אדום). הוכרזה נקודת עצירה (Hold Point). להלן כרטיסי ה-RED הקריטיים המלאים עם כל המדידות והספים:"
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
