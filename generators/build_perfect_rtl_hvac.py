import docx, os, zipfile, re, shutil
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_SECTION, WD_ORIENTATION
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
from perfect_rtl_utils import set_perfect_rtl, NAVY, CRIMSON, DARK_GRAY, GREEN_COLOR, ORANGE_COLOR, BLUE_COLOR

target_filename = 'HVAC_DESIGNER_CORRECTION_AND_CLOSURE_REPORT_REV01.docx'
doc_path = os.path.join('/home/yogi/lod_project', target_filename)
doc = docx.Document()

# Section 1 Setup
s1 = doc.sections[0]
s1.orientation = WD_ORIENTATION.PORTRAIT
s1.page_width = Inches(8.27)
s1.page_height = Inches(11.69)
s1.top_margin = Inches(0.984)
s1.bottom_margin = Inches(0.984)
s1.left_margin = Inches(0.984)
s1.right_margin = Inches(0.984)

hdr = s1.header
hdr.is_linked_to_previous = False
p_hdr = hdr.paragraphs[0]
set_perfect_rtl(p_hdr)
r_hdr = p_hdr.add_run("פרויקט לוד ניר צבי | דוח הנחיות תיקון וסגירת ממצאים למתכנן המיזוג — Legalix Designer Closure Report")
r_hdr.font.name = 'David'
r_hdr.font.size = Pt(8.5)
r_hdr.font.color.rgb = RGBColor(120, 120, 120)

ftr = s1.footer
ftr.is_linked_to_previous = False
p_ftr = ftr.paragraphs[0]
p_ftr.alignment = WD_ALIGN_PARAGRAPH.LEFT
r_ftr = p_ftr.add_run("סבב בדיקה: 01 | מהדורה לקראת Rev 02 | דוח סגירת ממצאים למתכנן")
r_ftr.font.name = 'David'
r_ftr.font.size = Pt(8.5)
r_ftr.font.color.rgb = RGBColor(120, 120, 120)

# Title: Pure Hebrew first
p_title = doc.add_paragraph()
set_perfect_rtl(p_title)
r_title = p_title.add_run('דוח הנחיות תיקון, חלופות וסגירת ממצאים למתכנן')
r_title.font.name = 'David'
r_title.font.size = Pt(20)
r_title.font.bold = True
r_title.font.color.rgb = NAVY

p_sub = doc.add_paragraph()
set_perfect_rtl(p_sub)
r_sub = p_sub.add_run('מערכות מיזוג אוויר, אוורור ושחרור עשן (HVAC) — תוכנית עבודה למהדורה 02 (Rev 02)')
r_sub.font.name = 'David'
r_sub.font.size = Pt(14)
r_sub.font.bold = True
r_sub.font.color.rgb = CRIMSON

# Metadata lines (Each line as a separate right-aligned paragraph!)
meta_lines = [
    "פרויקט: לוד ניר צבי",
    "יזם: עמרם אברהם",
    "מיועד עבור: מתכנן מערכות מיזוג אוויר ושחרור עשן (צ'רלי חורי / צוות תכנון)",
    "מבנים / מגרשים: מגדלים 321, 339 ומבנה 223",
    "גרסת מודל ותוכניות שנבדקה: LOD_HV_ALL_R23 (רוויט, שלד, כיבוי ואדריכלות)",
    "תאריך הפקה: ספטמבר 2026 | מהדורה: סבב 01 לקראת מהדורה מתוקנת (Revision 02)",
    "מטרת המסמך: מתן מפת עבודה מוכנה, פעולות מועדפות, הנחיות עדכון מודל מדויקות והערכת זמן לקיצור ימי תכנון."
]

for ml in meta_lines:
    p_m = doc.add_paragraph()
    set_perfect_rtl(p_m)
    r_m = p_m.add_run(ml)
    r_m.font.name = 'David'
    r_m.font.size = Pt(10)
    r_m.font.color.rgb = DARK_GRAY

doc.add_paragraph() # Spacer

# Section 1: Executive Summary
p_ex_h = doc.add_paragraph()
set_perfect_rtl(p_ex_h)
r_exh = p_ex_h.add_run('1. תקציר ומטרת המסמך עבור צוות התכנון')
r_exh.font.name = 'David'
r_exh.font.size = Pt(13)
r_exh.font.bold = True
r_exh.font.color.rgb = NAVY

p_ex_p1 = doc.add_paragraph()
set_perfect_rtl(p_ex_p1)
r_exp1 = p_ex_p1.add_run('דוח זה נבנה ככלי עבודה מעשי עבור המתכנן, שמטרתו לקצר את זמן העבודה מממצא במודל (Finding) לפתרון סגור ומאושר (Resolved).')
r_exp1.font.name = 'David'
r_exp1.font.size = Pt(10.5)

