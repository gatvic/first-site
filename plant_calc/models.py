from django.db import models


class Plant(models.Model):
    name = models.CharField(max_length=200, verbose_name='Растение')
    n = models.IntegerField()
    p = models.IntegerField()
    k = models.IntegerField()
    ca = models.IntegerField()
    mg = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:

        verbose_name = 'Растение'
        verbose_name_plural = 'Растения'


class Substance(models.Model):
    title = models.CharField(max_length=200, verbose_name='Удобрение')
    n = models.IntegerField()
    p = models.IntegerField()
    k = models.IntegerField()
    ca = models.IntegerField()
    mg = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вещество'
        verbose_name_plural = 'Вещества'
