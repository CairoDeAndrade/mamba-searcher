from django.urls import path
from . import views

urlpatterns = [
        path('', views.home, name='home'),
        path('search/', views.search, name='search'),
        path('about/', views.about, name='about'),
        path('ranking/', views.ranking, name='ranking'),
        path('upload/', views.upload, name='upload'),
]
