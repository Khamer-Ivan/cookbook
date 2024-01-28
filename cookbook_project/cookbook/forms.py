from django import forms
from .models import Product, Recipe


class AddProductToRecipeForm(forms.Form):
    recipe = forms.ModelChoiceField(queryset=Recipe.objects.all(), label='Recipe')
    product = forms.ModelChoiceField(queryset=Product.objects.all(), label='Product')
    weight = forms.IntegerField(label='Weight (grams)')


class CookRecipeForm(forms.Form):
    recipe_id = forms.IntegerField()


class ShowRecipesWithoutProductForm(forms.Form):
    product_id = forms.IntegerField()
