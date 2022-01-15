from django.db import models


class Plants(models.Model):
    plant = models.CharField(max_length=200, verbose_name='Растение')
    n = models.IntegerField()
    p = models.IntegerField()
    k = models.IntegerField()
    ca = models.IntegerField()
    mg = models.IntegerField()

    def __str__(self):
        return self.plant


class Substances(models.Model):
    sub = models.CharField(max_length=200, verbose_name='Удобрение')
    n = models.IntegerField()
    p = models.IntegerField()
    k = models.IntegerField()
    ca = models.IntegerField()
    mg = models.IntegerField()

    def __str__(self):
        return self.sub
