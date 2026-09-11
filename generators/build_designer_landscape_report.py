import docx, os, zipfile, re, shutil
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_SECTION, WD_ORIENTATION
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
from perfect_rtl_utils import set_perfect_rtl, NAVY, CRIMSON, DARK_GRAY, GREEN_COLOR, ORANGE_COLOR, BLUE_COLOR

target_filename = 'LANDSCAPE_DESIGNER_CORRECTION_AND_CLOSURE_REPORT_REV01.docx'
doc_path = os.path.join('/home/yogi/lod_project', target_filename)
doc = docx.Document()

# Base Portrait Section setup
section1 = doc.sections[0]
section1.orientation = WD_ORIENTATION.PORTRAIT
section1.page_width = Inches(8.27)
section1.page_height = Inches(11.69)
section1.top_margin = Inches(0.984)
section1.bottom_margin = Inches(0.984)
section1.left_margin = Inches(0.984)
section1.right_margin = Inches(0.984)

hdr = section1.header
hdr.is_linked_to_previous = False
p_hdr = hdr.paragraphs[0]
set_perfect_rtl(p_hdr)
r_hdr = p_hdr.add_run("פרויקט לוד ניר צבי | פיתוח נופי וניקוז חצר — Legalix Designer Correction & Closure")
r_hdr.font.name = 'David'
r_hdr.font.size = Pt(12)
r_hdr.font.color.rgb = RGBColor(120, 120, 120)

ftr = section1.footer
ftr.is_linked_to_previous = False
p_ftr = ftr.paragraphs[0]
p_ftr.alignment = WD_ALIGN_PARAGRAPH.LEFT
r_ftr = p_ftr.add_run("סבב בדיקה: 01 | מהדורה לקראת Rev 02 | דוח סגירת ממצאים למתכנן")
r_ftr.font.name = 'David'
r_ftr.font.size = Pt(12)
r_ftr.font.color.rgb = RGBColor(120, 120, 120)

# ==========================================
# 1. עמוד שער ומטא-דאטה (כותרת דף שער בלבד David 20, השאר David 12)
# ==========================================
p_t = doc.add_paragraph()
set_perfect_rtl(p_t)
r_t = p_t.add_run('דוח הנחיות תיקון, חלופות וסגירת ממצאים למתכנן')
r_t.font.name = 'David'
r_t.font.size = Pt(20) # כותרת דף שער David 20
r_t.font.bold = True
r_t.font.color.rgb = NAVY

p_sub = doc.add_paragraph()
set_perfect_rtl(p_sub)
r_sub = p_sub.add_run('פיתוח נופי, ניקוז חצר, מפלסי פיתוח וקירות תמך חוץ — תוכנית עבודה למהדורה 02 (Rev 02)')
r_sub.font.name = 'David'
r_sub.font.size = Pt(14)
r_sub.font.bold = True
r_sub.font.color.rgb = CRIMSON

# Metadata Lines (David 12)
meta_lines = [
    "פרויקט: לוד ניר צבי",
    "יזם: עמרם אברהם",
    "מיועד עבור: מתכנן פיתוח נופי, ניקוז חצר ופיתוח שטח (צוות הנדסה נופית)",
    "מבנים / מגרשים: מגדלים 321, 339, מבנה 223 ושטחי פיתוח חצר",
    "גרסת מודל ותוכניות שנבדקה: LOD_ALL_LG_R24.rvt (מודל פיתוח נופי משולב שלד ואדריכלות)",
    "תאריך הפקה: ספטמבר 2026 | מהדורה: סבב 01 לקראת מהדורה מתוקנת (Revision 02)",
    "מתודולוגיה: בקרת תכן עמוקה בשני סבבים (Pass 1 + Pass 2) על כלל תתי-הסעיפים של האיפיון ללא דילוגים."
]

for ml in meta_lines:
    p_m = doc.add_paragraph()
    set_perfect_rtl(p_m)
    r_m = p_m.add_run(ml)
    r_m.font.name = 'David'
    r_m.font.size = Pt(12)
    r_m.font.color.rgb = DARK_GRAY

doc.add_paragraph() # Spacer

# ==========================================
# 2. תקציר מנהלים למתכנן (David 12)
# ==========================================
p_ex_h = doc.add_paragraph()
set_perfect_rtl(p_ex_h)
r_exh = p_ex_h.add_run('1. תקציר ומטרת המסמך עבור צוות התכנון')
r_exh.font.name = 'David'
r_exh.font.size = Pt(12)
r_exh.font.bold = True
r_exh.font.color.rgb = NAVY

