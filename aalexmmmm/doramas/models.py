from django.db import models
from django.urls import reverse


class Doramas(models.Model):  # Модель для базы данных из списка дорам
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name="Категории")

    def __str__(self):  # Функция для того, чтобы вместо идентификаторов выводились заголовки – поле title,
        return self.title  # при вызове Women.objects.all().

    def get_absolute_url(self):  # Здесь используется функция reverse, которая строит текущий URL-адрес каждого поста на
        return reverse('post', kwargs={'post_id': self.pk})  # основе имени маршрута post и словаря параметров kwargs.

    class Meta:
        verbose_name = 'Дорамы'
        verbose_name_plural = 'Дорамы'
        ordering = ['time_create', 'title']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
        ordering = ['id']   # Порядок сортировки