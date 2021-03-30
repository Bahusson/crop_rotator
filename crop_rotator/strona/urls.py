from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("crop/<int:crop_id>/", views.crop, name="crop"),
    path("family/<int:family_id>/", views.family, name="family"),
    path("all_plant_families", views.all_plant_families, name="all_plant_families"),
    path("tag/<int:tag_id>", views.tag, name="tag"),
    path("all_tags", views.all_tags, name="all_tags"),
]
