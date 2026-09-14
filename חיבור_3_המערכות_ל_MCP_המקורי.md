# חיבור 3 המערכות (Mega-Case, TaxLand, Engineering) לתוך ה-MCP המקורי שלכם
## מדריך ארכיטקטורה ורישום כלים מובנה בתוך `tools.ts` של ה-Gateway המקורי

---

### 🏛️ 1. איך שלושת המודולים מתחברים בתוך ה-Gateway המקורי שלכם:

בתוך קובץ ה-**`tools.ts`** של ה-MCP Gateway המקורי שלכם, שלושת המודולים רשומים כעת כ-Native Tools רשמיים:

```text
               Legalix MCP Gateway (server.ts)
                             │
                             ▼
                    tools.ts (רשימת הכלים)
                             │
       ┌─────────────────────┼─────────────────────┐
       ▼                     ▼                     ▼
1. Legalix Mega-Case   2. Legalix TaxLand    3. Legalix Engineering
   (`legalix_mega_case`)  (`legalix_taxland`)   (`legalix_engineering`)
       │                     │                     │
       ▼                     ▼                     ▼
• 13 מחסנים בדרייב     • שבח ליניארי מוטב    • בקרת תכן 14 יועצים
• סתירות וראיות       • פיצול סעיף 49ז       • כתבי כמויות (BOQ)
• ציר זמן מלא         • פריסת מס            • שרטוטי CAD ומודלי Revit
• שומות אלזנר         • בקרת Red Team       • אנליזות OpenSees FEA
```

---

### 🧰 2. שמות הכלים שמופיעים בקלוד (Tools List ב-Claude):

1. ⚖️ **`legalix_mega_case`** — מפעיל את חדר המלחמה, סורק את 13 המחסנים בדרייב, מחלץ סתירות ומפיק בקשות לפי תקנה 91.
2. 🏛️ **`legalix_taxland_plan`** — מפעיל את מנוע ה-Numeric Core של TaxLand, מחשב 3 חלופות מס ומצליב פסיקת נמדר (ע״א 579/02 חלבני).
3. 🏗️ **`legalix_engineering_master`** — מפעיל את מנוע ההנדסה, שואב כתבי כמויות (חשמל, אינסטלציה, שלד), ומציג שרטוטים וגיליונות.

בנוסף לכל הכלים המקוריים שלכם:  
`legalix_tax_shevach`, `legalix_tax_rechisha`, `legalix_tax_section_49z_plan`, `legalix_kepa_timeline`, `legalix_nezikin_tachshiv`, `legalix_madad_calculator`.

---

### 🚀 3. איך מפעילים את זה ב-Cloud Run:
יונתן לוקח את תיקיית **`Legalix MCP Gateway/`** המעודכנת מתוך Google Drive (או מתוך ה-GitHub המרכזי), ומריץ פקודת Deploy אחת ל-Cloud Run:

```bash
gcloud run deploy legalix-mcp-gateway \
  --source "Legalix MCP Gateway/" \
  --region europe-west3 \
  --platform managed \
  --allow-unauthenticated \
  --port 8080
```

---

### 🏆 התוצאה בקלוד:
כשאתה מתחבר ל-`https://mcp.legalix.ai/mcp` — כל 3 המערכות (Mega-Case, TaxLand, Engineering) זמינות לך ופעילות תחת ה-MCP המקורי והרשמי שבניתם!
EOF
