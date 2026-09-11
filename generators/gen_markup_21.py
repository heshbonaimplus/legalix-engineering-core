import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Enhanced Complete Markup for Section 6.3 (Round 2: Flexible Seismic Expansion Sleeves for Ducts crossing 120mm Structural Joints, Rod Stiffeners against Buckling & Cable Swaged Bracing)
fig, ax = plt.subplots(figsize=(14, 11), dpi=220)
ax.set_facecolor("#0b132b")
fig.patch.set_facecolor("#0b132b")

ax.set_xlim(-15, 15)
ax.set_ylim(-12, 12)

# Multi-Discipline Seismic Envelope
park_box = patches.Rectangle((-13.0, -7.0), 26.0, 15.0, linewidth=2.5, edgecolor="#48cae4", facecolor="#1c2541", alpha=0.9)
ax.add_patch(park_box)
ax.text(0.0, 7.0, "תמיכות וריסון סיסמי מבוצר לתעלות מיזוג ושחרור עשן (סבב בדיקה מורחב סעיף 6.3)\nמחבר סיסמי גמיש בחציית תפר 120 מ\"מ, מקשיחי מוטות הברגה (Rod Stiffeners) ועוגני Hilti", color="#ffffff", fontsize=9.5, ha="center", fontweight="bold")

# Concrete Slab
slab = patches.Rectangle((-13.0, 4.0), 26.0, 1.5, linewidth=2, edgecolor="#48cae4", facecolor="#2b2d42", alpha=0.95)
ax.add_patch(slab)
ax.text(0.0, 4.75, "תקרת בטון חניון מרתף 1-", color="#ffffff", fontsize=8, ha="center", fontweight="bold")

# Heavy Smoke Exhaust Duct with 45° Steel Angle Bracing
duct_box = patches.Rectangle((-6.0, -1.0), 8.0, 3.5, linewidth=2.5, edgecolor="#06d6a0", facecolor="#1c2541", alpha=0.9, zorder=6)
ax.add_patch(duct_box)
ax.text(-2.0, 0.75, "תעלת עשן 1.60x0.75 מ' מחוזקת סיסמית ✅\nזוויתן 50x50x5 מ\"מ ב-45° + עוגני Hilti HST3", color="#ffffff", fontsize=7.5, ha="center", fontweight="bold")

# Diagonal Bracing Rods
ax.plot([-6.0, -9.5], [-1.0, 4.0], color="#06d6a0", linewidth=3.5, zorder=7)
ax.plot([2.0, 5.5], [-1.0, 4.0], color="#06d6a0", linewidth=3.5, zorder=7)

# DEFECT 4: Rigid Sheet Metal Duct Crossing 120mm Structural Seismic Separation Joint without Flexible Bellows
# During differential building motion, rigid sheet metal duct shears, tears and collapses across the joint!
ax.text(6.0, 3.5, "חציית תפר מבני 120 מ\"מ ללא שרוול גמיש! ❌\nתנודה דינמית של ±120 מ\"מ תגזור ותרסק את התעלה;\n(חובת שרוול אקורדיון בד סיליקון גמיש ±150 מ\"מ)", color="#ff0054", fontsize=7.5, ha="center", fontweight="bold", bbox=dict(boxstyle="round,pad=0.3", facecolor="#1b263b", ec="#ff0054"))

# DEFECT 5: Long Threaded Rods (L > 1.20m) without Rod Stiffener Clamps (סכנת קריסת מוטות בכפיפה תחת עומס לחיצה סיסמי)
ax.text(-12.5, 1.5, "מוטות הברגה ארוכים ללא מקשיחי כפיפה! ❌\n(מוטות תלייה באורך 1.5 מטר יקרסו בלחיצה;\nחובת זוויתן הקשחה Rod Stiffener כל 45 ס\"מ)", color="#ff0054", fontsize=7.5, fontweight="bold", bbox=dict(boxstyle="round,pad=0.2", facecolor="#1b263b", ec="#ff0054"))

# DEFECT 6: Heavy Ceiling Equipment (> 20 kg) attached to drywall / unistrut without direct structural slab anchoring
ax.text(-12.5, -5.5, "מפוחים מושהים ללא עיגון לשלד הראשי! ❌", color="#ffbe0b", fontsize=7.5, fontweight="bold", bbox=dict(boxstyle="round,pad=0.2", facecolor="#1b263b", ec="#ffbe0b"))

