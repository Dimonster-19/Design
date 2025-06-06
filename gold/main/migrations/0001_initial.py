# Generated by Django 5.2.1 on 2025-05-14 15:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('description', models.TextField(verbose_name='Описание')),
                ('cover', models.ImageField(upload_to='projects/', verbose_name='Обложка')),
                ('client', models.CharField(max_length=100, verbose_name='Клиент')),
                ('year', models.PositiveIntegerField(verbose_name='Год')),
                ('is_featured', models.BooleanField(default=False, verbose_name='В избранном')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='project_images/', verbose_name='Изображение')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.project')),
            ],
            options={
                'verbose_name': 'Изображение проекта',
                'verbose_name_plural': 'Изображения проектов',
                'ordering': ['order'],
            },
        ),
    ]
