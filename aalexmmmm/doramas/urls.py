from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', DoramasHome.as_view(), name='home'),  # Путь для главной страницы.
    path('about/', about, name='about'),  # Путь для страницы О сайте.
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),  # url-адреса для каждого из постов
    path('category/<slug:cat_slug>/', DoramasCategory.as_view(), name='category'),
]