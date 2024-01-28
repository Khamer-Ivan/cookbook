from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Product, Recipe, RecipeProduct
from .forms import AddProductToRecipeForm, CookRecipeForm, ShowRecipesWithoutProductForm
from django.http import JsonResponse


def home(request):

	"""Инициализация домашней страницы"""

	return render(request, 'home.html')


def go_to_admin(request):

	"""Админ панель"""

	return redirect('admin:index')


def add_product_to_recipe(request):

	"""Добавление продукта в рецепт с указанием веса в граммах"""

	if request.method == 'POST':
		form = AddProductToRecipeForm(request.POST)
		if form.is_valid():
			recipe = form.cleaned_data['recipe']
			product = form.cleaned_data['product']
			weight = form.cleaned_data['weight']

			print(f"Weight received: {weight}")

			if weight is not None and weight >= 0:
				recipe_product = RecipeProduct.objects.filter(recipe=recipe, product=product).first()

				if not recipe_product:
					recipe_product = RecipeProduct(recipe=recipe, product=product, weight=weight)
					recipe_product.save()
				else:
					recipe_product.weight = weight
					recipe_product.save()

				return redirect('add_product_to_recipe')
			else:
				return HttpResponse("Weight should be a non-negative number.")
	else:
		form = AddProductToRecipeForm()

	return render(request, 'add_product_to_recipe.html', {'form': form})


def cook_recipe(request):

	"""
	Приготовление блюда с увеличением
	счётчика использования продуктов
	"""

	if request.method == 'POST':
		recipe_id = request.POST.get('recipe_id')
		recipe = get_object_or_404(Recipe, pk=recipe_id)

		for recipe_product in recipe.recipeproduct_set.all():
			product = recipe_product.product
			product.times_used_in_recipe += 1
			product.save()

		return redirect('cook_recipe')

	recipes = Recipe.objects.all()
	return render(request, 'cook_recipe.html', {'recipes': recipes})


def show_recipes_without_product(request):

	"""Просмотр рецептов без какого-либо продукта"""

	products = Product.objects.all()
	return render(request, 'show_recipes_without_product.html', {'products': products})


def get_recipes_data(request, product_id):

	"""Метод дополняющий работу show_recipes_without_product"""

	product = get_object_or_404(Product, pk=product_id)

	recipes_without_product = Recipe.objects.exclude(recipeproduct__product=product).distinct()
	recipes_with_low_quantity = Recipe.objects.filter(recipeproduct__product=product,
													  recipeproduct__weight__lt=10).distinct()

	data = {
		'product_name': product.name,
		'recipes_without_product': [{'id': recipe.id, 'name': recipe.name} for recipe in recipes_without_product],
		'recipes_with_low_quantity': [{'id': recipe.id, 'name': recipe.name} for recipe in recipes_with_low_quantity],
	}

	return JsonResponse(data)
