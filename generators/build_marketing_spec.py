import docx, os, zipfile, re, shutil
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
from perfect_rtl_utils import set_perfect_rtl, NAVY, CRIMSON, DARK_GRAY, GREEN_COLOR, ORANGE_COLOR, BLUE_COLOR

doc_path = '/home/yogi/lod_project/תוכנית_עבודה_ואיפיון_הצלבת_תוכניות_מכר_מול_ביצוע_מאסטר.docx'
doc = docx.Document()

s = doc.sections[0]
s.page_width = Inches(8.27)
s.page_height = Inches(11.69)
s.top_margin = Inches(0.984)
s.bottom_margin = Inches(0.984)
s.left_margin = Inches(0.984)
s.right_margin = Inches(0.984)

hdr = s.header
hdr.is_linked_to_previous = False
p_hdr = hdr.paragraphs[0]
set_perfect_rtl(p_hdr)
r_hdr = p_hdr.add_run("פרויקט לוד ניר צבי | הצלבת תוכניות מכר מול ביצוע — איפיון מאסטר סבב 2 מעמיק")
r_hdr.font.name = 'David'
r_hdr.font.size = Pt(12)
r_hdr.font.color.rgb = RGBColor(120, 120, 120)

ftr = s.footer
ftr.is_linked_to_previous = False
p_ftr = ftr.paragraphs[0]
p_ftr.alignment = WD_ALIGN_PARAGRAPH.LEFT
r_ftr = p_ftr.add_run("סבב בדיקה: 01 | מהדורה לקראת Rev 02 | דוח סגירת ממצאים למתכנן")
r_ftr.font.name = 'David'
r_ftr.font.size = Pt(12)
r_ftr.font.color.rgb = RGBColor(120, 120, 120)

# Title: Pure Hebrew
p_t = doc.add_paragraph()
set_perfect_rtl(p_t)
r_t = p_t.add_run('איפיון הנדסי ומשפטי מלא — הצלבת תוכניות מכר מול ביצוע (סבב 2 מעמיק)')
r_t.font.name = 'David'
r_t.font.size = Pt(18)
r_t.font.bold = True
r_t.font.color.rgb = NAVY

p_sub = doc.add_paragraph()
set_perfect_rtl(p_sub)
r_sub = p_sub.add_run('פרויקט: לוד ניר צבי (עמרם אברהם) | חבילת מכר מול מודלי ביצוע BIM | סבב בדיקה מעמיק 02')
r_sub.font.name = 'David'
r_sub.font.size = Pt(12)
r_sub.font.bold = True
r_sub.font.color.rgb = CRIMSON

p_desc = doc.add_paragraph()
set_perfect_rtl(p_desc)
desc_text = (
    "מסמך זה מהווה את איפיון התכן ההנדסי, המשפטי והתכנוני המעמיק והמורחב (סבב 2 מלא) להצלבת תוכניות מכר, חוזי רוכשים ומפרטים טכניים מול מודלי הביצוע בפועל (BIM Execution Models) בפרויקט \"לוד ניר צבי — עמרם אברהם\".\n\n"
    "בסבב מעמיק זה הורחבו והועמקו כלל ממשקי החשיפה המשפטית והתכנונית ליזם, לרבות: חישובי שטח פלדיום מול ביצוע (סטיית חוק המכר עד 2.0%), גריעת שטחים עקב פירי מערכות חודרים שלא סומנו במכר, בליטות עמודי שלד, גובה תקרה נטו (מינימום 2.50 מ' ו-2.20 מ' בהנמכות גבס), מידות חניות מוצמדות מול עמודים (רוחב 2.40 מ' ו-2.90 מ' ליד קיר), גובה ראש חופשי בחניות (H ≥ 2.20m), שטח מחסנים מוצמדים ומסתורי כביסה.\n\n"
    "האיפיון מובנה ב-5 פרקים ראשיים, 18 סעיפי בקרה מפורטים ו-56 תת-סעיפים הנדסיים מבוצרים בהתאם לחוק המכר (דירות) תשל״ג-1973, צו מכר דירות (טופס של מפרט), תקנות התכנון והבנייה ות״י 1918 (נגישות):"
)
r_d = p_desc.add_run(desc_text)
r_d.font.name = 'David'
r_d.font.size = Pt(12)

