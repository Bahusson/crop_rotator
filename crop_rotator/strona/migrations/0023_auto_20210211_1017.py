# Generated by Django 3.1.5 on 2021-02-11 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0022_auto_20210211_0906'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basicelement',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='fertilizer',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='fertilizerpagenames',
            name='artificial_fertilizers_descr',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fertilizerpagenames',
            name='artificial_fertilizers_descr_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fertilizerpagenames',
            name='artificial_fertilizers_descr_pl',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fertilizerpagenames',
            name='artificial_fertilizers_head',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='fertilizerpagenames',
            name='artificial_fertilizers_head_en',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='fertilizerpagenames',
            name='artificial_fertilizers_head_pl',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='fertilizerpagenames',
            name='elements_head',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='fertilizerpagenames',
            name='elements_head_en',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='fertilizerpagenames',
            name='elements_head_pl',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='fertilizerpagenames',
            name='fertilizers_head',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='fertilizerpagenames',
            name='fertilizers_head_en',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='fertilizerpagenames',
            name='fertilizers_head_pl',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='fertilizerpagenames',
            name='makro_descr',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fertilizerpagenames',
            name='makro_descr_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fertilizerpagenames',
            name='makro_descr_pl',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fertilizerpagenames',
            name='makro_head',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='fertilizerpagenames',
            name='makro_head_en',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='fertilizerpagenames',
            name='makro_head_pl',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='fertilizerpagenames',
            name='micro_descr',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fertilizerpagenames',
            name='micro_descr_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fertilizerpagenames',
            name='micro_descr_pl',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fertilizerpagenames',
            name='micro_head',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='fertilizerpagenames',
            name='micro_head_en',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='fertilizerpagenames',
            name='micro_head_pl',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='fertilizerpagenames',
            name='natural_fertilizers_descr',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fertilizerpagenames',
            name='natural_fertilizers_descr_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fertilizerpagenames',
            name='natural_fertilizers_descr_pl',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fertilizerpagenames',
            name='natural_fertilizers_head',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='fertilizerpagenames',
            name='natural_fertilizers_head_en',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='fertilizerpagenames',
            name='natural_fertilizers_head_pl',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]