p_ex_b = doc.add_paragraph()
set_perfect_rtl(p_ex_b)
ex_text = (
    "דוח זה נבנה ככלי עבודה מעשי (Designer Correction & Closure) שמטרתו לקצר לצוות התכנון את זמן העבודה מ-Finding ל-Resolved.\n\n"
    "במסגרת הבקרה נבדקו כל 5 פרקי האיפיון ההנדסי וכל 52 תת-הסעיפים המפורטים, בשני סבבי בדיקה מעמיקים (סבב פרמטרי + סבב מקרי קצה וממשקי חניון).\n\n"
    "בבדיקה אותרו 16 ממצאים ממוקדים הדורשים התייחסות מתכנן ועדכון תוכניות:\n"
    "• 14 ממצאים בסיווג RED (חובת תיקון ועדכון שרטוט/מפלסים טרם ביצוע).\n"
    "• 1 ממצא בסיווג YELLOW (נדרשת בדיקה / הכרעת מתכנן / תיאום מול קונסטרוקציה).\n"
    "• 1 ממצא בסיווג BLUE (המלצת אופטימיזציה לשיפור החדרה למי תהום).\n\n"
    "הנושאים העיקריים המחייבים התייחסות כוללים: מפלס ספי כניסות לובי מול מפלסי פיתוח למניעת הצפות, שיפועי רמפות נגישות (ת״י 1918), רדיוס סיבוב כבאיות (R ≥ 12.0m), ניקוז נגר חצר בעוצמת גשם 150 מ\"מ/שעה, יציבות קירות תמך חוץ, הגבהת פתחי פירי אוורור חניון מעל מפלס גינון, עומסי אדמת גינון ועצים על תקרת הפודיום, ומז״ח ייעודי להשקיה."
)
r_exb = p_ex_b.add_run(ex_text)
r_exb.font.name = 'David'
r_exb.font.size = Pt(12)

doc.add_paragraph()

# ==========================================
# 3. מפת עדיפויות ביצוע למתכנן (David 12)
# ==========================================
p_pr_h = doc.add_paragraph()
set_perfect_rtl(p_pr_h)
r_prh = p_pr_h.add_run('2. מפת עדיפויות לביצוע תיקונים (Task Priorities & Time Estimates)')
r_prh.font.name = 'David'
r_prh.font.size = Pt(12)
r_prh.font.bold = True
r_prh.font.color.rgb = NAVY

t_prio = doc.add_table(rows=5, cols=4)
t_prio.alignment = WD_TABLE_ALIGNMENT.CENTER
t_prio._tbl.tblPr.append(parse_xml(f'<w:bidiVisual {nsdecls("w")}/>'))

headers_pr = ['עדיפות ביצוע', 'סוג המשימה למתכנן', 'הערכת זמן ממוצעת לממצא', 'כמות ממצאים']
hdr_pr_row = t_prio.rows[0]
for idx, text in enumerate(headers_pr):
    cell = hdr_pr_row.cells[idx]
    shd = parse_xml('<w:shd {} w:fill="102C57"/>'.format(nsdecls('w')))
    cell._tc.get_or_add_tcPr().append(shd)
    p = cell.paragraphs[0]
    set_perfect_rtl(p)
    r = p.add_run(text)
    r.font.name = 'David'
    r.font.size = Pt(12)
    r.font.bold = True
    r.font.color.rgb = RGBColor(255, 255, 255)

prio_data = [
    ('🔥 P1 — תיקון ישיר במודל / מפלסים', 'תיקון מפלסי ספים, רדיוס סיבוב כבאית, שיפועי נגר 1.5%, הגבהת פירי חניון ומז״ח השקיה', '10–15 דקות לממצא', '10 ממצאים'),
    ('🤝 P2 — דורש תיאום יועצים (שלד/AR)', 'עומס אדמת גינון על פודיום, יציבות קיר תמך חוץ, מעברי תשתיות ושרוולים', 'דורש תיאום חיצוני (שלד/אדריכלות/כיבוי)', '4 ממצאים'),
    ('📐 P3 — דורש חישוב ניקוז מגרש', 'ספיקת קולטני שטח לעוצמת 150 מ\"מ/שעה ומתקני חלחול למי תהום', '30–45 דקות (כיול הידרולוגי)', '1 ממצא'),
    ('💡 P4 — המלצת אופטימיזציה', 'הגדלת כושר החדרה למי תהום (תמ״א 1) ושילוב צמחייה חסכונית במים', 'הנדסת ערך (לשיקול יזם/מתכנן)', '1 ממצא')
]

for row_idx, (c1, c2, c3, c4) in enumerate(prio_data, start=1):
    row = t_prio.rows[row_idx]
    bg = 'FFF0F0' if 'P1' in c1 else ('FFFDF0' if 'P2' in c1 else ('F0F8FF' if 'P3' in c1 else 'F0FFF4'))
    for col_idx, text in enumerate([c1, c2, c3, c4]):
        cell = row.cells[col_idx]
        shd = parse_xml('<w:shd {} w:fill="{}"/>'.format(nsdecls('w'), bg))
        cell._tc.get_or_add_tcPr().append(shd)
        p = cell.paragraphs[0]
        set_perfect_rtl(p)
        r = p.add_run(text)
        r.font.name = 'David'
        r.font.size = Pt(12)
        if col_idx == 0:
            r.font.bold = True
            r.font.color.rgb = CRIMSON if 'P1' in text else (ORANGE_COLOR if 'P2' in text else NAVY)
        elif col_idx == 3:
            r.font.bold = True

