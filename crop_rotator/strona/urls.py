from django.urls import path
from . import views
from .views import AllPlantFamilies, AllTags, AllCrops

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("crop/<int:crop_id>/", views.crop, name="crop"),
    path("family/<int:family_id>/", views.family, name="family"),
    path("all_plant_families", AllPlantFamilies.as_view(), name="all_plant_families"),
    path("tag/<int:tag_id>", views.tag, name="tag"),
    path("all_tags", AllTags.as_view(), name="all_tags"),
    path("all_crops", AllCrops.as_view(), name="all_crops"),

]
