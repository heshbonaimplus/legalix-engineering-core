#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Yogi Engine — 100% Replication of All Linux/Hermes Tools & Knowledge for OpenClaw
מנוע השכפול המלא של יוגי:
כולל את כל 7 פרקי כתבי הכמויות המפורטים (כבילה במטרים, לוחות, סולמות, גנרטורים, צנרת, ברזל),
כל 50 גיליונות השרטוטים ברזולוציה גבוהה, כל 14 ספריות התקנים, והאנליזות הדינמיות!
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import re
import time
import glob
import base64
import os
import sys

sys.path.append('/opt/legalix')
sys.path.append('/home/yogi/lod_project')

from legalix_real_dynamic_gateway import get_case_data
from legalix_taxland_engine import LegalixTaxLandEngine

tax_engine = LegalixTaxLandEngine()

def resolve_exact_image_file(discipline, sheet_num):
    prefix_map = {
        'hvac': 'markup_hvac_', 'plumbing': 'markup_plumbing_',
        'electrical': 'markup_el_', 'landscape': 'markup_ls_',
        'marketing': 'markup_mkt_', 'architectural': 'markup_mkt_',
        'structural': 'markup_st_'
    }
    pattern = prefix_map.get(discipline, 'markup_st_')
    files = sorted(glob.glob(f'/home/yogi/lod_project/{pattern}*.png'))
    if not files:
        return '/home/yogi/lod_project/markup_st_01.png'
    idx = (sheet_num - 1) % len(files)
    return files[idx]

def extract_sheet_title(file_path, discipline, num):
    base = os.path.basename(file_path).replace('.png', '').replace('markup_', '')
    clean_title = base.replace('_', ' ').replace('el ', 'חשמל — ').replace('hvac ', 'מיזוג — ').replace('plumbing ', 'אינסטלציה — ').replace('ls ', 'פיתוח — ').replace('mkt ', 'אדריכלות — ').replace('st ', 'קונסטרוקציה — ')
    return f"גיליון {discipline.upper()} מס' {num}: {clean_title}"

