# Generated by Django 3.1.3 on 2020-12-08 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rotator', '0009_crop_takes_mix_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crop',
            name='takes_mix_level',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Nieznane'), (1, 'Niższe'), (2, 'Niższe-Średnie'), (3, 'Średnie'), (4, 'Średnie-Wyższe'), (5, 'Wyższe')], default=0),
        ),
    ]
