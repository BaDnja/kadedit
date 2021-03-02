# Generated by Django 3.1.4 on 2021-03-01 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0002_auto_20210301_1136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='semester',
            name='name',
        ),
        migrations.AddField(
            model_name='semester',
            name='number',
            field=models.IntegerField(blank=True, null=True, unique=True, verbose_name='number'),
        ),
    ]
