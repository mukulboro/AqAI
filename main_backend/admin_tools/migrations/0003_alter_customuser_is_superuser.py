# Generated by Django 5.2.3 on 2025-06-28 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_tools', '0002_rename_is_user_customuser_is_public_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
