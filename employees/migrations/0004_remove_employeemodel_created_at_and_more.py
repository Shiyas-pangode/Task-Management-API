# Generated by Django 5.1.7 on 2025-06-12 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_alter_employeemodel_assigned_to'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeemodel',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='employeemodel',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='employeemodel',
            name='is_deleted',
        ),
    ]
