import docx, os, zipfile, re, shutil, json
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

doc_path = '/home/yogi/lod_project/LOD_HVAC_Design_Review_MASTER.docx'
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
BLUE_COLOR = RGBColor(0, 102, 204)

# Document Header Title
p_title = doc.add_paragraph()
set_rtl(p_title)
r_title = p_title.add_run('דוח בקרת תכן הנדסית מקדמית — מיזוג אוויר, אוורור ושחרור עשן (HVAC)')
r_title.font.name = 'David'
r_title.font.size = Pt(19)
r_title.font.bold = True
r_title.font.color.rgb = NAVY

p_sub = doc.add_paragraph()
set_rtl(p_sub)
r_sub = p_sub.add_run('פרויקט: לוד ניר צבי (עמרם אברהם) | מודל LOD_HV_ALL_R23 | מנוע בקרת תכן MEP דיגיטלי (מהדורה מעודכנת)')
r_sub.font.name = 'David'
r_sub.font.size = Pt(12)
r_sub.font.italic = True
r_sub.font.color.rgb = DARK_GRAY

# Section 1: Process Flow & 3-Engine Architecture
p_arch = doc.add_paragraph()
set_rtl(p_arch)
r_arch = p_arch.add_run('ארכיטקטורת הבקרה הדיגיטלית ותהליך העבודה (The 3-Engine Core Architecture):')
r_arch.font.name = 'David'
r_arch.font.size = Pt(14)
r_arch.font.bold = True
r_arch.font.color.rgb = NAVY

p_flow = doc.add_paragraph()
set_rtl(p_flow)
flow_text = (
    "תהליך הבקרה ההנדסי של המערכת מבוסס על Digital Twin ורשת מנועים הנדסיים רציפים:\n"
    "1. קליטת קבצי מקור גולמיים: קליטת מודלי RVT, IFC, קבצי DWG ותוכניות PDF ללא תלות בהמרה ידנית מוקדמת של היועץ.\n"
    "2. מנוע גיאומטרי (Geometry Engine): מדידה ישירה ומיפוי תלת-ממדי של התנגשויות (Clashes), מרחקים מקורות, חתכי תעלות, גבהי נטו FFL ושיפועים.\n"
    "3. מנוע כללים דטרמיניסטי (Deterministic Rules Engine): השוואה אוטומטית של המדידות מול ספרית חוקי התכן (HVAC Rule Library) ומספרי סף מוחלטים.\n"
    "4. שכבת בינה מלאכותית (AI Synthesizer): ניתוח המשמעות ההנדסית של החריגה, פירוט הסיכון התפעולי והצעת פתרון כירורגי מותאם ליועץ.\n"
    "5. מודל BCF והכרעת יועץ: כל ממצא מוצג על גבי המודל התלת-ממדי ברוויט עם חופש הכרעה מלא ליועץ (מאושר / דחוי / חלופת שטח)."
)
r_flow = p_flow.add_run(flow_text)
r_flow.font.name = 'David'
r_flow.font.size = Pt(10.5)

# Status Matrix Table (4 Colors)
p_stat = doc.add_paragraph()
set_rtl(p_stat)
r_stat = p_stat.add_run('מפתח 4 הסטטוסים ההנדסיים לבקרת תכן (4-Tier Status System):')
r_stat.font.name = 'David'
r_stat.font.size = Pt(13)
r_stat.font.bold = True
r_stat.font.color.rgb = NAVY

t_stat = doc.add_table(rows=5, cols=3)
t_stat.alignment = WD_TABLE_ALIGNMENT.CENTER
headers = ['סטטוס וסיווג', 'הגדרה הנדסית ומשמעות', 'הנחיית פעולה ליועץ / מודל']
hdr_row = t_stat.rows[0]
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

status_data = [
    ('🔴 אדום (RED)', 'חובה לתקן — כשל קריטי, בטיחות חיים (Life Safety), התנגשות קשה בשלד או פסילת תקן מחייבת.', 'חובת תיקון מיידי בתוכניות ובמודל ⛔'),
    ('🟡 צהוב (YELLOW)', 'דורש החלטת יועץ / תיאום ביצוע מול קונסטרוקציה, אדריכלות או חלופת שטח מקובלת.', 'קבלת החלטת יועץ והגדרת מפרט ביצוע ⚠️'),
    ('🔵 כחול (BLUE)', 'המלצת אופטימיזציה, הנדסת ערך (Value Engineering), יעילות אנרגטית וחיסכון בעלויות ליזם.', 'המלצה כלכלית לבחירת היזם והמתכנן 💡'),
    ('🟢 ירוק (GREEN)', 'נבדק במודל ואומת כתקין ב-100% לפי כל דרישות התקנים והחישובים ההנדסיים.', 'נבדק ואושר לתעודת גמר / טופס 4 ✅')
]

