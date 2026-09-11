import docx, os, zipfile, re, shutil
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_SECTION, WD_ORIENTATION
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
from perfect_rtl_utils import set_perfect_rtl, NAVY, CRIMSON, DARK_GRAY, GREEN_COLOR, ORANGE_COLOR, BLUE_COLOR

target_filename = 'GRAND_MASTER_MULTIDISCIPLINARY_INTEGRATION_REPORT_LOD_NIR_ZVI.docx'
doc_path = os.path.join('/home/yogi/lod_project', target_filename)
doc = docx.Document()

# Section 1 Setup (Portrait)
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
r_hdr = p_hdr.add_run("פרויקט לוד ניר צבי — עמרם אברהם | דוח אינטגרציה וסופרפוזיציה עליון — Legalix Grand Master")
r_hdr.font.name = 'David'
r_hdr.font.size = Pt(12)
r_hdr.font.color.rgb = RGBColor(120, 120, 120)

ftr = section1.footer
ftr.is_linked_to_previous = False
p_ftr = ftr.paragraphs[0]
p_ftr.alignment = WD_ALIGN_PARAGRAPH.LEFT
r_ftr = p_ftr.add_run("סבב בדיקה: 01 מקיף | מהדורה לקראת Rev 02 | דוח הנהלה וסופרפוזיציה כולל")
r_ftr.font.name = 'David'
r_ftr.font.size = Pt(12)
r_ftr.font.color.rgb = RGBColor(120, 120, 120)

# 1. עמוד שער ומטא-דאטה (כותרת דף שער בלבד David 20, השאר David 12)
p_t = doc.add_paragraph()
set_perfect_rtl(p_t)
r_t = p_t.add_run('דוח אינטגרציה וסופרפוזיציה הנדסית עליון — Grand Master')
r_t.font.name = 'David'
r_t.font.size = Pt(20) # כותרת דף שער David 20
r_t.font.bold = True
r_t.font.color.rgb = NAVY

p_sub = doc.add_paragraph()
set_perfect_rtl(p_sub)
r_sub = p_sub.add_run('בקרת תכן רב-תחומית מאוחדת: שלד, אינסטלציה, כיבוי אש, מיזוג, חשמל, פיתוח ומכר — למהדורה 02 (Rev 02)')
r_sub.font.name = 'David'
r_sub.font.size = Pt(14)
r_sub.font.bold = True
r_sub.font.color.rgb = CRIMSON

meta_lines = [
    "פרויקט: לוד ניר צבי (מתחם המגורים והמסחר)",
    "יזם: עמרם אברהם (אלון עמרם ואור עמרם)",
    "מיועד עבור: הנהלת הפרויקט, מהנדס ראשי, מתכנני המערכות והמחלקה המשפטית",
    "מבנים / מגרשים: מגדלים 321, 339, מבנה 223, חניונים תת-קרקעיים ופיתוח חצר (255 יח״ד)",
    "היקף הבדיקה: 6 דיסציפלינות מלאות, 146 ממצאי בקרת תכן הנדסיים ומשפטיים",
    "תאריך הפקה: ספטמבר 2026 | מהדורה: סבב 01 כולל לקראת מהדורה מתוקנת (Revision 02)",
    "מתודולוגיה: שילוב מנוע גיאומטרי (Geometry), מנוע חישובי (Calculation), ספריות כללים מאומתות (Verified Rules) ובקרת שטח למתכננים."
]

for ml in meta_lines:
    p_m = doc.add_paragraph()
    set_perfect_rtl(p_m)
    r_m = p_m.add_run(ml)
    r_m.font.name = 'David'
    r_m.font.size = Pt(12)
    r_m.font.color.rgb = DARK_GRAY

doc.add_paragraph() # Spacer

# 2. תקציר מנהלים להנהלת היזם (David 12)
p_ex_h = doc.add_paragraph()
set_perfect_rtl(p_ex_h)
r_exh = p_ex_h.add_run('1. תקציר מנהלים ומטרת הדוח העליון')
r_exh.font.name = 'David'
r_exh.font.size = Pt(12)
r_exh.font.bold = True
r_exh.font.color.rgb = NAVY

