from django.contrib import admin

# Register your models here.
from .models import (
RotationPlan,
RotationStep,
)

admin.site.register(RotationPlan)
admin.site.register(RotationStep)
