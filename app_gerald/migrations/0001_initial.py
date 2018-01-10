# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-06 08:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('father_name', models.CharField(max_length=30)),
                ('birthday', models.DateTimeField(verbose_name='Birthday')),
                ('sex', models.CharField(choices=[('m', 'male'), ('f', 'female')], max_length=1)),
                ('creation_date', models.DateTimeField(verbose_name='creation date')),
                ('father', models.IntegerField(default=-1)),
                ('mother', models.IntegerField(default=-1)),
            ],
        ),
    ]