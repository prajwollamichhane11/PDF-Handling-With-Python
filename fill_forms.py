import pdfrw
from datetime import date


ANNOT_KEY = "/Annots"


def fill_pdf(input_pdf_path, output_pdf_path, data):
    template_pdf = pdfrw.PdfReader(input_pdf_path)
    for page in template_pdf.pages:
        annotations = page[ANNOT_KEY]
        i = 0
        for annotation in annotations:
            annotation.update(pdfrw.PdfDict(V=data[i]))
            i += 1
    template_pdf.Root.AcroForm.update(
        pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject("true"))
    )
    pdfrw.PdfWriter().write(output_pdf_path, template_pdf)


if __name__ == "__main__":
    pdf_template = "personal_information.pdf"
    pdf_output = "output.pdf"

    data = ["John", "Doe", "28", "others", "3123123123", "Ohio"]
    fill_pdf(pdf_template, pdf_output, data)
