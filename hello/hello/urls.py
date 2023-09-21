# это URL-декларации текущего проекта Django, или, иначе говоря, это
# «диспетчер URL-aдpecoв» Django-пpoeктa;

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('firstapp.urls')),
    path('admin/', admin.site.urls),
]
