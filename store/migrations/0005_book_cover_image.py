# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-02 18:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20170328_0114'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(default='books/empty_cover.jpg', upload_to='books/'),
        ),
    ]
