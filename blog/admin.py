from django.contrib import admin
from .models import Blog

# Register your models here.


@admin.register(Blog)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'publication_sign')
    list_filter = ('title',)
    search_fields = ('title', 'content',)