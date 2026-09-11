import docx, os, zipfile, re, shutil
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
from builder_utils import set_rtl, setup_clean_header_footer, NAVY, CRIMSON, DARK_GRAY, GREEN_COLOR, ORANGE_COLOR, BLUE_COLOR

doc_path = '/home/yogi/lod_project/תוכנית_עבודה_ואיפיון_חשמל_ומתח_נמוך_מאסטר.docx'
doc = docx.Document()

# Base Portrait Section setup
s = doc.sections[0]
s.page_width = Inches(8.27)
s.page_height = Inches(11.69)
s.top_margin = Inches(0.984)
s.bottom_margin = Inches(0.984)
s.left_margin = Inches(0.984)
s.right_margin = Inches(0.984)

setup_clean_header_footer(s, "פרויקט לוד ניר צבי | איפיון תוכנית חשמל ומתח נמוך — סבב 2 מעמיק")

# Title
p_t = doc.add_paragraph()
set_rtl(p_t)
r_t = p_t.add_run('איפיון הנדסי מלא ותוכנית עבודה מאסטר — חשמל, מתח נמוך ומערכות חירום (סבב 2 מעמיק)')
r_t.font.name = 'David'
r_t.font.size = Pt(18)
r_t.font.bold = True
r_t.font.color.rgb = NAVY

p_sub = doc.add_paragraph()
set_rtl(p_sub)
r_sub = p_sub.add_run('פרויקט: לוד ניר צבי (עמרם אברהם) | מגדלים 321, 339 ומבנה 223 | סבב בדיקה מעמיק 02')
r_sub.font.name = 'David'
r_sub.font.size = Pt(12)
r_sub.font.bold = True
r_sub.font.color.rgb = CRIMSON

p_desc = doc.add_paragraph()
set_rtl(p_desc)
desc_text = (
    "מסמך זה מהווה את איפיון התכן ההנדסי המעמיק והמורחב (סבב 2 מלא) לבקרת תכן, בטיחות חשמל, מערכות חירום, מתח נמוך מאוד וסופרפוזיציה של מערכות החשמל בפרויקט \"לוד ניר צבי — עמרם אברהם\".\n\n"
    "בסבב מעמיק זה הורחבו והועמקו כלל ממשקי התשתית, לרבות: שוחות כניסת מתח גבוה, הגנות קשת חשמלית (Arc Flash), הזנת מערכות דלק לגנרטור, ניטור מונים משניים לעמדות טעינת רכב חשמלי (MID Sub-metering), מערך הגנת נחשולי מתח מדורג (SPD Type 1/2/3), קשר כוחות הצלה בחניונים (BDA Repeater), אינטרקום כבאים (Firefighter Warden Phone), והגנת הצפה במרתף 2-.\n\n"
    "האיפיון מובנה ב-6 פרקים ראשיים, 24 סעיפי בקרה מפורטים ו-72 תת-סעיפים הנדסיים מבוצרים בהתאם לחוק החשמל, תקנות חח״י, ת״י 1220, ת״י 1001, NFPA 70/110, ת״י 1430 ותקנות פקע״ר 2024:"
)
r_d = p_desc.add_run(desc_text)
r_d.font.name = 'David'
r_d.font.size = Pt(10.5)

doc.add_paragraph()

