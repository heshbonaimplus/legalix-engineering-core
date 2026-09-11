import docx, os, zipfile, re, shutil
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
DARK_GRAY = RGBColor(60, 60, 60)
GREEN_COLOR = RGBColor(0, 120, 0)
ORANGE_COLOR = RGBColor(210, 105, 0)
BLUE_COLOR = RGBColor(0, 102, 204)

# Document Header Title
p_title = doc.add_paragraph()
set_rtl(p_title)
r_title = p_title.add_run('דוח בקרת תכן הנדסית — מערכות מיזוג אוויר, אוורור ושחרור עשן (HVAC)')
r_title.font.name = 'David'
r_title.font.size = Pt(18)
r_title.font.bold = True
r_title.font.color.rgb = NAVY

# Meta Details Box
p_meta = doc.add_paragraph()
set_rtl(p_meta)
meta_text = (
    "פרויקט: לוד ניר צבי — עמרם אברהם\n"
    "מגרשים / מבנים: מגדלים 321, 339 ומבנה 223\n"
    "גרסת תוכניות ומודלים שנבדקה: LOD_HV_ALL_R23 (רוויט, קונסטרוקציה, ספרינקלרים)\n"
    "סטטוס: דוח בקרת תכן הנדסית — סבב 01\n"
    "הערת מתודולוגיה: הבדיקה בוצעה בסיוע מערכת בקרת תכן דיגיטלית המבצעת ניתוח גיאומטרי, חישובי ובין־תחומי של מודלי התכנון."
)
r_meta = p_meta.add_run(meta_text)
r_meta.font.name = 'David'
r_meta.font.size = Pt(10.5)
r_meta.font.color.rgb = DARK_GRAY

# Section 1: Executive Summary
p_ex_head = doc.add_paragraph()
set_rtl(p_ex_head)
r_exh = p_ex_head.add_run('1. תקציר מנהלים (Executive Summary)')
r_exh.font.name = 'David'
r_exh.font.size = Pt(14)
r_exh.font.bold = True
r_exh.font.color.rgb = NAVY

p_ex_body = doc.add_paragraph()
set_rtl(p_ex_body)
ex_body_text = (
    "במסגרת בקרת התכן נבדקו מערכות מיזוג האוויר, האוורור, שחרור העשן, מערכות לחץ היתר וממשקי התיאום עם מערכות השלד, הכיבוי והחשמל בפרויקט \"לוד ניר צבי\".\n\n"
    "בבדיקה אותרו ממצאים המחייבים טיפול טרם קידום התכנון לביצוע, לצד ממצאים הדורשים תיאום בין־תחומי והמלצות לשיפור התכנון והתייעלות כלכלית ואנרגטית.\n\n"
    "הממצאים המפורטים בדוח מבוססים על המידע והמסמכים שהועמדו לבדיקה במועד עריכת הדוח. האחריות לתכנון המפורט, לחישובים ולאישור הפתרונות נותרת בידי המתכננים והיועצים המוסמכים מטעם הפרויקט."
)
r_exb = p_ex_body.add_run(ex_body_text)
r_exb.font.name = 'David'
r_exb.font.size = Pt(10.5)

# Section 2: Executive Dashboard
p_db_head = doc.add_paragraph()
set_rtl(p_db_head)
r_dbh = p_db_head.add_run('2. ריכוז סטטוס ממצאים (Executive Dashboard)')
r_dbh.font.name = 'David'
r_dbh.font.size = Pt(13)
r_dbh.font.bold = True
r_dbh.font.color.rgb = NAVY

t_dash = doc.add_table(rows=5, cols=4)
t_dash.alignment = WD_TABLE_ALIGNMENT.CENTER
headers_d = ['סטטוס', 'משמעות והגדרה', 'הנחיית פעולה', 'מספר ממצאים']
hdr_d_row = t_dash.rows[0]
for idx, text in enumerate(headers_d):
    cell = hdr_d_row.cells[idx]
    shd = parse_xml('<w:shd {} w:fill="102C57"/>'.format(nsdecls('w')))
    cell._tc.get_or_add_tcPr().append(shd)
    p = cell.paragraphs[0]
    set_rtl(p)
    r = p.add_run(text)
    r.font.name = 'David'
    r.font.size = Pt(10)
    r.font.bold = True
    r.font.color.rgb = RGBColor(255, 255, 255)

