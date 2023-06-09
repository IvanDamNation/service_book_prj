# Generated by Django 4.2 on 2023-04-09 12:50

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': '__Справочник__',
                'verbose_name_plural': '__Справочники__',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ServiceCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Описание')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Сервисная компания',
                'verbose_name_plural': 'Сервисные компании',
            },
        ),
        migrations.CreateModel(
            name='EngineModel',
            fields=[
                ('dictionary_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='machine_service_app.dictionary')),
                ('type_dict', models.CharField(default='Модель двигателя', editable=False, max_length=32, verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Двигатель',
                'verbose_name_plural': 'Двигатели',
            },
            bases=('machine_service_app.dictionary',),
        ),
        migrations.CreateModel(
            name='FailureType',
            fields=[
                ('dictionary_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='machine_service_app.dictionary')),
                ('type_dict', models.CharField(default='Характер отказа', editable=False, max_length=32, verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Характер отказа',
                'verbose_name_plural': 'Характеры отказа',
            },
            bases=('machine_service_app.dictionary',),
        ),
        migrations.CreateModel(
            name='FrontAxle',
            fields=[
                ('dictionary_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='machine_service_app.dictionary')),
                ('type_dict', models.CharField(default='Передний управляемый мост', editable=False, max_length=32, verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Передний управляемый мост',
                'verbose_name_plural': 'Передние управляемые мосты',
            },
            bases=('machine_service_app.dictionary',),
        ),
        migrations.CreateModel(
            name='MachineModel',
            fields=[
                ('dictionary_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='machine_service_app.dictionary')),
                ('type_dict', models.CharField(default='Модель машины', editable=False, max_length=32, verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Модель машины',
                'verbose_name_plural': 'Модели машин',
            },
            bases=('machine_service_app.dictionary',),
        ),
        migrations.CreateModel(
            name='MaintainType',
            fields=[
                ('dictionary_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='machine_service_app.dictionary')),
                ('type_dict', models.CharField(default='Вид ТО', editable=False, max_length=32, verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Вид ТО',
                'verbose_name_plural': 'Виды ТО',
            },
            bases=('machine_service_app.dictionary',),
        ),
        migrations.CreateModel(
            name='RearAxleModel',
            fields=[
                ('dictionary_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='machine_service_app.dictionary')),
                ('type_dict', models.CharField(default='Задний ведущий мост', editable=False, max_length=32, verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Задний ведущий мост',
                'verbose_name_plural': 'Задние ведущие мосты',
            },
            bases=('machine_service_app.dictionary',),
        ),
        migrations.CreateModel(
            name='RecoveryMethods',
            fields=[
                ('dictionary_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='machine_service_app.dictionary')),
                ('type_dict', models.CharField(default='Способ восстановления', editable=False, max_length=32, verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Способ восстановления',
                'verbose_name_plural': 'Способы восстановления',
            },
            bases=('machine_service_app.dictionary',),
        ),
        migrations.CreateModel(
            name='TransmissionModel',
            fields=[
                ('dictionary_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='machine_service_app.dictionary')),
                ('type_dict', models.CharField(default='Трансмиссия', editable=False, max_length=32, verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Трансмиссия',
                'verbose_name_plural': 'Трансмиссии',
            },
            bases=('machine_service_app.dictionary',),
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factory_number', models.CharField(max_length=32, unique=True, verbose_name='Зав. № машины')),
                ('engine_num', models.CharField(max_length=16, unique=True, verbose_name='Зав. № двигателя')),
                ('transmission_num', models.CharField(max_length=16, unique=True, verbose_name='Зав. № трансмиссии')),
                ('rear_axle_num', models.CharField(max_length=16, unique=True, verbose_name='Зав. № ведущего моста')),
                ('front_axle_num', models.CharField(max_length=16, verbose_name='Зав. № управляемого моста')),
                ('supply_contract', models.CharField(max_length=32, verbose_name='Договор поставки №, дата')),
                ('shipment_date', models.DateField(default=datetime.date.today, verbose_name='Дата отгрузки с завода')),
                ('consignee', models.CharField(max_length=64, verbose_name='Грузополучатель (конечный потребитель)')),
                ('shipment_address', models.CharField(max_length=128, verbose_name='Адрес поставки (эксплуатации)')),
                ('equipment', models.CharField(max_length=128, verbose_name='Комплектация (доп. опции)')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='client', to='accounts_app.customer', verbose_name='Клиент')),
                ('service_comp', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='service', to='machine_service_app.servicecompany', verbose_name='Сервисная компания')),
                ('engine', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='machine_service_app.enginemodel', verbose_name='Модель двигателя')),
                ('front_axle', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='frontaxle', to='machine_service_app.frontaxle', verbose_name='Модель управляемого моста')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='machine_service_app.machinemodel', verbose_name='Модель техники')),
                ('rear_axle', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='rearaxle', to='machine_service_app.rearaxlemodel', verbose_name='Модель ведущего моста')),
                ('transmission', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='machine_service_app.transmissionmodel', verbose_name='Модель трансмиссии')),
            ],
            options={
                'verbose_name': 'Машина',
                'verbose_name_plural': 'Машины',
                'ordering': ['model', 'factory_number'],
            },
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Дата проведения ТО')),
                ('operating_hours', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100000, django.core.validators.MinValueValidator(0))], verbose_name='Наработка, м/час')),
                ('work_order', models.CharField(max_length=32, verbose_name='№ заказ-наряда')),
                ('work_order_date', models.DateField(default=datetime.date.today, verbose_name='Дата заказ-наряда')),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='machinemaintein', to='machine_service_app.machine', verbose_name='Машина')),
                ('maintain_corp', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='machine_service_app.servicecompany', verbose_name='Организация, проводившая ТО')),
                ('service_comp', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts_app.servicemanager', verbose_name='Сервисная компания')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='machine_service_app.maintaintype', verbose_name='Вид ТО')),
            ],
            options={
                'verbose_name': 'Техническое обслуживание',
                'verbose_name_plural': 'Техническое обслуживание',
                'ordering': ['-work_order_date'],
            },
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_complaint', models.DateField(default=datetime.date.today, verbose_name='Дата отказа')),
                ('operating_hours', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100000, django.core.validators.MinValueValidator(0))], verbose_name='Наработка, м/час')),
                ('failure_description', models.CharField(max_length=255, verbose_name='Описание отказа')),
                ('used_parts', models.CharField(max_length=255, verbose_name='Используемые запасные части')),
                ('date_of_repair', models.DateField(default=datetime.date.today, verbose_name='Дата восстановления')),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='machine_service_app.machine', verbose_name='Mашина')),
                ('service_comp', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts_app.servicemanager', verbose_name='Cервисная компания')),
                ('recovery_method', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='machine_service_app.recoverymethods', verbose_name='Способ восстановления')),
                ('unit_failure', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='machine_service_app.failuretype', verbose_name='Узел отказа')),
            ],
            options={
                'verbose_name': 'Рекламация',
                'verbose_name_plural': 'Рекламации',
                'ordering': ['-date_of_complaint'],
            },
        ),
    ]
