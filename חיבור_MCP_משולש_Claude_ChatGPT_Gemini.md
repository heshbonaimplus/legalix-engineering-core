# מדריך חיבור אחיד של שרת ה-MCP של Legalix לשלושת הענקים (ChatGPT, Claude, Gemini)

שרת ה-FastMCP שבנינו (`legalix_fastmcp_server.py`) תומך בתקן הפתוח הרשמי של **Model Context Protocol (MCP)**, ומאפשר חיבור מיידי ל-**Claude**, ל-**ChatGPT** ול-**Google Gemini** במקביל!

---

### 1. 🟣 חיבור ל-Claude (Anthropic Claude Desktop):
1. פתח את קובץ ההגדרות של קלוד במחשב:
   `%APPDATA%\Claude\claude_desktop_config.json`
2. הדבק את ההגדרה הבאה:
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
3. פתח מחדש את Claude ➔ **מופיעים כל כלי הבקרה והאנליזה בתוך קלוד!**

---

### 2. 🟢 חיבור ל-ChatGPT (OpenAI Custom GPT & Actions):
1. ב-ChatGPT ➔ **Explore GPTs** ➔ **Create/Edit GPT**.
2. בלשונית **Configure** ➔ **Actions**:
3. הדבק את הסכימה החיה מתוך `legalix_live_tunnel_schema_v2.json`.
4. שמור ב-`Anyone with a link` ➔ **ה-ChatGPT מחובר בלייב!**

---

### 3. 🔵 חיבור ל-Google Gemini (Gemini Function Calling & Extensions):
1. ב-Google AI Studio / Gemini Workspace Extension:
2. מחברים את כתובת ה-API של שרת ה-Live שלנו:
   `https://employment-sic-recognized-menu.trycloudflare.com`
3. מגדירים את ה-Function Calling Schema עבור `auditStructuralModel` ו-`queryStandards`.
4. **Gemini מקבל גישה ישירה לכל מנועי הפיזיקה וה-BIM של Legalix!**

---
כל הזכויות שמורות © Legalix Engineering.
