# Generated by Django 5.1.7 on 2025-03-25 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_band_like_new'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='like_new',
        ),
    ]
