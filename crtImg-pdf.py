from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.colors import red

canvas = Canvas("new-pdf.pdf", pagesize=LETTER)
canvas.setFont("Courier", 16)
canvas.setFillColor(red)
canvas.drawString(100, 700, "Adding Image Here.")
canvas.drawInlineImage("x.jpeg", 100, 450)

canvas.save()
