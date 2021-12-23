# PyMuPDF
import fitz
import io
from PIL import Image

# path to our input file
pdf_file = "sample.pdf"

# Input PDF file
pdf_file = fitz.open(pdf_file)

for page_no in range(len(pdf_file)):
    curr_page = pdf_file[page_no]
    images = curr_page.get_images()

    for image_no, image in enumerate(curr_page.get_images()):
        # get the XREF of the image
        xref = image[0]
        # extract the image bytes
        curr_image = pdf_file.extract_image(xref)
        img_bytes = curr_image["image"]
        # get the image extension
        img_extension = curr_image["ext"]
        # load it to PIL
        image = Image.open(io.BytesIO(img_bytes))
        # save it to local disk
        image.save(open(f"page{page_no+1}_img{image_no}.{img_extension}", "wb"))
