import fitz

doc = fitz.open("sample.pdf")
rect = fitz.Rect(0, 0, 100, 100)


for page in doc:
    page.insertImage(rect, filename="logo.jpg")


doc.save("output.pdf")