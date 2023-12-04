# Generated by Django 4.2.4 on 2023-12-04 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0010_alter_task_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('done', 'Выполнено'), ('in_progress', 'В процессе выполнения'), ('postponed', 'Отложено')], default='in_progress', max_length=11),
        ),
    ]