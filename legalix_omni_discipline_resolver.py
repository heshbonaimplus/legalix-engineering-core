#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Legalix Omni-Discipline Knowledge & Card Resolver (Precision Ordered Matching)
"""

def resolve_discipline_payload(raw_query):
    q = (raw_query or "").lower().strip()
    
    # 1. LANDSCAPE & DRAINAGE (פיתוח נופי, ניקוז חצר, גינון, ספי לובי)
    if any(w in q for w in ["נוף", "פיתוח", "גינון", "חצר", "ספי לובי", "כבאית", "ניקוז חצר", "landscape"]):
        return {
            "status": "SUCCESS",
            "discipline": "פיתוח נופי, ניקוז חצר ותשתיות סביבה (Landscape & Site Drainage)",
            "project_name": "פרויקט לוד ניר צבי — עמרם אברהם",
            "model_audited": "Files_08- Landscape Engineer.zip",
            "total_findings": 16,
            "red_count": 14,
            "yellow_count": 1,
            "blue_count": 1,
            "hold_point": True,
            "critical_cards": [
                {
                    "id": "LND-FFL-001",
                    "title": "אי-הפרדת מפלס סף לובי מרוצף פיתוח (סכנת הצפה)",
                    "status": "🔴 RED",
                    "prio": "P1",
                    "effort": "15 דקות",
                    "location": "כניסה ראשית לובי מגדל 321 ומגדל 339",
                    "element": "סף כניסה ראשית FFL מול פיתוח חוץ",
                    "finding": "מפלס הריצוף הפנימי של הלובי תוכנן בגובה זהה לפיתוח החוץ (FFL=+0.00).",
                    "measured_val": "הפרש גובה: 0 ס\"מ",
                    "required_threshold": "הפרש גובה מינימלי: 3+ ס\"מ עם שיפוע נגר 1.5% כלפי חוץ ומגרעת ניקוז",
                    "delta": "חוסר מדרגת סף של 3 ס\"מ למניעת חדירת מי גשמים",
                    "impact": "הצפת לובי המגדלים ופירי המעליות בכל אירוע גשם חורפי!",
                    "standard_source": "ת״י 1918 חלק 2 (נגישות סביבה בנויה), ת״י 1205.3",
                    "recommended_action": "להגביה את מפלס הריצוף הפנימי ב-3 ס\"מ ולתכנן תעלת ניקוז סמויה עם רשת נירוסטה נגישה.",
                    "rev_update_instruction": "לעדכן בתוכניות פיתוח L-101 ובתוכנית אדריכלות כניסות A-100.",
                    "auto_closure_criterion": "סף כניסה מוגדר FFL_in >= FFL_out + 3cm עם שיפוע 1.5%."
                },
                {
                    "id": "LND-TRK-002",
                    "title": "רדיוס סיבוב בלתי מספק לרכב כיבוי אש סביב מגדל 321",
                    "status": "🔴 RED",
                    "prio": "P1",
                    "effort": "25 דקות",
                    "location": "כביש שירות ופיתוח צפון-מערבי מגדל 321",
                    "element": "נתיב גישת רכב כיבוי (Fire Truck Access Route)",
                    "finding": "רדיוס הפנייה הפנימי שורטט 8.50 מ' בלבד ללא מפרץ פריסה תקני.",
                    "measured_val": "רדיוס פנייה קיים: R = 8.50 מ'",
                    "required_threshold": "רדיוס סיבוב מינימלי: R_inner >= 12.50 מ' ורוחב נתיב 4.00 מ' per הוראות כבאות",
                    "delta": "חוסר של 4.00 מ' ברדיוס הסיבוב",
                    "impact": "רכב כיבוי אש כבד לא יוכל להסתובב ולהגיע למוקד שריפה במגדל!",
                    "standard_source": "הוראות נציב כבאות והצלה 502, תקנות התכנון והבנייה",
                    "recommended_action": "להרחיב את רדיוס עקומת הנסיעה ל-12.50 מ' על חשבון רצועת גינון סמוכה.",
                    "rev_update_instruction": "לעדכן בתוכנית תנועה ופיתוח L-002.",
                    "auto_closure_criterion": "Turning Radius R >= 12.50m מאומת בסימולציית AutoTURN."
                }
            ],
            "downloads": {
                "word_docx_url": "https://drive.google.com/file/d/1yGD83p1LFG8Vz_ZgYLLwbVVmGiuR8_uL/view?usp=sharing",
                "pdf_report_url": "https://drive.google.com/file/d/13VPfmd6GDCNjoQSeP81HWi5ndSCMJbz3/view?usp=sharing"
            },
            "summary": "בקרת תכן פיתוח נופי וניקוז חצר לפרויקט לוד ניר צבי הושלמה: 16 ממצאים (14 אדום). דוח Word מלא ו-PDF זמינים להורדה ישירה."
        }

    # 2. MARKETING VS BIM (מכר, שיווק, פלדיום, חוק המכר)
    elif any(w in q for w in ["מכר", "שיווק", "פלדיום", "חוק המכר", "חניה ליד קיר", "שטח דירה"]):
        return {
            "status": "SUCCESS",
            "discipline": "הצלבת תוכניות מכר מול ביצוע אדריכלי",
            "project_name": "פרויקט לוד ניר צבי — עמרם אברהם",
            "model_audited": "3D-Marketing.rvt / Lod_AR_321.rvt",
            "total_findings": 18,
            "red_count": 16,
            "yellow_count": 2,
            "blue_count": 0,
            "hold_point": True,
            "critical_cards": [
                {
                    "id": "MKT-PLD-001",
                    "title": "סטיית שטח פלדיום מחושב מול שטח מכר חוזי בדירות 4 חדרים",
                    "status": "🔴 RED",
                    "prio": "P1",
                    "effort": "20 דקות",
                    "location": "מגדל 321 ומגדל 339, דירות טיפוס 01 ו-02 (קומות 1-18)",
                    "element": "שטח עיקרי דירתי רשום במפרט מכר מול שטח ברוויט ביצוע",
                    "finding": "בתוכנית המכר נרשם שטח של 102.5 מ\"ר, בפועל במודל הביצוע השטח נטו הוא 98.2 מ\"ר.",
                    "measured_val": "סטיית שטח נמדדת: 4.3 מ\"ר (4.2%)",
                    "required_threshold": "סטייה מקסימלית מותרת לפי חוק המכר: 2.0%",
                    "delta": "חריגת שטח של 2.2% מעבר למותר בחוק",
                    "impact": "חשיפה מיידית לתביעות פיצויים מרוכשי הדירות (פיצוי כספי של כ-150,000 ש\"ח לכל דירה!)",
                    "standard_source": "חוק המכר (דירות) תשל״ג-1973, צו מכר דירות טופס 1",
                    "recommended_action": "לעדכן מיידית את תוכניות המכר החוזיות לשטח האמיתי או לתאם הסטת מחיצות פנים במודל האדריכלי.",
                    "rev_update_instruction": "לעדכן בנספח המכר החוזי ובתוכנית אדריכלות A-201.",
                    "auto_closure_criterion": "סטיית שטח <= 2.0% בין מודל הביצוע לחוזה המכר."
                }
            ],
            "downloads": {
                "word_docx_url": "https://drive.google.com/file/d/1VW2wrk-oOBIYxla-gm2nlNKY8b2ngfSu/view?usp=sharing",
                "pdf_report_url": "https://drive.google.com/file/d/182KoEYpZzOfnI5mbjShn8xLroCtAYXmf/view?usp=sharing"
            },
            "summary": "הצלבת תוכניות מכר מול ביצוע לפרויקט לוד ניר צבי הושלמה: 18 ממצאים (16 אדום). דוח Word מלא ו-PDF זמינים להורדה ישירה."
        }

    # 3. HVAC (מיזוג אויר, אוורור, שחרור עשן, מפוחי סילון)
    elif any(w in q for w in ["מיזוג", "hvac", "אוורור", "עשן", "מפוח", "סילון", "jet", "דמפר", "וילון"]):
        return {
            "status": "SUCCESS",
            "discipline": "מיזוג אוויר, אוורור ושחרור עשן (HVAC & Smoke Control)",
            "project_name": "פרויקט לוד ניר צבי — עמרם אברהם",
            "model_audited": "LOD_HV_ALL_R23.rvt / Files_03 - HVAC.zip",
            "total_findings": 22,
            "red_count": 21,
            "yellow_count": 0,
            "blue_count": 1,
            "hold_point": True,
            "critical_cards": [
                {
                    "id": "HVAC-JET-001",
                    "title": "חסימת סילון מפוח ע\"י קורת שלד יורדת B-101",
                    "status": "🔴 RED",
                    "prio": "P1",
                    "effort": "15 דקות",
                    "location": "חניון מרתף 2-, ציר F-8, מודל LOD_HV_ALL_R23",
                    "element": "מפוח סילון JF-08 (ספיקה 22 מ\"ש) מול קורת בטון יורדת B-101 בעומק 80 ס\"מ",
                    "finding": "מפוח הסילון מותקן במרחק 1.20 מ' בלבד מקורת בטון יורדת בעומק 80 ס\"מ ללא כנפוני הטיה.",
                    "measured_val": "מרחק 1.20 מ' מקורה יורדת 80 ס\"מ ללא כנפוני הטיה",
                    "required_threshold": "מרחק פנוי של 8.00 מ' או הטיית הסילון ב-5°- כלפי מטה מתחת לתחתית הקורה",
                    "delta": "פער של 6.80 מ' חסרים ללא כנפוני הטיה",
                    "impact": "סילון האוויר פוגע בקורה, נשבר ומערבל עשן וגזים רעילים כלפי מטה לתוך נתיב המילוט של הדיירים!",
                    "standard_source": "ת״י 1001 חלק 7 (שחרור עשן בחניונים), BS 7346-7 סעיף 8.4",
                    "recommended_action": "להתקין כנפוני הטיה מובנים בזווית 5°- כלפי מטה במפוח JF-08 או להרחיק את המפוח למרחק L >= 8.00 מ' מהקורה.",
                    "rev_update_instruction": "לעדכן במשפחת המפוח ברוויט פרמטר Deflector Vane Angle = -5° ובתוכנית מיזוג M-202.",
                    "auto_closure_criterion": "DeflectorAngle <= -5° OR Distance >= 8.0m בבדיקה חוזרת ב-Rev 02."
                }
            ],
            "downloads": {
                "word_docx_url": "https://drive.google.com/file/d/1UzmBVKxuIcxuZd1KStJWtW11xEQTrvb_/view?usp=sharing",
                "pdf_report_url": "https://drive.google.com/file/d/1hu249Si51s6qb1etSU7UJ4zqA6eZQ1k9/view?usp=sharing"
            },
            "summary": "בקרת תכן מיזוג אוויר ושחרור עשן לפרויקט לוד ניר צבי הושלמה: 22 ממצאים (21 אדום). דוח Word מלא ו-PDF זמינים להורדה ישירה."
        }

    # 4. ELECTRICAL (חשמל, מתח נמוך, מערכות חירום)
    elif any(w in q for w in ["חשמל", "electrical", "מתח נמוך", "לוח", "גנרטור", "תאורה", "ev", "שנאי"]):
        return {
            "status": "SUCCESS",
            "discipline": "חשמל, מתח נמוך ומערכות חירום",
            "project_name": "פרויקט לוד ניר צבי — עמרם אברהם",
            "model_audited": "LOD_EL_ALL_R25.rvt / Files_05 - Electrical.zip",
            "total_findings": 22,
            "red_count": 21,
            "yellow_count": 0,
            "blue_count": 1,
            "hold_point": True,
            "critical_cards": [
                {
                    "id": "ELEC-PUMP-001",
                    "title": "איסור מפסק פחת (RCD) בהזנת משאבות כיבוי אש",
                    "status": "🔴 RED",
                    "prio": "P1",
                    "effort": "10 דקות",
                    "location": "לוח חרום ראשי EM-MSB / חדר משאבות כיבוי",
                    "element": "מפסק מגן דלף RCD 300mA במעגל משאבת ספרינקלרים 75kW",
                    "finding": "הותקן מפסק מגן מזרם דלף (פחת) המנתק את ההזנה למשאבת הכיבוי הראשית.",
                    "measured_val": "קיים RCD 300mA עם ניתוק אוטומטי",
                    "required_threshold": "איסור ניתוק אוטומטי — התרעה בלבד ללא הפסקת הזנה",
                    "delta": "כשל בטיחותי חמור — איסור מוחלט על פחת במשאבות כיבוי",
                    "impact": "זליגת לחות רגעית תשבית את משאבת הכיבוי בזמן שריפה ותסכן חיי אדם!",
                    "standard_source": "חוק החשמל (התקנת לוחות), ת״י 1596, NFPA 20 סעיף 9.6",
                    "recommended_action": "לבטל את מפסק הפחת המנתק, ולהתקין משגוח בידוד / התרעה קולית-חזותית בלבד ללא ניתוק ההזנה.",
                    "rev_update_instruction": "לעדכן בתוכנית חד-קווית E-101 ובמפרט לוח EM-MSB.",
                    "auto_closure_criterion": "ביטול רכיב הפחת המנתק והחלפתו במפסק מגנטי בלבד (Magnetic Only MCP)."
                }
            ],
            "downloads": {
                "word_docx_url": "https://drive.google.com/file/d/1oBSdHsbB0l6LDNSR9dij6gNYOhbaAmRk/view?usp=sharing",
                "pdf_report_url": "https://drive.google.com/file/d/1TZaEBr5SeDoWCY3Ck2C9PBR6nrJRr6Up/view?usp=sharing"
            },
            "summary": "בקרת תכן חשמל ומתח נמוך לפרויקט לוד ניר צבי הושלמה: 22 ממצאים (21 אדום). דוח Word מלא ו-PDF זמינים להורדה ישירה."
        }

    # 5. PLUMBING (אינסטלציה סניטרית, כיבוי אש, מים, ביוב, שופכין)
    elif any(w in q for w in ["אינסטלציה", "ספרינקלר", "כיבוי", "הידרולוגיה", "ביוב", "שופכין", "prv", "משאבות כיבוי"]):
        return {
            "status": "SUCCESS",
            "discipline": "אינסטלציה סניטרית, הידרולוגיה וכיבוי אש",
            "project_name": "פרויקט לוד ניר צבי — עמרם אברהם",
            "model_audited": "LOD_PL_ALL_R25.rvt / Files_04 - Plumbing.zip",
            "total_findings": 30,
            "red_count": 27,
            "yellow_count": 2,
            "blue_count": 1,
            "hold_point": True,
            "critical_cards": [
                {
                    "id": "PLB-PRV-001",
                    "title": "לחץ הידרוסטטי עודף בברזים בקומות תחתונות (היעדר תחנות PRV)",
                    "status": "🔴 RED",
                    "prio": "P1",
                    "effort": "20 דקות",
                    "location": "מגדל 321, קומות 1 עד 6",
                    "element": "קו הזנת מים ראשי ולוחות מים קומתיים",
                    "finding": "לחץ המים בברזי הדירות בקומות 1-4 מגיע ל-7.2 bar ללא ויסות לחץ.",
                    "measured_val": "לחץ מדוד במודל: 7.2 bar",
                    "required_threshold": "לחץ מקסימלי מותר per הל״ת: 5.0 bar (מומלץ 3.5–4.0 bar)",
                    "delta": "עודף לחץ חמור של 2.2 bar (חריגה של 44%)",
                    "impact": "פיצוצי צנרת בדירות, פגיעה במכשירי חשמל ואיטום, והלם מים (Water Hammer) חריף!",
                    "standard_source": "הוראות למיתקני תברואה (הל״ת), ת״י 1205 חלק 1",
                    "recommended_action": "לתכנן מערכת חלוקה ל-3 אזורי לחץ (High, Mid, Low) עם תחנות ויסות לחץ PRV כפולות.",
                    "rev_update_instruction": "לעדכן בתוכנית סכמת מים ראשית PL-001.",
                    "auto_closure_criterion": "Static Pressure <= 5.0 bar בכל נקודות הקצה בדירות."
                }
            ],
            "downloads": {
                "word_docx_url": "https://drive.google.com/file/d/1Z4Hdos1icRO9eKqFfqp4ts7w2X5HVst6/view?usp=sharing",
                "pdf_report_url": "https://drive.google.com/file/d/1mjeH3HitY7XZtvh187LqG1YNmhBE4nZp/view?usp=sharing"
            },
            "summary": "בקרת תכן אינסטלציה וכיבוי אש לפרויקט לוד ניר צבי הושלמה: 30 ממצאים (27 אדום). דוח Word מלא ו-PDF זמינים להורדה ישירה."
        }

    # 6. STRUCTURE / DEFAULT (קונסטרוקציה, שלד, ביסוס, 321, 339)
    else:
        return {
            "status": "SUCCESS",
            "discipline": "קונסטרוקציה, שלד וביסוס",
            "project_name": "פרויקט לוד ניר צבי — עמרם אברהם",
            "model_audited": "Lod_ST_321_R25.rvt / Lod_ST_PR_R25.rvt",
            "total_findings": 38,
            "red_count": 36,
            "yellow_count": 2,
            "blue_count": 0,
            "hold_point": True,
            "critical_cards": [
                {
                    "id": "ST-TRN-001",
                    "title": "חוסר זיון ותת-תסבולת בקורת טרנספר ראשית TG-1",
                    "status": "🔴 RED",
                    "prio": "P3",
                    "effort": "45 דקות",
                    "location": "מגדל 321, קומה 1, ציר B/2-3",
                    "element": "קורת טרנספר TG-1 (חתך 120/180 ס״מ) תומכת 18 קומות",
                    "finding": "שורטטו 8 מוטות Ø25 בלבד בכפיפה תחתונה ללא כלובי גזירה מעובים.",
                    "measured_val": "זיון קיים: 39.3 סמ״ר (8Ø25)",
                    "required_threshold": "זיון תכן מחושב: 78.5 סמ״ר (16Ø25) + כלובי גזירה 4 ענפים Ø14@10",
                    "delta": "חוסר זיון קריטי של 49.9% בכפיפה ובגזירה תחת עומס 18 קומות",
                    "impact": "סכנת שקיעה מיידית, סדיקה עמוקה וכשל שלד בקומה הראשונה!",
                    "standard_source": "ת״י 466 חלק 1 (בטון מזוין), סעיף 9.2",
                    "recommended_action": "לבצע תכן מחדש ב-Strut-and-Tie, להכפיל את הזיון התחתון ל-16Ø25 ולהוסיף חישוקי גזירה 4 ענפים.",
                    "rev_update_instruction": "לעדכן בתוכנית קונסטרוקציה גיליון ST-102 ובמודל SAFE.",
                    "auto_closure_criterion": "שטח ברזל מתוכנן >= 78.5 סמ״ר ובדיקת כפיפה+גזירה D/C <= 1.0."
                }
            ],
            "downloads": {
                "word_docx_url": "https://drive.google.com/file/d/1adze8TVSSkGVRaTpBN4DBH-wW1iIjTkA/view?usp=sharing",
                "pdf_report_url": "https://drive.google.com/file/d/1cGDg9dLzV8nt1w2F-GVOLuQqKhxR9p-A/view?usp=sharing"
            },
            "summary": "בקרת תכן קונסטרוקציה למגדל 321 הושלמה: 38 ממצאים (36 אדום). דוח Word מלא ו-PDF זמינים להורדה ישירה."
        }

if __name__ == '__main__':
    for q_test in [
        "דוח בקרת תכן פיתוח נופי וניקוז חצר פרויקט ניר צבי",
        "בקרת תכן מיזוג אוויר ניר צבי",
        "הצלבת תוכניות מכר מול ביצוע",
        "אינסטלציה וספרינקלרים",
        "חשמל ומערכות חירום",
        "קונסטרוקציה ושלד"
    ]:
        res = resolve_discipline_payload(q_test)
        print(f"שאילתה: '{q_test}' ➔ נותב ל: '{res['discipline']}' (ממצאים: {res['total_findings']}) | Word: {res['downloads']['word_docx_url'][:35]}...")
