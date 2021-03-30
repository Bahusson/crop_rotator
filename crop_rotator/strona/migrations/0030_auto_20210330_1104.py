# Generated by Django 3.1.5 on 2021-03-30 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0029_auto_20210328_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='rotatoreditorpagenames',
            name='analysis_by_text',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='rotatoreditorpagenames',
            name='analysis_by_text_en',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='rotatoreditorpagenames',
            name='analysis_by_text_pl',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='rotatoreditorpagenames',
            name='evaluate_button',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='rotatoreditorpagenames',
            name='evaluate_button_en',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='rotatoreditorpagenames',
            name='evaluate_button_pl',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
