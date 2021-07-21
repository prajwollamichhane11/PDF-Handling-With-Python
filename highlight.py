import fitz

pdf_file = fitz.open("sample.pdf")

for page in pdf_file:
    text = "<sample_text_to_highlight>"
    match_words = page.searchFor(text)

    for word in match_words:
        highlight = page.addHighlightAnnot(word)
        highlight.update()

pdf_file.save("output.pdf")