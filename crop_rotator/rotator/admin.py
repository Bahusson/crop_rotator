from django.contrib import admin

# Register your models here.
from .models import (
 RotationPlan, CropFamily, Crop, CropMix, RotationStep, CropTag,
 CropDataSource, CropDataString, CropInteraction, FamilyInteraction,
 )

admin.site.register(RotationPlan)
admin.site.register(CropFamily)
admin.site.register(Crop)
admin.site.register(CropMix)
admin.site.register(RotationStep)
admin.site.register(CropTag)
admin.site.register(CropDataSource)
admin.site.register(CropDataString)
admin.site.register(CropInteraction)
admin.site.register(FamilyInteraction)
