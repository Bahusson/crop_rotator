from django.contrib import admin

# Register your models here.
from .models import PageNames, RegNames, PageSkin, AboutPageNames


admin.site.register(PageNames)
admin.site.register(RegNames)
admin.site.register(PageSkin)
admin.site.register(AboutPageNames)
