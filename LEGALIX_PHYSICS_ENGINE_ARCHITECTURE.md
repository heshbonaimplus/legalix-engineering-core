# Legalix Physics & Finite Element Engine Architecture (Beyond Standards)
# ארכיטקטורת מנוע האנליזה והפיזיקה של Legalix: שילוב FEA + פיזיקה דטרמיניסטית + התאמה לתקנים

## 🏛️ 1. ליבת האלמנטים הסופיים (Core FEA Solver Engine):
- מטריצות קשיחות תלת-ממדיות (Beam-Column, 4-Node Shell Element, 8-Node Solid).
- חישובי מאמצים, דפורמציות, מומנטי כפיפה וגזירה.
- חישוב ערכים עצמיים (Eigenvalues) לזמני מחזור וצורות תנודה.

## 🌊 2. מנוע אינטראקציית קרקע-מבנה (Soil-Structure Interaction - SSI):
- קפיצי וינקלר (Winkler Springs) דיפרנציאליים לא-ליניאריים.
- עקומות t-z לחיכוך כלונסאות ועקומות p-y לדחף אופקי.
- חישוב שקיעות דיפרנציאליות אמיתיות ועיוות זוויתי (Angular Distortion).

## 🌪️ 3. מנוע דינמיקה לא-ליניארית (Nonlinear Time-History & P-Delta):
- שילוב גלי רעידת אדמה היסטוריים (Accelerograms).
- מעקב אחר פלסטיזציה של בטון ופלדה (Plastic Hinges).
- חישוב אנרגיית ריסון ודריפט קומתי אמיתי.

## ⚖️ 4. שכבת ה-Code Compliance (החיבור לתקנים):
- ת״י 466 (חוקת הבטון)
- ת״י 413 (רעידות אדמה)
- ת״י 940 (קרקע וביסוס)
- ת״י 412 (עומסים)
- ACI 318 / Eurocode 2 / ASCE 7-16
EOF
