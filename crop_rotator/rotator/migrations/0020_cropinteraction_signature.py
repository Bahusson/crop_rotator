# Generated by Django 3.1.5 on 2021-05-06 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rotator', '0019_cropinteraction_interaction_sign'),
    ]

    operations = [
        migrations.AddField(
            model_name='cropinteraction',
            name='signature',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]