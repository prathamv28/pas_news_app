# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-27 10:09
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=500)),
                ('body', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
