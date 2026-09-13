#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Legalix True Multi-Discipline Dynamic Image Server
משרת תמונות נפרדות ומדויקות לכל דיסציפלינה: אינסטלציה, חשמל, מיזוג, אדריכלות, שלד ופיתוח!
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import re
import os
import sys

sys.path.append('/opt/legalix')
sys.path.append('/home/yogi/lod_project')

from legalix_real_dynamic_gateway import get_case_data
from legalix_taxland_engine import LegalixTaxLandEngine

tax_engine = LegalixTaxLandEngine()

IMAGE_PATHS = {
    "structural": "/mnt/c/Users/user1/Desktop/פרויקט_לוד_קונסטרוקציה/צילום_תוכנית_קונסטרוקציה_מלאה.png",
    "architectural": "/mnt/c/Users/user1/Desktop/פרויקט_לוד_קונסטרוקציה/צילום_תוכנית_אדריכלות_נקייה.png",
    "electrical": "/mnt/c/Users/user1/Desktop/פרויקט_לוד_קונסטרוקציה/צילום_גיליון_חשמל_26.png",
    "plumbing": "/mnt/c/Users/user1/Desktop/פרויקט_לוד_קונסטרוקציה/markup_plumbing_01_water_tanks.png",
    "hvac": "/mnt/c/Users/user1/Desktop/פרויקט_לוד_קונסטרוקציה/markup_hvac_01_jet_fans_parking.png",
    "landscape": "/mnt/c/Users/user1/Desktop/פרויקט_לוד_קונסטרוקציה/markup_ls_01_lobby_threshold_flooding.png"
}

HEBREW_ORDINALS = {
    "ראשון": 1, "ראשונה": 1, "שני": 2, "שניה": 2, "שלישי": 3, "שלישית": 3,
    "רביעי": 4, "רביעית": 4, "חמישי": 5, "חמישית": 5, "שישי": 6, "שישית": 6,
    "שביעי": 7, "שביעית": 7, "שמיני": 8, "שמינית": 8, "תשיעי": 9, "תשיעית": 9,
    "עשירי": 10, "עשרים": 20, "שלושים": 30, "ארבעים": 40
}

def extract_number_from_text(p):
    digits = re.findall(r'\d+', p)
    if digits:
        return int(digits[0])
    for word, val in HEBREW_ORDINALS.items():
        if word in p:
            return val
    return 1

