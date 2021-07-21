from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.pdf import ContentStream
from PyPDF2.generic import TextStringObject, NameObject
from PyPDF2.utils import b_

# watermark to remove
wm_text = "DOI"
# replacing the watermark with nothing
replace_with = "Hello Hello"

# Load PDF into pyPDF
source = PdfFileReader("sample.pdf")
output = PdfFileWriter()

# Iterating through each page
for page in range(source.getNumPages()):
    # Current Page
    page = source.getPage(page)
    content_object = page["/Contents"].getObject()
    content = ContentStream(content_object, source)

    # Iterating over all pdf elements
    for operands, operator in content.operations:
        if operator == b_("TJ"):
            text = operands[0][0]
            if isinstance(text, TextStringObject) and text.startswith(wm_text):
                operands[0] = TextStringObject(replace_with)

    page.__setitem__(NameObject("/Contents"), content)

    output.addPage(page)

outputStream = open("output.pdf", "wb")
output.write(outputStream)