import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Enhanced Complete Markup for Section 6.2 (Round 2: Acoustic Enclosure Barrier Walls, Snubber Restraints for Wind Load, Flanking Transmission through Riser Shafts & Floating Floor Pads)
fig, ax = plt.subplots(figsize=(14, 11), dpi=220)
ax.set_facecolor("#0b132b")
fig.patch.set_facecolor("#0b132b")

ax.set_xlim(-15, 15)
ax.set_ylim(-12, 12)

# Rooftop Mechanical Plant Deck above Penthouse Floor
roof_box = patches.Rectangle((-13.0, -7.0), 26.0, 15.0, linewidth=2.5, edgecolor="#48cae4", facecolor="#1c2541", alpha=0.9)
ax.add_patch(roof_box)
ax.text(0.0, 7.0, "מרפסת גג טכנית מבוצרת אקוסטית מעל פנטהאוז (סבב בדיקה מורחב סעיף 6.2)\nקירות מיסוך אקוסטיים 25 dB, מרסנים סיסמיים לרוח (Snubbers) ורצפה צפה (ת״י 1004 / הגנת הסביבה)", color="#ffffff", fontsize=9.5, ha="center", fontweight="bold")

# Penthouse Concrete Ceiling Slab
slab = patches.Rectangle((-13.0, -1.0), 26.0, 1.5, linewidth=2, edgecolor="#48cae4", facecolor="#2b2d42", alpha=0.95)
ax.add_patch(slab)
ax.text(0.0, -0.25, "תקרת בטון דירת פנטהאוז", color="#ffffff", fontsize=8, ha="center", fontweight="bold")

# Chiller on Compliant Inertia Base + Mason Springs
chiller = patches.Rectangle((-10.0, 2.0), 8.0, 4.0, linewidth=2, edgecolor="#06d6a0", facecolor="#06d6a0", alpha=0.35, zorder=6)
ax.add_patch(chiller)
ax.text(-6.0, 4.0, "צ'ילר על בסיס אינרציה צף\n+ משככי קפיץ 50 מ\"מ ✅", color="#ffffff", fontsize=7.5, ha="center", fontweight="bold")

# Concrete Floating Inertia Base (y = 1.0 to 2.0)
inertia_base = patches.Rectangle((-10.5, 1.0), 9.0, 1.0, linewidth=2, edgecolor="#ffd166", facecolor="#ffd166", alpha=0.8, zorder=5)
ax.add_patch(inertia_base)
ax.text(-6.0, 1.5, "בסיס בטון צף (Inertia Base 150mm) ✅", color="#0b132b", fontsize=7, ha="center", va="center", fontweight="bold")

# DEFECT 4: Missing Rooftop Acoustic Barrier / Louver Walls (קירות מיסוך אקוסטיים) around Outdoor Chillers
# Noise radiates freely horizontally across roof -> Disturbing penthouse balconies and neighboring towers!
ax.text(6.0, 3.5, "ללא קירות מיסוך אקוסטיים בגג! ❌\n(רעש אופקי של 85 dB פוגע ישירות במרפסות הפנטהאוז;\nחובת קירות מיסוך אקוסטיים רפפתיים עם הנחתה 25 dB)", color="#ff0054", fontsize=7.5, ha="center", fontweight="bold", bbox=dict(boxstyle="round,pad=0.3", facecolor="#1b263b", ec="#ff0054"))

# DEFECT 5: Missing All-Directional Seismic & Wind Snubbers (מרסני תנודות רוח ורעידות אדמה לקפיצים)
# Strong winds at 58m tower roof rock chillers off un-restrained springs!
ax.text(6.0, -1.5, "קפיצים פתוחים ללא ריסון רוח (Snubbers)! ❌\n(רוחות עזות בגובה 58 מטר יעקרו את הצ'ילר מהקפיצים)", color="#ff0054", fontsize=7.5, fontweight="bold", bbox=dict(boxstyle="round,pad=0.2", facecolor="#1b263b", ec="#ff0054"))

# DEFECT 6: Flanking Acoustic Transmission through Unsealed Pipe Penetrations in Penthouse Slab
ax.text(-12.5, -5.5, "מעברי צנרת בתקרה ללא איטום אקוסטי! ❌\n(רעש מוטס חודר דרך חריצי יציקה לתקרה)", color="#ffbe0b", fontsize=7.5, fontweight="bold", bbox=dict(boxstyle="round,pad=0.2", facecolor="#1b263b", ec="#ffbe0b"))

