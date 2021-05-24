from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, request
from django.shortcuts import redirect
from django.contrib import messages

from .forms import PantryForm
from .models import UserIngredient
from project.recipes.models import Recipe, Food
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

class PantryIndexView(LoginRequiredMixin, ListView):
    model = UserIngredient
    login_url = 'login'
    template_name = "pantrys/base.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ingredient_list = context['object_list']
        user_food_id = [obj.food.id for obj in ingredient_list]
        user_food_id_complement = Food.objects.exclude(id__in=user_food_id)
        recipe_list = Recipe.objects.exclude(ingredients__food_id__in=user_food_id_complement)
        for recipe in recipe_list:
            for ingredient in recipe.ingredients.all():
                user_amount = UserIngredient.objects.filter(food=ingredient.food).first().amount
                if user_amount < ingredient.amount:
                    recipe_list = recipe_list.exclude(id=recipe.id)
                    break
        context["recipes_list"] = recipe_list
        return context

pantry_index_view = PantryIndexView.as_view()

class UserIngredientListView(LoginRequiredMixin, ListView):
    model = UserIngredient
    login_url = 'login'
    template_name = "pantrys/user_ingredients.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ingredient_list = context['object_list']
        user_food_id = [obj.food.id for obj in ingredient_list]
        user_food_id_complement = Food.objects.exclude(id__in=user_food_id)
        context['recipes_list'] = Recipe.objects.exclude(ingredients__food_id__in=user_food_id_complement)
        return context

user_ingredient_list_view = UserIngredientListView.as_view()

class UserIngredientCreateView(LoginRequiredMixin, CreateView):
    model = UserIngredient
    form_class = PantryForm
    login_url = 'login'
    template_name = "pantrys/create_form.html"
    success_url = reverse_lazy('pantrys:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

user_ingredient_create_view = UserIngredientCreateView.as_view()

class UserIngredientUpdateView(LoginRequiredMixin, UpdateView):
    model = UserIngredient
    form_class = PantryForm
    login_url = 'login'
    template_name = "pantrys/update_form.html"
    success_url = reverse_lazy('pantrys:index')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

user_ingredient_update_view = UserIngredientUpdateView.as_view()

class UserIngredientDeleteView(LoginRequiredMixin, DeleteView):
    model = UserIngredient
    login_url = 'login'
    template_name = "pantrys/delete_form.html"
    success_url = reverse_lazy('pantrys:ingredients')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

user_ingredient_delete_view = UserIngredientDeleteView.as_view()

@login_required(login_url='login')
def autocomplete(request):
    print("auto")
    if "term" in request.GET:
        query_res = Food.objects.filter(name__istartswith=request.GET.get("term"))
        ingredient_list = []
        for i in query_res:
            ingredient_list.append(i.name)
        
        return JsonResponse(ingredient_list, safe=False)
    
    return redirect("pantrys:ingredients")

@login_required(login_url='login')
def submitfood(request):
    if request.method == "POST":
        try:
            food_name = request.POST["food"]
            food_amount = request.POST["amount"]
            food_unit = request.POST["unit"]
            food_obj = Food.objects.filter(name=food_name).first()
        except:
            return redirect("pantrys:ingredients")
        
        try:
            useringredient_obj, created = UserIngredient.objects.get_or_create(
                food=food_obj, user=request.user, 
                defaults={"amount": food_amount, "unit": food_unit}
            )
        except:
            messages.error(request, 'This is not a valid food item')
            return redirect("pantrys:create")

    return redirect("pantrys:ingredients")