from datetime import date

from django.db import models

from accounts_app.models import Customer
from .other import Dictionary, ServiceCompany


class MachineModel(Dictionary):
    type_dict = models.CharField(max_length=32, default='Модель машины', editable=False, verbose_name='Тип')

    class Meta:
        verbose_name = 'Модель машины'
        verbose_name_plural = 'Модели машин'


class EngineModel(Dictionary):
    type_dict = models.CharField(max_length=32, default='Модель двигателя', editable=False, verbose_name='Тип')

    class Meta:
        verbose_name = 'Двигатель'
        verbose_name_plural = 'Двигатели'


class TransmissionModel(Dictionary):
    type_dict = models.CharField(max_length=32, default='Трансмиссия', editable=False, verbose_name='Тип')

    class Meta:
        verbose_name = 'Трансмиссия'
        verbose_name_plural = 'Трансмиссии'


class RearAxleModel(Dictionary):
    type_dict = models.CharField(max_length=32, default='Задний ведущий мост', editable=False, verbose_name='Тип')

    class Meta:
        verbose_name = 'Задний ведущий мост'
        verbose_name_plural = 'Задние ведущие мосты'


class FrontAxle(Dictionary):
    type_dict = models.CharField(max_length=32, default='Передний управляемый мост', editable=False, verbose_name='Тип')

    class Meta:
        verbose_name = 'Передний управляемый мост'
        verbose_name_plural = 'Передние управляемые мосты'


class Machine(models.Model):
    factory_number = models.CharField(
        max_length=32, unique=True, verbose_name='Зав. № машины'
    )
    model = models.ForeignKey(
        MachineModel, on_delete=models.PROTECT, verbose_name='Модель техники'
    )
    engine = models.ForeignKey(
        EngineModel, on_delete=models.PROTECT, verbose_name='Модель двигателя'
    )
    engine_num = models.CharField(
        max_length=16, unique=True, verbose_name='Зав. № двигателя'
    )
    transmission = models.ForeignKey(
        TransmissionModel, on_delete=models.PROTECT, verbose_name='Модель трансмиссии'
    )
    transmission_num = models.CharField(
        max_length=16, unique=True, verbose_name='Зав. № трансмиссии'
    )
    rear_axle = models.ForeignKey(
        RearAxleModel, on_delete=models.PROTECT, verbose_name='Модель ведущего моста',
        related_name='rearaxle'
    )
    rear_axle_num = models.CharField(
        max_length=16, unique=True, verbose_name='Зав. № ведущего моста'
    )
    front_axle = models.ForeignKey(
        FrontAxle, on_delete=models.PROTECT, verbose_name='Модель управляемого моста',
        related_name='frontaxle'
    )
    front_axle_num = models.CharField(
        max_length=16, verbose_name='Зав. № управляемого моста'
    )
    supply_contract = models.CharField(
        max_length=32, verbose_name='Договор поставки №, дата'
    )
    shipment_date = models.DateField(
        default=date.today, verbose_name='Дата отгрузки с завода'
    )
    consignee = models.CharField(
        max_length=64, verbose_name='Грузополучатель (конечный потребитель)'
    )
    shipment_address = models.CharField(
        max_length=128, verbose_name='Адрес поставки (эксплуатации)'
    )
    equipment = models.CharField(
        max_length=128, verbose_name='Комплектация (доп. опции)'
    )
    client = models.ForeignKey(
        Customer, on_delete=models.PROTECT, verbose_name='Клиент', related_name='client'
    )
    service_comp = models.ForeignKey(
        ServiceCompany, on_delete=models.PROTECT, verbose_name='Сервисная компания',
        related_name='service'
    )

    def __str__(self):
        return '{}'.format(self.factory_number)

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'
        ordering = ['model', 'factory_number']
