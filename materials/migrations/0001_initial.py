# Generated by Django 5.0.7 on 2024-07-30 13:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Укажите название', max_length=100, verbose_name='Курс')),
                ('preview_image', models.ImageField(upload_to='materials/course/')),
                ('description', models.TextField(blank=True, help_text='Укажите описание', null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Укажите название', max_length=100, verbose_name='Урок')),
                ('preview_image', models.ImageField(upload_to='materials/lesson/')),
                ('description', models.TextField(blank=True, help_text='Укажите описание', null=True, verbose_name='Описание')),
                ('video_url', models.URLField(blank=True, help_text='Укажите ссылку на видео', null=True, verbose_name='Ссылка на видео')),
                ('course', models.ForeignKey(blank=True, help_text='Выберите курс', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lessons', to='materials.course', verbose_name='Курс')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
            },
        ),
    ]
