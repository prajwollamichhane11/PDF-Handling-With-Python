from pdf2image import convert_from_path

pages = convert_from_path("sample.pdf", 120)

for page in pages:
    page.save("out.jpg", "JPEG")
