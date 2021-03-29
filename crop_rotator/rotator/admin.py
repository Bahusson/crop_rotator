from django.contrib import admin

# Register your models here.
from .models import (
    CropFamily,
    Crop,
    CropMix,
    CropTag,
    CropDataSource,
    CropDataFamilySource,
    CropsInteraction,
    FamilyInteraction,
    TagsInteraction,
    CropBookString,
    CropImageString,

)

admin.site.register(CropFamily)
admin.site.register(Crop)
admin.site.register(CropMix)
admin.site.register(CropTag)
admin.site.register(CropDataSource)
admin.site.register(CropDataFamilySource)
admin.site.register(CropsInteraction)
admin.site.register(FamilyInteraction)
admin.site.register(TagsInteraction)
admin.site.register(CropBookString)
admin.site.register(CropImageString)
