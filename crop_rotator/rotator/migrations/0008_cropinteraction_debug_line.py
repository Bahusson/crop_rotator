# Generated by Django 3.1.5 on 2021-04-20 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rotator', '0007_auto_20210420_0642'),
    ]

    operations = [
        migrations.AddField(
            model_name='cropinteraction',
            name='debug_line',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]