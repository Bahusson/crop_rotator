# Generated by Django 3.1.5 on 2021-04-29 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rotator', '0016_auto_20210429_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cropinteraction',
            name='type_of_interaction',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Współrzędne'), (1, 'Allelopatyczne'), (2, 'Następcze'), (3, 'W drugim roku'), (4, 'W trzecim roku'), (5, 'W dwóch kolejnych latach')], default=0),
        ),
    ]