# Compliant Flexible Seismic Sleeve Detail
flex_sleeve = patches.Rectangle((4.5, -1.0), 3.0, 3.5, linewidth=2, edgecolor="#ffd166", facecolor="#ffd166", alpha=0.3, zorder=7)
ax.add_patch(flex_sleeve)
ax.text(6.0, -3.0, "שרוול אקורדיון גמיש לחציית תפר\nכושר תנועה תלת-ממדי ±150 מ\"מ ✅", color="#06d6a0", fontsize=7.5, ha="center", fontweight="bold")

# Failure Clouds
cloud_flx = patches.Ellipse((6.0, 3.5), 11.5, 4.0, edgecolor="#ff006e", facecolor="none", linestyle=":", linewidth=3, zorder=8)
cloud_stf = patches.Ellipse((-7.5, 1.5), 11.5, 3.5, edgecolor="#ff006e", facecolor="none", linestyle=":", linewidth=3, zorder=8)
ax.add_patch(cloud_flx)
ax.add_patch(cloud_stf)

# Annotations & Directives
ax.annotate("מוקדי כשל סעיף 6.3 (סבב בדיקה מורחב — ת״י 413, SMACNA ו-ASCE 7-16):\n1. חציית תפר הפרדה סיסמי 120 מ\"מ בצנרת/תעלות קשיחות ללא שרוול גמיש: סכנת שבר גזירה ברעידת אדמה ❌.\n2. מוטות הברגה ארוכים (L > 1.20m) ללא מקשיחי כפיפה (Rod Stiffeners) הנוטים לקרוס בלחיצה ❌.\n3. ציוד תלוי כבד (מפוחי שחרור עשן) מעוגן למסגרות קלות במקום עיגון ישיר לשלד הבטון ❌.\n4. היעדר חיזוקים אלכסוניים 45° ועוגנים ללא דירוג סיסמי ❌.",
            xy=(-6.0, -1.0), xytext=(-14.0, -11.2),
            arrowprops=dict(facecolor="#ff0054", edgecolor="#ffffff", shrink=0.08, width=2.5, headwidth=8),
            bbox=dict(boxstyle="round,pad=0.6", facecolor="#ff0054", edgecolor="#ffffff", lw=1.5, alpha=0.95),
            color="#ffffff", fontsize=9.5, fontweight="bold", zorder=10)

ax.annotate("הנחיית תיקון תכן מקיפה לסעיף 6.3 (Hold Point Resolution):\n1. התקנת שרוול אקורדיון סיסמי גמיש מבד סיליקון-פיברגלס (כושר תנועה ±150 מ\"מ) בכל חציית תפר מבני בין מגדל 321 למבנה 223.\n2. שילוב מקשיחי זוויתן פלדה (Rod Stiffeners עם חבקי C-Clamps) על גבי מוטות הברגה שאורכם עולה על 1.00 מטר.\n3. עיגון ישיר של כל ציוד מעל 20 ק\"ג לתקרת בטון מזוין בלבד בעוגני Hilti HST3.\n4. חיזוקים רוחביים כל 9.0 מטר, אורכיים כל 18.0 מטר ועוגנים 4-כיווניים בפירים.",
            xy=(6.0, -1.0), xytext=(-2.0, 8.2),
            arrowprops=dict(facecolor="#06d6a0", edgecolor="#ffffff", shrink=0.08, width=2.5, headwidth=8),
            bbox=dict(boxstyle="round,pad=0.6", facecolor="#06d6a0", edgecolor="#ffffff", lw=1.5, alpha=0.95),
            color="#073b4c", fontsize=9.5, fontweight="bold", zorder=10)

ax.set_title("בקרת תכן הנדסית — סעיף 6.3 מורחב: שרוול סיסמי גמיש לתפר 120 מ\"מ, מקשיחי מוטות ועוגני Hilti\nפרויקט לוד ניר צבי (עמרם אברהם) | חניון ותפרי מבנים (LOD_HV_ALL_R23) | תקנים: ת״י 413, SMACNA",
             color="#ffffff", fontsize=11.5, pad=18, fontweight="bold", ha="center")

plt.tight_layout()
out_img = "/home/yogi/lod_project/markup_hvac_21_seismic_sway_bracing.png"
plt.savefig(out_img, facecolor=fig.get_facecolor(), edgecolor="none", bbox_inches="tight")
plt.close()
print("Enhanced HVAC Section 6.3 markup saved successfully:", out_img)
