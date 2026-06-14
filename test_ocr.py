import fitz
import os
import json

pdf_path = r"C:\Users\User\Downloads\Robert McKee - Story (pdf).pdf"
output_dir = r"C:\Users\User\AppData\Local\Temp\book_skill_work"
os.makedirs(output_dir, exist_ok=True)

doc = fitz.open(pdf_path)
total_pages = len(doc)
print(f"Total pages: {total_pages}")

# Try OCR via pymupdf's built-in Tesseract wrapper
try:
    page = doc[10]
    tp = page.get_textpage(flags=fitz.TEXT_PRESERVE_WHITESPACE)
    text = tp.extractText()
    if len(text.strip()) > 50:
        print(f"PyMuPDF textpage works! Got {len(text)} chars")
        print(text[:500])
    else:
        print(f"PyMuPDF textpage returned only {len(text.strip())} chars, trying OCR flag...")
        # Try with OCR
        tp_ocr = page.get_textpage_ocr(flags=0, language="eng", dpi=300)
        text_ocr = tp_ocr.extractText()
        print(f"OCR result: {len(text_ocr)} chars")
        print(text_ocr[:500])
except Exception as e:
    print(f"Error: {e}")
    print("Will need alternative OCR approach")

doc.close()