def parse_and_execute_generic_engineering_query(prompt_text, host_header):
    p = prompt_text.lower()
    sheet_num = extract_number_from_text(p)
    base_img_url = f"https://{host_header}/images"

    # 1. Plumbing (אינסטלציה, ספרינקלר, מים, ביוב)
    if any(k in p for k in ["אינסטלציה", "ספרינקלר", "plumbing", "ביוב", "מים", "שופכין", "משאבות"]):
        img_url = f"{base_img_url}/plumbing.png"
        return {
            "status": "SUCCESS",
            "operation": "PLUMBING_SHEET_RENDER",
            "project_name": "פרויקט לוד ניר צבי — עמרם אברהם",
            "sheet_id": f"PL-{sheet_num:03d}",
            "sheet_title": f"צילום גיליון אינסטלציה וספרינקלרים מס' {sheet_num} (PL-{sheet_num:03d}) — פריסת צנרת מים, ביוב ומאגרי כיבוי",
            "scale": "1:50",
            "direct_image_png_url": img_url,
            "image_markdown": f"![צילום גיליון אינסטלציה PL-{sheet_num:03d}]({img_url})",
            "message": f"הנה צילום הגיליון הישיר של אינסטלציה (תמונת PNG נקייה): {img_url}"
        }

    # 2. Electrical (חשמל)
    elif any(k in p for k in ["חשמל", "electrical", "תאורה", "לוח", "כבלים", "מפסק"]):
        img_url = f"{base_img_url}/electrical.png"
        return {
            "status": "SUCCESS",
            "operation": "ELECTRICAL_SHEET_RENDER",
            "project_name": "פרויקט לוד ניר צבי — עמרם אברהם",
            "sheet_id": f"EL-{sheet_num:03d}",
            "sheet_title": f"צילום גיליון חשמל מס' {sheet_num} (EL-{sheet_num:03d}) — פריסת לוחות, תאורת חירום ומסלולי כבלים",
            "scale": "1:50",
            "direct_image_png_url": img_url,
            "image_markdown": f"![צילום גיליון חשמל EL-{sheet_num:03d}]({img_url})",
            "message": f"הנה צילום הגיליון הישיר של חשמל (תמונת PNG נקייה): {img_url}"
        }

    # 3. Architecture (אדריכלות)
    elif any(k in p for k in ["אדריכל", "arch", "דירות", "מכר", "חלוקה", "קומה טיפוסית"]):
        img_url = f"{base_img_url}/architectural.png"
        return {
            "status": "SUCCESS",
            "operation": "ARCHITECTURAL_SHEET_RENDER",
            "project_name": "פרויקט לוד ניר צבי — עמרם אברהם",
            "sheet_id": f"A-{sheet_num:03d}",
            "sheet_title": f"צילום גיליון אדריכלות מס' {sheet_num} (A-{sheet_num:03d}) — תוכנית קומה טיפוסית, חלוקת דירות ומרפסות",
            "scale": "1:50",
            "direct_image_png_url": img_url,
            "image_markdown": f"![צילום גיליון אדריכלות A-{sheet_num:03d}]({img_url})",
            "message": f"הנה צילום הגיליון הישיר של אדריכלות (תמונת PNG נקייה): {img_url}"
        }

    # 4. HVAC / Smoke (מיזוג ועשן)
    elif any(k in p for k in ["מיזוג", "hvac", "עשן", "מפוח", "אוורור"]):
        img_url = f"{base_img_url}/hvac.png"
        return {
            "status": "SUCCESS",
            "operation": "HVAC_SHEET_RENDER",
            "project_name": "פרויקט לוד ניר צבי — עמרם אברהם",
            "sheet_id": f"M-{sheet_num:03d}",
            "sheet_title": f"צילום גיליון מיזוג ועשן מס' {sheet_num} (M-{sheet_num:03d}) — פריסת מפוחי סילון ותעלות עשן",
            "scale": "1:50",
            "direct_image_png_url": img_url,
            "image_markdown": f"![צילום גיליון מיזוג M-{sheet_num:03d}]({img_url})",
            "message": f"הנה צילום הגיליון הישיר של מיזוג ועשן (תמונת PNG נקייה): {img_url}"
        }

    # 5. Landscape & Development (פיתוח נופי)
    elif any(k in p for k in ["נוף", "פיתוח", "חצר", "landscape"]):
        img_url = f"{base_img_url}/landscape.png"
        return {
            "status": "SUCCESS",
            "operation": "LANDSCAPE_SHEET_RENDER",
            "project_name": "פרויקט לוד ניר צבי — עמרם אברהם",
            "sheet_id": f"LND-{sheet_num:03d}",
            "sheet_title": f"צילום גיליון פיתוח נופי מס' {sheet_num} (LND-{sheet_num:03d}) — מפלסי ספי לובי וניקוז",
            "scale": "1:100",
            "direct_image_png_url": img_url,
            "image_markdown": f"![צילום גיליון פיתוח LND-{sheet_num:03d}]({img_url})",
            "message": f"הנה צילום הגיליון הישיר של פיתוח נופי: {img_url}"
        }

    # 6. Default: Structural (שלד וקונסטרוקציה)
    else:
        img_url = f"{base_img_url}/structural.png"
        return {
            "status": "SUCCESS",
            "operation": "STRUCTURAL_SHEET_RENDER",
            "project_name": "פרויקט לוד ניר צבי — עמרם אברהם",
            "sheet_id": f"ST-{sheet_num:03d}",
            "sheet_title": f"צילום גיליון קונסטרוקציה מס' {sheet_num} (ST-{sheet_num:03d}) — תוכנית יסודות וקורות זיון",
            "scale": "1:50",
            "direct_image_png_url": img_url,
            "image_markdown": f"![צילום גיליון קונסטרוקציה ST-{sheet_num:03d}]({img_url})",
            "message": f"הנה צילום הגיליון הישיר של קונסטרוקציה: {img_url}"
        }

class DirectImageMasterHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.end_headers()

    def do_GET(self):
        if "/images/" in self.path:
            img_name = self.path.split("/images/")[-1].replace(".png", "").strip().lower()
            file_path = IMAGE_PATHS.get(img_name, IMAGE_PATHS["structural"])
            
            if os.path.exists(file_path):
                self.send_response(200)
                self.send_header('Content-Type', 'image/png')
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
        self.wfile.write(json.dumps({"status": "ONLINE", "server": "Legalix Multi-Discipline Image Server"}, ensure_ascii=False).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        host_header = self.headers.get('Host', 'inclusion-refer-maintenance-associations.trycloudflare.com')
        
        try:
            req_json = json.loads(post_data.decode('utf-8'))
        except Exception:
            req_json = {}

        prompt_text = (
            str(req_json.get("building_id", "")) + " " +
            str(req_json.get("instruction", "")) + " " +
            str(req_json.get("query", "")) + " " +
            str(req_json.get("task", ""))
        ).strip()

        path = self.path.lower()
        
        if "taxland" in path:
            res = tax_engine.calculate_betterment_tax_linear(
                purchase_price=float(req_json.get("purchase_price", 1000000)),
                sale_price=float(req_json.get("sale_price", 3500000)),
                purchase_date_str=req_json.get("purchase_date", "2005-01-01"),
                sale_date_str="2026-06-01"
            )
        elif "mega" in path or "poliner" in prompt_text.lower():
            res = get_case_data(req_json.get("case_id", "CASE-POLINER"), prompt_text)
        else:
            res = parse_and_execute_generic_engineering_query(prompt_text, host_header)

        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(res, ensure_ascii=False).encode('utf-8'))

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8080), DirectImageMasterHandler)
    print("Legalix Multi-Discipline Image Server running on port 8080...")
    server.serve_forever()
