import json, os, sys
sys.path.append('/home/yogi/lod_project')

def generate_html_report_for_gdocs(title, discipline, findings, meta_info):
    html = f"""<!DOCTYPE html>
<html dir="rtl" lang="he">
<head>
<meta charset="utf-8">
<title>{title}</title>
<style>
    body {{
        direction: rtl;
        text-align: right;
        font-family: 'David', 'Arial', 'Segoe UI', sans-serif;
        font-size: 14pt;
        line-height: 1.5;
        color: #222222;
        padding: 40px;
        background-color: #ffffff;
    }}
    h1 {{
        color: #102c57;
        font-size: 24pt;
        font-weight: bold;
        margin-bottom: 5px;
        direction: rtl;
        text-align: right;
    }}
    h2 {{
        color: #b40000;
        font-size: 18pt;
        margin-top: 0;
        margin-bottom: 25px;
        direction: rtl;
        text-align: right;
    }}
    h3 {{
        color: #102c57;
        font-size: 16pt;
        border-bottom: 2px solid #102c57;
        padding-bottom: 6px;
        margin-top: 35px;
        direction: rtl;
        text-align: right;
    }}
    .meta-box {{
        background-color: #f4f6f9;
        border-right: 5px solid #102c57;
        padding: 15px 20px;
        margin-bottom: 30px;
        font-size: 12pt;
        color: #444444;
        direction: rtl;
        text-align: right;
    }}
    .meta-line {{
        margin-bottom: 6px;
    }}
    table {{
        direction: rtl;
        width: 100%;
        border-collapse: collapse;
        margin-top: 15px;
        margin-bottom: 25px;
    }}
    th {{
        background-color: #102c57;
        color: #ffffff;
        font-weight: bold;
        padding: 10px 12px;
        border: 1px solid #102c57;
        text-align: right;
        font-size: 12pt;
    }}
    td {{
        padding: 10px 12px;
        border: 1px solid #cccccc;
        text-align: right;
        font-size: 11.5pt;
        vertical-align: top;
    }}
    .card-box {{
        border: 1px solid #d0d7de;
        border-radius: 6px;
        margin-bottom: 35px;
        padding: 20px;
        background-color: #ffffff;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        direction: rtl;
        text-align: right;
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
<body>

<h1>{title}</h1>
<h2>{discipline} — תוכנית עבודה וסגירת ממצאים למהדורה 02 (Rev 02)</h2>

<div class="meta-box">
    <div class="meta-line"><strong>פרויקט:</strong> לוד ניר צבי</div>
    <div class="meta-line"><strong>יזם:</strong> עמרם אברהם</div>
    <div class="meta-line"><strong>מיועד עבור:</strong> מתכנן המערכות (צ'רלי חורי / צוות תכנון)</div>
    <div class="meta-line"><strong>מבנים / מגרשים:</strong> מגדלים 321, 339 ומבנה 223</div>
    <div class="meta-line"><strong>גרסת מודל שנבדקה:</strong> {meta_info.get('model', 'LOD_MODEL')}</div>
    <div class="meta-line"><strong>תאריך הפקה:</strong> ספטמבר 2026 | <strong>מהדורה:</strong> סבב 01 לקראת Revision 02</div>
    <div class="meta-line"><strong>מטרת המסמך:</strong> מתן חבילת עבודה מוכנה, פעולות מועדפות, הנחיות עדכון מודל מדויקות והערכת זמן לקיצור ימי תכנון.</div>
</div>

<h3>1. תקציר ומטרת המסמך עבור צוות התכנון</h3>
<p>דוח זה נבנה ככלי עבודה מעשי (Legalix Designer Correction &amp; Closure) שמטרתו לקצר לצוות התכנון את זמן העבודה מממצא במודל (Finding) לפתרון סגור ומאושר (Resolved).</p>
<p>עבור כל אחד מהממצאים שאותרו במודל, הדוח מציג מבנה עבודה תלת-אזורי ממוקד:</p>
<ul>
    <li><strong>אזור 1: מה נמצא במודל</strong> — מיקום מדויק, צילום מסומן, נתון מדוד מול דרישה תקנית ופער מספרי.</li>
    <li><strong>אזור 2: מה לעשות עכשיו</strong> — הפעולה המומלצת המועדפת, הסיבה לבחירתה, מה בדיוק לעדכן ב-Rev 02 והערכת זמן ביצוע.</li>
    <li><strong>אזור 3: איך נסגור את הממצא</strong> — קריטריון סגירה אוטומטי שהמערכת תבדוק ב-Rev 02, דיסציפלינות לתיאום וטופס החלטה.</li>
</ul>

<h3>2. מפת עדיפויות לביצוע תיקונים (Task Priorities &amp; Time Estimates)</h3>
<table>
    <tr>
        <th>עדיפות ביצוע</th>
        <th>סוג המשימה למתכנן</th>
        <th>הערכת זמן ממוצעת לממצא</th>
        <th>כמות ממצאים</th>
    </tr>
    <tr style="background-color: #fff0f0;">
        <td><strong class="badge-red">🔥 P1 — תיקון ישיר במודל</strong></td>
        <td>ממצאים הניתנים לתיקון מיידי במודל רוויט ללא תלות בגורם חיצוני</td>
        <td>10–15 דקות לממצא</td>
        <td>{meta_info.get('p1_count', '12')} ממצאים</td>
    </tr>
    <tr style="background-color: #fffdf0;">
        <td><strong class="badge-yellow">🤝 P2 — דורש תיאום יועצים</strong></td>
        <td>ממצאים הדורשים תיאום מול קונסטרוקציה, אדריכלות או כיבוי</td>
        <td>דורש תיאום חיצוני</td>
        <td>{meta_info.get('p2_count', '6')} ממצאים</td>
    </tr>
    <tr style="background-color: #f0f8ff;">
        <td><strong class="badge-blue">📐 P3 — דורש חישוב תרמי / הידראולי</strong></td>
        <td>ממצאים הדורשים כיול עומסים, ספיקות אוורור או לחצים</td>
        <td>30–45 דקות (כיול חישוב)</td>
        <td>{meta_info.get('p3_count', '3')} ממצאים</td>
    </tr>
    <tr style="background-color: #f0fff4;">
        <td><strong style="color: #007a3d;">💡 P4 — המלצת אופטימיזציה</strong></td>
        <td>הנדסת ערך וחיסכון בעלויות ליזם ולמתכנן (Value Engineering)</td>
        <td>לשיקול דעת היזם/מתכנן</td>
        <td>{meta_info.get('p4_count', '1')} ממצא</td>
    </tr>
</table>

<h3>3. פירוט כרטיסי עבודה במבנה 3 האזורים למתכנן</h3>
"""

    for item in findings:
        val_curr = item.get('val_curr') or item.get('val_current', '')
        val_calc = item.get('val_calc', 'N/A')
        rec_act = item.get('rec_action') or item.get('action', '')
        rec_rsn = item.get('rec_reason') or "מבטיחה עמידה מלאה בדרישות התקן ללא סיבוכי ביצוע."
        rev_up = item.get('rev_update') or f"לעדכן במודל רוויט את {item['id']} בהתאם להנחיות."
        cls_cr = item.get('closure_crit') or "אימות תיקון האלמנט במודל רוויט בבדיקה חוזרת."
        
        badge_class = "badge-red" if "🔴" in item['status'] else ("badge-yellow" if "🟡" in item['status'] else "badge-blue")
        html += f"""
<div class="card-box">
    <div class="card-header">{item['id']} | {item['title']}</div>
    <div style="margin-bottom: 15px;">
        <span class="{badge_class}">סטטוס: {item['status']}</span> | 
        <strong>עדיפות:</strong> {item.get('prio', 'P1')} | 
        <strong>זמן משוער:</strong> {item.get('effort', '15 דקות')}
    </div>
    
    <div class="block-hdr">🔍 אזור 1: מה נמצא במודל</div>
    <table style="margin-top: 5px;">
        <tr><td style="width: 25%; font-weight: bold; background-color: #f4f6f9;">מיקום מדויק ואלמנט:</td><td>{item['loc']}<br>אלמנט: {item['elem']}</td></tr>
        <tr><td style="font-weight: bold; background-color: #f4f6f9;">הממצא והפער שנמדד:</td><td>ממצא: {item['finding']}<br>ערך במודל: <strong>{val_curr}</strong> | מחושב: {val_calc}<br>דרישת תכן: <strong>{item['req']}</strong><br>פער: <span class="badge-red">{item['delta']}</span></td></tr>
        <tr><td style="font-weight: bold; background-color: #f4f6f9;">משמעות הנדסית ומקור:</td><td>משמעות: {item['impact']}<br>מקור מאומת: <strong>{item['src']}</strong></td></tr>
    </table>
    
    <div class="block-hdr" style="background-color: #b40000;">⚡ אזור 2: מה לעשות עכשיו (הנחיית פעולה מועדפת)</div>
    <div class="highlight-action">
        <div class="rec-action-text">הפעולה המומלצת לביצוע (מועדפת):</div>
        <div>{rec_act}</div>
        <div style="margin-top: 6px; font-size: 11pt; color: #555555;"><strong>הסבר לבחירה:</strong> {rec_rsn}</div>
    </div>
    <div style="margin: 10px 0;">
        <div class="rev-update-text">מה בדיוק לעדכן בתוכניות / מודל (Rev 02):</div>
        <div>{rev_up}</div>
    </div>
    <div style="font-size: 11pt; color: #666666; margin-top: 8px;">
        <strong>חלופות נוספות שנבחנו:</strong> {str(item.get('alts', '')).replace(chr(10), '<br>')}
    </div>
    
    <div class="block-hdr" style="background-color: #005a9c;">🎯 אזור 3: איך נסגור את הממצא</div>
    <table style="margin-top: 5px;">
        <tr><td style="width: 25%; font-weight: bold; background-color: #f4f6f9;">קריטריון סגירה אוטומטי:</td><td><span class="auto-closure-text">✅ {cls_cr}</span><br><strong>תיאום נדרש:</strong> {item.get('coord', 'אינסטלציה')}</td></tr>
        <tr><td style="font-weight: bold; background-color: #f4f6f9;">טופס החלטת המתכנן:</td><td>☐ התקבל כהמלצה מועדפת &nbsp;&nbsp;&nbsp; ☐ התקבלה חלופה אחרת &nbsp;&nbsp;&nbsp; ☐ לא התקבל (מצורף נימוק)<br><strong>סטטוס סגירה:</strong> ☐ OPEN &nbsp;&nbsp;&nbsp; ☐ RESOLVED IN REV 02</td></tr>
    </table>
</div>
"""

    html += f"""
<h3>4. תוכנית עבודה ומעקב סגירת ממצאים למתכנן (Action &amp; Closure Plan)</h3>
<table>
    <tr>
        <th>Finding ID</th>
        <th>נושא הממצא</th>
        <th>עדיפות</th>
        <th>מיקום במודל</th>
        <th>הפעולה המומלצת לביצוע (מועדפת)</th>
        <th>מה בדיוק לעדכן ב-Rev 02</th>
        <th>קריטריון סגירה אוטומטי</th>
        <th>סטטוס</th>
    </tr>
"""
    for item in findings:
        rec_act = item.get('rec_action') or item.get('action', '')
        rev_up = item.get('rev_update') or f"לעדכן במודל את {item['id']}."
        cls_cr = item.get('closure_crit') or "אימות תיקון ברוויט."
        badge_style = "color: #b40000; font-weight: bold;" if "🔴" in item['status'] else "color: #d26900; font-weight: bold;"
        html += f"""
    <tr>
        <td><strong>{item['id']}</strong></td>
        <td>{item['title']}</td>
        <td><span style="{badge_style}">{item.get('prio', 'P1')[:2]}</span></td>
        <td>{item['loc'].split('|')[0]}</td>
        <td><strong>{rec_act}</strong></td>
        <td style="color: #007a3d;"><strong>{rev_up}</strong></td>
        <td style="color: #005a9c;">{cls_cr}</td>
        <td><strong>OPEN</strong></td>
    </tr>
"""

    html += """
</table>

<h3>5. הנחיות להגשת Revision 02 ותהליך סגירת ממצאים אוטומטי</h3>
<p>על בסיס הממצאים, החלופות והפעולות המומלצות שפורטו בדוח זה, צוות התכנון מתבקש לפעול לפי סדר העדיפויות (P1 עד P4).</p>
<p>עם קבלת תוכניות ומודל Revision 02 המעודכנים, המערכת תריץ בדיקת סגירת ממצאים אוטומטית (Automated Closure Verification) ותפיק טבלת השוואת גרסאות (Rev Comparison) שתאשר את סגירת הממצאים.</p>

<h3>6. המלצה לנקודת עצירה (Recommended Hold Point)</h3>
<div style="background-color: #fff0f0; border-right: 4px solid #b40000; padding: 15px; font-size: 11.5pt;">
    <strong class="badge-red">RECOMMENDED HOLD POINT:</strong><br>
    מומלץ שלא לקדם ביצוע של העבודות הרלוונטיות לממצאים הקריטיים המסומנים באדום (RED) עד לקבלת התייחסות המתכנן ועדכון המודלים ב-Revision 02.
</div>

</body>
</html>
"""
    return html

