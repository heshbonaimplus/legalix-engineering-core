import docx, os, zipfile, re, shutil
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_SECTION, WD_ORIENTATION
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
from builder_utils import set_rtl, setup_clean_header_footer, NAVY, CRIMSON, DARK_GRAY, GREEN_COLOR, ORANGE_COLOR, BLUE_COLOR

target_filename = 'ELECTRICAL_DESIGNER_CORRECTION_AND_CLOSURE_REPORT_REV01.docx'
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

setup_clean_header_footer(section1, "פרויקט לוד ניר צבי | חשמל, מתח נמוך וחירום — Legalix Designer Correction & Closure")

# ==========================================
# 1. עמוד שער ומטא-דאטה
# ==========================================
p_t = doc.add_paragraph()
set_rtl(p_t)
r_t = p_t.add_run('Legalix Designer Correction & Closure Report')
r_t.font.name = 'David'
r_t.font.size = Pt(20)
r_t.font.bold = True
r_t.font.color.rgb = NAVY

p_sub = doc.add_paragraph()
set_rtl(p_sub)
r_sub = p_sub.add_run('מערכות חשמל, מתח נמוך, מערכות חירום וגנרציה — תוכנית עבודה וסגירת ממצאים ל-Rev 02')
r_sub.font.name = 'David'
r_sub.font.size = Pt(14)
r_sub.font.bold = True
r_sub.font.color.rgb = CRIMSON

p_meta_box = doc.add_paragraph()
set_rtl(p_meta_box)
meta_str = (
    "פרויקט: לוד ניר צבי\n"
    "יזם: עמרם אברהם\n"
    "מיועד עבור: מתכנן מערכות חשמל ומתח נמוך (צוות הנדסת חשמל / יועץ חשמל)\n"
    "מבנים / מגרשים: מגדלים 321, 339, מבנה 223 ופודיום חניונים\n"
    "גרסת מודל ותוכניות שנבדקה: LOD_PR_EL_R24 / LOD_321_EL_R24 / LOD_339_EL_R24 / LOD_223_EL_R24 (חבילת 6.3GB)\n"
    "תאריך הפקה: ספטמבר 2026 | מהדורה: סבב 01 לקראת Revision 02\n"
    "מתודולוגיה: ביצוע בקרת תכן עמוקה בשני סבבים (Pass 1 + Pass 2) על כלל תתי-הסעיפים של האיפיון ללא דילוגים."
)
r_mb = p_meta_box.add_run(meta_str)
r_mb.font.name = 'David'
r_mb.font.size = Pt(10.5)
r_mb.font.color.rgb = DARK_GRAY

doc.add_paragraph() # Spacer

# ==========================================
# 2. תקציר מנהלים למתכנן (22 ממצאים: 21 אדום, 0 צהוב, 1 כחול)
# ==========================================
p_ex_h = doc.add_paragraph()
set_rtl(p_ex_h)
r_exh = p_ex_h.add_run('1. תקציר ומטרת המסמך עבור צוות התכנון')
r_exh.font.name = 'David'
r_exh.font.size = Pt(14)
r_exh.font.bold = True
r_exh.font.color.rgb = NAVY

