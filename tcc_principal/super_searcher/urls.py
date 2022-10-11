from django.urls import path
from . import views

urlpatterns = [
        path('', views.home, name='home'),
        path('upload/', views.upload, name='upload'),
        path('search/', views.search, name='search'),
        path('ranking/', views.ranking, name='ranking'),
        path('about/', views.about, name='about'),
        path('synonyms/', views.synonyms, name='synonyms'),
        path('ranking_synonyms/', views.ranking_synonyms, name='ranking_synonyms'),
        path('email_input/', views.email_input, name='email_input'),
        path('email_response/', views.email_response, name='email_response'),
]
