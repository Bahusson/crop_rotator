# Generated by Django 3.1.3 on 2020-12-08 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rotator', '0008_auto_20201208_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='crop',
            name='takes_mix_level',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Nieznane'), (1, 'Niższe'), (2, 'Średnie'), (3, 'Wyższe')], default=0),
        ),
    ]
