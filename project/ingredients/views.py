from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.http import Http404

from django.views.generic import (
    View,
    ListView,
    CreateView,
    DeleteView,
)

from .models import (
    Food,
    User_Food,
)

from .forms import (
    User_FoodCreateForm,
    FoodCreateForm,
)

class User_FoodListView(LoginRequiredMixin, ListView):
    model = User_Food
    login_url = 'login'
    template_name = "pages/ingredients.html"
    context_object_name = "food_list"

    def get_queryset(self):
        queryset = super().get_queryset()
        print(queryset)
        return queryset.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["food_list"] = [i.fd_id for i in self.object_list]

        return context

user_food_list_view = User_FoodListView.as_view()

class IngredientCreateView(LoginRequiredMixin, CreateView):
    model = User_Food
    login_url = 'login'
    template_name = "pages/ingredients.html"
    form_class = User_FoodCreateForm

    def form_valid(self, form):
        print("ok")
        print(form.cleaned_data)
        print(self.request.user)
        return super().form_valid()

class IngredientDeleteView(LoginRequiredMixin, DeleteView):
    pass


def ingredient_deleteAll_view(request):
    try:
        Food.objects.all().delete()
    except:
        print("Error: ingredient_deleteAll_view")
    return redirect("ingredients-home")

# class IngredientIndexView(LoginRequiredMixin, View):
#     template_name = "pages/ingredients.html"
#     login_url = 'login'
    

#     def get(self, request, *args, **kwargs):
#         obj = Food.objects.all()
#         print(obj)
#         return render(request, self.template_name, {"objects": obj})

#     def post(self, request, *args, **kwargs):
#         form = FoodCreateForm(request.POST or None)

#         if form.is_valid():
#             food_name = form.cleaned_data.get("scientific_name")
#             Food.objects.create(scientific_name=food_name)

#         return redirect("ingredients-home")

# ingredient_index_view = IngredientIndexView.as_view()

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