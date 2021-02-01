from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("allplans", views.allplans, name="allplans"),
    path("plan/<int:plan_id>/", views.plan, name="plan"),
    path("lurk_plan/<int:plan_id>/", views.lurk_plan, name="lurk_plan"),
    path("crop/<int:crop_id>/", views.crop, name="crop"),
    path("family/<int:family_id>/", views.family, name="family"),
    path("my_plans", views.my_plans, name="my_plans"),
    path("plan_edit/<int:plan_id>", views.plan_edit, name="plan_edit"),
    path("step/<int:step_id>", views.step, name="step")
]
