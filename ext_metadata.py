from PyPDF2 import PdfFileReader

with open("result.pdf", "rb") as f:
    pdf = PdfFileReader(f)
    info = pdf.getDocumentInfo()
    number_of_pages = pdf.getNumPages()

    print(info)
