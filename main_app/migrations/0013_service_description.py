# Generated by Django 2.2.6 on 2019-11-29 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_records'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='description',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
    ]
