# Generated by Django 3.1.7 on 2021-08-23 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_phase', '0004_offerbook_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='offerbook',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
