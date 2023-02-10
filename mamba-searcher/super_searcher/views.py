from django.shortcuts import render
from . import searchService


# Rendering pages
def home(request):
    return render(request, 'super_searcher/home.html')


def search(request):
    searchService.remove_filtered()

    return render(request, 'super_searcher/search.html')


def synonyms(request):
    searchService.remove_filtered()
    return render(request, 'super_searcher/synonyms.html')


def about(request):
    return render(request, 'super_searcher/about.html')


def personalize(request):
    return render(request, 'super_searcher/personalize.html')
