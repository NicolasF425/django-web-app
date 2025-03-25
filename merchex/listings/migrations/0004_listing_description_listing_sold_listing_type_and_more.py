# Generated by Django 5.1.7 on 2025-03-24 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_band_active_band_biography_band_genre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='description',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='sold',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='listing',
            name='type',
            field=models.CharField(choices=[('REC', 'Records'), ('CLO', 'Clothing'), ('POS', 'Poster'), ('MIS', 'Miscellaneous')], default='MIS', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='year_formed',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
