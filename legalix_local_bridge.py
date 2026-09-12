#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Legalix Unified Master Bridge Server — Engineering + TaxLand + 13-Agent Litigation War-Room (GCP Cloud)
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os
import sys

sys.path.append('/opt/legalix')
sys.path.append('/opt/legalix/generators')
sys.path.append('/home/yogi/lod_project')

from legalix_omni_discipline_resolver import resolve_discipline_payload
from legalix_taxland_engine import LegalixTaxLandEngine
from legalix_war_room_engine import LegalixLeadCaseOrchestrator

tax_engine = LegalixTaxLandEngine()

class LegalixMasterBridgeHandler(BaseHTTPRequestHandler):
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
        resp = {
            "status": "ONLINE",
            "server": "Legalix Master Cloud Engine (35.242.250.144)",
            "active_modules": [
                "Legalix Engineering (14 Disciplines + FEA)",
                "Legalix TaxLand (Real Estate Tax & 49Z)",
                "Legalix Litigation War-Room (13 Autonomous Sub-Agents)"
            ],
            "active_cases": ["תיק פולינר ואורמקס אגרו (ת״א 62449-03-24)", "פרויקט לוד ניר צבי — עמרם אברהם"]
        }
        self.wfile.write(json.dumps(resp, ensure_ascii=False).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        
        try:
            req_json = json.loads(post_data.decode('utf-8'))
        except Exception:
            req_json = {}

        path = self.path.lower()
        print(f"\n[LEGALIX MASTER API] Inbound Request path: {path} | Data: {req_json}")

        # --- ROUTE 1: LITIGATION WAR-ROOM (13 SUB-AGENTS) ---
        if any(w in path or w in str(req_json) for w in ["war_room", "litigation", "poliner", "פולינר", "אורמקס", "תביעה", "הגנה", "משפט"]):
            case_id = "CASE-POLINER-62449-03-24"
            case_title = "פולינר ואורמקס אגרו בע״מ נ' עיריית חדרה ואח' (ת״א 62449-03-24 מחוזי חיפה, כב' השופט מאזן דאוד)"
            orchestrator = LegalixLeadCaseOrchestrator(case_id, case_title)
            analysis_result = orchestrator.execute_full_war_room_audit({
                "documents": [
                    "כתב תביעה (148 עמודים)",
                    "כתב הגנה (487 עמודים)",
                    "הודעת צד ג (92 עמודים)",
                    "כתב הגנה צד ג 1 (129 עמודים)",
                    "חוות דעת שמאית מומחית ביהמ״ש אילת אלזנר (30 עמודים)"
                ]
            })
            response_payload = {
                "status": "SUCCESS",
                "module": "Legalix Litigation War-Room",
                "case_id": case_id,
                "case_title": case_title,
                "appraisal_summary": {
                    "expert_appraiser": "אילת אלזנר (מומחית בית המשפט)",
                    "property": "גוש 12798 חלקות 67+68 (מתחם אגרובנק חדרה)",
                    "unlawful_seizure_area_sqm": 2667,
                    "seizure_period_years": 4.5,
                    "primary_valuation_nis": 1878000.0,
                    "secondary_reservoir_valuation_nis": 657149.0,
                    "total_claim_with_restoration_and_interest_nis": 3500000.0
                },
                "war_room_intelligence": analysis_result,
                "downloads": {
                    "war_room_docx": "https://drive.google.com/file/d/1adze8TVSSkGVRaTpBN4DBH-wW1iIjTkA/view?usp=sharing",
                    "appraisal_analysis_docx": "https://drive.google.com/file/d/1adze8TVSSkGVRaTpBN4DBH-wW1iIjTkA/view?usp=sharing"
                },
                "summary": "תיק פולינר ואורמקס אגרו נפתח ונותח בהצלחה ע״י 13 סוכני חדר המלחמה של Legalix."
            }

        # --- ROUTE 2: TAXLAND (REAL ESTATE TAX) ---
        elif "tax" in path or req_json.get("module") == "taxland":
            sale_price = float(req_json.get("sale_price", 3500000))
            purchase_price = float(req_json.get("purchase_price", 1000000))
            p_date = req_json.get("purchase_date", "2005-01-01")
            s_date = req_json.get("sale_date", "2026-06-01")
            expenses = float(req_json.get("expenses", 100000))

            res_tax = tax_engine.calculate_betterment_tax_linear(
                purchase_price=purchase_price,
                sale_price=sale_price,
                purchase_date_str=p_date,
                sale_date_str=s_date,
                expenses=expenses
            )
            response_payload = {
                "status": "SUCCESS",
                "module": "Legalix TaxLand",
                "calculation_results": res_tax,
                "summary": "חישוב מס שבח ליניארי מוטב הושלם בהצלחה ע״י Legalix TaxLand."
            }

        # --- ROUTE 3: ENGINEERING (14 DISCIPLINES) ---
        else:
            raw_query = str(req_json.get('building_id', '') or req_json.get('discipline', '') or req_json.get('project_name', '') or '')
            response_payload = resolve_discipline_payload(raw_query)

        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(response_payload, ensure_ascii=False).encode('utf-8'))

def run_server(port=8080):
    server_address = ('0.0.0.0', port)
    httpd = HTTPServer(server_address, LegalixMasterBridgeHandler)
    print(f"Legalix Master Unified Server running on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    p = 8080
    if len(sys.argv) > 1:
        p = int(sys.argv[1])
    run_server(p)
