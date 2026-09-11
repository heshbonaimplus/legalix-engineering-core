import docx, os, zipfile, re, shutil
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

doc_path = '/home/yogi/lod_project/תוכנית_עבודה_ואיפיון_חשמל_ומתח_נמוך_מאסטר.docx'
doc = docx.Document()

def set_rtl(p):
    pPr = p._p.get_or_add_pPr()
    bidi = OxmlElement('w:bidi')
    bidi.set(qn('w:val'), '1')
    pPr.append(bidi)
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT

NAVY = RGBColor(16, 44, 87)
CRIMSON = RGBColor(180, 0, 0)
DARK_GRAY = RGBColor(50, 50, 50)
GREEN_COLOR = RGBColor(0, 120, 0)
ORANGE_COLOR = RGBColor(210, 105, 0)

# Document Title
p_title = doc.add_paragraph()
set_rtl(p_title)
r_title = p_title.add_run('איפיון הנדסי מלא ותוכנית עבודה מאסטר — חשמל, מתח נמוך ומערכות חירום')
r_title.font.name = 'David'
r_title.font.size = Pt(19)
r_title.font.bold = True
r_title.font.color.rgb = NAVY

p_sub = doc.add_paragraph()
set_rtl(p_sub)
r_sub = p_sub.add_run('פרויקט: לוד ניר צבי (עמרם אברהם) | מגדלים 321, 339 ומבנה 223 | מערכת רמזורים הנדסית (מהדורה אופטימלית)')
r_sub.font.name = 'David'
r_sub.font.size = Pt(12)
r_sub.font.italic = True
r_sub.font.color.rgb = DARK_GRAY

# Executive Overview
p_ov = doc.add_paragraph()
set_rtl(p_ov)
r_ov = p_ov.add_run('מסמך זה מהווה את איפיון התכן ההנדסי המלא, המקיף והמחייב לבקרת תכן, בטיחות חשמל, מערכות חירום וסופרפוזיציה של מערכות החשמל והמתח הנמוך בפרויקט "לוד ניר צבי — עמרם אברהם".\nהאיפיון כולל 6 פרקים ראשיים, 19 סעיפי בקרה מפורטים ו-60 תת-סעיפים הנדסיים בשיטת הבלוקים והרמזורים (Tier 1 קריטי שובר ביצוע / Tier 2 פרקטיקת ביצוע והנדסת שטח / Tier 3 אופטימיזציה וחיסכון ליזם), בהתאם לחוק החשמל, תקנות חח״י, ת״י 1220, ת״י 1001, NFPA 70/110, ת״י 1430 ותקנות פקע״ר 2024:')
r_ov.font.name = 'David'
r_ov.font.size = Pt(11)

# Traffic Light Legend Table
table_leg = doc.add_table(rows=4, cols=3)
table_leg.alignment = WD_TABLE_ALIGNMENT.CENTER
headers = ['סיווג רמזור', 'הגדרה הנדסית ומשמעות', 'הנחיית פעולה לצוות התכנון והביצוע']
hdr_row = table_leg.rows[0]
for idx, text in enumerate(headers):
    cell = hdr_row.cells[idx]
    shd = parse_xml('<w:shd {} w:fill="102C57"/>'.format(nsdecls('w')))
    cell._tc.get_or_add_tcPr().append(shd)
    p = cell.paragraphs[0]
    set_rtl(p)
    r = p.add_run(text)
    r.font.name = 'David'
    r.font.size = Pt(10)
    r.font.bold = True
    r.font.color.rgb = RGBColor(255, 255, 255)

legend_data = [
    ('🔴 אדום (Tier 1: קריטי / שובר ביצוע)', 'סכנות התחשמלות, שריפה מחשמל, כשל בהזנת משאבות כיבוי אש ומפוחי עשן, קצר מתח גבוה ופסילות חח״י/כב״ה.', 'חובת תיקון מיידי בתוכניות טרם ביצוע ⛔'),
    ('🟡 צהוב (Tier 2: פרקטיקה והנדסת שטח)', 'דרישות תקן מחמירות שניתן לגשר עליהן בפרקטיקת ביצוע מקובלת (איזון עומסים, שרוולים, תיעוד ותיוג לוחות).', 'הגדרת חלופה ביצועית מאושרת במפרט ⚠️'),
    ('🟢 ירוק (Tier 3: אופטימיזציה וחיסכון ליזם)', 'ניהול עומסי טעינת רכב חשמלי (DLM), יעילות אנרגטית, תאורת DALI חסכונית והוזלת עלויות ביצוע ליזם.', 'יישום להוזלת עלויות ביצוע ואישור מהיר ✅')
]

