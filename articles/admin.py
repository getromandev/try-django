from django.contrib import admin

# Register your models here.
from .models import Article

class ArtcielAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    
admin.site.register(Article, ArtcielAdmin)
