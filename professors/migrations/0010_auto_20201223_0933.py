# Generated by Django 3.1.4 on 2020-12-23 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professors', '0009_auto_20201223_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='inactive',
            field=models.BooleanField(default=False, verbose_name='inactive'),
        ),
    ]