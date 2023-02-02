from django.contrib import admin
from .models import *


@admin.register(Banners)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('alt_text','image_tag')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title','image_tag')


@admin.register(Pages)
class PagesAdmin(admin.ModelAdmin):
    list_display = ['title','detail']

@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ['quest','ans']

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ['full_name','email','detail','send_time']

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title','image_tag')

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('alt_text','image_tag')
