import os

import fitz


dirPath = r"C:\Users\entra21\Desktop\testes"
result = next(os.walk(dirPath))[2]

for j in result:
    palavras = ['vitor', 'silva', 'maria', 'python', 'beautiful']

    DIGITIZED_FILE = fr"C:\Users\entra21\Desktop\testes\{j}".lower()
    SCANNED_FILE = fr"C:\Users\entra21\Desktop\testes\{j}".lower()
    try:
        with fitz.open(DIGITIZED_FILE) as doc:
           for page in doc:
               text = page.get_text()
               for palavra in palavras:
                   if palavra in text:
                       print(f'PDF - Palavra "{palavra}": ✔')
                   else:
                       print(f'PDF - Palavra "{palavra}": ❌')
    except:
        pass
