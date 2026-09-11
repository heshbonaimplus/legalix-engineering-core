import os, sys, json, re

# Let's generate clean, 100% valid HTML for Google Docs conversion with ZERO syntax errors
sys.path.append('/home/yogi/lod_project')
from build_el_data import get_all_22_electrical_designer_cards
from gen_full_45_st_cards import get_full_45_structural_cards

def create_clean_semantic_gdoc_html(title, subtitle, recipient, model_name, findings, p_counts):
    lines = []
    lines.append('<!DOCTYPE html>')
    lines.append('<html dir="rtl" lang="he">')
    lines.append('<head>')
    lines.append('<meta charset="utf-8">')
    lines.append(f'<title>{title}</title>')
    lines.append('<style>')
    lines.append('body { direction: rtl; text-align: right; font-family: Arial, sans-serif; font-size: 11pt; line-height: 1.5; color: #222222; }')
    lines.append('h1 { direction: rtl; text-align: right; color: #102C57; font-size: 18pt; font-weight: bold; margin-bottom: 4px; }')
    lines.append('h2 { direction: rtl; text-align: right; color: #B40000; font-size: 14pt; margin-top: 0; margin-bottom: 15px; }')
    lines.append('h3 { direction: rtl; text-align: right; color: #102C57; font-size: 13pt; margin-top: 25px; margin-bottom: 10px; border-bottom: 2px solid #102C57; padding-bottom: 4px; }')
    lines.append('p, div, li { direction: rtl; text-align: right; }')
    lines.append('table { direction: rtl; width: 100%; border-collapse: collapse; margin: 15px 0; }')
    lines.append('th { direction: rtl; text-align: right; background-color: #102C57; color: #ffffff; padding: 8px 10px; font-weight: bold; border: 1px solid #102C57; }')
    lines.append('td { direction: rtl; text-align: right; padding: 8px 10px; border: 1px solid #cccccc; vertical-align: top; }')
    lines.append('.meta-box { direction: rtl; text-align: right; background-color: #F4F6F9; border-right: 4px solid #102C57; padding: 12px 16px; margin-bottom: 20px; }')
    lines.append('.card { direction: rtl; text-align: right; border: 1px solid #D0D7DE; margin-bottom: 25px; padding: 15px; background-color: #FFFFFF; }')
    lines.append('.card-hdr { direction: rtl; text-align: right; font-size: 13pt; font-weight: bold; color: #102C57; margin-bottom: 6px; }')
    lines.append('.sec-hdr { direction: rtl; text-align: right; background-color: #102C57; color: #ffffff; padding: 6px 10px; font-weight: bold; margin-top: 10px; margin-bottom: 6px; }')
    lines.append('.action-box { direction: rtl; text-align: right; background-color: #FFF5F5; border-right: 4px solid #B40000; padding: 10px 12px; margin: 10px 0; }')
    lines.append('</style>')
    lines.append('</head>')
    lines.append('<body dir="rtl" align="right">')
    
    # Title
    lines.append(f'<h1 dir="rtl" align="right">{title}</h1>')
    lines.append(f'<h2 dir="rtl" align="right">{subtitle} — תוכנית עבודה ל-Rev 02</h2>')
    
    # Meta Box
    lines.append('<div class="meta-box" dir="rtl" align="right">')
    lines.append('<p dir="rtl" align="right"><strong>פרויקט:</strong> לוד ניר צבי &nbsp;|&nbsp; <strong>יזם:</strong> עמרם אברהם</p>')
    lines.append(f'<p dir="rtl" align="right"><strong>מיועד עבור:</strong> {recipient}</p>')
    lines.append('<p dir="rtl" align="right"><strong>מבנים / מגרשים:</strong> מגדלים 321, 339 ומבנה 223</p>')
    lines.append(f'<p dir="rtl" align="right"><strong>גרסת מודל שנבדקה:</strong> {model_name}</p>')
    lines.append('<p dir="rtl" align="right"><strong>מהדורה:</strong> סבב 01 לקראת Revision 02 &nbsp;|&nbsp; <strong>תאריך:</strong> ספטמבר 2026</p>')
    lines.append('</div>')
    
    # 1. תקציר
    lines.append('<h3 dir="rtl" align="right">1. תקציר ומטרת המסמך עבור צוות התכנון</h3>')
    lines.append('<p dir="rtl" align="right">דוח זה נבנה כחבילת עבודה מעשית (Designer Correction &amp; Closure) שמטרתה לקצר למתכנן את זמן העבודה מממצא במודל (Finding) לפתרון סגור ומאושר (Resolved).</p>')
    lines.append('<p dir="rtl" align="right">עבור כל אחד מהממצאים, הדוח מציג מבנה עבודה תלת-אזורי ממוקד:</p>')
    lines.append('<ul dir="rtl" align="right">')
    lines.append('<li dir="rtl" align="right"><strong>אזור 1: מה נמצא במודל</strong> — מיקום מדויק, נתון מדוד מול דרישה תקנית ופער מספרי.</li>')
    lines.append('<li dir="rtl" align="right"><strong>אזור 2: מה לעשות עכשיו</strong> — הפעולה המומלצת המועדפת, הסיבה לבחירתה ומה בדיוק לעדכן ב-Rev 02.</li>')
    lines.append('<li dir="rtl" align="right"><strong>אזור 3: איך נסגור את הממצא</strong> — קריטריון סגירה אוטומטי שהמערכת תבדוק ב-Rev 02 וטופס החלטה.</li>')
    lines.append('</ul>')
    
    # 2. מפת עדיפויות
    lines.append('<h3 dir="rtl" align="right">2. מפת עדיפויות לביצוע תיקונים (Task Priorities)</h3>')
    lines.append('<table dir="rtl" align="right">')
    lines.append('<tr><th dir="rtl" align="right">עדיפות</th><th dir="rtl" align="right">סוג המשימה למתכנן</th><th dir="rtl" align="right">זמן משוער</th><th dir="rtl" align="right">כמות ממצאים</th></tr>')
    lines.append(f'<tr style="background-color: #FFF0F0;"><td dir="rtl" align="right"><strong>🔥 P1</strong></td><td dir="rtl" align="right">תיקון ישיר במודל רוויט / שרטוט</td><td dir="rtl" align="right">10–15 דקות לממצא</td><td dir="rtl" align="right"><strong>{p_counts["p1"]} ממצאים</strong></td></tr>')
    lines.append(f'<tr style="background-color: #FFFDF0;"><td dir="rtl" align="right"><strong>🤝 P2</strong></td><td dir="rtl" align="right">דורש תיאום מול יועצים נוספים</td><td dir="rtl" align="right">תיאום חיצוני</td><td dir="rtl" align="right"><strong>{p_counts["p2"]} ממצאים</strong></td></tr>')
    lines.append(f'<tr style="background-color: #F0F8FF;"><td dir="rtl" align="right"><strong>📐 P3</strong></td><td dir="rtl" align="right">דורש כיול חישוב / הרצת מודל</td><td dir="rtl" align="right">30–45 דקות</td><td dir="rtl" align="right"><strong>{p_counts["p3"]} ממצאים</strong></td></tr>')
    lines.append(f'<tr style="background-color: #F0FFF4;"><td dir="rtl" align="right"><strong>💡 P4</strong></td><td dir="rtl" align="right">המלצת אופטימיזציה והנדסת ערך</td><td dir="rtl" align="right">לשיקול דעת</td><td dir="rtl" align="right"><strong>{p_counts["p4"]} ממצאים</strong></td></tr>')
    lines.append('</table>')
    
    # 3. כרטיסי עבודה
    lines.append('<h3 dir="rtl" align="right">3. פירוט כרטיסי עבודה למתכנן</h3>')
    for item in findings:
        val_curr = item.get('val_curr') or item.get('val_current', '')
        val_calc = item.get('val_calc', 'N/A')
        rec_act = item.get('rec_action') or item.get('action', '')
        rec_rsn = item.get('rec_reason', 'מבטיחה עמידה מלאה בדרישות התקן.')
        rev_up = item.get('rev_update', 'לעדכן במודל רוויט.')
        cls_cr = item.get('closure_crit', 'אימות בבדיקה חוזרת.')
        
        lines.append('<div class="card" dir="rtl" align="right">')
        lines.append(f'<div class="card-hdr" dir="rtl" align="right">{item["id"]} | {item["title"]}</div>')
        lines.append(f'<p dir="rtl" align="right"><strong>סטטוס:</strong> {item["status"]} &nbsp;|&nbsp; <strong>עדיפות:</strong> {item.get("prio", "P1")}</p>')
        
        # אזור 1
        lines.append('<div class="sec-hdr" dir="rtl" align="right">🔍 אזור 1: מה נמצא במודל</div>')
        lines.append('<table dir="rtl" align="right">')
        lines.append(f'<tr><td dir="rtl" align="right" style="width: 25%; font-weight: bold; background-color: #F4F6F9;">מיקום ואלמנט:</td><td dir="rtl" align="right">{item["loc"]}<br>אלמנט: {item["elem"]}</td></tr>')
        lines.append(f'<tr><td dir="rtl" align="right" style="font-weight: bold; background-color: #F4F6F9;">הממצא והפער:</td><td dir="rtl" align="right">ממצא: {item["finding"]}<br>ערך במודל: <strong>{val_curr}</strong> | מחושב: {val_calc}<br>דרישת תכן: <strong>{item["req"]}</strong><br>פער: <span style="color: #B40000; font-weight: bold;">{item["delta"]}</span></td></tr>')
        lines.append(f'<tr><td dir="rtl" align="right" style="font-weight: bold; background-color: #F4F6F9;">משמעות ומקור:</td><td dir="rtl" align="right">משמעות: {item["impact"]}<br>מקור מאומת: <strong>{item["src"]}</strong></td></tr>')
        lines.append('</table>')
        
        # אזור 2
        lines.append('<div class="sec-hdr" style="background-color: #B40000;" dir="rtl" align="right">⚡ אזור 2: מה לעשות עכשיו (הנחיית פעולה מועדפת)</div>')
        lines.append('<div class="action-box" dir="rtl" align="right">')
        lines.append(f'<p dir="rtl" align="right" style="font-size: 12pt; font-weight: bold; color: #102C57;">הפעולה המומלצת לביצוע (מועדפת):</p>')
        lines.append(f'<p dir="rtl" align="right">{rec_act}</p>')
        lines.append(f'<p dir="rtl" align="right" style="font-size: 10.5pt; color: #555555;"><strong>הסבר לבחירה:</strong> {rec_rsn}</p>')
        lines.append('</div>')
        lines.append(f'<p dir="rtl" align="right" style="color: #007A3D; font-weight: bold;">מה בדיוק לעדכן ב-Rev 02: {rev_up}</p>')
        lines.append(f'<p dir="rtl" align="right" style="font-size: 10.5pt; color: #666666;"><strong>חלופות נוספות:</strong> {str(item.get("alts", "")).replace(chr(10), "<br>")}</p>')
        
        # אזור 3
        lines.append('<div class="sec-hdr" style="background-color: #005A9C;" dir="rtl" align="right">🎯 אזור 3: איך נסגור את הממצא</div>')
        lines.append('<table dir="rtl" align="right">')
        lines.append(f'<tr><td dir="rtl" align="right" style="width: 25%; font-weight: bold; background-color: #F4F6F9;">קריטריון סגירה:</td><td dir="rtl" align="right" style="color: #005A9C; font-weight: bold;">✅ {cls_cr}<br><span style="color: #222222;">תיאום נדרש: {item.get("coord", "תיאום הנדסי")}</span></td></tr>')
        lines.append('<tr><td dir="rtl" align="right" style="font-weight: bold; background-color: #F4F6F9;">החלטת המתכנן:</td><td dir="rtl" align="right">☐ התקבל כהמלצה מועדפת &nbsp;&nbsp;&nbsp; ☐ התקבלה חלופה אחרת &nbsp;&nbsp;&nbsp; ☐ לא התקבל (מצורף נימוק)<br><strong>סטטוס:</strong> ☐ OPEN &nbsp;&nbsp;&nbsp; ☐ RESOLVED IN REV 02</td></tr>')
        lines.append('</table>')
        lines.append('</div>')
        
    # 4. טבלת מעקב
    lines.append('<h3 dir="rtl" align="right">4. תוכנית עבודה ומעקב סגירת ממצאים (Action Plan)</h3>')
    lines.append('<table dir="rtl" align="right">')
    lines.append('<tr><th dir="rtl" align="right">Finding ID</th><th dir="rtl" align="right">נושא הממצא</th><th dir="rtl" align="right">עדיפות</th><th dir="rtl" align="right">מיקום</th><th dir="rtl" align="right">הפעולה המומלצת לביצוע</th><th dir="rtl" align="right">מה לעדכן ב-Rev 02</th><th dir="rtl" align="right">קריטריון סגירה</th><th dir="rtl" align="right">סטטוס</th></tr>')
    for item in findings:
        rec_act = item.get('rec_action') or item.get('action', '')
        rev_up = item.get('rev_update', 'לעדכן ברוויט.')
        cls_cr = item.get('closure_crit', 'אימות בבדיקה חוזרת.')
        lines.append(f'<tr><td dir="rtl" align="right"><strong>{item["id"]}</strong></td><td dir="rtl" align="right">{item["title"]}</td><td dir="rtl" align="right" style="color: #B40000; font-weight: bold;">{item.get("prio", "P1")[:2]}</td><td dir="rtl" align="right">{item["loc"].split("|")[0]}</td><td dir="rtl" align="right"><strong>{rec_act}</strong></td><td dir="rtl" align="right" style="color: #007A3D;">{rev_up}</td><td dir="rtl" align="right" style="color: #005A9C;">{cls_cr}</td><td dir="rtl" align="right"><strong>OPEN</strong></td></tr>')
    lines.append('</table>')
    
    # 5. מסקנות והמלצת Hold Point
    lines.append('<h3 dir="rtl" align="right">5. הנחיות להגשת Revision 02 ותהליך סגירת ממצאים</h3>')
    lines.append('<p dir="rtl" align="right">על בסיס הממצאים והפעולות המומלצות, צוות התכנון מתבקש להגיש סט תוכניות מעודכן (Rev 02) תוך 14 יום לצורך הרצת בדיקת סגירת ממצאים אוטומטית.</p>')
    lines.append('<div style="background-color: #FFF0F0; border-right: 4px solid #B40000; padding: 12px; margin-top: 15px;" dir="rtl" align="right">')
    lines.append('<strong style="color: #B40000;">RECOMMENDED HOLD POINT:</strong><br>')
    lines.append('מומלץ שלא לקדם ביצוע של העבודות הרלוונטיות לממצאי RED עד לקבלת התייחסות המתכנן ואישור סגירת הממצאים ב-Revision 02.')
    lines.append('</div>')
    
    lines.append('</body>')
    lines.append('</html>')
    return '\n'.join(lines)

