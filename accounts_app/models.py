from django.db import models
from django.contrib.auth.models import User


class FactoryManager(models.Model):
    manager = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Менеджер производителя'
        verbose_name_plural = 'Менеджеры производителя'
        ordering = ['manager']


class ServiceManager(models.Model):
    manager = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Менеджер сервиса'
        verbose_name_plural = 'Менеджеры сервисных компаний'
        ordering = ['manager']


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['user']
