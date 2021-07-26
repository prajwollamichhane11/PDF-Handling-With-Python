from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

document = SimpleDocTemplate("table.pdf", pagesize=letter)
items = []
# Data to be stored on table
data = [
    ["ID", "312hk"],
    ["Name", "John Doe"],
    ["Profession", "Software Development"],
    ["Age", "29"],
    ["Sex", "Male"],
    ["Location", "Ohio"],
]
# Creating the table with 6 rows
t = Table(data, 1 * [1.6 * inch], 6 * [0.5 * inch])
# setting up style and alignments of borders and grids
t.setStyle(
    TableStyle(
        [
            ("ALIGN", (1, 1), (0, 0), "LEFT"),
            ("VALIGN", (-1, -1), (-1, -1), "TOP"),
            ("ALIGN", (-1, -1), (-1, -1), "RIGHT"),
            ("VALIGN", (-1, -1), (-1, -1), "TOP"),
            ("INNERGRID", (0, 0), (-1, -1), 1, colors.black),
            ("BOX", (0, 0), (-1, -1), 2, colors.black),
        ]
    )
)
items.append(t)
document.build(items)