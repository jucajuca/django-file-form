# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 11:30
from __future__ import unicode_literals

from django.db import migrations, models
import django_file_form.models


class Migration(migrations.Migration):

    dependencies = [
        ("django_file_form", "0002_auto_20170316_0901"),
    ]

    operations = [
        migrations.AlterField(
            model_name="uploadedfile",
            name="uploaded_file",
            field=models.FileField(max_length=255),
        ),
    ]
