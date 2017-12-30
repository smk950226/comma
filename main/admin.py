from django.contrib import admin
from .models import ActPhoto
from django.utils.safestring import mark_safe

@admin.register(ActPhoto)
class ActPhotoAdmin(admin.ModelAdmin):
    list_display = ['img', 'site', 'year', 'date']
    list_display_links = ['img', 'site']

    def img(self, actphoto):
        if actphoto.photo:
            return mark_safe('<img src="{}" style="width: 75px;">'.format(actphoto.photo.url))
        return None