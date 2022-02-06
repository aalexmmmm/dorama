from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse('Страница приложения doramas.')

def categories(request, cat):
    return HttpResponse(f"<h1>Статьи по категориям</h1>{cat}</p>")

def archive(request, year):
    if (int(year) > 2020):
        return redirect('home', permanent=True)
    return HttpResponse(f"<h1>Архив по годам</h1>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')