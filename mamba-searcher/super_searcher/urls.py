from django.urls import path
from . import views, homeService, rankingService, emailService

urlpatterns = [
        path('', views.home, name='home'),
        path('about/', views.about, name='about'),
        path('search/', views.search, name='search'),
        path('synonyms/', views.synonyms, name='synonyms'),
        path('personalize/', views.personalize, name='personalize'),

        path('upload/', homeService.upload_files, name='upload'),
        path('delete_files/', homeService.delete_files, name='delete_files'),

        path('ranking/', rankingService.ranking, name='ranking'),
        path('ranking_synonyms/', rankingService.ranking_synonyms, name='ranking_synonyms'),

        path('email_input/', emailService.email_input, name='email_input'),
        path('email_response/', emailService.email_response, name='email_response'),
]