p_ex_p2 = doc.add_paragraph()
set_perfect_rtl(p_ex_p2)
r_exp2 = p_ex_p2.add_run('עבור כל אחד מ-22 הממצאים שאותרו במודל, הדוח מציג מבנה עבודה תלת-אזורי ממוקד:')
r_exp2.font.name = 'David'
r_exp2.font.size = Pt(10.5)

bullets = [
    "• אזור 1: מה נמצא במודל — מיקום מדויק, צילום מסומן, נתון מדוד מול דרישה תקנית ופער מספרי.",
    "• אזור 2: מה לעשות עכשיו — הפעולה המומלצת המועדפת, הסיבה לבחירתה, מה בדיוק לעדכן ב-Rev 02 והערכת זמן ביצוע.",
    "• אזור 3: איך נסגור את הממצא — קריטריון סגירה אוטומטי שהמערכת תבדוק ב-Rev 02, דיסציפלינות לתיאום וטופס החלטה."
]

for b in bullets:
    p_b = doc.add_paragraph()
    set_perfect_rtl(p_b)
    r_b = p_b.add_run(b)
    r_b.font.name = 'David'
    r_b.font.size = Pt(10)

p_ex_p3 = doc.add_paragraph()
set_perfect_rtl(p_ex_p3)
r_exp3 = p_ex_p3.add_run('הדוח כולל מפת עדיפויות ביצוע (P1 עד P4) המאפשרת למתכנן לפתוח את היום עם משימות ממוקדות הניתנות לסגירה מהירה.')
r_exp3.font.name = 'David'
r_exp3.font.size = Pt(10.5)

doc.add_paragraph() # Spacer

# Section 2: Priority Table
p_pr_h = doc.add_paragraph()
set_perfect_rtl(p_pr_h)
r_prh = p_pr_h.add_run('2. מפת עדיפויות לביצוע תיקונים (Task Priorities & Time Estimates)')
r_prh.font.name = 'David'
r_prh.font.size = Pt(13)
r_prh.font.bold = True
r_prh.font.color.rgb = NAVY

t_prio = doc.add_table(rows=5, cols=4)
t_prio.alignment = WD_TABLE_ALIGNMENT.CENTER
tblPr = t_prio._tbl.tblPr
tblPr.append(parse_xml(f'<w:bidiVisual {nsdecls("w")}/>'))

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
    r.font.size = Pt(9.5)
    r.font.bold = True
    r.font.color.rgb = RGBColor(255, 255, 255)

