# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-09 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0021_auto_20170909_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='pet_image',
            field=models.ImageField(blank=True, null=True, upload_to='pets/'),
        ),
    ]
