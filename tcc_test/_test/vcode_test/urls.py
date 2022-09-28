from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.mamba, name='mamba'),
    path('sinonimos/', views.sinonimos, name='sinonimos'),
    ]
