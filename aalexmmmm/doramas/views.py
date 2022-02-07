from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *


menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

def index(request):  # Функция представления для главной страницы.
    posts = Doramas.objects.all()
    return render(request, 'doramas/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})

def about(request):  # Функция представления для страницы О сайте.
    return render(request, 'doramas/about.html', {'menu': menu, 'title': 'О сайте'})

# def categories(request, cat):
#     return HttpResponse(f"<h1>Статьи по категориям</h1>{cat}</p>")
#
# def archive(request, year):
#     if (int(year) > 2020):
#         return redirect('home', permanent=True)  # Код для 301 редиректа - перенаправление на главную страницу
#     return HttpResponse(f"<h1>Архив по годам</h1>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')  # Функция для обработки исключений
