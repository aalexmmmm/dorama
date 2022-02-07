from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),  # Путь для главной страницы.
    path('about/', about, name='about'), # Путь для страницы О сайте.
]