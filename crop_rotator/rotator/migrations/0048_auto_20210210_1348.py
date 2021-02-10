# Generated by Django 3.1.5 on 2021-02-10 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rotator', '0047_cropimagessource'),
    ]

    operations = [
        migrations.AddField(
            model_name='crop',
            name='image_source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='set_image_cds', to='rotator.cropdatastring'),
        ),
        migrations.AlterField(
            model_name='crop',
            name='family',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='set_family', to='rotator.cropfamily'),
        ),
        migrations.DeleteModel(
            name='CropImagesSource',
        ),
    ]