for row_idx, (c1, c2, c3) in enumerate(status_data, start=1):
    row = t_stat.rows[row_idx]
    bg = 'FFF0F0' if '🔴' in c1 else ('FFFDF0' if '🟡' in c1 else ('F0F8FF' if '🔵' in c1 else 'F0FFF4'))
    tc = CRIMSON if '🔴' in c1 else (ORANGE_COLOR if '🟡' in c1 else (BLUE_COLOR if '🔵' in c1 else GREEN_COLOR))
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

doc.add_paragraph() # Spacer

# Full 22 Findings Structured by Chapter
chapters_data = [
    ("פרק א׳: חניונים תת-קרקעיים — מפוחי סילון (Jet Fans), תעלות עשן וגלאי CO", [
        ("HVAC-JET-001", "חסימת סילון אוויר ע\"י קורות שלד יורדות B-101", "חניון מרתף 2- (ציר F-8)", "Jet_Fan", "מרחק 1.20 מטר מקורה יורדת 80 ס\"מ ללא כנפוני הטיה", "מרחק ≥ 8.0 מטר או כנפוני הטיה -5°", "סילון 22 מ\"ש פוגע בקורה ומערבל עשן מטה לנתיב מילוט", "🔴 אדום (חובה לתקן)", "ת״י 1001.7 / BS 7346-7", True, "התקנת כנפוני הטיה -5° או הרחקת המפוח למרחק L ≥ 8.0 מטר מהקורה.", "/home/yogi/lod_project/markup_hvac_01_jet_fans_parking.png"),
        ("HVAC-DCT-001", "גובה ראש נטו מתחת לתעלת שחרור עשן ראשית בנתיב נסיעה", "חניון מרתף 1- (נתיב ראשי)", "Duct", "תעלת עשן צוללת תחת קורה ומורידה גובה ראש ל-1.95 מטר", "גובה ראש נטו H_clear ≥ 2.40 מטר (2.70 מ' לרכב שירות)", "חוסר גובה של 45 ס\"מ וסכנת פגיעת משאיות כיבוי", "🔴 אדום (חובה לתקן)", "תקנות התכנון והבנייה / משרד התחבורה", True, "תיאום שרוול פלדה יצוק מראש בשליש המרכזי של הקורה (h/3) לשמירה על גובה 2.45 מטר.", "/home/yogi/lod_project/markup_hvac_02_smoke_ducts_headroom.png"),
        ("HVAC-CO-001", "גובה התקנת גלאי פחמן חד-חמצני (CO) מעל הרצפה", "חניון מרתף 1- ו-2-", "CO_Sensor", "גלאי CO הותקנו בתקרה בגובה 3.20 מטר מעל הרצפה", "גובה נשימת אדם מדויק 1.50 מטר (±0.20 מטר)", "עיכוב גילוי של 40 דקות והרעלת שוהים בחניון", "🔴 אדום (חובה לתקן)", "ת״י 1001.7 / EN 50545-1", True, "העתקת גלאי ה-CO לעמודי בטון בגובה 1.50 מטר עם כלובי מגן מפלדה.", "/home/yogi/lod_project/markup_hvac_03_co_detection_vfd.png"),
        ("HVAC-SFT-001", "מרחק הפרדה בין פיר פליטת עשן לפיר יניקת אוויר צח", "חצר פיתוח מפלס 0.00", "Shaft_Discharge", "מרחק של 3.0 מטר בלבד בין פיר עשן לפיר אוויר צח", "מרחק הפרדה פיזי מינימלי L_sep ≥ 10.0 מטר", "קצר אוויר קטלני — שאיבת עשן שחור בחזרה לחניון", "🔴 אדום (חובה לתקן)", "ת״י 1001.7 / NFPA 92", True, "הרחקת הפירים למרחק של לפחות 10.0 מטר או פליטת עשן בגג המגדל ברום +58 מטר.", "/home/yogi/lod_project/markup_hvac_04_main_extract_fans.png")
    ]),
    ("פרק ב׳: חדרי אנרגיה, שנאים, גנרטור חירום ומצברים בחניון", [
        ("HVAC-TX-001", "טמפרטורת חדר שנאים ומתח גבוה בשיא קיץ (עומס 36 kW)", "חדר שנאים מרתף 2-", "Room_Cooling", "אוורור טבעי בלבד — טמפרטורה מחושבת מגיעה ל-62°C", "טמפרטורה מרבית מותרת T_max ≤ 40°C (מומלץ ≤ 35°C)", "חריגה של 22°C וסכנת קפיצת שנאי חח״י והשבתת חשמל לבניין", "🔴 אדום (חובה לתקן)", "מפרט חח״י / IEC 60076", False, "התקנת מערך מפוחי אוורור מאולץ כפול (Duty/Standby 12,000 m³/h) לשמירה על T ≤ 38°C.", "/home/yogi/lod_project/markup_hvac_05_transformer_room.png"),
        ("HVAC-GEN-001", "פליטת אוויר חם מרדיאטור גנרטור חירום (450 kW)", "חדר גנרטור מרתף 2-", "Radiator_Duct", "פליטה חופשית ישירות לחלל חניון מרתף 2- ללא תעלה לפיר", "תעלת פח אטומה ישירות מפתח הרדיאטור לפיר חיצוני", "חום 65°C מעלה חום חניון ל-75°C וחונק מנוע גנרטור ב-2 דקות", "🔴 אדום (חובה לתקן)", "ת״י 1001.4 / NFPA 110", True, "תכנון תעלת פח אטומה (1.80x1.20 מ') ישירות מפתח הרדיאטור לפיר שחרור ייעודי.", "/home/yogi/lod_project/markup_hvac_06_generator_room.png"),
        ("HVAC-BAT-001", "פליטת גז מימן מתקרת חדר מצברים ומערכות אל-פסק (UPS)", "חדר מצברים מרתף 1-", "Exhaust_Fan", "ללא מפוח פליטת תקרה ייעודי וללא גלאי מימן", "מפוח פליטה רציף ATEX Zone 1 Ex-d (6 החלפות/שעה)", "הצטברות מימן מעל 4% (LEL) וסכנת פיצוץ גז אדיר במרתף", "🔴 אדום (חובה לתקן)", "ת״י 1001 / NFPA 855", True, "התקנת מפוח פליטה מוגן פיצוץ ATEX Zone 1 בתקרה וגלאי H2 אלקטרוכימי 10 ס\"מ מתחת לתקרה.", "/home/yogi/lod_project/markup_hvac_07_battery_room.png")
    ]),
    ("פרק ג׳: מגדלי המגורים — מערכות לחץ יתר בחדרי מדרגות, פירים ושחרור עשן", [
        ("HVAC-PRS-001", "כוח פתיחת דלתות מילוט בחדר מדרגות מוגן בעל-לחץ", "קומות 14–18 מגדל 321", "Egress_Door", "הזרקה עליונה בודדת — לחץ 85 Pa וכוח פתיחת דלת 215 N", "כוח פתיחה מקסימלי מותר F ≤ 133 N (לחץ 25–50 Pa)", "חריגה של 61%+ וכליאת ילדים וקשישים בדירות ללא מילוט", "🔴 אדום (חובה לתקן)", "ת״י 1001.2.2 / NFPA 92", False, "הזרקת אוויר רב-נקודתית כל 3 קומות, בקרת VFD ודמפר פריקה ברומטרי 50 Pa בגג.", "/home/yogi/lod_project/markup_hvac_08_stairwell_pressurization.png"),
        ("HVAC-PRS-003", "מהירות זרימת אוויר בפיר בטון של על-הלחץ", "פיר אנכי מגדל 321/339", "Supply_Shaft", "פיר צר (0.50 מ\"ר) מייצר מהירות זרימה 23.3 מ\"ש", "מהירות זרימה מרבית מותרת v ≤ 12.0 מ\"ש", "מפל לחץ חיכוך 650 Pa, חנק אוויר לקומות תחתונות ושריקות", "🔴 אדום (חובה לתקן)", "ת״י 1001.2.2 / NFPA 92", False, "הגדלת שטח חתך הפיר ל-1.10 מ\"ר (1.10x1.00 מ') להורדת מהירות ל-10.5 מ\"ש.", "/home/yogi/lod_project/markup_hvac_09_pressurization_shaft.png"),
        ("HVAC-COR-001", "דמפרי שחרור עשן ממונעים במסדרונות קומתיים", "מסדרונות קומות 1–18", "Corridor_Damper", "פתחי פיר פתוחים ללא דמפרים ממונעים — יניקה צונחת ל-0.08 מ\"ק/שנ'", "דמפרי עשן ממונעים 24V סגורים בשגרה (Normally Closed)", "איבוד 92% מספיקת הפינוי וחנק דיירים במסדרון המילוט", "🔴 אדום (חובה לתקן)", "ת״י 1001.2.2 / NFPA 92", True, "התקנת דמפרי עשן ממונעים 24V סגורים בשגרה הנפתחים ממוקד בקומה השרופה בלבד (1.0 m³/s).", "/home/yogi/lod_project/markup_hvac_10_corridor_smoke_exhaust.png"),
        ("HVAC-LFT-001", "מפוח על-לחץ עצמאי לפיר מעלית לוחמי אש", "פיר מעלית כבאים", "Elevator_Shaft", "השמטה מלאה של מפוח על-לחץ ייעודי לפיר המעלית", "מערך מפוחי על-לחץ עצמאי (VFD 25–50 Pa) לפיר מעלית כבאים", "חדירת עשן חם לפיר, כליאת כבאים והשבתת פעולות חילוץ", "🔴 אדום (חובה לתקן)", "EN 81-72 / ת״י 1001.2.2", True, "התקנת מפוח על-לחץ עצמאי (25,000 m³/h מבוקר VFD) לפיר מעלית לוחמי האש.", "/home/yogi/lod_project/markup_hvac_11_firefighters_lift_shaft.png")
    ]),
    ("פרק ד׳: דירות מגורים ומסחר — VRF, ניקוז מי עיבוי, אוורור ושומן מסחרי", [
        ("HVAC-CND-001", "שיפוע גרביטציוני לצנרת ניקוז מי עיבוי מזגנים", "דירות מגורים קומות 1–18", "Condensate_Pipe", "שיפוע כמעט אפסי של 0.2% לאורך 8.0 מטר", "שיפוע גרביטציוני מינימלי מחייב s ≥ 1.5%", "סתימת אצות והצפת מים מעל תקרות גבס ופרקטים יוקרתיים", "🔴 אדום (חובה לתקן)", "ת״י 1205 / ת״י 920", True, "הקפדה על שיפוע s ≥ 1.5% ושילוב סיפון יבש מכני שקוף מחוץ לדירה.", "/home/yogi/lod_project/markup_hvac_12_condensate_drainage.png"),
        ("HVAC-REF-001", "ריכוז גז קירור רעיל בחדר שינה הורים סגור (RCL)", "חדרי שינה מגדל 321/339", "VRF_System", "מערכת VRF יחידה (18.5 ק\"ג גז) מייצרת ריכוז פריצה 0.66 kg/m³", "ריכוז מרבי מותר RCL ≤ 0.44 kg/m³ (גז R-410A)", "חריגה של 50%+ וסכנת חנק מוחי ודום לב של דיירים בשינה", "🔴 אדום (חובה לתקן)", "ת״י 920 / EN 378", False, "חלוקת מעגלי ה-VRF למערכות מפוצלות (M ≤ 8.0 kg) וגלאי גז עם שסתומי ניתוק.", "/home/yogi/lod_project/markup_hvac_13_refrigerant_rcl_safety.png"),
        ("HVAC-WET-001", "אוורור מאולץ לחדרים רטובים ושסתומי אל-חוזר מניעת ריחות", "חדרי רחצה ללא חלון", "Exhaust_Fan", "חיבור 90° ישיר לפיר ללא שסתום אל-חוזר ומפוח רועש 48 dB(A)", "פיר שאנט 45°, שסתום אל-חוזר כפול ומפוח מושתק ≤ 30 dB(A)", "חדירת ריחות ביוב ועשן סיגריות בין דירות ומטרד רעש לשינה", "🔴 אדום (חובה לתקן)", "ת״י 1205.1 / ת״י 1004.3", True, "פיר שאנט 45°, שסתומי סיליקון כפולים, מפוחי Silent 100 (26.5 dB) וממסר 15 דק'.", "/home/yogi/lod_project/markup_hvac_14_wet_rooms_ventilation.png"),
        ("HVAC-KIT-001", "תעלות שומן ומנדפים מסחריים במבנה 223", "מטבחים מסחריים מבנה 223", "Grease_Duct", "פח מגולוון ספירלי 0.6 מ\"מ ללא כיבוי אוטומטי במנדף", "פלדה שחורה 1.5 מ\"מ בריתוך רציף + כיבוי Ansul R-102 (UL 300)", "שומן בוער ב-1000°C נוזל מתפרי נעילה ומצית תקרות גבס", "🔴 אדום (חובה לתקן)", "ת״י 1001.6 / NFPA 96", False, "שדרוג לפלדה שחורה 1.5 מ\"מ מרותכת, שמיכת בידוד 3M שעתיים ומערכת Ansul R-102.", "/home/yogi/lod_project/markup_hvac_15_commercial_kitchen_grease.png")
    ]),
    ("פרק ה׳: מרחבים מוגנים (ממ״ד) — סינון אב״כ, שסתומי הדף ומיזוג אוויר", [
        ("HVAC-MMD-001", "מרווח תפעול חופשי לידית המפוח הידני במערכת אב״כ", "ממ״דים מגדל 321/339", "CBRN_Unit", "מרווח של 35 ס\"מ בלבד מדופן ארון בגדים ומפינת קיר", "רדיוס תפעול פנוי של לפחות 1.00 מטר סביב ידית המנואלה", "אי-יכולת סיבוב מנואלה בחירום ופסילה אוטומטית לטופס 4", "🔴 אדום (חובה לתקן)", "תקנות פקע״ר 2024 / ת״י 4570", True, "הזזת ארונות וריהוט להבטחת רדיוס פנוי של לפחות 1.00 מטר סביב ידית המפוח.", "/home/yogi/lod_project/markup_hvac_16_mamad_cbrn_filtration.png"),
        ("HVAC-MMD-002", "שסתום פריקת לחץ הדף (Overpressure Blast Valve) בממ״ד", "קיר הדף חיצוני ממ״ד", "Blast_Valve", "ללא שסתום פריקה על שרוול הפליטה (פליטה אטומה)", "שסתום פריקת הדף מורשה מכויל בטווח 50–100 Pa (ת״י 448)", "לחץ אוויר מזנק מעל 250 Pa, קרע בעור התוף ונעילת דלת הדף", "🔴 אדום (חובה לתקן)", "תקנות פקע״ר / ת״י 448", True, "התקנת שסתום פריקת לחץ הדף 50–100 Pa (ת״י 448) ופלטת מגן רסיסים 10 מ\"מ.", "/home/yogi/lod_project/markup_hvac_17_mamad_blast_valves.png"),
        ("HVAC-MMD-003", "שסתום הדף Type B על קו ניקוז מי עיבוי מזגן הממ״ד", "קיר הדף ממ״ד", "Blast_Valve_TypeB", "צינור ניקוז פלסטיק פשוט ללא שסתום הדף ואטם סיליקון", "שסתום הדף מורשה פקע\"ר Type B ואטם מודולרי Roxtec R-75", "גל הדף 1.5 bar מעיף את המזגן על ראשי דיירים ומחדיר גזים", "🔴 אדום (חובה לתקן)", "תקנות פקע״ר 2024 / ת״י 448", True, "התקנת שסתום הדף Type B על קו הניקוז, אטם Roxtec R-75 ושרוול פלדה ת״י 448.", "/home/yogi/lod_project/markup_hvac_18_mamad_ac_blast_valve.png")
    ]),
    ("פרק ו׳: סופרפוזיציה, אקוסטיקה, תמיכות סיסמיות, TAB ומסירה", [
        ("HVAC-SUP-001", "התנגשות תעלת מיזוג בקורת שלד נושאת B-108 וספרינקלר", "חניון מרתף 2-", "Hard_Clash", "תעלה 1.40x0.50 מ' חותכת זיון תחתון וחוסמת ספרינקלר מעל חניה", "שרוול פלדה ב-h/3 וראשי ספרינקלר תחת תעלה (Below-Duct)", "כשל גזירה בקורת שלד ושריפת רכבים תחת תעלה ללא כיבוי", "🔴 אדום (חובה לתקן)", "ת״י 466 / NFPA 13", True, "שרוול פלדה בשליש הקורה h/3 וראשי ספרינקלר Below-Duct עם מגיני מים.", "/home/yogi/lod_project/markup_hvac_19_superposition_clashes.png"),
        ("HVAC-ACS-001", "בידוד אקוסטי ומשככי קפיץ לצ'ילרים/מעבים בגג המגדל", "גג טכני מעל פנטהאוז", "Acoustic_Isolator", "עיגון קשיח לרצפת הגג — רעש המהום 52 dB(A) בחדר שינה", "משככי קפיץ סיסמיים (שקיעה 50 מ\"מ) ורעש L_Aeq ≤ 30 dB(A)", "חריגה אקוסטית של 22 dB ומטרד רעידות בלתי נסבל בשינה", "🔴 אדום (חובה לתקן)", "ת״י 1004.3 / הגנת הסביבה", False, "משככי קפיץ 50 מ\"מ, בסיס אינרציה צף 150 מ\"מ, קירות מיסוך 25 dB ומשתיקים.", "/home/yogi/lod_project/markup_hvac_20_acoustic_vibration_isolators.png"),
        ("HVAC-SEIS-001", "תמיכות סיסמיות לתעלות עשן כבדות (A ≥ 0.5 m²)", "חניון ופירי מגדל", "Seismic_Bracing", "תעלות 180 kg/m תלויות על מוטות הברגה בלבד ללא חיזוק 45°", "חיזוקים אלכסוניים ב-45° (רוחבי 9m, אורכי 18m) ועוגני HST3", "קריסת תעלות כבדות ברעידת אדמה וריסוק צנרת כיבוי ורכבים", "🔴 אדום (חובה לתקן)", "ת״י 413 / SMACNA", True, "תמיכות אלכסוניות 45° מזוויתן 50x50x5 מ\"מ, שרוול תפר גמיש ועוגני Hilti HST3.", "/home/yogi/lod_project/markup_hvac_21_seismic_sway_bracing.png"),
        ("HVAC-TAB-001", "פרוטוקול בדיקות הרצה, איזון ספיקות (TAB) והכרזת HOLD POINT", "כלל מתקני הפרויקט", "Commissioning", "המשך ביצוע ללא פתרון 21 הליקויים הקריטיים שהתגלו במודל", "הכרזת עצירה רשמית עד להגשת סט תוכניות מתוקן Rev 02", "הטמעת ליקויים בלתי הפיכים ביציקות שלד ונזק כספי כבד ליזם", "🔴 אדום (חובה לתקן)", "ת״י 1001 / כב״ה / פקע״ר", False, "הכרזת HOLD POINT רשמית לעצירת יציקות והתקנות עד להגשת תוכניות Rev 02 מתוקנות.", "/home/yogi/lod_project/markup_hvac_22_commissioning_tab_holdpoint.png")
    ])
]

