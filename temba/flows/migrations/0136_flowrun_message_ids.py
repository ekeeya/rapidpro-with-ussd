# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-14 15:33
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flows', '0135_new_path_trigger'),
    ]

    operations = [
        migrations.AddField(
            model_name='flowrun',
            name='message_ids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.BigIntegerField(), help_text='The IDs of messages associated with this run', null=True, size=None),
        ),
    ]
