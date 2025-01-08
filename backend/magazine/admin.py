from django.contrib import admin
from .models import Magazine

@admin.register(Magazine)
class MagazineAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'pdf_file', 'cover_image')
    list_filter = ('date',)                                     
    search_fields = ('title',)                                  
    ordering = ('-date',)                                       

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'date')
        }),
        ('Files', {
            'fields': ('pdf_file', 'cover_image')
        }),
    )
