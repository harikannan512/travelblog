from django.contrib import admin
from .models import Continent, Article


class ArticleAdmin(admin.ModelAdmin):
    fields = ['c_name', 'title', 'content', 'pub_date', 'author']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Continent)
