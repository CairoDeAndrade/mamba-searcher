from django.shortcuts import render, redirect
from django.contrib import messages
from .. import views
from . import searchService
import docx2txt
import fitz
import unicodedata
import os
from operator import itemgetter
from pysinonimos.sinonimos import Search
import shutil


def ranking(request):
    term = request.GET.get('term')
    if not term:
        messages.error(request, 'O campo de pesquisa não pode estar vazio!')
        return redirect('search')

    views.remove_filtered()

    # Using the variables to the search
    real_final_list = searchService.real_final(request)
    total_list = searchService.total(request)
    files_name_list = searchService.list_files(request)

    # If there is no keyword in the files
    words = False
    for i in real_final_list:
        if i[1] != 0:
            words = True

    if not words:
        messages.warning(request, 'Não há currículos com esta(s) palavra(s)')

    # Saving the filtered files in the database
    dirPath = r"media\files"
    lista_arquivos = next(os.walk(dirPath))[2]

    for aqur in lista_arquivos:
        for filtered in files_name_list:
            if aqur == filtered:
                shutil.copy2(f'media/files/{aqur}', f'media/filtered_files/{aqur}')

    return render(request, 'super_searcher/ranking.html', {'real_final_list': real_final_list,
                                                           'total_list': total_list,
                                                           'files_name_list': files_name_list})


def ranking_synonyms(request):
    term = request.GET.get('term')
    if not term:
        messages.error(request, 'O campo de pesquisa não pode estar vazio!')
        return redirect('synonyms')

    views.remove_filtered()

    # functionalities
    dirPath = r"media\files"
    lista_arquivos = next(os.walk(dirPath))[2]

    lista_quantidade_palavras, texto, lista_final, list_files_name, list_word_qtd, real_final = [], [], [], [], [], []
    total = 0
    caminho, contained_words, no_synonyms = '', '', ''
    result, list_contained_words, final_contained_words = [], [], []

    # Using the synonyms to search
    try:
        palavras_chave = str(request.GET.get('term')).lower()
        search_word = ''.join(ch for ch in unicodedata.normalize('NFKD', palavras_chave).lower()
                              if not unicodedata.combining(ch))
        synonym_word = Search(f'{search_word}')
        synonym_results = synonym_word.synonyms()
    except:
        messages.warning(request, 'Erro de conexão com internet!')
        return redirect('ranking_synonyms')

    # Checking if there is not a synonym
    if synonym_results == 404:
        novas_palavras = [search_word]
        messages.add_message(request, messages.WARNING, 'Não há sinônimos para esta palavra!')
    else:
        novas_palavras = synonym_results
        novas_palavras.append(search_word)

    # Main code
    for i in lista_arquivos:
        try:
            caminho = fr"media\files\{i}"
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

        lista_final.append(final_dict)
        result = sorted(lista_final, key=itemgetter('quantidade_palavras'), reverse=True)

    for i in result:
        list_files_name.append(i['arquivo'])
        list_word_qtd.append(i['quantidade_palavras'])
        final_contained_words.append(i['palavras_contidas'])

    for files_name, word_qtd, words in zip(list_files_name, list_word_qtd, final_contained_words):
        complete_list = [files_name, word_qtd, words]
        real_final.append(complete_list)

    # Saving the filtered files in the database
    files_list = searchService.list_files(request)
    for aqur in lista_arquivos:
        for filtered in files_list:
            if aqur == filtered:
                shutil.copy2(f'media/files/{aqur}', f'media/filtered_files/{aqur}')

    return render(request, 'super_searcher/ranking_synonyms.html', {'real_final': real_final, 'total': total,
                                                                    'synonym_results': synonym_results,
                                                                    'no_synonyms': no_synonyms, })