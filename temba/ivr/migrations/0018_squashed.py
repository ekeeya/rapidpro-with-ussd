# Generated by Django 4.0.3 on 2022-03-10 17:56

from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("channels", "0137_squashed"),
    ]

    operations = [
        migrations.CreateModel(
            name="IVRCall",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("channels.channelconnection",),
        ),
    ]