# Generate pure HTML for Electrical and Structure
el_html_pure = create_clean_semantic_gdoc_html(
    "דוח הנחיות תיקון, חלופות וסגירת ממצאים למתכנן החשמל",
    "מערכות חשמל, מתח נמוך ומערכות חירום",
    "מתכנן מערכות חשמל ותקשורת (צוות הנדסת חשמל)",
    "LOD_PR_EL_R24 / LOD_321_EL_R24 (חבילת 6.3GB)",
    get_all_22_electrical_designer_cards(),
    {"p1": "15", "p2": "4", "p3": "2", "p4": "1"}
)
with open('/home/yogi/lod_project/ELECTRICAL_PERFECT_PURE_RTL.html', 'w', encoding='utf-8') as f:
    f.write(el_html_pure)

st_html_pure = create_clean_semantic_gdoc_html(
    "דוח הנחיות תיקון, חלופות וסגירת ממצאים למתכנן הקונסטרוקציה",
    "הנדסת קונסטרוקציה, ביסוס ושלד",
    "מתכנן קונסטרוקציה ושלד (אלי חלמיש / הנדסת מבנים)",
    "Lod_ST_PR_R25 / Lod_ST_321_R25 / Lod_ST_339_R25",
    get_full_45_structural_cards(),
    {"p1": "20", "p2": "8", "p3": "10", "p4": "0"}
)
with open('/home/yogi/lod_project/STRUCTURE_PERFECT_PURE_RTL.html', 'w', encoding='utf-8') as f:
    f.write(st_html_pure)

print("Generated ELECTRICAL_PERFECT_PURE_RTL.html and STRUCTURE_PERFECT_PURE_RTL.html successfully!")
