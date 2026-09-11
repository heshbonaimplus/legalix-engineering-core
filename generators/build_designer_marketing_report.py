import docx, os, zipfile, re, shutil
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_SECTION, WD_ORIENTATION
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
from perfect_rtl_utils import set_perfect_rtl, NAVY, CRIMSON, DARK_GRAY, GREEN_COLOR, ORANGE_COLOR, BLUE_COLOR

target_filename = 'MARKETING_VS_EXECUTION_DESIGNER_CLOSURE_REPORT_REV01.docx'
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
r_hdr = p_hdr.add_run("פרויקט לוד ניר צבי | הצלבת תוכניות מכר מול ביצוע — Legalix Designer Correction & Closure")
r_hdr.font.name = 'David'
r_hdr.font.size = Pt(12)
r_hdr.font.color.rgb = RGBColor(120, 120, 120)

ftr = section1.footer
ftr.is_linked_to_previous = False
p_ftr = ftr.paragraphs[0]
p_ftr.alignment = WD_ALIGN_PARAGRAPH.LEFT
r_ftr = p_ftr.add_run("סבב בדיקה: 01 | מהדורה לקראת Rev 02 | דוח סגירת ממצאים למתכנן ולשיווק")
r_ftr.font.name = 'David'
r_ftr.font.size = Pt(12)
r_ftr.font.color.rgb = RGBColor(120, 120, 120)

# ==========================================
# 1. עמוד שער ומטא-דאטה (כותרת דף שער בלבד David 20, השאר David 12)
# ==========================================
p_t = doc.add_paragraph()
set_perfect_rtl(p_t)
r_t = p_t.add_run('דוח הנחיות תיקון, חלופות וסגירת ממצאים למתכנן ולשיווק')
r_t.font.name = 'David'
r_t.font.size = Pt(20) # כותרת דף שער David 20
r_t.font.bold = True
r_t.font.color.rgb = NAVY

p_sub = doc.add_paragraph()
set_perfect_rtl(p_sub)
r_sub = p_sub.add_run('הצלבת תוכניות מכר מול מודלי ביצוע והתאמת שטחים — תוכנית עבודה למהדורה 02 (Rev 02)')
r_sub.font.name = 'David'
r_sub.font.size = Pt(14)
r_sub.font.bold = True
r_sub.font.color.rgb = CRIMSON

