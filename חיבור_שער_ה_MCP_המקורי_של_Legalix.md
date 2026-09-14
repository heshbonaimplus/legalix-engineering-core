# תוכנית החיבור והפריסה של שער ה-MCP המקורי של Legalix (The Original Legalix MCP Gateway)
## מבוסס על קוד המקור המקורי שנבנה באוגוסט 2026 מתוך תיקיית `Legalix MCP Gateway` ב-Google Drive

---

### 🏛️ 1. כלי ה-MCP המקוריים של המערכת (שנבנו על ידכם):

1. **כלי מיסוי מקרקעין ורווחי הון (Tax & Mas Module):**
   * `legalix_tax_shevach` — חישוב מס שבח ליניארי מוטב.
   * `legalix_tax_rechisha` — חישוב מדרגות מס רכישה 2026.
   * `legalix_tax_section_49z_plan` — תכנון מס ופיצול רעיוני לזכויות בנייה לפי סעיף 49ז.
   * `legalix_tax_search` & `legalix_tax_lookup` — חיפוש מקורות, חקיקה והחלטות מיסוי.
   * `legalix_tax_circulars` & `legalix_tax_full_text` — שליפת חוזרי והוראות ביצוע רשות המסים.

2. **כלי חדר המלחמה והליטיגציה (Mega-Case Module):**
   * `legalix_mega_case` — ניתוח חדר מלחמה של תיקי ענק ע״י 13 סוכני-משנה בדרייב.
   * `legalix_kepa_timeline` — ציר זמן כרונולוגי אבסולוטי.
   * `legalix_kepa_entities` — מיפוי ישויות וצדדים.
   * `legalix_machsanim_protocol` — פרוטוקול 13 המחסנים.

3. **כלי נזיקין, מדדים ותקנים (Nezikin & Madad Module):**
   * `legalix_nezikin_tachshiv` — תחשיבי נזקי גוף והפסדי השתכרות.
   * `legalix_madad_calculator` — הצמדה למדד המחירים לצרכן ומדד תשומות הבנייה.
   * `legalix_house_standard` — בדיקת תקני דיור ותקנות תכנון ובנייה.

---

### 🚀 2. פקודת הפריסה עבור יונתן (מתוך תיקיית ה-Gateway המקורית):

יונתן פורס את שרת ה-Gateway המקורי שלכם ישירות מתוך קובץ ה-`Dockerfile` ו-`server.ts` המקוריים:

```bash
# פריסה ישירה ל-Cloud Run של ה-MCP Gateway המקורי
gcloud run deploy legalix-mcp-gateway \
  --source "Legalix MCP Gateway/" \
  --region europe-west3 \
  --platform managed \
  --allow-unauthenticated \
  --port 8080
```
EOF