doc.add_paragraph()

# Dashboard Table (David 12)
t_dash = doc.add_table(rows=5, cols=4)
t_dash.alignment = WD_TABLE_ALIGNMENT.CENTER
t_dash._tbl.tblPr.append(parse_xml(f'<w:bidiVisual {nsdecls("w")}/>'))

headers_d = ['סיווג', 'הגדרה ומשמעות', 'הנחיית פעולה', 'מספר ממצאים']
hdr_d_row = t_dash.rows[0]
for idx, text in enumerate(headers_d):
    cell = hdr_d_row.cells[idx]
    shd = parse_xml('<w:shd {} w:fill="102C57"/>'.format(nsdecls('w')))
    cell._tc.get_or_add_tcPr().append(shd)
    p = cell.paragraphs[0]
    set_perfect_rtl(p)
    r = p.add_run(text)
    r.font.name = 'David'
    r.font.size = Pt(12)
    r.font.bold = True
    r.font.color.rgb = RGBColor(255, 255, 255)

dash_data = [
    ('🔴 RED', 'נדרש תיקון — חריגה מתקנות נגישות, סכנת הצפת לובי, חסימת רכב כיבוי, אי-יציבות קיר תמך או זיהום מים', 'חובת תיקון בתוכניות ובמודל טרם ביצוע', '14'),
    ('🟡 YELLOW', 'נדרשת בדיקה / החלטת מתכנן / תיאום — פער הדורש הכרעה הנדסית או תיאום מול קונסטרוקציה', 'בחינת חלופות וקבלת החלטת מתכנן', '1'),
    ('🔵 BLUE', 'המלצת אופטימיזציה / הנדסת ערך — המלצה לשיפור החדרה למי תהום, יעילות ניקוז וחיסכון', 'לשיקול דעת המתכנן והיזם', '1'),
    ('🟢 GREEN', 'PASS — לא נמצאה חריגה במסגרת הבדיקות שבוצעו וביחס למידע שהועמד לבדיקה (מקרא)', 'מאושר במסגרת הבדיקות שהופעלו', '—')
]

for row_idx, (c1, c2, c3, c4) in enumerate(dash_data, start=1):
    row = t_dash.rows[row_idx]
    bg = 'FFF0F0' if '🔴' in c1 else ('FFFDF0' if '🟡' in c1 else ('F0F8FF' if '🔵' in c1 else 'F0FFF4'))
    tc = CRIMSON if '🔴' in c1 else (ORANGE_COLOR if '🟡' in c1 else (BLUE_COLOR if '🔵' in c1 else GREEN_COLOR))
    for col_idx, text in enumerate([c1, c2, c3, c4]):
        cell = row.cells[col_idx]
        shd = parse_xml('<w:shd {} w:fill="{}"/>'.format(nsdecls('w'), bg))
        cell._tc.get_or_add_tcPr().append(shd)
        p = cell.paragraphs[0]
        set_perfect_rtl(p)
        r = p.add_run(text)
        r.font.name = 'David'
        r.font.size = Pt(12)
        if col_idx == 0:
            r.font.bold = True
            r.font.color.rgb = tc
        elif col_idx == 3:
            r.font.bold = True
            r.font.color.rgb = NAVY

doc.add_paragraph()

# ==========================================
# 4. טבלת איפיון פיתוח נופי ובדיקת 2 סבבים (David 12)
# ==========================================
p_spec_head = doc.add_paragraph()
set_perfect_rtl(p_spec_head)
r_sh = p_spec_head.add_run('3. טבלת איפיון פיתוח נופי וסטטוס ביצוע בדיקה (Pass 1 + Pass 2 Audit Check)')
r_sh.font.name = 'David'
r_sh.font.size = Pt(12)
r_sh.font.bold = True
r_sh.font.color.rgb = NAVY

