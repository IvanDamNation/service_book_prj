# Generated by Django 4.2 on 2023-04-08 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_app', '0001_initial'),
        ('machine_service_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='owner', to='accounts_app.customer', verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='service_comp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='service', to='machine_service_app.servicecompany', verbose_name='Сервисная компания'),
        ),
    ]