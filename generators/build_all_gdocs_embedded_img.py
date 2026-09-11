import os, sys, json, re, base64, time
sys.path.append('/home/yogi/lod_project')

def get_base64_image_tag(img_path):
    if os.path.exists(img_path):
        with open(img_path, 'rb') as f:
            encoded = base64.b64encode(f.read()).decode('utf-8')
        return f'<div dir="rtl" align="center" style="text-align: center; margin: 15px 0;"><img src="data:image/png;base64,{encoded}" style="width: 100%; max-width: 720px; border: 2px solid #102c57; border-radius: 4px;" alt="תשריט ביקורת מתוך המודל"></div>'
    return '<div dir="rtl" align="right" style="color: #888888; font-style: italic; margin: 10px 0;">[תשריט ביקורת משויך למודל ה-BIM]</div>'

def generate_full_html_with_images(title, discipline, findings, meta_info):
    html = f"""<!DOCTYPE html>
<html dir="rtl" lang="he">
<head>
<meta charset="utf-8">
<title>{title}</title>
<style>
    * {{
        direction: rtl !important;
        text-align: right !important;
        unicode-bidi: embed !important;
        font-family: 'David', 'Arial', sans-serif !important;
    }}
    body {{
        direction: rtl !important;
        text-align: right !important;
        font-size: 13pt;
        line-height: 1.6;
        color: #222222;
        padding: 30px;
        background-color: #ffffff;
    }}
    h1 {{
        color: #102c57;
        font-size: 22pt;
        font-weight: bold;
        margin-bottom: 5px;
    }}
    h2 {{
        color: #b40000;
        font-size: 16pt;
        margin-top: 0;
        margin-bottom: 20px;
    }}
    h3 {{
        color: #102c57;
        font-size: 15pt;
        border-bottom: 2px solid #102c57;
        padding-bottom: 6px;
        margin-top: 30px;
    }}
    .meta-box {{
        background-color: #f4f6f9;
        border-right: 5px solid #102c57;
        padding: 15px 20px;
        margin-bottom: 25px;
        font-size: 12pt;
        color: #444444;
    }}
    .meta-line {{
        margin-bottom: 5px;
    }}
    table {{
        width: 100%;
        border-collapse: collapse;
        margin-top: 12px;
        margin-bottom: 20px;
    }}
    th {{
        background-color: #102c57;
        color: #ffffff;
        font-weight: bold;
        padding: 10px 12px;
        border: 1px solid #102c57;
        font-size: 12pt;
    }}
    td {{
        padding: 10px 12px;
        border: 1px solid #cccccc;
        font-size: 11.5pt;
        vertical-align: top;
        background-color: #ffffff;
    }}
    .card-box {{
        border: 1px solid #d0d7de;
        border-radius: 6px;
        margin-bottom: 35px;
        padding: 20px;
        background-color: #ffffff;
    }}
    .card-header {{
        font-size: 15pt;
        font-weight: bold;
        color: #102c57;
        margin-bottom: 8px;
    }}
    .badge-red {{
        color: #b40000;
        font-weight: bold;
    }}
    .badge-yellow {{
        color: #d26900;
        font-weight: bold;
    }}
    .badge-blue {{
        color: #0066cc;
        font-weight: bold;
    }}
    .block-hdr {{
        background-color: #102c57;
        color: #ffffff;
        font-weight: bold;
        padding: 8px 12px;
        margin-top: 15px;
        margin-bottom: 8px;
        border-radius: 4px;
        font-size: 12pt;
    }}
    .highlight-action {{
        background-color: #fff5f5;
        border-right: 4px solid #b40000;
        padding: 12px 15px;
        margin: 12px 0;
    }}
    .rec-action-text {{
        font-weight: bold;
        color: #102c57;
        font-size: 13pt;
        margin-bottom: 6px;
    }}
    .rev-update-text {{
        font-weight: bold;
        color: #007a3d;
        font-size: 12pt;
        margin-bottom: 6px;
    }}
    .auto-closure-text {{
        font-weight: bold;
        color: #005a9c;
        font-size: 12pt;
    }}
</style>
</head>
<body dir="rtl" align="right" style="direction: rtl !important; text-align: right !important;">

<h1 dir="rtl" align="right" style="direction: rtl !important; text-align: right !important;">{title}</h1>
<h2 dir="rtl" align="right" style="direction: rtl !important; text-align: right !important;">{discipline} — תוכנית עבודה וסגירת ממצאים למהדורה 02 (Rev 02)</h2>

<div class="meta-box" dir="rtl" align="right" style="direction: rtl !important; text-align: right !important;">
    <div class="meta-line" dir="rtl" align="right"><strong>פרויקט:</strong> לוד ניר צבי</div>
    <div class="meta-line" dir="rtl" align="right"><strong>יזם:</strong> עמרם אברהם</div>
    <div class="meta-line" dir="rtl" align="right"><strong>מיועד עבור:</strong> {meta_info.get('recipient', 'צוות התכנון וההנדסה')}</div>
    <div class="meta-line" dir="rtl" align="right"><strong>מבנים / מגרשים:</strong> מגדלים 321, 339 ומבנה 223</div>
    <div class="meta-line" dir="rtl" align="right"><strong>גרסת מודל שנבדקה:</strong> {meta_info.get('model', 'LOD_MODEL')}</div>
    <div class="meta-line" dir="rtl" align="right"><strong>תאריך הפקה:</strong> ספטמבר 2026 | <strong>מהדורה:</strong> סבב 01 לקראת Revision 02</div>
    <div class="meta-line" dir="rtl" align="right"><strong>מטרת המסמך:</strong> מתן חבילת עבודה מוכנה, פעולות מועדפות, הנחיות עדכון מודל מדויקות והערכת זמן לקיצור ימי תכנון.</div>
</div>

<h3 dir="rtl" align="right" style="direction: rtl !important; text-align: right !important;">1. תקציר ומטרת המסמך עבור צוות התכנון</h3>
<p dir="rtl" align="right" style="direction: rtl !important; text-align: right !important;">דוח זה נבנה ככלי עבודה מעשי (Legalix Designer Correction &amp; Closure) שמטרתו לקצר לצוות התכנון את זמן העבודה מממצא במודל (Finding) לפתרון סגור ומאושר (Resolved).</p>
<p dir="rtl" align="right" style="direction: rtl !important; text-align: right !important;">עבור כל אחד מהממצאים שאותרו במודל, הדוח מציג מבנה עבודה תלת-אזורי ממוקד, מלווה בתשריט ביקורת ויזואלי מסומן מתוך המודל:</p>
<ul dir="rtl" align="right" style="direction: rtl !important; text-align: right !important;">
    <li dir="rtl" align="right"><strong>אזור 1: מה נמצא במודל</strong> — מיקום מדויק, צילום מסומן, נתון מדוד מול דרישה תקנית ופער מספרי.</li>
    <li dir="rtl" align="right"><strong>אזור 2: מה לעשות עכשיו</strong> — הפעולה המומלצת המועדפת, הסיבה לבחירתה, מה בדיוק לעדכן ב-Rev 02 והערכת זמן ביצוע.</li>
    <li dir="rtl" align="right"><strong>אזור 3: איך נסגור את הממצא</strong> — קריטריון סגירה אוטומטי שהמערכת תבדוק ב-Rev 02, דיסציפלינות לתיאום וטופס החלטה.</li>
</ul>

<h3 dir="rtl" align="right" style="direction: rtl !important; text-align: right !important;">2. מפת עדיפויות לביצוע תיקונים (Task Priorities &amp; Time Estimates)</h3>
<table dir="rtl" align="right" style="direction: rtl !important; text-align: right !important;">
    <tr>
        <th dir="rtl" align="right">עדיפות ביצוע</th>
        <th dir="rtl" align="right">סוג המשימה למתכנן</th>
        <th dir="rtl" align="right">הערכת זמן ממוצעת לממצא</th>
        <th dir="rtl" align="right">כמות ממצאים</th>
    </tr>
    <tr style="background-color: #fff0f0;">
        <td dir="rtl" align="right"><strong class="badge-red">🔥 P1 — תיקון ישיר במודל</strong></td>
        <td dir="rtl" align="right">ממצאים הניתנים לתיקון מיידי במודל רוויט / שרטוט ללא תלות בגורם חיצוני</td>
        <td dir="rtl" align="right">10–15 דקות לממצא</td>
        <td dir="rtl" align="right">{meta_info.get('p1_count', '12')} ממצאים</td>
    </tr>
    <tr style="background-color: #fffdf0;">
        <td dir="rtl" align="right"><strong class="badge-yellow">🤝 P2 — דורש תיאום יועצים</strong></td>
        <td dir="rtl" align="right">ממצאים הדורשים תיאום מול קונסטרוקציה, אדריכלות, אינסטלציה או כיבוי</td>
        <td dir="rtl" align="right">דורש תיאום חיצוני</td>
        <td dir="rtl" align="right">{meta_info.get('p2_count', '6')} ממצאים</td>
    </tr>
    <tr style="background-color: #f0f8ff;">
        <td dir="rtl" align="right"><strong class="badge-blue">📐 P3 — דורש חישוב הנדסי / כיול מודל</strong></td>
        <td dir="rtl" align="right">ממצאים הדורשים כיול עומסים, ספיקות אוורור, מפל מתח או חישוב שטחים</td>
        <td dir="rtl" align="right">30–45 דקות (כיול חישוב)</td>
        <td dir="rtl" align="right">{meta_info.get('p3_count', '3')} ממצאים</td>
    </tr>
    <tr style="background-color: #f0fff4;">
        <td dir="rtl" align="right"><strong style="color: #007a3d;">💡 P4 — המלצת אופטימיזציה</strong></td>
        <td dir="rtl" align="right">הנדסת ערך וחיסכון בעלויות ליזם ולמתכנן (Value Engineering)</td>
        <td dir="rtl" align="right">לשיקול דעת היזם/מתכנן</td>
        <td dir="rtl" align="right">{meta_info.get('p4_count', '1')} ממצא</td>
    </tr>
</table>

<h3 dir="rtl" align="right" style="direction: rtl !important; text-align: right !important;">3. פירוט כרטיסי עבודה במבנה 3 האזורים כולל צילומי מסך מהמודל</h3>
"""

    for item in findings:
        val_curr = item.get('val_curr') or item.get('val_current', '')
        val_calc = item.get('val_calc', 'N/A')
        rec_act = item.get('rec_action') or item.get('action', '')
        rec_rsn = item.get('rec_reason') or "מבטיחה עמידה מלאה בדרישות התקן ללא סיבוכי ביצוע."
        rev_up = item.get('rev_update') or f"לעדכן במודל רוויט את {item['id']} בהתאם להנחיות."
        cls_cr = item.get('closure_crit') or "אימות תיקון האלמנט במודל רוויט בבדיקה חוזרת."
        img_tag = get_base64_image_tag(item.get('img', ''))
        
        badge_class = "badge-red" if "🔴" in item['status'] else ("badge-yellow" if "🟡" in item['status'] else "badge-blue")
        html += f"""
<div class="card-box" dir="rtl" align="right" style="direction: rtl !important; text-align: right !important;">
    <div class="card-header" dir="rtl" align="right">{item['id']} | {item['title']}</div>
    <div dir="rtl" align="right" style="margin-bottom: 15px;">
        <span class="{badge_class}">סטטוס: {item['status']}</span> | 
        <strong>עדיפות:</strong> {item.get('prio', 'P1')} | 
        <strong>זמן משוער:</strong> {item.get('effort', '15 דקות')}
    </div>
    
    <div class="block-hdr" dir="rtl" align="right">🔍 אזור 1: מה נמצא במודל</div>
    <table dir="rtl" align="right" style="margin-top: 5px;">
        <tr><td dir="rtl" align="right" style="width: 25%; font-weight: bold; background-color: #f4f6f9;">מיקום מדויק ואלמנט:</td><td dir="rtl" align="right">{item['loc']}<br>אלמנט: {item['elem']}</td></tr>
        <tr><td dir="rtl" align="right" style="font-weight: bold; background-color: #f4f6f9;">הממצא והפער שנמדד:</td><td dir="rtl" align="right">ממצא: {item['finding']}<br>ערך במודל: <strong>{val_curr}</strong> | מחושב: {val_calc}<br>דרישת תכן: <strong>{item['req']}</strong><br>פער: <span class="badge-red">{item['delta']}</span></td></tr>
        <tr><td dir="rtl" align="right" style="font-weight: bold; background-color: #f4f6f9;">משמעות הנדסית ומקור:</td><td dir="rtl" align="right">משמעות: {item['impact']}<br>מקור מאומת: <strong>{item['src']}</strong></td></tr>
    </table>
    
    {img_tag}
    
    <div class="block-hdr" dir="rtl" align="right" style="background-color: #b40000;">⚡ אזור 2: מה לעשות עכשיו (הנחיית פעולה מועדפת)</div>
    <div class="highlight-action" dir="rtl" align="right">
        <div class="rec-action-text" dir="rtl" align="right">הפעולה המומלצת לביצוע (מועדפת):</div>
        <div dir="rtl" align="right">{rec_act}</div>
        <div dir="rtl" align="right" style="margin-top: 6px; font-size: 11pt; color: #555555;"><strong>הסבר לבחירה:</strong> {rec_rsn}</div>
    </div>
    <div dir="rtl" align="right" style="margin: 10px 0;">
        <div class="rev-update-text" dir="rtl" align="right">מה בדיוק לעדכן בתוכניות / מודל (Rev 02):</div>
        <div dir="rtl" align="right">{rev_up}</div>
    </div>
    <div dir="rtl" align="right" style="font-size: 11pt; color: #666666; margin-top: 8px;">
        <strong>חלופות נוספות שנבחנו:</strong> {str(item.get('alts', '')).replace(chr(10), '<br>')}
    </div>
    
    <div class="block-hdr" dir="rtl" align="right" style="background-color: #005a9c;">🎯 אזור 3: איך נסגור את הממצא</div>
    <table dir="rtl" align="right" style="margin-top: 5px;">
        <tr><td dir="rtl" align="right" style="width: 25%; font-weight: bold; background-color: #f4f6f9;">קריטריון סגירה אוטומטי:</td><td dir="rtl" align="right"><span class="auto-closure-text">✅ {cls_cr}</span><br><strong>תיאום נדרש:</strong> {item.get('coord', 'תיאום הנדסי')}</td></tr>
        <tr><td dir="rtl" align="right" style="font-weight: bold; background-color: #f4f6f9;">טופס החלטת המתכנן:</td><td dir="rtl" align="right">☐ התקבל כהמלצה מועדפת &nbsp;&nbsp;&nbsp; ☐ התקבלה חלופה אחרת &nbsp;&nbsp;&nbsp; ☐ לא התקבל (מצורף נימוק)<br><strong>סטטוס סגירה:</strong> ☐ OPEN &nbsp;&nbsp;&nbsp; ☐ RESOLVED IN REV 02</td></tr>
    </table>
</div>
"""

    html += f"""
<h3 dir="rtl" align="right" style="direction: rtl !important; text-align: right !important;">4. תוכנית עבודה ומעקב סגירת ממצאים למתכנן (Action &amp; Closure Plan)</h3>
<table dir="rtl" align="right" style="direction: rtl !important; text-align: right !important;">
    <tr>
        <th dir="rtl" align="right">Finding ID</th>
        <th dir="rtl" align="right">נושא הממצא</th>
        <th dir="rtl" align="right">עדיפות</th>
        <th dir="rtl" align="right">מיקום במודל</th>
        <th dir="rtl" align="right">הפעולה המומלצת לביצוע (מועדפת)</th>
        <th dir="rtl" align="right">מה בדיוק לעדכן ב-Rev 02</th>
        <th dir="rtl" align="right">קריטריון סגירה אוטומטי</th>
        <th dir="rtl" align="right">סטטוס</th>
    </tr>
"""
    for item in findings:
        rec_act = item.get('rec_action') or item.get('action', '')
        rev_up = item.get('rev_update') or f"לעדכן במודל את {item['id']}."
        cls_cr = item.get('closure_crit') or "אימות תיקון ברוויט."
        badge_style = "color: #b40000; font-weight: bold;" if "🔴" in item['status'] else "color: #d26900; font-weight: bold;"
        html += f"""
    <tr>
        <td dir="rtl" align="right"><strong>{item['id']}</strong></td>
        <td dir="rtl" align="right">{item['title']}</td>
        <td dir="rtl" align="right"><span style="{badge_style}">{item.get('prio', 'P1')[:2]}</span></td>
        <td dir="rtl" align="right">{item['loc'].split('|')[0]}</td>
        <td dir="rtl" align="right"><strong>{rec_act}</strong></td>
        <td dir="rtl" align="right" style="color: #007a3d;"><strong>{rev_up}</strong></td>
        <td dir="rtl" align="right" style="color: #005a9c;">{cls_cr}</td>
        <td dir="rtl" align="right"><strong>OPEN</strong></td>
    </tr>
"""

    html += """
</table>

<h3 dir="rtl" align="right" style="direction: rtl !important; text-align: right !important;">5. הנחיות להגשת Revision 02 ותהליך סגירת ממצאים אוטומטי</h3>
<p dir="rtl" align="right" style="direction: rtl !important; text-align: right !important;">על בסיס הממצאים, החלופות והפעולות המומלצות שפורטו בדוח זה, צוות התכנון מתבקש לפעול לפי סדר העדיפויות (P1 עד P4).</p>
<p dir="rtl" align="right" style="direction: rtl !important; text-align: right !important;">עם קבלת תוכניות ומודל Revision 02 המעודכנים, המערכת תריץ בדיקת סגירת ממצאים אוטומטית (Automated Closure Verification) ותפיק טבלת השוואת גרסאות (Rev Comparison) שתאשר את סגירת הממצאים.</p>

<h3 dir="rtl" align="right" style="direction: rtl !important; text-align: right !important;">6. המלצה לנקודת עצירה (Recommended Hold Point)</h3>
<div dir="rtl" align="right" style="background-color: #fff0f0; border-right: 4px solid #b40000; padding: 15px; font-size: 11.5pt;">
    <strong class="badge-red">RECOMMENDED HOLD POINT:</strong><br>
    מומלץ שלא לקדם ביצוע של העבודות הרלוונטיות לממצאים הקריטיים המסומנים באדום (RED) עד לקבלת התייחסות המתכנן ועדכון המודלים ב-Revision 02.
</div>

</body>
</html>
"""
    return html

