from django.shortcuts import render
from django.urls import reverse_lazy
from .models import UserIngredient
from project.recipes.models import Recipe

from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import PantryCreateForm

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

class UserIngredientListView(LoginRequiredMixin, ListView):
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
        context['recipes_list'] = Recipe.objects.filter(ingredients__food_id__in=user_food_id)
        return context

user_ingredient_list_view = UserIngredientListView.as_view()

class UserIngredientCreateView(LoginRequiredMixin, CreateView):
    model = UserIngredient
    form_class = PantryCreateForm
    login_url = 'login'
    template_name = "pantrys/pantrys_create.html"
    success_url = reverse_lazy('pantrys:list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

user_ingredient_create_view = UserIngredientCreateView.as_view()

class UserIngredientUpdateView(LoginRequiredMixin, UpdateView):
    model = UserIngredient
    form_class = PantryCreateForm
    login_url = 'login'
    template_name = "pantrys/pantrys_update.html"
    success_url = reverse_lazy('pantrys:list')

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
    template_name = "pantrys/pantrys_delete.html"
    success_url = reverse_lazy('pantrys:list')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

user_ingredient_delete_view = UserIngredientDeleteView.as_view()