from django.shortcuts import render
from .models import UserIngredient
from project.recipes.models import Recipe

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
)


class UserIngredientListView(LoginRequiredMixin, ListView):
    model = UserIngredient
    login_url = 'login'
    template_name = "pantrys/pantrys_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        ingredient_list = context['object_list']
        recipe_list = Recipe.objects.all()

        user_food_id = [obj.food.id for obj in ingredient_list]
        print(user_food_id)

        recipe_food_id = []
        for recipe in recipe_list:
            for obj in recipe.ingredients.all():
                recipe_food_id.append(obj.food.id)
    
        print(recipe_food_id)

        print()
        print(Recipe.objects.filter(ingredients__food_id__in=user_food_id))
        print()

        context['recipes_list'] = Recipe.objects.filter(ingredients__food_id__in=user_food_id)
        print(context)
        return context

user_ingredient_list_view = UserIngredientListView.as_view()