prio_data = [
    ('🔥 P1 — תיקון ישיר במודל', 'הטיית כנפוני מפוחי סילון, גובה גלאי CO, שסתומי אל-חוזר, שסתום הדף Type B וריסון סיסמי', '10–15 דקות לממצא', '12 ממצאים'),
    ('🤝 P2 — דורש תיאום יועצים', 'שרוול בקורה B-108, גובה ראש תעלה, הרחקת פירי עשן, מרחב מנואלה אב״כ וספרינקלר תחת תעלה', 'דורש תיאום חיצוני (שלד/אדריכלות/כיבוי)', '6 ממצאים'),
    ('📐 P3 — דורש חישוב תרמי / הידראולי', 'ספיקת אוורור שנאים 12,000 m³/h, כוח פתיחת דלתות על-לחץ ומהירות זרימה בפיר', '30–45 דקות (כיול חישוב תרמי/הידראולי)', '3 ממצאים'),
    ('💡 P4 — המלצת אופטימיזציה', 'שילוב בקרי VFD מדורגים למפוחי פליטה בחניון לפי ריכוז CO', 'הנדסת ערך (לשיקול יזם/מתכנן)', '1 ממצא')
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
        r.font.size = Pt(9)
        if col_idx == 0:
            r.font.bold = True
            r.font.color.rgb = CRIMSON if 'P1' in text else (ORANGE_COLOR if 'P2' in text else NAVY)
        elif col_idx == 3:
            r.font.bold = True

doc.add_paragraph()

# Read 22 cards and add cards
from build_designer_hvac_action_report import hvac_designer_cards

effort_map_el = {
    "P1": "10–15 דקות (תיקון ישיר במודל רוויט / מפרט)",
    "P2": "תיאום יועצים (שלד / מיזוג / בטיחות)",
    "P3": "30–45 דקות (כיול חישוב מפל מתח / קצר)",
    "P4": "הנדסת ערך (לשיקול דעת היזם והמתכנן)"
}

p_cards_head = doc.add_paragraph()
set_perfect_rtl(p_cards_head)
r_c_h = p_cards_head.add_run('3. פירוט כרטיסי עבודה במבנה 3 האזורים למתכנן (Finding & Action Cards)')
r_c_h.font.name = 'David'
r_c_h.font.size = Pt(14)
r_c_h.font.bold = True
r_c_h.font.color.rgb = NAVY

action_rows_full = []
current_ch = ""

for item in hvac_designer_cards:
    ch = item['chapter']
    if ch != current_ch:
        current_ch = ch
        p_ch_t = doc.add_paragraph()
        set_perfect_rtl(p_ch_t)
        r_cht = p_ch_t.add_run(current_ch)
        r_cht.font.name = 'David'
        r_cht.font.size = Pt(13)
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
    set_perfect_rtl(p_fh)
    r_fhid = p_fh.add_run(f"{item['id']} | {item['title']}\n")
    r_fhid.font.name = 'David'
    r_fhid.font.size = Pt(11.5)
    r_fhid.font.bold = True
    r_fhid.font.color.rgb = NAVY
    
    r_fhst = p_fh.add_run(f"סטטוס: {item['status']}  |  עדיפות: {item['prio']}  |  זמן משוער: {effort_str}")
    r_fhst.font.name = 'David'
    r_fhst.font.size = Pt(9.5)
    r_fhst.font.bold = True
    r_fhst.font.color.rgb = CRIMSON if '🔴' in item['status'] else (ORANGE_COLOR if '🟡' in item['status'] else BLUE_COLOR)
    
    # 3-Block Table
    t_c = doc.add_table(rows=11, cols=2)
    t_c.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_c._tbl.tblPr.append(parse_xml(f'<w:bidiVisual {nsdecls("w")}/>'))
    
    card_rows_data = [
        ("🔍 אזור 1: מה נמצא במודל", "פירוט עובדתי, מדידות ופרמטרים מתוך המודל"),
        ("מיקום מדויק ואלמנט נבדק:", f"{item['loc']}\nאלמנט: {item['elem']}"),
        ("הממצא והפער שנמדד:", f"ממצא: {item['finding']}\nערך במודל: {item['val_curr']} | מחושב: {item['val_calc']}\nקריטריון תכן: {item['req']}\nפער שנמדד: {item['delta']}"),
        ("משמעות הנדסית ומקור מאומת:", f"משמעות: {item['impact']}\nמקור מאומת: {item['src']}"),
        
        ("⚡ אזור 2: מה לעשות עכשיו (הנחיית פעולה מועדפת)", "הנחיות קונקרטיות לביצוע ב-Rev 02"),
        ("הפעולה המומלצת לביצוע (מועדפת):", f"{item['rec_action']}\n\nהסבר לבחירה: {item['rec_reason']}"),
        ("מה בדיוק לעדכן בתוכניות / מודל (Rev 02):", f"👉 {item['rev_update']}"),
        ("חלופות הנדסיות נוספות שנבחנו:", item['alts']),
        
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
        r0.font.size = Pt(9.5 if is_block_hdr else 9)
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
        set_perfect_rtl(p_img_t)
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
# 5. מקטע חדש לרוחב (Landscape Section) לטבלת תוכנית עבודה
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
r_hdr2 = p_hdr2.add_run("פרויקט לוד ניר צבי | מיזוג אוויר ושחרור עשן — תוכנית פעולה וסגירת ממצאים ל-Rev 02")
r_hdr2.font.name = 'David'
r_hdr2.font.size = Pt(8.5)
r_hdr2.font.color.rgb = RGBColor(120, 120, 120)

ftr2 = section2.footer
ftr2.is_linked_to_previous = False
p_ftr2 = ftr2.paragraphs[0]
p_ftr2.alignment = WD_ALIGN_PARAGRAPH.LEFT
r_ftr2 = p_ftr2.add_run("סבב בדיקה: 01 | מהדורה לקראת Rev 02 | דוח סגירת ממצאים למתכנן")
r_ftr2.font.name = 'David'
r_ftr2.font.size = Pt(8.5)
r_ftr2.font.color.rgb = RGBColor(120, 120, 120)

p_act_head = doc.add_paragraph()
set_perfect_rtl(p_act_head)
r_act_h = p_act_head.add_run('4. תוכנית עבודה ומעקב סגירת ממצאים למתכנן (HVAC Action & Closure Plan)')
r_act_h.font.name = 'David'
r_act_h.font.size = Pt(14)
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
        set_perfect_rtl(p)
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
# 6. החזרת מקטע לאורך (Portrait Section) למסקנות
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
r_hdr3 = p_hdr3.add_run("פרויקט לוד ניר צבי | מיזוג אוויר — הנחיות להגשת Rev 02")
r_hdr3.font.name = 'David'
r_hdr3.font.size = Pt(8.5)
r_hdr3.font.color.rgb = RGBColor(120, 120, 120)

ftr3 = section3.footer
ftr3.is_linked_to_previous = False
p_ftr3 = ftr3.paragraphs[0]
p_ftr3.alignment = WD_ALIGN_PARAGRAPH.LEFT
r_ftr3 = p_ftr3.add_run("סבב בדיקה: 01 | מהדורה לקראת Rev 02 | דוח סגירת ממצאים למתכנן")
r_ftr3.font.name = 'David'
r_ftr3.font.size = Pt(8.5)
r_ftr3.font.color.rgb = RGBColor(120, 120, 120)

p_conc_h = doc.add_paragraph()
set_perfect_rtl(p_conc_h)
r_ch_t = p_conc_h.add_run('5. הנחיות להגשת Revision 02 ותהליך סגירת ממצאים אוטומטי')
r_ch_t.font.name = 'David'
r_ch_t.font.size = Pt(14)
r_ch_t.font.bold = True
r_ch_t.font.color.rgb = NAVY

p_conc_b = doc.add_paragraph()
set_perfect_rtl(p_conc_b)
conc_text = (
    "על בסיס הממצאים, החלופות והפעולות המומלצות שפורטו בדוח זה, מתכנן מערכות המיזוג ושחרור העשן מתבקש לפעול לפי סדר העדיפויות:\n"
    "1. עדכון ישיר במודל של כל ממצאי P1 (כנפוני הטיה למפוחי סילון, גובה גלאי CO, שסתומי אל-חוזר, שסתום הדף Type B וריסון סיסמי).\n"
    "2. תיאום מול מתכנן השלד והאדריכל עבור ממצאי P2 (שרוול בקורה B-108, גובה ראש תעלה, הרחקת פירי עשן, מרחב מנואלה אב״כ וספרינקלר תחת תעלה).\n"
    "3. אימות חישוב תרמי / הידראולי לממצאי P3 (ספיקת אוורור שנאים 12,000 m³/h, כוח פתיחת דלתות על-לחץ, ומהירות זרימה בפיר).\n\n"
    "עם קבלת מודל Revision 02 המעודכן, המערכת תריץ בדיקת סגירת ממצאים אוטומטית (Automated Closure Verification) ותפיק טבלת השוואת גרסאות (Rev Comparison) שתאשר את סגירת הממצאים."
)
r_cb = p_conc_b.add_run(conc_text)
r_cb.font.name = 'David'
r_cb.font.size = Pt(10.5)

doc.add_paragraph()

# Recommended Hold Point
p_hp_h = doc.add_paragraph()
set_perfect_rtl(p_hp_h)
r_hph = p_hp_h.add_run('6. המלצה לנקודת עצירה (Recommended Hold Point)')
r_hph.font.name = 'David'
r_hph.font.size = Pt(13)
r_hph.font.bold = True
r_hph.font.color.rgb = CRIMSON

p_hp_b = doc.add_paragraph()
set_perfect_rtl(p_hp_b)
hp_text = (
    "RECOMMENDED HOLD POINT:\n"
    "מומלץ שלא לקדם ביצוע של העבודות הרלוונטיות לממצאים המפורטים להלן עד לקבלת התייחסות המתכנן ואישור הגורמים המקצועיים הרלוונטיים:\n\n"
    "• ממצאים קריטיים בשלד ובחניון: HVAC-JET-001 (מפוח מול קורה), HVAC-DCT-001 (גובה תעלה בנתיב), HVAC-SUP-001 (חציית קורה B-108 וספרינקלר).\n"
    "• חדרי אנרגיה וחירום: HVAC-TX-001 (אוורור שנאים), HVAC-GEN-001 (רדיאטור וארובת גנרטור), HVAC-BAT-001 (מצברי UPS).\n"
    "• מערכות על-לחץ ומילוט: HVAC-PRS-001 (כוח פתיחת דלת), HVAC-PRS-003 (פיר על-לחץ), HVAC-LIFT-001 (מעלית כבאים).\n"
    "• מרחבים מוגנים (ממ״ד): HVAC-MMD-001 (רדיוס מנואלה 1.0 מ'), HVAC-MMD-002 (שסתום פריקת הדף), HVAC-MMD-003 (שסתום הדף Type B בניקוז מזגן)."
)
r_hpb = p_hp_b.add_run(hp_text)
r_hpb.font.name = 'David'
r_hpb.font.size = Pt(10)
r_hpb.font.color.rgb = CRIMSON

doc.save(doc_path)
print("Perfect RTL Designer-Facing HVAC Report generated successfully at:", doc_path)
