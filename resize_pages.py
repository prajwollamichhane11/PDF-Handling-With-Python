import PyPDF2

pdf = "sample.pdf"

pdf = PyPDF2.PdfFileReader(pdf)
page0 = pdf.getPage(0)
# Resizing the first page
page0.scaleBy(0.5)
resized = PyPDF2.PdfFileWriter()
resized.addPage(page0)
with open("sample2.pdf", "wb+") as f:
    resized.write(f)