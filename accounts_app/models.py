from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class FactoryManager(models.Model):
    manager = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.CharField(max_length=32, default='Менеджер производителя', editable=False)

    def __str__(self):
        return '{}'.format(self.manager.username)

    class Meta:
        verbose_name = 'Менеджер производителя'
        verbose_name_plural = 'Менеджеры производителя'
        ordering = ['manager']


class ServiceManager(models.Model):
    manager = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.CharField(max_length=32, default='Менеджер сервис-центра', editable=False)

    def __str__(self):
        return '{}'.format(self.manager.username)

    class Meta:
        verbose_name = 'Менеджер сервиса'
        verbose_name_plural = 'Менеджеры сервисных компаний'
        ordering = ['manager']


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.CharField(max_length=32, default='Пользователь', editable=False)

    def __str__(self):
        return '{}'.format(self.user.username)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['user']

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Customer.objects.create(user=instance)
