# Generated by Django 2.2.6 on 2019-11-24 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_master_free_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='free_time',
        ),
    ]
