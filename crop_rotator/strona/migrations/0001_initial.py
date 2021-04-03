# Generated by Django 3.1.5 on 2021-04-03 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPageNames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_project', models.TextField()),
                ('about_project_pl', models.TextField(null=True)),
                ('about_project_en', models.TextField(null=True)),
                ('send_email', models.CharField(max_length=200)),
                ('send_email_pl', models.CharField(max_length=200, null=True)),
                ('send_email_en', models.CharField(max_length=200, null=True)),
                ('gitter', models.CharField(max_length=200)),
                ('gitter_pl', models.CharField(max_length=200, null=True)),
                ('gitter_en', models.CharField(max_length=200, null=True)),
                ('github', models.CharField(max_length=200)),
                ('github_pl', models.CharField(max_length=200, null=True)),
                ('github_en', models.CharField(max_length=200, null=True)),
                ('login_to_see', models.CharField(max_length=200)),
                ('login_to_see_pl', models.CharField(max_length=200, null=True)),
                ('login_to_see_en', models.CharField(max_length=200, null=True)),
                ('curr_prog_includes', models.CharField(blank=True, max_length=40, null=True)),
                ('curr_prog_includes_pl', models.CharField(blank=True, max_length=40, null=True)),
                ('curr_prog_includes_en', models.CharField(blank=True, max_length=40, null=True)),
                ('over', models.CharField(blank=True, max_length=30, null=True)),
                ('over_pl', models.CharField(blank=True, max_length=30, null=True)),
                ('over_en', models.CharField(blank=True, max_length=30, null=True)),
                ('plants', models.CharField(blank=True, max_length=30, null=True)),
                ('plants_pl', models.CharField(blank=True, max_length=30, null=True)),
                ('plants_en', models.CharField(blank=True, max_length=30, null=True)),
                ('coming_from', models.CharField(blank=True, max_length=30, null=True)),
                ('coming_from_pl', models.CharField(blank=True, max_length=30, null=True)),
                ('coming_from_en', models.CharField(blank=True, max_length=30, null=True)),
                ('families', models.CharField(blank=True, max_length=30, null=True)),
                ('families_pl', models.CharField(blank=True, max_length=30, null=True)),
                ('families_en', models.CharField(blank=True, max_length=30, null=True)),
                ('marked_by', models.CharField(blank=True, max_length=30, null=True)),
                ('marked_by_pl', models.CharField(blank=True, max_length=30, null=True)),
                ('marked_by_en', models.CharField(blank=True, max_length=30, null=True)),
                ('categories', models.CharField(blank=True, max_length=30, null=True)),
                ('categories_pl', models.CharField(blank=True, max_length=30, null=True)),
                ('categories_en', models.CharField(blank=True, max_length=30, null=True)),
                ('and_over', models.CharField(blank=True, max_length=30, null=True)),
                ('and_over_pl', models.CharField(blank=True, max_length=30, null=True)),
                ('and_over_en', models.CharField(blank=True, max_length=30, null=True)),
                ('unique_interactions', models.CharField(blank=True, max_length=30, null=True)),
                ('unique_interactions_pl', models.CharField(blank=True, max_length=30, null=True)),
                ('unique_interactions_en', models.CharField(blank=True, max_length=30, null=True)),
                ('described_by', models.CharField(blank=True, max_length=30, null=True)),
                ('described_by_pl', models.CharField(blank=True, max_length=30, null=True)),
                ('described_by_en', models.CharField(blank=True, max_length=30, null=True)),
                ('sources', models.CharField(blank=True, max_length=30, null=True)),
                ('sources_pl', models.CharField(blank=True, max_length=30, null=True)),
                ('sources_en', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'verbose_name_plural': 'About Page Names',
            },
        ),
        migrations.CreateModel(
            name='BasicElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('name_pl', models.CharField(max_length=50, null=True)),
                ('name_en', models.CharField(max_length=50, null=True)),
                ('latin_name', models.CharField(max_length=50)),
                ('symbol', models.CharField(max_length=2)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('is_trace_element', models.BooleanField(default=True)),
                ('descr', models.TextField()),
                ('descr_pl', models.TextField(null=True)),
                ('descr_en', models.TextField(null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ElementDataString',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('title_pl', models.CharField(max_length=150, null=True)),
                ('title_en', models.CharField(max_length=150, null=True)),
                ('part1', models.CharField(blank=True, max_length=500, null=True)),
                ('part1_pl', models.CharField(blank=True, max_length=500, null=True)),
                ('part1_en', models.CharField(blank=True, max_length=500, null=True)),
                ('link', models.CharField(blank=True, max_length=500, null=True)),
                ('link_pl', models.CharField(blank=True, max_length=500, null=True)),
                ('link_en', models.CharField(blank=True, max_length=500, null=True)),
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
                ('name_pl', models.CharField(max_length=50, null=True)),
                ('name_en', models.CharField(max_length=50, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('descr', models.TextField()),
                ('descr_pl', models.TextField(null=True)),
                ('descr_en', models.TextField(null=True)),
                ('is_natural', models.BooleanField(default=False)),
                ('contains_elements', models.ManyToManyField(blank=True, related_name='contains_elements', to='strona.BasicElement')),
                ('image_source', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='set_image_eds_fertilizer', to='strona.elementdatastring')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='FertilizerPageNames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('title_pl', models.CharField(max_length=50, null=True)),
                ('title_en', models.CharField(max_length=50, null=True)),
                ('descr', models.TextField()),
                ('descr_pl', models.TextField(null=True)),
                ('descr_en', models.TextField(null=True)),
                ('elements_head', models.CharField(blank=True, max_length=50, null=True)),
                ('elements_head_pl', models.CharField(blank=True, max_length=50, null=True)),
                ('elements_head_en', models.CharField(blank=True, max_length=50, null=True)),
                ('makro_head', models.CharField(blank=True, max_length=50, null=True)),
                ('makro_head_pl', models.CharField(blank=True, max_length=50, null=True)),
                ('makro_head_en', models.CharField(blank=True, max_length=50, null=True)),
                ('makro_descr', models.TextField(blank=True, null=True)),
                ('makro_descr_pl', models.TextField(blank=True, null=True)),
                ('makro_descr_en', models.TextField(blank=True, null=True)),
                ('micro_head', models.CharField(blank=True, max_length=50, null=True)),
                ('micro_head_pl', models.CharField(blank=True, max_length=50, null=True)),
                ('micro_head_en', models.CharField(blank=True, max_length=50, null=True)),
                ('micro_descr', models.TextField(blank=True, null=True)),
                ('micro_descr_pl', models.TextField(blank=True, null=True)),
                ('micro_descr_en', models.TextField(blank=True, null=True)),
                ('fertilizers_head', models.CharField(blank=True, max_length=50, null=True)),
                ('fertilizers_head_pl', models.CharField(blank=True, max_length=50, null=True)),
                ('fertilizers_head_en', models.CharField(blank=True, max_length=50, null=True)),
                ('natural_fertilizers_head', models.CharField(blank=True, max_length=50, null=True)),
                ('natural_fertilizers_head_pl', models.CharField(blank=True, max_length=50, null=True)),
                ('natural_fertilizers_head_en', models.CharField(blank=True, max_length=50, null=True)),
                ('natural_fertilizers_descr', models.TextField(blank=True, null=True)),
                ('natural_fertilizers_descr_pl', models.TextField(blank=True, null=True)),
                ('natural_fertilizers_descr_en', models.TextField(blank=True, null=True)),
                ('artificial_fertilizers_head', models.CharField(blank=True, max_length=50, null=True)),
                ('artificial_fertilizers_head_pl', models.CharField(blank=True, max_length=50, null=True)),
                ('artificial_fertilizers_head_en', models.CharField(blank=True, max_length=50, null=True)),
                ('artificial_fertilizers_descr', models.TextField(blank=True, null=True)),
                ('artificial_fertilizers_descr_pl', models.TextField(blank=True, null=True)),
                ('artificial_fertilizers_descr_en', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Fertilizer Page Names',
            },
        ),
        migrations.CreateModel(
            name='PageNames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang_flag', models.ImageField(upload_to='images')),
                ('lang_flag_pl', models.ImageField(null=True, upload_to='images')),
                ('lang_flag_en', models.ImageField(null=True, upload_to='images')),
                ('lang_flag_id', models.CharField(blank=True, max_length=20, null=True)),
                ('lang_flag_id_pl', models.CharField(blank=True, max_length=20, null=True)),
                ('lang_flag_id_en', models.CharField(blank=True, max_length=20, null=True)),
                ('headtitle', models.CharField(max_length=200)),
                ('headtitle_pl', models.CharField(max_length=200, null=True)),
                ('headtitle_en', models.CharField(max_length=200, null=True)),
                ('mainpage', models.CharField(max_length=200)),
                ('mainpage_pl', models.CharField(max_length=200, null=True)),
                ('mainpage_en', models.CharField(max_length=200, null=True)),
                ('all_plants', models.CharField(blank=True, max_length=200, null=True)),
                ('all_plants_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('all_plants_en', models.CharField(blank=True, max_length=200, null=True)),
                ('about', models.CharField(max_length=200)),
                ('about_pl', models.CharField(max_length=200, null=True)),
                ('about_en', models.CharField(max_length=200, null=True)),
                ('contact', models.CharField(max_length=200)),
                ('contact_pl', models.CharField(max_length=200, null=True)),
                ('contact_en', models.CharField(max_length=200, null=True)),
                ('logout', models.CharField(max_length=200)),
                ('logout_pl', models.CharField(max_length=200, null=True)),
                ('logout_en', models.CharField(max_length=200, null=True)),
                ('login', models.CharField(max_length=200)),
                ('login_pl', models.CharField(max_length=200, null=True)),
                ('login_en', models.CharField(max_length=200, null=True)),
                ('register', models.CharField(max_length=50)),
                ('register_pl', models.CharField(max_length=50, null=True)),
                ('register_en', models.CharField(max_length=50, null=True)),
                ('my_plans', models.CharField(blank=True, max_length=200, null=True)),
                ('my_plans_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('my_plans_en', models.CharField(blank=True, max_length=200, null=True)),
                ('all_plans', models.CharField(blank=True, max_length=200, null=True)),
                ('all_plans_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('all_plans_en', models.CharField(blank=True, max_length=200, null=True)),
                ('see_more', models.CharField(blank=True, max_length=200, null=True)),
                ('see_more_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('see_more_en', models.CharField(blank=True, max_length=200, null=True)),
                ('of_steps', models.CharField(blank=True, max_length=200, null=True)),
                ('of_steps_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('of_steps_en', models.CharField(blank=True, max_length=200, null=True)),
                ('of_plants', models.CharField(blank=True, max_length=200, null=True)),
                ('of_plants_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('of_plants_en', models.CharField(blank=True, max_length=200, null=True)),
                ('by_crops', models.CharField(blank=True, max_length=50, null=True)),
                ('by_crops_pl', models.CharField(blank=True, max_length=50, null=True)),
                ('by_crops_en', models.CharField(blank=True, max_length=50, null=True)),
                ('by_families', models.CharField(blank=True, max_length=50, null=True)),
                ('by_families_pl', models.CharField(blank=True, max_length=50, null=True)),
                ('by_families_en', models.CharField(blank=True, max_length=50, null=True)),
                ('by_tags', models.CharField(blank=True, max_length=50, null=True)),
                ('by_tags_pl', models.CharField(blank=True, max_length=50, null=True)),
                ('by_tags_en', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'Page Names',
            },
        ),
        migrations.CreateModel(
            name='PageSkin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('themetitle', models.CharField(max_length=200)),
                ('position', models.IntegerField()),
                ('planimagedefault', models.ImageField(blank=True, null=True, upload_to='skins')),
                ('rotatorlogo_main', models.ImageField(blank=True, null=True, upload_to='skins')),
            ],
            options={
                'verbose_name_plural': 'Page Skins',
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='RegNames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(blank=True, max_length=50, null=True)),
                ('password_pl', models.CharField(blank=True, max_length=50, null=True)),
                ('password_en', models.CharField(blank=True, max_length=50, null=True)),
                ('re_password', models.CharField(blank=True, max_length=50, null=True)),
                ('re_password_pl', models.CharField(blank=True, max_length=50, null=True)),
                ('re_password_en', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('name_pl', models.CharField(blank=True, max_length=50, null=True)),
                ('name_en', models.CharField(blank=True, max_length=50, null=True)),
                ('refresh', models.CharField(blank=True, max_length=50, null=True)),
                ('refresh_pl', models.CharField(blank=True, max_length=50, null=True)),
                ('refresh_en', models.CharField(blank=True, max_length=50, null=True)),
                ('passwd_too_simple', models.CharField(blank=True, max_length=250, null=True)),
                ('passwd_too_simple_pl', models.CharField(blank=True, max_length=250, null=True)),
                ('passwd_too_simple_en', models.CharField(blank=True, max_length=250, null=True)),
                ('register', models.CharField(blank=True, max_length=50, null=True)),
                ('register_pl', models.CharField(blank=True, max_length=50, null=True)),
                ('register_en', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'Registry Names',
            },
        ),
        migrations.CreateModel(
            name='RotatorEditorPageNames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_plan', models.CharField(max_length=200)),
                ('new_plan_pl', models.CharField(max_length=200, null=True)),
                ('new_plan_en', models.CharField(max_length=200, null=True)),
                ('new_step', models.CharField(max_length=200)),
                ('new_step_pl', models.CharField(max_length=200, null=True)),
                ('new_step_en', models.CharField(max_length=200, null=True)),
                ('name_plan', models.CharField(max_length=200)),
                ('name_plan_pl', models.CharField(max_length=200, null=True)),
                ('name_plan_en', models.CharField(max_length=200, null=True)),
                ('name_step', models.CharField(max_length=200)),
                ('name_step_pl', models.CharField(max_length=200, null=True)),
                ('name_step_en', models.CharField(max_length=200, null=True)),
                ('plan_remove', models.CharField(max_length=200)),
                ('plan_remove_pl', models.CharField(max_length=200, null=True)),
                ('plan_remove_en', models.CharField(max_length=200, null=True)),
                ('step_remove', models.CharField(max_length=200)),
                ('step_remove_pl', models.CharField(max_length=200, null=True)),
                ('step_remove_en', models.CharField(max_length=200, null=True)),
                ('remove_warning', models.CharField(blank=True, max_length=200, null=True)),
                ('remove_warning_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('remove_warning_en', models.CharField(blank=True, max_length=200, null=True)),
                ('remove_permanent', models.CharField(blank=True, max_length=200, null=True)),
                ('remove_permanent_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('remove_permanent_en', models.CharField(blank=True, max_length=200, null=True)),
                ('dont_remove', models.CharField(blank=True, max_length=200, null=True)),
                ('dont_remove_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('dont_remove_en', models.CharField(blank=True, max_length=200, null=True)),
                ('editme', models.CharField(max_length=200)),
                ('editme_pl', models.CharField(max_length=200, null=True)),
                ('editme_en', models.CharField(max_length=200, null=True)),
                ('switch_places', models.CharField(max_length=200)),
                ('switch_places_pl', models.CharField(max_length=200, null=True)),
                ('switch_places_en', models.CharField(max_length=200, null=True)),
                ('switch_with', models.CharField(max_length=200)),
                ('switch_with_pl', models.CharField(max_length=200, null=True)),
                ('switch_with_en', models.CharField(max_length=200, null=True)),
                ('switch_text', models.CharField(max_length=200)),
                ('switch_text_pl', models.CharField(max_length=200, null=True)),
                ('switch_text_en', models.CharField(max_length=200, null=True)),
                ('u_edit_step_no', models.CharField(max_length=200)),
                ('u_edit_step_no_pl', models.CharField(max_length=200, null=True)),
                ('u_edit_step_no_en', models.CharField(max_length=200, null=True)),
                ('title', models.CharField(max_length=200)),
                ('title_pl', models.CharField(max_length=200, null=True)),
                ('title_en', models.CharField(max_length=200, null=True)),
                ('descr', models.CharField(max_length=200)),
                ('descr_pl', models.CharField(max_length=200, null=True)),
                ('descr_en', models.CharField(max_length=200, null=True)),
                ('early_crop', models.CharField(max_length=200)),
                ('early_crop_pl', models.CharField(max_length=200, null=True)),
                ('early_crop_en', models.CharField(max_length=200, null=True)),
                ('middle_crop', models.CharField(blank=True, max_length=200, null=True)),
                ('middle_crop_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('middle_crop_en', models.CharField(blank=True, max_length=200, null=True)),
                ('late_crop', models.CharField(max_length=200)),
                ('late_crop_pl', models.CharField(max_length=200, null=True)),
                ('late_crop_en', models.CharField(max_length=200, null=True)),
                ('destroy_early_crop', models.CharField(max_length=200)),
                ('destroy_early_crop_pl', models.CharField(max_length=200, null=True)),
                ('destroy_early_crop_en', models.CharField(max_length=200, null=True)),
                ('destroy_middle_crop', models.CharField(blank=True, max_length=200, null=True)),
                ('destroy_middle_crop_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('destroy_middle_crop_en', models.CharField(blank=True, max_length=200, null=True)),
                ('destroy_late_crop', models.CharField(max_length=200)),
                ('destroy_late_crop_pl', models.CharField(max_length=200, null=True)),
                ('destroy_late_crop_en', models.CharField(max_length=200, null=True)),
                ('add_fertilizer', models.CharField(max_length=200)),
                ('add_fertilizer_pl', models.CharField(max_length=200, null=True)),
                ('add_fertilizer_en', models.CharField(max_length=200, null=True)),
                ('add_fertilizer_onhover', models.CharField(max_length=800)),
                ('add_fertilizer_onhover_pl', models.CharField(max_length=800, null=True)),
                ('add_fertilizer_onhover_en', models.CharField(max_length=800, null=True)),
                ('change', models.CharField(max_length=200)),
                ('change_pl', models.CharField(max_length=200, null=True)),
                ('change_en', models.CharField(max_length=200, null=True)),
                ('publish', models.CharField(blank=True, max_length=200, null=True)),
                ('publish_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('publish_en', models.CharField(blank=True, max_length=200, null=True)),
                ('unpublish', models.CharField(blank=True, max_length=200, null=True)),
                ('unpublish_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('unpublish_en', models.CharField(blank=True, max_length=200, null=True)),
                ('publish_text', models.CharField(blank=True, max_length=200, null=True)),
                ('publish_text_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('publish_text_en', models.CharField(blank=True, max_length=200, null=True)),
                ('unpublish_text', models.CharField(blank=True, max_length=200, null=True)),
                ('unpublish_text_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('unpublish_text_en', models.CharField(blank=True, max_length=200, null=True)),
                ('publish_onhover', models.CharField(blank=True, max_length=900, null=True)),
                ('publish_onhover_pl', models.CharField(blank=True, max_length=900, null=True)),
                ('publish_onhover_en', models.CharField(blank=True, max_length=900, null=True)),
                ('unpublish_onhover', models.CharField(blank=True, max_length=900, null=True)),
                ('unpublish_onhover_pl', models.CharField(blank=True, max_length=900, null=True)),
                ('unpublish_onhover_en', models.CharField(blank=True, max_length=900, null=True)),
                ('more_info', models.CharField(blank=True, max_length=900, null=True)),
                ('more_info_pl', models.CharField(blank=True, max_length=900, null=True)),
                ('more_info_en', models.CharField(blank=True, max_length=900, null=True)),
                ('option_select', models.CharField(blank=True, max_length=200, null=True)),
                ('option_select_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('option_select_en', models.CharField(blank=True, max_length=200, null=True)),
                ('in_this_plan', models.CharField(blank=True, max_length=200, null=True)),
                ('in_this_plan_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('in_this_plan_en', models.CharField(blank=True, max_length=200, null=True)),
                ('fabs_and', models.CharField(blank=True, max_length=200, null=True)),
                ('fabs_and_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('fabs_and_en', models.CharField(blank=True, max_length=200, null=True)),
                ('should_be_fabs', models.CharField(blank=True, max_length=200, null=True)),
                ('should_be_fabs_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('should_be_fabs_en', models.CharField(blank=True, max_length=200, null=True)),
                ('error_len', models.CharField(blank=True, max_length=200, null=True)),
                ('error_len_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('error_len_en', models.CharField(blank=True, max_length=200, null=True)),
                ('len_required', models.CharField(blank=True, max_length=200, null=True)),
                ('len_required_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('len_required_en', models.CharField(blank=True, max_length=200, null=True)),
                ('remove_or_add', models.CharField(blank=True, max_length=200, null=True)),
                ('remove_or_add_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('remove_or_add_en', models.CharField(blank=True, max_length=200, null=True)),
                ('plan_limit_reached', models.TextField(blank=True, null=True)),
                ('plan_limit_reached_pl', models.TextField(blank=True, null=True)),
                ('plan_limit_reached_en', models.TextField(blank=True, null=True)),
                ('family', models.CharField(blank=True, max_length=200, null=True)),
                ('family_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('family_en', models.CharField(blank=True, max_length=200, null=True)),
                ('species', models.CharField(blank=True, max_length=200, null=True)),
                ('species_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('species_en', models.CharField(blank=True, max_length=200, null=True)),
                ('sources', models.CharField(blank=True, max_length=200, null=True)),
                ('sources_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('sources_en', models.CharField(blank=True, max_length=200, null=True)),
                ('notes', models.CharField(blank=True, max_length=200, null=True)),
                ('notes_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('notes_en', models.CharField(blank=True, max_length=200, null=True)),
                ('allelopatic_conflict', models.CharField(blank=True, max_length=200, null=True)),
                ('allelopatic_conflict_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('allelopatic_conflict_en', models.CharField(blank=True, max_length=200, null=True)),
                ('harms', models.CharField(blank=True, max_length=200, null=True)),
                ('harms_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('harms_en', models.CharField(blank=True, max_length=200, null=True)),
                ('in_step', models.CharField(blank=True, max_length=200, null=True)),
                ('in_step_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('in_step_en', models.CharField(blank=True, max_length=200, null=True)),
                ('well_cooperates', models.CharField(blank=True, max_length=200, null=True)),
                ('well_cooperates_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('well_cooperates_en', models.CharField(blank=True, max_length=200, null=True)),
                ('collides', models.CharField(blank=True, max_length=200, null=True)),
                ('collides_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('collides_en', models.CharField(blank=True, max_length=200, null=True)),
                ('image_source', models.CharField(blank=True, max_length=200, null=True)),
                ('image_source_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('image_source_en', models.CharField(blank=True, max_length=200, null=True)),
                ('add_fertilizer_main', models.CharField(blank=True, max_length=200, null=True)),
                ('add_fertilizer_main_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('add_fertilizer_main_en', models.CharField(blank=True, max_length=200, null=True)),
                ('add_fertilizer_onhover_main', models.CharField(blank=True, max_length=300, null=True)),
                ('add_fertilizer_onhover_main_pl', models.CharField(blank=True, max_length=300, null=True)),
                ('add_fertilizer_onhover_main_en', models.CharField(blank=True, max_length=300, null=True)),
                ('infl_type', models.CharField(blank=True, max_length=100, null=True)),
                ('infl_type_pl', models.CharField(blank=True, max_length=100, null=True)),
                ('infl_type_en', models.CharField(blank=True, max_length=100, null=True)),
                ('companion', models.CharField(blank=True, max_length=100, null=True)),
                ('companion_pl', models.CharField(blank=True, max_length=100, null=True)),
                ('companion_en', models.CharField(blank=True, max_length=100, null=True)),
                ('following', models.CharField(blank=True, max_length=100, null=True)),
                ('following_pl', models.CharField(blank=True, max_length=100, null=True)),
                ('following_en', models.CharField(blank=True, max_length=100, null=True)),
                ('allelopatic', models.CharField(blank=True, max_length=150, null=True)),
                ('allelopatic_pl', models.CharField(blank=True, max_length=150, null=True)),
                ('allelopatic_en', models.CharField(blank=True, max_length=150, null=True)),
                ('source_button', models.CharField(blank=True, max_length=50, null=True)),
                ('source_button_pl', models.CharField(blank=True, max_length=50, null=True)),
                ('source_button_en', models.CharField(blank=True, max_length=50, null=True)),
                ('known_interactions', models.CharField(blank=True, max_length=200, null=True)),
                ('known_interactions_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('known_interactions_en', models.CharField(blank=True, max_length=200, null=True)),
                ('plant_to_other', models.CharField(blank=True, max_length=200, null=True)),
                ('plant_to_other_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('plant_to_other_en', models.CharField(blank=True, max_length=200, null=True)),
                ('other_to_plant', models.CharField(blank=True, max_length=200, null=True)),
                ('other_to_plant_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('other_to_plant_en', models.CharField(blank=True, max_length=200, null=True)),
                ('family_to_other', models.CharField(blank=True, max_length=200, null=True)),
                ('family_to_other_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('family_to_other_en', models.CharField(blank=True, max_length=200, null=True)),
                ('other_to_family', models.CharField(blank=True, max_length=200, null=True)),
                ('other_to_family_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('other_to_family_en', models.CharField(blank=True, max_length=200, null=True)),
                ('category_to_other', models.CharField(blank=True, max_length=200, null=True)),
                ('category_to_other_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('category_to_other_en', models.CharField(blank=True, max_length=200, null=True)),
                ('other_to_category', models.CharField(blank=True, max_length=200, null=True)),
                ('other_to_category_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('other_to_category_en', models.CharField(blank=True, max_length=200, null=True)),
                ('annual', models.CharField(blank=True, max_length=50, null=True)),
                ('annual_pl', models.CharField(blank=True, max_length=50, null=True)),
                ('annual_en', models.CharField(blank=True, max_length=50, null=True)),
                ('perennial', models.CharField(blank=True, max_length=50, null=True)),
                ('perennial_pl', models.CharField(blank=True, max_length=50, null=True)),
                ('perennial_en', models.CharField(blank=True, max_length=50, null=True)),
                ('evaluate_button', models.CharField(blank=True, max_length=50, null=True)),
                ('evaluate_button_pl', models.CharField(blank=True, max_length=50, null=True)),
                ('evaluate_button_en', models.CharField(blank=True, max_length=50, null=True)),
                ('analysis_by_text', models.CharField(blank=True, max_length=200, null=True)),
                ('analysis_by_text_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('analysis_by_text_en', models.CharField(blank=True, max_length=200, null=True)),
                ('remove_element', models.CharField(blank=True, max_length=50, null=True)),
                ('remove_element_pl', models.CharField(blank=True, max_length=50, null=True)),
                ('remove_element_en', models.CharField(blank=True, max_length=50, null=True)),
                ('add_element', models.CharField(blank=True, max_length=50, null=True)),
                ('add_element_pl', models.CharField(blank=True, max_length=50, null=True)),
                ('add_element_en', models.CharField(blank=True, max_length=50, null=True)),
                ('return_to_plan', models.CharField(blank=True, max_length=50, null=True)),
                ('return_to_plan_pl', models.CharField(blank=True, max_length=50, null=True)),
                ('return_to_plan_en', models.CharField(blank=True, max_length=50, null=True)),
                ('categories', models.CharField(blank=True, max_length=50, null=True)),
                ('categories_pl', models.CharField(blank=True, max_length=50, null=True)),
                ('categories_en', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'Rotator Editor Page Names',
            },
        ),
        migrations.CreateModel(
            name='FertilizerDataSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('title_pl', models.CharField(max_length=150, null=True)),
                ('title_en', models.CharField(max_length=150, null=True)),
                ('descr', models.TextField(blank=True, null=True)),
                ('descr_pl', models.TextField(blank=True, null=True)),
                ('descr_en', models.TextField(blank=True, null=True)),
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
