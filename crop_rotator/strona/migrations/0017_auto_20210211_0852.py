# Generated by Django 3.1.5 on 2021-02-11 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0016_auto_20210211_0756'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('latin_name', models.CharField(max_length=50)),
                ('symbol', models.CharField(max_length=2)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('is_trace_element', models.BooleanField(default=True)),
                ('descr', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ElementDataString',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('part1', models.CharField(blank=True, max_length=500, null=True)),
                ('link', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Fertilizer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('descr', models.TextField()),
                ('is_natural', models.BooleanField(default=False)),
                ('contains_elements', models.ManyToManyField(blank=True, related_name='contains_elements', to='strona.BasicElement')),
                ('image_source', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='set_image_eds_fertilizer', to='strona.elementdatastring')),
            ],
        ),
        migrations.CreateModel(
            name='FertilizerPageNames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('descr', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Fertilizer Page Names',
            },
        ),
        migrations.CreateModel(
            name='FertilizerDataSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('descr', models.TextField(blank=True, null=True)),
                ('pages_from', models.IntegerField(blank=True, null=True)),
                ('pages_to', models.IntegerField(blank=True, null=True)),
                ('at_data_string', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='element_data_string_set', to='strona.elementdatastring')),
                ('from_fertilizer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fertilizer_source_set', to='strona.fertilizer')),
            ],
            options={
                'ordering': ['from_fertilizer', 'title'],
            },
        ),
        migrations.AddField(
            model_name='basicelement',
            name='image_source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='set_image_eds_basic', to='strona.elementdatastring'),
        ),
    ]
