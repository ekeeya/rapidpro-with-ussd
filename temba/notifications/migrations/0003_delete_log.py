# Generated by Django 3.2.6 on 2021-09-10 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("notifications", "0002_auto_20210903_2101"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Log",
        ),
    ]
