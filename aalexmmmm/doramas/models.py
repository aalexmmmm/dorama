from django.db import models
from django.urls import reverse


class Doramas(models.Model):  # Модель для базы данных из списка дорам
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):  # Функция для того, чтобы вместо идентификаторов выводились заголовки – поле title,
        return self.title  # при вызове Women.objects.all().

    def get_absolute_url(self):  # Здесь используется функция reverse, которая строит текущий URL-адрес каждого поста на
        return reverse('post', kwargs={'post_id': self.pk})  # основе имени маршрута post и словаря параметров kwargs.


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})