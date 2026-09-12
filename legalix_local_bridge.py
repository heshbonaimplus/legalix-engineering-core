#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Legalix Dynamic Remote MCP Server — Zero Mock, Real Disk & Skills Gateway
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os
import sys

sys.path.append('/opt/legalix')
sys.path.append('/home/yogi/lod_project')

from legalix_real_dynamic_gateway import get_case_data
from legalix_taxland_engine import LegalixTaxLandEngine
from legalix_omni_discipline_resolver import resolve_discipline_payload

tax_engine = LegalixTaxLandEngine()

MCP_TOOLS_MANIFEST = [
    {
        "name": "legalix_mega_case",
        "description": "חדר המלחמה המשפטי של Legalix Mega-Case: ניתוח עומק של תיקי ענק, סתירות כירורגיות וציר זמן דינמי מתוך 13 המחסנים המאונדקסים.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "case_id": {"type": "string", "description": "מזהה התיק"},
                "query": {"type": "string", "description": "שאלת החקירה או הנושא המבוקש"}
            },
            "required": ["case_id"]
        }
    },
    {
        "name": "legalix_taxland_autonomous_agent",
        "description": "סוכן OpenClaw האוטונומי של TaxLand: תכנון מס מקרקעין רב-מסלולי (ליניארי מוטב 48א, פיצול 49ז, פריסת מס 48א(ה), בקרת Red Team ושליפת נמדר).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "sale_price": {"type": "number", "description": "שווי מכירה"},
                "purchase_price": {"type": "number", "description": "שווי רכישה"},
                "purchase_date": {"type": "string", "description": "יום רכישה (YYYY-MM-DD)"}
            },
            "required": ["sale_price", "purchase_price"]
        }
    },
    {
        "name": "audit_structural_model",
        "description": "בקרת תכן הנדסית רב-תחומית (שלד, אינסטלציה, מיזוג, חשמל, פיתוח ומכר) מבית Legalix Engineering.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "building_id": {"type": "string", "description": "שם הפרויקט או הדיסציפלינה"}
            },
            "required": ["building_id"]
        }
    }
]

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
            "server": "Legalix Master Dynamic Gateway (Zero-Mock Engine)",
            "tools": [t["name"] for t in MCP_TOOLS_MANIFEST]
        }
        self.wfile.write(json.dumps(resp, ensure_ascii=False).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        
        try:
            req_json = json.loads(post_data.decode('utf-8'))
        except Exception:
            req_json = {}

        if "jsonrpc" in req_json:
            method = req_json.get("method")
            req_id = req_json.get("id")
            
            if method == "initialize":
                reply = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "protocolVersion": "2024-11-05",
                        "capabilities": {"tools": {}},
                        "serverInfo": {"name": "legalix-mega-case-dynamic", "version": "2.0.0"}
                    }
                }
            elif method == "tools/list":
                reply = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {"tools": MCP_TOOLS_MANIFEST}
                }
            elif method == "tools/call":
                params = req_json.get("params", {})
                tool_name = params.get("name")
                args = params.get("arguments", {})
                
                if tool_name == "legalix_mega_case":
                    case_id = args.get("case_id", "")
                    query = args.get("query", "")
                    res = get_case_data(case_id, query)
                    content_text = json.dumps(res, ensure_ascii=False, indent=2)
                elif tool_name == "legalix_taxland_autonomous_agent":
                    res = tax_engine.calculate_betterment_tax_linear(
                        purchase_price=float(args.get("purchase_price", 1000000)),
                        sale_price=float(args.get("sale_price", 3500000)),
                        purchase_date_str=args.get("purchase_date", "2005-01-01"),
                        sale_date_str="2026-06-01"
                    )
                    content_text = json.dumps(res, ensure_ascii=False, indent=2)
                else:
                    res = resolve_discipline_payload(args.get("building_id", "שלד"))
                    content_text = json.dumps(res, ensure_ascii=False, indent=2)

                reply = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {"content": [{"type": "text", "text": content_text}]}
                }
            else:
                reply = {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(reply, ensure_ascii=False).encode('utf-8'))
            return

        # Direct REST API
        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        res = get_case_data(str(req_json.get("case_id", "")))
        self.wfile.write(json.dumps(res, ensure_ascii=False).encode('utf-8'))

def run_server(port=8080):
    server_address = ('0.0.0.0', port)
    httpd = HTTPServer(server_address, LegalixMasterBridgeHandler)
    print(f"Legalix Master Dynamic Server running on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    p = 8080
    if len(sys.argv) > 1:
        p = int(sys.argv[1])
    run_server(p)
