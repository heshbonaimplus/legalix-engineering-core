import docx, os, zipfile, re, shutil
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_SECTION, WD_ORIENTATION
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_perfect_rtl(p):
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    pPr = p._p.get_or_add_pPr()
    # Remove existing bidi/jc if any
    for child in list(pPr):
        if child.tag.endswith(('bidi', 'jc')):
            pPr.remove(child)
    bidi = parse_xml(f'<w:bidi {nsdecls("w")}/>')
    jc = parse_xml(f'<w:jc {nsdecls("w")} w:val="right"/>')
    pPr.append(bidi)
    pPr.append(jc)

NAVY = RGBColor(16, 44, 87)
CRIMSON = RGBColor(180, 0, 0)
DARK_GRAY = RGBColor(60, 60, 60)
GREEN_COLOR = RGBColor(0, 120, 0)
ORANGE_COLOR = RGBColor(210, 105, 0)
BLUE_COLOR = RGBColor(0, 102, 204)

print("Perfect RTL helper ready.")
