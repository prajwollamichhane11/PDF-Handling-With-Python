from io import StringIO
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

# PDFMiner Analyzers
rsrcmgr = PDFResourceManager()
sio = StringIO()
codec = "utf-8"
laparams = LAParams()
device = TextConverter(rsrcmgr, sio, codec=codec, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)

# path to our input file
pdf_file = "sample.pdf"

# Extract text
pdfFile = open(pdf_file, "rb")
for page in PDFPage.get_pages(pdfFile):
    interpreter.process_page(page)
pdfFile.close()

# Return text from StringIO
text = sio.getvalue()

print(text)

# Freeing Up
device.close()
sio.close()
