# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 03:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20170518_0341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer', verbose_name='cliente'),
        ),
        migrations.AlterField(
            model_name='order',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Service', verbose_name='servi\xe7o'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.OrderStatus', verbose_name='status'),
        ),
    ]