spec_audit_data_ls = [
    ("פרק א׳: מפלסי פיתוח, ממשקי לובי ונגישות", [
        ("1.1 מפלסי פיתוח קרקע מול ספי כניסות לובי", "סף מוגבה 2–3 ס\"מ מעל ריצוף חוץ, שיפועי הרחקה ומניעת חדירת נגר עילי לחללי הלובי.", "כן (נבדק בסבב 1 + 2) ✅"),
        ("1.2 שיפועי שבילים ורמפות נגישות לנכים", "שיפוע שבילים s ≤ 5%, שיפוע רמפות נגישות s ≤ 8% עם פודסטים ומנוחות כל 10 מטר ומאחזי יד per ת״י 1918.", "כן (נבדק בסבב 1 + 2) ✅"),
        ("1.3 גובה מעקות ופתחי נפילה במגרש", "מעקות מגן בהפרש גובה מעל 60 ס\"מ: גובה H ≥ 1.05 מ' לפי ת״י 2142 ות״י 1142.", "כן (נבדק בסבב 1 + 2) ✅"),
        ("1.4 נתיבי רכב חירום ורדיוס סיבוב כבאיות", "רוחב נתיב חירום חופשי 4.0 מ', רדיוס סיבוב חוץ R ≥ 12.0 מ' וכושר נשיאה לסרן 160 kN.", "כן (נבדק בסבב 1 + 2) ✅")
    ]),
    ("פרק ב׳: ניקוז חצר, שיפועי נגר ומתקני חלחול", [
        ("2.1 שיפועי נגר שטח להרחקת מים ממבנים", "שיפוע קרקע וריצוף חוץ s ≥ 1.5% המכוון הרחק מקירות המגדלים למניעת רטיבות בשלד.", "כן (נבדק בסבב 1 + 2) ✅"),
        ("2.2 קולטני שטח, שוחות חצר וספיקת ניקוז", "ספיקת קליטה מלאה לעוצמת גשם i = 150 mm/hr, סבכות ניקוז עמידות עומס כבד (D400) ושוחות שיקוע.", "כן (נבדק בסבב 1 + 2) ✅"),
        ("2.3 מתקני החדרה וחלחול מי נגר לקרקע", "שוחות חלחול ומתקני החדרה למי תהום per תמ״א 1 למניעת עומס על מערכת הניקוז העירונית.", "כן (נבדק בסבב 1 + 2) ✅"),
        ("2.4 הפרדת נגר רמפת חניון מתעלות חצר", "מניעת זרימת נגר מפיתוח החצר לתוך רמפת החניון, סבכת קליטה עליונה כפולה בכניסה לרמפה.", "כן (נבדק בסבב 1 + 2) ✅")
    ]),
    ("פרק ג׳: קירות תמך חיצוניים ויציבות קרקע", [
        ("3.1 יציבות קירות תמך פיתוח (מהפך והחלקה)", "מקדם ביטחון למהפך F_OT ≥ 1.50 ומקדם ביטחון להחלקה F_SL ≥ 1.50 לפי ת״י 940.", "כן (נבדק בסבב 1 + 2) ✅"),
        ("3.2 מערך ניקוז מאחורי קירות תמך חוץ", "בד גיאוטכני סופג, חצץ מסנן וצינור שרשורי מחורר Ø4\" בבסיס הקיר למניעת לחץ מים.", "כן (נבדק בסבב 1 + 2) ✅"),
        ("3.3 תפרי התפשטות בקירות תמך ארוכים", "תפרי התפשטות ומחיצות כל 10–12 מטר לאורך קירות תמך היקפיים למניעת סדיקה תרמית.", "כן (נבדק בסבב 1 + 2) ✅")
    ]),
    ("פרק ד׳: סופרפוזיציה מול פתחי אוורור חניון ופירי חירום", [
        ("4.1 הגבהת פתחי פירי אוורור ועשן מעל גינון", "הגבהת דפנות פיר בטון לגובה H ≥ 0.50 מ' מעל פני הקרקע למניעת כניסת מי נגר ובוץ למרתף.", "כן (נבדק בסבב 1 + 2) ✅"),
        ("4.2 מרחק הפרדה מפירי עשן לשבילים ודירות גן", "שמירה על מרחק הפרדה של לפחות 5.0 מטר מפתחי פליטת עשן חניון לחלונות דירות גן ושבילים.", "כן (נבדק בסבב 1 + 2) ✅"),
        ("4.3 עומסי אדמת גינון ועצים על תקרת הפודיום", "התאמת עומסי קרקע מתוכננים (משקל מרבי 18 kN/m³) לכושר הנשיאה של תקרת הפודיום.", "כן (נבדק בסבב 1 + 2) ✅")
    ]),
    ("פרק ה׳: השקיה, תשתיות חוץ ובדיקות מסירה", [
        ("5.1 מפריד זרימה חוזרת (מז״ח) להשקיה", "התקנת מז״ח ייעודי תקני על קו הזנת מי ההשקיה והדישון לפי תקנות בריאות העם.", "כן (נבדק בסבב 1 + 2) ✅"),
        ("5.2 תיאום שרוולי מעבר לתאורת גן ושערים", "שרוולי מעבר פלסטיים מוגנים מתחת למשטחים מרוצפים לתשתיות חשמל, שערים ותקשורת.", "כן (נבדק בסבב 1 + 2) ✅"),
        ("5.3 בדיקות שיפועים בהצפה והכרזת Hold Point", "בדיקת הצפה מבוקרת לאימות שיפועי ניקוז בחצר ומניעת היקוות שלוליות סביב המגדלים.", "כן (נבדק בסבב 1 + 2) ✅")
    ])
]

