from django.shortcuts import render
import docx2txt
import fitz
import unicodedata
import os


def mamba(request, ):
    dirPath = r"C:\Users\entra21\Desktop\testes"
    lista_arquivos = next(os.walk(dirPath))[2]

    lista_quantidade_palavras, texto, lista_final = [], [], []
    total = 0
    quantidade = ''
    palavras_chave = 'python'
    novas_palavras = ''.join(ch for ch in unicodedata.normalize('NFKD', palavras_chave).lower()
                             if not unicodedata.combining(ch))
    try:
        for i in lista_arquivos:
            sum = 0
            texto = docx2txt.process(fr"C:\Users\entra21\Desktop\testes\{i}")
            novo_texto = ''.join(ch for ch in unicodedata.normalize('NFKD', texto).lower()
                                 if not unicodedata.combining(ch))

            total = len(novas_palavras)

            for palavra in novas_palavras:
                if palavra in novo_texto:
                    sum += 1
                else:
                    continue
            lista_quantidade_palavras.append(sum)

        for arquivo, quantidade_palavras in zip(lista_arquivos, lista_quantidade_palavras):
            quantidade = [arquivo, quantidade_palavras, total]
            lista_final.append(quantidade)
    except:
        text = ''

        for i in lista_arquivos:
            sum = 0

            with fitz.open(rf"C:\Users\entra21\Desktop\testes\{i}") as doc:
                for page in doc:
                    text = page.get_text()
            new_text = ''.join(ch for ch in unicodedata.normalize('NFKD', text).lower()
                               if not unicodedata.combining(ch))

            for j in novas_palavras:
                if j in new_text:
                    sum += 1
                else:
                    continue
            lista_quantidade_palavras.append(sum)

        for arquivo, quantidade_palavras in zip(lista_arquivos, lista_quantidade_palavras):
            quantidade = [arquivo, quantidade_palavras, total]
            lista_final.append(quantidade)

    return render(request, 'vcode_test/mamba.html', {'lista_final': lista_final})

#
# def index(request):
#     dirPath = r"C:\Users\entra21\Desktop\testes"
#     # dirPath = r"C:\Users\cairo\OneDrive\Área de Trabalho\tcc_test" # Home
#     lista_arquivos = next(os.walk(dirPath))[2]
#
#     lista_quantidade_palavras, palavras_chave, texto, lista_final = [], [], [], []
#     total = 0
#     quantidade = ''
#
#     for i in lista_arquivos:
#         sum = 0
#         texto = docx2txt.process(fr"C:\Users\entra21\Desktop\testes\{i}").lower()
#
#         # texto = docx2txt.process(fr"C:\Users\cairo\OneDrive\Área de Trabalho\tcc_test\{i}").lower()
#         palavras_chave = ['python', 'vitor da silva']
#         total = len(palavras_chave)
#
#         for palavra in palavras_chave:
#             if palavra in texto:
#                 sum += 1
#             else:
#                 continue
#         lista_quantidade_palavras.append(sum)
#
#     for arquivo, quantidade_palavras in zip(lista_arquivos, lista_quantidade_palavras):
#         quantidade = [arquivo, quantidade_palavras, total]
#         lista_final.append(quantidade)
#
#     return render(request, 'vcode_test/index.html', {'lista_final': lista_final,
#                                                      'palavras_chave': palavras_chave, })
