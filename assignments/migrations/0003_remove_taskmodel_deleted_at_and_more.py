# Generated by Django 5.1.7 on 2025-06-12 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0002_taskmodel_deleted_at_taskmodel_is_deleted_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskmodel',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='taskmodel',
            name='is_deleted',
        ),
    ]
