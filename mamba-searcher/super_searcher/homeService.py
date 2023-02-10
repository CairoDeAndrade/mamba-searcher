from django.shortcuts import render, redirect
from django.contrib import messages
from .models import File
import os


def delete_files(request):
    dirPath = r"media/files"
    lista_arquivo = next(os.walk(dirPath))[2]

    # Deleting files
    for i in lista_arquivo:
        os.remove(f'media/files/{i}')
    messages.success(request, 'Os arquivos foram deletados com sucesso!')

    return redirect('home')


def upload_files(request):
    if request.method == 'POST':
        files = request.FILES.getlist('files')

        for f in files:
            File(file=f).save()

        messages.add_message(request, messages.SUCCESS, 'Os arquivos foram enviados com sucesso!')

    return redirect('home')
