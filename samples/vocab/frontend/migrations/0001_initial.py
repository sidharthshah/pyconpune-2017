# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current', models.CharField(max_length=255)),
                ('meaning', models.TextField()),
            ],
        ),
    ]