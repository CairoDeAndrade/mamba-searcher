# Django imports
from django.http import HttpResponse
from django.shortcuts import render, redirect
# Models imports
from .models import File, FilteredFiles
# Super-searcher imports
import docx2txt
import fitz
import unicodedata
import os
from operator import itemgetter
# Synonyms search imports
from pysinonimos.sinonimos import Search
# email imports
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import shutil


# Main page
def mamba(request):
    return render(request, 'vcode_test/mamba.html')


# Functions that return variables to use
def list_files_name(request):
    # functionalities
    # dirPath = r"C:\Users\entra21\Desktop\testes"
    dirPath = r"media\files"  # Vitor
    # dirPath = r"C:\Users\cairo\OneDrive\Área de Trabalho\testes"  # cairo
    lista_arquivos = next(os.walk(dirPath))[2]

    lista_quantidade_palavras, texto, lista_final, list_files_name, list_word_qtd, real_final = [], [], [], [], [], []
    total = 0
    caminho, contained_words = '', ''
    result, list_contained_words, final_contained_words = [], [], []
    final_dict = {}
    palavras_chave = str(request.GET.get('term')).lower()
    novas_palavras = ''.join(ch for ch in unicodedata.normalize('NFKD', palavras_chave).lower()
                             if not unicodedata.combining(ch))
    novas_palavras = novas_palavras.split(",")

    for i in lista_arquivos:
        try:
            # caminho = fr"C:\Users\entra21\Desktop\testes\{i}"
            caminho = fr"media\files\{i}"  # vitor
            # caminho = fr"C:\Users\cairo\OneDrive\Área de Trabalho\testes\{i}"  # cairo
            sum = 0
            texto = docx2txt.process(caminho)
            novo_texto = ''.join(ch for ch in unicodedata.normalize('NFKD', texto).lower()
                                 if not unicodedata.combining(ch))

            total = len(novas_palavras)

            for palavra in novas_palavras:
                if palavra in novo_texto:
                    sum += 1
                    contained_words += f'{palavra}, '
                else:
                    continue

            list_contained_words.append(contained_words)
            contained_words = ''
            lista_quantidade_palavras.append(sum)

        except:
            # quantidade = []
            text = ''
            sum = 0
            with fitz.open(caminho) as doc:
                for page in doc:
                    text = page.get_text()
            new_text = ''.join(ch for ch in unicodedata.normalize('NFKD', text).lower()
                               if not unicodedata.combining(ch))

            for j in novas_palavras:
                if j in new_text:
                    sum += 1
                    contained_words += f'{j}, '
                else:
                    continue

            list_contained_words.append(contained_words)
            contained_words = ''
            lista_quantidade_palavras.append(sum)

    for arquivo, quantidade_palavras, palavras_contidas in zip(lista_arquivos, lista_quantidade_palavras,
                                                               list_contained_words):
        final_dict = {'arquivo': arquivo, 'quantidade_palavras': quantidade_palavras,
                      'palavras_contidas': palavras_contidas}

        # quantidade = [arquivo, quantidade_palavras, total]
        lista_final.append(final_dict)
        result = sorted(lista_final, key=itemgetter('quantidade_palavras'), reverse=True)

    for i in result:
        if i['quantidade_palavras'] != 0:
            list_files_name.append(i['arquivo'])
            list_word_qtd.append(i['quantidade_palavras'])
            final_contained_words.append(i['palavras_contidas'])
        else:
            pass

    for files_name, word_qtd, words in zip(list_files_name, list_word_qtd, final_contained_words):
        complete_list = [files_name, word_qtd, words]
        real_final.append(complete_list)

    # If the search input is empty
    term = request.GET.get('term')
    if not term:
        return redirect('mamba')

    return list_files_name


