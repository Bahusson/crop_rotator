# Generated by Django 3.1.3 on 2021-01-02 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rotator', '0022_cropdatasource_cropdatastring'),
    ]

    operations = [
        migrations.AddField(
            model_name='cropdatasource',
            name='pages_from',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cropdatasource',
            name='pages_to',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]