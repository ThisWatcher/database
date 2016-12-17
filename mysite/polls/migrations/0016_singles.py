# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 21:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_auto_20161102_2002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Singles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Single', models.CharField(default='', max_length=200)),
                ('Year', models.DateField(verbose_name='Year')),
                ('AlbumID', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Album')),
                ('ArtistID', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='polls.Artist')),
            ],
        ),
    ]