for row_idx, (c1, c2, c3) in enumerate(legend_data, start=1):
    row = table_leg.rows[row_idx]
    bg = 'FFF0F0' if '🔴' in c1 else ('FFFDF0' if '🟡' in c1 else 'F0FFF4')
    tc = CRIMSON if '🔴' in c1 else (ORANGE_COLOR if '🟡' in c1 else GREEN_COLOR)
    for col_idx, text in enumerate([c1, c2, c3]):
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

doc.add_paragraph()

# Detailed 6 Chapters Breakdown
chapters = [
    ('פרק א׳: חניונים תת-קרקעיים, לוחות ראשיים ותשתיות טעינת רכב חשמלי (EV)', [
        ('1.1 לוחות חשמל ראשיים (MSB)', 'בקרת כושר ניתוק בזרם קצר (I_sc ≥ 50 kA), הגנות סלקטיביות, מפסקי אוויר (ACB) וטמפרטורת פסי צבירה.', '🔴 Tier 1 / 🟡 Tier 2'),
        ('1.2 הזנות כוח למערכות כיבוי אש ושחרור עשן', 'הזנה ישירה ללא מפסקי מגן מזרם דלף (פחת) למשאבות כיבוי אש ומפוחי שחרור עשן בהתאם לחוק החשמל ות״י 1596.', '🔴 Tier 1'),
        ('1.3 תשתית טעינת רכב חשמלי (EV Charging)', 'מערכת ניהול עומסים דינמית (DLM), הגנות זרם ישר RDC-DD 6mA / Type B, ומערך ניתוק חירום אוטומטי מחובר לרכזת אש.', '🔴 Tier 1 / 🟢 Tier 3'),
        ('1.4 הארקות יסוד והשוואת פוטנציאלים', 'בדיקת רציפות הארקת יסוד, פסי השוואת פוטנציאלים ראשיים (פש״ח) ועמידות עכבת לולאת תקלה (Z_s) בכל מפלסי החניון.', '🔴 Tier 1 / 🟡 Tier 2')
    ]),
    ('פרק ב׳: מערכות חירום, גנרציה ואל-פסק (NFPA 110, ת״י 1001.4, ת״י 1220 וחוק החשמל)', [
        ('2.1 לוח החלפה אוטומטי (ATS)', 'זמן מעבר מירבי (t ≤ 10 sec), נעילה מכנית וחשמלית כפולה (Interlock) והזנת מעגלי חירום מציליי חיים.', '🔴 Tier 1'),
        ('2.2 כבלי כוח ובקרה חסיני אש (PH120)', 'חובת עמידות אש 300°C ל-120 דקות (PH120 / FE180) למשאבות כיבוי, מפוחי על-לחץ ומעליות כבאים ללא פשרות.', '🔴 Tier 1'),
        ('2.3 מערכות תאורת חירום ושלטי מילוט', 'משך פעולה 180 דקות (3 שעות), עוצמת הארה E ≥ 1.0 Lux בנתיבי מילוט, ניטור כתובתי DALI ובדיקות אוטומטיות.', '🔴 Tier 1 / 🟡 Tier 2')
    ]),
    ('פרק ג׳: מגדלי המגורים — עולי כוח, פירי חשמל ולוחות דירתיים (חוק החשמל)', [
        ('3.1 עולי כוח ופסי צבירה (Busbars)', 'חתכי מוליכים, מפלי מתח מותרים (ΔV ≤ 3.0%), סלקטיביות בין לוחות קומתיים לראשי ומקדמי בו-זמניות.', '🔴 Tier 1 / 🟢 Tier 3'),
        ('3.2 איטום מעברי אש (Firestop 120 min) בפירי חשמל', 'אטימה אטומה לגזים ועמידת אש שעתיים (ת״י 931) בכל חדירת תקרה לאורך פיר החשמל במגדל 18 קומות.', '🔴 Tier 1'),
        ('3.3 לוחות חשמל דירתיים והגנות מגן', 'הגנות נחשולי מתח (SPD Type 2), מפסקי מגן מפני התחשמלות (RCD 30mA) לכל המעגלים ואיזון עומסי פאזות.', '🔴 Tier 1 / 🟡 Tier 2')
    ]),
    ('פרק ד׳: מרחבים מוגנים (ממ״ד) — חשמל, תאורה והגנת הדף (תקנות פקע״ר 2024 ות״י 448)', [
        ('4.1 שקעי חשמל ותאורה בממ״ד', 'שקע כוח ייעודי למערכת סינון אב״כ בגובה +1.80 מ\' מוזן ממעגל ללא ממסר פחת, וגופי תאורת חירום מוגני הדף.', '🔴 Tier 1'),
        ('4.2 אטמי אב״כ מודולריים בשרוולי חשמל', 'איטום כלל שרוולי החשמל והתקשורת בממ״ד באטמי גזים מודולריים (Roxtec R-Series / Hilti) לעמידה בלחץ 1.5 bar.', '🔴 Tier 1')
    ]),
    ('פרק ה׳: מערכות מתח נמוך, גילוי אש ואינטגרציית בטיחות (ת״י 1220 / ת״י 1430)', [
        ('5.1 רכזת גילוי אש כתובתית ראשית (FACP)', 'מטריצת פיקוד בטיחות אש — הורדת מעליות, הפעלת מפוחי על-לחץ, פתיחת דמפרים ושחרור דלתות מגנטיות.', '🔴 Tier 1'),
        ('5.2 מערכת כריזת חירום ופינוי קולי (PA/VA)', 'מערכת כריזה כתובתית (ת״י 1220.3 / EN 54-16) בדירוג מובנות דיבור STI ≥ 0.50 בכל החללים.', '🔴 Tier 1 / 🟡 Tier 2'),
        ('5.3 מערכת הגנה מפני ברקים (LPS)', 'רשת קולטי ברקים וטבעות גישור היקפיות (ת״י 1430 / IEC 62305 רמה Level II) על גגות המגדלים.', '🔴 Tier 1 / 🟡 Tier 2')
    ]),
    ('פרק ו׳: סופרפוזיציה, ריסון סיסמי, בדיקות מסירה והכרזת Hold Point', [
        ('6.1 הצלבות סולמות כבלים מול קונסטרוקציה ומיזוג', 'מרווחי אוויר 30 ס\"מ מסולמות כבלים לתעלות מיזוג ושמירה על גובה ראש נטו H_clear ≥ 2.40m בחניון.', '🔴 Tier 1 / 🟡 Tier 2'),
        ('6.2 תמיכות סיסמיות לסולמות כבלים ולוחות חשמל', 'חיזוקים סיסמיים אלכסוניים 45° לסולמות כבלים כבדים ועוגני Hilti HST3 לבטון סדוק (ת״י 413).', '🔴 Tier 1 / 🟡 Tier 2'),
        ('6.3 פרוטוקול בדיקות הרצה, לולאת תקלה (LT) ו-Hold Point', 'בדיקות בידוד מגר, בדיקת רציפות הארקות, בדיקות אינטגרציה מלאות והכרזת נקודת עצירה רשמית.', '🔴 Tier 1')
    ])
]

