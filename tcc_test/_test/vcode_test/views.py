from django.shortcuts import render, redirect
import docx2txt
import fitz
import unicodedata
import os
from operator import itemgetter
from pysinonimos.sinonimos import Search
from .models import File
from .forms import FileForm
# email imports
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import shutil



def mamba(request):
    if request.method != 'POST':
        form = FileForm()
        return render(request, 'vcode_test/mamba.html', {'form': form})

    form = FileForm(request.POST, request.FILES)

    if not form.is_valid():
        form = FileForm(request.POST)
        return render(request, 'vcode_test/mamba.html', {'form': form})

    form.save()
    return redirect('mamba')


def lista_final(request):
    # functionalities
    # dirPath = r"C:\Users\entra21\Desktop\testes"
    dirPath = r"media"  # Vitor
    # dirPath = r"C:\Users\cairo\OneDrive\Área de Trabalho\testes"  # cairo
    lista_arquivos = next(os.walk(dirPath))[2]
    list_files_name = []
    lista_quantidade_palavras, texto, lista_final, list_word_qtd, real_final = [], [], [], [], []
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
            caminho = fr"media\{i}"  # vitor
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
        if i['quantidade_palavras'] == 0:
            pass
        else:
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

def totalizar(request):
    # functionalities
    # dirPath = r"C:\Users\entra21\Desktop\testes"
    dirPath = r"media"  # Vitor
    # dirPath = r"C:\Users\cairo\OneDrive\Área de Trabalho\testes"  # cairo
    lista_arquivos = next(os.walk(dirPath))[2]
    list_files_name = []
    lista_quantidade_palavras, texto, lista_final, list_word_qtd, real_final = [], [], [], [], []
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
            caminho = fr"media\{i}"  # vitor
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
        if i['quantidade_palavras'] == 0:
            pass
        else:
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

def lista_nomes(request):
    # functionalities
    # dirPath = r"C:\Users\entra21\Desktop\testes"
    dirPath = r"media"  # Vitor
    # dirPath = r"C:\Users\cairo\OneDrive\Área de Trabalho\testes"  # cairo
    lista_arquivos = next(os.walk(dirPath))[2]
    list_files_name = []
    lista_quantidade_palavras, texto, lista_final, list_word_qtd, real_final = [], [], [], [], []
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
            caminho = fr"media\{i}"  # vitor
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
        if i['quantidade_palavras'] == 0:
            pass
        else:
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

    return list_files_name




def index(request):
    real_final = lista_final(request)
    total = totalizar(request)
    list_files_name = lista_nomes(request)
    return render(request, 'vcode_test/index.html', {'real_final': real_final, 'total': total,'list_files_name': list_files_name})


def sinonimos(request):
    return render(request, 'vcode_test/sinonimos.html')


def sinonimos_results(request):
    # If the search input is empty
    term = request.GET.get('term')
    if not term:
        return redirect('sinonimos')

    # functionalities
    # dirPath = r"C:\Users\entra21\Desktop\testes"
    dirPath = r"media"  # vitor
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
            caminho = fr"media\{i}"  # vitor
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


def email_request(request):
    list_files_name = lista_nomes(request)
    for i in list_files_name:
        shutil.move(f'media/{i}',
                    f'media/{i}'.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú",
                                                                                                                 "u").replace(
                        "ã", "a").replace("ç", "c").replace(" ", "_").replace(",", "").replace("õ", "o"))

    fromaddr = "mamba.python.entra21@gmail.com"
    toaddr = str(request.GET.get('term').replace('%40', '@'))

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Emails Filtrados"
    body = "Aqui estão seus email filtrados"
    msg.attach(MIMEText(body, 'plain'))

    for i in list_files_name:
        filename = i
        attachment = open(f"media/{i}", "rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
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