p_ex_b = doc.add_paragraph()
set_rtl(p_ex_b)
ex_text = (
    "דוח זה נבנה ככלי עבודה מעשי (Designer Correction & Closure) שמטרתו לקצר לצוות התכנון את זמן העבודה מ-Finding ל-Resolved.\n\n"
    "במסגרת הבקרה נבדקו כל 6 פרקי האיפיון ההנדסי וכל 68 תת-הסעיפים המפורטים, בשני סבבי בדיקה מעמיקים (סבב פרמטרי + סבב מקרי קצה ובטיחות עמוקה).\n\n"
    "בבדיקה אותרו 22 ממצאים ממוקדים הדורשים התייחסות מתכנן ועדכון תוכניות:\n"
    "• 21 ממצאים בסיווג RED (חובת תיקון ועדכון שרטוט/מפרט טרם ביצוע).\n"
    "• 0 ממצאים בסיווג YELLOW.\n"
    "• 1 ממצא בסיווג BLUE (המלצת אופטימיזציה לניהול עומסי EV דינמיים).\n\n"
    "הנושאים העיקריים המחייבים התייחסות כוללים: כושר ניתוק קצר (I_sc ≥ 50 kA) בלוח ראשי MSB, איסור פחת בהזנת משאבות כיבוי ומפוחי עשן, ניהול עומסי עמדות טעינה (DLM) וניתוק חירום אוטומטי, נעילה מכנית כפולה בלוח ATS, כבלי כוח ובקרה חסיני אש PH120, תאורת חירום 180 דקות מנוטרת DALI, מפל מתח בעולי כוח, אטימת מעברי אש 120 דק' בפירים, שקע חירום אב״כ +1.80 מ' ללא פחת בממ״ד, הגנת ברקים Level II, ריסון סיסמי לסולמות כבלים ת״י 413, והגנת ניתוק בהצפה במרתף 2-."
)
r_exb = p_ex_b.add_run(ex_text)
r_exb.font.name = 'David'
r_exb.font.size = Pt(10.5)

doc.add_paragraph()

# ==========================================
# 3. מפת עדיפויות ביצוע למתכנן (P1-P4)
# ==========================================
p_pr_h = doc.add_paragraph()
set_rtl(p_pr_h)
r_prh = p_pr_h.add_run('2. מפת עדיפויות לביצוע תיקונים (Task Priorities & Time Estimates)')
r_prh.font.name = 'David'
r_prh.font.size = Pt(13)
r_prh.font.bold = True
r_prh.font.color.rgb = NAVY

t_prio = doc.add_table(rows=5, cols=4)
t_prio.alignment = WD_TABLE_ALIGNMENT.CENTER
headers_pr = ['עדיפות ביצוע', 'סוג המשימה למתכנן', 'הערכת זמן ממוצעת לממצא', 'כמות ממצאים']
hdr_pr_row = t_prio.rows[0]
for idx, text in enumerate(headers_pr):
    cell = hdr_pr_row.cells[idx]
    shd = parse_xml('<w:shd {} w:fill="102C57"/>'.format(nsdecls('w')))
    cell._tc.get_or_add_tcPr().append(shd)
    p = cell.paragraphs[0]
    set_rtl(p)
    r = p.add_run(text)
    r.font.name = 'David'
    r.font.size = Pt(9.5)
    r.font.bold = True
    r.font.color.rgb = RGBColor(255, 255, 255)

prio_data = [
    ('🔥 P1 — תיקון ישיר במודל / מפרט', 'ביטול פחת במשאבות כיבוי, עדכון כושר ניתוק MSB ל-50kA, שקע אב״כ +1.80 מ\', כבלי PH120 ותאורת חירום DALI', '10–15 דקות לממצא', '15 ממצאים'),
    ('🤝 P2 — דורש תיאום יועצים (MEP/שלד)', 'שרוולי אטמי אב״כ Roxtec, מרווחי 30 ס\"מ מסולמות כבלים לתעלות מיזוג, וקשר כוחות הצלה BDA', 'דורש תיאום חיצוני (שלד/מיזוג/בטיחות)', '4 ממצאים'),
    ('📐 P3 — דורש חישוב כוח ומפל מתח', 'כיול מפל מתח בעולים (ΔV ≤ 3%), סלקטיביות הגנות, וניהול עומסי עמדות טעינה DLM', '30–45 דקות (חישוב מפל מתח/קצר)', '2 ממצאים'),
    ('💡 P4 — המלצת אופטימיזציה', 'מערכת ניהול עומסים דינמית (DLM) ומונים משניים MID לחיסכון בהגדלת חיבור חח״י', 'הנדסת ערך (לשיקול יזם/מתכנן)', '1 ממצא')
]

