import json, os, sys

sys.path.append('/home/yogi/lod_project')
from build_html_gdocs import generate_html_report_for_gdocs
from build_el_data import get_all_22_electrical_designer_cards
from gen_full_45_st_cards import get_full_45_structural_cards
from fix_landscape_and_marketing_rtl import force_ultra_strict_rtl

# 1. Generate clean, lightweight, ultra-fast Electrical HTML
html_el = generate_html_report_for_gdocs(
    "דוח הנחיות תיקון, חלופות וסגירת ממצאים למתכנן החשמל",
    "מערכות חשמל, מתח נמוך ומערכות חירום",
    get_all_22_electrical_designer_cards(),
    {"model": "LOD_PR_EL_R24 / LOD_321_EL_R24", "recipient": "מתכנן מערכות חשמל ותקשורת (צוות הנדסת חשמל)", "p1_count": "15", "p2_count": "4", "p3_count": "2", "p4_count": "1"}
)
el_path = '/home/yogi/lod_project/ELECTRICAL_CLEAN_LIGHT_GDOC.html'
with open(el_path, 'w', encoding='utf-8') as f:
    f.write(html_el)
force_ultra_strict_rtl(el_path)
print(f"Generated clean Electrical HTML (Size: {os.path.getsize(el_path)/1024:.1f} KB)")

# 2. Generate clean, lightweight, ultra-fast Structure HTML
html_st = generate_html_report_for_gdocs(
    "דוח הנחיות תיקון, חלופות וסגירת ממצאים למתכנן הקונסטרוקציה",
    "הנדסת קונסטרוקציה, ביסוס ושלד",
    get_full_45_structural_cards(),
    {"model": "Lod_ST_PR_R25 / Lod_ST_321_R25 / Lod_ST_339_R25", "recipient": "מתכנן קונסטרוקציה ושלד (אלי חלמיש / הנדסת מבנים)", "p1_count": "20", "p2_count": "8", "p3_count": "10", "p4_count": "0"}
)
st_path = '/home/yogi/lod_project/STRUCTURE_CLEAN_LIGHT_GDOC.html'
with open(st_path, 'w', encoding='utf-8') as f:
    f.write(html_st)
force_ultra_strict_rtl(st_path)
print(f"Generated clean Structure HTML (Size: {os.path.getsize(st_path)/1024:.1f} KB)")
