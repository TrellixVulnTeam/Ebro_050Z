# Generated by Django 3.1.7 on 2021-06-09 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_phase', '0084_categorys'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorys',
            name='domain_name',
            field=models.CharField(default='www.bichatravels.com', max_length=200),
        ),
        migrations.AddField(
            model_name='categorys',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]