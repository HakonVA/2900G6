from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .models import Food, Pantry
from .forms import PantryCreateForm

from django.views.generic import (
    View,
    ListView,
    CreateView,
    DeleteView,
)

class PantryIndexView(LoginRequiredMixin, View):
    model = Pantry
    login_url = 'login'
    http_method_names = ['get', 'post', 'delete']
    
    
    template_name = "pages/ingredients.html"
    context = None
    # context_object_name = None
    # queryset = None

    def get(self, request, *args, **kwargs):
        object_list = self.model.objects.filter(user=self.request.user)

        self.context = {
            'food_list': object_list,
        }
        
        return render(request, template_name=self.template_name, context=self.context)

    def post(self, request, *args, **kwargs):
        form = PantryCreateForm(request.POST or None)

        if form.is_valid():
            fd_item = form.cleaned_data.get("name").lower()
            queryset = Food.objects.filter(scientific_name=fd_item)

            if queryset.count() != 0:
                model_instance = form.save(commit=False)
                model_instance.user = self.request.user
                model_instance.name = fd_item
                model_instance.save()

        return redirect("pantry-home")

    def delete(self, request, *args, **kwargs):
        pass

pantry_index_view = PantryIndexView.as_view()

class PantryListView(LoginRequiredMixin, ListView):
    model = Pantry
    login_url = 'login'
    template_name = "ingredients/pantry_list_detail.html"
    context_object_name = "food_list"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

pantry_list_view = PantryListView.as_view()

class PantryCreateView(LoginRequiredMixin, CreateView):
    model = Pantry
    login_url = 'login'
    template_name = "pages/ingredients.html"
    success_url = "/ingredients/"
    form_class = PantryCreateForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PantryCreateView, self).form_valid(form)

pantry_create_view = PantryCreateView.as_view()

class PantryDeleteView(LoginRequiredMixin, DeleteView):
    pass

pantry_create_view = PantryDeleteView.as_view()

def pantry_DeleteAll_view(request):
    try:
        Pantry.objects.filter(user=request.user).delete()
    except:
        print("Error: ingredient_deleteAll_view")
    return redirect("pantry-home")