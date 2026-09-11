import json
import os

electrical_rule_library = {
    "system_name": "Legalix Engineering Electrical & Low Voltage Rules Engine",
    "version": "2.0.0",
    "status_model": {
        "RED": "חובה לתקן — כשל קריטי / בטיחות חיים / התנגשות קשה בשלד (Life Safety & Hard Clash)",
        "YELLOW": "דורש החלטת יועץ / תיאום ביצוע מול קונסטרוקציה ואדריכלות (Engineering Coordination)",
        "BLUE": "המלצת אופטימיזציה / הנדסת ערך וחיסכון בעלויות ליזם (Value Engineering & Efficiency)",
        "GREEN": "נבדק במודל ואומת כתקין לפי התקן (Verified Compliant Pass)"
    },
    "engine_layers": {
        "Layer_1_Geometry_Engine": "מדידה גיאומטרית מדויקת מתוך RVT/IFC/DWG (התנגשויות, מרחקים, גבהים, סולמות כבלים, שרוולים)",
        "Layer_2_Rules_Engine": "השוואת נתוני המדידה מול ספי תכן וחוק החשמל במספרים מוחלטים (IF Condition -> Severity)",
        "Layer_3_AI_Synthesizer": "ניתוח הנדסי, הסבר מהות הכשל, אומדן עומסים והצעת פתרון כירורגי ליועץ"
    },
    "rules": [
        # --- פרק א: חניונים, לוחות ראשיים ותשתיות EV ---
        {
            "Rule_ID": "ELEC-MSB-001",
            "Discipline": "Electrical",
            "Sub_System": "Main_Switchboards",
            "Element_Type": "MSB_Panel",
            "Rule_Name": "כושר ניתוק בזרם קצר בלוח חשמל ראשי (Short-Circuit Breaking Capacity)",
            "Trigger_Condition": "MSB.BreakingCapacity_kA < Calculated_Isc_kA",
            "Standard_Threshold": "I_cu / I_cs >= 50 kA (at Transformer Secondary Terminals) per IEC 61439 / חוק החשמל",
            "Severity": "RED",
            "Standard_Source": "חוק החשמל / תקנות חח״י / IEC 61439-2",
            "Auto_Detectable_By_Geometry": False,
            "Required_Inputs": ["Transformer kVA & Impedance Z%", "Main Busbar Breaking Capacity Rating (kA)"],
            "Description_He": "כושר ניתוק נמוך של 25 kA מול זרם קצר צפוי של 42 kA יגרום לפיצוץ אלים של לוח החשמל הראשי והתכת פסי צבירה בעת קצר.",
            "Suggested_Remediation": "שדרוג מפסקי האוויר הראשיים (ACB) והמפסקים היצוקים (MCCB) לכושר ניתוק של לפחות 50 kA / 65 kA."
        },
        {
            "Rule_ID": "ELEC-FP-001",
            "Discipline": "Electrical",
            "Sub_System": "Fire_Safety_Power_Supply",
            "Element_Type": "Feeder_Circuit",
            "Rule_Name": "איסור התקנת ממסר פחת (RCD) במעגלי הזנת משאבות כיבוי אש ומפוחי עשן",
            "Trigger_Condition": "LifeSafetyCircuit.HasRCD == True",
            "Standard_Threshold": "Direct Feed WITHOUT Residual Current Device (RCD / פחת) per Electricity Law & SI 1596",
            "Severity": "RED",
            "Standard_Source": "חוק החשמל (התקנת לוחות) / ת״י 1596 / ת״י 1001 / NFPA 20",
            "Auto_Detectable_By_Geometry": False,
            "Required_Inputs": ["Single Line Diagram (SLD)", "Protection Device Type"],
            "Description_He": "התקנת מפסק מגן מזרם דלף (פחת) במעגל משאבת כיבוי תגרום להקפצת המשאבה בעת זרם זליגה שולי בשריפה — השבתת כלל הספרינקלרים במגדל!",
            "Suggested_Remediation": "ביטול ממסר הפחת במעגלי משאבות כיבוי ומפוחי עשן והסתמכות על הגנת מגנטי-בלבד (Magnetic Only) / התראת זליגה בלבד."
        },
        {
            "Rule_ID": "ELEC-EV-001",
            "Discipline": "Electrical",
            "Sub_System": "EV_Charging_Infrastructure",
            "Element_Type": "EV_Charger",
            "Rule_Name": "מערכת ניהול עומסים דינמית והגנת זרם ישר לעמדות טעינה (Dynamic Load Management & DC 6mA)",
            "Trigger_Condition": "EV_System.HasDLM == False OR EV_Charger.HasRDC_DD == False",
            "Standard_Threshold": "Dynamic Load Management (DLM) + RDC-DD (6mA DC) / Type B RCD per IEC 61851 / חוק החשמל",
            "Severity": "RED",
            "Standard_Source": "חוק החשמל (עמדות טעינה לרכב חשמלי) / IEC 61851 / ת״י 62752",
            "Auto_Detectable_By_Geometry": False,
            "Required_Inputs": ["Total EV Load (kW)", "Main Transformer Capacity", "Charger Protection Specs"],
            "Description_He": "טעינה בו-זמנית של עשרות רכבים ללא מערכת DLM תקריס את שנאי הבניין; ללא הגנת DC 6mA זרם זליגה ישתק את כל הפחתים במבנה.",
            "Suggested_Remediation": "התקנת מערכת ניהול עומסים דינמית (DLM) המגבילה את ההספק לשנאי, וממסרי מגן Type B או התקן RDC-DD 6mA בכל עמדה."
        },
        {
            "Rule_ID": "ELEC-GND-001",
            "Discipline": "Electrical",
            "Sub_System": "Grounding_Bonding",
            "Element_Type": "Equipotential_Bonding",
            "Rule_Name": "רציפות הארקת יסוד ועכבת לולאת תקלה (Loop Impedance Z_s)",
            "Trigger_Condition": "LoopImpedance_Zs * BreakerTripCurrent > 230.0",
            "Standard_Threshold": "Z_s <= U_0 / I_a (Ensuring disconnection within 5.0 sec / 0.4 sec) per Electricity Law",
            "Severity": "RED",
            "Standard_Source": "חוק החשמל (הארקות ואמצעי הגנה בפני חישמול)",
            "Auto_Detectable_By_Geometry": False,
            "Required_Inputs": ["Calculated Z_s (Ohms)", "Circuit Breaker Type & Rating (A)"],
            "Description_He": "עכבת לולאת תקלה גבוהה מונעת ניתוק אוטומטי של המפסק בעת קצר לאדמה — סכנת התחשמלות קטלנית וחישמול מעטפת הרכבים בחניון.",
            "Suggested_Remediation": "שילוב מוליכי הארקה בעלי חתך מוגדל, גישור לפס השוואת פוטנציאלים ראשי (פש״ח) ובדיקת רציפות הארקת יסוד בריתוך שלד."
        },

        # --- פרק ב: מערכות חירום, גנרציה ואל-פסק ---
        {
            "Rule_ID": "ELEC-ATS-001",
            "Discipline": "Electrical",
            "Sub_System": "Emergency_Power_ATS",
            "Element_Type": "ATS_Switch",
            "Rule_Name": "זמן מעבר ונעילה מכנית כפולה בלוח החלפה אוטומטי (ATS Transfer Time & Interlock)",
            "Trigger_Condition": "ATS.TransferTime_sec > 10.0 OR ATS.HasMechanicalInterlock == False",
            "Standard_Threshold": "Transfer Time t <= 10.0 sec + Dual Mechanical & Electrical Interlock per NFPA 110 Type 10",
            "Severity": "RED",
            "Standard_Source": "NFPA 110 (Type 10 Class 2) / חוק החשמל / ת״י 1001.4",
            "Auto_Detectable_By_Geometry": False,
            "Required_Inputs": ["ATS Specification Parameter: Transfer_Time", "Interlock_Type"],
            "Description_He": "היעדר נעילה מכנית כפולה עלול לגרום לחיבור במקביל של הגנרטור לרשת חח״י — קצר תלת-פאזי אדיר, שריפה וסיכון חיי עובדי חח״י.",
            "Suggested_Remediation": "התקנת לוח ATS בעל נעילה מכנית וחשמלית כפולה מובנית (4 קטבים) וזמן מעבר מדוד של פחות מ-10 שניות."
        },
        {
            "Rule_ID": "ELEC-CBL-001",
            "Discipline": "Electrical",
            "Sub_System": "Fire_Resistant_Cables",
            "Element_Type": "Power_Cable",
            "Rule_Name": "עמידות אש לכבלי הזנת מערכות מצילות חיים (Fire Resistant Cables PH120)",
            "Trigger_Condition": "LifeSafetyCable.FireRating < 120",
            "Standard_Threshold": "Class PH120 (300°C for 120 min) / FE180 (750°C for 180 min) per SI 1001 / IEC 60331",
            "Severity": "RED",
            "Standard_Source": "ת״י 1001 / חוק החשמל / הוראות כב״ה / IEC 60331",
            "Auto_Detectable_By_Geometry": False,
            "Required_Inputs": ["Cable Schedule Parameter: Fire_Rating_Minutes", "Circuit Service Type"],
            "Description_He": "שימוש בכבלים פלסטיים רגילים יגרום לשריפת המוליכים תוך 45 שניות בעת שריפה והשבתת מפוחי עשן, משאבות ומעליות כבאים.",
            "Suggested_Remediation": "שימוש בלעדי בכבלים נעדרי הלוגן עמידי אש (דגם N2XH-FE180/E90 או NHXH PH120) למערכות חירום."
        },
        {
            "Rule_ID": "ELEC-EMG-001",
            "Discipline": "Electrical",
            "Sub_System": "Emergency_Lighting",
            "Element_Type": "Exit_Sign_Fixture",
            "Rule_Name": "עוצמת הארה ומשך פעולה למערכות תאורת חירום ומילוט (Emergency Lighting Illumination)",
            "Trigger_Condition": "EmergencyLight.BatteryDuration_Hours < 3.0 OR Measured_Lux_Egress < 1.0",
            "Standard_Threshold": "Duration >= 180 min (3 hours) AND Illumination E >= 1.0 Lux along Egress path per SI 1838",
            "Severity": "RED",
            "Standard_Source": "ת״י 1838 (תאורת חירום) / ת״י 1220 / תקנות התכנון והבנייה",
            "Auto_Detectable_By_Geometry": True,
            "Required_Inputs": ["3D Emergency Lighting Layout", "Photometric Egress Calculation (Lux)", "Battery Duration"],
            "Description_He": "גופי תאורה עם מצבר לשעה אחת בלבד או עוצמת הארה מתחת ל-1 לוקס יגרמו לעלטה מוחלטת בנתיבי מילוט בעת שריפה ממושכת.",
            "Suggested_Remediation": "התקנת גופי תאורת חירום ושלטי יציאה מוארים LED בעלי מצבר ל-3 שעות (DALI Addressable) עם בדיקה אוטומטית."
        },

        # --- פרק ג: מגדלי מגורים ולוחות דירתיים ---
        {
            "Rule_ID": "ELEC-BUS-001",
            "Discipline": "Electrical",
            "Sub_System": "Vertical_Busbar_Risers",
            "Element_Type": "Busbar_Trunking",
            "Rule_Name": "מפל מתח מרבי בקצה עולה כוח במגדל 18 קומות (Maximum Voltage Drop)",
            "Trigger_Condition": "Calculated_Voltage_Drop_Percent > 3.0",
            "Standard_Threshold": "Voltage Drop Delta_V <= 3.0% from Main Board to furthest apartment DB per Electricity Law",
            "Severity": "RED",
            "Standard_Source": "חוק החשמל (העמסה והגנה של מוליכים) / ת״י 1087",
            "Auto_Detectable_By_Geometry": False,
            "Required_Inputs": ["Busbar / Cable Impedance (mOhm/m)", "Total Design Current (A)", "Riser Length (58m)"],
            "Description_He": "מפל מתח מעל 3% גורם להבהוב תאורה, תקלות במכשירי אינוורטר ו-VRF בדירות פנטהאוז והתחממות מוליכים בפיר.",
            "Suggested_Remediation": "הגדלת חתך פסי הצבירה (Busbar Trunking) מנחושת ל-1000A / 1250A או הוספת עולה כוח מפוצל לקומות 10–18."
        },
        {
            "Rule_ID": "ELEC-FST-001",
            "Discipline": "Electrical",
            "Sub_System": "Electrical_Shaft_Firestop",
            "Element_Type": "Shaft_Penetration",
            "Rule_Name": "איטום מעברי אש ועשן בפירי חשמל (Electrical Shaft Firestopping 120 min)",
            "Trigger_Condition": "ShaftPenetration.HasCertifiedFirestop == False",
            "Standard_Threshold": "Certified 120-minute Firestop Mortar / Sealant System per SI 931 / UL 1479",
            "Severity": "RED",
            "Standard_Source": "ת״י 931 / הוראות כב״ה / UL 1479",
            "Auto_Detectable_By_Geometry": True,
            "Required_Inputs": ["3D Electrical Shaft Floor Openings", "Firestop Sealant Detail"],
            "Description_He": "מעברי כבלים פתוחים בין קומות מייצרים 'אפקט ארובה' ומאפשרים התפשטות עשן שחור ואש לכל 18 הקומות בתוך שניות.",
            "Suggested_Remediation": "איטום כל חדירות התקרה בפיר החשמל בכריות אש ומסטיק תופח עמיד 120 דקות (Hilti Firestop CP 670 / CFS)."
        },
        {
            "Rule_ID": "ELEC-DB-001",
            "Discipline": "Electrical",
            "Sub_System": "Apartment_Distribution_Boards",
            "Element_Type": "Apartment_Panel",
            "Rule_Name": "הגנה מפני נחשולי מתח ומפסקי פחת בלוחות דירתיים (Surge Protection & RCDs)",
            "Trigger_Condition": "ApartmentDB.HasSPD == False OR ApartmentDB.AllCircuitsProtectedByRCD == False",
            "Standard_Threshold": "SPD Type 2 (Surge Protective Device) + 30mA RCDs protecting all socket circuits per Electricity Law",
            "Severity": "RED",
            "Standard_Source": "חוק החשמל / IEC 61643-11 / ת״י 60364",
            "Auto_Detectable_By_Geometry": False,
            "Required_Inputs": ["Apartment DB Single Line Diagram", "SPD Parameter", "RCD Protection Scheme"],
            "Description_He": "היעדר מגן ברקים SPD שורף כרטיסי אלקטרוניקה ומזגנים בדירות; היעדר פחת 30mA מהווה סכנת התחשמלות ישירה.",
            "Suggested_Remediation": "התקנת מגן נחשולי מתח SPD Type 2 בכניסה לכל לוח דירתי ומפסקי מגן RCD 30mA מפוצלים למניעת ניתוק כללי."
        },

        # --- פרק ד: מרחבים מוגנים (ממ״ד) ---
        {
            "Rule_ID": "ELEC-MMD-001",
            "Discipline": "Electrical",
            "Sub_System": "MAMAD_Electrical_Power",
            "Element_Type": "Power_Socket",
            "Rule_Name": "שקע כוח חירום ייעודי למערכת סינון אב״כ בממ״ד (CBRN Power Socket)",
            "Trigger_Condition": "MAMAD_Socket.Elevation_FFL < 1.70 OR MAMAD_Socket.ProtectedByRCD == True",
            "Standard_Threshold": "Dedicated Emergency Socket at +1.80m elevation WITHOUT RCD per Home Front Command Regulations 2024",
            "Severity": "RED",
            "Standard_Source": "תקנות פיקוד העורף 2024 (פקע״ר) / חוק החשמל",
            "Auto_Detectable_By_Geometry": True,
            "Required_Inputs": ["3D MAMAD Socket Coordinates", "Circuit Diagram (No RCD connection)"],
            "Description_He": "שקע בגובה נמוך או שקע המוזן דרך ממסר פחת עלול לקפוץ ולהשבית את מערכת סינון האב״כ בעת שהייה בממ״ד תחת מתקפה.",
            "Suggested_Remediation": "התקנת שקע כוח ייעודי בגובה +1.80 מטר ישירות מתחת למערכת הסינון המוזן ממעגל נפרד ללא ממסר פחת."
        },
        {
            "Rule_ID": "ELEC-MMD-002",
            "Discipline": "Electrical",
            "Sub_System": "MAMAD_Sleeves_Sealing",
            "Element_Type": "Sleeve_Seal",
            "Rule_Name": "איטום אב״כ מודולרי בשרוולי חשמל ותקשורת בממ״ד (Modular CBRN Gas Seals)",
            "Trigger_Condition": "MAMAD_ElectricalSleeve.HasModularSeal == False",
            "Standard_Threshold": "Certified Modular Gastight & Blast Seal (Roxtec R-Series / Hilti CFS) 1.5 bar per SI 448",
            "Severity": "RED",
            "Standard_Source": "תקנות פקע״ר 2024 / ת״י 448",
            "Auto_Detectable_By_Geometry": True,
            "Required_Inputs": ["3D Electrical Sleeve Geometry", "Modular Seal Specification Parameter"],
            "Description_He": "איטום סיליקון פשוט בשרוולי חשמל נפרץ בלחץ הדף ומאפשר חדירת גזים כימיים רעילים לתוך הממ״ד.",
            "Suggested_Remediation": "איטום כלל שרוולי החשמל, הטלפוניה והתקשורת בממ״ד באטמי אב״כ מודולריים תקניים (Roxtec R-75)."
        },

        # --- פרק ה: מערכות מתח נמוך וגילוי אש ---
        {
            "Rule_ID": "ELEC-FACP-001",
            "Discipline": "Low_Voltage",
            "Sub_System": "Fire_Alarm_Control_Panel",
            "Element_Type": "FACP_Panel",
            "Rule_Name": "מטריצת פיקוד בטיחות אש ברכזת גילוי אש ראשית (FACP Fire Command Matrix)",
            "Trigger_Condition": "FACP.MatrixInterlocksConfigured == False",
            "Standard_Threshold": "Fully Programmable Fire Command Matrix (Elevator Recall, Stairwell Fans, Smoke Dampers, Access Control) per SI 1220.3",
            "Severity": "RED",
            "Standard_Source": "ת״י 1220 חלק 3 / ת״י 1001 / NFPA 72",
            "Auto_Detectable_By_Geometry": False,
            "Required_Inputs": ["FACP Control Matrix Schedule", "Interface Modules List"],
            "Description_He": "היעדר מטריצת פיקוד אוטומטית ישאיר מעליות פעולות בשריפה, דלתות מילוט נעולות ומפוחי על-לחץ מושבתים.",
            "Suggested_Remediation": "תכנות והגדרת מטריצת פיקוד בטיחות אש מלאה ברכזת הכתובתית כולל כרטיסי ממשק ובקרת סוף מהלך."
        },
        {
            "Rule_ID": "ELEC-LPS-001",
            "Discipline": "Electrical",
            "Sub_System": "Lightning_Protection",
            "Element_Type": "Lightning_Rod",
            "Rule_Name": "מערכת הגנה מפני ברקים ברמה Level II במגדל 18 קומות (Lightning Protection System)",
            "Trigger_Condition": "Building.HasLPS == False OR LPS.ProtectionLevel != 'Level_II'",
            "Standard_Threshold": "LPS Level II Grid (10x10m mesh + Air Terminals + Down Conductors every 10m) per SI 1430 / IEC 62305",
            "Severity": "RED",
            "Standard_Source": "ת״י 1430 / IEC 62305 / NFPA 780",
            "Auto_Detectable_By_Geometry": True,
            "Required_Inputs": ["3D Roof Model", "LPS Air Terminals Coordinates", "Down Conductor Paths"],
            "Description_He": "מגדל בגובה 58 מטר ללא מערכת הגנת ברקים Level II חשוף לפגיעות ברק ישירות השורפות מערכות אלקטרוניות ומציתות אש בגג.",
            "Suggested_Remediation": "תכנון רשת קולטי ברקים מנחושת (גריד 10x10 מ') בגג, מוליכי הורדה כל 10 מטר ובדיקת שוויון פוטנציאלים."
        },

        # --- פרק ו: סופרפוזיציה, ריסון סיסמי ובדיקות מסירה ---
        {
            "Rule_ID": "ELEC-SUP-001",
            "Discipline": "Electrical",
            "Sub_System": "Cable_Tray_Superposition",
            "Element_Type": "Cable_Tray",
            "Rule_Name": "מרווחי אוויר בין סולמות כבלים לתעלות מיזוג וספרינקלרים (Cable Tray Clearances)",
            "Trigger_Condition": "Distance(CableTray, HVAC_Duct) < 0.30 OR CableTray.BottomElevation_FFL < 2.40",
            "Standard_Threshold": "Clearance >= 30cm from HVAC Ducts AND Headroom H_clear >= 2.40m per SI 1001 / NFPA 13",
            "Severity": "RED",
            "Standard_Source": "חוק החשמל / NFPA 13 / ת״י 1001",
            "Auto_Detectable_By_Geometry": True,
            "Required_Inputs": ["3D Cable Trays Model", "3D HVAC Ducts Model", "Floor Level FFL"],
            "Description_He": "סולמות כבלים צמודים לתעלות מיזוג חוסמים מניפות ספרינקלר ומורידים את גובה הראש בנתיבי הנסיעה מתחת ל-2.40 מטר.",
            "Suggested_Remediation": "שמירה על מרווח אוויר נקי של 30 ס\"מ מסולמות כבלים לתעלות מיזוג ותיאום גובה H_clear ≥ 2.45 מטר."
        },
        {
            "Rule_ID": "ELEC-SEIS-001",
            "Discipline": "Electrical",
            "Sub_System": "Seismic_Restraint",
            "Element_Type": "Tray_Bracing",
            "Rule_Name": "תמיכות סיסמיות אלכסוניות 45° לסולמות כבלים כבדים (Seismic Cable Tray Bracing)",
            "Trigger_Condition": "CableTray.Weight_kg_m >= 15.0 AND CableTray.HasSeismicBracing == False",
            "Standard_Threshold": "45° Steel Angle Bracing (Lateral <= 9.0m, Longitudinal <= 18.0m) per SI 413 / SMACNA",
            "Severity": "RED",
            "Standard_Source": "ת״י 413 / SMACNA / ASCE 7-16",
            "Auto_Detectable_By_Geometry": True,
            "Required_Inputs": ["3D Cable Tray Model", "Cable Tray Total Weight (kg/m)", "Support Coordinates"],
            "Description_He": "סולמות כבלים כבדים התלויים על מוטות הברגה בלבד יתנדנדו ברעידת אדמה, יקרעו כבלי חירום ויקריסו מערכות בטיחות.",
            "Suggested_Remediation": "התקנת תמיכות סיסמיות אלכסוניות 45° מזוויתן פלדה 40x40x4 מ\"מ ועוגני פלדה סיסמיים Hilti HST3."
        }
    ]
}

# Save JSON Rule Library
json_path = '/home/yogi/lod_project/ELECTRICAL_RULE_LIBRARY.json'
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(electrical_rule_library, f, ensure_ascii=False, indent=2)

print(f"Electrical Rule Library JSON generated successfully with {len(electrical_rule_library['rules'])} core rules at: {json_path}")
