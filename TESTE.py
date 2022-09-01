import docx2txt
import os

dirPath = r"C:\Users\entra21\PycharmProjects\TCC\tcc-entra21\docx\testes"

result = next(os.walk(dirPath))[2]

for j in result:
    texto = docx2txt.process(fr"C:\Users\entra21\PycharmProjects\TCC\tcc-entra21\docx\testes\{j}").lower()
    palavras = ['vitor da silva', 'ave', 'maria', 'blumenau', 'beautiful']

    for i in palavras:
        if i in texto:
            print(f'DOCX({j}) - Palavra "{i}": ✔')
            print(fr"C:\Users\entra21\Desktop\testes\{j}")
        else:
            print(f'DOCX({j}) - Palavra "{i}": ❌')
    print()