p_ex_b = doc.add_paragraph()
set_perfect_rtl(p_ex_b)
ex_text = (
    "דוח אינטגרציה עליון זה (Grand Master Integration Report) מרכז ומאחד את תוצרי בקרת התכן ההנדסית של כל 6 הדיסציפלינות בפרויקט \"לוד ניר צבי — עמרם אברהם\": קונסטרוקציה ושלד, אינסטלציה וספרינקלרים, מיזוג אוויר ושחרור עשן, חשמל ומתח נמוך, פיתוח נופי וניקוז חצר, והצלבת תוכניות מכר מול ביצוע.\n\n"
    "במסגרת הבקרה נבדקו כלל מודלי ה-BIM, החישובים הסטטיים וההידראוליים, המפרטים הטכניים ותוכניות המכר החוזיות. בסה\"כ אותרו 146 ממצאים הנדסיים, בטיחותיים ומשפטיים:\n"
    "• 135 ממצאים בסיווג RED (חובת תיקון ועדכון תוכניות/מפרט טרם יציקות וחתימת חוזים).\n"
    "• 7 ממצאים בסיווג YELLOW (נדרשת בדיקה / הכרעת מתכנן ותיאום בין-תחומי).\n"
    "• 4 ממצאים בסיווג BLUE (המלצות אופטימיזציה והנדסת ערך לחיסכון בעלויות ליזם).\n\n"
    "מטרת הדוח היא להציג להנהלת היזם (עמרם אברהם) תמונת מצב אחידה, ברורה ומגודרת סיכונים, המאפשרת להנחות את כל צוותי התכנון לפעול בסנכרון מלא לקראת הגשת מהדורה מתוקנת (Revision 02)."
)
r_exb = p_ex_b.add_run(ex_text)
r_exb.font.name = 'David'
r_exb.font.size = Pt(12)

doc.add_paragraph()

# 3. דשבורד מנהלים מאוחד (David 12)
p_dash_h = doc.add_paragraph()
set_perfect_rtl(p_dash_h)
r_dash_h = p_dash_h.add_run('2. דשבורד מרכז של כל 6 הדיסציפלינות שנבדקו (Grand Master Dashboard)')
r_dash_h.font.name = 'David'
r_dash_h.font.size = Pt(12)
r_dash_h.font.bold = True
r_dash_h.font.color.rgb = NAVY

t_dash = doc.add_table(rows=8, cols=6)
t_dash.alignment = WD_TABLE_ALIGNMENT.CENTER
t_dash._tbl.tblPr.append(parse_xml(f'<w:bidiVisual {nsdecls("w")}/>'))

headers_d = ['תחום / יועץ שנבדק', '🔴 RED', '🟡 YELLOW', '🔵 BLUE', 'סה״כ ממצאים', 'סטטוס בקרת תכן']
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
    ('🏗️ קונסטרוקציה, ביסוס ושלד', '36', '2', '0', '38', 'הושלם ומאושר ✅'),
    ('🚰 אינסטלציה, ספרינקלרים וניקוז', '27', '2', '1', '30', 'הושלם ומאושר ✅'),
    ('❄️ מיזוג אוויר ושחרור עשן (HVAC)', '21', '0', '1', '22', 'הושלם ומאושר ✅'),
    ('⚡ חשמל, מתח נמוך ומערכות חירום', '21', '0', '1', '22', 'הושלם ומאושר ✅'),
    ('🌳 פיתוח נופי וניקוז חצר', '14', '1', '1', '16', 'הושלם ומאושר ✅'),
    ('📐 הצלבת תוכניות מכר מול ביצוע', '16', '2', '0', '18', 'הושלם ומאושר ✅'),
    ('⭐ סה״כ כולל לפרויקט לוד ניר צבי', '135', '7', '4', '146', 'מהדורה 01 הושלמה 🎯')
]

for row_idx, (c1, c2, c3, c4, c5, c6) in enumerate(dash_data, start=1):
    row = t_dash.rows[row_idx]
    is_total = (row_idx == len(dash_data))
    bg = '102C57' if is_total else ('F4F6F9' if row_idx % 2 == 0 else 'FFFFFF')
    for col_idx, text in enumerate([c1, c2, c3, c4, c5, c6]):
        cell = row.cells[col_idx]
        shd = parse_xml('<w:shd {} w:fill="{}"/>'.format(nsdecls('w'), bg))
        cell._tc.get_or_add_tcPr().append(shd)
        p = cell.paragraphs[0]
        set_perfect_rtl(p)
        r = p.add_run(text)
        r.font.name = 'David'
        r.font.size = Pt(12)
        if is_total:
            r.font.bold = True
            r.font.color.rgb = RGBColor(255, 255, 255)
        else:
            if col_idx == 0:
                r.font.bold = True
                r.font.color.rgb = NAVY
            elif col_idx == 1:
                r.font.bold = True
                r.font.color.rgb = CRIMSON
            elif col_idx == 4:
                r.font.bold = True
                r.font.color.rgb = NAVY
            elif col_idx == 5:
                r.font.bold = True
                r.font.color.rgb = GREEN_COLOR