dash_data = [
    ('🔴 אדום (RED)', 'נדרש תיקון לפני אישור — כשל בטיחותי, התנגשות שלד או אי-התאמה לקריטריון תכן מחייב', 'חובת תיקון בתוכניות טרם ביצוע', '18'),
    ('🟡 צהוב (YELLOW)', 'נדרש תיאום / החלטת יועץ — פער תכנוני הדורש הכרעה הנדסית, תיאום בין-תחומי או מפרט שטח', 'הכרעת יועץ ותיאום ביצוע', '3'),
    ('🔵 כחול (BLUE)', 'המלצת אופטימיזציה — הנדסת ערך (Value Engineering), חיסכון באנרגיה ושיפור יעילות ליזם', 'בחינת כדאיות ע\"י היזם/מתכנן', '1'),
    ('🟢 ירוק (GREEN)', 'PASS — נבדק ולא נמצאה חריגה במסגרת הבדיקות שבוצעו וביחס למידע שהועמד לבדיקה', 'מאושר ללא הערות נוספות', 'נבדק')
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

doc.add_paragraph() # Spacer

# Section 3: Detailed Finding Cards by Chapter
p_body_h = doc.add_paragraph()
set_rtl(p_body_h)
r_bh = p_body_h.add_run('3. פירוט כרטיסי הממצאים ההנדסיים (Detailed Finding Cards)')
r_bh.font.name = 'David'
r_bh.font.size = Pt(14)
r_bh.font.bold = True
r_bh.font.color.rgb = NAVY

chapters_content = [
    ("פרק א׳: חניונים תת-קרקעיים — מפוחי סילון, תעלות עשן וגלאי CO", [
        ("HVAC-JET-001", "חסימת סילון מפוח ע\"י קורת שלד", "🔴 נדרש תיקון", "חניון מרתף 2-, ציר F–8", "מפוח הסילון ממוקם במרחק 1.20 מ' מקורה יורדת B-101 (עומק 80 ס\"מ) ללא כנפוני הטיה.", "פגיעת זרם האוויר בקורה עלולה לשבור את שכבת הציפה התרמית ולפגוע בתפקוד מערך פינוי העשן.", "מרחק פנוי מספק או ניתוב זרם האוויר מתחת לתחתית הקורות למניעת ערבול.", "הנחיות תכנון BS 7346-7 / ת״י 1001 חלק 7", "התאמת אופן הזריקה באמצעות כנפוני הטיה (-5°) או שינוי מיקום המפוח, בכפוף לאישור מתכנן פינוי העשן.", "/home/yogi/lod_project/markup_hvac_01_jet_fans_parking.png", "יועץ מיזוג"),
        ("HVAC-DCT-001", "גובה ראש חופשי מתחת לתעלת שחרור עשן בנתיב נסיעה", "🔴 נדרש תיקון", "חניון מרתף 1-, נתיב נסיעה ראשי", "תעלת העשן (1.80x0.70 מ') מותקנת מתחת לקורה ויוצרת גובה ראש נטו של 1.95 מטר.", "גובה המעבר אינו מאפשר תנועה בטוחה של רכבי שירות ורכבי כיבוי.", "גובה ראש נטו חופשי H_clear ≥ 2.40 מטר (2.70 מ' לנתיבי רכבי חירום ושירות).", "תקנות התכנון והבנייה (התקנת מקומות חניה) / הנחיות משרד התחבורה", "נדרש תיאום קונסטרוקטיבי לשינוי התוואי או בחינת מעבר מאושר ע\"י מהנדס השלד לשמירה על גובה ראש נטו.", "/home/yogi/lod_project/markup_hvac_02_smoke_ducts_headroom.png", "מיזוג + קונסטרוקציה"),
        ("HVAC-CO-001", "מיקום וגובה התקנת גלאי פחמן חד-חמצני (CO)", "🔴 נדרש תיקון", "חניון מרתף 1- ו-2-", "גלאי CO סומנו בתקרה בגובה 3.20 מטר מעל מפלס הרצפה.", "התקנה בגובה התקרה עלולה להאט את זיהוי הצטברות הגז באזור שהיית בני אדם.", "התקנת גלאים בגובה אזור הנשימה (כ-1.50 מטר מעל הרצפה) וברדיוס כיסוי תקני.", "ת״י 1001 חלק 7 / תקן EN 50545-1", "עדכון מיקום הגלאים לעמודים בגובה 1.50 מטר כולל מיגון פיזי נגד פגיעת כלי רכב.", "/home/yogi/lod_project/markup_hvac_03_co_detection_vfd.png", "מיזוג / חשמל"),
        ("HVAC-SFT-001", "מרחק הפרדה בין פיר פליטת עשן לפיר יניקת אוויר צח", "🔴 נדרש תיקון", "מפלס קרקע / פיתוח חצר", "פתחי פיר פליטת עשן ופיר אוויר צח מוקמו במרחק של כ-3.0 מטרים זה מזה.", "מרחק קצר בין הפתחים עלול לגרום לסחרור חוזר של עשן וגזים לתוך מערכת אספקת האוויר.", "הפרדה פיזית של לפחות 10.0 מטרים או פליטה מעל מפלס הגג.", "ת״י 1001 חלק 7 / תקן NFPA 92", "הגדלת המרחק בין פתחי הפירים במפלס הקרקע או הגבהת פליטת העשן אל גג המגדל.", "/home/yogi/lod_project/markup_hvac_04_main_extract_fans.png", "מיזוג + אדריכלות")
    ]),
    ("פרק ב׳: חדרי אנרגיה, שנאים, גנרטור ומצברים", [
        ("HVAC-TX-001", "אוורור ופינוי עומס חום בחדר שנאים ראשי", "🔴 נדרש תיקון", "חדר שנאים, מרתף 2-", "מערך האוורור שתוכנן אינו מבטיח פינוי עומס החום הצפוי (36 kW) בתנאי שיא קיץ.", "עליית טמפרטורה מעל הגבול המותר עלולה לפגוע באמינות אספקת החשמל ובאורך חיי הציוד.", "שמירה על טמפרטורת חדר שלא תעלה על דרישות יצרן השנאים ומפרט חברת החשמל (T ≤ 40°C).", "מפרט חברת החשמל / תקן IEC 60076", "תכנון ספיקת אוורור מאולץ מחושבת (Q_required) לפיזור עומס החום לשמירה על טמפרטורה תקינה.", "/home/yogi/lod_project/markup_hvac_05_transformer_room.png", "יועץ מיזוג"),
        ("HVAC-GEN-001", "פינוי אוויר חם מרדיאטור גנרטור חירום", "🔴 נדרש תיקון", "חדר גנרטור, מרתף 2-", "אוויר הפליטה החם מרדיאטור הגנרטור נפלט לחלל החניון ללא תעלה אטומה לפיר חיצוני.", "פליטת אוויר חם לחלל סגור תגרום לעליית טמפרטורה חדה ולחנק תרמי של מנוע הגנרטור.", "תעלת פח ייעודית ואטומה מפתח הרדיאטור ישירות לפיר פליטה חיצוני.", "ת״י 1001 חלק 4 / תקן NFPA 110", "השלמת תכנון תעלת רדיאטור אטומה ישירות אל פיר האוורור החיצוני.", "/home/yogi/lod_project/markup_hvac_06_generator_room.png", "יועץ מיזוג"),
        ("HVAC-BAT-001", "אוורור ופינוי גז מימן מחדר מצברים ומערכות אל-פסק (UPS)", "🔴 נדרש תיקון", "חדר מצברים, מרתף 1-", "לא הוגדר מפוח פליטה רציף מתקרת החדר ומערך גילוי מימן.", "פליטת גז מימן בעת טעינת מצברים עלולה להביא להצטברות גז דליק בחלק העליון של החדר.", "אוורור רציף בציוד מוגן ניצוץ (ATEX) ופינוי אוויר מחלקו העליון של החדר.", "ת״י 1001 / תקן NFPA 855 / IEEE 484", "הגדרת מפוח פליטה ייעודי מוגן ניצוץ בתקרה ושילוב גלאי מימן מחובר למערכת הבקרה.", "/home/yogi/lod_project/markup_hvac_07_battery_room.png", "מיזוג / חשמל")
    ]),
    ("פרק ג׳: מגדלי המגורים — מערכות על-לחץ בחדרי מדרגות, פירים ושחרור עשן", [
        ("HVAC-PRS-001", "כוח פתיחת דלתות מילוט במערכת על-לחץ במדרגות", "🔴 נדרש תיקון", "מגדל 321, קומות עליונות", "כוח פתיחת הדלת המחושב (215 N) חורג מקריטריון התכן בעת פעולת על-הלחץ.", "כוח פתיחה מופרז עלול לפגוע ביכולת השימוש והפתיחה של דלת המילוט בשעת חירום.", "כוח פתיחת דלת מירבי שלא יעלה על 133 N (והפרש לחצים בתחום 25–50 Pa).", "ת״י 1001 חלק 2.2 / תקן NFPA 92 / NFPA 101", "ויסות הלחץ באמצעות הזרקה רב-נקודתית, בקרת מהירות (VFD) ושסתומי פריקה ברומטריים.", "/home/yogi/lod_project/markup_hvac_08_stairwell_pressurization.png", "יועץ מיזוג"),
        ("HVAC-PRS-003", "מהירות זרימת אוויר בפיר אספקת על-לחץ", "🔴 נדרש תיקון", "פיר אספקה ראשי, מגדלים 321/339", "מהירות הזרימה המחושבת בפיר (23.3 מ\"ש) חורגת מההמלצות המקובלות לתעלות ופירי בטון.", "מהירות גבוהה גורמת למפלי לחץ מוגברים, שריקות זרימה ואי-איזון אספקת האוויר בין הקומות.", "מהירות זרימה מרבית מומלצת v ≤ 12.0 מ\"ש בפיר אספקה.", "ת״י 1001 חלק 2.2 / הנחיות תכן NFPA 92", "הגדלת שטח חתך הפיר בהתאם לספיקה הנדרשת להורדת מהירות הזרימה.", "/home/yogi/lod_project/markup_hvac_09_pressurization_shaft.png", "מיזוג + אדריכלות"),
        ("HVAC-COR-001", "בקרת דמפרי שחרור עשן במסדרונות קומתיים", "🔴 נדרש תיקון", "מסדרונות מילוט, קומות 1–18", "פתחי הפיר תוכננו ללא דמפרים ממונעים סגורים בשגרה (Normally Closed).", "פתיחה מקבילה של כל הקומות תדלל את ספיקת השאיבה בקומה שבה נדרש פינוי עשן.", "דמפרים ממונעים הנפתחים באופן מבוקר בקומה הרלוונטית בלבד.", "ת״י 1001 חלק 2.2 / תקן NFPA 92", "התקנת דמפרי עשן ממונעים 24V הנשלטים ע\"י רכזת גילוי האש לפתיחה ממוקדת בקומה הנדרשת.", "/home/yogi/lod_project/markup_hvac_10_corridor_smoke_exhaust.png", "יועץ מיזוג"),
        ("HVAC-LIFT-001", "על-לחץ בפיר מעלית לוחמי אש", "🔴 נדרש תיקון", "פיר מעלית כבאים, מגדלים 321/339", "לא הוגדרה מערכת על-לחץ ייעודית לפיר מעלית לוחמי האש.", "חדירת עשן לפיר המעלית עלולה להשבית את פעולת המעלית המשמשת את כוחות הכיבוי.", "אספקת על-לחץ ייעודית להגנה על פיר המעלית והמבואות המוגנות.", "תקן EN 81-72 / ת״י 1001.2.2 / EN 12101-6", "השלמת תכנון מערך על-לחץ עצמאי לפיר מעלית לוחמי האש בהתאם לדרישות התקן.", "/home/yogi/lod_project/markup_hvac_11_firefighters_lift_shaft.png", "יועץ מיזוג")
    ]),
    ("פרק ד׳: דירות מגורים ומסחר — VRF, ניקוז מי עיבוי, אוורור ושומן", [
        ("HVAC-CND-001", "שיפוע צנרת ניקוז מי עיבוי יחידות פנימיות", "🔴 נדרש תיקון", "דירות מגורים, תקרות גבס", "צנרת ניקוז מי עיבוי סומנה בשיפוע של כ-0.2% בלבד לאורך תוואי אופקי ממושך.", "שיפוע לא מספק עלול להביא להצטברות משקעים, סתימת הקו ונזקי רטיבות מעל תקרות הגבס.", "הקפדה על שיפוע גרביטציוני רציף s ≥ 1.5% (או התקנת משאבות ניקוז ייעודיות).", "ת״י 1205 / ת״י 920", "עדכון תוואי צנרת הניקוז להבטחת שיפוע תקני ושילוב סיפונים יבשים למניעת ריחות.", "/home/yogi/lod_project/markup_hvac_12_condensate_drainage.png", "יועץ מיזוג"),
        ("HVAC-REF-001", "בדיקת מגבלת ריכוז גז קירור בחדרי מגורים (RCL)", "🔴 נדרש תיקון", "חדרי שינה, מגדלים 321/339", "מערכת ה-VRF מכילה מטען גז משמעותי ללא מעגלים מפוצלים או אמצעי ניתוק.", "בעת דליפה מלאה של מטען הגז לחדר סגור קטן, הריכוז עלול לחרוג מסף הבטיחות של הגז.", "עמידה במגבלת ריכוז גז קירור (RCL) בחדר המאוכלס הקטן ביותר לפי סוג הגז.", "ת״י 920 / תקן EN 378 / ISO 5149", "פיצול מעגלי הקירור להקטנת המטען למעגל, או שילוב שסתומי ניתוק מהיר וגלאי דליפה ייעודיים.", "/home/yogi/lod_project/markup_hvac_13_refrigerant_rcl_safety.png", "יועץ מיזוג"),
        ("HVAC-WET-001", "אוורור חדרים רטובים ושסתומי מניעת חזרת ריחות", "🔴 נדרש תיקון", "חדרי רחצה ללא חלון חיצוני", "חיבור ישיר של מפוחים לפיר משותף ללא שסתומי אל-חוזר מתאימים.", "היעדר שסתומי אל-חוזר עלול לאפשר מעבר ריחות ואדי לחות בין דירות שונות המחוברות לאותו הפיר.", "התקנת שסתומי אל-חוזר אטומים ומפוחים בעלי מפלס רעש מותאם למבני מגורים.", "ת״י 1205.1 / ת״י 1004.3", "התקנת שסתומי אל-חוזר קפיציים אטומים ושדרוג המפוחים למפוחים מושתקים.", "/home/yogi/lod_project/markup_hvac_14_wet_rooms_ventilation.png", "מיזוג / אינסטלציה"),
        ("HVAC-KIT-001", "תעלות שומן ומערך כיבוי במנדפי מטבח מסחרי", "🔴 נדרש תיקון", "מטבחים ושטחי מסחר, מבנה 223", "תעלות השומן תוכננו מפח ספירלי רגיל ללא ריתוך אטום וללא מערכת כיבוי ייעודית במנדף.", "תעלות שאינן מרותכות עלולות לנזול שומן דליק בעת שריפה, ולהגביר את סיכון התפשטות האש.", "תעלות פלדה מרותכות באופן אטום נוזלים ומערכת כיבוי בכימיקל רטוב (UL 300) במנדף.", "ת״י 1001 חלק 6 / תקן NFPA 96", "שדרוג התעלות לפלדה שחורה מרותכת (1.5 מ\"מ) והתקנת מערכת כיבוי ייעודית במנדפים.", "/home/yogi/lod_project/markup_hvac_15_commercial_kitchen_grease.png", "יועץ מיזוג")
    ]),
    ("פרק ה׳: מרחבים מוגנים דירתיים (ממ״ד)", [
        ("HVAC-MMD-001", "מרחב תפעול סביב ידית הפעלה ידנית במערכת אב״כ", "🔴 נדרש תיקון", "ממ״דים, מגדלים 321/339", "המרחק שסומן בין ידית המנואלה לקיר/ארון קטן מ-1.00 מטר.", "חוסר מרחב תפעולי עלול להקשות על הפעלת המפוח הידני בשעת חירום ללא חשמל.", "שמירה על רדיוס תפעול פנוי של לפחות 1.00 מטר סביב ידית המפוח הידני.", "תקנות פיקוד העורף 2024 / ת״י 4570", "התאמת מיקום הריהוט והמערכת להבטחת רדיוס פנוי של 1.00 מטר.", "/home/yogi/lod_project/markup_hvac_16_mamad_cbrn_filtration.png", "מיזוג + אדריכלות"),
        ("HVAC-MMD-002", "שסתום פריקת לחץ הדף (Overpressure Blast Valve) בממ״ד", "🔴 נדרש תיקון", "קירות הדף חיצוניים בממ״ד", "לא הוגדר שסתום פריקת לחץ הדף תקני על גבי שרוול פליטת האוויר.", "הזרקת אוויר ללא פריקה מבוקרת תעלה את הלחץ הפנימי ותקשה על פתיחת הדלת והשהייה.", "שסתום פריקת לחץ הדף מכויל (50–100 Pa) הפונה לקיר חיצוני.", "תקנות פיקוד העורף / ת״י 448", "התקנת שסתום פריקת לחץ הדף מאושר פקע״ר ומיגון הפתח החיצוני מפני רסיסים.", "/home/yogi/lod_project/markup_hvac_17_mamad_blast_valves.png", "יועץ מיזוג"),
        ("HVAC-MMD-003", "שסתום הדף על קו ניקוז מזגן בממ״ד", "🔴 נדרש תיקון", "מעברי קירות ממ״ד", "קו ניקוז המזגן חוצה את קיר הממ״ד ללא שסתום הדף ייעודי (Type B).", "חציית קיר ללא שסתום הדף פוגעת באטימות הממ״ד בעת אירוע הדף חיצוני.", "התקנת שסתום הדף ייעודי מורשה פיקוד העורף על קו ניקוז המזגן.", "תקנות פיקוד העורף 2024 / ת״י 448", "התקנת שסתום הדף מאושר (דגם Type B) על קו ניקוז המזגן ואיטום המעבר באטם גזים תקני.", "/home/yogi/lod_project/markup_hvac_18_mamad_ac_blast_valve.png", "יועץ מיזוג")
    ]),
    ("פרק ו׳: סופרפוזיציה, אקוסטיקה ותמיכות סיסמיות", [
        ("HVAC-SUP-001", "התנגשות תעלת מיזוג בקורת שלד נושאת ומיגון ספרינקלר", "🔴 נדרש תיקון", "חניון מרתף 2-, קורה B-108", "תעלת אספקה רחבה חוצה בגובה קורת שלד נושאת וחוסמת פיזור ספרינקלר עליון.", "חיתוך בטון ללא תיאום פוגע בשלד; חסימת ספרינקלר מותירה שטח ללא כיבוי ישיר.", "תיאום מעבר מאושר בשלד והוספת ראשי ספרינקלר תחת תעלות שרוחבן עולה על 1.20 מטר.", "ת״י 466 / תקן NFPA 13 (Section 10.2.7)", "תיאום תוואי מאושר עם מהנדס השלד והוספת ראשי ספרינקלר תחת התעלה.", "/home/yogi/lod_project/markup_hvac_19_superposition_clashes.png", "מיזוג + קונסטרוקציה + כיבוי"),
        ("HVAC-ACS-001", "בידוד אקוסטי ושיכוך רעידות מציוד גג מעל דירות פנטהאוז", "🔴 נדרש תיקון", "מרפסת גג טכנית, מעל קומה 18", "צ'ילרים ומעבים מותקנים ללא משככי קפיץ ייעודיים וללא מיסוך אקוסטי.", "העברת ויברציות בתדר נמוך לשלד הבניין עלולה לגרום למפלסי רעש חריגים בחדרי השינה שמתחת.", "שיכוך רעידות יעיל ועמידה במפלס רעש מרבי מותר בחדרי מגורים (L_Aeq ≤ 30 dB).", "ת״י 1004 חלק 3 / תקנות למניעת מפגעים (רעש)", "התקנת משככי קפיץ סיסמיים מותאמים, בסיס אינרציה ומשתיקי קול תעלתיים.", "/home/yogi/lod_project/markup_hvac_20_acoustic_vibration_isolators.png", "יועץ אקוסטיקה + מיזוג"),
        ("HVAC-SEIS-001", "תמיכות סיסמיות לתעלות שחרור עשן כבדות", "🔴 נדרש תיקון", "חניון ופירים אנכיים", "תעלות שחרור עשן כבדות (חתך מעל 0.5 מ\"ר) תלויות על מוטות הברגה ללא חיזוק אלכסוני.", "היעדר ריסון סיסמי עלול לגרום לתנודות חופשיות ולכשל מערך התלייה באירוע רעידת אדמה.", "התקנת תמיכות סיסמיות רוחביות ואורכיות ועוגנים מאושרים לבטון סדוק.", "ת״י 413 / הנחיות SMACNA Seismic Restraint", "תכנון תמיכות אלכסוניות ב-45° ועוגנים סיסמיים בהתאם להנחיות התקן.", "/home/yogi/lod_project/markup_hvac_21_seismic_sway_bracing.png", "מיזוג + קונסטרוקציה")
    ])
]

# Generate Clean Structured Finding Cards with Embedded Images
all_actions_table_rows = []

for ch_idx, (ch_title, findings) in enumerate(chapters_content, start=1):
    p_ch = doc.add_paragraph()
    set_rtl(p_ch)
    r_ch = p_ch.add_run(ch_title)
    r_ch.font.name = 'David'
    r_ch.font.size = Pt(14)
    r_ch.font.bold = True
    r_ch.font.color.rgb = NAVY
    
    for f in findings:
        rule_id, name, status_str, loc, defect, impact, req, src, fix, img_path, responsible = f
        
        # Action Table Row Cache
        all_actions_table_rows.append((rule_id, name, status_str[:1], responsible, fix, "פתוח"))
        
        p_card_h = doc.add_paragraph()
        set_rtl(p_card_h)
        r_c_id = p_card_h.add_run(f"{rule_id} | {name}\n")
        r_c_id.font.name = 'David'
        r_c_id.font.size = Pt(12)
        r_c_id.font.bold = True
        r_c_id.font.color.rgb = NAVY
        
        r_c_st = p_card_h.add_run(f"סטטוס: {status_str}")
        r_c_st.font.name = 'David'
        r_c_st.font.size = Pt(11)
        r_c_st.font.bold = True
        r_c_st.font.color.rgb = CRIMSON if '🔴' in status_str else (ORANGE_COLOR if '🟡' in status_str else BLUE_COLOR)
        
        # 5-Field Clean Card Table
        t_card = doc.add_table(rows=6, cols=2)
        t_card.alignment = WD_TABLE_ALIGNMENT.CENTER
        
        card_fields = [
            ("מיקום במודל:", loc),
            ("הממצא שנמדד:", defect),
            ("משמעות הנדסית:", impact),
            ("דרישה / קריטריון תכן:", req),
            ("מקור תקן / אסמכתה:", src),
            ("המלצה והנחיית פעולה:", fix)
        ]
        
        for r_i, (k_txt, v_txt) in enumerate(card_fields):
            row = t_card.rows[r_i]
            
            c0 = row.cells[0]
            shd0 = parse_xml('<w:shd {} w:fill="F4F6F9"/>'.format(nsdecls('w')))
            c0._tc.get_or_add_tcPr().append(shd0)
            p0 = c0.paragraphs[0]
            set_rtl(p0)
            r0 = p0.add_run(k_txt)
            r0.font.name = 'David'
            r0.font.size = Pt(9.5)
            r0.font.bold = True
            r0.font.color.rgb = NAVY
            c0.width = Inches(2.2)
            
            c1 = row.cells[1]
            shd1 = parse_xml('<w:shd {} w:fill="FFFFFF"/>'.format(nsdecls('w')))
            c1._tc.get_or_add_tcPr().append(shd1)
            p1 = c1.paragraphs[0]
            set_rtl(p1)
            r1 = p1.add_run(v_txt)
            r1.font.name = 'David'
            r1.font.size = Pt(9.5)
            if r_i == 5:
                r1.font.bold = True
                r1.font.color.rgb = NAVY
            c1.width = Inches(4.5)
            
        doc.add_paragraph() # Spacer
        
        # Embed High-Res Markup Image
        if os.path.exists(img_path):
            p_img_t = doc.add_paragraph()
            set_rtl(p_img_t)
            r_it = p_img_t.add_run(f"תשריט ביקורת מתוך המודל — {rule_id}:")
            r_it.font.name = 'David'
            r_it.font.size = Pt(10.5)
            r_it.font.bold = True
            r_it.font.color.rgb = DARK_GRAY
            
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.add_run().add_picture(img_path, width=Inches(6.0))
            
        doc.add_paragraph() # Spacer between cards

# Section 4: Action Management Table
p_act_head = doc.add_paragraph()
set_rtl(p_act_head)
r_act_h = p_act_head.add_run('4. טבלת ריכוז פעולות ומעקב ליקויים (Action Items Table)')
r_act_h.font.name = 'David'
r_act_h.font.size = Pt(14)
r_act_h.font.bold = True
r_act_h.font.color.rgb = NAVY

t_act = doc.add_table(rows=len(all_actions_table_rows)+1, cols=6)
t_act.alignment = WD_TABLE_ALIGNMENT.CENTER
headers_act = ['מס׳ ממצא', 'נושא הממצא', 'חומרה', 'אחראי לטיפול', 'פעולה נדרשת לתיקון', 'סטטוס מעקב']
hdr_act_row = t_act.rows[0]
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

for a_idx, row_data in enumerate(all_actions_table_rows, start=1):
    row = t_act.rows[a_idx]
    r_id, r_name, r_sev, r_resp, r_fix, r_stat = row_data
    bg = 'FFF0F0' if '🔴' in r_sev else ('FFFDF0' if '🟡' in r_sev else 'F0F8FF')
    
    for col_i, cell_text in enumerate([r_id, r_name, r_sev, r_resp, r_fix, r_stat]):
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

doc.add_paragraph() # Spacer

# Section 5: Conclusion & Recommendations
p_conc_head = doc.add_paragraph()
set_rtl(p_conc_head)
r_conch = p_conc_head.add_run('5. מסקנות והמלצות בקרת התכן (Conclusions & Next Steps)')
r_conch.font.name = 'David'
r_conch.font.size = Pt(14)
r_conch.font.bold = True
r_conch.font.color.rgb = NAVY

p_conc_body = doc.add_paragraph()
set_rtl(p_conc_body)
conc_text = (
    "על בסיס התוכניות והמודלים שהועמדו לבדיקה, אותרו ממצאים המחייבים התייחסות ותיקון מצד צוות התכנון טרם קידום המערכות לביצוע באזורים הרלוונטיים.\n\n"
    "מומלץ להעביר את הממצאים למתכנני המערכות וליועצים הרלוונטיים, לקבל את התייחסותם ולהגיש גרסת תכנון מעודכנת לסבב בקרת תכן חוזר.\n\n"
    "ממצאים המסומנים באדום (🔴) מומלץ לסגור טרם ביצוע עבודות העלולות לקבע את המצב הקיים או להקשות על תיקונו."
)
r_concb = p_conc_body.add_run(conc_text)
r_concb.font.name = 'David'
r_concb.font.size = Pt(11)

doc.save(doc_path)
print("Client Final HVAC Master Report generated successfully at:", doc_path)
