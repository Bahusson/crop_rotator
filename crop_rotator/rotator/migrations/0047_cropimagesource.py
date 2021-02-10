# Generated by Django 3.1.5 on 2021-02-10 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rotator', '0046_auto_20210209_1239'),
    ]

    operations = [
        migrations.CreateModel(
            name='CropImageSource',
            fields=[
                ('cropdatasource_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='rotator.cropdatasource')),
            ],
            options={
                'ordering': ['-from_crop', 'title'],
            },
            bases=('rotator.cropdatasource',),
        ),
    ]
