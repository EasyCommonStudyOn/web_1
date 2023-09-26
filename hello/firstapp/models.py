# хранит определение моделей, которые описьmают данные, используемые
# в приложении;

# Связь между моделями и таблицами в БД максимально прямая: одна таблица - одна модель.
'''
В Django получить значение данных из БД можно несколькими методами:
□ get () - для одного объекта;
□ get _ or _ create () - для одного объекта с добавлением его в БД;
□ all () - для всех объектов;
□ count ( )- получить число объектов;
□ filter () - для группы объектов по фильтру;
□ exclude () - для группы объектов с исключением некоторых;
□ in bulk () - для группы объектов в виде словаря.

Параметр on ctelete может принимать следующие значения:
□ models.CASCADE- автоматически удаляет строку (строки) из зависимой таблицы, если
удаляется связанная строка из главной таблицы;
□ models. РRОГЕСТ - блокирует удаление строки из главной таблицы, если с ней связаны
какие-либо строки в зависимой таблице;
□ models. SET NULL - устанавливает значение NULL при удалении связанной строки из
главной таблицы;
□ models.SET.:DEFAULT - устанавливает значение по умолчанию для внешнего ключа
в зависимой таблице (в таком случае для этого столбца должно быть задано значение
по умолчанию);
□ models.DO_NOГHING- при удалении связанной строки из главной таблицы не вьшол-
няются никакие действия в зависимой таблице.






'''

from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20, verbose_name="Имя клиента")
    age = models.IntegerField(verbose_name="Boзpacт клиента")
    objects = models.Manager()  # This is the default manager - это интерфейс, через который для моделей Django предоставляютсяоперации запросов к базе данных.


# Чтобы переименовать мanager для данного класса, можно воспользоваться, например,
# следующей инструкцией:
# objectperson = models.Manager()
    object_person = models.Manager()


class Company(models.Model):
    name = models.CharField(max_length=20)  # Changed "пате" to "name"


class Product(models.Model):
    company = models.ForeignKey(Company,
                                on_delete=models.CASCADE)  # предусмотрено каскадное удаление всех записей для случая, если компания будет удалена из главной таблицы.
    name = models.CharField(max_length=20)  # Changed "ЗO" to 20
    price = models.IntegerField()


class Course(models.Model):
    name = models.CharField(max_length=30)  # Changed "ЗO" to 30 as an example


class Student(models.Model):
    name = models.CharField(max_length=30)  # Changed "ЗO" to 30 as an example
    courses = models.ManyToManyField(Course)


class User(models.Model):
    name = models.CharField(max_length=20)


class Account(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                primary_key=True)  # указьmает, что внешний ключ (через который идет связь с главной моделью) одновременно будет выступать и в роли первичного ключа и соответственно создавать отдельное поле для первичного ключа.



class Image(models.Model):
    title = models.CharField(max_length=100, null=False, verbose_name="Описание изображения")
    image = models.ImageField(upload_to='images', verbose_name="Файл с изображением", null=True, blank=True) #поле image_file может оставаться пустыми (null=Тrue, Ыank=Тrue).

    obj_img = models.Manager() #менеджер для работы с объектами изображений в модели.

    def __str__(self):
        return self.title