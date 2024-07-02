from PIL import Image

from src.constants import DOT_PDF
from src.pdf_combining import combine_pdfs


def convert_image_to_pdf(path, image_name, output, rotate_for_portrait=True):
    with Image.open(path + image_name) as img:
        if rotate_for_portrait:
            width, height = img.size
            if width > height:
                img = img.rotate(90, expand=True)

        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        img.save(path + output, "PDF", resolution=100.0)


def convert_images_to_single_pdf(path, images, output_filename, rotate_for_portrait=True):
    pdf_files = []
    for image_name in images:
        image_output = image_name.split(".")[0] + DOT_PDF
        convert_image_to_pdf(path, image_name, image_output, rotate_for_portrait)
        pdf_files.append(image_output)
    combine_pdfs(pdf_files, path, output_filename)
