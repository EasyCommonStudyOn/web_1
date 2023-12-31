from django.urls import path
from django.urls import re_path
# Далее приведены некоторые базовые элементы регулярных
# выражений, которые пригодны для определения адресов URL:
# □ ^ - начало адреса;
# □ $ - конец адреса;
# □ + - один и более символов;
# □ ? - ноль или один символ;
# □ {n} - п символов;
# □ {n, m} - от n до m символов;
# □ . - любой символ;
# □ \d+ - одна или несколько цифр;
# □ \D+ - одна или несколько НЕ цифр;
# □ \w+ - один или несколько буквенных символов.

from . import views
from django.views.generic import TemplateView

urlpatterns = [
    # path('about/', TemplateView.as_view(template_name="firstapp/about.html")),
    # path('contact/', TemplateView.as_view(template_name="firstapp/contact.html", extra_context={"work": "Разработка программных продуктов"})),
    path('contact/', views.contact, name="contact"),  # имя этой ссылка для использования в шаблонах
    path('about/', views.about, name="about"),
    path('', views.index, name="index"),
    path('my_form/', views.my_form, name='my_form'),
    path('my_form/edit_form/<int:id>/', views.edit_form, name='edit_form'),
    path('my_form/delete/<int:id>/', views.delete, name='delete'),
    path('form_up_img/', views.form_up_img, name='form_up_img'),
    path('form_up_img/delete_img/<int:id>', views.delete_img),
    path('form_up_pdf/', views.form_up_pdf, name='form_up_pdf'),
    path('form_up_pdf/delete_pdf/<int:id>/', views.delete_pdf),
    path('form_up_video/', views.form_up_video, name='form_up_video'),
    path('form_up_video/delete_video/<int:id>/', views.delete_video),
    path('form_up_audio/', views.form_up_audio, name='form_up_audio'),
    path('form_up_audio/delete_audio/<int:id>', views.form_up_audio),
    # re_path(r'^about', views.about),
    # re_path(r'^contact', views.contact),
    # re_path(r'^products/(?P<productid>\d+)/$', views.products),
    path('products/<int:productid>/', views.products),
    path('products/', views.products),
    # re_path(r'^products/$', views.products),
    # re_path(r'^users/(?P<id>\d+)/(?P<name>\D+)/$', views.users),
    path('users/<int:id>/<str:name>/', views.users),
    path('users/', views.users),
    path('details/', views.details),
    path('access/<int:age>', views.access),

]
