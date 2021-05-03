from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import ShoppingList, Shopping

from .forms import CreateForm

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

class ShoppingListView(LoginRequiredMixin, ListView):
    model = ShoppingList
    login_url = 'login'
    template_name = "shoppinglists/base.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        return context

shopping_list_view = ShoppingListView.as_view()

class ShoppingtestListView(LoginRequiredMixin, ListView):
    model = Shopping
    login_url = 'login'
    template_name = "shoppinglists/basetest.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user).order_by('checked')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context) 
        return context

shopping_test_list_view = ShoppingtestListView.as_view()

class ShoppingtestCreateView(LoginRequiredMixin, CreateView):
    model = Shopping
    form_class = CreateForm
    login_url = 'login'
    template_name = "shoppinglists/create_view.html"
    success_url = reverse_lazy('shopping:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

shopping_test_create_view = ShoppingtestCreateView.as_view()


class ShoppingtestUpdateView(LoginRequiredMixin, UpdateView):
    model = Shopping
    form_class = CreateForm
    login_url = 'login'
    template_name = "shoppinglists/update_view.html"
    success_url = reverse_lazy('shopping:list')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

shopping_test_update_view = ShoppingtestUpdateView.as_view()


class ShoppingtestDeleteView(LoginRequiredMixin, DeleteView):
    model = Shopping
    login_url = 'login'
    template_name = "shoppinglists/delete_view.html"
    success_url = reverse_lazy('shopping:list')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

shopping_test_delete_view = ShoppingtestDeleteView.as_view()