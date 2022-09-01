import os
import fitz

dirPath = r"C:\Users\entra21\Desktop\teste pdf"
result = next(os.walk(dirPath))[2]

for j in result:
    palavras = ['Python', 'Inglês']

    DIGITIZED_FILE = fr"C:\Users\entra21\Desktop\teste pdf\{j}".lower()
    try:
        with fitz.open(DIGITIZED_FILE) as pdf:
            for page in pdf:
                text = page.get_text()
                for palavra in palavras:
                    if palavra in text:
                        print(f'PDF({j}) - Palavra "{palavra}": ✔')
                    else:
                        print(f'PDF({j}) - Palavra "{palavra}": ❌')
    except:
        pass