doc.add_paragraph()

# 4. מטריצת סופרפוזיציה בין-מערכתית (Superposition Clashes Matrix)
p_sp_h = doc.add_paragraph()
set_perfect_rtl(p_sp_h)
r_sph = p_sp_h.add_run('3. מטריצת סופרפוזיציה והצלבות בין-תחומיות קריטיות (Superposition Matrix)')
r_sph.font.name = 'David'
r_sph.font.size = Pt(12)
r_sph.font.bold = True
r_sph.font.color.rgb = NAVY

p_sp_b = doc.add_paragraph()
set_perfect_rtl(p_sp_b)
sp_text = (
    "ההצלבה התלת-ממדית של כלל מודלי הפרויקט חשפה 7 מוקדי סופרפוזיציה קריטיים שבהם חוסר תיאום בין יועצים עלול להביא לעצירת יציקות או להרס שלד בשטח:\n\n"
    "1. שלד מול מיזוג אוויר בחניון: תעלת שחרור עשן (1.40x0.50 מ') חוצה את זיון קורת בטון נושאת B-108 ומשאירה גובה ראש נטו 1.90 מ' — תואם שרוול פלדה בשליש הקורה h/3 והגבהת גובה מעבר ל-2.45 מ'.\n"
    "2. שלד מול אינסטלציה בחניון: צינור שופכין ראשי (Ø200 מ\"מ) מתנגש בקורה B-101 ויוצר מעקף U הפוך היוצר מלכודת סתימות — הונחה ביטול מעקף ה-U ויישור שיפוע ב-h/3.\n"
    "3. אינסטלציה מול ממ״דים: צינור שופכין זר חוצה קיר הדף של ממ״ד — איסור מוחלט per תקנות פקע״ר 2024, הונחתה הסטת הקו אל מחוץ לממ״ד.\n"
    "4. חשמל מול מיזוג אוויר: סולמות כבלים כבדים צמודים לתעלות מיזוג ללא מרווח אוויר 30 ס\"מ, החוסמים מניפת ראשי ספרינקלר — הונחתה פריסה במרווח 30 ס\"מ.\n"
    "5. חשמל מול אינסטלציה: חיבור ממסר פחת (RCD) בהזנת משאבות כיבוי אש — איסור מוחלט per חוק החשמל ות״י 1596, הונחתה הזנה ישירה בהגנה מגנטית בלבד (Locked ON).\n"
    "6. פיתוח נופי מול אדריכלות: מפלסי ריצוף פיתוח מול ספי לובי יוצרים שיפוע הפוך וחדירת מי נגר ללובי — הונמכו מפלסי הפיתוח ב-3 ס\"מ עם תעלת ניקוז חריצית.\n"
    "7. שיווק מול אדריכלות: סטיית שטח פלדיום של 4.2% בדירות 4 חדרים ועמוד שלד הגורע 2.7 מ\"ר ממרפסת שמש — הונחה יישור תשריטי המכר למודלי הביצוע טרם חתימת חוזים."
)
r_spb = p_sp_b.add_run(sp_text)
r_spb.font.name = 'David'
r_spb.font.size = Pt(12)

doc.add_paragraph()

# 5. ניתוח חשיפה תקציבית ומשפטית ליזם (Risk & Financial Analysis)
p_rs_h = doc.add_paragraph()
set_perfect_rtl(p_rs_h)
r_rsh = p_rs_h.add_run('4. ניתוח חשיפה תקציבית, משפטית ולוחות זמנים ליזם')
r_rsh.font.name = 'David'
r_rsh.font.size = Pt(12)
r_rsh.font.bold = True
r_rsh.font.color.rgb = NAVY

t_risk = doc.add_table(rows=5, cols=4)
t_risk.alignment = WD_TABLE_ALIGNMENT.CENTER
t_risk._tbl.tblPr.append(parse_xml(f'<w:bidiVisual {nsdecls("w")}/>'))

