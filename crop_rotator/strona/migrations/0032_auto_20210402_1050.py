# Generated by Django 3.1.5 on 2021-04-02 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0031_auto_20210402_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='rotatoreditorpagenames',
            name='add_element',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='rotatoreditorpagenames',
            name='add_element_en',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='rotatoreditorpagenames',
            name='add_element_pl',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='rotatoreditorpagenames',
            name='remove_element',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='rotatoreditorpagenames',
            name='remove_element_en',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='rotatoreditorpagenames',
            name='remove_element_pl',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='rotatoreditorpagenames',
            name='return_to_plan',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='rotatoreditorpagenames',
            name='return_to_plan_en',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='rotatoreditorpagenames',
            name='return_to_plan_pl',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]