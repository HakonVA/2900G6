from project.pantrys.models import UserIngredient
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from project.shoppinglists.models import Shopping
from .models import Food, Ingredient, Recipe
from django.views.generic import (
    ListView,
    DetailView,
)

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    login_url = 'login'
    template_name = "recipes/recipes_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

recipe_detail_view = RecipeDetailView.as_view()

class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    login_url = 'login'
    template_name = "recipes/recipes_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

recipe_list_view = RecipeListView.as_view()

@login_required(login_url='login')
def recipe_to_shopping_list(request, pk=0):
    recipe = Recipe.objects.get(pk=pk)
    for i in recipe.ingredients.all():

        pantry_ingredient = UserIngredient.objects.filter(food=i.food, user=request.user.id)
        pantry_amount = 0
        if pantry_ingredient:
            pantry_amount = pantry_ingredient.first().amount

        # If user does not already have enough of the ingredient, add it
        if pantry_amount < i.amount:
            obj, created = Shopping.objects.get_or_create(
                name=i.food.name,
                user=User.objects.get(pk=request.user.id)
            )

            # Only add the difference to shopping list
            if obj.amount + pantry_amount < i.amount:
                obj.amount = i.amount - pantry_amount

            obj.unit = i.unit 
            obj.save()

    return redirect("shopping:list")