#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Legalix Unified Master Remote MCP Server — Claude Mobile & Web Compatible (JSON-RPC 2.0 & REST)
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os
import sys

sys.path.append('/opt/legalix')
sys.path.append('/home/yogi/lod_project')

from legalix_omni_discipline_resolver import resolve_discipline_payload
from legalix_taxland_engine import LegalixTaxLandEngine
from legalix_megacase_agent_standalone import LegalixMegaCaseAgent

tax_engine = LegalixTaxLandEngine()
megacase_agent = LegalixMegaCaseAgent()

MCP_TOOLS_MANIFEST = [
    {
        "name": "legalix_mega_case",
        "description": "חדר המלחמה המשפטי של Legalix Mega-Case: ניתוח עומק של תיקי ענק, סתירות כירורגיות, ציר זמן מלא וחקירה נגדית ע״י 13 סוכני-משנה מומחים.",
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
            "server": "Legalix Cloud Master Remote MCP Engine (35.242.250.144)",
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

        # Handle Standard JSON-RPC 2.0 (Claude Remote MCP Protocol)
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
                        "serverInfo": {"name": "legalix-mega-case-cloud", "version": "1.0.0"}
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
                    res = megacase_agent.run_investigation(args.get("case_id", "CASE-POLINER"), args.get("query", ""))
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

        # Handle Standard REST APIs
        path = self.path.lower()
        if "taxland" in path:
            res = tax_engine.calculate_betterment_tax_linear(
                purchase_price=float(req_json.get("purchase_price", 1000000)),
                sale_price=float(req_json.get("sale_price", 3500000)),
                purchase_date_str=req_json.get("purchase_date", "2005-01-01"),
                sale_date_str="2026-06-01"
            )
        elif "mega_case" in path or "poliner" in str(req_json):
            res = megacase_agent.run_investigation("CASE-POLINER-62449-03-24", str(req_json))
        else:
            res = resolve_discipline_payload(str(req_json.get("building_id", "")))

        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(res, ensure_ascii=False).encode('utf-8'))

def run_server(port=8080):
    server_address = ('0.0.0.0', port)
    httpd = HTTPServer(server_address, LegalixMasterBridgeHandler)
    print(f"Legalix Master Remote MCP Server running on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    p = 8080
    if len(sys.argv) > 1:
        p = int(sys.argv[1])
    run_server(p)
