# Generated by Django 3.1.7 on 2021-04-26 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_phase', '0031_notifications'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notifications',
            old_name='product',
            new_name='username',
        ),
    ]
