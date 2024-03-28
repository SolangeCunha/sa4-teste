from django.urls import path
from page_app.views import index, contato, service

urlpatterns = [
    # Cadastrar URLs aqui
    path('', index),

    path('contato/', contato),
    path('services/', service),
    
]