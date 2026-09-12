#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Legalix Omni-Discipline Knowledge & Card Resolver
מנוע החזרת נתוני אמת לכל 6 הדיסציפלינות של פרויקט לוד ניר צבי + Grand Master
"""

def resolve_discipline_payload(raw_query):
    q = (raw_query or "").lower().strip()
    
    # --- 1. HVAC / מיזוג אויר / אוורור / שחרור עשן ---
    if any(w in q for w in ["מיזוג", "hvac", "אוורור", "עשן", "מפוח", "סילון", "jet", "דמפר", "וילון"]):
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
                },
                {
                    "id": "HVAC-SUP-002",
                    "title": "חציית תעלת שחרור עשן ראשית דרך קורת בטון ראשית B-108",
                    "status": "🔴 RED",
                    "prio": "P2",
                    "effort": "תיאום יועצים (P2)",
                    "location": "מעבר חניון למגדל 321, ציר D-4",
                    "element": "תעלת פינוי עשן 1200x500 מ\"מ מול קורת בטון נושאת B-108",
                    "finding": "תוואי תעלת פינוי העשן חוצה ישירות את גוף קורת הבטון הראשית ללא שרוול מעבר מאושר.",
                    "measured_val": "התנגשות גיאומטרית קשה (Clash) של 100% בין התעלה לקורה",
                    "required_threshold": "מעבר מונמך תחת הקורה עם גובה ראש מינימלי 2.20 מ' או שרוול פלדה מתואם מראש",
                    "delta": "התנגשות שלד-מיזוג מלאה",
                    "impact": "קדיחה מאוחרת בקורה תפגע בזיון התחתון הראשי ותסכן את יציבות התקרה!",
                    "standard_source": "ת״י 466 חלק 1, ת״י 1001 חלק 7",
                    "recommended_action": "להנמיך את תוואי התעלה מתחת לקורה B-108, או להגדיר שרוול מעבר מלבני מתואם עם מהנדס הקונסטרוקציה.",
                    "rev_update_instruction": "לעדכן בתוכנית מיזוג M-101 ובתוכנית שלד ST-102.",
                    "auto_closure_criterion": "אפס התנגשויות (Zero Clash) בין תעלת העשן לקורת השלד בסופרפוזיציה."
                },
                {
                    "id": "HVAC-PRS-003",
                    "title": "היעדר שסתומי על-לחץ מבוקרים בפירי מדרגות מוגנים",
                    "status": "🔴 RED",
                    "prio": "P1",
                    "effort": "30 דקות",
                    "location": "חדר מדרגות מוגן מגדל 321 ומגדל 339",
                    "element": "מערכת דיחוס פיר מדרגות (Pressurization System)",
                    "finding": "לחץ הדיחוס המתוכנן עומד על 85 Pa ללא שסתומי שחרור לחץ (Barometric Dampers).",
                    "measured_val": "לחץ דיחוס מתוכנן: 85 Pa",
                    "required_threshold": "לחץ דיחוס תקני: 50 Pa (טווח מותר 25–50 Pa) וכוח פתיחת דלת <= 133 N",
                    "delta": "עודף לחץ של 35 Pa (חריגה של 70%)",
                    "impact": "דיירים וילדים לא יצליחו לפתוח את דלת המילוט בעת שריפה בגלל הפרש הלחצים!",
                    "standard_source": "ת״י 1001 חלק 2.2, NFPA 92 סעיף 4.4.2",
                    "recommended_action": "להתקין שסתומי ויסות לחץ ברומטריים (Pressure Relief Dampers) לכיול הלחץ ל-50 Pa בדיוק.",
                    "rev_update_instruction": "לעדכן במפרט המפוח ובתוכנית דיחוס M-401.",
                    "auto_closure_criterion": "Differential Pressure מוגדר בדיוק בטווח 25-50 Pa."
                }
            ],
            "downloads": {
                "word_docx_url": "https://drive.google.com/file/d/1UzmBVKxuIcxuZd1KStJWtW11xEQTrvb_/view?usp=sharing",
                "pdf_report_url": "https://drive.google.com/file/d/1hu249Si51s6qb1etSU7UJ4zqA6eZQ1k9/view?usp=sharing"
            },
            "summary": "בקרת תכן מיזוג אוויר ושחרור עשן לפרויקט לוד ניר צבי הושלמה: 22 ממצאים (21 אדום). דוח Word מלא ו-PDF זמינים להורדה ישירה."
        }

    # --- 2. PLUMBING & FIRE PROTECTION / אינסטלציה וכיבוי אש ---
    elif any(w in q for w in ["אינסטלציה", "ספרינקלר", "כיבוי", "מים", "ביוב", "שופכין", "ניקוז", "prv", "משאבות"]):
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
                },
                {
                    "id": "PLB-MMD-002",
                    "title": "חציית צנרת שופכין ודלוחין ראשית בקירות ממ״ד",
                    "status": "🔴 RED",
                    "prio": "P1",
                    "effort": "15 דקות",
                    "location": "דירות טיפוס 01 ו-02 בכל הקומות, קיר ממ״ד צפוני",
                    "element": "צינור שופכין ראשי Ø4\" (110 מ\"מ) מפלסטיק",
                    "finding": "צינור השופכין שורטט כשהוא חודר ועובר בתוך קיר הבטון של הממ״ד.",
                    "measured_val": "צינור שופכין חודר לקיר ממ״ד",
                    "required_threshold": "איסור מוחלט על מעבר צנרת שפכים ונוזלים בתוך קירות ממ״ד (למעט שרוול מעבר מוגן פקע״ר)",
                    "delta": "אי-עמידה מוחלטת בהוראות פיקוד העורף",
                    "impact": "פסילה מיידית של כל הממ״דים ע״י פקע״ר ועצירת קבלת טופס 4 לפרויקט!",
                    "standard_source": "תקנות פיקוד העורף 2024 (סעיף 3.4), ת״י 448",
                    "recommended_action": "להסיט את תוואי צינור השופכין אל מחוץ לשטח הממ״ד, לפיר אינסטלציה ייעודי בלובי.",
                    "rev_update_instruction": "לעדכן בתוכניות אינסטלציה קומתיות PL-101 עד PL-118.",
                    "auto_closure_criterion": "ביטול מלא של תוואי הצנרת בקירות הממ״ד במודל ה-BIM."
                }
            ],
            "downloads": {
                "word_docx_url": "https://drive.google.com/file/d/1Z4Hdos1icRO9eKqFfqp4ts7w2X5HVst6/view?usp=sharing",
                "pdf_report_url": "https://drive.google.com/file/d/1mjeH3HitY7XZtvh187LqG1YNmhBE4nZp/view?usp=sharing"
            },
            "summary": "בקרת תכן אינסטלציה וכיבוי אש לפרויקט לוד ניר צבי הושלמה: 30 ממצאים (27 אדום). דוח Word מלא ו-PDF זמינים להורדה ישירה."
        }

    # --- 3. ELECTRICAL & EMERGENCY / חשמל וחירום ---
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

    # --- 4. LANDSCAPE & DRAINAGE / פיתוח נופי וניקוז ---
    elif any(w in q for w in ["נוף", "פיתוח", "גינון", "חצר", "ספי לובי", "כבאית"]):
        return {
            "status": "SUCCESS",
            "discipline": "פיתוח נופי, ניקוז חצר ותשתיות סביבה",
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
                }
            ],
            "downloads": {
                "word_docx_url": "https://drive.google.com/file/d/1yGD83p1LFG8Vz_ZgYLLwbVVmGiuR8_uL/view?usp=sharing",
                "pdf_report_url": "https://drive.google.com/file/d/13VPfmd6GDCNjoQSeP81HWi5ndSCMJbz3/view?usp=sharing"
            },
            "summary": "בקרת תכן פיתוח נופי וניקוז חצר לפרויקט לוד ניר צבי הושלמה: 16 ממצאים (14 אדום). דוח Word מלא ו-PDF זמינים להורדה ישירה."
        }

    # --- 5. MARKETING VS BIM / הצלבת מכר מול ביצוע ---
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

    # --- 6. DEFAULT: STRUCTURAL DISCIPLINE / קונסטרוקציה ושלד ---
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
                },
                {
                    "id": "ST-FND-001",
                    "title": "עומס תגובת קרקע יתר על כלונסאות תחת קיר גזירה W-1",
                    "status": "🔴 RED",
                    "prio": "P3",
                    "effort": "30 דקות",
                    "location": "רפסודת ביסוס מגדל 321, ציר W-1",
                    "element": "כלונסאות ביסוס P-44 ו-P-45 בקוטר Ø100 ס״מ",
                    "finding": "עומס התכן המחושב על כלונס מגיע ל-4,645 kN מול תסבולת מורשית של 4,000 kN.",
                    "measured_val": "עומס פועל: 4,645 kN לכלונס",
                    "required_threshold": "תסבולת מורשית מדוח הקרקע: 4,000 kN",
                    "delta": "חריגת עומס של 645 kN (16.1% מעבר לכושר הנשיאה)",
                    "impact": "סכנת שקיעות קרקע לא אחידות וסדיקה אלכסונית ברפסודה!",
                    "standard_source": "ת״י 940 (ביסוס מבנים), דוח יועץ קרקע",
                    "recommended_action": "להוסיף 2 כלונסאות ביסוס מתחת למרכז קיר W-1 ולעדכן את מפת התגובות במודל SAFE.",
                    "rev_update_instruction": "להוסיף בתוכנית ביסוס ST-001 את כלונסאות P-44A ו-P-45A.",
                    "auto_closure_criterion": "עומס מקסימלי לכלונס <= 4,000 kN בהרצת SAFE מעודכנת."
                }
            ],
            "downloads": {
                "word_docx_url": "https://drive.google.com/file/d/1adze8TVSSkGVRaTpBN4DBH-wW1iIjTkA/view?usp=sharing",
                "pdf_report_url": "https://drive.google.com/file/d/1cGDg9dLzV8nt1w2F-GVOLuQqKhxR9p-A/view?usp=sharing"
            },
            "summary": "בקרת תכן קונסטרוקציה למגדל 321 הושלמה: 38 ממצאים (36 אדום). דוח Word מלא ו-PDF זמינים להורדה ישירה."
        }

if __name__ == '__main__':
    for test in ["מיזוג אוויר", "אינסטלציה", "חשמל", "נוף", "מכר", "שלד"]:
        res = resolve_discipline_payload(test)
        print(f"Test Query: '{test}' ➔ Returned Discipline: '{res['discipline']}' (Total findings: {res['total_findings']})")