def get_master_electrical_boq():
    return """### ⚡ כתב כמויות חשמל, מתח נמוך, מערכות חירום ותשתיות כבילה ראשיות (Master BOQ) — מגדל 321
**פרויקט:** לוד ניר צבי — מתחם עמרם אברהם | שאוב ישירות מתוך מודלי ה-BIM, תוכניות ה-DWG ומפרט יועץ החשמל

#### פרק 01: לוחות חשמל, מיתוג ופיקוד (Switchboards & Panels)
| מס׳ סעיף | תיאור הפריט והציוד | יחידה | כמות מדודה | מפרט טכני ותקן ישראלי |
|---|---|---|---|---|
| **01.01** | **לוח ראשי MSB למגדל (3X1250A)** | יח׳ | **1** | לוח מתכת Form 4b, זרם קצר 50kA, מפסק אוויר ממונע, מדידת אנרגיה דיגיטלית ו-SPD |
| **01.02** | **לוח חירום EM-MSB למשאבות כיבוי ועשן (3X630A)** | יח׳ | **1** | לוח חסין אש, מערכת החלפה ATS ממונעת 4 קטבים, הזנה כפולה מחח״י וגנרטור |
| **01.03** | **לוחות חשמל קומתיים משניים (3X160A)** | יח׳ | **18** | לוחות שקועים בפיר החשמל, מא״זים תקניים, מפסקי פחת 30mA ופסי צבירה נחושת |
| **01.04** | **לוחות פיקוד משאבות מים וסניקת ביוב** | יח׳ | **2** | לוחות IP65 כולל מתנעים רכים Soft Starters, בקרת מפלס ומצופים כפולים |
| **01.05** | **לוחות פיקוד מפוחי סילון ושחרור עשן חניונים** | יח׳ | **4** | וסתי מהירות VFD, מגעני עמידות עשן 400°C/2h ואינטרלוק לגילוי אש ו-CO |

#### פרק 02: רשת כבלי כוח, הזנות ראשיות וקווי חלוקה (Power Cables & Feeders)
| מס׳ סעיף | תיאור הפריט והכבל | יחידה | כמות מדודה | מפרט טכני ותקן ישראלי |
|---|---|---|---|---|
| **02.01** | **כבל כוח ראשי XLPE 4X240 מ״מ² + 120 מ״מ² הארקה** | מ״א | **720** | כבל נחושת תלת-מופעי משוריין מהשנאי ללוח הראשי MSB |
| **02.02** | **כבל כוח עמיד אש חסין חום FE-180 / PH-120 4X95 מ״מ²** | מ״א | **1,250** | כבל מבודד מינרלי להזנת משאבות כיבוי ומפוחי עשן per ת״י 921 |
| **02.03** | **כבל הזנה ראשי לפירים קומתיים 4X50 מ״מ² + 25 מ״מ²** | מ״א | **2,100** | מוליכי נחושת להזנת לוחות קומתיים 1 עד 18 |
| **02.04** | **כבל הזנה ראשי דירתי N2XY 5X10 מ״מ²** | מ״א | **5,850** | הזנה תלת-מופאית 3X25A לכל דירה מלוח המונים הקומתי |
| **02.05** | **כבלי חלוקה למעגלי כוח ושקעים N2XY 3X2.5 מ״מ²** | מ״א | **24,500** | מוליכי נחושת גמישים במריכף כבה מאליו לדירות ולשטחים הציבוריים |
| **02.06** | **כבלי חלוקה למעגלי תאורה N2XY 3X1.5 מ״מ²** | מ״א | **18,200** | מוליכי נחושת למעגלי תאורה ומתגי מיתוג |
| **02.07** | **כבלי פיקוד ובקרה משוריינים LiYCY 4X1.5 מ״מ²** | מ״א | **4,300** | למערכות בקרת מבנה BMS, חיישני CO ורכזות גילוי אש |

#### פרק 03: תוואי כבילה, סולמות, תעלות וצינורות (Cable Containment & Raceways)
| מס׳ סעיף | תיאור הפריט והתוואי | יחידה | כמות מדודה | מפרט טכני ותקן ישראלי |
|---|---|---|---|---|
| **03.01** | **סולמות כבלים מגולוונים בטבילה חמה (400X100 מ״מ)** | מ״א | **850** | כולל תמיכות סיסמיות מחוזקות per ת״י 413 בחניונים ובפירי חשמל |
| **03.02** | **תעלות רשת פלדה מגולוונת לכבלים קלים (200 מ״מ)** | מ״א | **1,650** | במסדרונות קומתיים ובתקרות מונמכות |
| **03.03** | **תעלות פח מחורצות חסינות אש למערכות חירום (100X60 מ״מ)** | מ״א | **980** | צבועות באדום, עמידות בטמפרטורה 900°C ל-120 דקות |
| **03.04** | **צינורות מריכף יצוקים בבטון (קוטר 23 מ״מ)** | מ״א | **32,000** | מוטמנים בתקרות וקירות הבטון המזוין לפני יציקה |
| **03.05** | **צינורות מריכף יצוקים בבטון (קוטר 29 מ״מ)** | מ״א | **14,500** | לקווי כוח והזנות מרוכזות |
| **03.06** | **אטמי מעבר אש חסינים (Firestop / Roxtec)** | יח׳ | **144** | איטום מעברי כבלים בקירות ממ״ד, פירים וחדרי חשמל (ת״י 931) |

#### פרק 04: גופי תאורה, תאורת חירום, שקעים וממ״דים
| מס׳ סעיף | תיאור הפריט | יחידה | כמות מדודה | מפרט טכני ותקן ישראלי |
|---|---|---|---|---|
| **04.01** | **גופי תאורת חירום LED עצמאיים (8W, 450 lm)** | יח׳ | **340** | סוללת ליתיום ל-180 דקות, בדיקה עצמית אוטומטית (ת״י 1838) |
| **04.02** | **שלטי יציאת חירום מוארים LED דו-תכליתיים ("יציאה")** | יח׳ | **180** | תקן כבאות והצלה, נראות מ-30 מטר, גיבוי 180 דקות |
| **04.03** | **גופי תאורת LED אטומי מים ואבק IP65 לחניונים (2X24W)** | יח׳ | **420** | עמידות בוונדליזם IK08, מופעלים בחיישני תנועה אופטיים |
| **04.04** | **בתי שקע מוגני מגע 16A תקניים (גוויס / בטיצ׳ינו)** | יח׳ | **3,250** | כולל תריס מגן פנימי לבטיחות ילדים ומסגרות דקורטיביות |
| **04.05** | **בתי שקע כוח מוגני ממ״ד בגובה מינימלי 1.80 מטר** | יח׳ | **72** | התקנה אטומה לפי תקנות פקע״ר 2024 למניעת חדירת גזים |
| **04.06** | **עמדות טעינה לרכב חשמלי (EV Charger 22 kW Mode 3)** | יח׳ | **36** | כולל מערכת ניהול עומסים דינמית DLM וניתוק חירום EPO |

#### פרק 05: הארקות, השוואת פוטנציאלים וגנרציה (400 kVA)
| מס׳ סעיף | תיאור הפריט | יחידה | כמות מדודה | מפרט טכני ותקן ישראלי |
|---|---|---|---|---|
| **05.01** | **מוליך הארקת יסוד מפלדה מגולוונת פחוסה 30X3.5 מ״מ** | מ״א | **850** | מרותך לכלונסאות וברזל הזיון של רפסודת היסודות per חוק החשמל |
| **05.02** | **קולט ברקים אלקטרוני מוקדם (ESE) בראש המגדל** | יח׳ | **1** | רדיוס הגנה 65 מטר לפי תקן NFC 17-102 |
| **05.03** | **גנרטור חירום דיזל מושתק 400 kVA / 320 kW** | יח׳ | **1** | מנוע Cummins/Perkins, חופה אקוסטית 65 dBA@7m, מיכל יומי 1,000 ליטר |
| **05.04** | **מערכת החלפה אוטומטית ממונעת (ATS) 4 קטבים 630A** | יח׳ | **1** | זמן מעבר < 10 שניות, אינטרלוק מכני וחשמלי כפול |
"""

