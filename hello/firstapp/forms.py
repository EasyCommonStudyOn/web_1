'''
поля класса формы сопоставляются с элементами ввода ( <input>) НТМL-страницы
'''
from django import forms
from .models import Image


class UserForm(forms.Form):
    name = forms.CharField(label="Имя клиента", max_length=15, help_text="ФИO не более 15 символов",
                           initial="Bвeдитe ФИО")
    age = forms.IntegerField(label="Возраст", help_text="Введите возраст", initial=18)
    comment = forms.CharField(
        label="Комментарий", widget=forms.Textarea  # Назначим для поля ввода комментариев другой виджет
    )
    email = forms.EmailField(label="Электронный адрес")
    reklama = forms.BooleanField(label="Согласны получать рекламу", required=False)
    # field_order = ["age", "name"]

    required_css_class = "field"
    error_css_class = "error"


# ''' Здесь из модуля с моделями бьm импортирован класс rmage, и создана наша форма -
# # класс ImageForm на основе базового класса forms. ModelForm. Затем инициирован класс меtа,
# # в котором созданы объекты model и fields. Преимущество создания формы на основе
# # базового класса Django forms.ModelForm заключается в том, что форма автоматически
# # создаст поля на НТМL-странице в соответствии с полями модели Image, упомянутыми
# # в модуле model.py.
# # '''
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'


# basket = forms.BooleanField(label="Пoлoжить товар в корзину", required=False)
# ling = forms.ChoiceField(label="Bыбepитe язык", choices=((1, "Английский"),
#                                                          (2, "Немецкий"),
#                                                          (3, "Французский")))
# country = forms.MultipleChoiceField(
#     label="Выберите страны",
#     choices=(
#         (1, "Англия"),
#         (2, "Германия"),
#         (3, "Испания"),
#         (4, "Россия"),
#     ),
#     widget=forms.CheckboxSelectMultiple,  # Use checkboxes for multiple selections
# )
#
# city = forms.TypedChoiceField(
#     label="Выберите город",
#     empty_value=None,  # Optional, you can specify the default empty value
#     choices=(
#         (1, "Москва"),
#         (2, "Воронеж"),
#         (3, "Курск"),
#     ),
#     coerce=int,  # Specify the data type you want to enforce (int in this case)
# )
#
# city2 = forms.TypedMultipleChoiceField(
#     label="Выберите город",
#     empty_value=None,  # Optional, you can specify the default empty value
#     choices=(
#         (1, "Москва"),
#         (2, "Воронеж"),
#         (3, "Курск"),
#         (4, "Томск"),
#     ),
#     coerce=int,  # Specify the data type you want to enforce (int in this case)
# )
#
# date = forms.DateField(label="Введите дату")
# date_time = forms.DateTimeField(label="Введите дату и время")
# date_time1 = forms.SplitDateTimeField(
#     label="Введите дату и время"
# )
#
# num = forms.DecimalField(label="Введите десятичное число", decimal_places=2)
#
# time_delta = forms.DurationField(label="Введите промежуток времени")
# email = forms.EmailField(label="Электронный адрес", help_text="Обязательный символ - @")
# file = forms.FileField(label="Файл")
# # file_path = forms.FilePathField(
# #     label="Выберите файл",
# #     path="C:/my_doc/",  # Specify the directory path you want to display files from
# #     match="*.txt",  # Optionally, you can specify a file pattern to filter files
# # )
# numF = forms.FloatField(label="Введите число")
# #
# ip_adres = forms.GenericIPAddressField(
#     label="IP адрес",
#     help_text="Пример формата 192.0.2.0"
# )
# #
# image = forms.ImageField(label="Изображение")
# data = forms.JSONField(label="Данные формата JSON")
# will_travel = forms.NullBooleanField(label="Bы поедете в Сочи этим летом?")
# reg_text = forms.RegexField(
#     label="Текст",
#     regex=r"л[0-9] [A-F] [0-9]$",
#     help_text="Пожалуйста, введите текст, соответствующий паттерну 'л[0-9] [A-F] [0-9]'"
# )
# slug_text = forms.SlugField(label="Введите текст")
# time = forms.TimeField(label="Введите время")
# url_text = forms.URLField(
#     label="Введите URL",
#     help_text="Пример: http://www.yandex.ru",
# )
# uuid_text = forms.UUIDField(
#     label="Введите UUID",
#     help_text="Формат ххххххх-хххх-хххх-хххх-хххххххххххх",
# )
# combo_text = forms.ComboField(
#     label='Введите данные',
#     fields=[
#         forms.CharField(max_length=20),
#         forms.EmailField(),
#     ]
# )
#
# combo_text2 = forms.MultiValueField(
#     label='Комплексное поле',
#     fields=(
#         forms.CharField(max_length=20),
#         forms.EmailField(),
#     )
# )
#


'''
fоrm.название_поля.nаmе-возвращает название поля;
□ fоrm.название_поля.vаluе -возвращает значение поля, которое ему бьшо передано по
умолчанию;
□ form. название_ nоля. label - возвращает текст метки, которая генерируется рядом
с полем;
□ fоrm.название_поля.id_fоr_lаЬеl - возвращает id для поля, которое по умолчанию
создается по схеме id имя_ поля;
□ fоrm.название_поля.аutо_id-возвращает id для поля, которое по умолчанию создается
по схеме id_имя_поля;
□ fоrm.название_поля.lаЬеl_tаg -возвращает элемент laЬel, который представляет метку
рядом с полем;
□ fоrm.название_поля.hеlр_tехt -возвращает текст подсказки, ассоциированной с по-
лем;
□ tоrm.название
_
поля .еrrоrs -возвращает ошибки валидации, связанные с полем;
□ form.нaзвaниe_пoля.css_classes -возвращает СSS-классы поля;
□ form.нaзвaниe_пoля.as_hidden - генерирует для поля разметку в виде скрытого поля
<input type="hidden">;
□ form. название
_
поля. is hidden -возвращает True или False в зависимости от того, является
ли поле скрытым;
□ fоrm.название_поля.аs_tехt -генерирует для поля разметку в виде текстового поля
<input type="text">;

fоrm.название поля.аs textarea генерирует для поля разметку в виде <textarea>

forrn.нaзвaниe_пoля.as_widget - возвращает виджет Django, который ассоциирован
с полем.
'''
