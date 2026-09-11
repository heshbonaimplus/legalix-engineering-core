import json
import os

plumbing_rule_library = {
    "system_name": "Legalix Engineering Plumbing & Fire Protection Rules Engine",
    "version": "2.0.0",
    "status_model": {
        "RED": "חובה לתקן — כשל קריטי / בטיחות חיים / התנגשות קשה בשלד (Life Safety & Hard Clash)",
        "YELLOW": "דורש החלטת יועץ / תיאום ביצוע מול קונסטרוקציה ואדריכלות (Engineering Coordination)",
        "BLUE": "המלצת אופטימיזציה / הנדסת ערך וחיסכון בעלויות ליזם (Value Engineering & Efficiency)",
        "GREEN": "נבדק במודל ואומת כתקין לפי התקן (Verified Compliant Pass)"
    },
    "engine_layers": {
        "Layer_1_Geometry_Engine": "מדידה גיאומטרית מדויקת מתוך RVT/IFC/DWG (התנגשויות, מרחקים, גבהים, שיפועים, שטחים)",
        "Layer_2_Rules_Engine": "השוואת נתוני המדידה מול ספי תכן ותקנים במספרים מוחלטים (IF Condition -> Severity)",
        "Layer_3_AI_Synthesizer": "ניתוח הנדסי, הסבר מהות הכשל, אומדן חריגה והצעת פתרון כירורגי ליועץ"
    },
    "rules": [
        # --- פרק א: מאגרי מים, שאיבה ותשתיות חניון ---
        {
            "Rule_ID": "PLB-TNK-001",
            "Discipline": "Plumbing",
            "Sub_System": "Water_Storage_Tanks",
            "Element_Type": "Separation_Wall",
            "Rule_Name": "דופן הפרדה בין מאגר מי שתייה למאגר כיבוי אש (Drinking vs Fire Water Separation)",
            "Trigger_Condition": "Tank.SeparationWallType == 'Single_Wall' AND Tank.HasCrystalAdmixture == False",
            "Standard_Threshold": "Double Wall with Air Gap OR Single W8/C40 Concrete with Crystalline Admixture + SI 5452 Coating",
            "Severity": "YELLOW",
            "Standard_Source": "הנחיות משרד הבריאות / ת״י 1205.2 / פרקטיקת שטח",
            "Auto_Detectable_By_Geometry": True,
            "Required_Inputs": ["3D Concrete Tank Model", "Wall Thickness (cm)", "Material Specification Parameter"],
            "Description_He": "דופן הפרדה בודדת ללא מוסף גבישי אטום עלולה לאפשר חלחול מים עומדים ממאגר הכיבוי למאגר מי השתייה של 255 הדירות.",
            "Suggested_Remediation": "הגדרת בטון אטום W8 / C40 עם מוסף גבישי קריסטלי ואיטום צמנטי מאושר מי שתייה לפי ת״י 5452, או דופן כפולה עם מרווח אוויר 30 ס\"מ."
        },
        {
            "Rule_ID": "PLB-TNK-002",
            "Discipline": "Plumbing",
            "Sub_System": "Water_Storage_Tanks",
            "Element_Type": "Overflow_Pipe",
            "Rule_Name": "קוטר צינור גלישת חירום במאגרי מים (Tank Overflow Sizing)",
            "Trigger_Condition": "OverflowPipe.Diameter_inch < 6 AND TotalInflowRate_Lpm > 500",
            "Standard_Threshold": "Overflow Diameter >= Ø6\" (150mm) for inflow Q >= 500 L/min per SI 1205.2",
            "Severity": "RED",
            "Standard_Source": "ת״י 1205.2 / ת״י 1596",
            "Auto_Detectable_By_Geometry": True,
            "Required_Inputs": ["3D Overflow Pipe Diameter", "Maximum Inflow Fill Rate (L/min)"],
            "Description_He": "צינור גלישה צר של Ø4\" אינו מסוגל לפרוק ספיקת מילוי בעת תקיעת מצוף — המים יעלו על גדותיהם ויציפו את חדר המשאבות ומרתף 2-.",
            "Suggested_Remediation": "הגדלת קוטר צינור הגלישה ל-Ø6\" (150 מ\"מ) עם משפך קליטה ומרווח אוויר (Air Gap) מעל בור הניקוז."
        },
        {
            "Rule_ID": "PLB-PMP-001",
            "Discipline": "Plumbing",
            "Sub_System": "Booster_Pumps",
            "Element_Type": "Suction_Pipe",
            "Rule_Name": "אורך מקטע יניקה ישר טרם כניסה למשאבה (Suction Straight Pipe Run)",
            "Trigger_Condition": "SuctionPipe.StraightLength < (5 * SuctionPipe.Diameter)",
            "Standard_Threshold": "Straight Run L >= 5 x Pipe Diameter (or 10x for High Flow) per NFPA 20 / Hydraulic Institute",
            "Severity": "RED",
            "Standard_Source": "NFPA 20 סעיף 4.14 / Hydraulic Institute Standards",
            "Auto_Detectable_By_Geometry": True,
            "Required_Inputs": ["3D Suction Pipe Centerline Length", "Pipe Diameter (mm)"],
            "Description_He": "מקטע ישר קצר מ-5 קטרים מייצר זרימה טורבולנטית בכניסת האימפלר, גורם לקוויטציה (Cavitation), שחיקת להבים והשבתת משאבות.",
            "Suggested_Remediation": "הארכת מקטע היניקה הישר ל-L ≥ 5D (לפחות 100 ס\"מ) טרם ברך הכניסה למשאבה."
        },
        {
            "Rule_ID": "PLB-PMP-002",
            "Discipline": "Plumbing",
            "Sub_System": "Fire_Pumps",
            "Element_Type": "Backup_Pump",
            "Rule_Name": "חובת משאבת כיבוי אש דיזל מונעת עצמאית במבנה רב-קומות (Diesel Fire Pump Backup)",
            "Trigger_Condition": "Building.Stories > 15 AND FirePumpingStation.HasDieselBackup == False",
            "Standard_Threshold": "100% Diesel Driven Fire Pump Backup (NFPA 20 / SI 1596)",
            "Severity": "RED",
            "Standard_Source": "ת״י 1596 / NFPA 20 / הוראות מכ״ר כב״ה",
            "Auto_Detectable_By_Geometry": False,
            "Required_Inputs": ["Building Height / Number of Stories", "Equipment Schedule: Fire_Pumps"],
            "Description_He": "הסתמכות על משאבה חשמלית בלבד במגדל 18 קומות משביתה את כל מערך הספרינקלרים בהפסקת חשמל בעת שריפה.",
            "Suggested_Remediation": "הוספת משאבת כיבוי אש מונעת מנוע דיזל עצמאי בגיבוי 100% כולל מיכל סולר יומי ומצברי התנעה כפולים."
        },
        {
            "Rule_ID": "PLB-RPZ-001",
            "Discipline": "Plumbing",
            "Sub_System": "Backflow_Prevention",
            "Element_Type": "RPZ_Valve",
            "Rule_Name": "מז״ח (מונע זרימה חוזרת) בהזנה ראשית למאגרי מים (RPZ Backflow Preventer)",
            "Trigger_Condition": "CityWaterFeed.HasRPZ == False",
            "Standard_Threshold": "Reduced Pressure Zone (RPZ) Device per Ministry of Health / SI 1205.2",
            "Severity": "RED",
            "Standard_Source": "תקנות בריאות העם / ת״י 1205.2",
            "Auto_Detectable_By_Geometry": True,
            "Required_Inputs": ["3D City Feed Pipe", "RPZ Valve Assembly"],
            "Description_He": "הזנת מאגרי מים וכיבוי אש ללא מז״ח מאפשרת שאיבה חוזרת של מים מזוהמים לרשת המים העירונית הראשית.",
            "Suggested_Remediation": "התקנת מערך מז״ח כפול במקביל (Dual RPZ) בור מונה המים הראשי בכניסה למבנה."
        },

        # --- פרק ב: ביוב, שאיבה וניקוז חניונים ---
        {
            "Rule_ID": "PLB-SEW-001",
            "Discipline": "Plumbing",
            "Sub_System": "Sewage_Pumping",
            "Element_Type": "Backwater_Loop",
            "Rule_Name": "לולאת מניעת הצפה חוזרת בסניקת שופכין (Inverted Backwater Loop)",
            "Trigger_Condition": "ForceMain.LoopTopElevation_FFL < 0.50",
            "Standard_Threshold": "Loop Crown Elevation >= +0.50m above street road level per SI 1205.1",
            "Severity": "RED",
            "Standard_Source": "ת״י 1205 חלק 1 (מערכות שפכים)",
            "Auto_Detectable_By_Geometry": True,
            "Required_Inputs": ["3D Force Main Geometry", "Street Road Level Elevation"],
            "Description_He": "חיבור אופקי ישיר לביוב העירוני ללא לולאה מעל מפלס הרחוב יגרום להצפת חניון מרתף 2- במי ביוב גולמיים בעת סתימה ברחוב.",
            "Suggested_Remediation": "העלאת קו הסניקה בלולאה אנכית (Backwater Loop) לגובה של לפחות 0.50 מטר מעל מפלס פני הכביש העירוני."
        },
        {
            "Rule_ID": "PLB-OIL-001",
            "Discipline": "Plumbing",
            "Sub_System": "Parking_Ramp_Drainage",
            "Element_Type": "Oil_Separator",
            "Rule_Name": "מפריד שמן ודלקים בקולטני רמפת חניון (Oil / Fuel Interceptor)",
            "Trigger_Condition": "RampDrainage.HasOilSeparator == False",
            "Standard_Threshold": "Class 1 Coalescence Oil Separator (< 5 mg/L) with automatic shutoff float per EN 858",
            "Severity": "RED",
            "Standard_Source": "תקנות המים (מניעת זיהום מים) / EN 858 / ת״י 1205.1",
            "Auto_Detectable_By_Geometry": True,
            "Required_Inputs": ["3D Ramp Trench Drains", "Oil Separator Unit"],
            "Description_He": "הזרמת מי נגר מרמפת החניון ללא מפריד שמן מזהמת את מערכת הניקוז העירונית בדלקים ושמנים ומהווה עבירה פלילית.",
            "Suggested_Remediation": "התקנת מפריד שמן קואלסנטי תקני (EN 858 Class 1) הכולל מצוף נעילה אוטומטי ורגש התראת שמן ב-BMS."
        },
        {
            "Rule_ID": "PLB-SLP-001",
            "Discipline": "Plumbing",
            "Sub_System": "Gravity_Sewer_Lines",
            "Element_Type": "Sewer_Pipe",
            "Rule_Name": "שיפוע מינימלי ומהירות שטיפה עצמית בקווי ביוב (Self-Cleansing Velocity)",
            "Trigger_Condition": "SewerPipe.Slope < 1.0 OR Calculated_Velocity < 0.70",
            "Standard_Threshold": "Slope s >= 1.0% AND Self-Cleansing Velocity v >= 0.70 m/s per SI 1205.1",
            "Severity": "RED",
            "Standard_Source": "ת״י 1205 חלק 1",
            "Auto_Detectable_By_Geometry": True,
            "Required_Inputs": ["3D Sewer Pipe Slope", "Pipe Diameter", "Flow Rate (L/s)"],
            "Description_He": "שיפוע של 0.5% מייצר מהירות 0.42 מ\"ש בלבד — שקיעת מוצקים, הצטברות מגבונים וסתימות ביוב כרוניות בחניון.",
            "Suggested_Remediation": "הקפדה על שיפוע גרביטציוני s ≥ 1.0% (ו-1.5% לקווי דלוחין) להבטחת מהירות שטיפה עצמית v ≥ 0.70 מ\"ש."
        },

        # --- פרק ג: אספקת מים ואזורי לחץ במגדלים ---
        {
            "Rule_ID": "PLB-PRS-001",
            "Discipline": "Plumbing",
            "Sub_System": "Water_Supply_Zones",
            "Element_Type": "Pressure_Zone",
            "Rule_Name": "לחץ מים סטטי מרבי בדירות מגורים (Maximum Fixture Static Pressure)",
            "Trigger_Condition": "Fixture_Static_Pressure > 5.0",
            "Standard_Threshold": "Static Pressure P_static <= 5.0 bar (Target 3.0 - 4.0 bar) per SI 1205.2",
            "Severity": "RED",
            "Standard_Source": "ת״י 1205 חלק 2 (אספקת מים) / DIN 1988",
            "Auto_Detectable_By_Geometry": False,
            "Required_Inputs": ["Booster System Discharge Pressure (bar)", "Floor Elevation FFL", "Fixture Elevation"],
            "Description_He": "הזנה באזור לחץ יחיד במגדל 18 קומות מייצרת לחץ של 9.9 בר בקומות תחתונות — פיצוץ גמישים, רעשי הלם והצפת דירות.",
            "Suggested_Remediation": "חלוקת המגדל ל-3 אזורי לחץ נפרדים (קומות 1–6, 7–12, 13–18) באמצעות תחנות הפחתת לחץ (PRV)."
        },
        {
            "Rule_ID": "PLB-PRV-001",
            "Discipline": "Plumbing",
            "Sub_System": "Pressure_Reducing_Stations",
            "Element_Type": "PRV_Station",
            "Rule_Name": "יתירות שסתומי הפחתת לחץ ושסתום ביטחון (Dual PRV & Safety Relief)",
            "Trigger_Condition": "PRV_Station.IsDualParallel == False OR PRV_Station.HasReliefValve == False",
            "Standard_Threshold": "Dual Parallel PRV (Duty/Standby) + Safety Relief Valve (5.5 bar) per SI 1205.2",
            "Severity": "RED",
            "Standard_Source": "ת״י 1205.2 / DIN 1988",
            "Auto_Detectable_By_Geometry": True,
            "Required_Inputs": ["3D PRV Assembly Elements"],
            "Description_He": "שסתום PRV בודד ללא גיבוי ישבית את אספקת המים לקומות שלמות בעת טיפול, ופריצת דיאפרגמה תפוצץ צנרת בדירות.",
            "Suggested_Remediation": "תכנון תחנת PRV כפולה במקביל (Dual Parallel) עם שסתום פריקת לחץ ביטחון (5.5 בר) ומסנני Y."
        },
        {
            "Rule_ID": "PLB-REC-001",
            "Discipline": "Plumbing",
            "Sub_System": "Hot_Water_Recirculation",
            "Element_Type": "Hot_Water_Return",
            "Rule_Name": "זמן המתנה מקסימלי למים חמים בברז (Hot Water Waiting Time)",
            "Trigger_Condition": "Calculated_Waiting_Time > 15.0",
            "Standard_Threshold": "Waiting Time T_wait <= 15.0 sec (SI 1205.2 / SI 579)",
            "Severity": "RED",
            "Standard_Source": "ת״י 1205.2 / ת״י 579 (מערכות סולאריות)",
            "Auto_Detectable_By_Geometry": False,
            "Required_Inputs": ["Piping Distance from Riser to Furthest Tap", "Pipe Diameter", "Flow Rate"],
            "Description_He": "זמן המתנה מעל 120 שניות בקומות עליונות ללא קו סחרור חוזר גורם לבזבוז של 35 ליטר מים קרים בכל מקלחת.",
            "Suggested_Remediation": "פריסת קו סחרור מים חמים חוזר (HW-R Ø1\") עם שסתומי איזון תרמוסטטיים (55°C) בכל קומה."
        },

        # --- פרק ד: כיבוי אש, ספרינקלרים ועמדות כיבוי ---
        {
            "Rule_ID": "FP-SPK-001",
            "Discipline": "Fire_Protection",
            "Sub_System": "Sprinkler_Layout",
            "Element_Type": "Sprinkler_Head",
            "Rule_Name": "חסימת מניפת ספרינקלר ע\"י קורות שלד יורדות (Beam Rule Obstruction)",
            "Trigger_Condition": "Sprinkler.DistanceToBeam < (3.0 * Beam.DropDepth)",
            "Standard_Threshold": "Beam Rule Table compliance per NFPA 13 (Section 8.6.5.1) / SI 1596",
            "Severity": "RED",
            "Standard_Source": "ת״י 1596 / NFPA 13",
            "Auto_Detectable_By_Geometry": True,
            "Required_Inputs": ["3D Sprinkler Head Coordinates", "3D Structural Beam Solids", "Beam Drop Depth"],
            "Description_He": "ספרינקלר במרחק 30 ס\"מ מקורה יורדת בעומק 80 ס\"מ נחסם לחלוטין ומייצר שטח צל יבש ברוחב 4.5 מטר ללא כיבוי.",
            "Suggested_Remediation": "הרחקת ראשי הספרינקלר בהתאם לטבלת ה-Beam Rule של NFPA 13 או הוספת שורת ראשים תחת הקורה."
        },
        {
            "Rule_ID": "FP-SPK-002",
            "Discipline": "Fire_Protection",
            "Sub_System": "Sprinkler_Density",
            "Element_Type": "Sprinkler_Grid",
            "Rule_Name": "שטח כיסוי מירבי לראש ספרינקלר בחניון (Coverage Area per Head OH2)",
            "Trigger_Condition": "Sprinkler.CoverageArea > 12.1",
            "Standard_Threshold": "Coverage Area A <= 12.1 m² (130 sq ft) per Head (Ordinary Hazard Group 2)",
            "Severity": "RED",
            "Standard_Source": "ת״י 1596 / NFPA 13",
            "Auto_Detectable_By_Geometry": True,
            "Required_Inputs": ["Sprinkler Spacing S (m)", "Sprinkler Spacing L (m)"],
            "Description_He": "שטח כיסוי של 20.2 מ\"ר לראש (מרווח 4.8x4.2 מ') מדלל את ספיקת המים ומונע כיבוי של שריפת רכבים מודרניים.",
            "Suggested_Remediation": "תכנון מחדש של גריד הספרינקלרים למרווח מרבי S ≤ 3.50 מטר ושטח כיסוי A ≤ 12.1 מ\"ר לראש (K=8.0)."
        },
        {
            "Rule_ID": "FP-CAB-001",
            "Discipline": "Fire_Protection",
            "Sub_System": "Fire_Hose_Cabinets",
            "Element_Type": "Hose_Cabinet",
            "Rule_Name": "רדיוס כיסוי גלגלון כיבוי אש (Fire Hose Coverage Radius)",
            "Trigger_Condition": "WalkingDistanceToFurthestPoint > 30.0",
            "Standard_Threshold": "Maximum Hose Reach <= 30.0m per SI 1933",
            "Severity": "RED",
            "Standard_Source": "ת״י 1933 / תקנות התכנון והבנייה / כב״ה",
            "Auto_Detectable_By_Geometry": True,
            "Required_Inputs": ["3D Cabinet Location", "Floor Plan Walking Path Network"],
            "Description_He": "מרחק הליכה של 42 מטר מותיר שטחים מתים בפינות החניון שבהם רכבים בוערים יישארו ללא מענה כיבוי.",
            "Suggested_Remediation": "הוספת עמדות כיבוי משולבות נוספות במבואות מוגנות להבטחת כיסוי מלא ברדיוס גלגלון של 30 מטר."
        },
        {
            "Rule_ID": "FP-RIS-001",
            "Discipline": "Fire_Protection",
            "Sub_System": "Combined_Standpipe_Risers",
            "Element_Type": "Standpipe_Riser",
            "Rule_Name": "קוטר עולה סניקה משולב במבנה מעל 4 קומות (Combined Standpipe Diameter)",
            "Trigger_Condition": "CombinedRiser.Diameter_inch < 6 AND Building.Stories > 4",
            "Standard_Threshold": "Diameter >= Ø6\" (150mm / Schedule 40) per NFPA 14 (Section 7.6)",
            "Severity": "RED",
            "Standard_Source": "NFPA 14 / ת״י 1596 / כב״ה",
            "Auto_Detectable_By_Geometry": True,
            "Required_Inputs": ["3D Combined Riser Diameter", "Building Stories"],
            "Description_He": "עולה סניקה בקוטר Ø4\" אינו מסוגל לספק ספיקה של 1,000 GPM (3,800 ליטר/דקה) הנדרשת להפעלת זרנוקי כבאים במגדל.",
            "Suggested_Remediation": "שדרוג עולי הסניקה המשולבים לקוטר Ø6\" (150 מ\"מ Schedule 40) פלדה ללא תפר."
        },
        {
            "Rule_ID": "FP-RES-001",
            "Discipline": "Fire_Protection",
            "Sub_System": "Residential_Sprinklers",
            "Element_Type": "Sprinkler_Head",
            "Rule_Name": "סוג ראשי ספרינקלר בדירות מגורים (Residential Quick Response)",
            "Trigger_Condition": "ApartmentSprinkler.Type != 'Residential_Quick_Response'",
            "Standard_Threshold": "Concealed Flat Plate Residential Quick-Response (RTI <= 50) per NFPA 13R / SI 1596",
            "Severity": "RED",
            "Standard_Source": "ת״י 1596 / NFPA 13R",
            "Auto_Detectable_By_Geometry": False,
            "Required_Inputs": ["Apartment Sprinkler Schedule Parameter: Head_Type", "RTI_Rating"],
            "Description_He": "ראשי Standard Response גלויים נפתחים באיחור של דקות קריטיות בשריפה דירתית — סכנת שאיפת עשן וחנק.",
            "Suggested_Remediation": "שדרוג כל ראשי הספרינקלרים בדירות לראשי תגובה מהירה סמויים (Concealed Flat Plate 57°C / RTI ≤ 50)."
        },
        {
            "Rule_ID": "PLB-MMD-001",
            "Discipline": "Plumbing",
            "Sub_System": "MAMAD_Penetrations",
            "Element_Type": "Pipe_Penetration",
            "Rule_Name": "איסור חציית צנרת ביוב/ניקוז זרה בקירות ממ״ד (Prohibited Foreign Pipes in Shelter)",
            "Trigger_Condition": "Pipe.CrossesMAMADWall == True AND Pipe.ServiceType != 'MAMAD_Dedicated'",
            "Standard_Threshold": "Zero Prohibited Foreign Pipes crossing MAMAD per Home Front Command Regulations 2024",
            "Severity": "RED",
            "Standard_Source": "תקנות פיקוד העורף 2024 (פקע״ר) / ת״י 448",
            "Auto_Detectable_By_Geometry": True,
            "Required_Inputs": ["3D Pipes Model", "3D MAMAD Solid Walls"],
            "Description_He": "צנרת שופכין של דירה עליונה החוצה קיר ממ\"ד מהווה עבירה חמורה על תקנות פקע״ר ופוסלת קבלת טופס 4.",
            "Suggested_Remediation": "הסטה מוחלטת של כל צנרת שופכין, דלוחין וצמ״גים אל מחוץ לשטח הממ״דים והעברתה בפירים בלבד."
        }
    ]
}

# Save JSON Rule Library
json_path = '/home/yogi/lod_project/PLUMBING_RULE_LIBRARY.json'
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(plumbing_rule_library, f, ensure_ascii=False, indent=2)

print(f"Plumbing Rule Library JSON generated successfully with {len(plumbing_rule_library['rules'])} core rules at: {json_path}")
