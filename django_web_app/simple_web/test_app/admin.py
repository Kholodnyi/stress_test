from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Entry


@admin.register(Entry)
class UserMainDataAdmin(ModelAdmin):
    list_display = ('amount', )
    search_fields = ('text', )
