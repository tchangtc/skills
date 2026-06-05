"""
Minimal xlsx generator using only Python standard library.
Generates valid .xlsx files without any external dependencies.
"""
import zipfile

def _escape_xml(s):
    """Escape special XML characters."""
    if s is None:
        return ""
    s = str(s)
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&apos;")

def generate_xlsx(filename, headers, rows, sheet_name="Sheet1", col_widths=None):
    """
    Generate a valid .xlsx file.

    Args:
        filename: Output file path
        headers: List of header strings
        rows: List of lists (each inner list is a row)
        sheet_name: Name of the worksheet
        col_widths: Optional list of column widths (in characters)
    """
    # Collect all strings for shared strings table
    shared_strings = []
    ss_index = {}

    def get_ss_index(s):
        s = str(s) if s is not None else ""
        if s not in ss_index:
            ss_index[s] = len(shared_strings)
            shared_strings.append(s)
        return ss_index[s]

    # Pre-index all strings
    for h in headers:
        get_ss_index(h)
    for row in rows:
        for cell in row:
            get_ss_index(cell)

    # Build XML files
    content_types = _build_content_types()
    rels = _build_rels()
    workbook_xml = _build_workbook(sheet_name)
    workbook_rels = _build_workbook_rels()
    styles_xml = _build_styles()
    shared_strings_xml = _build_shared_strings(shared_strings)
    sheet_xml = _build_sheet(headers, rows, get_ss_index, col_widths)

    # Write ZIP
    with zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.writestr('[Content_Types].xml', content_types)
        zf.writestr('_rels/.rels', rels)
        zf.writestr('xl/workbook.xml', workbook_xml)
        zf.writestr('xl/_rels/workbook.xml.rels', workbook_rels)
        zf.writestr('xl/styles.xml', styles_xml)
        zf.writestr('xl/sharedStrings.xml', shared_strings_xml)
        zf.writestr('xl/worksheets/sheet1.xml', sheet_xml)

def _col_letter(idx):
    """Convert 0-based column index to Excel column letter(s)."""
    result = ""
    while True:
        result = chr(65 + idx % 26) + result
        idx = idx // 26 - 1
        if idx < 0:
            break
    return result

def _build_content_types():
    return '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>
  <Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
  <Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>
  <Override PartName="/xl/sharedStrings.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sharedStrings+xml"/>
</Types>'''

def _build_rels():
    return '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>
</Relationships>'''

def _build_workbook(sheet_name):
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <sheets>
    <sheet name="{_escape_xml(sheet_name)}" sheetId="1" r:id="rId1"/>
  </sheets>
</workbook>'''

def _build_workbook_rels():
    return '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/sharedStrings" Target="sharedStrings.xml"/>
</Relationships>'''

def _build_styles():
    """Build styles XML with header style (bold, colored background) and wrap text."""
    return '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
  <fonts count="2">
    <font><sz val="10"/><name val="Arial"/></font>
    <font><b/><sz val="10"/><color rgb="FFFFFFFF"/><name val="Arial"/></font>
  </fonts>
  <fills count="3">
    <fill><patternFill patternType="none"/></fill>
    <fill><patternFill patternType="gray125"/></fill>
    <fill><patternFill patternType="solid"><fgColor rgb="FF2F5496"/></patternFill></fill>
  </fills>
  <borders count="2">
    <border><left/><right/><top/><bottom/><diagonal/></border>
    <border>
      <left style="thin"><color auto="1"/></left>
      <right style="thin"><color auto="1"/></right>
      <top style="thin"><color auto="1"/></top>
      <bottom style="thin"><color auto="1"/></bottom>
      <diagonal/>
    </border>
  </borders>
  <cellStyleXfs count="1">
    <xf numFmtId="0" fontId="0" fillId="0" borderId="0"/>
  </cellStyleXfs>
  <cellXfs count="4">
    <xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/>
    <xf numFmtId="0" fontId="1" fillId="2" borderId="1" xfId="0" applyFont="1" applyFill="1" applyBorder="1" applyAlignment="1">
      <alignment horizontal="center" vertical="center" wrapText="1"/>
    </xf>
    <xf numFmtId="0" fontId="0" fillId="0" borderId="1" xfId="0" applyBorder="1" applyAlignment="1">
      <alignment vertical="top" wrapText="1"/>
    </xf>
    <xf numFmtId="0" fontId="0" fillId="0" borderId="1" xfId="0" applyBorder="1" applyAlignment="1">
      <alignment vertical="top" wrapText="1"/>
    </xf>
  </cellXfs>
</styleSheet>'''

def _build_shared_strings(strings):
    parts = [f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>']
    parts.append(f'<sst xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" count="{len(strings)}" uniqueCount="{len(strings)}">')
    for s in strings:
        parts.append(f'  <si><t>{_escape_xml(s)}</t></si>')
    parts.append('</sst>')
    return '\n'.join(parts)

def _build_sheet(headers, rows, get_ss_index, col_widths):
    parts = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>']
    parts.append('<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">')

    # Column widths
    if col_widths:
        parts.append('  <cols>')
        for i, w in enumerate(col_widths):
            parts.append(f'    <col min="{i+1}" max="{i+1}" width="{w}" customWidth="1"/>')
        parts.append('  </cols>')

    parts.append('  <sheetData>')

    # Header row (style 1 = bold white on blue)
    row_num = 1
    parts.append(f'    <row r="{row_num}" ht="30">')
    for j, h in enumerate(headers):
        ref = f'{_col_letter(j)}{row_num}'
        si = get_ss_index(h)
        parts.append(f'      <c r="{ref}" s="1" t="s"><v>{si}</v></c>')
    parts.append('    </row>')

    # Data rows (style 2 = wrap text with border)
    for i, row in enumerate(rows):
        row_num = i + 2
        parts.append(f'    <row r="{row_num}">')
        for j, cell in enumerate(row):
            ref = f'{_col_letter(j)}{row_num}'
            si = get_ss_index(cell)
            parts.append(f'      <c r="{ref}" s="2" t="s"><v>{si}</v></c>')
        parts.append('    </row>')

    parts.append('  </sheetData>')

    # Auto-filter on header row
    last_col = _col_letter(len(headers) - 1)
    parts.append(f'  <autoFilter ref="A1:{last_col}{len(rows)+1}"/>')

    # Freeze top row
    parts.append('  <sheetViews><sheetView tabSelected="1" workbookViewId="0">')
    parts.append('    <pane ySplit="1" topLeftCell="A2" activePane="bottomLeft" state="frozen"/>')
    parts.append('  </sheetView></sheetViews>')

    parts.append('</worksheet>')
    return '\n'.join(parts)
