import docx2txt
import os

dirPath = r"C:\Users\entra21\Desktop\testes"
result = next(os.walk(dirPath))[2]
for j in result:
    texto = docx2txt.process(fr"C:\Users\entra21\Desktop\testes\{j}").lower()
    palavras = ['python', 'inglês']

    for i in palavras:
        if i in texto:
            print(f'DOCX({j}) - Palavra "{i}": ✔')
            # print(fr"C:\Users\entra21\Desktop\testes\{j}")
        else:
            print(f'DOCX({j}) - Palavra "{i}": ❌')
    print()
