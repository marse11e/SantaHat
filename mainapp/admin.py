from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import PhotoEdit

@admin.register(PhotoEdit)
class PhotoEditAdmin(admin.ModelAdmin):
    list_display = ['photo', 'id']
    list_filter = ['created_at',]
    search_fields = ['created_at']
    
        
    def photo(self, obj):
        if obj.image:
            return mark_safe(
                f'<img src="{obj.image.url}" width="100" height="100">')
        else:
            return 'Нет фото'