import os

from PyPDF2 import PdfMerger


def combine_pdfs(pdf_list, folder_path, output_filename):
    """
    Combine the pdfs in pdf list located at folder_path into output_filename

    :param pdf_list: list of str
    :param folder_path: str, folder in which all the pdfs are located
    :param output_filename: str
    :return:
    """
    merger = PdfMerger()

    for pdf in pdf_list:
        pdf_path = os.path.join(folder_path, pdf)
        merger.append(pdf_path)

    output_path = os.path.join(folder_path, output_filename)
    merger.write(output_path)
    merger.close()