def total(request):
    # functionalities
    # dirPath = r"C:\Users\entra21\Desktop\testes"
    dirPath = r"media\files"  # Vitor
    # dirPath = r"C:\Users\cairo\OneDrive\Área de Trabalho\testes"  # cairo
    lista_arquivos = next(os.walk(dirPath))[2]

    lista_quantidade_palavras, texto, lista_final, list_files_name, list_word_qtd, real_final = [], [], [], [], [], []
    total = 0
    caminho, contained_words = '', ''
    result, list_contained_words, final_contained_words = [], [], []
    final_dict = {}
    palavras_chave = str(request.GET.get('term')).lower()
    novas_palavras = ''.join(ch for ch in unicodedata.normalize('NFKD', palavras_chave).lower()
                             if not unicodedata.combining(ch))
    novas_palavras = novas_palavras.split(",")

    for i in lista_arquivos:
        try:
            # caminho = fr"C:\Users\entra21\Desktop\testes\{i}"
            caminho = fr"media\files\{i}"  # vitor
            # caminho = fr"C:\Users\cairo\OneDrive\Área de Trabalho\testes\{i}"  # cairo
            sum = 0
            texto = docx2txt.process(caminho)
            novo_texto = ''.join(ch for ch in unicodedata.normalize('NFKD', texto).lower()
                                 if not unicodedata.combining(ch))

            total = len(novas_palavras)

            for palavra in novas_palavras:
                if palavra in novo_texto:
                    sum += 1
                    contained_words += f'{palavra}, '
                else:
                    continue

            list_contained_words.append(contained_words)
            contained_words = ''
            lista_quantidade_palavras.append(sum)

        except:
            # quantidade = []
            text = ''
            sum = 0
            with fitz.open(caminho) as doc:
                for page in doc:
                    text = page.get_text()
            new_text = ''.join(ch for ch in unicodedata.normalize('NFKD', text).lower()
                               if not unicodedata.combining(ch))

            for j in novas_palavras:
                if j in new_text:
                    sum += 1
                    contained_words += f'{j}, '
                else:
                    continue

            list_contained_words.append(contained_words)
            contained_words = ''
            lista_quantidade_palavras.append(sum)

    for arquivo, quantidade_palavras, palavras_contidas in zip(lista_arquivos, lista_quantidade_palavras,
                                                               list_contained_words):
        final_dict = {'arquivo': arquivo, 'quantidade_palavras': quantidade_palavras,
                      'palavras_contidas': palavras_contidas}

        # quantidade = [arquivo, quantidade_palavras, total]
        lista_final.append(final_dict)
        result = sorted(lista_final, key=itemgetter('quantidade_palavras'), reverse=True)

    for i in result:
        list_files_name.append(i['arquivo'])
        list_word_qtd.append(i['quantidade_palavras'])
        final_contained_words.append(i['palavras_contidas'])

    for files_name, word_qtd, words in zip(list_files_name, list_word_qtd, final_contained_words):
        complete_list = [files_name, word_qtd, words]
        real_final.append(complete_list)

    # If the search input is empty
    term = request.GET.get('term')
    if not term:
        return redirect('mamba')

    return total