# 1. Plumbing
from build_designer_action_closure_report import plumbing_designer_cards
html_pl = generate_html_report_for_gdocs(
    "דוח הנחיות תיקון, חלופות וסגירת ממצאים למתכנן האינסטלציה",
    "מערכות אינסטלציה סניטרית, ספרינקלרים וניקוז",
    plumbing_designer_cards,
    {"model": "LOD_PL_339_R23 / Lod-FP-PR-R25", "p1_count": "16", "p2_count": "8", "p3_count": "5", "p4_count": "1"}
)
with open('/home/yogi/lod_project/PLUMBING_DESIGNER_CLOSURE_REPORT.html', 'w', encoding='utf-8') as f:
    f.write(html_pl)

# 2. HVAC
from build_designer_hvac_action_report import hvac_designer_cards
html_hv = generate_html_report_for_gdocs(
    "דוח הנחיות תיקון, חלופות וסגירת ממצאים למתכנן המיזוג ושחרור עשן",
    "מערכות מיזוג אוויר, אוורור ושחרור עשן (HVAC)",
    hvac_designer_cards,
    {"model": "LOD_HV_ALL_R23", "p1_count": "12", "p2_count": "6", "p3_count": "3", "p4_count": "1"}
)
with open('/home/yogi/lod_project/HVAC_DESIGNER_CLOSURE_REPORT.html', 'w', encoding='utf-8') as f:
    f.write(html_hv)

