# ארכיטקטורת זיכרון מתמיד ופרויקטים ייעודיים — Projects & Custom GPTs Stateful Workspace
## איך נועלים סביבת עבודה קבועה ב-Claude Projects וב-ChatGPT Custom GPTs שלא נמחקת לעולם

---

### 🏛️ 1. למה צ'אט רגיל "נמחק" ולמה Projects / Custom GPT פותרים את זה לתמיד:

* **בצ'אט רגיל:** כעבור כמה ימים או בפתיחת חלון חדש — ההקשר אובד, ה-Connectors לא נטענים אוטומטית, והמשתמש צריך להסביר הכל מחדש.
* **ב-Claude Project / ChatGPT Custom GPT:**
  1. **זיכרון קבוע ומתמיד (Stateful Vault):** הפרויקט שומר את כל היסטוריית השיחות, קובצי ההוראות וחיבורי ה-MCP.
  2. **נעילת הלקוח למערכת הרצויה בלבד:** הלקוח נכנס ישירות לפרויקט של `Legalix Mega-Case` ➔ וקלוד פיזית אינו יכול לחפש בשום מקום אחר!
  3. **המשך עבודה מאותה נקודה:** הלקוח חוזר לפרויקט אחרי חצי שנה — וכל התיקים, הסתירות, ציר הזמן והמסמכים מחכים לו בדיוק באותה נקודה שעצר.

---

### 🚀 2. איך בונים ומגדירים את 3 הפרויקטים הקבועים ב-Claude (קלוד):

ב-Claude (באתר [Claude.ai](https://claude.ai) או באפליקציה בטלפון):

#### 📁 פרויקט 1: `Legalix Mega-Case War-Room` (עבור עורכי דין וליטיגציה)
* **Custom Instructions:** חוקת ה-Mega-Case, חובת הפעלת `legalix_mega_case`, ואיסור תשובות מהראש.
* **Connected MCP:** מחובר בלעדית ל-`Legalix Mega-Case`.
* **תוצאה:** כל תיק שהלקוח מעלה נשמר בתוך הפרויקט הזה לתמיד!

#### 📁 פרויקט 2: `Legalix TaxLand Master` (עבור מיסוי מקרקעין והשבחה)
* **Custom Instructions:** חוקת ה-TaxLand, חובת הפעלת `legalix_taxland_autonomous_agent`, מנוע 49ז וליניארי מוטב.
* **Connected MCP:** מחובר בלעדית ל-`Legalix TaxLand`.

#### 📁 פרויקט 3: `Legalix Engineering Co-Pilot` (עבור בקרת תכן ורוויט)
* **Custom Instructions:** חוקת ההנדסה, 14 היועצים, הספר הכחול ות״י 466/413.
* **Connected MCP:** מחובר בלעדית ל-`Legalix Engineering`.

---

### 🟢 3. אותו הדבר בדיוק ב-ChatGPT (3 סוכני Custom GPTs ייעודיים):
* ב-ChatGPT הלקוח נכנס ישירות ל-GPT הייעודי שלו מסרגל הצד (Pinned to Sidebar).
* הצ'אטים שמורים בתוך ה-GPT, והסוכן תמיד מחובר לאותו שרת MCP בענן!
EOF