# Generate Chapters and Detailed Finding Blocks
for ch_idx, (ch_title, findings) in enumerate(chapters_data, start=1):
    p_ch = doc.add_paragraph()
    set_rtl(p_ch)
    r_ch = p_ch.add_run(ch_title)
    r_ch.font.name = 'David'
    r_ch.font.size = Pt(15)
    r_ch.font.bold = True
    r_ch.font.color.rgb = NAVY
    
    for f in findings:
        rule_id, name, loc, elem, defect, req, impact, sev, src, auto_det, fix, img_path = f
        
        p_fhead = doc.add_paragraph()
        set_rtl(p_fhead)
        r_fh = p_fhead.add_run(f"ממצא בקרת תכן: [{rule_id}] — {name}")
        r_fh.font.name = 'David'
        r_fh.font.size = Pt(12.5)
        r_fh.font.bold = True
        r_fh.font.color.rgb = CRIMSON if '🔴' in sev else (ORANGE_COLOR if '🟡' in sev else BLUE_COLOR)
        
        # 8-Field Finding Table
        t_f = doc.add_table(rows=8, cols=2)
        t_f.alignment = WD_TABLE_ALIGNMENT.CENTER
        
        fields = [
            ("מזהה חוק ואלמנט נבדק:", f"Rule ID: {rule_id} | אלמנט: {elem}"),
            ("מיקום גיאומטרי במודל:", loc),
            ("מהות הכשל שנמדד במודל:", defect),
            ("דרישת תקן וסף מחייב:", req),
            ("השפעה הנדסית ובטיחותית:", impact),
            ("סטטוס חומרה ומקור תקן:", f"{sev} | מקור: {src}"),
            ("זיהוי גיאומטרי אוטומטי:", "כן (Geometry Engine Auto-Detected)" if auto_det else "חישוב הנדסי משולב (Rules Engine + Schedule)"),
            ("הנחיית תיקון כירורגית למתכנן:", fix)
        ]
        
        for r_i, (f_label, f_val) in enumerate(fields):
            row = t_f.rows[r_i]
            # Left Header Cell
            c0 = row.cells[0]
            shd0 = parse_xml('<w:shd {} w:fill="F4F6F9"/>'.format(nsdecls('w')))
            c0._tc.get_or_add_tcPr().append(shd0)
            p0 = c0.paragraphs[0]
            set_rtl(p0)
            r0 = p0.add_run(f_label)
            r0.font.name = 'David'
            r0.font.size = Pt(9.5)
            r0.font.bold = True
            r0.font.color.rgb = NAVY
            c0.width = Inches(2.2)
            
            # Right Content Cell
            c1 = row.cells[1]
            bg_c = 'FFF0F0' if (r_i == 5 and '🔴' in sev) else 'FFFFFF'
            shd1 = parse_xml('<w:shd {} w:fill="{}"/>'.format(nsdecls('w'), bg_c))
            c1._tc.get_or_add_tcPr().append(shd1)
            p1 = c1.paragraphs[0]
            set_rtl(p1)
            r1 = p1.add_run(f_val)
            r1.font.name = 'David'
            r1.font.size = Pt(9.5)
            if r_i == 5:
                r1.font.bold = True
                r1.font.color.rgb = CRIMSON if '🔴' in sev else ORANGE_COLOR
            elif r_i == 7:
                r1.font.bold = True
                r1.font.color.rgb = GREEN_COLOR
            c1.width = Inches(4.5)
            
        doc.add_paragraph() # Spacer
        
        # Embed High-Res Markup Image
        if os.path.exists(img_path):
            p_img_t = doc.add_paragraph()
            set_rtl(p_img_t)
            r_it = p_img_t.add_run(f"תשריט ביקורת ויזואלי מסומן מתוך המודל — [{rule_id}]:")
            r_it.font.name = 'David'
            r_it.font.size = Pt(11)
            r_it.font.bold = True
            r_it.font.color.rgb = NAVY
            
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.add_run().add_picture(img_path, width=Inches(6.2))
            
        doc.add_paragraph() # Spacer between findings

