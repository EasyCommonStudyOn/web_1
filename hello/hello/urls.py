# это URL-декларации текущего проекта Django, или, иначе говоря, это
# «диспетчер URL-aдpecoв» Django-пpoeктa;

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('firstapp.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #Здесь задана инструкция if settings. DEBUG, т. е. подключение этих адресов будет происходить только тогда, когда выполняется разработка и отладка программного кода. Это означает, что указанные URL-aдpeca будут использоваться только на этапе создания сайта на компьютере разработчика.
