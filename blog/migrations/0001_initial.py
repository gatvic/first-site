# Generated by Django 4.0.1 on 2022-01-17 08:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Создано')),
                ('published_date', models.DateTimeField(blank=True, null=True, verbose_name='Опубликовано')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
        ),
    ]
