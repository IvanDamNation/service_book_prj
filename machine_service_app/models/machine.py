from datetime import date

from django.db import models

from accounts_app.models import Customer
from .other import Dictionary, ServiceCompany


class MachineModel(Dictionary):
    type_dict = models.CharField(max_length=32, default='Модель машины')

    class Meta:
        verbose_name = 'Модель машины'
        verbose_name_plural = 'Модели машин'


class EngineModel(Dictionary):
    type_dict = models.CharField(max_length=32, default='Модель двигателя')

    class Meta:
        verbose_name = 'Двигатель'
        verbose_name_plural = 'Двигатели'


class TransmissionModel(Dictionary):
    type_dict = models.CharField(max_length=32, default='Трансмиссия')

    class Meta:
        verbose_name = 'Трансмиссия'
        verbose_name_plural = 'Трансмиссии'


class RearAxleModel(Dictionary):
    type_dict = models.CharField(max_length=32, default='Задний ведущий мост')

    class Meta:
        verbose_name = 'Задний ведущий мост'
        verbose_name_plural = 'Задние ведущие мосты'


class FrontAxle(Dictionary):
    type_dict = models.CharField(max_length=32, default='Передний управляемый мост')

    class Meta:
        verbose_name = 'Передний управляемый мост'
        verbose_name_plural = 'Передние управляемые мосты'


class Machine(models.Model):
    factory_number = models.CharField(max_length=32, unique=True)
    model = models.ForeignKey(MachineModel, on_delete=models.PROTECT)
    engine = models.ForeignKey(EngineModel, on_delete=models.PROTECT)
    engine_num = models.CharField(max_length=16, unique=True)
    transmission = models.ForeignKey(TransmissionModel, on_delete=models.PROTECT)
    transmission_num = models.CharField(max_length=16, unique=True)
    rear_axle = models.ForeignKey(RearAxleModel, on_delete=models.PROTECT)
    rear_axle_num = models.CharField(max_length=16, unique=True)
    front_axle = models.ForeignKey(FrontAxle, on_delete=models.PROTECT)
    front_axle_num = models.CharField(max_length=16)
    supply_contract = models.CharField(max_length=32)
    shipment_date = models.DateField(default=date.today)
    consignee = models.CharField(max_length=64)
    shipment_address = models.CharField(max_length=128)
    equipment = models.CharField(max_length=128)
    client = models.ForeignKey(Customer, on_delete=models.PROTECT)
    service_comp = models.ForeignKey(ServiceCompany, on_delete=models.PROTECT)

    def __str__(self):
        return '{}'.format(self.factory_number)

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'
        ordering = ['model', 'factory_number']

