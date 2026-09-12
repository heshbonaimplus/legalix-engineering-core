# חוקת שרת ה-MCP המרכזי של Legalix — The Absolute Server-Side MCP Constitution
## פרוטוקול: החוקה, הכללים, 13 הסוכנים והטריגרים מוזרקים כולם בצד השרת בלבד (100% Server-Side)

---

### 🏛️ 1. העיקרון המנחה:
- אין צורך להעלות קבצים ידנית ל-Custom GPTs או לחפש תיבות הגדרות.
- **כל החוקה כולה מוזרקת ישירות לתוך קוד שרת ה-MCP בענן (`legalix_megacase_mcp_server.py`)**.
- כאשר כל מודל (Claude, ChatGPT, Cursor, וכו') מתחבר ל-MCP — השרת עצמו אוכף את החוקה, מציג את תיאורי הכלים המדויקים, ומחייב את הפעלת 13 הסוכנים!

---

### 🔌 2. הכלים שחשופים כעת ישירות בשרת ה-MCP בענן (GCP 35.242.250.144):

1. `legalix_mega_case_ingest(case_id, drive_folder_url)`:
   - קליטה מולטי-מודלית מ-Drive/Dropbox.
   - מנוע Vision OCR מואץ ברמת אות-אחר-אות.
   - ניתוב אטומי אוטומטי ל-13 המחסנים ב-Google Drive.

2. `legalix_query_13_agents_swarm(case_id, query, target_agent)`:
   - תשאול חדר המלחמה: עובדות, כספים, ציר זמן, סתירות, ראיות, תמלולים, פסיקה, Red Team, חקירה נגדית.
   - שליפה כירורגית מתוך קובצי ה-JSON המאונדקסים בדרייב.

3. `legalix_generate_court_pleading(case_id, pleading_type)`:
   - הפקת כתבי תביעה, בקשות לפי תקנה 91, ושאלות הבהרה ב-Word (DOCX) ב-100% RTL.

4. `legalix_get_system_constitution()`:
   - כלי שמחזיר למודל השפה את חוקת העל המלאה של Legalix (איסור תמצות, Zero-Trust, 13 הסוכנים).
EOF
