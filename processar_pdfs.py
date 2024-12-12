import os
import sys
import fitz  # PyMuPDF
from PIL import Image
import io

def main():
    # Determina o diretório raiz dependendo se está rodando em modo 'frozen' (executável) ou não.
    if getattr(sys, 'frozen', False):
        root_dir = os.path.dirname(sys.executable)
    else:
        root_dir = os.path.dirname(os.path.abspath(__file__))

    pdf_dir = os.path.join(root_dir, "PDF")
    imagens_dir = os.path.join(root_dir, "Imagens")

    # Verifica se a pasta PDF existe
    if not os.path.exists(pdf_dir):
        print("A pasta 'PDF' não foi encontrada no diretório do executável.")
        input("Pressione ENTER para sair...")
        return

    # Cria a pasta Imagens se não existir
    if not os.path.exists(imagens_dir):
        print(f"Criando pasta de saída: {imagens_dir}")
        os.makedirs(imagens_dir)

    pdf_files = [f for f in os.listdir(pdf_dir) if f.lower().endswith(".pdf")]

    if not pdf_files:
        print("Nenhum arquivo PDF encontrado na pasta 'PDF'.")
        input("Pressione ENTER para sair...")
        return

    print(f"Foram encontrados {len(pdf_files)} PDF(s) para processar.\n")

    for filename in pdf_files:
        pdf_path = os.path.join(pdf_dir, filename)
        base_name = os.path.splitext(filename)[0]

        pdf_imagens_dir = os.path.join(imagens_dir, base_name)
        if not os.path.exists(pdf_imagens_dir):
            print(f"Criando pasta para o PDF '{base_name}': {pdf_imagens_dir}")
            os.makedirs(pdf_imagens_dir)

        print(f"\nProcessando PDF: {filename}")

        # Abre o PDF
        doc = fitz.open(pdf_path)

        # Definição da escala para 300 DPI
        zoom = 300.0 / 72.0
        mat = fitz.Matrix(zoom, zoom)

        num_paginas = len(doc)
        print(f"Total de páginas: {num_paginas}")

        for page_index, page in enumerate(doc, start=1):
            print(f"Processando página {page_index}/{num_paginas}...")

            # Rasterização da página completa
            full_page_pix = page.get_pixmap(matrix=mat, alpha=False)
            raster_filename = f"pagina_{page_index}_rasterizada.png"
            raster_path = os.path.join(pdf_imagens_dir, raster_filename)
            full_page_pix.save(raster_path)
            print(f" - Página rasterizada salva em: {raster_filename}")

            # Extração de imagens incorporadas
            images = page.get_images(full=True)
            image_count = 1
            for img in images:
                xref = img[0]
                pixmap = doc.extract_image(xref)
                img_data = pixmap["image"]
                pil_img = Image.open(io.BytesIO(img_data))
                embedded_img_filename = f"pagina_{page_index}_imagem_{image_count}.jpg"
                embedded_img_path = os.path.join(pdf_imagens_dir, embedded_img_filename)
                pil_img.convert("RGB").save(embedded_img_path, "JPEG")
                print(f" - Imagem incorporada extraída: {embedded_img_filename}")
                image_count += 1

            # Extração dos componentes de imagem individuais da página
            page_dict = page.get_text("rawdict")
            component_count = 1
            for block in page_dict["blocks"]:
                if block["type"] == 1:
                    bbox = block["bbox"]  # [x0, y0, x1, y1]
                    clip_rect = fitz.Rect(bbox)
                    component_pix = page.get_pixmap(matrix=mat, alpha=False, clip=clip_rect)
                    component_filename = f"pagina_{page_index}_componente_{component_count}.png"
                    component_path = os.path.join(pdf_imagens_dir, component_filename)
                    component_pix.save(component_path)
                    print(f" - Componente de imagem extraído: {component_filename}")
                    component_count += 1

        doc.close()
        print(f"\nConcluído processamento do PDF: {filename}")

    print("\nTodos os PDFs foram processados com sucesso.")

    print("\n--------------------------------------------------------")
    print("Créditos:")
    print("Desenvolvido por: Michael Souto (Desenvolvedor)")
    print("Código-fonte disponível no GitHub: https://github.com/michael-souto/image_from_pdf")
    print("--------------------------------------------------------")

    input("Pressione ENTER para sair...")
    
if __name__ == "__main__":
    main()
