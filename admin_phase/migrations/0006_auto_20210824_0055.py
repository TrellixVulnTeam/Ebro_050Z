# Generated by Django 3.1.7 on 2021-08-23 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_phase', '0005_offerbook_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offerbook',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_phase.products'),
        ),
    ]