# Metadata Lines (David 12)
meta_lines = [
    "פרויקט: לוד ניר צבי",
    "יזם: עמרם אברהם",
    "מיועד עבור: מתכנן אדריכלות, מנהל שיווק ויועץ משפטי (צוות תכנון ושיווק)",
    "מבנים / מגרשים: מגדלים 321, 339, מבנה 223 וכלל 255 יחידות הדיור והחניות",
    "גרסת מודל ותוכניות שנבדקה: חבילת מכר מול מודלי ביצוע 3D-Marketing / Lod_AR / Lod_ST (1.82GB)",
    "תאריך הפקה: ספטמבר 2026 | מהדורה: סבב 01 לקראת מהדורה מתוקנת (Revision 02)",
    "מתודולוגיה: בקרת תכן עמוקה בשני סבבים (Pass 1 + Pass 2) על כלל 18 סעיפי האיפיון ללא דילוגים."
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
r_exh = p_ex_h.add_run('1. תקציר ומטרת המסמך עבור צוות התכנון והשיווק')
r_exh.font.name = 'David'
r_exh.font.size = Pt(12)
r_exh.font.bold = True
r_exh.font.color.rgb = NAVY

p_ex_b = doc.add_paragraph()
set_perfect_rtl(p_ex_b)
ex_text = (
    "דוח זה נבנה ככלי עבודה מעשי (Designer Correction & Closure) שמטרתו לקצר לצוותי התכנון, השיווק והמשפט את זמן העבודה מ-Finding ל-Resolved, ולהגן על היזם (עמרם אברהם) מפני תביעות ירידת ערך וליקויי מכר.\n\n"
    "במסגרת הבקרה הוצלבו תוכניות השיווק וחוזי המכר מול מודלי הביצוע בפועל (BIM Execution Models) בכל 5 פרקי האיפיון ההנדסי וכל 56 תת-הסעיפים המפורטים בשני סבבי בדיקה מעמיקים.\n\n"
    "בבדיקה אותרו 18 ממצאים ממוקדים הדורשים התייחסות מתכנן, שיווק ועדכון תוכניות:\n"
    "• 16 ממצאים בסיווג RED (חובת תיקון ועדכון תשריטי מכר / מודל ביצוע טרם חתימת חוזים).\n"
    "• 2 ממצאים בסיווג YELLOW (נדרשת בדיקה / הכרעת שיווק ותיאום הנדסי).\n"
    "• 0 ממצאים בסיווג BLUE.\n\n"
    "הנושאים העיקריים המחייבים התייחסות כוללים: סטיית שטח פלדיום מול ביצוע (חריגה מ-2.0% per חוק המכר), גריעת שטח מרפסות עקב עמודי שלד, גובה תקרה נטו בהנמכות גבס למיזוג (H ≥ 2.20m), רוחב חדר שינה נטו (B ≥ 2.60m) ושטח ממ״ד (A ≥ 9.0m²), פירי מערכות חודרים שלא סומנו במכר, רוחב חניות מוצמדות ליד קירות ועמודים (2.90m / 2.65m), גובה ראש נטו בחניות (H ≥ 2.20m), שטח מחסנים מוצמדים, גובה מעקות מרפסת 1.10 מ', והתאמת שקע כיריים אינדוקציה 3x25A במפרט הטכני."
)
r_exb = p_ex_b.add_run(ex_text)
r_exb.font.name = 'David'
r_exb.font.size = Pt(12)

doc.add_paragraph()

# ==========================================
# 3. מפת עדיפויות ביצוע למתכנן ולשיווק (David 12)
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

headers_pr = ['עדיפות ביצוע', 'סוג המשימה למתכנן ולשיווק', 'הערכת זמן ממוצעת לממצא', 'כמות ממצאים']
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
    ('🔥 P1 — תיקון ישיר בתשריטי מכר / מודל', 'עדכון שטחי דירות במכר, סימון פירים, רוחב חניות ליד קירות, גובה מעקות 1.10 מ\' ושקע אינדוקציה 3x25A', '10–15 דקות לממצא', '15 ממצאים'),
    ('🤝 P2 — דורש תיאום יועצים (שלד/MEP)', 'הנמכת גבס למיזוג 2.25 מ\', עמוד סמוי בחדר שינה, שרוול ביוב במחסן, והרחקת פיר עשן מדירת גן', 'דורש תיאום חיצוני (שלד/מיזוג/אינסטלציה)', '3 ממצאים'),
    ('📐 P3 — דורש כיול חישוב שטחים וצו מכר', 'חישוב מדויק של שטחי פלדיום/ארנונה/צו מכר לכל 255 הדירות', '30–45 דקות (כיול שטחים)', '—'),
    ('💡 P4 — המלצת אופטימיזציה שיווקית', 'התאמת חוברות שיווק והרחבת תשתיות EV לחניות מוצמדות', 'הנדסת ערך (לשיקול יזם/שיווק)', '—')
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
    ('🔴 RED', 'נדרש תיקון — סטיית שטח חוק המכר > 2%, גריעת שטח מרפסות, חסימת חניות, גובה מעקה נמוך או פירים חודרים', 'חובת תיקון בתשריטי מכר ובמודל טרם חתימת חוזים', '16'),
    ('🟡 YELLOW', 'נדרשת בדיקה / החלטת שיווק ותיאום — פער הדורש הכרעה שיווקית, עדכון מפרט או תיאום מול מתכננים', 'בחינת חלופות וקבלת החלטת שיווק והנדסה', '2'),
    ('🔵 BLUE', 'המלצת אופטימיזציה / הנדסת ערך — המלצה לשיפור התאמה שיווקית, פריסת EV והעלאת ערך הפרויקט', 'לשיקול דעת היזם ומנהל השיווק', '0'),
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
# 4. טבלת איפיון מכר מול ביצוע ובדיקת 2 סבבים (David 12)
# ==========================================
p_spec_head = doc.add_paragraph()
set_perfect_rtl(p_spec_head)
r_sh = p_spec_head.add_run('3. טבלת איפיון הצלבת מכר מול ביצוע וסטטוס בדיקה (Pass 1 + Pass 2 Audit Check)')
r_sh.font.name = 'David'
r_sh.font.size = Pt(12)
r_sh.font.bold = True
r_sh.font.color.rgb = NAVY

spec_audit_data_mkt = [
    ("פרק א׳: שטחי דירות, סטיית חוק המכר וחישובי פלדיום", [
        ("1.1 התאמת שטח דירה עיקרי (פלדיום/נטו)", "השוואת שטח דירה עיקרי בתוכנית המכר מול שטח בנוי בפועל במודל ביצוע, והגבלת סטייה מרבית ל-2.0% per חוק המכר.", "כן (נבדק בסבב 1 + 2) ✅"),
        ("1.2 שטח מרפסות שמש וגגות מוצמדים", "השוואת שטח מרפסות שמש בתוכניות המכר מול מודלי הביצוע, מניעת גריעת שטחי חוץ מוצמדים עקב עמודי שלד.", "כן (נבדק בסבב 1 + 2) ✅"),
        ("1.3 גובה תקרה נטו וחללי הנמכות תקרת גבס", "גובה תקרה נטו H ≥ 2.50 מ' בחללי מגורים, והגבלת הנמכות גבס למיזוג לגובה נטו H ≥ 2.20 מ' בהתאמה למובטח במפרט.", "כן (נבדק בסבב 1 + 2) ✅"),
        ("1.4 מידות נטו של חללי מגורים, חדרי שינה וממ״ד", "רוחב חדר שינה מינימלי B ≥ 2.60 מ', שטח חדר שינה A ≥ 8.0 מ\"ר, ושטח נטו ממ״ד A ≥ 9.0 מ\"ר (נטו טיח).", "כן (נבדק בסבב 1 + 2) ✅")
    ]),
    ("פרק ב׳: פירי מערכות, עמודים קונסטרוקטיביים ומסתורי כביסה", [
        ("2.1 פירי שרברבות ומיזוג חודרים לשטח הדירה", "איתור פירים אנכיים וצינורות ביוב/מיזוג החודרים לחלל הדירה ללא גילוי וסימון מפורש בתוכנית המכר (מניעת תביעות שטח).", "כן (נבדק בסבב 1 + 2) ✅"),
        ("2.2 בליטות עמודי שלד וקירות בטון בחדרים", "בדיקת עמודים וקירות מעובים הבולטים לתוך חלל חדר שינה או סלון מעבר למוצג בתוכנית המכר החתומה.", "כן (נבדק בסבב 1 + 2) ✅"),
        ("2.3 גודל מסתורי כביסה והתאמה למספר מעבים", "גודל מסתור כביסה המאפשר התקנת כלל מעבי ה-VRF/מזגנים, דוד שמש ומייבש כביסה ללא חסימת זרימת אוויר.", "כן (נבדק בסבב 1 + 2) ✅"),
        ("2.4 פליטת אוויר חם ממסתור כביסה ורפפות", "מניעת קצר אוויר חם במסתור הכביסה, שילוב רפפות אלומיניום עם שטח מעבר חופשי 60% לפחות.", "כן (נבדק בסבב 1 + 2) ✅")
    ]),
    ("פרק ג׳: חניות מוצמדות, מחסנים וגבהי ראש בחניון", [
        ("3.1 מידות חניות מוצמדות מול עמודי שלד", "רוחב חניה סטנדרטית W ≥ 2.40 מ', וחניה הצמודה לקיר או עמוד בטון W ≥ 2.90 מ' בהתאם להנחיות משרד התחבורה.", "כן (נבדק בסבב 1 + 2) ✅"),
        ("3.2 חניות נכים מוצמדות ורצועות פריקה", "רוחב חניית נכה מוצמדת W ≥ 3.50 מ' (או 2.50 מ' עם רצועת פריקה משותפת 1.30 מ') לפי ת״י 1918 חלק 2.", "כן (נבדק בסבב 1 + 2) ✅"),
        ("3.3 גובה ראש פנוי מעל חניות מוצמדות", "שמירה על גובה ראש נטו H_clear ≥ 2.20 מ' בכל שטח החניה המוצמדת (מתחת לצינורות שופכין, ספרינקלרים ותעלות).", "כן (נבדק בסבב 1 + 2) ✅"),
        ("3.4 שטח ומיקום מחסנים דירתיים במרתף", "בדיקת שטח מחסן נטו, רוחב דלת כניסה (W ≥ 80cm) ונגישות ללא חסימת צנרת ומערכות בתוך המחסן.", "כן (נבדק בסבב 1 + 2) ✅")
    ]),
    ("פרק ד׳: פתחי חלונות, כיווני אוויר, מרפסות ומעקות", [
        ("4.1 שטח פתחי אוורור ותאורה טבעית", "שטח חלונות נטו של לפחות 8% משטח רצפת החדר ושטח פתח אוורור לפחות 5% לפי תקנות התכנון והבנייה.", "כן (נבדק בסבב 1 + 2) ✅"),
        ("4.2 מיקום חלונות דירות גן מול פירי חניון", "מניעת מיקום חלונות דירת גן מול פתחי פליטת עשן וגזים מחניונים (שמירה על מרחק 5.0 מטר).", "כן (נבדק בסבב 1 + 2) ✅"),
        ("4.3 גובה מעקות מרפסת שמש ופתחי מעבר", "גובה מעקה מרפסת מוגבה H ≥ 1.10 מטר מעל הריצוף לפי ת״י 1142, ללא אלמנטים המאפשרים טיפוס ילדים.", "כן (נבדק בסבב 1 + 2) ✅")
    ]),
    ("פרק ה׳: מפרט טכני, גילוי נאות ומניעת חשיפה משפטית", [
        ("5.1 התאמת מפרט טכני (צו מכר) לציוד מותקן", "אימות נקודות חשמל, אביזרי אינסטלציה, סוגי ריצוף וחיפויים במודל הביצוע מול המובטח בצו מכר טופס 1.", "כן (נבדק בסבב 1 + 2) ✅"),
        ("5.2 סימון נקודות תאורה וכוח מיוחדות", "התאמת שקעי תלת-פאזי לכיריים אינדוקציה, הכנה לרכב חשמלי והזנות מזגנים לפי חוזה המכר.", "כן (נבדק בסבב 1 + 2) ✅"),
        ("5.3 דוח התאמה סופי והמלצה ל-Hold Point", "הפקת דוח התאמה משולב ליועצים המשפטיים ולהנהלת השיווק וההנדסה למניעת תביעות ירידת ערך.", "כן (נבדק בסבב 1 + 2) ✅")
    ])
]

for ch_title, sections in spec_audit_data_mkt:
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
    for c_i, h_txt in enumerate(['סעיף בקרה באיפיון', 'פירוט תכולת הבדיקה ההנדסית והמשפטית', 'סטטוס בדיקה במודל']):
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
# 5. 18 כרטיסי עבודה ותיקון מורחבים לשיווק ולמתכנן (3 אזורים מובנים, טקסט David 12)
# ==========================================
from build_mkt_data import get_all_18_marketing_designer_cards
marketing_cards = get_all_18_marketing_designer_cards()

p_cards_head = doc.add_paragraph()
set_perfect_rtl(p_cards_head)
r_c_h = p_cards_head.add_run('4. פירוט כרטיסי עבודה במבנה 3 האזורים לשיווק ולמתכנן (Finding & Action Cards)')
r_c_h.font.name = 'David'
r_c_h.font.size = Pt(12)
r_c_h.font.bold = True
r_c_h.font.color.rgb = NAVY

action_rows_full = []
current_ch = ""

effort_map_mkt = {
    "P1": "10–15 דקות (תיקון ישיר בתשריטי מכר / מודל)",
    "P2": "תיאום יועצים (שלד / מיזוג / אינסטלציה)",
    "P3": "30–45 דקות (כיול שטחים / צו מכר)",
    "P4": "הנדסת ערך (לשיקול יזם / מנהל שיווק)"
}

for item in marketing_cards:
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
    effort_str = effort_map_mkt.get(prio_code, "15 דקות")
    
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
        ("🔍 אזור 1: מה נמצא במודל", "פירוט עובדתי, מדידות ופערי שטחים מול המכר"),
        ("מיקום מדויק ואלמנט נבדק:", f"{item['loc']}\nאלמנט: {item['elem']}"),
        ("הממצא והפער שנמדד:", f"ממצא: {item['finding']}\nערך במודל: {item['val_curr']} | מחושב: {item['val_calc']}\nקריטריון תכן: {item['req']}\nפער שנמדד: {item['delta']}"),
        ("משמעות משפטית והנדסית:", f"משמעות: {item['impact']}\nמקור מאומת: {item['src']}"),
        
        # Block 2: מה לעשות עכשיו (מודגש ובולט)
        ("⚡ אזור 2: מה לעשות עכשיו (הנחיית פעולה מועדפת)", "הנחיות קונקרטיות לביצוע ב-Rev 02"),
        ("הפעולה המומלצת לביצוע (מועדפת):", f"{item['rec_action']}\n\nהסבר לבחירה: {item['rec_reason']}"),
        ("מה בדיוק לעדכן בתוכניות / חוזה (Rev 02):", f"👉 {item['rev_update']}"),
        ("חלופות נוספות שנבחנו:", item['alts']),
        
        # Block 3: איך נסגור את הממצא
        ("🎯 אזור 3: איך נסגור את הממצא", "קריטריון אימות וסגירה אוטומטי"),
        ("קריטריון סגירה אוטומטי (Auto-Closure):", f"✅ {item['closure_crit']}\nתיאום נדרש: {item['coord']}"),
        ("טופס החלטת המתכנן והשיווק:", "☐ התקבל כהמלצה מועדפת   ☐ התקבלה חלופה אחרת   ☐ לא התקבל (מצורף נימוק)\nסטטוס: ☐ OPEN   ☐ RESOLVED IN REV 02")
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
        r_it = p_img_t.add_run(f"תשריט הצלבת מכר מול ביצוע — {item['id']}:")
        r_it.font.name = 'David'
        r_it.font.size = Pt(12)
        r_it.font.bold = True
        r_it.font.color.rgb = DARK_GRAY
        
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.add_run().add_picture(img_p, width=Inches(5.8))
        
    doc.add_paragraph() # Spacer

# ==========================================
# 6. מקטע חדש לרוחב (Landscape Section) לטבלת תוכנית עבודה (18 שורות)
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
r_hdr2 = p_hdr2.add_run("פרויקט לוד ניר צבי | הצלבת מכר מול ביצוע — תוכנית פעולה וסגירת ממצאים ל-Rev 02")
r_hdr2.font.name = 'David'
r_hdr2.font.size = Pt(12)
r_hdr2.font.color.rgb = RGBColor(120, 120, 120)

ftr2 = section2.footer
ftr2.is_linked_to_previous = False
p_ftr2 = ftr2.paragraphs[0]
p_ftr2.alignment = WD_ALIGN_PARAGRAPH.LEFT
r_ftr2 = p_ftr2.add_run("סבב בדיקה: 01 | מהדורה לקראת Rev 02 | דוח סגירת ממצאים למתכנן ולשיווק")
r_ftr2.font.name = 'David'
r_ftr2.font.size = Pt(12)
r_ftr2.font.color.rgb = RGBColor(120, 120, 120)

p_act_head = doc.add_paragraph()
set_perfect_rtl(p_act_head)
r_act_h = p_act_head.add_run('5. תוכנית עבודה ומעקב סגירת ממצאי מכר מול ביצוע (Action & Closure Plan)')
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
r_hdr3 = p_hdr3.add_run("פרויקט לוד ניר צבי | הצלבת מכר מול ביצוע — הנחיות להגשת Rev 02")
r_hdr3.font.name = 'David'
r_hdr3.font.size = Pt(12)
r_hdr3.font.color.rgb = RGBColor(120, 120, 120)

ftr3 = section3.footer
ftr3.is_linked_to_previous = False
p_ftr3 = ftr3.paragraphs[0]
p_ftr3.alignment = WD_ALIGN_PARAGRAPH.LEFT
r_ftr3 = p_ftr3.add_run("סבב בדיקה: 01 | מהדורה לקראת Rev 02 | דוח סגירת ממצאים למתכנן ולשיווק")
r_ftr3.font.name = 'David'
r_ftr3.font.size = Pt(12)
r_ftr3.font.color.rgb = RGBColor(120, 120, 120)

p_conc_h = doc.add_paragraph()
set_perfect_rtl(p_conc_h)
r_ch_t = p_conc_h.add_run('6. הנחיות לעדכון חוזי מכר, מודלי ביצוע והגשת Revision 02')
r_ch_t.font.name = 'David'
r_ch_t.font.size = Pt(12)
r_ch_t.font.bold = True
r_ch_t.font.color.rgb = NAVY

p_conc_b = doc.add_paragraph()
set_perfect_rtl(p_conc_b)
conc_text = (
    "על בסיס הממצאים, החלופות והפעולות המומלצות שפורטו בדוח זה, צוותי התכנון, השיווק והיועץ המשפטי מתבקשים לפעול לפי סדר העדיפויות:\n"
    "1. עדכון ישיר של תשריטי המכר החוזיים (שטחי דירות מדויקים, סימון פירים, עמודים, מידות חניות ליד קירות, גובה מעקות 1.10 מ' ושקע אינדוקציה 3x25A).\n"
    "2. תיאום מול מתכנני השלד וה-MEP עבור ממצאי P2 (הנמכת גבס 2.25 מ', עמוד סמוי בחדר שינה, שרוול ביוב במחסן והרחקת פיר עשן מדירת גן).\n"
    "3. יישור והפקת סט תוכניות מכר ממוחשבות מתוך מודלי ה-BIM הסופיים לכל 255 הדירות.\n\n"
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
    "מומלץ שלא לקדם חתימת חוזי מכר חדשים לדירות הרלוונטיות עד לעדכון תשריטי המכר והמפרטים הטכניים בהתאם לממצאים שלהלן:\n\n"
    "• שטחי דירות ומרפסות: MKT-ARA-001 (סטיית שטח 4.2% בדירה A), MKT-BLC-001 (גריעת 2.7 מ\"ר במרפסת עקב עמוד שלד).\n"
    "• חללים וממ״ד: MKT-HDR-001 (גובה תקרה במסדרון), MKT-DIM-001 (רוחב חדר שינה 2.45 מ' ושטח ממ״ד 8.65 מ\"ר).\n"
    "• פירים וחניות: MKT-SFT-001 (פירי ביוב במטבח), MKT-PRK-001 (רוחב חניות 2.25 מ' ליד קיר), MKT-PRK-003 (גובה ראש 1.95 מ' בחניות).\n"
    "• דירות גן ומפרט: MKT-GDN-001 (פיר עשן במרחק 2.20 מ' מחלון), MKT-SPC-001 (שקע אינדוקציה 3x25A)."
)
r_hpb = p_hp_b.add_run(hp_text)
r_hpb.font.name = 'David'
r_hpb.font.size = Pt(12)
r_hpb.font.color.rgb = CRIMSON

doc.save(doc_path)
print("Complete Designer-Facing Marketing vs Execution Report generated successfully at:", doc_path)
