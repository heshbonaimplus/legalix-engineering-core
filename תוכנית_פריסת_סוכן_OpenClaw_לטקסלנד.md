# Legalix TaxLand Autonomous OpenClaw Agent Deployment Plan
# תוכנית פריסה מהירה ב-3 שלבים (15 דקות סה״כ)

---

### ⏱️ לוח זמנים מפורט (15 דקות מקצה לקצה):

#### 1. שלב א' (5 דקות) — פריסת סביבת הסוכן על שרת הענן הקיים:
- הקמת תיקייה ייעודית מבודדת בשרת הענן (`/opt/legalix-taxland-agent`).
- משיכת קוד הליבה של OpenClaw מה-GitHub והגדרת סביבת Python וירטואלית.

#### 2. שלב ב' (5 דקות) — הטענת חליפת TaxLand (SOUL, Tools & Knowledge):
- הזרקת ה-`SOUL.md` המבוצר של TaxLand (תפקיד, סודיות, 100% RTL, איסור סטייה).
- חיבור ארגז הכלים הייעודי: `legalix_taxland_engine.py` (Numeric Core), פיצול 49ז, מחולל חוות דעת ב-Word.
- חיבור ישיר למאגר פסקי הדין והחלטות מיסוי מקרקעין 2026 (`real-estate-tax-db`).

#### 3. שלב ג' (5 דקות) — חיבור ה-MCP Server והפעלת שירות קבוע (Systemd):
- הגדרת שרת ה-MCP של סוכן TaxLand והרצת שירות קבוע (`legalix-taxland-agent.service`).
- עדכון ה-Action ב-ChatGPT כך שיפעיל את הסוכן האוטונומי בלייב!

---

### 🚀 תוצאה בסיום:
סוכן OpenClaw מלא, עצמאי ואוטונומי של TaxLand רץ 24/7 בענן, קורא חוזים ומפיק חוות דעת מושלמות!
EOF
