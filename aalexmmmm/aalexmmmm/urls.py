from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from aalexmmmm import settings
from doramas.views import *
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('', include('doramas.urls')),
]

if settings.DEBUG:  # Настройка для поля ImageField модели Doramas
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = page_not_found  # Обработка исключений


