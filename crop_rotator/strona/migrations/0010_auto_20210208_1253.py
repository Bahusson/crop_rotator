# Generated by Django 3.1.5 on 2021-02-08 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0009_auto_20210208_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='regnames',
            name='passwd_too_simple',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='regnames',
            name='passwd_too_simple_en',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='regnames',
            name='passwd_too_simple_pl',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='regnames',
            name='register',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='regnames',
            name='register_en',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='regnames',
            name='register_pl',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]