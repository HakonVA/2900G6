from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.http import Http404

from django.views.generic import (
    View,
    ListView,
    CreateView,
)

from .models import Food

from .forms import FoodCreateForm

class IngredientIndexView(LoginRequiredMixin, View):
    template_name = "pages/ingredients.html"
    login_url = 'login'
    

    def get(self, request, *args, **kwargs):
        obj = Food.objects.all()
        print(obj)
        return render(request, self.template_name, {"objects": obj})

    def post(self, request, *args, **kwargs):
        form = FoodCreateForm(request.POST or None)

        if form.is_valid():
            food_name = form.cleaned_data.get("scientific_name")
            Food.objects.create(scientific_name=food_name)

        return redirect("ingredients-home")

ingredient_index_view = IngredientIndexView.as_view()


class IngredientListView(LoginRequiredMixin, ListView):
    model = Food
    login_url = 'login'
    template_name = "pages/ingredients.html"

    def get_queryset(self):
        return Food.objects.filter(user_id=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        print(context)
        
        return context


class IngredientCreateView(LoginRequiredMixin, CreateView):
    model = Food
    login_url = 'login'
    template_name = "pages/ingredients.html"
    form_class = FoodCreateForm

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        print(form.cleaned_data)
        print(self.request.user)
        return super().form_valid()


def ingredient_deleteAll_view(request):
    try:
        Food.objects.all().delete()
    except:
        print("Error: ingredient_deleteAll_view")
    return redirect("ingredients-home")


# def ingredient_index_view(request):
#     """[summary]

#     Args:
#         request ([type]): [description]

#     Raises:
#         Http404: [description]

#     Returns:
#         [type]: [description]
#     """
    
#     form = None
#     obj = None

#     try:
#         obj = Food.objects.all()

#         form = FoodCreateForm(request.POST or None)
#         if form.is_valid():
#             food_name = form.cleaned_data.get("scientific_name")
#             Food.objects.create(scientific_name=food_name)

#     except obj.DoesNotExist:
#         raise Http404

#     return render(request, "pages/ingredients.html", {"objects": obj, "form": form})