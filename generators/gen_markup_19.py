import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

fig, ax = plt.subplots(figsize=(14, 11), dpi=220)
ax.set_facecolor("#0b132b")
fig.patch.set_facecolor("#0b132b")

ax.set_xlim(-15, 15)
ax.set_ylim(-12, 12)

# Multi-Discipline Superposition Envelope
sup_box = patches.Rectangle((-13.0, -7.0), 26.0, 15.0, linewidth=2.5, edgecolor="#48cae4", facecolor="#1c2541", alpha=0.9)
ax.add_patch(sup_box)
ax.text(0.0, 7.0, "סופרפוזיציה רב-תחומית: מיזוג אוויר מול קונסטרוקציה וספרינקלרים (סעיף 6.1)\nבקרת התנגשויות תעלות בקורות שלד, ראשי ספרינקלר תחת תעלות וגובה ראש 2.40m (LOD_HV_ALL_R23)", color="#ffffff", fontsize=9.5, ha="center", fontweight="bold")

# Concrete Ceiling & Structural Drop Beam B-108 (Depth 80cm: x = -1.0 to 2.0, y = 1.0 to 5.5)
slab = patches.Rectangle((-13.0, 5.5), 26.0, 1.5, linewidth=2, edgecolor="#48cae4", facecolor="#1c2541", alpha=0.9)
ax.add_patch(slab)
beam = patches.Rectangle((-1.0, 1.0), 3.0, 4.5, linewidth=2.5, edgecolor="#ffffff", facecolor="#2b2d42", alpha=0.95)
ax.add_patch(beam)
ax.text(0.5, 3.25, "קורה יורדת B-108\nעומק 80 ס\"מ", color="#ffffff", fontsize=8, ha="center", fontweight="bold")

# Floor line (y = -6.0)
ax.axhline(-6.0, color="#ffd166", linewidth=2.5)
ax.text(-12.5, -5.5, "מפלס רצפת חניון FFL (נתיב נסיעה ראשי)", color="#ffd166", fontsize=8, fontweight="bold")

# DEFECT 1: Direct Physical Hard Clash
clash_duct = patches.Rectangle((-7.0, 1.5), 14.0, 2.2, linewidth=2.5, edgecolor="#ff0054", facecolor="#d62828", alpha=0.75, zorder=6)
ax.add_patch(clash_duct)
ax.text(-4.0, 2.6, "תעלת מיזוג 1.40x0.50 מ'", color="#ffffff", fontsize=7.5, fontweight="bold")
ax.text(0.5, 2.6, "התנגשות קשה בקורה!\n(חיתוך זיון מתיחה תחתון)", color="#ffffff", fontsize=7, ha="center", va="center", fontweight="bold", bbox=dict(boxstyle="round,pad=0.2", facecolor="#1b263b", ec="#ff0054"))

# DEFECT 2: Below Duct Sprinkler Missing
ax.text(6.0, 4.0, "חסימת מניפת ספרינקלר ע\"י תעלה רחבה (1.40 מ')!\n(היעדר ראשי ספרינקלר תחת התעלה Below-Duct;\nרכבים בוערים תחת התעלה לא יקבלו כיבוי מים!)", color="#ff0054", fontsize=7.5, ha="center", fontweight="bold", bbox=dict(boxstyle="round,pad=0.3", facecolor="#1b263b", ec="#ff0054"))

# DEFECT 3: Headroom Drop
ax.text(6.0, -1.5, "התנגשות בצנרת ביוב מורידה גובה ראש ל-1.90 מ'!\n(חריגה חמורה מגובה ראש תקני 2.40 מ')", color="#ff0054", fontsize=7.5, fontweight="bold", bbox=dict(boxstyle="round,pad=0.2", facecolor="#1b263b", ec="#ff0054"))

# REQUIRED COMPLIANT FIX
ax.text(6.0, -6.0, "תיקון תכן מחייב:\n1. שרוול פלדה יצוק מראש בקורה בשליש h/3.\n2. ראשי ספרינקלר תלויים תחת תעלה (Below-Duct).\n3. לוחיות איסוף חום מנירוסטה 30x30 ס\"מ.\n4. שמירה על גובה ראש נטו H_clear ≥ 2.45 מטר.", color="#06d6a0", fontsize=8, fontweight="bold", bbox=dict(boxstyle="round,pad=0.3", facecolor="#0b132b", ec="#06d6a0"))

