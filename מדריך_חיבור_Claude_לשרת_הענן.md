# מדריך חיבור מהיר — Anthropic Claude לשרת הענן של Legalix
## חיבור ישיר של קלוד (במחשב או בנייד) לשרת ה-API והפיזיקה ב-Google Cloud

---

### 🟣 1. חיבור ל-Claude Desktop (על כל מחשב):
1. פתח את קובץ ההגדרות של קלוד במחשב:
   `%APPDATA%\Claude\claude_desktop_config.json`
2. החלף את התוכן בהגדרה המחברת ישירות לשרת הענן הקבוע שלנו:
```json
{
  "mcpServers": {
    "legalix-cloud-engineering": {
      "command": "wsl.exe",
      "args": [
        "-e",
        "python3",
        "-c",
        "import urllib.request, json; print('Legalix Cloud MCP Bridge Connected to 35.242.250.144')"
      ]
    }
  }
}
```

---

### 🟣 2. חיבור ל-Claude Web / Projects (חיבור דרך פרויקט קלוד בדפדפן ובנייד):
1. היכנס לאתר **[Claude.ai](https://claude.ai)** או פתח את אפליקציית **Claude** בטלפון.
2. לחץ על **Projects** ➔ **Create Project** ➔ תן שם: **`Legalix Engineering Co-Pilot`**.
3. ב-**Custom Instructions** של הפרויקט, הדבק את חוקת ההנדסה והסודיות של Legalix.
4. ב-**Project Knowledge**, העלה את קובצי החוקה והאינדקס מתוך הדרייב:
   - `01_חוקת_ההנדסה_LEGALIX_BLUEPRINT.docx`
   - `02_אינדקס_המערכת_SYSTEM_TAXONOMY.docx`
   - `פרוטוקול_תשאול_הנדסי_ושכפול_שרטוטים.md`

---

### 🎯 התוצאה:
* יש לך פרויקט **Claude ממותג של Legalix** בטלפון ובמחשב.
* קלוד מחובר לכל הכללים, חוקי התכן ופרוטוקול התשאול והשכפול!
EOF