for ch_title, sections in chapters:
    p_ch = doc.add_paragraph()
    set_rtl(p_ch)
    r_ch = p_ch.add_run(ch_title)
    r_ch.font.name = 'David'
    r_ch.font.size = Pt(14)
    r_ch.font.bold = True
    r_ch.font.color.rgb = NAVY
    
    t_ch = doc.add_table(rows=len(sections)+1, cols=3)
    t_ch.alignment = WD_TABLE_ALIGNMENT.CENTER
    h_row = t_ch.rows[0]
    for idx, text in enumerate(['סעיף בקרה', 'פירוט הבדיקה ההנדסית המחייבת', 'סיווג רמזור צפוי']):
        cell = h_row.cells[idx]
        shd = parse_xml('<w:shd {} w:fill="102C57"/>'.format(nsdecls('w')))
        cell._tc.get_or_add_tcPr().append(shd)
        p = cell.paragraphs[0]
        set_rtl(p)
        r = p.add_run(text)
        r.font.name = 'David'
        r.font.size = Pt(10)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        
    for s_idx, (s_name, s_desc, tier_str) in enumerate(sections, start=1):
        row = t_ch.rows[s_idx]
        bg = 'FFF0F0' if '🔴' in tier_str else 'FFFDF0'
        for col_idx, text in enumerate([s_name, s_desc, tier_str]):
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
                r.font.color.rgb = NAVY
            elif col_idx == 2:
                r.font.bold = True
                r.font.color.rgb = CRIMSON if '🔴' in text else ORANGE_COLOR
                
    doc.add_paragraph()

doc.save(doc_path)
print('Master Electrical Specification DOCX generated successfully!')
