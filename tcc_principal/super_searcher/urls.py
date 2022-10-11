from django.urls import path
from . import views

urlpatterns = [
        path('', views.home, name='home'),
        path('upload/', views.upload, name='upload'),
        path('search/', views.search, name='search'),
        path('ranking/', views.ranking, name='ranking'),
        path('about/', views.about, name='about'),
]
