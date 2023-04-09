from datetime import date as date_module, datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from accounts_app.models import ServiceManager
from machine_service_app.models import Machine
from .other import Dictionary


class FailureType(Dictionary):
    type_dict = models.CharField(max_length=32, default='Характер отказа', editable=False, verbose_name='Тип')

    class Meta:
        verbose_name = 'Характер отказа'
        verbose_name_plural = 'Характеры отказа'


class RecoveryMethods(Dictionary):
    type_dict = models.CharField(max_length=32, default='Способ восстановления', editable=False, verbose_name='Тип')

    class Meta:
        verbose_name = 'Способ восстановления'
        verbose_name_plural = 'Способы восстановления'


class Complaint(models.Model):
    date_of_complaint = models.DateField(default=date_module.today, verbose_name='Дата отказа')
    operating_hours = models.IntegerField(validators=[MaxValueValidator(100000, MinValueValidator(0))],
                                          verbose_name='Наработка, м/час')
    unit_failure = models.ForeignKey(FailureType, on_delete=models.PROTECT, verbose_name='Узел отказа')
    failure_description = models.CharField(max_length=255, verbose_name='Описание отказа')
    recovery_method = models.ForeignKey(RecoveryMethods,
                                        on_delete=models.PROTECT,
                                        verbose_name='Способ восстановления')
    used_parts = models.CharField(max_length=255, verbose_name='Используемые запасные части')
    date_of_repair = models.DateField(default=date_module.today, verbose_name='Дата восстановления')
    # downtime (property) (Время простоя техники)
    machine = models.ForeignKey(Machine, on_delete=models.PROTECT, verbose_name='Mашина')
    service_comp = models.ForeignKey(ServiceManager, on_delete=models.PROTECT, verbose_name='Cервисная компания')

    @property
    def downtime(self):
        date_format = "%d/%m/%Y"
        complaint = datetime.strptime(str(self.date_of_repair), date_format)
        repair = datetime.strptime(str(self.date_of_repair), date_format)
        days_downtime = complaint - repair
        return days_downtime

    class Meta:
        verbose_name = 'Рекламация'
        verbose_name_plural = 'Рекламации'
        ordering = ['-date_of_complaint', ]
