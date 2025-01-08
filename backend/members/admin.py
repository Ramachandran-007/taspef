from django.contrib import admin

# Register your models here.
from .models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'subscription','joining_date', 'phone') 
    search_fields = ('name', 'designation') 
    list_filter = ('designation', 'joining_date')
