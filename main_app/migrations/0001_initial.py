# Generated by Django 2.2.6 on 2019-11-22 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('master_name', models.CharField(max_length=50)),
                ('age', models.FloatField()),
                ('description', models.TextField()),
            ],
        ),
    ]
