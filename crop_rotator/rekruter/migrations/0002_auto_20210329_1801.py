# Generated by Django 3.1.5 on 2021-03-29 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rekruter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rotationplan',
            name='title_en',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='rotationplan',
            name='title_pl',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='rotationstep',
            name='descr_en',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='rotationstep',
            name='descr_pl',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='rotationstep',
            name='title_en',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='rotationstep',
            name='title_pl',
            field=models.CharField(max_length=150, null=True),
        ),
    ]