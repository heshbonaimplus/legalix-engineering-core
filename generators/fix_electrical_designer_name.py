import os

el_html_p = '/home/yogi/lod_project/ELECTRICAL_DESIGNER_CLOSURE_REPORT.html'
if os.path.exists(el_html_p):
    with open(el_html_p, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace("צ'רלי חורי / צוות תכנון", "מתכנן מערכות חשמל ותקשורת (צוות הנדסת חשמל)")
    with open(el_html_p, 'w', encoding='utf-8') as f:
        f.write(c)
    print("Fixed Electrical HTML: Charlie Khoury removed from Electrical.")

# Also let's check and upload all Google Docs properly to the dedicated folder for Or Amram
