from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE, verbose_name='Автор')
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name="URL")
    title = models.CharField(max_length=255, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Создано')
    published_date = models.DateTimeField(blank=True, null=True, verbose_name='Опубликовано')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
# Create your models here.
