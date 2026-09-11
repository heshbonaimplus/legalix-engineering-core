import docx, os, zipfile, re, shutil
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_SECTION, WD_ORIENTATION
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
from builder_utils import set_rtl, setup_clean_header_footer, NAVY, CRIMSON, DARK_GRAY, GREEN_COLOR, ORANGE_COLOR, BLUE_COLOR

def fix_complete_word_rtl_all(docx_path):
    temp_dir = docx_path + '_rtl_fix_temp'
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    os.makedirs(temp_dir)
    with zipfile.ZipFile(docx_path, 'r') as z:
        z.extractall(temp_dir)
        
    doc_xml_p = os.path.join(temp_dir, 'word', 'document.xml')
    with open(doc_xml_p, 'r', encoding='utf-8') as f:
        xml = f.read()
        
    # 1. Ensure EVERY <w:p> has <w:pPr><w:bidi/><w:jc w:val="right"/></w:pPr>
    def fix_p(match):
        p_content = match.group(0)
        if '<w:pPr>' not in p_content:
            p_content = p_content.replace('<w:p', '<w:p><w:pPr><w:bidi/><w:jc w:val="right"/></w:pPr>', 1)
        else:
            if '<w:bidi/>' not in p_content and '<w:bidi' not in p_content:
                p_content = p_content.replace('<w:pPr>', '<w:pPr><w:bidi/>', 1)
            if '<w:jc' not in p_content:
                p_content = p_content.replace('</w:pPr>', '<w:jc w:val="right"/></w:pPr>', 1)
        return p_content
        
    xml = re.sub(r'<w:p[ >].*?</w:p>', fix_p, xml, flags=re.DOTALL)
    
    # 2. Ensure EVERY <w:r> has <w:rtl/>, <w:rFonts w:ascii="David" w:hAnsi="David" w:cs="David"/> and <w:lang w:bidi="he-IL"/>
    def fix_r(match):
        r_content = match.group(0)
        if '<w:rPr>' not in r_content:
            r_content = r_content.replace('<w:r', '<w:r><w:rPr><w:rFonts w:ascii="David" w:hAnsi="David" w:cs="David"/><w:rtl/><w:lang w:val="he-IL" w:bidi="he-IL"/></w:rPr>', 1)
        else:
            if '<w:rtl/>' not in r_content:
                r_content = r_content.replace('<w:rPr>', '<w:rPr><w:rtl/>', 1)
            if '<w:lang' not in r_content:
                r_content = r_content.replace('</w:rPr>', '<w:lang w:val="he-IL" w:bidi="he-IL"/></w:rPr>', 1)
            if 'w:cs=' not in r_content:
                r_content = r_content.replace('<w:rFonts ', '<w:rFonts w:cs="David" ', 1)
        return r_content
        
    xml = re.sub(r'<w:r[ >].*?</w:r>', fix_r, xml, flags=re.DOTALL)
    
    # 3. Ensure tables are bidiVisual
    xml = re.sub(r'<w:tblPr>(.*?)</w:tblPr>', lambda m: '<w:tblPr>' + (m.group(1) if '<w:bidiVisual/>' in m.group(1) else m.group(1) + '<w:bidiVisual/>') + '</w:tblPr>', xml, flags=re.DOTALL)
    
    # 4. Ensure sections are bidi
    xml = re.sub(r'<w:sectPr>(.*?)</w:sectPr>', lambda m: '<w:sectPr>' + (m.group(1) if '<w:bidi/>' in m.group(1) else '<w:bidi/>' + m.group(1)) + '</w:sectPr>', xml, flags=re.DOTALL)

    with open(doc_xml_p, 'w', encoding='utf-8') as f:
        f.write(xml)
        
    # Styles.xml
    styles_p = os.path.join(temp_dir, 'word', 'styles.xml')
    if os.path.exists(styles_p):
        with open(styles_p, 'r', encoding='utf-8') as f:
            st = f.read()
        st = re.sub(r'<w:docDefaults>.*?</w:docDefaults>', 
                    '<w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="David" w:hAnsi="David" w:cs="David"/><w:rtl/><w:lang w:val="he-IL" w:bidi="he-IL"/></w:rPr></w:rPrDefault><w:pPrDefault><w:pPr><w:bidi/><w:jc w:val="right"/></w:pPr></w:pPrDefault></w:docDefaults>', 
                    st, flags=re.DOTALL)
        with open(styles_p, 'w', encoding='utf-8') as f:
            f.write(st)
            
    # Settings.xml
    settings_p = os.path.join(temp_dir, 'word', 'settings.xml')
    if os.path.exists(settings_p):
        with open(settings_p, 'r', encoding='utf-8') as f:
            se = f.read()
        if '<w:themeFontLang' in se:
            se = re.sub(r'<w:themeFontLang[^>]*/>', '<w:themeFontLang w:val="en-US" w:eastAsia="ja-JP" w:bidi="he-IL"/>', se)
        else:
            se = se.replace('</w:settings>', '<w:themeFontLang w:val="en-US" w:eastAsia="ja-JP" w:bidi="he-IL"/></w:settings>')
        with open(settings_p, 'w', encoding='utf-8') as f:
            f.write(se)
            
    os.remove(docx_path)
    with zipfile.ZipFile(docx_path, 'w', zipfile.ZIP_DEFLATED) as z_out:
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                fp = os.path.join(root, file)
                rp = os.path.relpath(fp, temp_dir)
                z_out.write(fp, rp)
                
    shutil.rmtree(temp_dir)
    print("Fixed complete Word RTL successfully for:", docx_path)

# Apply to all 4 reports
reports = [
    '/home/yogi/lod_project/PLUMBING_DESIGNER_CORRECTION_AND_CLOSURE_REPORT_REV01.docx',
    '/home/yogi/lod_project/HVAC_DESIGNER_CORRECTION_AND_CLOSURE_REPORT_REV01.docx',
    '/home/yogi/lod_project/STRUCTURE_DESIGNER_CORRECTION_AND_CLOSURE_REPORT_REV01.docx',
    '/home/yogi/lod_project/ELECTRICAL_DESIGNER_CORRECTION_AND_CLOSURE_REPORT_REV01.docx'
]

for r in reports:
    if os.path.exists(r):
        fix_complete_word_rtl_all(r)
