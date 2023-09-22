# определяет функции, которые получают запросы пользователей,
# обрабатывают их и возвращают ответ.
# в представлениях реализованы функции обработки, которые принимают данные
# запроса пользователя в виде объекта request и генерируют некий ответ (response), который
# затем отправляется пользователю в виде НТМL-страницы.

from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect, HttpResponseBadRequest, \
    HttpResponseForbidden
from django.template.response import TemplateResponse
import datetime
from .forms import UserForm




def index(request):
    my_text = 'Изучаем формы Django'
    context = {'my_text': my_text}
    return render(request, "firstapp/index.html", context)

def about(request):
    return render(request, "firstapp/about.html")
    # return HttpResponse("<h2>0 сайте</h2>")


def contact(request):
    return render(request, "firstapp/contact.html")
    # return HttpResponseRedirect("/about")
    # return HttpResponse("<h2>Koнтaкты</h2>")


def my_form(request):
    my_form = UserForm()
    context = {"form": my_form}
    return render(request, "firstapp/my_form.html", context)

def products(request, productid=1):
    category = request.GET.get("cat", "Не задано")
    output = "<h2>Продукт № {0} Категория: {1}</h2>".format(productid, category)
    return HttpResponse(output)


def users(request, id=1, name="Max"):
    id = request.GET.get("id", "Не задано")
    name = request.GET.get("name", "Не задано")
    output = "<h2>Пользователь</h2><h3>id: {0} Имя: {1}</h3>".format(id, name)
    return HttpResponse(output)


def details(request):
    return HttpResponsePermanentRedirect("/")


def access(request, age):
    # если возраст НЕ входит в диапазон 1-110, посылаем ошибку 400
    if age not in range(1, 111):
        return HttpResponseBadRequest("Heкoppeк тныe данные")
    if age > 17:  # если возраст больше 17, то доступ разрешен
        return HttpResponse("Доступ разрешен")
    else:  # если нет, то возвращаем ошибку 403
        return HttpResponseForbidden("Доступ заблокирован: недостаточно лет")