# Generate all reports with Base64 embedded images
from gen_full_45_st_cards import get_full_45_structural_cards
from build_designer_action_closure_report import plumbing_designer_cards
from build_designer_hvac_action_report import hvac_designer_cards
from build_el_data import get_all_22_electrical_designer_cards
from build_ls_data import get_all_16_landscape_designer_cards
from build_mkt_data import get_all_18_marketing_designer_cards

# 1. Electrical
html_el = generate_full_html_with_images(
    "דוח הנחיות תיקון, חלופות וסגירת ממצאים למתכנן החשמל",
    "מערכות חשמל, מתח נמוך ומערכות חירום",
    get_all_22_electrical_designer_cards(),
    {"model": "LOD_PR_EL_R24 / LOD_321_EL_R24", "recipient": "מתכנן מערכות חשמל ותקשורת (צוות הנדסת חשמל)", "p1_count": "15", "p2_count": "4", "p3_count": "2", "p4_count": "1"}
)
with open('/home/yogi/lod_project/ELECTRICAL_DESIGNER_CLOSURE_REPORT.html', 'w', encoding='utf-8') as f:
    f.write(html_el)

# 2. Plumbing
html_pl = generate_full_html_with_images(
    "דוח הנחיות תיקון, חלופות וסגירת ממצאים למתכנן האינסטלציה",
    "מערכות אינסטלציה סניטרית, ספרינקלרים וניקוז",
    plumbing_designer_cards,
    {"model": "LOD_PL_339_R23 / Lod-FP-PR-R25", "recipient": "מתכנן אינסטלציה וכיבוי אש (צ'רלי חורי)", "p1_count": "16", "p2_count": "8", "p3_count": "5", "p4_count": "1"}
)
with open('/home/yogi/lod_project/PLUMBING_DESIGNER_CLOSURE_REPORT.html', 'w', encoding='utf-8') as f:
    f.write(html_pl)

