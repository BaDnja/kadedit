# Generated by Django 3.1.4 on 2021-02-05 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65, unique=True, verbose_name='academic title')),
            ],
            options={
                'verbose_name': 'academic title',
                'verbose_name_plural': 'academic titles',
            },
        ),
        migrations.CreateModel(
            name='Engagement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65, unique=True, verbose_name='calling')),
            ],
            options={
                'verbose_name': 'calling',
                'verbose_name_plural': 'engagements',
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='datum kreiranja')),
                ('modification_date', models.DateTimeField(auto_now=True, verbose_name='datum izmjene')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(max_length=80, verbose_name='last name')),
                ('birthdate', models.DateField(blank=True, null=True, verbose_name='birthdate')),
                ('dissertation', models.CharField(blank=True, max_length=200, null=True, verbose_name='dissertation')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('academic_title', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='professors.academictitle', verbose_name='academic title')),
                ('calling', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='professors.calling', verbose_name='calling')),
            ],
            options={
                'verbose_name': 'professor',
                'verbose_name_plural': 'professors',
            },
        ),
        migrations.CreateModel(
            name='WorkStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65, unique=True, verbose_name='work status')),
            ],
            options={
                'verbose_name': 'work status',
                'verbose_name_plural': 'work statuses',
            },
        ),
        migrations.CreateModel(
            name='XProfessorSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('practice', models.BooleanField(blank=True, default=False, verbose_name='practice')),
                ('professor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='professors.professor', verbose_name='professor')),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='subjects.subject', verbose_name='subject')),
            ],
            options={
                'verbose_name': 'professor subject information',
                'verbose_name_plural': 'professor subjects information',
                'db_table': 'x_professor_subject',
            },
        ),
        migrations.AddField(
            model_name='professor',
            name='work_status',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='professors.workstatus', verbose_name='work status'),
        ),
    ]
