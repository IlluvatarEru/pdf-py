import os

from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def create_image_overlay(image_path, filename, x, y, page_size):
    c = canvas.Canvas(filename, pagesize=page_size)
    c.drawImage(image_path, x, y)
    c.save()


def add_image_to_pdf(input_pdf_path, output_pdf_path, image_path, page_number, x, y):
    # Create a temporary PDF with the image overlay
    overlay_pdf_path = "overlay.pdf"
    create_image_overlay(image_path, overlay_pdf_path, x, y, A4)

    # Read the input PDF
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    # Open the overlay PDF and read it
    with open(overlay_pdf_path, "rb") as overlay_file:
        overlay_reader = PdfReader(overlay_file)
        overlay_page = overlay_reader.pages[0]

        # Add all pages to the writer, merging the overlay with the specified page
        for i in range(len(reader.pages)):
            page = reader.pages[i]
            if i == page_number - 1:  # If it's the page to modify (0-based index)
                page.merge_page(overlay_page)
            writer.add_page(page)

    # Write the modified PDF to the output path
    with open(output_pdf_path, "wb") as output_pdf:
        writer.write(output_pdf)

    # Clean up temporary overlay file
    os.remove(overlay_pdf_path)
