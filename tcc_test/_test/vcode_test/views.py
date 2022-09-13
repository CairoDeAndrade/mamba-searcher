from django.shortcuts import render
import docx2txt
import os


def index(request):
    dirPath = r"C:\Users\entra21\Desktop\tcc_test"
    lista_arquivos = next(os.walk(dirPath))[2]

    lista_quantidade_palavras, palavras_chave, texto, lista_final = [], [], [], []
    total = 0
    quantidade = ''

    for i in lista_arquivos:
        sum = 0
        texto = docx2txt.process(fr"C:\Users\entra21\Desktop\tcc_test\{i}").lower()
        palavras_chave = ['python', 'inglês', 'cep', 'arquivo']
        total = len(palavras_chave)

        for palavra in palavras_chave:
            if palavra in texto:
                sum += 1
            else:
                continue
        lista_quantidade_palavras.append(sum)

    for arquivo, quantidade_palavras in zip(lista_arquivos, lista_quantidade_palavras):
        quantidade = f'Em {arquivo} >> {quantidade_palavras}/{total}'
        lista_final.append(quantidade)

    return render(request, 'vcode_test/index.html', {'lista_final': lista_final})
