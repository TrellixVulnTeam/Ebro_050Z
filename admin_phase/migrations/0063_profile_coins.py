# Generated by Django 3.1.7 on 2021-05-31 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_phase', '0062_auto_20210531_0121'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='coins',
            field=models.BigIntegerField(blank=True, default='0', null=True),
        ),
    ]