from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('mamba/', views.mamba, name='mamba'),
    # path('search/', views.search, name='search'),
    ]
