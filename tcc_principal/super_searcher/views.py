# Django imports
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
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


def home(request):
    return render(request, 'super_searcher/home.html')


# upload the files in the database
def upload(request):
    if request.method == 'POST':
        files = request.FILES.getlist('files')

        # storing the files in the DataBase
        for f in files:
            File(file=f).save()
            messages.add_message(request, messages.SUCCESS, 'Os arquivos foram enviados com sucesso!')

    return redirect('home')


def search(request):
    return render(request, 'super_searcher/search.html')


def about(request):
    return render(request, 'super_searcher/about.html')


def ranking(request):
    return render(request, 'super_searcher/ranking.html')
