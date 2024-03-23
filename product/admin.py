from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields   = ('id', 'nameAr', 'nameEn')
    list_display    = ('id', 'nameAr', 'nameEn')
admin.site.register(Product, ProductAdmin)

class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields   = ('id', 'name')
    list_display    = ('id', 'name')
admin.site.register(Category, CategoryAdmin)

class Prices4sizesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields   =   ('id',)
    list_display    =   ('id',)
admin.site.register(Prices4sizes, Prices4sizesAdmin)