# Compliant Acoustic Barrier Wall on Right of Chiller (-1.0 to 0.0, y = 0.5 to 6.5)
barrier = patches.Rectangle((-1.0, 0.5), 1.0, 6.0, linewidth=2, edgecolor="#06d6a0", facecolor="#06d6a0", alpha=0.7, zorder=7)
ax.add_patch(barrier)
ax.text(-0.5, 3.5, "קיר מיסוך אקוסטי\nהנחתה 25 dB ✅", color="#0b132b", fontsize=7, ha="center", va="center", fontweight="bold", rotation=90)

# Failure Clouds
cloud_bar = patches.Ellipse((6.0, 3.5), 11.5, 3.5, edgecolor="#ff006e", facecolor="none", linestyle=":", linewidth=3, zorder=8)
cloud_snb = patches.Ellipse((6.0, -1.5), 11.0, 3.0, edgecolor="#ff006e", facecolor="none", linestyle=":", linewidth=3, zorder=8)
ax.add_patch(cloud_bar)
ax.add_patch(cloud_snb)

# Annotations & Directives
ax.annotate("מוקדי כשל סעיף 6.2 (סבב בדיקה מורחב — ת״י 1001, ת״י 1004 ות״י 413):\n1. היעדר קירות מיסוך אקוסטיים (Acoustic Barrier Louvers) בגג: מטרד רעש אופקי כבד למרפסות ולשכנים ❌.\n2. משככי קפיץ ללא מרסנים רב-כיווניים (Seismic & Wind Snubbers) לעמידה ברוחות סערה בגובה 58 מטר ❌.\n3. מעברי צנרת מים ומיזוג בתקרת הפנטהאוז ללא שרוולי איטום אקוסטיים רציפים (Flanking Transmission) ❌.\n4. רעש 52 dB(A) בחדר שינה, ללא בסיס אינרציה וללא משתיקי קול ❌.",
            xy=(-6.0, 2.0), xytext=(-14.0, -11.2),
            arrowprops=dict(facecolor="#ff0054", edgecolor="#ffffff", shrink=0.08, width=2.5, headwidth=8),
            bbox=dict(boxstyle="round,pad=0.6", facecolor="#ff0054", edgecolor="#ffffff", lw=1.5, alpha=0.95),
            color="#ffffff", fontsize=9.5, fontweight="bold", zorder=10)

ax.annotate("הנחיית תיקון תכן מקיפה לסעיף 6.2 (Hold Point Resolution):\n1. הקמת קירות מיסוך אקוסטיים רפפתיים (Acoustic Louvers) מבודדים בצמר סלעים סביב כל מתחם הצ'ילרים בגג (הנחתה 25 dB).\n2. שימוש במשככי קפיץ מרוסנים סיסמית (Housings with All-Directional Snubbers) לעמידה בכוחות רוח וסיסמיקה לפי ת״י 413.\n3. אטימה אקוסטית של כל מעברי הצנרת בתקרת הבטון בשרוולי EPDM ומסטיק אקוסטי כבד.\n4. בסיס אינרציה צף 150 מ\"מ, משככי קפיץ 50 מ\"מ ומשתיקי קול תעלתיים (L_Aeq ≤ 30 dB).",
            xy=(6.0, -6.0), xytext=(-2.0, 8.2),
            arrowprops=dict(facecolor="#06d6a0", edgecolor="#ffffff", shrink=0.08, width=2.5, headwidth=8),
            bbox=dict(boxstyle="round,pad=0.6", facecolor="#06d6a0", edgecolor="#ffffff", lw=1.5, alpha=0.95),
            color="#073b4c", fontsize=9.5, fontweight="bold", zorder=10)

ax.set_title("בקרת תכן הנדסית — סעיף 6.2 מורחב: קירות מיסוך אקוסטיים 25 dB, מרסני רוח ובידוד מעברי שלד\nפרויקט לוד ניר צבי (עמרם אברהם) | מרפסת גג מגדלים 321, 339 (LOD_HV_ALL_R23) | תקנים: ת״י 1004, ת״י 413",
             color="#ffffff", fontsize=11.5, pad=18, fontweight="bold", ha="center")

plt.tight_layout()
out_img = "/home/yogi/lod_project/markup_hvac_20_acoustic_vibration_isolators.png"
plt.savefig(out_img, facecolor=fig.get_facecolor(), edgecolor="none", bbox_inches="tight")
plt.close()
print("Enhanced HVAC Section 6.2 markup saved successfully:", out_img)