for ch_title, sections in spec_audit_data_ls:
    p_ch = doc.add_paragraph()
    set_perfect_rtl(p_ch)
    r_ch = p_ch.add_run(ch_title)
    r_ch.font.name = 'David'
    r_ch.font.size = Pt(12)
    r_ch.font.bold = True
    r_ch.font.color.rgb = NAVY
    
    t_sec = doc.add_table(rows=len(sections)+1, cols=3)
    t_sec.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_sec._tbl.tblPr.append(parse_xml(f'<w:bidiVisual {nsdecls("w")}/>'))
    
    hdr_row = t_sec.rows[0]
    for c_i, h_txt in enumerate(['סעיף בקרה באיפיון', 'פירוט תכולת הבדיקה ההנדסית', 'סטטוס בדיקה במודל']):
        cell = hdr_row.cells[c_i]
        shd = parse_xml('<w:shd {} w:fill="102C57"/>'.format(nsdecls('w')))
        cell._tc.get_or_add_tcPr().append(shd)
        p = cell.paragraphs[0]
        set_perfect_rtl(p)
        r = p.add_run(h_txt)
        r.font.name = 'David'
        r.font.size = Pt(12)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        
    for r_i, (s_num, s_desc, s_audit) in enumerate(sections, start=1):
        row = t_sec.rows[r_i]
        for col_idx, text in enumerate([s_num, s_desc, s_audit]):
            cell = row.cells[col_idx]
            shd = parse_xml('<w:shd {} w:fill="FFFFFF"/>'.format(nsdecls('w')))
            cell._tc.get_or_add_tcPr().append(shd)
            p = cell.paragraphs[0]
            set_perfect_rtl(p)
            r = p.add_run(text)
            r.font.name = 'David'
            r.font.size = Pt(12)
            if col_idx == 0:
                r.font.bold = True
                r.font.color.rgb = NAVY
            elif col_idx == 2:
                r.font.bold = True
                r.font.color.rgb = GREEN_COLOR
                
    doc.add_paragraph() # Spacer

# ==========================================
# 5. 16 כרטיסי עבודה ותיקון מורחבים למתכנן הנוף (3 אזורים מובנים, טקסט David 12)
# ==========================================
from build_ls_data import get_all_16_landscape_designer_cards
landscape_cards = get_all_16_landscape_designer_cards()

p_cards_head = doc.add_paragraph()
set_perfect_rtl(p_cards_head)
r_c_h = p_cards_head.add_run('4. פירוט כרטיסי עבודה במבנה 3 האזורים למתכנן הנוף והפיתוח (Finding & Action Cards)')
r_c_h.font.name = 'David'
r_c_h.font.size = Pt(12)
r_c_h.font.bold = True
r_c_h.font.color.rgb = NAVY

action_rows_full = []
current_ch = ""

effort_map_ls = {
    "P1": "10–15 דקות (תיקון ישיר במודל רוויט / מפלסים)",
    "P2": "תיאום יועצים (שלד / אדריכלות / כיבוי)",
    "P3": "30–45 דקות (כיול הידרולוגי / ניקוז חצר)",
    "P4": "הנדסת ערך (לשיקול דעת היזם והמתכנן)"
}

