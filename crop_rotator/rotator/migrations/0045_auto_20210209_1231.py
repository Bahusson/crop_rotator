# Generated by Django 3.1.5 on 2021-02-09 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rotator', '0044_auto_20210209_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='croptag',
            name='descr_en',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='croptag',
            name='descr_pl',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