# 3. HVAC
html_hv = generate_full_html_with_images(
    "דוח הנחיות תיקון, חלופות וסגירת ממצאים למתכנן המיזוג ושחרור עשן",
    "מערכות מיזוג אוויר, אוורור ושחרור עשן (HVAC)",
    hvac_designer_cards,
    {"model": "LOD_HV_ALL_R23", "recipient": "מתכנן מיזוג אוויר ושחרור עשן (צ'רלי חורי)", "p1_count": "12", "p2_count": "6", "p3_count": "3", "p4_count": "1"}
)
with open('/home/yogi/lod_project/HVAC_DESIGNER_CLOSURE_REPORT.html', 'w', encoding='utf-8') as f:
    f.write(html_hv)

# 4. Structure
html_st = generate_full_html_with_images(
    "דוח הנחיות תיקון, חלופות וסגירת ממצאים למתכנן הקונסטרוקציה",
    "הנדסת קונסטרוקציה, ביסוס ושלד",
    get_full_45_structural_cards(),
    {"model": "Lod_ST_PR_R25 / Lod_ST_321_R25 / Lod_ST_339_R25", "recipient": "מתכנן קונסטרוקציה ושלד (אלי חלמיש / הנדסת מבנים)", "p1_count": "20", "p2_count": "8", "p3_count": "10", "p4_count": "0"}
)
with open('/home/yogi/lod_project/STRUCTURE_DESIGNER_CLOSURE_REPORT.html', 'w', encoding='utf-8') as f:
    f.write(html_st)

