from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *


menu = [{'title': "О сайте", 'url_name': 'about'},  # словарь для меню шапки главной страницы
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]


def index(request):  # Функция представления для главной страницы.
    posts = Doramas.objects.all()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }

    return render(request, 'doramas/index.html', context=context)


def about(request):  # Функция представления для страницы О сайте.
    return render(request, 'doramas/about.html', {'menu': menu, 'title': 'О сайте'})


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def show_post(request, post_id):  # Функция для страниц с каждым из постов
    return HttpResponse(f"Отображение статьи с id = {post_id}")


def show_category(request, cat_id):
    posts = Doramas.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': cat_id,
    }

    return render(request, 'doramas/index.html', context=context)


def page_not_found(request, exception):  # Функция для обработки исключений
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