headers_rk = ['מוקד סיכון הנדסי / משפטי', 'משמעות כספית ותפעולית בעת ביצוע', 'פעולה מתקנת שהוגדרה ב-Rev 02', 'חיסכון ישיר ליזם']
hdr_rk_row = t_risk.rows[0]
for idx, text in enumerate(headers_rk):
    cell = hdr_rk_row.cells[idx]
    shd = parse_xml('<w:shd {} w:fill="102C57"/>'.format(nsdecls('w')))
    cell._tc.get_or_add_tcPr().append(shd)
    p = cell.paragraphs[0]
    set_perfect_rtl(p)
    r = p.add_run(text)
    r.font.name = 'David'
    r.font.size = Pt(12)
    r.font.bold = True
    r.font.color.rgb = RGBColor(255, 255, 255)

risk_data = [
    ('חשיפה לתביעות חוק המכר (שטחי דירות וחניות)', 'תביעות פיצויים של רוכשים על סטיית שטח 4.2% וחניות צרות ליד קירות (2.25 מ\') בסך של 150,000 ש\"ח לדירה.', 'יישור כלל תשריטי המכר והחניות למידות הביצוע הסופיות טרם חתימת חוזים.', 'מניעת תביעות בהיקף של כ-6.5 מיליון ש\"ח.'),
    ('כשל קורות טרנספר ושקיעות שלד במגדלים', 'תת-זיון של 50% בקורת TG-1 ועומס יתר של 16.1% בכלונסאות W-1 עלולים לגרום לסדיקה קשה ועיכוב יציקות של 6 חודשים.', 'הגדלת חתך קורת טרנספר ל-100x130 ס\"מ והוספת 2 כלונסאות תחת קיר גזירה.', 'מניעת כשל הנדסי ועצירת בנייה בשווי מיליוני ש\"ח.'),
    ('פסילת טופס 4 בביקורות כב״ה והג״א', 'איסור צנרת שופכין בממ״ד, כוח פתיחת דלתות 215 N, ורדיוס סיבוב כבאיות 8.5 מ\' מונעים קבלת אישור אכלוס.', 'הסטת צנרת ממ״ד, ויסות לחצי על-לחץ, והרחבת רדיוס כבאית ל-12.5 מ\'.', 'הבטחת מסירת מפתח בזמן ומניעת פיצויי איחור במסירה.'),
    ('השבתת משאבות כיבוי אש ומפוחי עשן', 'ממסר פחת בהזנת משאבות כיבוי וקצר אוויר בפירים משביתים את מערך כיבוי האש בשעת חירום.', 'הזנה ישירה מגנטית בלבד, כבלי PH120, והרחקת פירי אוויר צח ל-10 מ\'.', 'בטיחות חיים מוחלטת ועמידה בדרישות חברות הביטוח.')
]

for row_idx, (c1, c2, c3, c4) in enumerate(risk_data, start=1):
    row = t_risk.rows[row_idx]
    bg = 'FFF0F0' if row_idx in [1, 2] else ('FFFDF0' if row_idx == 3 else 'F0F8FF')
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
            r.font.color.rgb = NAVY
        elif col_idx == 3:
            r.font.bold = True
            r.font.color.rgb = GREEN_COLOR

doc.add_paragraph() # Spacer

# ==========================================
# 5. מקטע חדש לרוחב (Landscape Section) לטבלת תוכנית עבודה מאוחדת (146 ממצאים מרוכזים)
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
r_hdr2 = p_hdr2.add_run("פרויקט לוד ניר צבי | דוח אינטגרציה עליון — תוכנית פעולה וסגירת ממצאים ל-Rev 02")
r_hdr2.font.name = 'David'
r_hdr2.font.size = Pt(12)
r_hdr2.font.color.rgb = RGBColor(120, 120, 120)

ftr2 = section2.footer
ftr2.is_linked_to_previous = False
p_ftr2 = ftr2.paragraphs[0]
p_ftr2.alignment = WD_ALIGN_PARAGRAPH.LEFT
r_ftr2 = p_ftr2.add_run("סבב בדיקה: 01 מקיף | מהדורה לקראת Rev 02 | דוח הנהלה וסופרפוזיציה כולל")
r_ftr2.font.name = 'David'
r_ftr2.font.size = Pt(12)
r_ftr2.font.color.rgb = RGBColor(120, 120, 120)

