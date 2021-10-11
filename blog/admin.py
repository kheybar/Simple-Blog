from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'writer', 'slug']

admin.site.register(Article, ArticleAdmin)