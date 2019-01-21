# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-04 16:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(default='默认用户', max_length=30)),
                ('password', models.CharField(max_length=256)),
                ('phone', models.CharField(max_length=11, unique=True)),
                ('icon', models.CharField(max_length=256)),
                ('sex', models.CharField(choices=[('男性', '男性'), ('女性', '女性'), ('保密', '保密')], max_length=4)),
                ('age', models.IntegerField(default=18)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]