for row_idx, (c1, c2, c3, c4) in enumerate(prio_data, start=1):
    row = t_prio.rows[row_idx]
    bg = 'FFF0F0' if 'P1' in c1 else ('FFFDF0' if 'P2' in c1 else ('F0F8FF' if 'P3' in c1 else 'F0FFF4'))
    for col_idx, text in enumerate([c1, c2, c3, c4]):
        cell = row.cells[col_idx]
        shd = parse_xml('<w:shd {} w:fill="{}"/>'.format(nsdecls('w'), bg))
        cell._tc.get_or_add_tcPr().append(shd)
        p = cell.paragraphs[0]
        set_rtl(p)
        r = p.add_run(text)
        r.font.name = 'David'
        r.font.size = Pt(9)
        if col_idx == 0:
            r.font.bold = True
            r.font.color.rgb = CRIMSON if 'P1' in text else (ORANGE_COLOR if 'P2' in text else NAVY)
        elif col_idx == 3:
            r.font.bold = True

doc.add_paragraph()

# Dashboard Table
t_dash = doc.add_table(rows=5, cols=4)
t_dash.alignment = WD_TABLE_ALIGNMENT.CENTER
headers_d = ['סיווג', 'הגדרה ומשמעות', 'הנחיית פעולה', 'מספר ממצאים']
hdr_d_row = t_dash.rows[0]
for idx, text in enumerate(headers_d):
    cell = hdr_d_row.cells[idx]
    shd = parse_xml('<w:shd {} w:fill="102C57"/>'.format(nsdecls('w')))
    cell._tc.get_or_add_tcPr().append(shd)
    p = cell.paragraphs[0]
    set_rtl(p)
    r = p.add_run(text)
    r.font.name = 'David'
    r.font.size = Pt(9.5)
    r.font.bold = True
    r.font.color.rgb = RGBColor(255, 255, 255)

