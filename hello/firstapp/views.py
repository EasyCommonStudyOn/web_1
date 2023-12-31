# определяет функции, которые получают запросы пользователей,
# обрабатывают их и возвращают ответ.
# в представлениях реализованы функции обработки, которые принимают данные
# запроса пользователя в виде объекта request и генерируют некий ответ (response), который
# затем отправляется пользователю в виде НТМL-страницы.

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect, HttpResponseBadRequest, \
    HttpResponseForbidden, HttpResponseNotFound
from django.template.response import TemplateResponse
import datetime
from .forms import UserForm
from .models import Person
from .forms import ImageForm
from .models import Image
from .forms import FileForm
from .models import File
from .models import VideoFile
from .forms import VideoForm
from .models import AudioFile
from .forms import AudioForm


def form_up_img(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    my_text = 'Загруженные изображения'
    my_img = Image.obj_img.all()
    form = ImageForm()
    context = {'my_text': my_text, "my_img": my_img, "form": form}
    return render(request, 'firstapp/form_up_img.html', context)


def delete_img(request, id):
    try:
        img = Image.obj_img.get(id=id)
        img.delete()
        return redirect('form_up_img')
    except Image.DoesNotExist:
        return HttpResponseNotFound("<h2>Объект не найден</h2>")


def form_up_pdf(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            my_text = 'Загруженные файлы'
            form = FileForm()
            file_obj = File.objects.all()
            context = {'my_text': my_text, 'file_obj': file_obj, 'form': form}
            return render(request, 'firstapp/form_up_pdf.html', context)
    else:
        form = FileForm()
    return render(request, 'firstapp/form_up_pdf.html', {'form': form})


def delete_pdf(request, id):
    try:
        pdf = File.objects.get(id=id)
        pdf.delete()
        return redirect('form_up_pdf')
    except File.DoesNotExist:
        return HttpResponseNotFound('<h2>Объект не найден</h2>')


'''
def form_up_video(request)
В этой функции
проверяется условие, поступил ли запрос от пользователя на загрузку видеофайла
(if. request.method == 'POST'). Если такой запрос поступил, то на основе класса VideoForm
создается объект foпn, который получает запрос от пользователя на сохранение данных
о видеофайле (request.POsт), и сам загружаемый файл (request.FILES). Если форма не содержит
ошибок, то вьmолняется сохранение введенных пользователем данных
(form. save). После этого происходит обновление формы для загрузки видеофайлов.
Если форма вызывается первый раз, т. е. поступил запрос GET, то создаются:
□ текстовая переменная my text;
□ объект foпn, который создается на основе класса victeoForm (т. е. сама форма);
□ объект file_obj, который принимает из БД все сведения о загруженных файлах.
Затем создается объект context, в который в виде словаря передаются объекты: my_text,
file_obj, form. После этого вызывается шаблон form_up_video.html, в который передаются
все данные через объект context.


'''
def form_up_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            my_text = 'Загруженные видеофайлы'
            form = VideoForm()
            file_obj = VideoFile.objects.all()
            context = {'my_text': my_text, 'file_obj': file_obj, 'form': form}
            return render(request, 'firstapp/form_up_video.html', context)
    else:
        form = VideoForm()
        file_obj = VideoFile.objects.all()
        context = {'my_text': '', 'file_obj': file_obj, 'form': form}
        return render(request, 'firstapp/form_up_video.html', context)


def delete_video(request, id):
    try:
        video = VideoFile.objects.get(id=id)  # Corrected manager name to 'objects'
        video.delete()
        return redirect('form_up_video')
    except VideoFile.DoesNotExist:  # Corrected model name to 'VideoFile'
        return HttpResponseNotFound("<h2>Объект не найден</h2>")


def form_up_audio(request):
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            my_text = 'Загруженные аудиофайлы'
            form = AudioForm()  # Reset the form for future uploads
            file_obj = AudioFile.obj_audio.all()
            context = {'my_text': my_text, "file_obj": file_obj, "form": form}
            return render(request, 'firstapp/form_up_audio.html', context)
    else:
        form = AudioForm()  # Create a new empty form
    return render(request, 'firstapp/form_up_audio.html', {'form': form})

def delete_audio(request, id):
    try:
        audio = AudioFile.obj_audio.get(id=id)
        audio.delete()
        return redirect('form_up_audio')
    except AudioFile.DoesNotExist:
        return HttpResponseNotFound("<h2>Объект не найден</h2>")



def edit_form(request, id):
    try:
        person = Person.objects.get(id=id)  # Use 'objects' instead of 'object'

        # If the user submits edited data
        if request.method == "POST":
            person.name = request.POST.get("name")
            person.age = request.POST.get("age")
            person.save()
            return redirect('my_form')  # Redirect to the 'my_form' view

        # If the user requests data for editing
        data = {"person": person}
        return render(request, "firstapp/edit_form.html", context=data)
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Объект не найден</h2>")


def delete(request, id):
    try:
        person = Person.object.get(id=id)
        person.delete()
        return redirect('my_form')  # Redirect to the 'my_form' view
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Объект не найден</h2>")


def index(request):
    my_text = 'Изучаем модели Django'
    people_kol = Person.objects.count()  # Use "objects" instead of "object_person"
    context = {'my_text': my_text, "people_kol": people_kol}
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
        form = UserForm(request.POST)
        if form.is_valid():
            # Create a new Person object and save it to the database
            person = Person(
                name=form.cleaned_data['name'],
                age=form.cleaned_data['age']
            )
            person.save()
            return redirect('my_form')  # Redirect to a success page or another view
    else:
        form = UserForm()

    my_text = "Сведения о клиентах"
    people = Person.objects.all()
    context = {"my_text": my_text, "people": people, "form": form}
    return render(request, "firstapp/my_form.html", context)


# def my_form(request):
#     if request.method == "POST":
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form.save()
#     my_text = "Сведения о клиентах"
#     people = Person.object_person.all()  # Assuming you have a Person model
#     form = UserForm()  # Reinitialize the form
#     context = {"my_text": my_text, "people": people, "form": form}
#     return render(request, "firstapp/my_form.html", context)


# def my_form(request):
#     if request.method == "POST":
#         user_form = UserForm(request.POST)
#         if user_form.is_valid():
#             name = user_form.cleaned_data.get("name")  # Get the cleaned data for 'name' field
#             age = user_form.cleaned_data.get("age")  # Get the cleaned data for 'age' field
#             output = "<h2>Пользователь</h2><h3>Имя - {}, Возраст - {}</h3>".format(name, age)
#             return HttpResponse(output)
#     else:
#         user_form = UserForm()
#     return render(request, "firstapp/my_form.html", {"form": user_form})


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