# 3. Electrical
from build_el_data import get_all_22_electrical_designer_cards
html_el = generate_html_report_for_gdocs(
    "דוח הנחיות תיקון, חלופות וסגירת ממצאים למתכנן החשמל",
    "מערכות חשמל, מתח נמוך ומערכות חירום",
    get_all_22_electrical_designer_cards(),
    {"model": "LOD_PR_EL_R24 / LOD_321_EL_R24", "p1_count": "15", "p2_count": "4", "p3_count": "2", "p4_count": "1"}
)
with open('/home/yogi/lod_project/ELECTRICAL_DESIGNER_CLOSURE_REPORT.html', 'w', encoding='utf-8') as f:
    f.write(html_el)

# 4. Structure
from gen_full_45_st_cards import get_full_45_structural_cards
html_st = generate_html_report_for_gdocs(
    "דוח הנחיות תיקון, חלופות וסגירת ממצאים למתכנן הקונסטרוקציה",
    "הנדסת קונסטרוקציה, ביסוס ושלד",
    get_full_45_structural_cards(),
    {"model": "Lod_ST_PR_R25 / Lod_ST_321_R25 / Lod_ST_339_R25", "p1_count": "20", "p2_count": "8", "p3_count": "10", "p4_count": "0"}
)
with open('/home/yogi/lod_project/STRUCTURE_DESIGNER_CLOSURE_REPORT.html', 'w', encoding='utf-8') as f:
    f.write(html_st)

print("All 4 pure HTML reports for Google Docs generated successfully!")
