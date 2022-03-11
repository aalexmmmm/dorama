from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
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
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect('home')

    else:
        form = AddPostForm()
    return render(request, 'doramas/addpage.html', {'menu': menu, 'title': 'Добавление статьи', 'form': form})


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def show_post(request, post_slug):  # Функция для страниц с каждым из постов
    post = get_object_or_404(Doramas, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'doramas/post.html', context=context)


def show_category(request, cat_slug):
    cat = get_object_or_404(Category, slug=cat_slug)
    posts = Doramas.objects.filter(cat_id=cat.id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'title': cat.name,
        'cat_selected': cat.id,
    }

    return render(request, 'doramas/index.html', context=context)


def page_not_found(request, exception):  # Функция для обработки исключений
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
