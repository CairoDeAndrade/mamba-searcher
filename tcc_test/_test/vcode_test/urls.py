from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.mamba, name='mamba'),
    path('sinonimos/', views.sinonimos, name='sinonimos'),
    path('sinonimos_results/', views.sinonimos_results, name='sinonimos_results'),
    path('sinonimos_results/', views.sinonimos_results, name='sinonimos_results'),
    path('email_request/', views.email_request, name='email_request'),

    ]
