# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 21:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0018_auto_20161102_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singles',
            name='AlbumID',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Album'),
        ),
    ]
