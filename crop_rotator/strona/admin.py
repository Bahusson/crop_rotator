from django.contrib import admin

# Register your models here.
from .models import(
    PageNames,
    RegNames,
    PageSkin,
    AboutPageNames,
    RotatorEditorPageNames,
    FertilizerPageNames,
    BasicElement,
    Fertilizer,
    FertilizerDataSource,
    ElementDataString,
)


admin.site.register(PageNames)
admin.site.register(RegNames)
admin.site.register(PageSkin)
admin.site.register(AboutPageNames)
admin.site.register(RotatorEditorPageNames)
admin.site.register(FertilizerPageNames)
admin.site.register(BasicElement)
admin.site.register(Fertilizer)
admin.site.register(FertilizerDataSource)
admin.site.register(ElementDataString)
