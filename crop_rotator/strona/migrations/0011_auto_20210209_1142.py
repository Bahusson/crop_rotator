# Generated by Django 3.1.5 on 2021-02-09 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0010_auto_20210208_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='rotatoreditorpagenames',
            name='family',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='rotatoreditorpagenames',
            name='family_en',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='rotatoreditorpagenames',
            name='family_pl',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='rotatoreditorpagenames',
            name='sources',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='rotatoreditorpagenames',
            name='sources_en',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='rotatoreditorpagenames',
            name='sources_pl',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='rotatoreditorpagenames',
            name='species',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='rotatoreditorpagenames',
            name='species_en',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='rotatoreditorpagenames',
            name='species_pl',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]