# Generated by Django 3.1.5 on 2021-02-09 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rotator', '0042_auto_20210204_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='crop',
            name='latin_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
