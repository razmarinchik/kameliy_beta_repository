# Generated by Django 2.2.6 on 2019-11-23 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20191122_1932'),
    ]

    operations = [
        migrations.CreateModel(
            name='FreeTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='Свободное время')),
            ],
            options={
                'verbose_name': 'Время',
                'verbose_name_plural': 'Время',
            },
        ),
        migrations.AlterModelOptions(
            name='master',
            options={'verbose_name': 'Мастер', 'verbose_name_plural': 'Мастера'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Услуга', 'verbose_name_plural': 'Услуги'},
        ),
        migrations.AlterField(
            model_name='master',
            name='master_name',
            field=models.CharField(max_length=50, verbose_name='Имя мастера'),
        ),
        migrations.AlterField(
            model_name='service',
            name='service_name',
            field=models.CharField(max_length=30, verbose_name='Услуга'),
        ),
        migrations.AddField(
            model_name='service',
            name='free_time',
            field=models.ManyToManyField(to='main_app.FreeTime'),
        ),
    ]