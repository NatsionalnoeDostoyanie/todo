# Generated by Django 4.2.4 on 2023-11-25 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0006_rename_date_last_modified_task_date_updated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='date_postponed',
            new_name='postponed_date',
        ),
    ]
