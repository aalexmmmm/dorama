from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),  # Путь для главной страницы.
    path('about/', about, name='about'),  # Путь для страницы О сайте.
    path('addpage/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', show_post, name='post'),  # url-адреса для каждого из постов
    path('category/<slug:cat_slug>/', show_category, name='category'),
]