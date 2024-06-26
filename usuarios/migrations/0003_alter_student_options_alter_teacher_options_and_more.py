# Generated by Django 5.0.4 on 2024-04-29 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_student_teacher'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={},
        ),
        migrations.AlterModelOptions(
            name='usern',
            options={},
        ),
        migrations.AlterModelManagers(
            name='student',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='teacher',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='usern',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='usern',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='usern',
            name='username',
        ),
        migrations.AlterField(
            model_name='usern',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='usern',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='usern',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='staff status'),
        ),
        migrations.AlterField(
            model_name='usern',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='last name'),
        ),
    ]
