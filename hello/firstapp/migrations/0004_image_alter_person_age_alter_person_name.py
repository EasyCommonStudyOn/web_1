# Generated by Django 4.2.5 on 2023-09-26 08:15

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ("firstapp", "0003_course_user_account_student"),
    ]

    operations = [
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=100, verbose_name="Описание изображения"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="images",
                        verbose_name="Файл с изображением",
                    ),
                ),
            ],
            managers=[
                ("obj_img", django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name="person",
            name="age",
            field=models.IntegerField(verbose_name="Boзpacт клиента"),
        ),
        migrations.AlterField(
            model_name="person",
            name="name",
            field=models.CharField(max_length=20, verbose_name="Имя клиента"),
        ),
    ]
