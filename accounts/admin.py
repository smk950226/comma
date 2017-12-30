from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'group', 'univ', 'major']
    list_display_links = ['name', 'group', 'major']
    search_fields = ['name', 'major']
