from django.contrib import admin
from .models import *

class MessageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Message._meta.fields]

    class Meta:
        model = Message

admin.site.register(Message, MessageAdmin)