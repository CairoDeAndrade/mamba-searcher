from django.shortcuts import render
import docx2txt
import os


def index(request):
    global i
    # dirPath = r"C:\Users\cairo\OneDrive\Área de Trabalho\tcc_test" home
    dirPath = r"C:\Users\entra21\Desktop\tcc_test"
    result = next(os.walk(dirPath))[2]

    doc_texto, texto, palavras_chave,  = [], [], []
    for i in result:
        # texto = docx2txt.process(fr"C:\Users\cairo\OneDrive\Área de Trabalho\tcc_test\{i}").lower() home
        texto = docx2txt.process(fr"C:\Users\entra21\Desktop\tcc_test\{i}").lower()
        doc_texto.append(texto)
        palavras_chave = ['python', 'inglês']

    return render(request, 'vcode_test/index.html', {'texto': texto,
                                                     'palavras_chave': palavras_chave,
                                                     'result': result, 'doc_texto': doc_texto,
                                                     })
