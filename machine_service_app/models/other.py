from django.db import models


class Dictionary(models.Model):
    name = models.CharField(max_length=32, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = '__Справочник__'
        verbose_name_plural = '__Справочники__'
        ordering = ['name']


class ServiceCompany(models.Model):
    name = models.CharField(max_length=32, verbose_name='Описание')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Сервисная компания'
        verbose_name_plural = 'Сервисные компании'
