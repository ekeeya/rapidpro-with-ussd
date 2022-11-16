# Generated by Django 4.0.7 on 2022-11-14 10:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone
import temba.utils.uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('channels', '0154_delete_channelconnection'),
        ('orgs', '0102_alter_org_brand_alter_org_plan'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Handler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, help_text='Whether this item is active, use this instead of deleting')),
                ('created_on', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, help_text='When this item was originally created')),
                ('modified_on', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, help_text='When this item was last modified')),
                ('uuid', models.UUIDField(default=temba.utils.uuid.uuid4, unique=True)),
                ('aggregator', models.CharField(help_text='Your USSD aggregator', max_length=150, verbose_name='Aggregator')),
                ('short_code', models.CharField(help_text='The USSD shortcode sent by the aggregator in the request.', max_length=50, unique=True, verbose_name='Short code')),
                ('request_structure', models.TextField(help_text="The format of the request string from aggregator's USSD API e.g. in format {{from=msisdn}}")),
                ('signal_exit_or_reply_mode', models.IntegerField(choices=[(1, 'Starts With (Plain Text)'), (2, 'Ends With (Plain Text)'), (3, 'Is In Response (XML/JSON)'), (4, 'Is in Headers (XML/JSON)'), (5, 'Is in Headers (Plain Text)')], default=3, help_text='This indicates how the menu type signal flag/word will be sent back to the aggregator', verbose_name='Menu Type Flag Mode')),
                ('signal_header_key', models.CharField(blank=True, help_text='Represents header whose value is the menu type flag if mode is Is In Headers', max_length=20, null=True, verbose_name='Menu Type Header name')),
                ('response_structure', models.TextField(blank=True, help_text='The structure of the response as expected by the aggregator API', null=True, verbose_name='Response Structure')),
                ('signal_menu_type_strings', models.CharField(blank=True, help_text='Comma-separated key words that indicate which menu type end-user receives e.g END,CON', max_length=20, null=True, verbose_name='Signal Exit/Wait-Response Flag')),
                ('auth_scheme', models.CharField(choices=[('NONE', 'NONE'), ('TOKEN', 'TOKEN'), ('JWT', 'JWT'), ('BASIC', 'BASIC')], default='NONE', help_text='Authentication scheme with which aggregators must authenticate with when calling your callback', max_length=30, verbose_name='Authentication Scheme')),
                ('trigger_word', models.CharField(default='USSD', help_text='This will trigger execution of a given flow', max_length=50)),
                ('enable_repeat_current_step', models.BooleanField(default=False, help_text='Continue from current step in the flow even with a new USSD session')),
                ('expire_on_inactivity_of', models.IntegerField(default=300, editable=False, help_text='Expire all contacts out of their flows, when handler is idle for these seconds', verbose_name='')),
                ('last_accessed_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('auth_token', models.CharField(blank=True, editable=False, max_length=50, null=True)),
                ('channel', models.ForeignKey(help_text="Select any channel of 'External API' Type you would want this handler to use.", on_delete=django.db.models.deletion.PROTECT, to='channels.channel', verbose_name='USSD Channel')),
                ('created_by', models.ForeignKey(help_text='The user which originally created this item', on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_creations', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(help_text='The user which last modified this item', on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_modifications', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='USSDContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urn', models.CharField(max_length=25, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
            options={
                'db_table': 'ussd_contact',
            },
            managers=[
                ('contacts', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified_on', models.DateTimeField(auto_now=True, db_index=True)),
                ('is_active', models.BooleanField(default=True)),
                ('session_id', models.CharField(max_length=100, unique=True)),
                ('status', models.CharField(choices=[('P', 'In Progress'), ('TO', 'Timed Out'), ('C', 'Completed'), ('T', 'Terminated')], default='P', max_length=5)),
                ('badge', models.CharField(default='info', max_length=15)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ussd.ussdcontact')),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created', to='orgs.user')),
                ('handler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ussd.handler')),
                ('modified_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_modified', to='orgs.user')),
            ],
            options={
                'ordering': ['-created_on'],
            },
            managers=[
                ('sessions', django.db.models.manager.Manager()),
            ],
        ),
    ]
