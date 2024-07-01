import glob
import os

from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def create_watermark(text, filename, x, y):
    c = canvas.Canvas(filename, pagesize=A4)
    c.drawString(x, y, text)
    c.save()


def add_text_to_pdf(input_pdf_path, output_pdf_path, text, page_number, x, y):
    # Create a temporary PDF with the text
    watermark_pdf_path = "watermark.pdf"
    create_watermark(text, watermark_pdf_path, x, y)

    # Read the input PDF
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    # Add all pages to the writer
    for i in range(len(reader.pages)):
        if i == page_number - 1:  # If it's the page to modify
            page = reader.pages[i]
            with open(watermark_pdf_path, "rb") as watermark_file:
                watermark_reader = PdfReader(watermark_file)
                page.merge_page(watermark_reader.pages[0])
                writer.add_page(page)
        else:
            writer.add_page(reader.pages[i])

    # Write the modified PDF to the output path
    with open(output_pdf_path, "wb") as output_pdf:
        writer.write(output_pdf)

    # Clean up temporary watermark file
    os.remove(watermark_pdf_path)


def add_text_to_all_files(input_path, file_pattern, text, page_number, x, y):
    # Create a pattern for matching the files
    pattern = os.path.join(input_path, file_pattern)

    # Loop through all files matching the pattern
    for file_path in glob.glob(pattern):
        file_path = file_path.replace("\\", "/")
        add_text_to_pdf(file_path, file_path, text, page_number, x, y)
