from django.contrib import admin
from .models import addimg,addimg1
# Register your models here.
@admin.register(addimg)
class addimg(admin.ModelAdmin):
    list_display=['im']

@admin.register(addimg1)
class addimg(admin.ModelAdmin):
    list_display=['im','is_pri']