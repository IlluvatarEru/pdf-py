from PyPDF2 import PdfReader, PdfWriter


def extract_page(source_path, dest_path, n_page):
    reader = PdfReader(source_path)
    if len(reader.pages) >= n_page:
        writer = PdfWriter()
        writer.add_page(reader.pages[n_page - 1])
        with open(dest_path, 'wb') as output_pdf:
            writer.write(output_pdf)


def extract_pages_from_to(source_path, dest_path, page_from, page_to):
    reader = PdfReader(source_path)
    writer = PdfWriter()

    if len(reader.pages) >= page_to:
        for i in range(page_from - 1, page_to):
            writer.add_page(reader.pages[i])

        with open(dest_path, 'wb') as output_pdf:
            writer.write(output_pdf)
    else:
        print(f"File {source_path} does not have enough pages.")
