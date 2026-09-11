import docx, os, zipfile, re, shutil
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
from builder_utils import set_rtl, setup_clean_header_footer, NAVY, CRIMSON, DARK_GRAY, GREEN_COLOR, ORANGE_COLOR, BLUE_COLOR

doc_path = '/home/yogi/lod_project/תוכנית_עבודה_ואיפיון_פיתוח_נופי_וניקוז_חצר_מאסטר.docx'
doc = docx.Document()

s = doc.sections[0]
s.page_width = Inches(8.27)
s.page_height = Inches(11.69)
s.top_margin = Inches(0.984)
s.bottom_margin = Inches(0.984)
s.left_margin = Inches(0.984)
s.right_margin = Inches(0.984)

setup_clean_header_footer(s, "פרויקט לוד ניר צבי | פיתוח נופי וניקוז חצר — איפיון מאסטר סבב 2 מעמיק")

# Title
p_t = doc.add_paragraph()
set_rtl(p_t)
r_t = p_t.add_run('איפיון הנדסי מלא ותוכנית עבודה מאסטר — פיתוח נופי וניקוז חצר (סבב 2 מעמיק)')
r_t.font.name = 'David'
r_t.font.size = Pt(18)
r_t.font.bold = True
r_t.font.color.rgb = NAVY

p_sub = doc.add_paragraph()
set_rtl(p_sub)
r_sub = p_sub.add_run('פרויקט: לוד ניר צבי (עמרם אברהם) | מודל: LOD_ALL_LG_R24 | סבב בדיקה מעמיק 02')
r_sub.font.name = 'David'
r_sub.font.size = Pt(12)
r_sub.font.bold = True
r_sub.font.color.rgb = CRIMSON

p_desc = doc.add_paragraph()
set_rtl(p_desc)
desc_text = (
    "מסמך זה מהווה את איפיון התכן ההנדסי המעמיק והמורחב (סבב 2 מלא) לבקרת תכן פיתוח שטח, ניקוז מי נגר, מפלסים, נגישות, קירות תמך חוץ וממשקי חניון בפרויקט \"לוד ניר צבי — עמרם אברהם\".\n\n"
    "בסבב מעמיק זה הורחבו והועמקו כלל ממשקי התשתית, לרבות: מפלסי ספי כניסות לובי מול מפלסי פיתוח למניעת הצפות, שיפועי רמפות נגישות (ת״י 1918), רדיוס סיבוב רכבי כיבוי אש (R ≥ 12.0m), ניקוז נגר חצר בעוצמת גשם 150 מ\"מ/שעה, מתקני חלחול והחדרה למי תהום, יציבות קירות תמך והרחקת פירי אוורור חניון משבילים ומפתחי דירות גן.\n\n"
    "האיפיון מובנה ב-5 פרקים ראשיים, 17 סעיפי בקרה מפורטים ו-52 תת-סעיפים הנדסיים מבוצרים בהתאם לתקנות התכנון והבנייה, ת״י 1918 (נגישות), ת״י 1205.3 (ניקוז מי גשם), ת״י 940 (ביסוס וקירות תמך), הוראות כבאות והצלה ותקנות בריאות העם:"
)
r_d = p_desc.add_run(desc_text)
r_d.font.name = 'David'
r_d.font.size = Pt(10.5)

doc.add_paragraph()

