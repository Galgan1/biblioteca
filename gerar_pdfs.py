import os
from playwright.sync_api import sync_playwright
from PyPDF2 import PdfMerger, PdfReader

BASE_URL = "http://localhost:8000"

# Usa as paginas otimizadas para impressao (pasta print/)
pages = [
    {"url": f"{BASE_URL}/print/00_visao_geral.html", "output": "00_Visao_Geral.pdf"},
    {"url": f"{BASE_URL}/print/01_introducao.html", "output": "01_Introducao.pdf"},
    {"url": f"{BASE_URL}/print/02_capitulo_1.html", "output": "02_Capitulo_1.pdf"},
    {"url": f"{BASE_URL}/print/03_capitulo_2.html", "output": "03_Capitulo_2.pdf"},
    {"url": f"{BASE_URL}/print/04_capitulo_3.html", "output": "04_Capitulo_3.pdf"},
    {"url": f"{BASE_URL}/print/05_capitulo_4.html", "output": "05_Capitulo_4.pdf"},
    {"url": f"{BASE_URL}/print/06_capitulo_5.html", "output": "06_Capitulo_5.pdf"},
    {"url": f"{BASE_URL}/print/07_capitulo_6.html", "output": "07_Capitulo_6.pdf"},
    {"url": f"{BASE_URL}/print/08_capitulo_7.html", "output": "08_Capitulo_7.pdf"},
    {"url": f"{BASE_URL}/print/09_capitulo_8.html", "output": "09_Capitulo_8.pdf"},
]

OUTPUT_DIR = "pdfs"
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

generated_pdfs = []

print("Iniciando geracao de PDFs (1 pagina por capitulo, layout otimizado)...")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    
    for item in pages:
        print(f"\nAcessando {item['url']}...")
        page = browser.new_page()
        page.goto(item['url'], wait_until="networkidle")
        page.wait_for_timeout(1500)
        
        output_path = os.path.join(OUTPUT_DIR, item['output'])
        
        # Gerar PDF com margem zero (a pagina HTML ja tem seu proprio padding)
        page.pdf(
            path=output_path,
            format="A4",
            print_background=True,
            scale=1.0,
            margin={"top": "0", "bottom": "0", "left": "0", "right": "0"}
        )
        
        # Validar
        reader = PdfReader(output_path)
        num_pages = len(reader.pages)
        
        if num_pages == 1:
            print(f"[{item['output']}] OK - Exatamente 1 pagina.")
        else:
            print(f"[{item['output']}] AVISO - {num_pages} pagina(s). Ajustando scale...")
            # Se tiver mais de 1 pagina, tentar escalar para caber
            content_height = page.evaluate("() => document.documentElement.scrollHeight")
            a4_height = 1123
            new_scale = a4_height / content_height
            if new_scale < 0.1:
                new_scale = 0.1
            
            page.pdf(
                path=output_path,
                format="A4",
                print_background=True,
                scale=new_scale,
                margin={"top": "0", "bottom": "0", "left": "0", "right": "0"}
            )
            reader2 = PdfReader(output_path)
            print(f"[{item['output']}] Re-gerado com scale={new_scale:.3f} -> {len(reader2.pages)} pagina(s).")
        
        generated_pdfs.append(output_path)
        page.close()
        
    browser.close()

print("\n--- Resumo ---")
total = 0
for pdf in generated_pdfs:
    reader = PdfReader(pdf)
    n = len(reader.pages)
    total += n
    print(f"  {os.path.basename(pdf)}: {n} pagina(s)")

print(f"\nUnindo {len(generated_pdfs)} PDFs no Livro Completo...")
merger = PdfMerger()

for pdf in generated_pdfs:
    merger.append(pdf)

final_output = os.path.join(OUTPUT_DIR, "O_Significado_do_Casamento_Completo.pdf")
merger.write(final_output)
merger.close()

reader = PdfReader(final_output)
print(f"Livro completo: {len(reader.pages)} paginas em {final_output}")
