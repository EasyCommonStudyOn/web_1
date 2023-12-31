# Generated by Django 4.2.5 on 2023-09-26 18:48

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0006_videofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='AudioFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Описание файла')),
                ('file', models.FileField(blank=True, null=True, upload_to='audios', verbose_name='Аудиофайл')),
            ],
            managers=[
                ('obj_audio', django.db.models.manager.Manager()),
            ],
        ),
    ]
