from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("allplans", views.allplans, name="allplans"),
    path("plan/<int:plan_id>/", views.plan, name="plan"),
    path("crop/<int:crop_id>/", views.crop, name="crop"),
    path("family/<int:family_id>/", views.family, name="family"),
    path("new_plan", views.new_plan, name="new_plan"),
]
