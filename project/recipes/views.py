from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
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
