from django.contrib import admin
from .models import *

class ThingCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ThingCategory._meta.fields]

    class Meta:
        model = ThingCategory

admin.site.register(ThingCategory, ThingCategoryAdmin)

class ThingAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Thing._meta.fields]

    class Meta:
        model = Thing

admin.site.register(Thing, ThingAdmin)