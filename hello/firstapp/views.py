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


def index(request):
    return render(request, "firstapp/index.html")


# def index(request):
#     header = "Фильтры в шаблонах"
#     value_num = 2
#     value_date = datetime.date
#     value_time = datetime.time
#     value_title = "это пример использования фильтров"
#     value_upper = "это строка в верхнем регистре"
#     data = {
#         "header": header,
#         "value_num": value_num,
#         "value_date": value_date,
#         "value_time": value_time,
#         "value_title": value_title,
#         "value_upper": value_upper,
#     }
#     return TemplateResponse(request, "firstapp/index_app1.html", data)

# header = "Разветвления в шаблонах"
# num = 4
# var1 = "Это nервая ветка в инструкции if"
# var2 = "Это вторая ветка в инструкции if"
# data = {"header": header, "num": num, "varl": var1, "var2": var2}
# return TemplateResponse(request, "firstapp/index_app1.html", data)

# header = "Иностранные языки"  # символьная переменная
# list_langs = ["Английский", "Немецкий", "Испанский",
#               "Французский", "Итальянский"]  # список
# data = {"header": header, "list_langs": list_langs}
# return TemplateResponse(request, "firstapp/index_app1.html", data)

# header = "Персональные данные"  # символьная переменная
# langs = ["Английский", "Немецкий", "Испанский"]  # список
# user = {"name": "Максим, ", "age": 30}  # словарь
# addr = ("Виноградная", 23, 45)  # кортеж
# data = {"header": header, "langs": langs, "user": user, "address": addr}
# return render(request, "index.html", context=data)


# def index(request):
#    header = "Персональные данные"
#    langs = ["Английский", "Немецкий", "Испанский"]
#    user = {"пате": "Максим,", "age": 30}
#    addr = ("Виноградная", 23, 45)
#    data = {"header": header, "langs": langs, "user": user, "address": addr}
#    return TemplateResponse(request, "index.html", data)


# data = {
#     "header": "Передача параметров в шаблон Django",
#     "message": "Загружен шаблон templates/firstapp/index_app1.html"
# }
# return render(request, "firstapp/index_app1.html", context=data)

# def index(request):
#     return HttpResponse("<h2>Главная</h2>")


def about(request):
    return render(request, "firstapp/about.html")
    # return HttpResponse("<h2>0 сайте</h2>")


def contact(request):
    return render(request, "firstapp/contact.html")
    # return HttpResponseRedirect("/about")
    # return HttpResponse("<h2>Koнтaкты</h2>")


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
