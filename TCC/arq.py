import fitz
import unicodedata
import os

dirPath = r"C:\Users\entra21\Desktop\curriculos"
result = next(os.walk(dirPath))[2]

for i in result:
    DIGITIZED_FILE = rf"C:\Users\entra21\Desktop\curriculos\{i}"
    SCANNED_FILE = rf"C:\Users\entra21\Desktop\curriculos\{i}"

    with fitz.open(DIGITIZED_FILE) as doc:
        for page in doc:
            text = page.get_text()
    new_text = ''.join(ch for ch in unicodedata.normalize('NFKD', text).lower()
                       if not unicodedata.combining(ch))

    print(new_text)