# Generated by Django 3.1.5 on 2021-02-10 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0013_auto_20210209_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='rotatoreditorpagenames',
            name='image_source',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='rotatoreditorpagenames',
            name='image_source_en',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='rotatoreditorpagenames',
            name='image_source_pl',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
