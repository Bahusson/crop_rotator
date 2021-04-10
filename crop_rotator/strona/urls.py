from django.urls import path
from . import views
from .views import (
    AllPlantFamilies,
    AllTags,
    AllCrops,
    InteractionPage,
    InteractionFamily,
    InteractionTag,
    )

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("about_sources", views.about_sources, name="about_sources"),
    path("crop/<int:crop_id>/", InteractionPage.as_view(), name="crop"),
    path("family/<int:crop_id>/", InteractionFamily.as_view(), name="family"),
    path(
     "all_plant_families", AllPlantFamilies.as_view(),
     name="all_plant_families"),
    path("tag/<int:crop_id>", InteractionTag.as_view(), name="tag"),
    path("all_tags", AllTags.as_view(), name="all_tags"),
    path("all_crops", AllCrops.as_view(), name="all_crops"),

]
