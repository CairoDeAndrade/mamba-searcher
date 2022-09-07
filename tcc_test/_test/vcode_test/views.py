from django.shortcuts import render
import docx2txt
import os


def index(request):
    dirPath = r"C:\Users\cairo\OneDrive\Área de Trabalho\tcc_test"
    result = next(os.walk(dirPath))[2]

    texto = []
    palavras = []
    for i in result:
        texto = docx2txt.process(fr"C:\Users\cairo\OneDrive\Área de Trabalho\tcc_test\{i}").lower()
        palavras = ['python', 'inglês']

    return render(request, 'vcode_test/index.html', {'texto': texto,
                                                     'palavras': palavras,
                                                     'result': result})
