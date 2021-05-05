from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import ShoppingForm
from django.contrib.auth.models import User
from .models import Shopping
from project.pantrys.models import UserIngredient
from project.recipes.models import Food

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

class ShoppingListView(LoginRequiredMixin, ListView):
    model = Shopping
    login_url = 'login'
    template_name = "shoppinglists/base.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user).order_by('checked')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

shopping_list_view = ShoppingListView.as_view()

class ShoppingCreateView(LoginRequiredMixin, CreateView):
    model = Shopping
    form_class = ShoppingForm
    login_url = 'login'
    template_name = "shoppinglists/create_form.html"
    success_url = reverse_lazy('shopping:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        print(form)
        return super().form_valid(form)

shopping_create_view = ShoppingCreateView.as_view()

class ShoppingUpdateView(LoginRequiredMixin, UpdateView):
    model = Shopping
    form_class = ShoppingForm
    login_url = 'login'
    template_name = "shoppinglists/update_form.html"
    success_url = reverse_lazy('shopping:list')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

shopping_update_view = ShoppingUpdateView.as_view()

class ShoppingDeleteView(LoginRequiredMixin, DeleteView):
    model = Shopping
    login_url = 'login'
    template_name = "shoppinglists/delete_form.html"
    success_url = reverse_lazy('shopping:list')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

shopping_delete_view = ShoppingDeleteView.as_view()

@login_required(login_url='login')
def shopping_checkout(request):
    shopping_list = Shopping.objects.filter(user=request.user)

    # Check shopping list is empty 
    if shopping_list.exists():
        food = Food.objects.all()
        ingredients = shopping_list.filter(name__in=food.values('name'))

        # Check if allowed ingredients exists
        if ingredients.exists():
            for i in ingredients:
                obj, created = UserIngredient.objects.get_or_create(
                    food=Food.objects.filter(name=i.name).get(),
                    user=User.objects.get(pk=request.user.id),
                )

                obj.amount += i.amount
                # TODO: Should have a unit check safe
                obj.unit = i.unit           
                # Save object changes                
                obj.save()

    # Delete users shopping list 
    shopping_list.delete()
    return redirect("pantrys:index")