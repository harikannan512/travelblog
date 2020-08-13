from django.contrib import admin
from .models import Countries, CountryPage


class CountryPageAdmin(admin.ModelAdmin):
    fields = ['c_name', 'title', 'content', 'pub_date']


admin.site.register(CountryPage, CountryPageAdmin)
admin.site.register(Countries)