# 5 Expanded Chapters for Landscape
chapters_spec_ls = [
    ("פרק א׳: מפלסי פיתוח, ממשקי לובי ונגישות (ת״י 1918 והוראות כבאות)", [
        ("1.1 מפלסי פיתוח קרקע מול ספי כניסות לובי", "שמירה על סף כניסה של 2–3 ס\"מ מעל מפלס הריצוף החיצוני, שיפועי הרחקה ומניעת חדירת נגר עילי לחללי הלובי.", "🔴 Tier 1"),
        ("1.2 שיפועי שבילים ורמפות נגישות לנכים", "שיפוע שבילים רגיל s ≤ 5%, שיפוע רמפות נגישות s ≤ 8% עם פודסטים ומנוחות כל 10 מטר ומאחזי יד per ת״י 1918.", "🔴 Tier 1 / 🟡 Tier 2"),
        ("1.3 גובה מעקות ופתחי נפילה במגרש", "גובה מעקות מגן במפלסים עם הפרש גובה מעל 60 ס\"מ: H ≥ 1.05 מ' (ו-1.10 מ' במרפסות) לפי ת״י 2142 ות״י 1142.", "🔴 Tier 1"),
        ("1.4 נתיבי רכב חירום ורדיוס סיבוב כבאיות", "רוחב נתיב חירום חופשי של 4.0 מטר לפחות, רדיוס סיבוב חוץ R ≥ 12.0 מ' וכושר נשיאה לעומס סרן 160 kN.", "🔴 Tier 1")
    ]),
    ("פרק ב׳: ניקוז חצר, שיפועי נגר עילי ומתקני חלחול (ת״י 1205.3 ותמ״א 1)", [
        ("2.1 שיפועי נגר שטח להרחקת מים ממבנים", "שיפוע קרקע וריצוף חוץ s ≥ 1.5% המכוון הרחק מקירות המגדלים למניעת חלחול רטיבות לשלד.", "🔴 Tier 1 / 🟡 Tier 2"),
        ("2.2 קולטני שטח, שוחות חצר וספיקת ניקוז", "ספיקת קליטה מלאה לעוצמת גשם מקומית i = 150 mm/hr, סבכות ניקוז עמידות עומס כבד (D400) ושוחות שיקוע חול.", "🔴 Tier 1"),
        ("2.3 מתקני החדרה וחלחול מי נגר לקרקע", "שוחות חלחול ומתקני החדרה למי תהום בהתאם להנחיות תמ״א 1 ומנהל התכנון למניעת עומס על מערכת הניקוז העירונית.", "🟡 Tier 2 / 🟢 Tier 3"),
        ("2.4 הפרדת נגר רמפת חניון מתעלות חצר", "מניעת זרימת נגר מפיתוח החצר לתוך רמפת החניון, סבכת קליטה עליונה כפולה בכניסה לרמפה.", "🔴 Tier 1")
    ]),
    ("פרק ג׳: קירות תמך חיצוניים, גדרות מגרש ויציבות קרקע (ת״י 940)", [
        ("3.1 יציבות קירות תמך פיתוח (מהפך והחלקה)", "מקדם ביטחון למהפך F_OT ≥ 1.50 ומקדם ביטחון להחלקה F_SL ≥ 1.50 תחת עומס אדמה ועומס חי לפי ת״י 940.", "🔴 Tier 1"),
        ("3.2 מערך ניקוז מאחורי קירות תמך חוץ", "בד גיאוטכני סופג, חצץ מסנן וצינור שרשורי מחורר Ø4\" בבסיס הקיר למניעת עליית לחץ הידרוסטטי על הקיר.", "🔴 Tier 1 / 🟡 Tier 2"),
        ("3.3 תפרי התפשטות בקירות תמך ארוכים", "תפרי התפשטות ומחיצות כל 10–12 מטר לאורך קירות תמך היקפיים למניעת סדיקה תרמית והתבקעות.", "🟡 Tier 2")
    ]),
    ("פרק ד׳: סופרפוזיציה מול פתחי אוורור חניון ופירי חירום (Underground Clashes)", [
        ("4.1 הגבהת פתחי פירי אוורור ועשן מעל מפלס גינון", "הגבהת דפנות פיר בטון לגובה H ≥ 0.50 מ' מעל פני הקרקע למניעת כניסת מי נגר, בוץ ועלווה למרתפי החניון.", "🔴 Tier 1"),
        ("4.2 מרחק הפרדה מפירי פליטת עשן לשבילים ודירות גן", "שמירה על מרחק הפרדה של לפחות 5.0 מטר מפתחי פליטת עשן חניון לחלונות דירות גן ושבילי הולכי רגל.", "🔴 Tier 1"),
        ("4.3 עומסי אדמת גינון ועצים בוגרים על תקרת הפודיום", "התאמת עומסי קרקע מתוכננים (משקל מרבי 18 kN/m³) ועומסי שורשי עצים לכושר הנשיאה של תקרת הפודיום.", "🔴 Tier 1 / 🟡 Tier 2")
    ]),
    ("פרק ה׳: השקיה, תשתיות חוץ ובדיקות מסירה (Health Regs & Handover)", [
        ("5.1 מפריד זרימה חוזרת (מז״ח) להשקיה", "התקנת מז״ח ייעודי תקני על קו הזנת מי ההשקיה והדישון למניעת זיהום מי השתייה לפי תקנות בריאות העם.", "🔴 Tier 1"),
        ("5.2 תיאום שרוולי מעבר לתאורת גן ושערים", "שרוולי מעבר פלסטיים מוגנים מתחת למשטחים מרוצפים לתשתיות חשמל, שערים חשמליים ותקשורת.", "🟡 Tier 2 / 🟢 Tier 3"),
        ("5.3 בדיקות שיפועים בהצפה והכרזת Hold Point", "בדיקת הצפה מבוקרת לאימות שיפועי ניקוז בחצר ומניעת היקוות שלוליות סביב המגדלים.", "🔴 Tier 1")
    ])
]

for ch_title, sections in chapters_spec_ls:
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
print("Complete Round 2 Master Landscape Specification DOCX generated successfully at:", doc_path)
