import os, sys
sys.path.append('/home/yogi/lod_project')

from build_html_gdocs import generate_html_report_for_gdocs
from build_ls_data import get_all_16_landscape_designer_cards
from build_mkt_data import get_all_18_marketing_designer_cards
from fix_landscape_and_marketing_rtl import force_ultra_strict_rtl

# 1. Generate Landscape HTML
html_ls = generate_html_report_for_gdocs(
    "דוח הנחיות תיקון, חלופות וסגירת ממצאים למתכנן הנוף והפיתוח",
    "פיתוח נופי, ניקוז חצר, מפלסי פיתוח וקירות תמך חוץ",
    get_all_16_landscape_designer_cards(),
    {"model": "LOD_ALL_LG_R24.rvt", "p1_count": "10", "p2_count": "4", "p3_count": "1", "p4_count": "1"}
)
ls_p = '/home/yogi/lod_project/LANDSCAPE_DESIGNER_CLOSURE_REPORT.html'
with open(ls_p, 'w', encoding='utf-8') as f:
    f.write(html_ls)
force_ultra_strict_rtl(ls_p)

# 2. Generate Marketing HTML
html_mkt = generate_html_report_for_gdocs(
    "דוח הנחיות תיקון, חלופות וסגירת ממצאים לשיווק ולמתכנן",
    "הצלבת תוכניות מכר מול מודלי ביצוע והתאמת שטחים",
    get_all_18_marketing_designer_cards(),
    {"model": "חבילת מכר מול 3D-Marketing / Lod_AR / Lod_ST (1.82GB)", "p1_count": "15", "p2_count": "3", "p3_count": "0", "p4_count": "0"}
)
mkt_p = '/home/yogi/lod_project/MARKETING_DESIGNER_CLOSURE_REPORT.html'
with open(mkt_p, 'w', encoding='utf-8') as f:
    f.write(html_mkt)
force_ultra_strict_rtl(mkt_p)

print("Both Landscape and Marketing HTMLs generated and strictly formatted with RTL!")
