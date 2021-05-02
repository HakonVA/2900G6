from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .models import ShoppingList

from django.views.generic import (
    ListView,
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
        print(context)
        return context

shopping_list_view = ShoppingListView.as_view()