from django.urls import path
from . import views

urlpatterns = [
    path("allplans", views.allplans, name="allplans"),
    path("plan/<int:plan_id>/", views.plan, name="plan"),
    path("lurk_plan/<int:plan_id>/", views.lurk_plan, name="lurk_plan"),
    path("my_plans", views.my_plans, name="my_plans"),
    path("plan_edit/<int:plan_id>", views.plan_edit, name="plan_edit"),
    path("step/<int:step_id>", views.step, name="step"),
    path("plan_evaluated/<int:plan_id>/", views.plan_evaluated, name="plan_evaluated"),
]
