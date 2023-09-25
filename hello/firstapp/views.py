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
    if request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            name = user_form.cleaned_data.get("name")  # Get the cleaned data for 'name' field
            age = user_form.cleaned_data.get("age")  # Get the cleaned data for 'age' field
            output = "<h2>Пользователь</h2><h3>Имя - {}, Возраст - {}</h3>".format(name, age)
            return HttpResponse(output)
    else:
        user_form = UserForm()
    return render(request, "firstapp/my_form.html", {"form": user_form})

# def my_form(request):
#     if request.method == 'POST':
#         userform = UserForm(request.POST)  # Если выполняется РОSТ-запрос, то вначале происходит заполнение формы пришедшими данными:
#         if userform.is_valid(): #Потом с помощью метода is valid () проверяется их корректность:
#             name = userform.cleaned_data["name"] #Если данные введены корректно, то через объект cleaned data в переменную name заносимвведенное пользователем значение и формируем ответную страницу с сообщением,что данные корректны:
#             return HttpResponse("<h2>Имя введено корректно - {}</h2>".format(name))
#         else:
#             return HttpResponse("Ошибка ввода данных") #Если данные введены некорректно, то формируем ответную страницу с сообщением обошибке:
#     else:
#         userform = UserForm() #Если РОSТ-запрос отсутствует, то просто происходит вызов пользовательской формы:
#         return render(request, "firstapp/my_form.html", {"form": userform})


# def my_form(request):
#     my_form = UserForm()#field_order=["age", "name"]  вставив это в скобки поменяет порядок отображения полей
#     context = {"form": my_form}
#     return render(request, "firstapp/my_form.html", context)
#

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
