# Generated by Django 5.1.7 on 2025-06-12 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_remove_employeemodel_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeemodel',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='employeemodel',
            name='deleted_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='employeemodel',
            name='is_deleted',
            field=models.BooleanField(blank=True, default=None),
        ),
    ]