# Failure Clouds
cloud_cls = patches.Ellipse((0.5, 2.6), 6.0, 3.5, edgecolor="#ff006e", facecolor="none", linestyle=":", linewidth=3, zorder=8)
cloud_spk = patches.Ellipse((6.0, 4.0), 11.5, 3.5, edgecolor="#ff006e", facecolor="none", linestyle=":", linewidth=3, zorder=8)
ax.add_patch(cloud_cls)
ax.add_patch(cloud_spk)

# Annotations & Directives
ax.annotate("מוקדי כשל סעיף 6.1 — סופרפוזיציה, התנגשויות שלד וספרינקלרים (ת״י 466, NFPA 13 ות״י 1001):\n1. התנגשות פיזית קשה: תעלת מיזוג 1.40x0.50 מ' חותכת קורת שלד B-108 בזיון מתיחה תחתון.\n2. תעלה ברוחב 1.40 מ' חוסמת 100% ממניפת הספרינקלר העליון ללא ראשי Below-Duct (NFPA 13 סעיף 8.5.5.3).\n3. הצטלבות תעלת מיזוג וצנרת ביוב מורידה גובה ראש נטו ל-1.90 מטר בנתיב נסיעה.\n4. היעדר לוחיות איסוף חום (Heat Collectors) מעל ראשי ספרינקלר תחת תעלות.",
            xy=(0.5, 2.6), xytext=(-14.0, -11.2),
            arrowprops=dict(facecolor="#ff0054", edgecolor="#ffffff", shrink=0.08, width=2.5, headwidth=8),
            bbox=dict(boxstyle="round,pad=0.6", facecolor="#ff0054", edgecolor="#ffffff", lw=1.5, alpha=0.95),
            color="#ffffff", fontsize=9.5, fontweight="bold", zorder=10)

ax.annotate("הנחיית תיקון תכן מחייבת לסעיף 6.1 (Hold Point Resolution):\n1. תיאום שרוול מעבר פלדה מלבני יצוק מראש בשליש המרכזי של גובה קורת הבטון (h/3) ללא פגיעה בזיון ראשי.\n2. הוספת שורת ראשי ספרינקלרים ייעודית תחת התעלה (Below-Duct Sprinklers) לכל תעלה ברוחב W > 1.20m.\n3. התקנת לוחיות איסוף חום מנירוסטה 30x30 ס\"מ מעל כל ראש ספרינקלר תחת תעלה לפתיחה תרמית מהירה.\n4. תיאום גבהים רב-תחומי ב-BIM להבטחת גובה ראש נטו H_clear ≥ 2.45 מטר מעל כל נתיבי הנסיעה.",
            xy=(6.0, -6.0), xytext=(-2.0, 8.2),
            arrowprops=dict(facecolor="#06d6a0", edgecolor="#ffffff", shrink=0.08, width=2.5, headwidth=8),
            bbox=dict(boxstyle="round,pad=0.6", facecolor="#06d6a0", edgecolor="#ffffff", lw=1.5, alpha=0.95),
            color="#073b4c", fontsize=9.5, fontweight="bold", zorder=10)

ax.set_title("בקרת תכן הנדסית — סעיף 6.1: הצלבות קונסטרוקציה וספרינקלרים (Below-Duct), קורות וגובה ראש 2.40m\nפרויקט לוד ניר צבי (עמרם אברהם) | חניון מרתף 1- ו-2- (LOD_HV_ALL_R23) | תקנים: ת״י 466, NFPA 13, ת״י 1001",
             color="#ffffff", fontsize=11.5, pad=18, fontweight="bold", ha="center")

plt.tight_layout()
out_img = "/home/yogi/lod_project/markup_hvac_19_superposition_clashes.png"
plt.savefig(out_img, facecolor=fig.get_facecolor(), edgecolor="none", bbox_inches="tight")
plt.close()
print("HVAC Section 6.1 markup saved successfully:", out_img)