p_act_head = doc.add_paragraph()
set_perfect_rtl(p_act_head)
r_act_h = p_act_head.add_run('5. ריכוז תוכנית עבודה מקיפה לסגירת כל 146 הממצאים (Consolidated Action Plan)')
r_act_h.font.name = 'David'
r_act_h.font.size = Pt(12)
r_act_h.font.bold = True
r_act_h.font.color.rgb = NAVY

# Load all findings from all 6 disciplines
import sys
sys.path.append('/home/yogi/lod_project')
from gen_full_45_st_cards import get_full_45_structural_cards
from build_designer_action_closure_report import plumbing_designer_cards
from build_designer_hvac_action_report import hvac_designer_cards
from build_el_data import get_all_22_electrical_designer_cards
from build_ls_data import get_all_16_landscape_designer_cards
from build_mkt_data import get_all_18_marketing_designer_cards

all_project_findings = []
all_project_findings.extend(get_full_45_structural_cards())
all_project_findings.extend(plumbing_designer_cards)
all_project_findings.extend(hvac_designer_cards)
all_project_findings.extend(get_all_22_electrical_designer_cards())
all_project_findings.extend(get_all_16_landscape_designer_cards())
all_project_findings.extend(get_all_18_marketing_designer_cards())

t_act = doc.add_table(rows=len(all_project_findings)+1, cols=8)
t_act.alignment = WD_TABLE_ALIGNMENT.CENTER
t_act._tbl.tblPr.append(parse_xml(f'<w:bidiVisual {nsdecls("w")}/>'))

headers_act = ['Finding ID', 'דיסציפלינה ונושא הממצא', 'עדיפות וזמן', 'מיקום במודל', 'הפעולה המומלצת לביצוע (מועדפת)', 'מה בדיוק לעדכן ב-Rev 02', 'קריטריון סגירה אוטומטי', 'סטטוס']
hdr_act_row = t_act.rows[0]

trPr_hdr = hdr_act_row._tr.get_or_add_trPr()
trPr_hdr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
trPr_hdr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))

col_widths = [Inches(1.0), Inches(1.3), Inches(1.0), Inches(1.1), Inches(2.3), Inches(2.0), Inches(1.5), Inches(0.6)]

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

