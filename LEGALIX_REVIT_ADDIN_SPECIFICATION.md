# Legalix Engineering — Revit Add-in Specification & Architecture Master
## מערכת תיקון אוטומטי בלחיצת כפתור בתוך Autodesk Revit (One-Click Auto-Remediation)

---

### 🏛️ 1. עקרונות המערכת
1. **התקנה פשוטה אצל המתכנן:** קובץ מניפסט `LegalixEngineering.addin` + ספריית קוד המותקנת בנתיב התוספים הרשמי של Autodesk:
   `%APPDATA%\Autodesk\Revit\Addins\2024\` (או 2023 / 2025).
2. **סרגל כלים ייעודי (Ribbon Panel):** תוספת לשונית עליונה ברוויט בשם **`Legalix Engineering`** הכוללת:
   * 🔍 **Auto-Audit Model:** סריקה מהירה של המודל הפתוח מול שרתי ה-API של Legalix.
   * 📋 **Dockable Panel (סרגל צד חכם):** הצגת כל הממצאים מקוטלגים לפי P1–P4.
   * 🎯 **Zoom & Section Box:** קפיצה תלת-ממדית והתמקדות מיידית באלמנט הנבדק.
   * ⚡ **One-Click Auto-Fix:** כפתור "קבל ותקן במודל" המבצע את הפעולה ב-Revit API Transaction.
   * 📊 **Export Rev 02 & Closure Report:** הנפקת דוח סגירת ממצאים מעודכן ואישור יציקות.

---

### 🛠️ 2. חמשת התיקונים האוטומטיים המובילים (Top 5 Auto-Fix Transactions):

#### 1. HVAC-JET-001 (כנפוני הטיה למפוח סילון):
```csharp
[Transaction(TransactionMode.Manual)]
public Result Execute(ExternalCommandData commandData, ref string message, ElementSet elements)
{
    Document doc = commandData.Application.ActiveUIDocument.Document;
    ElementId jetFanId = new ElementId(1048572); // Finding Element ID
    Element jetFan = doc.GetElement(jetFanId);

    using (Transaction t = new Transaction(doc, "Legalix: Fix Jet Fan Deflector Angle"))
    {
        t.Start();
        Parameter deflectorParam = jetFan.LookupParameter("Deflector_Angle");
        if (deflectorParam != null && !deflectorParam.IsReadOnly)
        {
            deflectorParam.Set(-5.0 * Math.PI / 180.0); // -5 degrees in Radians
        }
        t.Commit();
    }
    return Result.Succeeded;
}
```

#### 2. PLB-SLP-001 (תיקון שיפוע צנרת שופכין ל-1.50%):
```csharp
using (Transaction t = new Transaction(doc, "Legalix: Correct Pipe Slope to 1.5%"))
{
    t.Start();
    Pipe pipe = doc.GetElement(pipeId) as Pipe;
    if (pipe != null)
    {
        Parameter slopeParam = pipe.get_Parameter(BuiltInParameter.RBS_PIPE_SLOPE);
        slopeParam.Set(0.015); // 1.5% slope
    }
    t.Commit();
}
```

#### 3. ELEC-MMD-001 (הגבהת שקע אב״כ בממ״ד ל-+1.80 מטר):
```csharp
using (Transaction t = new Transaction(doc, "Legalix: Elevate CBRN Socket to +1.80m"))
{
    t.Start();
    FamilyInstance socket = doc.GetElement(socketId) as FamilyInstance;
    Parameter elevParam = socket.get_Parameter(BuiltInParameter.INSTANCE_ELEVATION_PARAM);
    elevParam.Set(1.80 / 0.3048); // Convert 1.80m to feet
    t.Commit();
}
```

#### 4. HVAC-CO-001 (הנמכת גלאי CO לגובה נשימה +1.50 מטר):
```csharp
using (Transaction t = new Transaction(doc, "Legalix: Lower CO Detector to +1.50m"))
{
    t.Start();
    FamilyInstance coDetector = doc.GetElement(coSensorId) as FamilyInstance;
    Parameter elevParam = coDetector.get_Parameter(BuiltInParameter.INSTANCE_ELEVATION_PARAM);
    elevParam.Set(1.50 / 0.3048); // 1.50m above floor
    t.Commit();
}
```

#### 5. ST-SLB-004 / ST-FND-006 (הזרקת חישוקי חדירה סביב עמוד):
```csharp
using (Transaction t = new Transaction(doc, "Legalix: Inject Punching Shear Stud Rails"))
{
    t.Start();
    FamilySymbol studRailSymbol = GetFamilySymbol(doc, "Punching_Stud_Rail_Ø12");
    XYZ columnLoc = (column.Location as LocationPoint).Point;
    
    // Inject 4 radial stud rails around column perimeter
    for (int angle = 0; angle < 360; angle += 90)
    {
        double rad = angle * Math.PI / 180.0;
        XYZ insertPt = columnLoc + new XYZ(Math.Cos(rad) * 0.40, Math.Sin(rad) * 0.40, 0);
        doc.Create.NewFamilyInstance(insertPt, studRailSymbol, slab, StructuralType.NonStructural);
    }
    t.Commit();
}
```

---
כל הזכויות שמורות © Legalix Engineering / עו״ד אלי עמר / עמר חנני.