def real_final(request):
    # functionalities
    # dirPath = r"C:\Users\entra21\Desktop\testes"
    dirPath = r"media\files"  # Vitor
    # dirPath = r"C:\Users\cairo\OneDrive\Área de Trabalho\testes"  # cairo
    lista_arquivos = next(os.walk(dirPath))[2]

    lista_quantidade_palavras, texto, lista_final, list_files_name, list_word_qtd, real_final = [], [], [], [], [], []
    total = 0
    caminho, contained_words = '', ''
    result, list_contained_words, final_contained_words = [], [], []
    final_dict = {}
    palavras_chave = str(request.GET.get('term')).lower()
    novas_palavras = ''.join(ch for ch in unicodedata.normalize('NFKD', palavras_chave).lower()
                             if not unicodedata.combining(ch))
    novas_palavras = novas_palavras.split(",")

    for i in lista_arquivos:
        try:
            # caminho = fr"C:\Users\entra21\Desktop\testes\{i}"
            caminho = fr"media\files\{i}"  # vitor
            # caminho = fr"C:\Users\cairo\OneDrive\Área de Trabalho\testes\{i}"  # cairo
            sum = 0
            texto = docx2txt.process(caminho)
            novo_texto = ''.join(ch for ch in unicodedata.normalize('NFKD', texto).lower()
                                 if not unicodedata.combining(ch))

            total = len(novas_palavras)

            for palavra in novas_palavras:
                if palavra in novo_texto:
                    sum += 1
                    contained_words += f'{palavra}, '
                else:
                    continue

            list_contained_words.append(contained_words)
            contained_words = ''
            lista_quantidade_palavras.append(sum)

        except:
            # quantidade = []
            text = ''
            sum = 0
            with fitz.open(caminho) as doc:
                for page in doc:
                    text = page.get_text()
            new_text = ''.join(ch for ch in unicodedata.normalize('NFKD', text).lower()
                               if not unicodedata.combining(ch))

            for j in novas_palavras:
                if j in new_text:
                    sum += 1
                    contained_words += f'{j}, '
                else:
                    continue

            list_contained_words.append(contained_words)
            contained_words = ''
            lista_quantidade_palavras.append(sum)

    for arquivo, quantidade_palavras, palavras_contidas in zip(lista_arquivos, lista_quantidade_palavras,
                                                               list_contained_words):
        final_dict = {'arquivo': arquivo, 'quantidade_palavras': quantidade_palavras,
                      'palavras_contidas': palavras_contidas}

        # quantidade = [arquivo, quantidade_palavras, total]
        lista_final.append(final_dict)
        result = sorted(lista_final, key=itemgetter('quantidade_palavras'), reverse=True)

    for i in result:
        list_files_name.append(i['arquivo'])
        list_word_qtd.append(i['quantidade_palavras'])
        final_contained_words.append(i['palavras_contidas'])

    for files_name, word_qtd, words in zip(list_files_name, list_word_qtd, final_contained_words):
        complete_list = [files_name, word_qtd, words]
        real_final.append(complete_list)

    # If the search input is empty
    term = request.GET.get('term')
    if not term:
        return redirect('mamba')

    return real_final


# Search function
def index(request):
    real_final_list = real_final(request)
    total_list = total(request)
    files_name_list = list_files_name(request)

    # Saving the filtered files in the database
    files = File.objects.all()

    for f in files:
        FilteredFiles(filtered_files=f).save()

    return render(request, 'vcode_test/index.html', {'real_final_list': real_final_list,
                                                     'total_list': total_list,
                                                     'files_name_list': files_name_list})


# Synonyms search functions
def sinonimos(request):
    return render(request, 'vcode_test/sinonimos.html')


