# ארכיטקטורת הפרדת מוצרים ומפתחות רישוי ב-MCP — Product Isolation & Role-Based Gateways
## איך מחלקים 3 כתובות MCP נפרדות ומאובטחות לכל סוג לקוח

---

### 🏛️ 1. שלוש נקודות קצה (Endpoints) נפרדות בשרת הענן:

בשרת הענן המרכזי של Legalix (`35.242.250.144`), מוגדרות **3 כתובות MCP נפרדות לחלוטין**:

1. 🏗️ **עבור לקוחות הנדסה (יזמים, קבלנים ומהנדסים):**
   * **כתובת ה-MCP שהלקוח מקבל:**  
     👉 `https://inclusion-refer-maintenance-associations.trycloudflare.com/mcp/engineering`
   * **מה הלקוח רואה בקלוד/צ'אט שלו:**  
     אך ורק את כלי בקרת התכן, ה-BIM והפיזיקה (`audit_structural_model`).
   * **חסימה הרמטית:** אפס גישה למיסוי ואפס גישה לתיקים משפטיים!

2. 🏛️ **עבור לקוחות מיסוי (רואי חשבון, יועצי מס ושמאי מקרקעין):**
   * **כתובת ה-MCP שהלקוח מקבל:**  
     👉 `https://inclusion-refer-maintenance-associations.trycloudflare.com/mcp/taxland`
   * **מה הלקוח רואה בקלוד/צ'אט שלו:**  
     אך ורק את סוכן המיסוי, 49ז וליניארי מוטב (`legalix_taxland_autonomous_agent`).
   * **חסימה הרמטית:** אפס גישה להנדסה ואפס גישה לליטיגציה!

3. ⚖️ **עבור לקוחות ליטיגציה (משרדי עורכי דין):**
   * **כתובת ה-MCP שהלקוח מקבל:**  
     👉 `https://inclusion-refer-maintenance-associations.trycloudflare.com/mcp/megacase`
   * **מה הלקוח רואה בקלוד/צ'אט שלו:**  
     אך ורק את חדר המלחמה, 13 הסוכנים ופיצוח התיקים (`legalix_mega_case`).
   * **חסימה הרמטית:** אפס גישה להנדסה ואפס גישה למיסוי כללי!

4. 👑 **עבורך (Master Admin):**  
   * **כתובת ה-Master הכוללת (הכתובת שחיברת עכשיו):**  
     👉 `https://inclusion-refer-maintenance-associations.trycloudflare.com/mcp`
   * אתה היחיד שרואה ומנהל את כל 3 העולמות יחד!
EOF
