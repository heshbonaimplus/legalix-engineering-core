#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Legalix Dynamic Per-Discipline & Per-Sheet Image Server
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import re
import time
import glob
import os
import sys

sys.path.append('/opt/legalix')
sys.path.append('/home/yogi/lod_project')

from legalix_real_dynamic_gateway import get_case_data
from legalix_taxland_engine import LegalixTaxLandEngine

tax_engine = LegalixTaxLandEngine()

HEBREW_ORDINALS = {
    "ראשון": 1, "ראשונה": 1, "שני": 2, "שניה": 2, "שלישי": 3, "שלישית": 3,
    "רביעי": 4, "רביעית": 4, "חמישי": 5, "חמישית": 5, "שישי": 6, "שישית": 6,
    "שביעי": 7, "שביעית": 7, "שמיני": 8, "שמינית": 8, "תשיעי": 9, "תשיעית": 9,
    "עשירי": 10, "עשרים": 20, "שלושים": 30, "שלושים ואחת": 31, "ארבעים": 40
}

def extract_number_from_text(p):
    digits = re.findall(r'\d+', p)
    if digits:
        return int(digits[0])
    for word, val in HEBREW_ORDINALS.items():
        if word in p:
            return val
    return 1

def resolve_exact_image_file(discipline, sheet_num):
    prefix_map = {
        'hvac': 'markup_hvac_',
        'plumbing': 'markup_plumbing_',
        'electrical': 'markup_el_',
        'landscape': 'markup_ls_',
        'marketing': 'markup_mkt_',
        'architectural': 'markup_mkt_',
        'structural': 'LOD_321_FULL_STRUCTURAL_PLAN'
    }
    pattern = prefix_map.get(discipline, 'markup_ls_')
    files = sorted(glob.glob(f'/home/yogi/lod_project/{pattern}*.png'))
    if not files:
        return '/home/yogi/lod_project/markup_ls_01_lobby_threshold_flooding.png'
    idx = (sheet_num - 1) % len(files)
    return files[idx]

