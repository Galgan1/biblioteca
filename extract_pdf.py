import sys
import os
import json

pdf_path = r"c:\Users\User\.gemini\antigravity\scratch\biblioteca\downloads\a-arte-da-guerra.pdf"
output_dir = r"c:\Users\User\.gemini\antigravity\scratch\biblioteca\downloads"

# Try PyMuPDF first
try:
    import fitz
    print("Using PyMuPDF (fitz)")
    doc = fitz.open(pdf_path)
    
    # Extract cover image
    page = doc[0]
    pix = page.get_pixmap(dpi=200)
    cover_path = os.path.join(r"c:\Users\User\.gemini\antigravity\scratch\biblioteca\assets", "arte-da-guerra-cover.jpg")
    pix.save(cover_path)
    print(f"Cover saved to {cover_path}")
    
    # Extract full text
    full_text = []
    for i, page in enumerate(doc):
        text = page.get_text()
        full_text.append(f"\n\n--- PAGE {i+1} ---\n\n{text}")
    
    text_path = os.path.join(output_dir, "arte-da-guerra-full.txt")
    with open(text_path, "w", encoding="utf-8") as f:
        f.write("\n".join(full_text))
    
    # Metadata
    meta = {
        "title": doc.metadata.get("title", "A Arte da Guerra"),
        "author": doc.metadata.get("author", "Sun Tzu"),
        "pages": len(doc),
        "words": sum(len(p.get_text().split()) for p in doc),
    }
    meta_path = os.path.join(output_dir, "arte-da-guerra-meta.json")
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2, ensure_ascii=False)
    
    print(f"Text extracted: {meta['pages']} pages, ~{meta['words']} words")
    print(f"Metadata: {json.dumps(meta, indent=2, ensure_ascii=False)}")
    doc.close()

except ImportError:
    print("PyMuPDF not found, trying pdfplumber...")
    try:
        import pdfplumber
        print("Using pdfplumber")
        with pdfplumber.open(pdf_path) as pdf:
            full_text = []
            for i, page in enumerate(pdf.pages):
                text = page.extract_text() or ""
                full_text.append(f"\n\n--- PAGE {i+1} ---\n\n{text}")
            
            text_path = os.path.join(output_dir, "arte-da-guerra-full.txt")
            with open(text_path, "w", encoding="utf-8") as f:
                f.write("\n".join(full_text))
            
            total_words = sum(len(t.split()) for t in full_text)
            print(f"Text extracted: {len(pdf.pages)} pages, ~{total_words} words")
    except ImportError:
        print("ERROR: Neither PyMuPDF nor pdfplumber is installed.")
        print("Install with: pip install PyMuPDF")
        sys.exit(1)