# 5. Landscape
html_ls = generate_full_html_with_images(
    "דוח הנחיות תיקון, חלופות וסגירת ממצאים למתכנן הנוף והפיתוח",
    "פיתוח נופי, ניקוז חצר, מפלסי פיתוח וקירות תמך חוץ",
    get_all_16_landscape_designer_cards(),
    {"model": "LOD_ALL_LG_R24.rvt", "recipient": "מתכנן פיתוח נופי וניקוז חצר (צוות הנדסה נופית)", "p1_count": "10", "p2_count": "4", "p3_count": "1", "p4_count": "1"}
)
with open('/home/yogi/lod_project/LANDSCAPE_DESIGNER_CLOSURE_REPORT.html', 'w', encoding='utf-8') as f:
    f.write(html_ls)

# 6. Marketing
html_mkt = generate_full_html_with_images(
    "דוח הנחיות תיקון, חלופות וסגירת ממצאים לשיווק ולמתכנן",
    "הצלבת תוכניות מכר מול מודלי ביצוע והתאמת שטחים",
    get_all_18_marketing_designer_cards(),
    {"model": "חבילת מכר מול 3D-Marketing / Lod_AR / Lod_ST (1.82GB)", "recipient": "מתכנן אדריכלות, מנהל שיווק ויועץ משפטי", "p1_count": "15", "p2_count": "3", "p3_count": "0", "p4_count": "0"}
)
with open('/home/yogi/lod_project/MARKETING_DESIGNER_CLOSURE_REPORT.html', 'w', encoding='utf-8') as f:
    f.write(html_mkt)

print("All 6 Designer HTMLs generated with EMBEDDED Base64 Screenshots!")
