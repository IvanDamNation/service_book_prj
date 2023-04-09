from datetime import date as date_module

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from accounts_app.models import ServiceManager
from .machine import Machine
from .other import Dictionary, ServiceCompany


class MaintainType(Dictionary):
    type_dict = models.CharField(max_length=32, default='Вид ТО', editable=False, verbose_name='Тип')

    class Meta:
        verbose_name = 'Вид ТО'
        verbose_name_plural = 'Виды ТО'


class Maintenance(models.Model):
    type = models.ForeignKey(MaintainType, on_delete=models.PROTECT, verbose_name='Вид ТО')
    date = models.DateField(default=date_module.today, verbose_name='Дата проведения ТО')
    operating_hours = models.IntegerField(validators=[MaxValueValidator(100000, MinValueValidator(0))],
                                          verbose_name='Наработка, м/час')
    work_order = models.CharField(max_length=32, verbose_name='№ заказ-наряда')
    work_order_date = models.DateField(default=date_module.today, verbose_name='Дата заказ-наряда')
    maintain_corp = models.ForeignKey(ServiceCompany, on_delete=models.PROTECT,
                                      verbose_name='Организация, проводившая ТО')
    machine = models.ForeignKey(Machine, on_delete=models.PROTECT, verbose_name='Машина', related_name='machinemaintein')
    service_comp = models.ForeignKey(ServiceManager, on_delete=models.PROTECT, verbose_name='Сервисная компания')

    class Meta:
        verbose_name = 'Техническое обслуживание'
        verbose_name_plural = 'Техническое обслуживание'
        ordering = ['-work_order_date', ]


