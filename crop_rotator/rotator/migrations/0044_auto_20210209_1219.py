# Generated by Django 3.1.5 on 2021-02-09 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rotator', '0043_crop_latin_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='cropdatasource',
            name='descr_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cropdatasource',
            name='descr_pl',
            field=models.TextField(blank=True, null=True),
        ),
    ]