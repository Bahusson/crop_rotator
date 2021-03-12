from django.urls import path
from . import views

urlpatterns = [
    path("rotator_admin", views.rotator_admin, name="rotator_admin"),
]