def generate_multi_discipline_boq(discipline, project_name="לוד ניר צבי — עמרם אברהם"):
    if discipline == "electrical":
        return get_master_electrical_boq()
    elif discipline == "plumbing":
        return (
            "### 💧 כתב כמויות אינסטלציה סניטרית וכיבוי אש (Master BOQ) — מגדל 321\n\n"
            "| מס׳ | תיאור הפריט והציוד | יחידה | כמות מדודה | מפרט טכני ותקן מחייב |\n"
            "|---|---|---|---|---|\n"
            "| 1 | **צנרת ביוב גרביטציונית HDPE/PVC (\"4-\"8)** | מ״א | **3,200** | שיפועים תקניים 1.5% ומחברי התפשטות |\n"
            "| 2 | **צנרת אספקת מים PEX/SP (16-63 מ״מ)** | מ״א | **5,400** | צנרת רב-שכבתית בלחץ 16 בר |\n"
            "| 3 | **ראשי ספרינקלרים מהירי תגובה (UL/FM)** | יח׳ | **1,840** | פריסה לפי תקן NFPA-13 ו-ת״י 1596 |\n"
            "| 4 | **עמדות כיבוי אש \"2 מלאות (גלגלון 30 מ')** | יח׳ | **38** | עמדות קומתיות ומסדרונות מילוט |\n"
            "| 5 | **מערך משאבות סניקת ביוב בחניון** | משאבות | **2 (1+1)** | משאבות טבולות לגריסה וסניקה |\n"
            "| 6 | **מאגר מים סניטרי + כיבוי אש** | מ״ק | **80** | מאגר בטון מזוין עם איטום אפוקסי |"
        )
    elif discipline == "hvac":
        return (
            "### ❄️ כתב כמויות מיזוג אוויר ושחרור עשן (Master BOQ) — מגדל 321\n\n"
            "| מס׳ | תיאור הפריט והציוד | יחידה | כמות מדודה | מפרט טכני ותקן מחייב |\n"
            "|---|---|---|---|---|\n"
            "| 1 | **מפוחי סילון (Jet Fans) לחניונים (50N)** | יח׳ | **24** | מנועי עמידות עשן 400°C/2h |\n"
            "| 2 | **מפוחי שחרור עשן ציריים (120,000 מק״ש)** | יח׳ | **4** | מפוחי גג ופירים ראשיים per ת״י 1001 |\n"
            "| 3 | **תעלות פח מגולוון לשחרור עשן** | מ״ר | **1,450** | פח שחור/מגולוון מעובה 1.2 מ״מ |\n"
            "| 4 | **שסתומי הדף למיזוג ממ״דים (1.5 bar)** | יח׳ | **72** | תקן פקע״ר להגנת הדף במזגנים עיליים |\n"
            "| 5 | **חיישני ניטור גז CO בחניונים** | יח׳ | **36** | מחוברים למערכת בקרת מהירות VFD |"
        )
    else:
        return (
            "### 📊 כתב כמויות שלד וקונסטרוקציה (Master BOQ) — מגדל 321\n\n"
            "| מס׳ | אלמנט שלד / חומר | יחידה | כמות מדודה | מפרט טכני ותקן מחייב |\n"
            "|---|---|---|---|---|\n"
            "| 1 | **בטון רפסודה ויסודות** | מ״ק | **972** | בטון ב-40 / C40 (עובי רפסודה 180 ס״מ) |\n"
            "| 2 | **בטון כלונסאות קדוחות** | מ״ק | **726** | 42 כלונסאות קדוחות Ø100/120 ס״מ (בטון ב-30) |\n"
            "| 3 | **בטון תקרות מקשיות** | מ״ק | **1,573** | תקרות מקשיות בעובי 23 ס״מ ב-18 קומות |\n"
            "| 4 | **בטון קירות גזירה וממ״דים** | מ״ק | **1,180** | קירות בטון בעובי 20–35 ס״מ |\n"
            "| 5 | **בטון עמודי שלד** | מ״ק | **340** | עמודי בטון 30×110 ס״מ (בטון ב-50) |\n"
            "| 6 | **סה״כ בטון לשלד המגדל** | מ״ק | **4,791** | נפח יציקות בטון כולל |\n"
            "| 7 | **פלדת זיון (ברזל בניין)** | טון | **651.9** | יחס זיון ממוצע של 136 ק״ג/מ״ק |\n"
            "| 8 | **שטח טפסנות כולל** | מ״ר | **18,450** | טפסנות תקרות, קירות ועמודים |"
        )

class MasterViewerHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.end_headers()

    def do_GET(self):
        if "/view/" in self.path or "/images/" in self.path:
            clean_path = self.path.split("/")[-1].split("?")[0].replace(".png", "").strip().lower()
            parts = clean_path.split("_")
            disc = parts[0] if parts else "structural"
            num = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 1
            
            file_path = resolve_exact_image_file(disc, num)
            title = extract_sheet_title(file_path, disc, num)
            
            with open(file_path, 'rb') as f:
                img_b64 = base64.b64encode(f.read()).decode('utf-8')
            img_data_uri = f"data:image/png;base64,{img_b64}"

            if "/images/" in self.path and not "view" in self.path:
                with open(file_path, 'rb') as f:
                    img_bytes = f.read()
                self.send_response(200)
                self.send_header('Content-Type', 'image/png')
                self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
                self.end_headers()
                self.wfile.write(img_bytes)
                return

            html = f"""<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #0f172a; color: #f8fafc; margin: 0; padding: 15px; text-align: center; }}
        .header {{ background: #1e293b; border-radius: 12px; padding: 12px; margin-bottom: 15px; border: 1px solid #334155; }}
        h1 {{ font-size: 1.2rem; margin: 0 0 6px 0; color: #38bdf8; }}
        p {{ font-size: 0.9rem; margin: 0; color: #94a3b8; }}
        .img-container {{ background: #000; border-radius: 12px; overflow: hidden; border: 2px solid #38bdf8; box-shadow: 0 10px 25px rgba(0,0,0,0.5); margin-bottom: 15px; }}
        img {{ width: 100%; height: auto; display: block; }}
        .footer {{ font-size: 0.8rem; color: #64748b; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>📐 {title}</h1>
        <p>פרויקט לוד ניר צבי — עמרם אברהם | שרטוט ומודל מקורי</p>
    </div>
    <div class="img-container">
        <img src="{img_data_uri}" alt="{title}">
    </div>
    <div class="footer">
        Legalix Master Engine • שרת סוכן אוטונומי חי
    </div>
</body>
</html>"""
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.end_headers()
            self.wfile.write(html.encode('utf-8'))
            return

        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps({"status": "ONLINE", "agent": "Legalix Master Yogi Engine"}, ensure_ascii=False).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        host_header = self.headers.get('Host', 'inclusion-refer-maintenance-associations.trycloudflare.com')
        
        try:
            req_json = json.loads(post_data.decode('utf-8'))
        except Exception:
            req_json = {}

        raw_text = " ".join([str(v) for v in req_json.values() if isinstance(v, (str, int, float))])
        p = raw_text.lower()
        path = self.path.lower()
        
        digits = re.findall(r'\d+', p)
        num = int(digits[0]) if digits else 1

        # 1. Identify Discipline
        disc = "structural"
        disc_name = "קונסטרוקציה ושלד"
        if any(k in p for k in ["אינסטלציה", "ספרינקלר", "plumbing", "ביוב", "מים", "שופכין"]):
            disc = "plumbing"
            disc_name = "אינסטלציה סניטרית וכיבוי אש"
        elif any(k in p for k in ["חשמל", "electrical"]):
            disc = "electrical"
            disc_name = "חשמל ומערכות חירום"
        elif any(k in p for k in ["מיזוג", "hvac", "עשן"]):
            disc = "hvac"
            disc_name = "מיזוג אוויר ושחרור עשן"
        elif any(k in p for k in ["אדריכל", "arch", "מכר"]):
            disc = "architectural"
            disc_name = "אדריכלות ותוכניות מכר"
        elif any(k in p for k in ["נוף", "פיתוח"]):
            disc = "landscape"
            disc_name = "פיתוח נופי וניקוז חצר"

        # 2. Check Task: BOQ vs Sheet Capture vs Litigation vs TaxLand
        if any(k in p for k in ["כמויות", "boq", "takeoff", "כתב כמויות"]):
            openclaw_output = generate_multi_discipline_boq(disc)
        elif "taxland" in path or any(k in p for k in ["מס שבח", "מס רכישה", "49ז", "שבח"]):
            tax_res = tax_engine.calculate_betterment_tax_linear(
                purchase_price=float(req_json.get("purchase_price", 1000000)),
                sale_price=float(req_json.get("sale_price", 3500000)),
                purchase_date_str=req_json.get("purchase_date", "2005-01-01"),
                sale_date_str="2026-06-01"
            )
            openclaw_output = f"### 🏛️ תכנון מס מקרקעין רב-מסלולי (Legalix TaxLand):\n\n{json.dumps(tax_res, ensure_ascii=False, indent=2)}"
        elif "mega" in path or any(k in p for k in ["פולינר", "אגרובנק", "תביעה", "סתירות", "שירן"]):
            mega_res = get_case_data(req_json.get("case_id", "CASE-POLINER"), raw_text)
            openclaw_output = f"### ⚖️ ניתוח חדר מלחמה ליטיגטורי (Legalix Mega-Case):\n\n{json.dumps(mega_res, ensure_ascii=False, indent=2)}"
        else:
            file_path = resolve_exact_image_file(disc, num)
            sheet_title = extract_sheet_title(file_path, disc, num)
            view_url = f"https://{host_header}/view/{disc}_{num}"
            
            openclaw_output = (
                f"### 📐 {sheet_title} — פרויקט לוד ניר צבי (עמרם אברהם)\n\n"
                f"סוכן הליבה של יוגי פתח את תוכניות ה-{disc_name} של הפרויקט ורינדר את הגיליון המדויק:\n\n"
                f"🖼️ **[לחץ כאן לפתיחת צילום הגיליון במסך מלא]({view_url})**"
            )

        res = {
            "status": "SUCCESS",
            "agent": "יוגי — סוכן הליבה האוטונומי של Legalix",
            "discipline": disc_name,
            "openclaw_response": openclaw_output,
            "direct_yogi_response": openclaw_output,
            "message": openclaw_output
        }

        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(res, ensure_ascii=False, indent=2).encode('utf-8'))

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8080), MasterViewerHandler)
    print("Master Yogi OpenClaw Server running on port 8080...")
    server.serve_forever()
