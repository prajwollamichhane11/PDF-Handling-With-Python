# Import Module
import pdfx

# Read PDF File
pdf = pdfx.PDFx("sample1.pdf")

# Get list of URL
print(pdf.get_references_as_dict())