doc.add_paragraph()

# 5 Expanded Chapters for Marketing vs Execution
chapters_spec_mkt = [
    ("פרק א׳: שטחי דירות, סטיית חוק המכר וחישובי פלדיום (חוק המכר דירות)", [
        ("1.1 התאמת שטח דירה עיקרי (פלדיום/נטו)", "השוואת שטח דירה עיקרי בתוכנית המכר מול שטח בנוי בפועל במודל ביצוע, והגבלת סטייה מרבית ל-2.0% לפי חוק המכר.", "🔴 Tier 1"),
        ("1.2 שטח מרפסות שמש וגגות מוצמדים", "השוואת שטח מרפסות שמש בתוכניות המכר מול מודלי הביצוע, מניעת גריעת שטחי חוץ מוצמדים.", "🔴 Tier 1 / 🟡 Tier 2"),
        ("1.3 גובה תקרה נטו וחללי הנמכות תקרת גבס", "גובה תקרה נטו H ≥ 2.50 מ' בחללי מגורים, והגבלת הנמכות גבס למיזוג לגובה נטו H ≥ 2.20 מ' בהתאמה למובטח במפרט.", "🔴 Tier 1"),
        ("1.4 מידות נטו של חללי מגורים, חדרי שינה וממ״ד", "רוחב חדר שינה מינימלי B ≥ 2.60 מ', שטח חדר שינה A ≥ 8.0 מ\"ר, ושטח נטו ממ״ד A ≥ 9.0 מ\"ר (נטו טיח).", "🔴 Tier 1")
    ]),
    ("פרק ב׳: פירי מערכות, עמודים קונסטרוקטיביים ומסתורי כביסה", [
        ("2.1 פירי שרברבות ומיזוג חודרים לשטח הדירה", "איתור פירים אנכיים וצינורות ביוב/מיזוג החודרים לחלל הדירה ללא גילוי וסימון מפורש בתוכנית המכר (מניעת תביעות שטח).", "🔴 Tier 1"),
        ("2.2 בליטות עמודי שלד וקירות בטון בחדרים", "בדיקת עמודים וקירות מעובים הבולטים לתוך חלל חדר שינה או סלון מעבר למוצג בתוכנית המכר החתומה.", "🔴 Tier 1 / 🟡 Tier 2"),
        ("2.3 גודל מסתורי כביסה והתאמה למספר מעבים", "גודל מסתור כביסה המאפשר התקנת כלל מעבי ה-VRF/מזגנים, דוד שמש ומייבש כביסה ללא חסימת זרימת אוויר.", "🔴 Tier 1"),
        ("2.4 פליטת אוויר חם ממסתור כביסה ורפפות", "מניעת קצר אוויר חם במסתור הכביסה, שילוב רפפות אלומיניום עם שטח מעבר חופשי 60% לפחות.", "🟡 Tier 2 / 🟢 Tier 3")
    ]),
    ("פרק ג׳: חניות מוצמדות, מחסנים וגבהי ראש בחניון (תקנות התכנון והבנייה)", [
        ("3.1 מידות חניות מוצמדות מול עמודי שלד", "רוחב חניה סטנדרטית W ≥ 2.40 מ', וחניה הצמודה לקיר או עמוד בטון W ≥ 2.90 מ' בהתאם להנחיות משרד התחבורה.", "🔴 Tier 1"),
        ("3.2 חניות נכים מוצמדות ורצועות פריקה", "רוחב חניית נכה מוצמדת W ≥ 3.50 מ' (או 2.50 מ' עם רצועת פריקה משותפת 1.30 מ') לפי ת״י 1918 חלק 2.", "🔴 Tier 1"),
        ("3.3 גובה ראש פנוי מעל חניות מוצמדות", "שמירה על גובה ראש נטו H_clear ≥ 2.20 מ' בכל שטח החניה המוצמדת (מתחת לצינורות שופכין, ספרינקלרים ותעלות).", "🔴 Tier 1"),
        ("3.4 שטח ומיקום מחסנים דירתיים במרתף", "בדיקת שטח מחסן נטו, רוחב דלת כניסה (W ≥ 80cm) ונגישות ללא חסימת צנרת ומערכות בתוך המחסן.", "🔴 Tier 1 / 🟡 Tier 2")
    ]),
    ("פרק ד׳: פתחי חלונות, כיווני אוויר, מרפסות ומעקות (תקנות הבנייה)", [
        ("4.1 שטח פתחי אוורור ותאורה טבעית", "שטח חלונות נטו של לפחות 8% משטח רצפת החדר ושטח פתח אוורור לפחות 5% לפי תקנות התכנון והבנייה.", "🔴 Tier 1"),
        ("4.2 מיקום חלונות דירות גן מול פירי חניון", "מניעת מיקום חלונות דירת גן מול פתחי פליטת עשן וגזים מחניונים (שמירה על מרחק 5.0 מטר).", "🔴 Tier 1"),
        ("4.3 גובה מעקות מרפסת שמש ופתחי מעבר", "גובה מעקה מרפסת מוגבה H ≥ 1.10 מטר מעל הריצוף לפי ת״י 1142, ללא אלמנטים המאפשרים טיפוס ילדים.", "🔴 Tier 1")
    ]),
    ("פרק ה׳: מפרט טכני, גילוי נאות ומניעת חשיפה משפטית (צו מכר טופס 1)", [
        ("5.1 התאמת מפרט טכני (צו מכר) לציוד מותקן", "אימות נקודות חשמל, אביזרי אינסטלציה, סוגי ריצוף וחיפויים במודל הביצוע מול המובטח בצו מכר טופס 1.", "🔴 Tier 1"),
        ("5.2 סימון נקודות תאורה וכוח מיוחדות", "התאמת שקעי תלת-פאזי לכיריים אינדוקציה, הכנה לרכב חשמלי והזנות מזגנים לפי חוזה המכר.", "🟡 Tier 2 / 🟢 Tier 3"),
        ("5.3 דוח התאמה סופי והמלצה ל-Hold Point", "הפקת דוח התאמה משולב ליועצים המשפטיים ולהנהלת השיווק וההנדסה למניעת תביעות ירידת ערך.", "🔴 Tier 1")
    ])
]

