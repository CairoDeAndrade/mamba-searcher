import fitz

DIGITIZED_FILE = "pdffoda.pdf.pdf"
SCANNED_FILE = "pdffoda.pdf.pdf"
with fitz.open(DIGITIZED_FILE) as doc:
   for page in doc:
       text = page.get_text()
       print(text)
