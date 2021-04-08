from django.urls import path
from . import views
from .views import (
    AllCropsAdmin,
    AllFamiliesAdmin,
    AllTagsAdmin,
    CropAdmin,
    FamilyAdmin,
    TagAdmin,
    )

urlpatterns = [
    path("rotator_admin", views.rotator_admin, name="rotator_admin"),
    path("all_crops_admin", AllCropsAdmin.as_view(), name="all_crops_admin"),
    path("all_families_admin", AllFamiliesAdmin.as_view(), name="all_families_admin"),
    path("all_tags_admin", AllTagsAdmin.as_view(), name="all_tags_admin"),
    path("crop_admin/<int:element_id>", CropAdmin.as_view(), name='crop_admin'),
    path("family_admin/<int:element_id>", FamilyAdmin.as_view(), name='family_admin'),
    path("tag_admin/<int:element_id>", TagAdmin.as_view(), name='tag_admin'),
]
