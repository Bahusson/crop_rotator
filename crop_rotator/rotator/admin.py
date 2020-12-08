from django.contrib import admin

# Register your models here.
from .models import (
 RotationPlan, CropFamily, Crop, CropMix, RotationStep, CropTag)

admin.site.register(RotationPlan)
admin.site.register(CropFamily)
admin.site.register(Crop)
admin.site.register(CropMix)
admin.site.register(RotationStep)
admin.site.register(CropTag)
