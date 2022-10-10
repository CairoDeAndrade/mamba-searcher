from django.shortcuts import render


def home(request):
    return render(request, 'super_searcher/home.html')


def search(request):
    return render(request, 'super_searcher/search.html')
