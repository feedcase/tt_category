from django.contrib import admin
from category_api.models import *


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent']


@admin.register(Siblings)
class SiblingsAdmin(admin.ModelAdmin):
    list_display = ['parent_id', 'siblings']
