# Generated by Django 3.1.5 on 2021-03-31 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rotator', '0061_auto_20210329_1756'),
    ]

    operations = [
        migrations.CreateModel(
            name='CropDataTagSource',
            fields=[
                ('cropdatasource_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='rotator.cropdatasource')),
                ('from_tag', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='crop_data_tag_source_set', to='rotator.croptag')),
            ],
            bases=('rotator.cropdatasource',),
        ),
    ]