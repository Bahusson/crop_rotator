# Generated by Django 3.1.5 on 2021-02-11 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0018_auto_20210211_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicelement',
            name='descr_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='basicelement',
            name='descr_pl',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='basicelement',
            name='name_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='basicelement',
            name='name_pl',
            field=models.CharField(max_length=50, null=True),
        ),
    ]