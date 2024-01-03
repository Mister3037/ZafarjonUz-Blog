from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(HomePostNews)
class HomePostAdmin(admin.ModelAdmin):
    list_display = ['id', 'sarlavha', 'yaratilgan_sana' ]
    prepopulated_fields = {"slug": ("sarlavha",)}

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ['id', 'sarlavha']

