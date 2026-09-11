import zipfile, os, re, shutil

def inject_flawless_docx_rtl(docx_path):
    temp_dir = docx_path + '_flawless_temp'
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    os.makedirs(temp_dir)
    
    with zipfile.ZipFile(docx_path, 'r') as z:
        z.extractall(temp_dir)
        
    # 1. settings.xml
    set_p = os.path.join(temp_dir, 'word', 'settings.xml')
    if os.path.exists(set_p):
        with open(set_p, 'r', encoding='utf-8') as f:
            s_txt = f.read()
        if '<w:themeFontLang' in s_txt:
            s_txt = re.sub(r'<w:themeFontLang[^>]*/>', '<w:themeFontLang w:val="he-IL" w:bidi="he-IL"/>', s_txt)
        else:
            s_txt = s_txt.replace('</w:settings>', '<w:themeFontLang w:val="he-IL" w:bidi="he-IL"/></w:settings>')
        with open(set_p, 'w', encoding='utf-8') as f:
            f.write(s_txt)
            
    # 2. styles.xml
    sty_p = os.path.join(temp_dir, 'word', 'styles.xml')
    if os.path.exists(sty_p):
        with open(sty_p, 'r', encoding='utf-8') as f:
            st_txt = f.read()
        doc_def = '<w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="David" w:hAnsi="David" w:cs="David"/><w:bidi/><w:rtl/><w:lang w:val="he-IL" w:bidi="he-IL"/></w:rPr></w:rPrDefault><w:pPrDefault><w:pPr><w:bidi/><w:jc w:val="right"/></w:pPr></w:pPrDefault></w:docDefaults>'
        if '<w:docDefaults>' in st_txt:
            st_txt = re.sub(r'<w:docDefaults>.*?</w:docDefaults>', doc_def, st_txt, flags=re.DOTALL)
        else:
            st_txt = st_txt.replace('<w:styles', '<w:styles>' + doc_def, 1)
            
        # Normal style
        normal_replacement = '<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/><w:qFormat/><w:pPr><w:bidi/><w:jc w:val="right"/></w:pPr><w:rPr><w:rFonts w:ascii="David" w:hAnsi="David" w:cs="David"/><w:rtl/><w:lang w:val="he-IL" w:bidi="he-IL"/></w:rPr></w:style>'
        st_txt = re.sub(r'<w:style[^>]*w:styleId="Normal"[^>]*>.*?</w:style>', normal_replacement, st_txt, flags=re.DOTALL)
        with open(sty_p, 'w', encoding='utf-8') as f:
            f.write(st_txt)
            
    # 3. document.xml
    doc_p = os.path.join(temp_dir, 'word', 'document.xml')
    if os.path.exists(doc_p):
        with open(doc_p, 'r', encoding='utf-8') as f:
            d_txt = f.read()
            
        # Ensure every <w:p> has <w:pPr><w:bidi/><w:jc w:val="right"/></w:pPr>
        def patch_p(m):
            p_str = m.group(0)
            if '<w:pPr>' not in p_str:
                p_str = p_str.replace('<w:p', '<w:p><w:pPr><w:bidi/><w:jc w:val="right"/></w:pPr>', 1)
            else:
                if '<w:bidi/>' not in p_str and '<w:bidi' not in p_str:
                    p_str = p_str.replace('<w:pPr>', '<w:pPr><w:bidi/>', 1)
                if '<w:jc' not in p_str:
                    p_str = p_str.replace('</w:pPr>', '<w:jc w:val="right"/></w:pPr>', 1)
            return p_str
        d_txt = re.sub(r'<w:p[ >].*?</w:p>', patch_p, d_txt, flags=re.DOTALL)
        
        # Ensure every table has bidiVisual
        d_txt = re.sub(r'<w:tblPr>(.*?)</w:tblPr>', lambda m: '<w:tblPr>' + (m.group(1) if '<w:bidiVisual/>' in m.group(1) else m.group(1) + '<w:bidiVisual/><w:jc w:val="right"/>') + '</w:tblPr>', d_txt, flags=re.DOTALL)
        
        # Ensure every section has bidi
        d_txt = re.sub(r'<w:sectPr>(.*?)</w:sectPr>', lambda m: '<w:sectPr>' + (m.group(1) if '<w:bidi/>' in m.group(1) else '<w:bidi/><w:rtlGutter/>' + m.group(1)) + '</w:sectPr>', d_txt, flags=re.DOTALL)
        
        with open(doc_p, 'w', encoding='utf-8') as f:
            f.write(d_txt)
            
    os.remove(docx_path)
    with zipfile.ZipFile(docx_path, 'w', zipfile.ZIP_DEFLATED) as z_out:
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                fp = os.path.join(root, file)
                rp = os.path.relpath(fp, temp_dir)
                z_out.write(fp, rp)
                
    shutil.rmtree(temp_dir)
    print("Injected Flawless DOCX RTL with EMBEDDED IMAGES into:", docx_path)

# Apply to all 6 docx files
for dp in [
    '/home/yogi/lod_project/PLUMBING_DESIGNER_CORRECTION_AND_CLOSURE_REPORT_REV01.docx',
    '/home/yogi/lod_project/HVAC_DESIGNER_CORRECTION_AND_CLOSURE_REPORT_REV01.docx',
    '/home/yogi/lod_project/ELECTRICAL_DESIGNER_CORRECTION_AND_CLOSURE_REPORT_REV01.docx',
    '/home/yogi/lod_project/STRUCTURE_DESIGNER_CORRECTION_AND_CLOSURE_REPORT_REV01.docx',
    '/home/yogi/lod_project/LANDSCAPE_DESIGNER_CORRECTION_AND_CLOSURE_REPORT_REV01.docx',
    '/home/yogi/lod_project/MARKETING_VS_EXECUTION_DESIGNER_CLOSURE_REPORT_REV01.docx'
]:
    if os.path.exists(dp):
        inject_flawless_docx_rtl(dp)
