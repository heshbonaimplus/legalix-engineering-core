#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Legalix Unified Master Multi-Discipline Server
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

tax_engine = LegalixTaxLandEngine()

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
        resp = {"status": "ONLINE", "server": "Legalix Cloud Master Engine (35.242.250.144)"}
        self.wfile.write(json.dumps(resp, ensure_ascii=False).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        
        try:
            req_json = json.loads(post_data.decode('utf-8'))
        except Exception:
            req_json = {}

        path = self.path.lower()
        print(f"\n[LEGALIX MULTI-DISCIPLINE API] POST request: {path} | Payload: {req_json}")

        # Route 1: TaxLand
        if "tax" in path or req_json.get("module") == "taxland":
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

        # Route 2: Engineering (HVAC, Plumbing, Electrical, Structure, Landscape, Marketing)
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
    httpd = HTTPServer(server_address, LegalixBridgeHandler)
    print(f"Legalix Multi-Discipline Server is running on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    p = 8080
    if len(sys.argv) > 1:
        p = int(sys.argv[1])
    run_server(p)
