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








'''

from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
