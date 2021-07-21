from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_file = open("sample.pdf", "rb")
reader = PdfFileReader(pdf_file)
writer = PdfFileWriter()

writer.appendPagesFromReader(reader)
metadata = reader.getDocumentInfo()
writer.addMetadata(metadata)

writer.addMetadata({"/Author": "John Doe"})

output = open("result.pdf", "wb")
writer.write(output)

pdf_file.close()
output.close()