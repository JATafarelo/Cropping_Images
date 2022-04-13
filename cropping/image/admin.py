from django.contrib import admin
from image_cropping.admin import ImageCroppingMixin
from .models import Image

class ImageFKAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

class ImageAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

class MyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass
