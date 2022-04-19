# Generated by Django 4.0.3 on 2022-03-10 17:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("msgs", "0169_squashed"),
        ("orgs", "0093_squashed"),
        ("contacts", "0153_squashed"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("channels", "0137_squashed"),
    ]

    operations = [
        migrations.AddField(
            model_name="channellog",
            name="msg",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.PROTECT, related_name="channel_logs", to="msgs.msg"
            ),
        ),
        migrations.AddField(
            model_name="channelevent",
            name="channel",
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="channels.channel"),
        ),
        migrations.AddField(
            model_name="channelevent",
            name="contact",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="channel_events", to="contacts.contact"
            ),
        ),
        migrations.AddField(
            model_name="channelevent",
            name="contact_urn",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="channel_events",
                to="contacts.contacturn",
            ),
        ),
        migrations.AddField(
            model_name="channelevent",
            name="org",
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="orgs.org"),
        ),
        migrations.AddField(
            model_name="channelcount",
            name="channel",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="counts", to="channels.channel"
            ),
        ),
        migrations.AddField(
            model_name="channelconnection",
            name="channel",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="connections", to="channels.channel"
            ),
        ),
        migrations.AddField(
            model_name="channelconnection",
            name="contact",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="connections", to="contacts.contact"
            ),
        ),
        migrations.AddField(
            model_name="channelconnection",
            name="contact_urn",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="connections", to="contacts.contacturn"
            ),
        ),
        migrations.AddField(
            model_name="channelconnection",
            name="org",
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="orgs.org"),
        ),
        migrations.AddField(
            model_name="channel",
            name="created_by",
            field=models.ForeignKey(
                help_text="The user which originally created this item",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(app_label)s_%(class)s_creations",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="channel",
            name="modified_by",
            field=models.ForeignKey(
                help_text="The user which last modified this item",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(app_label)s_%(class)s_modifications",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="channel",
            name="org",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.PROTECT, related_name="channels", to="orgs.org"
            ),
        ),
        migrations.AddField(
            model_name="channel",
            name="parent",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to="channels.channel"),
        ),
        migrations.AddField(
            model_name="alert",
            name="channel",
            field=models.ForeignKey(
                help_text="The channel that this alert is for",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="alerts",
                to="channels.channel",
                verbose_name="Channel",
            ),
        ),
        migrations.AddField(
            model_name="alert",
            name="created_by",
            field=models.ForeignKey(
                help_text="The user which originally created this item",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(app_label)s_%(class)s_creations",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="alert",
            name="modified_by",
            field=models.ForeignKey(
                help_text="The user which last modified this item",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(app_label)s_%(class)s_modifications",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="alert",
            name="sync_event",
            field=models.ForeignKey(
                help_text="The sync event that caused this alert to be sent (if any)",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="alerts",
                to="channels.syncevent",
                verbose_name="Sync Event",
            ),
        ),
        migrations.AddIndex(
            model_name="channellog",
            index=models.Index(
                condition=models.Q(("is_error", True)),
                fields=["channel", "is_error", "-created_on"],
                name="channels_log_error_created",
            ),
        ),
        migrations.AlterIndexTogether(
            name="channelcount",
            index_together={("channel", "count_type", "day")},
        ),
        migrations.AddIndex(
            model_name="channelconnection",
            index=models.Index(
                condition=models.Q(
                    ("connection_type", "V"), ("next_attempt__isnull", False), ("status__in", ("Q", "E"))
                ),
                fields=["next_attempt"],
                name="channelconnection_ivr_to_retry",
            ),
        ),
    ]