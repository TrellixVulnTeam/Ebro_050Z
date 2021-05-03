# Generated by Django 3.1.7 on 2021-04-04 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_phase', '0014_deals_attachments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deals',
            name='attachments',
        ),
        migrations.AddField(
            model_name='attachments',
            name='deal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='admin_phase.deals'),
            preserve_default=False,
        ),
    ]
