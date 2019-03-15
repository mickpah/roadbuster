# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-03-15 16:27
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ('global_cms_contact_us', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactuscontainerpluginmodel',
            name='bg_image',
            field=filer.fields.file.FilerFileField(blank=True, on_delete=django.db.models.deletion.PROTECT, to='filer.File', verbose_name='background image'),
        ),
    ]
