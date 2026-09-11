import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

fig, ax = plt.subplots(figsize=(14, 11), dpi=220)
ax.set_facecolor("#0b132b")
fig.patch.set_facecolor("#0b132b")

ax.set_xlim(-15, 15)
ax.set_ylim(-12, 12)

# Master Summary & Hold Point Envelope
sum_box = patches.Rectangle((-13.0, -8.0), 26.0, 16.0, linewidth=2.5, edgecolor="#48cae4", facecolor="#1c2541", alpha=0.9)
ax.add_patch(sum_box)
ax.text(0.0, 7.0, "סיכום בקרת תכן הנדסית והכרזת נקודת עצירה (HOLD POINT) — מיזוג אוויר ושחרור עשן (HVAC)\nפרויקט לוד ניר צבי (עמרם אברהם) | מגדלים 321, 339 ומבנה 223 | 22 ליקויים הנדסיים מבוצרים", color="#ffffff", fontsize=9.5, ha="center", fontweight="bold")

# Hold Point Stamp Box in Center (x = -10.0 to 10.0, y = -1.5 to 5.0)
stamp_box = patches.Rectangle((-10.0, -1.0), 20.0, 6.0, linewidth=3, edgecolor="#ff0054", facecolor="#ff0054", alpha=0.15, zorder=5)
ax.add_patch(stamp_box)
ax.text(0.0, 3.8, "⛔ הכרזת נקודת עצירה רשמית (HOLD POINT) ⛔", color="#ff0054", fontsize=14, ha="center", fontweight="bold")
ax.text(0.0, 2.4, "חל איסור מוחלט על התקנת מפוחי סילון, יציקת קירות שנאים, פריסת תעלות עשן והתקנת צנרת VRF\nעד להגשת סט תוכניות וחישובים מתוקנים (Rev 02) הפותרים את כל 22 הליקויים ההנדסיים!", color="#ffffff", fontsize=8.5, ha="center", fontweight="bold")
ax.text(0.0, 0.4, "סיווג ממצאים: 17 ליקויים קריטיים שוברי ביצוע (🔴 Tier 1) | 5 ליקויי פרקטיקה ואופטימיזציה (🟡 Tier 2 / 🟢 Tier 3)", color="#ffd166", fontsize=8, ha="center", fontweight="bold")

# 6 Chapter Pillars
cols = [
    ("פרק א׳: חניונים", "מפוחי סילון F300,\nתעלות עשן וגלאי CO", -10.5),
    ("פרק ב׳: אנרגיה", "שנאים 40°C, גנרטור\nומצברי מימן ATEX", -6.3),
    ("פרק ג׳: על-לחץ", "מדרגות ΔP=25-50Pa,\nפירים ומעלית כבאים", -2.1),
    ("פרק ד׳: דירות", "ניקוז מזגנים, VRF\nושומן מסחרי Ansul", 2.1),
    ("פרק ה׳: ממ״דים", "סינון אב״כ 24/36m³,\nשסתומי הדף Type B", 6.3),
    ("פרק ו׳: סופרפוזיציה", "הצלבות שלד, אקוסטיקה\nוריסון סיסמי ת״י 413", 10.5)
]

for title, desc, cx in cols:
    c_box = patches.Rectangle((cx-1.9, -6.5), 3.8, 4.5, linewidth=1.8, edgecolor="#06d6a0", facecolor="#06d6a0", alpha=0.25, zorder=6)
    ax.add_patch(c_box)
    ax.text(cx, -3.0, f"{title}\n\n{desc}", color="#ffffff", fontsize=7, ha="center", va="center", fontweight="bold")

# Annotations
ax.annotate("חבילת מסירה מושלמת:\n1. דוח מאסטר DOCX מעוצב RTL מלא עם מפתח רמזורים.\n2. קובץ BCF מאוחד לרוויט (22 תקלות תלת-ממד).\n3. 22 תשריטי ביקורת ברזולוציה גבוהה מסונכרנים ל-Drive ולשולחן העבודה.",
            xy=(0.0, -1.0), xytext=(-14.0, -11.2),
            arrowprops=dict(facecolor="#06d6a0", edgecolor="#ffffff", shrink=0.08, width=2.5, headwidth=8),
            bbox=dict(boxstyle="round,pad=0.6", facecolor="#06d6a0", edgecolor="#ffffff", lw=1.5, alpha=0.95),
            color="#073b4c", fontsize=9.5, fontweight="bold", zorder=10)

ax.set_title("חבילת בקרת תכן הנדסית סופית — מיזוג אוויר, אוורור ושחרור עשן (LOD_HV_ALL_R23)\nפרויקט לוד ניר צבי (עמרם אברהם) | תוכניות מתוקנות Rev 02 | תקנים: ת״י 1001, NFPA 92, פקע״ר 2024, ת״י 413",
             color="#ffffff", fontsize=11.5, pad=18, fontweight="bold", ha="center")

plt.tight_layout()
out_img = "/home/yogi/lod_project/markup_hvac_22_commissioning_tab_holdpoint.png"
plt.savefig(out_img, facecolor=fig.get_facecolor(), edgecolor="none", bbox_inches="tight")
plt.close()
print("HVAC Section 6.4 markup saved successfully:", out_img)
