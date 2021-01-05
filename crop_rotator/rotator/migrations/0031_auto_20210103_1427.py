# Generated by Django 3.1.3 on 2021-01-03 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rotator', '0030_auto_20210103_1425'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cropdatasource',
            name='from_interaction',
        ),
        migrations.AddField(
            model_name='cropinteraction',
            name='info_source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='info_source_set', to='rotator.cropdatasource'),
        ),
    ]