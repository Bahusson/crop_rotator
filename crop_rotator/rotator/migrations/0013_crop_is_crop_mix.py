# Generated by Django 3.1.5 on 2021-04-24 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rotator', '0012_auto_20210424_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='crop',
            name='is_crop_mix',
            field=models.BooleanField(default=False),
        ),
    ]