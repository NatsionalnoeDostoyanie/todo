# Generated by Django 4.2.4 on 2023-11-09 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0004_task_date_postponed_task_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='is_complete',
        ),
    ]
