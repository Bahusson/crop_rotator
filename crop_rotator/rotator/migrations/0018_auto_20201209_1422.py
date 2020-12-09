# Generated by Django 3.1.3 on 2020-12-09 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rotator', '0017_crop_seed_norm'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crop',
            old_name='seed_norm',
            new_name='seed_norm_max',
        ),
        migrations.AddField(
            model_name='crop',
            name='seed_norm_min',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
