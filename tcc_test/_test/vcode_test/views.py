from django.shortcuts import render
import docx2txt
import os
import fitz
import unicodedata


def mamba(request):
    dirPath = r"C:\Users\entra21\Desktop\testes"
    lista_arquivos = next(os.walk(dirPath))[2]

    lista_quantidade_palavras, palavras_chave, texto, lista_final = [], [], [], []
    total = 0
    quantidade = ''
    palavras_chave = ['python', 'inglês', 'cep', 'arquivo']
    try:



        for i in lista_arquivos:
            sum = 0
            texto = docx2txt.process(fr"C:\Users\entra21\Desktop\testes\{i}").lower()

            total = len(palavras_chave)

            for palavra in palavras_chave:
                if palavra in texto:
                    sum += 1
                else:
                    continue
            lista_quantidade_palavras.append(sum)

        for arquivo, quantidade_palavras in zip(lista_arquivos, lista_quantidade_palavras):
            quantidade = f'Em {arquivo} >> tem {quantidade_palavras}/{total}'
            lista_final.append(quantidade)
    except:


        for i in result:
            DIGITIZED_FILE = rf"C:\Users\entra21\Desktop\curriculos\{i}"
            with fitz.open(DIGITIZED_FILE) as pdf:
                for page in pdf:
                    text = page.get_text()
            new_text = ''.join(ch for ch in unicodedata.normalize('NFKD', text).lower()
                               if not unicodedata.combining(ch))

            text = new_text.split()

            for j in palavras_chave:
                if j in text:
                    print(f"{i} Tem a palavra {j}")
                    tem.append(i)
                else:
                    print(f"{i} Não tem a palavra {j}")
                    ntem.append(i)

            print(f"\033[1;32mO arquivo {i} tem {tem.count(i)} de {len(palavras_chave)}\033[0;0m")

        return render(request, 'vcode_test/mamba.html', {'lista_final': lista_final})


def index(request):
    dirPath = r"C:\Users\entra21\Desktop\testes"
    lista_arquivos = next(os.walk(dirPath))[2]

    lista_quantidade_palavras, palavras_chave, texto, lista_final = [], [], [], []
    total = 0
    quantidade = ''

    for i in lista_arquivos:
        sum = 0
        texto = docx2txt.process(fr"C:\Users\entra21\Desktop\testes\{i}").lower()
        palavras_chave = ['python', 'inglês', 'cep', 'arquivo']
        total = len(palavras_chave)

        for palavra in palavras_chave:
            if palavra in texto:
                sum += 1
            else:
                continue
        lista_quantidade_palavras.append(sum)

    for arquivo, quantidade_palavras in zip(lista_arquivos, lista_quantidade_palavras):
        quantidade = f'Em {arquivo} >> tem {quantidade_palavras}/{total}'
        lista_final.append(quantidade)

    return render(request, 'vcode_test/mamba.html', {'lista_final': lista_final})