# Official Hold Point Section at the End
p_hp_head = doc.add_paragraph()
set_rtl(p_hp_head)
r_hph = p_hp_head.add_run('⛔ הכרזת נקודת עצירה רשמית (OFFICIAL HOLD POINT DECLARATION) ⛔')
r_hph.font.name = 'David'
r_hph.font.size = Pt(15)
r_hph.font.bold = True
r_hph.font.color.rgb = CRIMSON

p_hp_body = doc.add_paragraph()
set_rtl(p_hp_body)
hp_text = (
    "מוכרזת בזאת נקודת עצירה מחייבת (Hold Point) לכלל עבודות מיזוג האוויר, האוורור, פינוי העשן ועל-הלחץ בפרויקט \"לוד ניר צבי — עמרם אברהם\".\n"
    "חל איסור מוחלט על ביצוע יציקות בטון סביב פירים, התקנת מפוחי סילון, פריסת תעלות עשן וצנרת VRF עד להגשת סט תוכניות וחישובים מתוקן (Rev 02) הפותר את כל 22 הליקויים שפורטו בדוח זה ומאושר ע\"י בקר התכן."
)
r_hpb = p_hp_body.add_run(hp_text)
r_hpb.font.name = 'David'
r_hpb.font.size = Pt(11)
r_hpb.font.bold = True
r_hpb.font.color.rgb = CRIMSON

doc.save(doc_path)
print("New Structure HVAC Master Report generated successfully at:", doc_path)
