import camelot

# tables = camelot.read_pdf("table.pdf")
# pass comma seperated page numbers or page ranges
tables = camelot.read_pdf("1.pdf")
print(tables[0].df)