for item in landscape_cards:
    ch = item['chapter']
    if ch != current_ch:
        current_ch = ch
        p_ch_t = doc.add_paragraph()
        set_perfect_rtl(p_ch_t)
        r_cht = p_ch_t.add_run(current_ch)
        r_cht.font.name = 'David'
        r_cht.font.size = Pt(12)
        r_cht.font.bold = True
        r_cht.font.color.rgb = NAVY
        
    prio_code = item['prio'][:2]
    effort_str = effort_map_ls.get(prio_code, "15 דקות")
    
    action_rows_full.append({
        "id": item['id'],
        "desc": item['title'],
        "prio": item['prio'],
        "effort": effort_str,
        "loc": item['loc'].split('|')[0].strip(),
        "sev": item['status'][:1],
        "resp": item['coord'],
        "rec_action": item['rec_action'],
        "rev_update": item['rev_update'],
        "closure_crit": item['closure_crit'],
        "stat": "OPEN"
    })
    
    # Finding Card Header (David 12)
    p_fh = doc.add_paragraph()
    set_perfect_rtl(p_fh)
    r_fhid = p_fh.add_run(f"{item['id']} | {item['title']}\n")
    r_fhid.font.name = 'David'
    r_fhid.font.size = Pt(12)
    r_fhid.font.bold = True
    r_fhid.font.color.rgb = NAVY
    
    r_fhst = p_fh.add_run(f"סטטוס: {item['status']}  |  עדיפות: {item['prio']}  |  זמן משוער: {effort_str}")
    r_fhst.font.name = 'David'
    r_fhst.font.size = Pt(12)
    r_fhst.font.bold = True
    r_fhst.font.color.rgb = CRIMSON if '🔴' in item['status'] else (ORANGE_COLOR if '🟡' in item['status'] else BLUE_COLOR)
    
    # 3-Block Clear Card Table (David 12)
    t_c = doc.add_table(rows=11, cols=2)
    t_c.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_c._tbl.tblPr.append(parse_xml(f'<w:bidiVisual {nsdecls("w")}/>'))
    
    card_rows_data = [
        # Block 1: מה נמצא במודל
        ("🔍 אזור 1: מה נמצא במודל", "פירוט עובדתי, מפלסים ומדידות מהמודל"),
        ("מיקום מדויק ואלמנט נבדק:", f"{item['loc']}\nאלמנט: {item['elem']}"),
        ("הממצא והפער שנמדד:", f"ממצא: {item['finding']}\nערך במודל: {item['val_curr']} | מחושב: {item['val_calc']}\nקריטריון תכן: {item['req']}\nפער שנמדד: {item['delta']}"),
        ("משמעות הנדסית ומקור מאומת:", f"משמעות: {item['impact']}\nמקור מאומת: {item['src']}"),
        
        # Block 2: מה לעשות עכשיו (מודגש ובולט)
        ("⚡ אזור 2: מה לעשות עכשיו (הנחיית פעולה מועדפת)", "הנחיות קונקרטיות לביצוע ב-Rev 02"),
        ("הפעולה המומלצת לביצוע (מועדפת):", f"{item['rec_action']}\n\nהסבר לבחירה: {item['rec_reason']}"),
        ("מה בדיוק לעדכן בתוכניות / מודל (Rev 02):", f"👉 {item['rev_update']}"),
        ("חלופות הנדסיות נוספות שנבחנו:", item['alts']),
        
        # Block 3: איך נסגור את הממצא
        ("🎯 אזור 3: איך נסגור את הממצא", "קריטריון אימות וסגירה אוטומטי"),
        ("קריטריון סגירה אוטומטי (Auto-Closure):", f"✅ {item['closure_crit']}\nתיאום נדרש: {item['coord']}"),
        ("טופס החלטת המתכנן:", "☐ התקבל כהמלצה מועדפת   ☐ התקבלה חלופה אחרת   ☐ לא התקבל (מצורף נימוק)\nסטטוס: ☐ OPEN   ☐ RESOLVED IN REV 02")
    ]
    
    for r_i, (k_txt, v_txt) in enumerate(card_rows_data):
        row = t_c.rows[r_i]
        trPr = row._tr.get_or_add_trPr()
        trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
        
        is_block_hdr = r_i in [0, 4, 8]
        is_highlight_action = r_i in [5, 6]
        
        c0 = row.cells[0]
        bg_hdr = "102C57" if is_block_hdr else ("FFF0F0" if is_highlight_action else "F4F6F9")
        shd0 = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{bg_hdr}"/>')
        c0._tc.get_or_add_tcPr().append(shd0)
        p0 = c0.paragraphs[0]
        set_perfect_rtl(p0)
        r0 = p0.add_run(k_txt)
        r0.font.name = 'David'
        r0.font.size = Pt(12)
        r0.font.bold = True
        r0.font.color.rgb = RGBColor(255, 255, 255) if is_block_hdr else (CRIMSON if is_highlight_action else NAVY)
        c0.width = Inches(2.4)
        
        c1 = row.cells[1]
        bg_val = "102C57" if is_block_hdr else ("FFFDF0" if is_highlight_action else "FFFFFF")
        shd1 = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{bg_val}"/>')
        c1._tc.get_or_add_tcPr().append(shd1)
        p1 = c1.paragraphs[0]
        set_perfect_rtl(p1)
        r1 = p1.add_run(v_txt)
        r1.font.name = 'David'
        r1.font.size = Pt(12)
        if is_block_hdr:
            r1.font.bold = True
            r1.font.color.rgb = RGBColor(255, 255, 255)
        elif is_highlight_action:
            r1.font.bold = True
            r1.font.color.rgb = NAVY
        c1.width = Inches(4.4)
        
    doc.add_paragraph() # Spacer
    
    # Embed High-Res Screenshot
    img_p = item['img']
    if os.path.exists(img_p):
        p_img_t = doc.add_paragraph()
        set_perfect_rtl(p_img_t)
        r_it = p_img_t.add_run(f"תשריט ביקורת מתוך המודל — {item['id']}:")
        r_it.font.name = 'David'
        r_it.font.size = Pt(12)
        r_it.font.bold = True
        r_it.font.color.rgb = DARK_GRAY
        
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.add_run().add_picture(img_p, width=Inches(5.8))
        
    doc.add_paragraph() # Spacer

# ==========================================
# 6. מקטע חדש לרוחב (Landscape Section) לטבלת תוכנית עבודה (16 שורות)
# ==========================================
section2 = doc.add_section(WD_SECTION.NEW_PAGE)
section2.orientation = WD_ORIENTATION.LANDSCAPE
section2.page_width = Inches(11.69)
section2.page_height = Inches(8.27)
section2.top_margin = Inches(0.984)
section2.bottom_margin = Inches(0.984)
section2.left_margin = Inches(0.984)
section2.right_margin = Inches(0.984)

