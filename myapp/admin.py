from django.contrib import admin
from .models import thumb

# Register your models here.
@admin.register(thumb)
class ThumbAdmin(admin.ModelAdmin):
	list_display=['id','url','rating','img_url']
