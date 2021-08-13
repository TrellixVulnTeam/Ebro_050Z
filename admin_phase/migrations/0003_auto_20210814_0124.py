# Generated by Django 3.1.7 on 2021-08-13 19:54

import cloudinary.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('admin_phase', '0002_assign_deal_assign_job_offerbook'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='publish',
        ),
        migrations.AddField(
            model_name='products',
            name='apresentacao',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='products',
            name='foto',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='foto'),
        ),
        migrations.AddField(
            model_name='products',
            name='nome',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