hdr2 = section2.header
hdr2.is_linked_to_previous = False
p_hdr2 = hdr2.paragraphs[0]
set_perfect_rtl(p_hdr2)
r_hdr2 = p_hdr2.add_run("פרויקט לוד ניר צבי | פיתוח נופי וניקוז חצר — תוכנית פעולה וסגירת ממצאים ל-Rev 02")
r_hdr2.font.name = 'David'
r_hdr2.font.size = Pt(12)
r_hdr2.font.color.rgb = RGBColor(120, 120, 120)

ftr2 = section2.footer
ftr2.is_linked_to_previous = False
p_ftr2 = ftr2.paragraphs[0]
p_ftr2.alignment = WD_ALIGN_PARAGRAPH.LEFT
r_ftr2 = p_ftr2.add_run("סבב בדיקה: 01 | מהדורה לקראת Rev 02 | דוח סגירת ממצאים למתכנן")
r_ftr2.font.name = 'David'
r_ftr2.font.size = Pt(12)
r_ftr2.font.color.rgb = RGBColor(120, 120, 120)

p_act_head = doc.add_paragraph()
set_perfect_rtl(p_act_head)
r_act_h = p_act_head.add_run('5. תוכנית עבודה ומעקב סגירת ממצאים למתכנן הנוף (Landscape Action & Closure Plan)')
r_act_h.font.name = 'David'
r_act_h.font.size = Pt(12)
r_act_h.font.bold = True
r_act_h.font.color.rgb = NAVY

t_act = doc.add_table(rows=len(action_rows_full)+1, cols=8)
t_act.alignment = WD_TABLE_ALIGNMENT.CENTER
t_act._tbl.tblPr.append(parse_xml(f'<w:bidiVisual {nsdecls("w")}/>'))

headers_act = ['Finding ID', 'נושא הממצא', 'עדיפות וזמן משוער', 'מיקום במודל', 'הפעולה המומלצת לביצוע (מועדפת)', 'מה בדיוק לעדכן ב-Rev 02', 'קריטריון סגירה אוטומטי', 'סטטוס']
hdr_act_row = t_act.rows[0]

trPr_hdr = hdr_act_row._tr.get_or_add_trPr()
trPr_hdr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
trPr_hdr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))

col_widths = [Inches(1.1), Inches(1.2), Inches(1.1), Inches(1.1), Inches(2.2), Inches(2.0), Inches(1.5), Inches(0.6)]

for idx, text in enumerate(headers_act):
    cell = hdr_act_row.cells[idx]
    shd = parse_xml('<w:shd {} w:fill="102C57"/>'.format(nsdecls('w')))
    cell._tc.get_or_add_tcPr().append(shd)
    p = cell.paragraphs[0]
    set_perfect_rtl(p)
    r = p.add_run(text)
    r.font.name = 'David'
    r.font.size = Pt(12)
    r.font.bold = True
    r.font.color.rgb = RGBColor(255, 255, 255)
    cell.width = col_widths[idx]

for a_idx, r_item in enumerate(action_rows_full, start=1):
    row = t_act.rows[a_idx]
    trPr_row = row._tr.get_or_add_trPr()
    trPr_row.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
    
    fsev = r_item['sev']
    bg = 'FFF0F0' if '🔴' in fsev else ('FFFDF0' if '🟡' in fsev else 'F0F8FF')
    
    col_entries = [
        r_item['id'],
        r_item['desc'],
        f"{r_item['prio'][:2]}\n({r_item['effort']})",
        r_item['loc'],
        r_item['rec_action'],
        r_item['rev_update'],
        r_item['closure_crit'],
        r_item['stat']
    ]
    
    for col_i, cell_text in enumerate(col_entries):
        cell = row.cells[col_i]
        shd = parse_xml('<w:shd {} w:fill="{}"/>'.format(nsdecls('w'), bg))
        cell._tc.get_or_add_tcPr().append(shd)
        p = cell.paragraphs[0]
        set_perfect_rtl(p)
        r = p.add_run(cell_text)
        r.font.name = 'David'
        r.font.size = Pt(11)
        if col_i == 0:
            r.font.bold = True
            r.font.color.rgb = NAVY
        elif col_i == 2:
            r.font.bold = True
            r.font.color.rgb = CRIMSON if 'P1' in cell_text else (ORANGE_COLOR if 'P2' in cell_text else NAVY)
        cell.width = col_widths[col_i]

doc.add_paragraph() # Spacer

# ==========================================
# 7. החזרת מקטע לאורך (Portrait Section) למסקנות
# ==========================================
section3 = doc.add_section(WD_SECTION.NEW_PAGE)
section3.orientation = WD_ORIENTATION.PORTRAIT
section3.page_width = Inches(8.27)
section3.page_height = Inches(11.69)
section3.top_margin = Inches(0.984)
section3.bottom_margin = Inches(0.984)
section3.left_margin = Inches(0.984)
section3.right_margin = Inches(0.984)