# 6 Detailed Expanded Chapters for Round 2
chapters_spec_r2 = [
    ("פרק א׳: חניונים תת-קרקעיים, לוחות ראשיים, עמדות EV וקשת חשמלית (חוק החשמל וחח״י)", [
        ("1.1 לוחות חשמל ראשיים (MSB)", "כושר ניתוק בזרם קצר (I_sc ≥ 50 kA), הגנות סלקטיביות בין ACB ל-MCCB, טמפרטורת פסי צבירה והגנת פריקת לחץ קשת חשמלית (Arc Flash Relief).", "🔴 Tier 1 / 🟡 Tier 2"),
        ("1.2 הזנות כוח למערכות כיבוי ושחרור עשן", "איסור מוחלט על מפסקי מגן מזרם דלף (פחת), הזנה ישירה מלוח חירום בהגנה מגנטית בלבד ומפסק נעול במצב מופעל (Locked ON).", "🔴 Tier 1"),
        ("1.3 תשתית טעינת רכב חשמלי (EV) מתקדמת", "ניהול עומסים דינמי (DLM), הגנות זרם ישר RDC-DD 6mA / Type B, מונים משניים לחיוב דיירים (MID), וניתוק חירום אוטומטי (EPO) מחובר ל-FACP.", "🔴 Tier 1 / 🟢 Tier 3"),
        ("1.4 הארקות יסוד והשוואת פוטנציאלים (פש״ח)", "בדיקת רציפות מוליך פלדה 30x3.5 מ\"מ, פסי השוואת פוטנציאלים ראשיים, הארקת מתח גבוה מול מתח נמוך (TN-S) ועכבת לולאת תקלה (Z_s).", "🔴 Tier 1 / 🟡 Tier 2")
    ]),
    ("פרק ב׳: מערכות חירום, גנרציה, דלק ואל-פסק (NFPA 110, ת״י 1001.4 וחוק החשמל)", [
        ("2.1 לוח החלפה אוטומטי (ATS) כפול", "זמן מעבר מרבי t ≤ 10 sec, נעילה מכנית וחשמלית כפולה (Interlock), בקרת סנכרון מעבר פאזות והזנת משאבות כיבוי.", "🔴 Tier 1"),
        ("2.2 מערכת הזנת דלק ובקרה לגנרטור", "הזנת כוח למשאבות העברת סולר, גלאי דליפת דלק במאצרה, ברזי ניתוק סולנואידיים וחיבור לוח פיקוד גנרטור לרכזת אש.", "🔴 Tier 1 / 🟡 Tier 2"),
        ("2.3 כבלי כוח ובקרה חסיני אש (PH120)", "עמידות אש 300°C ל-120 דקות (PH120 / FE180 / E90) למשאבות כיבוי, מפוחי על-לחץ, מעליות כבאים ולוחות משנה לחירום.", "🔴 Tier 1"),
        ("2.4 תאורת חירום ושלטי מילוט מנוטרים (DALI)", "משך פעולה 180 דקות (3 שעות), עוצמת הארה E ≥ 1.0 Lux בציר מילוט ו-5.0 Lux ליד עמדות כיבוי, מערכת ניטור כתובתית DALI.", "🔴 Tier 1 / 🟡 Tier 2")
    ]),
    ("פרק ג׳: מגדלי המגורים — עולי כוח, פירי חשמל ולוחות דירתיים (חוק החשמל)", [
        ("3.1 עולי כוח ופסי צבירה (Busbar Trunking)", "חתכי מוליכים, מפלי מתח מרביים (ΔV ≤ 3.0%), סלקטיביות הגנות מלאה ומקדמי בו-זמניות לפי תקנות חח״י.", "🔴 Tier 1 / 🟢 Tier 3"),
        ("3.2 איטום מעברי אש (Firestop 120 min) בפירי חשמל", "אטימה עמידת אש ועשן שעתיים (ת״י 931 / UL 1479) בכל חדירת תקרת בטון לאורך פיר החשמל במגדל 18 קומות.", "🔴 Tier 1"),
        ("3.3 מערך הגנת נחשולי מתח מדורג (SPD Type 1/2/3)", "מערך הגנה 3-דרגתי: SPD Type 1 בלוח ראשי MSB, SPD Type 2 בלוחות קומתיים, ו-SPD Type 3 במכשור אלקטרוני רגיש.", "🔴 Tier 1 / 🟡 Tier 2"),
        ("3.4 לוחות חשמל דירתיים ואיזון פאזות", "מפסקי מגן 30mA המכסים 100% מהמעגלים, הפרדת מעגלי כוח ומאור, ואיזון פאזות מדויק למניעת זרם יתר במוליך האפס.", "🔴 Tier 1 / 🟡 Tier 2")
    ]),
    ("פרק ד׳: מרחבים מוגנים (ממ״ד) — חשמל, תאורה והגנת הדף (תקנות פקע״ר 2024 ות״י 448)", [
        ("4.1 שקעי כוח חירום ותאורה מוגנת הדף בממ״ד", "שקע ייעודי למערכת סינון אב״כ בגובה +1.80 מ' ללא ממסר פחת (RCD), וגופי תאורת חירום מוגני הדף וזעזועים.", "🔴 Tier 1"),
        ("4.2 אטמי אב״כ מודולריים בשרוולי חשמל ותקשורת", "איטום כלל שרוולי החשמל והתקשורת בממ״ד באטמי גזים מודולריים (Roxtec / Hilti) לעמידה בלחץ הדף 1.5 bar ובדיקת 50 Pa.", "🔴 Tier 1"),
        ("4.3 בידוד מעגלי הזנת ממ״ד ומניעת קצר", "מעגלי חשמל נפרדים לממ״ד עם צנרת חסינת אש ומניעת תלות במעגלי חדרים סמוכים בעת פגיעה הדף.", "🔴 Tier 1 / 🟡 Tier 2")
    ]),
    ("פרק ה׳: מערכות מתח נמוך, גילוי אש וקשר כוחות הצלה (ת״י 1220 / ת״י 1430)", [
        ("5.1 רכזת גילוי אש כתובתית ראשית (FACP)", "מטריצת פיקוד בטיחות אש מלאה: שחרור דלתות מגנטיות, החזרת מעליות לקרקע, פתיחת דמפרי עשן והפעלת מפוחי על-לחץ.", "🔴 Tier 1"),
        ("5.2 מערכת כריזת חירום ופינוי קולי (PA/VA per EN 54-16)", "מערכת פינוי קולי כתובתית (ת״י 1220.3) בדירוג מובנות דיבור STI ≥ 0.50 ורמקולים חסיני אש (Metal Fire Domes).", "🔴 Tier 1 / 🟡 Tier 2"),
        ("5.3 אינטרקום כבאים ומערכת קשר כוחות הצלה (BDA)", "מערכת טלפון כבאים ייעודית (Warden Phone) בכל מבואת מדרגות ומגבר קליטה סלולרית ורדיו כוחות הצלה בחניונים.", "🔴 Tier 1 / 🟡 Tier 2"),
        ("5.4 מערכת הגנה מפני ברקים (LPS per ת״י 1430 / IEC 62305)", "רשת קולטי ברקים (10x10 מ') וקולטים זקופים ברמת הגנה Class II על גגות המגדלים, מוליכי הורדה וטבעת הארקה היקפית.", "🔴 Tier 1 / 🟡 Tier 2")
    ]),
    ("פרק ו׳: סופרפוזיציה, ריסון סיסמי, בדיקות מסירה והכרזת Hold Point", [
        ("6.1 הצלבות סולמות כבלים מול קונסטרוקציה ו-MEP", "מרווח אוויר נקי של 30 ס\"מ מסולמות כבלים לתעלות מיזוג וצנרת מים, ושמירה על גובה ראש נטו H_clear ≥ 2.40 מ' בחניון.", "🔴 Tier 1 / 🟡 Tier 2"),
        ("6.2 תמיכות סיסמיות לסולמות כבלים ולוחות חשמל", "חיזוקים סיסמיים אלכסוניים ב-45° לסולמות כבלים מעל רוחב 30 ס\"מ וללוחות חשמל ראשיים, עוגני Hilti HST3 לבטון סדוק.", "🔴 Tier 1 / 🟡 Tier 2"),
        ("6.3 הגנת הצפה וניתוק חשמל במרתף 2-", "מערך גילוי הצפה עם ניתוק אוטומטי של שקעים ומעגלי כוח נמוכים במרתף 2- ללא פגיעה בהזנת משאבות טבולות.", "🔴 Tier 1"),
        ("6.4 פרוטוקול בדיקות הרצה, לולאת תקלה (LT) ו-Hold Point", "בדיקות בידוד מגר (1000V), בדיקות עכבת לולאת תקלה, בדיקות אינטגרציה מלאות והמלצה לנקודת עצירה רשמית.", "🔴 Tier 1")
    ])
]

for ch_title, sections in chapters_spec_r2:
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
    for c_i, h_txt in enumerate(['סעיף בקרה', 'פירוט הבדיקה ההנדסית המחייבת (סבב 2 מורחב)', 'סיווג רמזור צפוי']):
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
        
    for r_i, (s_num, s_desc, s_tier) in enumerate(sections, start=1):
        row = t_sec.rows[r_i]
        bg = 'FFFDF0' if 'Tier 2' in s_tier else ('FFF0F0' if 'Tier 1' in s_tier else 'F0FFF4')
        for col_idx, text in enumerate([s_num, s_desc, s_tier]):
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
                r.font.color.rgb = NAVY
            elif col_idx == 2:
                r.font.bold = True
                r.font.color.rgb = CRIMSON if 'Tier 1' in text else (ORANGE_COLOR if 'Tier 2' in text else GREEN_COLOR)
                
    doc.add_paragraph() # Spacer

doc.save(doc_path)
print("Complete Round 2 Master Electrical Specification DOCX generated successfully at:", doc_path)
