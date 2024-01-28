from django.contrib import admin
from .models import Product, Recipe, RecipeProduct


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


class RecipeAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


class RecipeProductAdmin(admin.ModelAdmin):
    list_display = ["recipe", "product"]
    search_fields = ["recipe"]


admin.site.register(Product, ProductAdmin)
admin.site.register(Recipe)
admin.site.register(RecipeProduct)
