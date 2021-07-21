from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.colors import red

canvas = Canvas("text-pdf.pdf", pagesize=LETTER)
canvas.setFont("Courier", 16)
canvas.setFillColor(red)
canvas.drawString(2 * inch, 8 * inch, "This is a newly created Python PDF.")

canvas.save()
