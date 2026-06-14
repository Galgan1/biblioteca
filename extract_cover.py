import fitz
import sys

pdf_path = r"C:\Users\User\Downloads\Maquiavel Pedagogo - Pascal Bernardin.pdf"
out_path = r"assets\maquiavel-cover.jpg"

try:
    doc = fitz.open(pdf_path)
    page = doc.load_page(0) # First page
    pix = page.get_pixmap(dpi=150)
    pix.save(out_path)
    print(f"Sucesso: Capa salva em {out_path}")
except Exception as e:
    print(f"Erro: {e}")
    sys.exit(1)
