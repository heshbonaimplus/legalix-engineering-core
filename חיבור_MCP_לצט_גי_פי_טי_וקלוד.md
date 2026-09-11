# מדריך חיבור שרת ה-MCP של Legalix ל-ChatGPT ו-Claude
## חיבור ישיר של מנועי ההנדסה, חוקי התכן וספריות הכללים לממשקי AI

---

### 🔌 1. איך לחבר את יוגי ו-Legalix ל-ChatGPT (OpenAI Custom GPT & Actions):

כדי להשתמש בכל מנועי הבקרה והחישובים ישירות מתוך ממשק ChatGPT הרגיל:

1. היכנס ל-**ChatGPT** בדפדפן ➔ לחץ על **Explore GPTs** ➔ **Create a GPT**.
2. בלשונית **Configure**:
   * **Name:** `Legalix Engineering Master Co-Pilot`
   * **Description:** `מערכת בקרת תכן הנדסית רב-תחומית (שלד, אינסטלציה, מיזוג, חשמל, פיתוח ומכר) מבית Legalix`.
   * **Instructions:** הזן את חוקת המערכת מתוך `LEGALIX_ENGINEERING_MASTER_BLUEPRINT.md`.
3. בחלק התחתון תחת **Actions** ➔ לחץ על **Create new action**:
   * חבר את כתובת ה-API של שרת ה-MCP של Legalix (או הפעלת ה-Bridge המקומי).
   * **תוצאה:** מופיעים בתוך ה-ChatGPT כפתורי הרצה ישירים לבדיקת מודלים, שליפת סעיפי חוק מהספר הכחול והפעלת פקודות Auto-Fix לרוויט!

---

### 🔌 2. איך לחבר את יוגי ל-Claude Desktop (במחשב שלך):

פרוטוקול **MCP (Model Context Protocol)** פותח במקור ע״י Anthropic עבור **Claude**, והחיבור אליו לוקח 30 שניות:

1. פתח את אפליקציית **Claude Desktop** במחשב שלך.
2. פתח את קובץ ההגדרות של קלוד (נמצא בנתיב: `%APPDATA%\Claude\claude_desktop_config.json` בווינדוס).
3. הוסף את בלוק ההגדרות של Legalix:

```json
{
  "mcpServers": {
    "legalix-engineering": {
      "command": "wsl.exe",
      "args": [
        "-e",
        "python3",
        "/home/yogi/lod_project/legalix_fastmcp_server.py"
      ]
    }
  }
}
```

4. סגור ופתח מחדש את Claude Desktop:
   * בצד ימין למטה בצ'אט של קלוד יופיע אייקון של **חיבור שרת MCP פעיל (ירוק)**!
   * כעת תוכל לשאול את קלוד: *"קלוד, תבדוק לי את מודל המיזוג"* — וקלוד יפעיל ישירות את המנועים של יוגי מאחורי הקלעים!

---

### 🛠️ הכלים הזמינים ב-MCP:
* `audit_bim_model` — הרצת בקרת תכן מלאה והפקת רשימת ליקויים מסווגת.
* `query_building_standards` — שליפת סעיפי תקן מאומתים לפי מהדורה מהספר הכחול ות״י.
* `execute_revit_autofix` — פקודת תיקון אוטומטית לקובץ הרוויט.
* `get_project_master_status` — שליפת תמונת מצב הפרויקטים והדוחות.

---
כל הזכויות שמורות © Legalix Engineering / עו״ד אלי עמר / עמר חנני.
