# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 00:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0013_auto_20170826_2146'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LostPet',
            new_name='Pet',
        ),
    ]