def parse_and_execute_generic_engineering_query(prompt_text, host_header):
    p = prompt_text.lower()
    sheet_num = extract_number_from_text(p)
    ts = int(time.time() * 1000)
    base_img_url = f"https://{host_header}/images"

    # 1. Landscape (פיתוח / נוף / חצר)
    if any(k in p for k in ["נוף", "פיתוח", "חצר", "landscape"]):
        img_url = f"{base_img_url}/landscape_{sheet_num}.png"
        return {
            "status": "SUCCESS",
            "operation": "LANDSCAPE_SHEET_RENDER",
            "project_name": "פרויקט לוד ניר צבי — עמרם אברהם",
            "sheet_number": f"LND-{sheet_num:03d}",
            "sheet_title": f"צילום גיליון פיתוח נופי מס' {sheet_num} (LND-{sheet_num:03d}) — מפלסי ספי לובי, השקיה וניקוז חצר",
            "scale": "1:100",
            "direct_image_png_url": img_url,
            "image_markdown": f"![צילום גיליון פיתוח LND-{sheet_num:03d}]({img_url})",
            "message": f"הנה צילום גיליון פיתוח נופי מס' {sheet_num}: {img_url}"
        }

    # 2. Architecture (אדריכלות / דירות / מכר)
    elif any(k in p for k in ["אדריכל", "arch", "דירות", "מכר", "חלוקה", "קומה טיפוסית"]):
        img_url = f"{base_img_url}/architectural_{sheet_num}.png"
        return {
            "status": "SUCCESS",
            "operation": "ARCHITECTURAL_SHEET_RENDER",
            "project_name": "פרויקט לוד ניר צבי — עמרם אברהם",
            "sheet_number": f"A-{sheet_num:03d}",
            "sheet_title": f"צילום גיליון אדריכלות מס' {sheet_num} (A-{sheet_num:03d}) — תוכנית קומה טיפוסית וחלוקת דירות",
            "scale": "1:50",
            "direct_image_png_url": img_url,
            "image_markdown": f"![צילום גיליון אדריכלות A-{sheet_num:03d}]({img_url})",
            "message": f"הנה צילום גיליון אדריכלות מס' {sheet_num}: {img_url}"
        }

    # 3. Electrical (חשמל / תאורה / לוחות)
    elif any(k in p for k in ["חשמל", "electrical", "תאורה", "לוח", "כבלים", "מפסק"]):
        img_url = f"{base_img_url}/electrical_{sheet_num}.png"
        return {
            "status": "SUCCESS",
            "operation": "ELECTRICAL_SHEET_RENDER",
            "project_name": "פרויקט לוד ניר צבי — עמרם אברהם",
            "sheet_number": f"EL-{sheet_num:03d}",
            "sheet_title": f"צילום גיליון חשמל מס' {sheet_num} (EL-{sheet_num:03d}) — פריסת לוחות, תאורת חירום ומסלולי כבלים",
            "scale": "1:50",
            "direct_image_png_url": img_url,
            "image_markdown": f"![צילום גיליון חשמל EL-{sheet_num:03d}]({img_url})",
            "message": f"הנה צילום גיליון חשמל מס' {sheet_num}: {img_url}"
        }

    # 4. HVAC / Smoke (מיזוג / עשן / מפוח)
    elif any(k in p for k in ["מיזוג", "hvac", "עשן", "מפוח", "אוורור"]):
        img_url = f"{base_img_url}/hvac_{sheet_num}.png"
        return {
            "status": "SUCCESS",
            "operation": "HVAC_SHEET_RENDER",
            "project_name": "פרויקט לוד ניר צבי — עמרם אברהם",
            "sheet_number": f"M-{sheet_num:03d}",
            "sheet_title": f"צילום גיליון מיזוג ועשן מס' {sheet_num} (M-{sheet_num:03d}) — פריסת מפוחי סילון ותעלות עשן",
            "scale": "1:50",
            "direct_image_png_url": img_url,
            "image_markdown": f"![צילום גיליון מיזוג M-{sheet_num:03d}]({img_url})",
            "message": f"הנה צילום גיליון מיזוג מס' {sheet_num}: {img_url}"
        }

    # 5. Plumbing (אינסטלציה / ספרינקלר / מים)
    elif any(k in p for k in ["אינסטלציה", "ספרינקלר", "plumbing", "ביוב", "מים"]):
        img_url = f"{base_img_url}/plumbing_{sheet_num}.png"
        return {
            "status": "SUCCESS",
            "operation": "PLUMBING_SHEET_RENDER",
            "project_name": "פרויקט לוד ניר צבי — עמרם אברהם",
            "sheet_number": f"PL-{sheet_num:03d}",
            "sheet_title": f"צילום גיליון אינסטלציה מס' {sheet_num} (PL-{sheet_num:03d}) — פריסת צנרת מים וביוב",
            "scale": "1:50",
            "direct_image_png_url": img_url,
            "image_markdown": f"![צילום גיליון אינסטלציה PL-{sheet_num:03d}]({img_url})",
            "message": f"הנה צילום גיליון אינסטלציה מס' {sheet_num}: {img_url}"
        }

    # 6. Default: Structural (קונסטרוקציה / שלד)
    else:
        img_url = f"{base_img_url}/structural_{sheet_num}.png"
        return {
            "status": "SUCCESS",
            "operation": "STRUCTURAL_SHEET_RENDER",
            "project_name": "פרויקט לוד ניר צבי — עמרם אברהם",
            "sheet_number": f"ST-{sheet_num:03d}",
            "sheet_title": f"צילום גיליון קונסטרוקציה מס' {sheet_num} (ST-{sheet_num:03d}) — תוכנית יסודות וקורות זיון",
            "scale": "1:50",
            "direct_image_png_url": img_url,
            "image_markdown": f"![צילום גיליון קונסטרוקציה ST-{sheet_num:03d}]({img_url})",
            "message": f"הנה צילום גיליון קונסטרוקציה מס' {sheet_num}: {img_url}"
        }

class PerSheetImageHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.end_headers()

    def do_GET(self):
        if "/images/" in self.path:
            clean_path = self.path.split("/images/")[-1].split("?")[0].replace(".png", "").strip().lower()
            parts = clean_path.split("_")
            disc = parts[0]
            num = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 1
            file_path = resolve_exact_image_file(disc, num)
            
            if os.path.exists(file_path):
                self.send_response(200)
                self.send_header('Content-Type', 'image/png')
                self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
                self.send_header('Pragma', 'no-cache')
                self.send_header('Expires', '0')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                with open(file_path, 'rb') as f:
                    self.wfile.write(f.read())
                return
            else:
                self.send_response(404)
                self.end_headers()
                return

        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps({"status": "ONLINE", "server": "Legalix Dynamic Per-Sheet Image Server"}, ensure_ascii=False).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        host_header = self.headers.get('Host', 'inclusion-refer-maintenance-associations.trycloudflare.com')
        
        try:
            req_json = json.loads(post_data.decode('utf-8'))
        except Exception:
            req_json = {}

        raw_text = " ".join([str(v) for v in req_json.values() if isinstance(v, (str, int, float))])

        path = self.path.lower()
        if "taxland" in path:
            res = tax_engine.calculate_betterment_tax_linear(
                purchase_price=float(req_json.get("purchase_price", 1000000)),
                sale_price=float(req_json.get("sale_price", 3500000)),
                purchase_date_str=req_json.get("purchase_date", "2005-01-01"),
                sale_date_str="2026-06-01"
            )
        elif "mega" in path or "poliner" in raw_text.lower():
            res = get_case_data(req_json.get("case_id", "CASE-POLINER"), raw_text)
        else:
            res = parse_and_execute_generic_engineering_query(raw_text, host_header)

        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(res, ensure_ascii=False).encode('utf-8'))

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8080), PerSheetImageHandler)
    print("Legalix Per-Sheet Image Server running on port 8080...")
    server.serve_forever()
