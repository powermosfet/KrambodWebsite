# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-16 22:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krambod', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Informasjon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_changed', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=160)),
                ('content', models.CharField(max_length=1024)),
            ],
        ),
    ]
