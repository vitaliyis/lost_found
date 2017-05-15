from django.contrib import admin
from .models import *

class CityAdmin(admin.ModelAdmin):
    list_display = [field.name for field in City._meta.fields]

    class Meta:
        model = City

admin.site.register(City, CityAdmin)

class CountryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Country._meta.fields]

    class Meta:
        model = Country

admin.site.register(Country, CountryAdmin)

class MarkAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Mark._meta.fields]

    class Meta:
        model = Mark

admin.site.register(Mark, MarkAdmin)

class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]

    class Meta:
        model = Status

admin.site.register(Status, StatusAdmin)

class StatementAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Statement._meta.fields]

    class Meta:
        model = Statement

admin.site.register(Statement, StatementAdmin)