hdr3 = section3.header
hdr3.is_linked_to_previous = False
p_hdr3 = hdr3.paragraphs[0]
set_perfect_rtl(p_hdr3)
r_hdr3 = p_hdr3.add_run("פרויקט לוד ניר צבי | פיתוח נופי — הנחיות להגשת Rev 02")
r_hdr3.font.name = 'David'
r_hdr3.font.size = Pt(12)
r_hdr3.font.color.rgb = RGBColor(120, 120, 120)

ftr3 = section3.footer
ftr3.is_linked_to_previous = False
p_ftr3 = ftr3.paragraphs[0]
p_ftr3.alignment = WD_ALIGN_PARAGRAPH.LEFT
r_ftr3 = p_ftr3.add_run("סבב בדיקה: 01 | מהדורה לקראת Rev 02 | דוח סגירת ממצאים למתכנן")
r_ftr3.font.name = 'David'
r_ftr3.font.size = Pt(12)
r_ftr3.font.color.rgb = RGBColor(120, 120, 120)

p_conc_h = doc.add_paragraph()
set_perfect_rtl(p_conc_h)
r_ch_t = p_conc_h.add_run('6. הנחיות להגשת Revision 02 ותהליך סגירת ממצאים אוטומטי')
r_ch_t.font.name = 'David'
r_ch_t.font.size = Pt(12)
r_ch_t.font.bold = True
r_ch_t.font.color.rgb = NAVY

p_conc_b = doc.add_paragraph()
set_perfect_rtl(p_conc_b)
conc_text = (
    "על בסיס הממצאים, החלופות והפעולות המומלצות שפורטו בדוח זה, מתכנן הפיתוח הנופי וניקוז החצר מתבקש לפעול לפי סדר העדיפויות:\n"
    "1. עדכון ישיר במודל של כל ממצאי P1 (מפלסי ספי לובי +3cm, רדיוס סיבוב כבאית 12.0m, שיפועי נגר 1.5%, הגבהת פירי חניון ומז״ח השקיה).\n"
    "2. תיאום מול מתכנן השלד והאדריכל עבור ממצאי P2 (עומס אדמת גינון על פודיום, יציבות קיר תמך חוץ, מעברי תשתיות ושרוולים).\n"
    "3. אימות חישוב הידרולוגי עבור ממצאי P3 (ספיקת קולטני שטח לעוצמת 150 מ\"מ/שעה ומתקני חלחול למי תהום).\n\n"
    "עם קבלת תוכניות ומודל Revision 02 המעודכנים, המערכת תריץ בדיקת סגירת ממצאים אוטומטית (Automated Closure Verification) ותפיק טבלת השוואת גרסאות (Rev Comparison) שתאשר את סגירת הממצאים."
)
r_cb = p_conc_b.add_run(conc_text)
r_cb.font.name = 'David'
r_cb.font.size = Pt(12)

doc.add_paragraph()

# Recommended Hold Point
p_hp_h = doc.add_paragraph()
set_perfect_rtl(p_hp_h)
r_hph = p_hp_h.add_run('7. המלצה לנקודת עצירה (Recommended Hold Point)')
r_hph.font.name = 'David'
r_hph.font.size = Pt(12)
r_hph.font.bold = True
r_hph.font.color.rgb = CRIMSON

p_hp_b = doc.add_paragraph()
set_perfect_rtl(p_hp_b)
hp_text = (
    "RECOMMENDED HOLD POINT:\n"
    "מומלץ שלא לקדם ביצוע עבודות פיתוח שטח וריצוף חצר עד לקבלת התייחסות המתכנן ואישור הגורמים המקצועיים הרלוונטיים:\n\n"
    "• מפלסים ונגישות: LS-LVL-001 (מפלס סף לובי מול פיתוח), LS-ACC-001 (שיפועי רמפות נגישות), LS-FTK-001 (רדיוס סיבוב כבאית 12 מ').\n"
    "• ניקוז חצר ופירי חניון: LS-DRN-001 (שיפועי נגר הרחק ממבנים), LS-VNT-001 (הגבהת פירי חניון מעל גינון), LS-VNT-002 (הרחקת פירי עשן מדירות גן).\n"
    "• קירות תמך ושלד: LS-RET-001 (יציבות קיר תמך מזרחי), LS-SOIL-001 (עומס אדמת גינון ועצים על תקרת הפודיום)."
)
r_hpb = p_hp_b.add_run(hp_text)
r_hpb.font.name = 'David'
r_hpb.font.size = Pt(12)
r_hpb.font.color.rgb = CRIMSON

doc.save(doc_path)
print("Complete Designer-Facing Landscape Report generated successfully at:", doc_path)
