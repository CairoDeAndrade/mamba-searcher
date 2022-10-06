from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.mamba, name='mamba'),
    path('upload/', views.upload, name='upload'),
    path('send_files/', views.send_files, name='send_files'),
    path('sinonimos/', views.sinonimos, name='sinonimos'),
    path('sinonimos_results/', views.sinonimos_results, name='sinonimos_results'),
    path('email/', views.email, name='email'),
    path('email_request/', views.email_request, name='email_request'),
    ]
