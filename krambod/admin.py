from django.contrib import admin
from krambod.models import Article, Information, Photo, PhotoTag

# Register your models here.

class PhotoAdmin(admin.ModelAdmin):    
    list_display = ('admin_image', 'tag_string')

admin.site.register(Article)
admin.site.register(Information)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(PhotoTag)