for ch_title, sections in chapters_spec_mkt:
    p_ch = doc.add_paragraph()
    set_perfect_rtl(p_ch)
    r_ch = p_ch.add_run(ch_title)
    r_ch.font.name = 'David'
    r_ch.font.size = Pt(13)
    r_ch.font.bold = True
    r_ch.font.color.rgb = NAVY
    
    t_sec = doc.add_table(rows=len(sections)+1, cols=3)
    t_sec.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_sec._tbl.tblPr.append(parse_xml(f'<w:bidiVisual {nsdecls("w")}/>'))
    
    hdr_row = t_sec.rows[0]
    for c_i, h_txt in enumerate(['סעיף בקרה', 'פירוט הבדיקה ההנדסית והמשפטית (סבב 2 מורחב)', 'סיווג חומרה צפוי']):
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
        
    for r_i, (s_num, s_desc, s_tier) in enumerate(sections, start=1):
        row = t_sec.rows[r_i]
        bg = 'FFFDF0' if 'Tier 2' in s_tier else ('FFF0F0' if 'Tier 1' in s_tier else 'F0FFF4')
        for col_idx, text in enumerate([s_num, s_desc, s_tier]):
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
            elif col_idx == 2:
                r.font.bold = True
                r.font.color.rgb = CRIMSON if 'Tier 1' in text else (ORANGE_COLOR if 'Tier 2' in text else GREEN_COLOR)
                
    doc.add_paragraph() # Spacer

doc.save(doc_path)
print("Complete Round 2 Master Marketing Specification DOCX generated successfully at:", doc_path)