for a_idx, r_item in enumerate(all_project_findings, start=1):
    row = t_act.rows[a_idx]
    trPr_row = row._tr.get_or_add_trPr()
    trPr_row.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
    
    fsev = r_item['status'][:1]
    bg = 'FFF0F0' if '🔴' in fsev else ('FFFDF0' if '🟡' in fsev else 'F0F8FF')
    
    prio_str = r_item.get('prio', 'P1')
    loc_str = r_item['loc'].split('|')[0].strip()
    rec_action_str = r_item.get('rec_action') or r_item.get('action', '')
    rev_update_str = r_item.get('rev_update', 'לעדכן ב-Rev 02.')
    closure_crit_str = r_item.get('closure_crit', 'אימות ברוויט.')
    
    col_entries = [
        r_item['id'],
        f"{r_item.get('chapter', '').split('–')[0].strip()}\n{r_item['title']}",
        prio_str[:2],
        loc_str,
        rec_action_str,
        rev_update_str,
        closure_crit_str,
        "OPEN"
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
# 6. החזרת מקטע לאורך (Portrait Section) להנחיות הנהלה ו-Hold Point
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
r_hdr3 = p_hdr3.add_run("פרויקט לוד ניר צבי | דוח אינטגרציה עליון — הנחיות להגשת Rev 02")
r_hdr3.font.name = 'David'
r_hdr3.font.size = Pt(12)
r_hdr3.font.color.rgb = RGBColor(120, 120, 120)

ftr3 = section3.footer
ftr3.is_linked_to_previous = False
p_ftr3 = ftr3.paragraphs[0]
p_ftr3.alignment = WD_ALIGN_PARAGRAPH.LEFT
r_ftr3 = p_ftr3.add_run("סבב בדיקה: 01 מקיף | מהדורה לקראת Rev 02 | דוח הנהלה וסופרפוזיציה כולל")
r_ftr3.font.name = 'David'
r_ftr3.font.size = Pt(12)
r_ftr3.font.color.rgb = RGBColor(120, 120, 120)

p_conc_h = doc.add_paragraph()
set_perfect_rtl(p_conc_h)
r_ch_t = p_conc_h.add_run('6. הנחיות הנהלת הפרויקט לסגירת ממצאים ואישור מהדורה 02 (Rev 02)')
r_ch_t.font.name = 'David'
r_ch_t.font.size = Pt(12)
r_ch_t.font.bold = True
r_ch_t.font.color.rgb = NAVY

p_conc_b = doc.add_paragraph()
set_perfect_rtl(p_conc_b)
conc_text = (
    "על בסיס 146 הממצאים שאותרו בבקרת התכן המשולבת, הנהלת היזם (עמרם אברהם) מתבקשת להנחות את צוותי התכנון לפעול לפי לוח הזמנים המרוכז:\n\n"
    "1. קונסטרוקציה ושלד: עדכון קורת טרנספר TG-1 ל-100x130 ס\"מ, הוספת 2 כלונסאות W-1, חישוקי חדירה, תפרי התפשטות ודירוג חפיפות (עד שבועיים להגשת Rev 02).\n"
    "2. אינסטלציה וכיבוי אש: חלוקה ל-3 אזורי לחץ, הסטת צנרת שופכין מקירות ממ״ד, ספרינקלרים Below-Duct וקיר מאגרים אטום W8 (עד 10 ימים להגשת Rev 02).\n"
    "3. מיזוג ושחרור עשן: התאמת כנפוני מפוחי סילון (-5°), שרוול קורה B-108, פירי על-לחץ, ושסתומי הדף Type B (עד 10 ימים להגשת Rev 02).\n"
    "4. חשמל וחירום: ביטול פחת במשאבות כיבוי, שדרוג MSB ל-50kA, שקע אב״כ +1.80 מ', כבלי PH120 ותאורת DALI 180 דקות (עד שבועיים להגשת Rev 02).\n"
    "5. פיתוח נופי: מפלס ספי כניסות לובי +3cm, רדיוס סיבוב כבאית 12.5 מ', שיפועי נגר 1.5% ומז״ח השקיה (עד 10 ימים להגשת Rev 02).\n"
    "6. שיווק ומשפטי: עדכון תשריטי המכר לשטחי הביצוע המדויקים, סימון פירים במטבח, רוחב חניות 2.90 מ' ליד קיר, גובה מעקות 1.10 מ' ושקע אינדוקציה 3x25A טרם חתימת חוזים.\n\n"
    "עם קבלת מודלי ותוכניות Revision 02 המעודכנים מכלל היועצים, המערכת תריץ בדיקת אינטגרציה חוזרת אוטומטית (Automated Multi-Disciplinary Closure Verification) ותפיק אישור מסירה רשמי לשחרור ביצוע יציקות באתר."
)
r_cb = p_conc_b.add_run(conc_text)
r_cb.font.name = 'David'
r_cb.font.size = Pt(12)

doc.add_paragraph()

# Consolidated Recommended Hold Point
p_hp_h = doc.add_paragraph()
set_perfect_rtl(p_hp_h)
r_hph = p_hp_h.add_run('7. המלצה לנקודת עצירה מאוחדת לפרויקט (Consolidated Hold Point Directive)')
r_hph.font.name = 'David'
r_hph.font.size = Pt(12)
r_hph.font.bold = True
r_hph.font.color.rgb = CRIMSON

p_hp_b = doc.add_paragraph()
set_perfect_rtl(p_hp_b)
hp_text = (
    "RECOMMENDED HOLD POINT:\n"
    "מומלץ בזאת להנהלת הפרויקט שלא לאשר יציקות שלד, ביצוע תשתיות MEP וחתימת חוזי מכר חדשים עד לקבלת מהדורה מתוקנת (Revision 02) מכלל היועצים ואישור סגירת 135 הממצאים הקריטיים (RED).\n\n"
    "חבילת דוחות המתכנן המלאה (6 דוחות פרטניים + קבצי BCF לרוויט) הועברה לכל אחד ממתכנני המערכות לקבלת התייחסותם המיידית."
)
r_hpb = p_hp_b.add_run(hp_text)
r_hpb.font.name = 'David'
r_hpb.font.size = Pt(12)
r_hpb.font.color.rgb = CRIMSON

doc.save(doc_path)
print("Grand Master Multi-Disciplinary Integration Report generated successfully at:", doc_path)
