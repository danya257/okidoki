from django.contrib import admin
from .models import *



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'range']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'available', 'range']
    list_filter = ['available', 'range']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)


class CatModAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(CatMod, CatModAdmin)


class ModificatorsAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', ]
    list_filter = ['available', ]
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Modificators, ModificatorsAdmin)
