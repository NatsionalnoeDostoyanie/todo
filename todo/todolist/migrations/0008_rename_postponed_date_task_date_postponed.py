# Generated by Django 4.2.4 on 2023-11-25 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0007_rename_date_postponed_task_postponed_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='postponed_date',
            new_name='date_postponed',
        ),
    ]
