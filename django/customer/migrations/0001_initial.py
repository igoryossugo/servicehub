# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-10 05:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='nome do consumidor')),
                ('cpf', models.CharField(max_length=30, verbose_name='cpf')),
                ('email', models.EmailField(max_length=254, verbose_name='email do consumidor')),
            ],
        ),
    ]