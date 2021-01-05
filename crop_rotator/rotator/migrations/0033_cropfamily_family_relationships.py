# Generated by Django 3.1.3 on 2021-01-05 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rotator', '0032_auto_20210105_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='cropfamily',
            name='family_relationships',
            field=models.ManyToManyField(blank=True, related_name='known_family_interactions', to='rotator.FamilyInteraction'),
        ),
    ]
