import fitz
import unicodedata
import os

tem = []
ntem = []

dirPath = r"C:\Users\entra21\Desktop\curriculos"
result = next(os.walk(dirPath))[2]

word = input("Digite palavra: ")
new_input = ''.join(ch for ch in unicodedata.normalize('NFKD', word).lower()
                    if not unicodedata.combining(ch))
word = new_input.split()
for i in result:
    DIGITIZED_FILE = rf"C:\Users\entra21\Desktop\curriculos\{i}"
    SCANNED_FILE = rf"C:\Users\entra21\Desktop\curriculos\{i}"

    with fitz.open(DIGITIZED_FILE) as doc:
        for page in doc:
            text = page.get_text()
    new_text = ''.join(ch for ch in unicodedata.normalize('NFKD', text).lower()
                       if not unicodedata.combining(ch))
    print(new_text)
    text = new_text.split()

    for j in word:
        if j in text:
            print(f"{i} Tem a palavra {j}")
            tem.append(i)
        else:
            print(f"{i} Não tem a palavra {j}")
            ntem.append(i)



    print(f"\033[1;32mO arquivo {i} tem {tem.count(i)} de {len(word)}\033[0;0m")
