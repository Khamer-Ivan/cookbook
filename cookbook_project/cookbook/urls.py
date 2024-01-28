from django.urls import path
from .views import add_product_to_recipe, cook_recipe, show_recipes_without_product, home, go_to_admin, get_recipes_data
from django.contrib import admin

urlpatterns = [
	path('admin/', admin.site.urls, name='admin'),
	path('go-to-admin/', go_to_admin, name='go_to_admin'),
	path('', home, name='home'),
	path('add_product_to_recipe/', add_product_to_recipe, name='add_product_to_recipe'),
	path('cook_recipe/', cook_recipe, name='cook_recipe'),
	path('show_recipes_without_product/', show_recipes_without_product, name='show_recipes_without_product'),
	path('get_recipes_data/<int:product_id>/', get_recipes_data, name='get_recipes_data')
]