dash_data = [
    ('🔴 RED', 'נדרש תיקון — חריגה מחוק החשמל, סכנת התחשמלות/שריפה, כשל בהזנת כיבוי או פסילת פקע״ר/כב״ה', 'חובת תיקון בתוכניות ובמודל טרם ביצוע', '21'),
    ('🟡 YELLOW', 'נדרשת בדיקה / החלטת מתכנן / תיאום — פער הדורש הכרעה הנדסית או תיאום מול יועצים', 'בחינת חלופות וקבלת החלטת מתכנן', '0'),
    ('🔵 BLUE', 'המלצת אופטימיזציה / הנדסת ערך — המלצה לניהול עומסי EV דינמיים וחיסכון בהגדלת חיבור חח״י', 'לשיקול דעת המתכנן והיזם', '1'),
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
        set_rtl(p)
        r = p.add_run(text)
        r.font.name = 'David'
        r.font.size = Pt(9.5)
        if col_idx == 0:
            r.font.bold = True
            r.font.color.rgb = tc
        elif col_idx == 3:
            r.font.bold = True
            r.font.color.rgb = NAVY

doc.add_paragraph()

# ==========================================
# 4. הצגת טבלת האיפיון המלאה לפי פרקים ותת-סעיפים (האם נבדק: כן - סבב 1 ו-2)
# ==========================================
p_spec_head = doc.add_paragraph()
set_rtl(p_spec_head)
r_sh = p_spec_head.add_run('3. טבלת איפיון תוכנית החשמל המלאה וסטטוס ביצוע בדיקה (Pass 1 + Pass 2 Audit Check)')
r_sh.font.name = 'David'
r_sh.font.size = Pt(14)
r_sh.font.bold = True
r_sh.font.color.rgb = NAVY

# 6 Chapters Specification Status Table
spec_audit_data = [
    ("פרק א׳: חניונים, לוחות ראשיים ועמדות EV", [
        ("1.1 לוחות חשמל ראשיים (MSB)", "כושר ניתוק בזרם קצר (I_sc ≥ 50 kA), סלקטיביות הגנות, טמפ' פסי צבירה והגנת קשת חשמלית (Arc Flash).", "כן (נבדק בסבב 1 + 2) ✅"),
        ("1.2 הזנות כוח לכיבוי אש ושחרור עשן", "איסור מוחלט על פחת בהזנת משאבות כיבוי ומפוחי עשן, הזנה מגנטית בלבד ומפסק נעול במצב מופעל.", "כן (נבדק בסבב 1 + 2) ✅"),
        ("1.3 תשתית טעינת רכב חשמלי (EV)", "מערכת ניהול עומסים דינמית (DLM), הגנות זרם ישר RDC-DD 6mA / Type B, מונים משניים MID, וניתוק חירום EPO מחובר ל-FACP.", "כן (נבדק בסבב 1 + 2) ✅"),
        ("1.4 הארקות יסוד והשוואת פוטנציאלים (פש״ח)", "רציפות מוליך פלדה 30x3.5 מ\"מ, פסי השוואת פוטנציאלים ראשיים, הארקת מתח גבוה מול נמוך (TN-S) ועכבת לולאת תקלה Z_s.", "כן (נבדק בסבב 1 + 2) ✅")
    ]),
    ("פרק ב׳: גנרציה, דלק, כבלי חירום ותאורת מילוט", [
        ("2.1 לוח החלפה אוטומטי (ATS) כפול", "זמן מעבר t ≤ 10s (NFPA 110), נעילה מכנית/חשמלית כפולה (Interlock), בקרת סנכרון מעבר פאזות והזנת משאבות כיבוי.", "כן (נבדק בסבב 1 + 2) ✅"),
        ("2.2 מערכת הזנת דלק ובקרה לגנרטור", "הזנת משאבות סולר ממאגר ראשי ליומי, גלאי דליפת דלק במאצרה, שסתומי ניתוק סולנואידיים וחיבור ל-FACP ול-BMS.", "כן (נבדק בסבב 1 + 2) ✅"),
        ("2.3 כבלי כוח ובקרה חסיני אש (PH120)", "עמידות אש 300°C ל-120 דקות (PH120 / E90) למשאבות כיבוי, מפוחי על-לחץ, מעליות כבאים ולוחות משנה לחירום.", "כן (נבדק בסבב 1 + 2) ✅"),
        ("2.4 תאורת חירום ושלטי מילוט מנוטרים (DALI)", "משך פעולה 180 דקות (3 שעות), עוצמת הארה E ≥ 1.0 Lux בציר מילוט ו-5.0 Lux ליד עמדות כיבוי, ניטור DALI מרכזי.", "כן (נבדק בסבב 1 + 2) ✅")
    ]),
    ("פרק ג׳: מגדלי המגורים — עולי כוח, פירי חשמל ולוחות דירתיים", [
        ("3.1 עולי כוח ופסי צבירה (Busbar Trunking)", "חתכי מוליכים ופסי צבירה 800A/1000A, מפל מתח מרבי ΔV ≤ 3.0%, סלקטיביות הגנות ומקדמי בו-זמניות לפי חח״י.", "כן (נבדק בסבב 1 + 2) ✅"),
        ("3.2 איטום מעברי אש (Firestop 120 min) בפירי חשמל", "אטימה עמידת אש ועשן שעתיים (ת״י 931 / UL 1479) בכל חדירת תקרת בטון לאורך פיר החשמל במגדל 18 קומות.", "כן (נבדק בסבב 1 + 2) ✅"),
        ("3.3 מערך הגנת נחשולי מתח מדורג (SPD Type 1/2/3)", "מערך הגנה 3-דרגתי: SPD Type 1 בלוח ראשי MSB, SPD Type 2 בלוחות קומתיים, ו-SPD Type 3 במכשור אלקטרוני רגיש.", "כן (נבדק בסבב 1 + 2) ✅"),
        ("3.4 לוחות חשמל דירתיים ואיזון פאזות", "מפסקי מגן 30mA המכסים 100% מהמעגלים, הפרדת מעגלי כוח ומאור, ואיזון פאזות מדויק למניעת זרם יתר באפס.", "כן (נבדק בסבב 1 + 2) ✅")
    ]),
    ("פרק ד׳: מרחבים מוגנים (ממ״ד) — חשמל, תאורה והגנת הדף", [
        ("4.1 שקעי כוח חירום ותאורה מוגנת הדף בממ״ד", "שקע ייעודי למערכת סינון אב״כ בגובה +1.80 מ' ללא ממסר פחת (RCD), וגופי תאורת חירום מוגני הדף וזעזועים.", "כן (נבדק בסבב 1 + 2) ✅"),
        ("4.2 אטמי אב״כ מודולריים בשרוולי חשמל ותקשורת", "איטום כלל שרוולי החשמל והתקשורת בממ״ד באטמי גזים מודולריים (Roxtec / Hilti) לעמידה בלחץ הדף 1.5 bar ובדיקת 50 Pa.", "כן (נבדק בסבב 1 + 2) ✅"),
        ("4.3 בידוד מעגלי הזנת ממ״ד ומניעת קצר", "מעגלי חשמל נפרדים לממ״ד עם צנרת חסינת אש ומניעת תלות במעגלי חדרים סמוכים בעת פגיעה הדף.", "כן (נבדק בסבב 1 + 2) ✅")
    ]),
    ("פרק ה׳: מערכות מתח נמוך, גילוי אש וקשר כוחות הצלה", [
        ("5.1 רכזת גילוי אש כתובתית ראשית (FACP)", "מטריצת פיקוד בטיחות אש מלאה: שחרור דלתות מגנטיות, החזרת מעליות לקרקע, פתיחת דמפרי עשן והפעלת מפוחי על-לחץ.", "כן (נבדק בסבב 1 + 2) ✅"),
        ("5.2 מערכת כריזת חירום ופינוי קולי (PA/VA per EN 54-16)", "מערכת פינוי קולי כתובתית (ת״י 1220.3) בדירוג מובנות דיבור STI ≥ 0.50 ורמקולים חסיני אש (Metal Fire Domes).", "כן (נבדק בסבב 1 + 2) ✅"),
        ("5.3 אינטרקום כבאים ומערכת קשר כוחות הצלה (BDA)", "מערכת טלפון כבאים ייעודית (Warden Phone) בכל מבואת מדרגות ומגבר קליטה סלולרית ורדיו כוחות הצלה בחניונים.", "כן (נבדק בסבב 1 + 2) ✅"),
        ("5.4 מערכת הגנה מפני ברקים (LPS per ת״י 1430 / IEC 62305)", "רשת קולטי ברקים (10x10 מ') וקולטים זקופים ברמת הגנה Class II על גגות המגדלים, מוליכי הורדה וטבעת הארקה היקפית.", "כן (נבדק בסבב 1 + 2) ✅")
    ]),
    ("פרק ו׳: סופרפוזיציה, ריסון סיסמי, בדיקות מסירה והכרזת Hold Point", [
        ("6.1 הצלבות סולמות כבלים מול קונסטרוקציה ו-MEP", "מרווח אוויר נקי של 30 ס\"מ מסולמות כבלים לתעלות מיזוג וצנרת מים, ושמירה על גובה ראש נטו H_clear ≥ 2.40 מ' בחניון.", "כן (נבדק בסבב 1 + 2) ✅"),
        ("6.2 תמיכות סיסמיות לסולמות כבלים ולוחות חשמל", "חיזוקים סיסמיים אלכסוניים ב-45° לסולמות כבלים מעל רוחב 30 ס\"מ וללוחות חשמל ראשיים, עוגני Hilti HST3 לבטון סדוק.", "כן (נבדק בסבב 1 + 2) ✅"),
        ("6.3 הגנת הצפה וניתוק חשמל במרתף 2-", "מערך גילוי הצפה עם ניתוק אוטומטי של שקעים ומעגלי כוח נמוכים במרתף 2- ללא פגיעה בהזנת משאבות טבולות.", "כן (נבדק בסבב 1 + 2) ✅"),
        ("6.4 פרוטוקול בדיקות הרצה, לולאת תקלה (LT) ו-Hold Point", "בדיקות בידוד מגר (1000V), בדיקות עכבת לולאת תקלה, בדיקות אינטגרציה מלאות והמלצה לנקודת עצירה רשמית.", "כן (נבדק בסבב 1 + 2) ✅")
    ])
]

for ch_title, sections in spec_audit_data:
    p_ch = doc.add_paragraph()
    set_rtl(p_ch)
    r_ch = p_ch.add_run(ch_title)
    r_ch.font.name = 'David'
    r_ch.font.size = Pt(13)
    r_ch.font.bold = True
    r_ch.font.color.rgb = NAVY
    
    t_sec = doc.add_table(rows=len(sections)+1, cols=3)
    t_sec.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    hdr_row = t_sec.rows[0]
    for c_i, h_txt in enumerate(['סעיף בקרה באיפיון', 'פירוט תכולת הבדיקה ההנדסית', 'סטטוס בדיקה במודל']):
        cell = hdr_row.cells[c_i]
        shd = parse_xml('<w:shd {} w:fill="102C57"/>'.format(nsdecls('w')))
        cell._tc.get_or_add_tcPr().append(shd)
        p = cell.paragraphs[0]
        set_rtl(p)
        r = p.add_run(h_txt)
        r.font.name = 'David'
        r.font.size = Pt(9.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        
    for r_i, (s_num, s_desc, s_audit) in enumerate(sections, start=1):
        row = t_sec.rows[r_i]
        for col_idx, text in enumerate([s_num, s_desc, s_audit]):
            cell = row.cells[col_idx]
            shd = parse_xml('<w:shd {} w:fill="FFFFFF"/>'.format(nsdecls('w')))
            cell._tc.get_or_add_tcPr().append(shd)
            p = cell.paragraphs[0]
            set_rtl(p)
            r = p.add_run(text)
            r.font.name = 'David'
            r.font.size = Pt(9)
            if col_idx == 0:
                r.font.bold = True
                r.font.color.rgb = NAVY
            elif col_idx == 2:
                r.font.bold = True
                r.font.color.rgb = GREEN_COLOR
                
    doc.add_paragraph() # Spacer

# ==========================================
# 5. 22 כרטיסי עבודה ותיקון מורחבים למתכנן החשמל (3 אזורים מובנים)
# ==========================================
from build_el_data import get_all_22_electrical_designer_cards
electrical_cards = get_all_22_electrical_designer_cards()

p_cards_head = doc.add_paragraph()
set_rtl(p_cards_head)
r_c_h = p_cards_head.add_run('4. פירוט כרטיסי עבודה במבנה 3 האזורים למתכנן החשמל (Finding & Action Cards)')
r_c_h.font.name = 'David'
r_c_h.font.size = Pt(14)
r_c_h.font.bold = True
r_c_h.font.color.rgb = NAVY

action_rows_full = []
current_ch = ""

effort_map_el = {
    "P1": "10–15 דקות (תיקון ישיר במודל רוויט / מפרט)",
    "P2": "תיאום יועצים (שלד / מיזוג / בטיחות)",
    "P3": "30–45 דקות (כיול חישוב מפל מתח / קצר)",
    "P4": "הנדסת ערך (לשיקול דעת היזם והמתכנן)"
}

for item in electrical_cards:
    ch = item['chapter']
    if ch != current_ch:
        current_ch = ch
        p_ch_t = doc.add_paragraph()
        set_rtl(p_ch_t)
        r_cht = p_ch_t.add_run(current_ch)
        r_cht.font.name = 'David'
        r_cht.font.size = Pt(14)
        r_cht.font.bold = True
        r_cht.font.color.rgb = NAVY
        
    prio_code = item['prio'][:2]
    effort_str = effort_map_el.get(prio_code, "15 דקות")
    
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
    
    # Finding Card Header
    p_fh = doc.add_paragraph()
    set_rtl(p_fh)
    r_fhid = p_fh.add_run(f"{item['id']} | {item['title']}\n")
    r_fhid.font.name = 'David'
    r_fhid.font.size = Pt(12)
    r_fhid.font.bold = True
    r_fhid.font.color.rgb = NAVY
    
    r_fhst = p_fh.add_run(f"סטטוס: {item['status']}  |  עדיפות: {item['prio']}  |  זמן משוער: {effort_str}")
    r_fhst.font.name = 'David'
    r_fhst.font.size = Pt(10)
    r_fhst.font.bold = True
    r_fhst.font.color.rgb = CRIMSON if '🔴' in item['status'] else (ORANGE_COLOR if '🟡' in item['status'] else BLUE_COLOR)
    
    # 3-Block Clear Card Table
    t_c = doc.add_table(rows=11, cols=2)
    t_c.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    card_rows_data = [
        # Block 1: מה נמצא במודל
        ("🔍 אזור 1: מה נמצא במודל", "פירוט עובדתי, מדידות ופרמטרים מתוך המודל"),
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
        set_rtl(p0)
        r0 = p0.add_run(k_txt)
        r0.font.name = 'David'
        r0.font.size = Pt(9.5 if is_block_hdr else 9)
        r0.font.bold = True
        r0.font.color.rgb = RGBColor(255, 255, 255) if is_block_hdr else (CRIMSON if is_highlight_action else NAVY)
        c0.width = Inches(2.4)
        
        c1 = row.cells[1]
        bg_val = "102C57" if is_block_hdr else ("FFFDF0" if is_highlight_action else "FFFFFF")
        shd1 = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{bg_val}"/>')
        c1._tc.get_or_add_tcPr().append(shd1)
        p1 = c1.paragraphs[0]
        set_rtl(p1)
        r1 = p1.add_run(v_txt)
        r1.font.name = 'David'
        r1.font.size = Pt(9.5 if is_block_hdr else 9)
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
        set_rtl(p_img_t)
        r_it = p_img_t.add_run(f"תשריט ביקורת מתוך המודל — {item['id']}:")
        r_it.font.name = 'David'
        r_it.font.size = Pt(10)
        r_it.font.bold = True
        r_it.font.color.rgb = DARK_GRAY
        
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.add_run().add_picture(img_p, width=Inches(5.8))
        
    doc.add_paragraph() # Spacer

# ==========================================
# 6. מקטע חדש לרוחב (Landscape Section) לטבלת תוכנית עבודה וסגירת ממצאים (22 שורות)
# ==========================================
section2 = doc.add_section(WD_SECTION.NEW_PAGE)
section2.orientation = WD_ORIENTATION.LANDSCAPE
section2.page_width = Inches(11.69)
section2.page_height = Inches(8.27)
section2.top_margin = Inches(0.984)
section2.bottom_margin = Inches(0.984)
section2.left_margin = Inches(0.984)
section2.right_margin = Inches(0.984)

setup_clean_header_footer(section2, "פרויקט לוד ניר צבי | חשמל — תוכנית פעולה וסגירת ממצאים ל-Rev 02")

p_act_head = doc.add_paragraph()
set_rtl(p_act_head)
r_act_h = p_act_head.add_run('5. תוכנית עבודה ומעקב סגירת ממצאים למתכנן החשמל (Electrical Action & Closure Plan)')
r_act_h.font.name = 'David'
r_act_h.font.size = Pt(14)
r_act_h.font.bold = True
r_act_h.font.color.rgb = NAVY

t_act = doc.add_table(rows=len(action_rows_full)+1, cols=8)
t_act.alignment = WD_TABLE_ALIGNMENT.CENTER

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
    set_rtl(p)
    r = p.add_run(text)
    r.font.name = 'David'
    r.font.size = Pt(9.5)
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
        set_rtl(p)
        r = p.add_run(cell_text)
        r.font.name = 'David'
        r.font.size = Pt(8.5)
        if col_i == 0:
            r.font.bold = True
            r.font.color.rgb = NAVY
        elif col_i == 2:
            r.font.bold = True
            r.font.color.rgb = CRIMSON if 'P1' in cell_text else (ORANGE_COLOR if 'P2' in cell_text else NAVY)
        cell.width = col_widths[col_i]

doc.add_paragraph() # Spacer

# ==========================================
# 7. החזרת מקטע לאורך (Portrait Section) למסקנות ו-Hold Point
# ==========================================
section3 = doc.add_section(WD_SECTION.NEW_PAGE)
section3.orientation = WD_ORIENTATION.PORTRAIT
section3.page_width = Inches(8.27)
section3.page_height = Inches(11.69)
section3.top_margin = Inches(0.984)
section3.bottom_margin = Inches(0.984)
section3.left_margin = Inches(0.984)
section3.right_margin = Inches(0.984)

setup_clean_header_footer(section3, "פרויקט לוד ניר צבי | חשמל — הנחיות להגשת Rev 02")

p_conc_h = doc.add_paragraph()
set_rtl(p_conc_h)
r_ch_t = p_conc_h.add_run('6. הנחיות להגשת Revision 02 ותהליך סגירת ממצאים אוטומטי')
r_ch_t.font.name = 'David'
r_ch_t.font.size = Pt(14)
r_ch_t.font.bold = True
r_ch_t.font.color.rgb = NAVY

p_conc_b = doc.add_paragraph()
set_rtl(p_conc_b)
conc_text = (
    "על בסיס הממצאים, החלופות והפעולות המומלצות שפורטו בדוח זה, מתכנן מערכות החשמל והמתח הנמוך מתבקש לפעול לפי סדר העדיפויות:\n"
    "1. עדכון ישיר בתוכניות ובמפרטי הלוחות של כל ממצאי P1 (ביטול פחת במשאבות כיבוי, שדרוג MSB ל-50kA, שקע אב״כ +1.80 מ', כבלי PH120 ותאורת DALI).\n"
    "2. תיאום מול מתכנן השלד והאדריכל עבור ממצאי P2 (שרוולי אטמי אב״כ Roxtec, מרווחי 30 ס\"מ מסולמות כבלים לתעלות מיזוג, וקשר כוחות הצלה BDA).\n"
    "3. אימות חישוב עומסים ומפל מתח עבור ממצאי P3 (כיול מפל מתח בעולים ΔV ≤ 3%, סלקטיביות הגנות וניהול עומסי EV).\n\n"
    "עם קבלת תוכניות ומודל Revision 02 המעודכנים, המערכת תריץ בדיקת סגירת ממצאים אוטומטית (Automated Closure Verification) ותפיק טבלת השוואת גרסאות (Rev Comparison) שתאשר את סגירת הממצאים."
)
r_cb = p_conc_b.add_run(conc_text)
r_cb.font.name = 'David'
r_cb.font.size = Pt(10.5)

doc.add_paragraph()

# ==========================================
# 8. Recommended Hold Point
# ==========================================
p_hp_h = doc.add_paragraph()
set_rtl(p_hp_h)
r_hph = p_hp_h.add_run('7. המלצה לנקודת עצירה (Recommended Hold Point)')
r_hph.font.name = 'David'
r_hph.font.size = Pt(13)
r_hph.font.bold = True
r_hph.font.color.rgb = CRIMSON

p_hp_b = doc.add_paragraph()
set_rtl(p_hp_b)
hp_text = (
    "RECOMMENDED HOLD POINT:\n"
    "מומלץ שלא לקדם ביצוע והזמנת לוחות חשמל ראשיים עד לקבלת התייחסות המתכנן ואישור הגורמים המקצועיים הרלוונטיים:\n\n"
    "• לוחות ראשיים והזנות חירום: ELEC-MSB-001 (כושר ניתוק קצר 50kA), ELEC-FP-001 (איסור פחת במשאבות כיבוי), ELEC-ATS-001 (זמן מעבר ונעילת ATS).\n"
    "• תשתיות כבלים ותאורת חירום: ELEC-CBL-001 (כבלי PH120 וסולמות E90), ELEC-EMG-001 (תאורת חירום 180 דקות ו-DALI).\n"
    "• עולי כוח ופירי חשמל: ELEC-BUS-001 (מפל מתח בעולים 3%), ELEC-FST-001 (איטום אש 120 דק' בפירים), ELEC-SPD-001 (הגנת נחשולים מדורגת).\n"
    "• מרחבים מוגנים (ממ״ד): ELEC-MMD-001 (שקע אב״כ +1.80 מ' ללא פחת), ELEC-MMD-002 (אטמי אב״כ מודולריים 1.5 bar)."
)
r_hpb = p_hp_b.add_run(hp_text)
r_hpb.font.name = 'David'
r_hpb.font.size = Pt(10)
r_hpb.font.color.rgb = CRIMSON

doc.save(doc_path)
print("Complete Designer-Facing Action & Closure Report for Electrical generated successfully at:", doc_path)
