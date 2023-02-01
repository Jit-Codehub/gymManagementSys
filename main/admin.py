from django.contrib import admin
from .models import *


@admin.register(Banners)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('alt_text','image_tag')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title','image_tag')
