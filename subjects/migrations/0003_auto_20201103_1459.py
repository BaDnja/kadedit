# Generated by Django 3.1.2 on 2020-11-03 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0002_auto_20201103_1356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='study_program',
        ),
        migrations.AddField(
            model_name='subject',
            name='study_program',
            field=models.ManyToManyField(to='subjects.StudyProgram'),
        ),
    ]