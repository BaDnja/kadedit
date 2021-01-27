# Generated by Django 3.1.4 on 2021-01-12 14:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0010_auto_20210112_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='datum kreiranja'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='deactivation_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='datum deaktivacije'),
        ),
        migrations.AddField(
            model_name='subject',
            name='modification_date',
            field=models.DateTimeField(auto_now=True, verbose_name='datum izmjene'),
        ),
    ]