def sinonimos_results(request):
    # If the search input is empty
    term = request.GET.get('term')
    if not term:
        return redirect('sinonimos')

    # functionalities
    # dirPath = r"C:\Users\entra21\Desktop\testes"
    dirPath = r"media\files"  # vitor
    # dirPath = r"C:\Users\cairo\OneDrive\Área de Trabalho\testes"  # cairo
    lista_arquivos = next(os.walk(dirPath))[2]

    lista_quantidade_palavras, texto, lista_final, list_files_name, list_word_qtd, real_final = [], [], [], [], [], []
    total = 0
    caminho, contained_words, no_synonyms = '', '', ''
    result, list_contained_words, final_contained_words = [], [], []
    final_dict = {}

    # Using the synonyms to search
    palavras_chave = str(request.GET.get('term')).lower()
    search_word = ''.join(ch for ch in unicodedata.normalize('NFKD', palavras_chave).lower()
                          if not unicodedata.combining(ch))
    synonym_word = Search(f'{search_word}')
    synonym_results = synonym_word.synonyms()

    # Checking if there is not a synonym
    if synonym_results == 404:
        novas_palavras = [search_word]
        no_synonyms = "Não há sinônimos para esta palavra"
    else:
        novas_palavras = synonym_results
        novas_palavras.append(search_word)

    # Main code
    for i in lista_arquivos:
        try:
            caminho = fr"media\files\{i}"  # vitor
            # caminho = fr"C:\Users\entra21\Desktop\testes\{i}"
            # caminho = fr"C:\Users\cairo\OneDrive\Área de Trabalho\testes\{i}"  # cairo
            sum = 0
            texto = docx2txt.process(caminho)
            novo_texto = ''.join(ch for ch in unicodedata.normalize('NFKD', texto).lower()
                                 if not unicodedata.combining(ch))

            total = len(novas_palavras)

            for palavra in novas_palavras:
                if palavra in novo_texto:
                    sum += 1
                    contained_words += f'{palavra}, '
                else:
                    continue

            list_contained_words.append(contained_words)
            contained_words = ''
            lista_quantidade_palavras.append(sum)

        except:
            # quantidade = []
            text = ''
            sum = 0
            with fitz.open(caminho) as pdf:
                for page in pdf:
                    text = page.get_text()
            new_text = ''.join(ch for ch in unicodedata.normalize('NFKD', text).lower()
                               if not unicodedata.combining(ch))

            for j in novas_palavras:
                if j in new_text:
                    sum += 1
                    contained_words += f'{j}, '
                else:
                    continue

            list_contained_words.append(contained_words)
            contained_words = ''
            lista_quantidade_palavras.append(sum)

    for arquivo, quantidade_palavras, palavras_contidas in zip(lista_arquivos, lista_quantidade_palavras,
                                                               list_contained_words):
        final_dict = {'arquivo': arquivo, 'quantidade_palavras': quantidade_palavras,
                      'palavras_contidas': palavras_contidas}

        # quantidade = [arquivo, quantidade_palavras, total]
        lista_final.append(final_dict)
        result = sorted(lista_final, key=itemgetter('quantidade_palavras'), reverse=True)

    for i in result:
        list_files_name.append(i['arquivo'])
        list_word_qtd.append(i['quantidade_palavras'])
        final_contained_words.append(i['palavras_contidas'])

    for files_name, word_qtd, words in zip(list_files_name, list_word_qtd, final_contained_words):
        complete_list = [files_name, word_qtd, words]
        real_final.append(complete_list)

    return render(request, 'vcode_test/sinonimos_results.html', {'real_final': real_final, 'total': total,
                                                                 'synonym_results': synonym_results,
                                                                 'no_synonyms': no_synonyms, })


# Files upload
def upload(request):
    return render(request, 'vcode_test/upload.html')


def send_files(request):
    if request.method == 'POST':
        files = request.FILES.getlist('files')

        # storing the files in the DataBase
        for f in files:
            File(file=f).save()

        return HttpResponse("The files were uploaded successfully!")


# Receiving the filtered files
def email(request):
    files_name_list = list_files_name(request)

    return render(request, 'vcode_test/email.html', {
        'files_name_list': files_name_list,
    })


def email_request(request):
    dirPath = r"media/filtered_files"
    lista_arquivos = next(os.walk(dirPath))[2]

    for i in lista_arquivos:
        shutil.move(f'media/filtered_files/{i}',
                    f'media/filtered_files/{i}'.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o")
                    .replace("ú", "u").replace("ã", "a").replace("ç", "c").replace(" ", "_")
                    .replace(",", "").replace("õ", "o"))

    fromaddr = "mamba.python.entra21@gmail.com"
    toaddr = str(request.GET.get('term').replace('%40', '@'))

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Emails Filtrados"
    body = "Aqui estão seus emails filtrados"
    msg.attach(MIMEText(body, 'plain'))

    for i in lista_arquivos:
        filename = i
        attachment = open(f"media/filtered_files/{i}", "rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload(attachment.read())
        encoders.encode_base64(p)

        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(p)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, "pzlyubevjrwgyobq")
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()

    return render(request, 'vcode_test/email_request.html', {'list_files_name': list_files_name})
