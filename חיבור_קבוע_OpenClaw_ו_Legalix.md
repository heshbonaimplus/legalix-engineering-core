# ארכיטקטורת ההטמעה הקבועה: Legalix Engineering כ-Native Plugin בתוך OpenClaw
## איך הופכים את Legalix Engineering לחלק אינטגרלי מ-OpenClaw שנטען אוטומטית בכל צ'אט חדש

---

### 🏛️ 1. הארכיטקטורה המובנית (Native Plugin Architecture):

כדי ש-OpenClaw יטען אוטומטית בכל צ'אט חדש את Legalix Engineering כברירת מחדל, אנחנו רושמים אותו בתיקיית ה-Extensions של OpenClaw:

```text
openclaw/
├── extensions/
│   └── legalix-engineering/
│       ├── openclaw.plugin.json    <-- מגדיר את ה-Plugin ב-OpenClaw
│       ├── package.json
│       ├── src/
│       │   ├── index.ts            <-- שער הכניסה הראשי
│       │   ├── agent.ts            <-- סוכן ההנדסה האוטונומי
│       │   ├── router.ts           <-- ניתוב אוטומטי (חשמל/שלד/אינסטלציה)
│       │   └── tools/
│       │       ├── boq.ts          <-- מנוע כתבי כמויות אוטונומי
│       │       ├── cad-bim.ts      <-- מנוע שרטוטים ורינדור גיליונות
│       │       └── structural.ts   <-- מנוע בקרת תכן ופיזיקה OpenSees
│       └── skills/
│           └── legalix-engineering/
│               └── SKILL.md        <-- חוקת התכן וספריות הכללים
```

---

### 🚀 2. מה קורה בכל צ'אט חדש מרגע זה:
1. המשתמש פותח צ'אט חדש מול OpenClaw.
2. ה-Runtime של OpenClaw טוען אוטומטית את `legalix-engineering` כסוכן פעיל ברקע.
3. כל בקשה הנדסית (כמויות, גיליונות, שרטוטים, נספחים) מופעלת ישירות מתוך הליבה ללא צורך בהגדרות נוספות!
EOF
