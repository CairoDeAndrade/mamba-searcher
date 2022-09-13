from PyPDF2 import PdfReader

reader = PdfReader("2021-03-19_exemplo-pdf.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()
print(text)
print("Ao clica com o botão" in text)