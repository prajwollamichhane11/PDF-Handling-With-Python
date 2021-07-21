# Extracting Informations
# Python PDF extract text
# _______________________________________________________________

# importing required modules
import PyPDF2

# creating a pdf file object
pdfFileObj = open("sample.pdf", "rb")

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
print(pdfReader.numPages)

# creating a page object
pageObj = pdfReader.getPage(0)

# extracting text from page
print(pageObj.extractText())

texts = pageObj.extractText()

print(texts)

# closing the pdf file object
pdfFileObj.close()


# Python PDF extract image
# _______________________________________________________________


# Python PDF extract table
# _______________________________________________________________


# Python PDF extract URLs
# _______________________________________________________________


# PDF extract page as an image
# _______________________________________________________________
