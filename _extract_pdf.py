from pathlib import Path
from pypdf import PdfReader
output_path = Path('_pdf_text.txt')
path = Path('【重要】-YiChip BL ASM.pdf')
reader = PdfReader(str(path))
with output_path.open('w', encoding='utf-8') as f:
    for i, page in enumerate(reader.pages, 1):
        text = page.extract_text() or ''
        f.write(f'=== Page {i} ===\n')
        f.write(text)
        f.write('\n')
