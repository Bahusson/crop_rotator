# Generated by Django 3.1.3 on 2021-01-03 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rotator', '0029_auto_20210103_1425'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='familyinteraction',
            options={'ordering': ['title']},
        ),
    ]